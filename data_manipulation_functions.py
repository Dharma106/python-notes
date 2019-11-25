#import openpyxl as xlsx
import pandas as pd
import numpy as np
import sys
import datetime
import win32com.client as win32

#######################################################################
#%%
# Define a function to take xls file and dictionary object to compile data of each 
# sheet into one dataframe object.
def many_to_one_sheet(excel_file = None , mapping_dict = None):
    """
    Take a excel file and a dictonary object to compile data from each  
    worksheet and make one dataframe object with only values of dictonary.
    """
    arg_list_name = ('excel_file', 'mapping_dict')
    arg_list_value = np.array((excel_file, mapping_dict))    
#    each_arg_len = np.vectorize(len)(arg_list)
    if(arg_list_value.any()== None):
        sys.exit(('Either of these', arg_list_name, 'is missing'))    
#    if(len(excel_file) == 0):
#        sys.exit('Excel path not provided')
#    if(len(mapping_dict) == 0):
#        sys.exit('Dictonary type argument is missing')    
    read_xls_file =pd.ExcelFile(excel_file)
    sheet_name = sorted(read_xls_file.sheet_names)
    df = []
    for i in range(len(sheet_name)):
        # read individual sheet data
        temp_data = read_xls_file.parse(sheet_name[i])
        # select data excluding null i.e. NaT
        temp_data = temp_data[temp_data['Data Forecast'].notnull()]
        # Add column which has value equals to sheet name
        temp_data.loc[:,"Municipal"] = np.repeat(sheet_name[i],  len(temp_data))
        # Reorder coloumns 
        temp_data = temp_data[['Municipal', 'RAIN', 'Data Forecast']]
        # Append each sheet data below the previous
        df.append(temp_data)
    # combine the list type into one dataframe
    req_data = pd.concat(df, ignore_index = True)
    req_data.columns = ['Municipal', 'Rainfall', 'Date']       
    req_data[['Region']] = req_data[['Municipal']]
    # replace the Region column with the dictionary values
    req_data["Region"].replace(mapping_dict, inplace = True)
    # filter data only having dictionary values
    final_data = req_data[req_data['Region'].isin(list(mapping_dict.values()))]
    final_data = final_data.sort_values(['Date', 'Region'])
    final_data = final_data[['Municipal', 'Region', 'Rainfall', 'Date']]
    # drop the row names from the dataframe, inplace true updates the dataframe
    final_data.reset_index(drop = True, inplace=True)  
    # convert date in the format "day-mon-year' i.e. '01-Jan-19'        
    final_data[["Date"]] = final_data.Date.dt.date
    return final_data
 
####################################################
# defined function to extract relevant data from excel file and append to database    
    
def append_database(excel_file = None , mapping_dict = None, csv_db_loc = None):
    """
    Takes an excel file and looks next day date by matching last updated 
    date in the database.
     
    """
    arg_list_name = ('excel_file', 'mapping_dict', 'csv_db_loc')
    arg_list_value = np.array((excel_file, mapping_dict, csv_db_loc))    
    #each_arg_len = np.vectorize(len)(arg_list)
    if(arg_list_value.any()== None):
        sys.exit(('Either of these', arg_list_name, 'is missing'))  
    db = pd.read_csv(csv_db_loc)
    db['Date'] = pd.to_datetime(db['Date'])
    # latest date avilability in the data base
    max_avail_date = db.Date.max()
    # data for which data has to be appendemax_avail_date = db.Date.max()d
    req_date = max_avail_date + pd.to_timedelta(1, unit='d')
    xls_data = pd.read_excel(excel_file)
    # remove first column as it is row number 
    xls_data = xls_data.drop(xls_data.columns[0], axis =1)
    # convert the date as the required date format
    xls_data.loc[0] = pd.to_datetime(xls_data.loc[0])
    # find the req_date corresponding column number
    # use pandas to_datetime and set unit equal to 'ns' to get 
    # right status of date availability
    date_match_status = req_date == pd.to_datetime(xls_data.loc[0],
                                                   unit = 'ns')
    if np.array(date_match_status).sum() == 0:
        sys.exit(('Required date', str(req_date),
                  'does not be exists in the excle file'))
        
    req_date_col_pos = pd.Index(pd.to_datetime(
            xls_data.loc[0], unit ='ns')).get_loc(req_date)
    
    temp_data = xls_data.iloc[:, [0, req_date_col_pos,
                                  req_date_col_pos+1, req_date_col_pos+2]]
    
    temp_data.columns = ["Municipal", "Min_Temp", "Max_Temp", "Rainfall"]
    temp_data = temp_data.loc[2:len(temp_data)]
    temp_data['Region'] = temp_data['Municipal']
    temp_data['Region'].replace(mapping_dict, inplace = True)
    cleaned_data = temp_data[temp_data['Region'].isin(
            list(mapping_dict.values()))]
    cleaned_data['Date'] = np.repeat(req_date, len(cleaned_data))
    cleaned_data = cleaned_data[['Municipal', 'Region', 
                                 'Rainfall', 'Date', "Min_Temp", "Max_Temp"]]
    # append the database with the updated
    final_data = db.append(cleaned_data, ignore_index = True,
                           verify_integrity=False)    
    final_data.to_csv(csv_db_loc, index = False)
    
##########################################################################################
# Function 3: calculates n_days forward or backward average from the given date 
def n_day_average(hist_db_loc, forecast_data, date, n_days = 30, 
                  avg_type_from_date = 'backward'):
    
    """
    It takes date argumnet and looks for type of average to be calculated. 
    Default for which_avg is set to 'backward'.
    If users provided 1st day of Jan 2019 and avg_type_from_date selected is
    'backward', it will calculate average of 30 days back for each year inlcuding 
    the date provided for each region.
    
    """
#    read historical data 
    read_db = pd.read_csv(hist_db_loc)
    req_cols = ['Municipal', 'Region', 'Rainfall', 'Date']
    read_db = read_db[req_cols]

#    include the future data in the database.
    combined_data = read_db.append(forecast_data)
    if avg_type_from_date == 'backward':
        combined_data = read_db
        date = pd.to_datetime(date)
    elif avg_type_from_date == 'forward':
        combined_data = combined_data
        date = pd.to_datetime(date) + pd.DateOffset(1)
        
    combined_data['Date']= pd.to_datetime(combined_data['Date'])
    unique_year = combined_data.Date.dt.year.unique()
    unique_year = unique_year[np.logical_not(np.isnan(unique_year))]
    unique_year = unique_year.astype(np.int)
    
    if date > combined_data.Date.max():
        sys.exit('Date provide is higher than the maximum date in database!')    
    
    mon = date.month
    day = date.day
#    create a list of each year date from the given date and then calculate
#    30 days back. 
#    if the date provided is of leap year then for feb month modify the last date
#    as 28 for all non-leap year        
    each_year_same_period = []    
    for i in range(0, len(unique_year)):
        if unique_year[i] %4 != 0 and mon ==2 and day ==29:
            temp_day = day-1
        else:
            temp_day = day
        each_year_same_period.append(datetime.datetime(unique_year[i],
                                                       mon, temp_day))        
#   create n_days for all year in the database.
    each_year_n_days = []
    if avg_type_from_date == 'backward':
        for x in range(0, len(each_year_same_period)):
            each_year_n_days.append([
                each_year_same_period[x] - datetime.timedelta(days =i)
                for i in range(0,n_days)]
                )
    elif avg_type_from_date == 'forward':
        for x in range(0, len(each_year_same_period)):
            each_year_n_days.append([
                    each_year_same_period[x] + datetime.timedelta(days =i)
                    for i in range(0,n_days)]
                )    
        
#    n_days from the date provided
    running_yr_date = each_year_n_days[-1]    
    running_yr_date = [datetime.datetime.strftime(item, "%Y-%m-%d") for
                       item in running_yr_date]
    running_yr_date = pd.to_datetime(running_yr_date)
#    to watch out, if the start year of the database does not have  
#    days <= n_days/3 then exclude that year from the avearge    
    date_aval_sts = pd.to_datetime(each_year_n_days[0]).year == unique_year[0]    
    if sum(np.logical_not(date_aval_sts)) >= n_days/3:
        each_year_n_days = each_year_n_days[1:-1]
    else:
        each_year_n_days = each_year_n_days[:-1]            
    
    req_date_list = [datetime.datetime.strftime(item, "%Y-%m-%d") for
                     item in sum(each_year_n_days,[])]
    req_date_list = pd.to_datetime(req_date_list)
    data_for_avg = combined_data[combined_data['Date'].isin(req_date_list)]
    data_for_avg['Year'] = data_for_avg.Date.dt.year
    unique_yrs_for_avg = data_for_avg.groupby(['Municipal'])['Year'].count()/n_days
    unique_yrs_for_avg = unique_yrs_for_avg.reset_index()
#    tot_yrs_for_avg = len(req_date_list.year.unique())
    grouped_avged_data = data_for_avg.groupby(
            ['Municipal', 'Region'])['Rainfall'].sum()
    grouped_avged_data = grouped_avged_data.reset_index()
    grouped_avged_data['Rainfall'] = grouped_avged_data['Rainfall']/unique_yrs_for_avg['Year']
    grouped_avged_data = grouped_avged_data.sort_values(['Region'])
    grouped_avged_data.reset_index(drop = True, inplace=True)  
#    select data where Date matches with running_yr_date 
    running_yr_data_for_sum = combined_data[combined_data['Date'].isin(running_yr_date)]
#    group the filtered data by Municipal and Region and then sum the rainfall
    grouped_sumed_data = running_yr_data_for_sum.groupby(
            ['Municipal', 'Region'])['Rainfall'].sum() 
#    resetting the index to get the dataframe object
    grouped_sumed_data = grouped_sumed_data.reset_index()
    grouped_sumed_data = grouped_sumed_data.sort_values(['Region'])
    grouped_sumed_data.reset_index(drop = True, inplace=True)
    delta_data = grouped_sumed_data[['Municipal', 'Region']]
    delta_data['% change'] = ((grouped_sumed_data['Rainfall']/
              grouped_avged_data['Rainfall'])-1)
    return grouped_avged_data, grouped_sumed_data, delta_data
    
############################################################################
# define a function to generate n number of months date backward 
# from the initial date provided
def generate_n_back_dates(initial_date, n =12):
    '''
    This function take a refernce date and generates n number of dates 
    backwards
    '''
    date_list = list()
    date_list.append(initial_date)
    for i in range(1, n):
        temp_date = initial_date
        one_month_back = temp_date.replace(day =1)- datetime.timedelta(days = 1)
        req_date = one_month_back.replace(day =1)
        date_list.append(req_date)
        initial_date = req_date        
    return date_list        

   
#%%
# this function is to save the excel range as a pdf file
def save_xls_range_as_pdf(xlsx_file_loc, sheet_name,
                          cell_range, name_for_pdf, loc_to_save):
    #create a com object of excel
    xlsx_app = win32.Dispatch('Excel.Application')
#    xlsx_app.Visible = False
    #open the desired excel file location
    if len(sheet_name) != len(cell_range) != len(name_for_pdf):
        exit('Cell range list should be equal to list of sheets')
    
    wb = xlsx_app.Workbooks.Open(xlsx_file_loc)
    for i in range(0, len(sheet_name)):
        ws = wb.Worksheets[sheet_name[i]]
        ws.PageSetup.Zoom = False
        ws.PageSetup.PrintArea = cell_range[i]
        wb.WorkSheets(sheet_name[i]).Select()
        wb.ActiveSheet.ExportAsFixedFormat(0, loc_to_save + "\\" +name_for_pdf[i])
    wb.Close(True)
    
###################################################################################
def send_mail(attach_files, file_loc, mail_to, 
              mail_cc, sub_name =" ",
              mail_body = " "):
    #create a com object of outlook
    outlook_app = win32.Dispatch('outlook.Application')
#    outlook_app.Visible = False
    
    if len(mail_to) == 0 or len(mail_cc) == 0:
        sys.exit('No recipient is provided')
        
    mail = outlook_app.CreateItem(0)
    todays_date = datetime.date.today()
    mail.Subject = sub_name + ' ('+ todays_date.strftime('%d-%B-%Y') +')'
    mail.Body = mail_body
    
    mail.To = mail_to
    mail.CC = mail_cc
    for i in range(0, len(attach_files)):
        mail.Attachments.Add(file_loc +'\\' + attach_files[i])    
    mail.Send()
    print('Mail has been been sent')
    
    
    
