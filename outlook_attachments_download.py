import win32com.client as win32
import datetime 
import zipfile
from shutil import copyfile
from fpdf import FPDF
from PIL import Image
import requests

# Step1:
base_path = '..\\..\\working'
path_for_attachs = base_path + "\\" + 'downloaded_attachments'
zip_file_date = (datetime.date.today()+datetime.timedelta(-1)).strftime('%Y%m%d')
file_name = "XYZ_"+ zip_file_date
zip_file_name = file_name + ".zip"
mail_folder_name = 'files for mail'
mail_folder_loc = base_path + '\\'+ mail_folder_name
# Step2:
outlook_app = win32.Dispatch('Outlook.Application')
myNamespace = outlook_app.GetNamespace("MAPI")
inbox = myNamespace.GetDefaultFolder(6)
# use the folder name created in the outlook which has been done basis assinging rules
outlook_req_folder = inbox.Folders("FOLDER_NAME")
# sort the mails of rainfall folder in descending order
messages =  outlook_req_folder.Items
messages.Sort("[ReceivedTime]", True)
# if required mail found then store it as a com object
for msg in messages:
    for atts in msg.Attachments:
        if atts.FileName == zip_file_name:
            req_msg = msg
            print("E-mail with required attachment found!")
            break
        else:
            req_msg = None      
    if type(req_msg) == win32.CDispatch:
        break   
# After finding required e-mail download attachments
if type(req_msg) == win32.CDispatch:
    for attachment in req_msg.Attachments:
        attachment.SaveAsFile(path_for_attachs +'\\'+ str(attachment))
    pwd = b'cafeldc'    
    with zipfile.ZipFile(path_for_attachs+"\\"+zip_file_name) as zf:
        zf.extractall(base_path+"\\"+ file_name,
                      pwd= b'password')

# Step3
xls_file_1 = 'first_excel.xls'
xls_file_2 = 'second_excel.xls'
xls_file_2_pre = 'second_excel_previous.xls'

copyfile(base_path + '\\' + xls_file_2, base_path + '\\'+xls_file_2_pre)
copyfile(base_path+"\\"+file_name+"\\"+xls_file_2, base_path+"\\"+xls_file_2)        
copyfile(base_path+"\\"+file_name+"\\"+xls_file_1, base_path+"\\"+xls_file_1)
              
# download the photos from website
url1 = "https://www.google.co.in/imghp?hl=en"
url2 = "https://www.google.co.in/imghp?hl=en"
url3 = "https://www.google.co.in/imghp?hl=en"

img_url = [url, url2, url3]
img_name = ["googleimg1", "googleimg2", "ecmwf_00Z]
#dowload image
for i in range(0, len(img_url)):
    url_content = requests.get(img_url[i])
    with open(base_path + '\\'+ mail_folder_name + '\\'+ img_name[i], 'wb') as img:
        img.write(url_content.content)

#As the dowloaded noaa_00z & ecmwf_00z is not directlly collable in the FPDF (reason
# seems to be GIF type so need to convert to RGB.
#reading those image through PIL package and converting them to "RGB" and saving
# as the JPEG.
if url_content.status_code == 500:
    img_name = img_name[0:2]        
for i in range(0,len(img_name)):
    temp_loc = mail_folder_loc + '\\' + img_name[i]
    temp_img = Image.open(temp_loc, mode = 'r')
    temp_img.convert('RGB').save(temp_loc, 'JPEG')    
        
# for gfs image 
img_list = ['img_01.jpg', 'img_02.jpg', 'img_03.jpg',
                         'img_04.jpg', 'img_05.jpg', 'img_06.jpg']
for img in img_list:
    copyfile(path_for_attachs+'\\'+img, 
             base_path+'\\'+file_name+'\\'+img)   
    

pdf_obj = FPDF() 
pdf_obj.add_page() 
pdf_obj.set_font('Times', '', 11)
# set text color to red
pdf_obj.set_text_color(0,0,250) 
pdf_obj.cell(w=0, h=5, txt='Image: Title', ln = 1)
x = [10,100,10,100,10,100]
y = [15, 15, 100, 100, 190, 190]
      
for i in range(0, len(img_list)):    
    pdf_obj.image(base_path+'\\'+file_name+'\\'+img_list[i],
                  x = x[i], y = y[i], w=85, h = 85)

pdf_obj.add_page()
pdf_obj.cell(w=0, h=5, txt='Image : Title ', ln = 1)
for i in range(0, len(noaa_00z)):    
    pdf_obj.image(mail_folder_loc +'\\'+img_name[i],
                  w = 150, h =120)

if url_content.status_code != 500:
    pdf_obj.add_page()
    pdf_obj.cell(w=0, h=5, txt='Image3:Title', ln = 1)
    pdf_obj.image(mail_folder_loc +'\\'+ "image_name", w = 160, h =150)    

pdf_obj.output(mail_folder_loc + '\\' +
               'output_image.pdf')            
