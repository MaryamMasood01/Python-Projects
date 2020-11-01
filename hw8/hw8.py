## Name: Maryam Masood
## x500: masoo013

#Part 1: get_data_list
#==========================================
# Purpose:
#   Extract the data from a CSV file as a list of rows
# Input Parameter(s):
#   fname is a string representing the name of a file
# Return Value:
#   Returns a list of every line in that file (a list of strings)
#   OR returns -1 if the file does not exist
#==========================================
def get_data_list(fname):
    try:
        with open(fname, 'r') as newfile:
            line_list = newfile.readlines()
            newfile.close()
            return line_list

    except FileNotFoundError:
        return -1



#Part 2: hw8_index
#==========================================
# Purpose:
#   Determine which column stores the grades for hw8
# Input Parameter(s):
#   row1_str is a string containing the first row of data 
#   (the column titles) in the CSV file
# Return Value:
#   Returns the index of the column labelled 'hw8 Grade' (an integer)
#   OR returns -1 if there is no column labelled 'hw8 Grade'
#==========================================
def hw8_index(row1_str):
    try:
        list_str = row1_str.split(',')
        in_val = list_str.index('hw8 Grade')
        return in_val

    except ValueError:
        return -1



#Part 3: alter_grade
#==========================================
# Purpose:
#   Change the hw8 grade in your row string to '40'
# Input Parameter(s):
#   row_str is a string containing any row of data from the CSV file
#   idx is an index for the column you want to alter
# Return Value:
#   Returns a string identical to row_str, except with the column
#   at the given index changed to '40'
#==========================================
def alter_grade(row_str,idx):
    
    list_str = row_str.split(',')
    list_str[idx] = '40'
    new_row_str = ','.join(list_str)
    return new_row_str




#Part 4: haxx
#==========================================
# Purpose:
#   Alters a gradebook CSV file so that your score on hw8 is '40'
# Input Parameter(s):
#   fname is the file name of the gradebook file
# Return Value:
#   Returns False if the file isn't open
#   Returns False if the file doesn't contain a 'hw8 Grade' column
#   Otherwise, returns True
#==========================================
def haxx(fname):

    list_of_vals = get_data_list(fname)

    if list_of_vals != -1:
        hw8_index_val = hw8_index(list_of_vals[0])

        if hw8_index_val != -1:
            FN_index_val = full_name(fname)

            if FN_index_val != -1:
                alter_str = list_of_vals[FN_index_val]
                final_val = alter_grade(alter_str, hw8_index_val)
                list_of_vals[FN_index_val] = final_val
                final_csv_vals = ''.join(list_of_vals)
                newfile = open(fname, 'w')
                newfile.write(final_csv_vals)
                newfile.close()
                return True

            else:
                return False

        else:
            return False

    else:
        return False
                            

# Helper function: full_name(fname)
#==========================================
# Purpose:
#   Determine which row stores the name "Maryam Masood" 
# Input Parameter(s):
#   fname - a string representing the name of a file
# Return Value:
#   Returns the index of the value with the name 'Maryam Masood' (an integer) in the 'Full Name' column
#   OR returns -1 if there is no value in that column labelled 'Maryam Masood'
#==========================================

def full_name(fname):

    try:
        list_vals = get_data_list(fname)
        with open(fname, 'r') as newfile:
            if list_vals != -1:
                list_str = list_vals[0].split(',')
                if 'Full Name' in list_vals[0]:
                    in_val = list_str.index('Full Name')
                    for i in range(len(list_vals)):
                        list_str_2 = list_vals[i].split(',')
                        if list_str_2[in_val] == "Maryam Masood":
                            newfile.close()
                            return i
                    newfile.close()
                    return -1

    except ValueError:
        return -1

    except FileNotFoundError:
        return -1


            
