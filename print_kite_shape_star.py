def print_star(n):
    if n % 2 == 1:
        if n == 3:
            start_pos = 2
        else :
            start_pos = 2 + n//3     
        print_pos_array = [list(range(start_pos-i, start_pos+i+1))
                      for i in range(1, start_pos)]      
        print_pos_array.insert(0, [start_pos])        
        temp_array = print_pos_array[:-1]
        temp_array.reverse()
        print_pos_array = print_pos_array + temp_array        
        for arr in print_pos_array:
            array_len = len(arr)
            print(" "*arr[0] + "*"*array_len)
    else:
        print("number provided is even try with odd number")
