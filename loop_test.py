flag = True
string_to_print = ""
while(flag == True):
    pos_integer = input("Enter a positive integer: ")
    
    try:
        val = int(pos_integer)
        if val < 0:
            print("Invald Entry")
            break
    except ValueError:
        print("Invalid Entry")
        break
    
    digit_string = str(pos_integer)
    digit_map = map(int, digit_string)
    digit_list = list(digit_map)

    for digit in digit_list:
        
        if digit == 1:
            string_to_print += "One "
        elif digit == 2:
            string_to_print += "Two "
        elif digit == 3:
            string_to_print += "Three "
        elif digit == 4:
            string_to_print += "Four "
        elif digit == 5:
            string_to_print += "Five "
        elif digit == 6:
            string_to_print += "Six "
        elif digit == 7:
            string_to_print += "Seven "
        elif digit == 8:
            string_to_print += "Eight "
        elif digit == 9:
            string_to_print += "Nine "
        elif digit == 0:
            string_to_print += "Zero "
            flag = False
            

    print(string_to_print)

    string_to_print = ""
