# Name: Maryam Masood
# x500: masoo013

# PROBLEM A

# first_words(fname)
#==========================================
# Purpose: produces a list of the first word in every sentence in that file, in order, including duplicates.
#
# Input Parameter(s):
# fname - a string representing the name of a file
#
# Return Value(s): a list of the first word in every sentence in that file, in order, including duplicates.
#==========================================

def first_words(fname):
    try:
        with open(fname, 'r') as newfile:
            list_of_first_words = []
            string_of_text = newfile.read()
            list_of_lines = string_of_text.split('\n')
            for line_index in range(len(list_of_lines)):
                list_of_words = list_of_lines[line_index].split()
                if list_of_words != []:
                    list_of_first_words.append(list_of_words[0])
            return list_of_first_words

    except FileNotFoundError:
        print("File not found.")



# next_words(fname)
#==========================================
# Purpose: produces a dictionary where the keys are each distinct word in the file (case matters), and the value for any given key is a list of
# every word that follows that key anywhere in the file, in order, including duplicates
#
# Input Parameter(s):
# fname - a string representing the name of a file
#
# Return Value(s): a dictionary where the keys are each distinct word in the file (case matters), and the value for any given key is a list of
# every word that follows that key anywhere in the file, in order, including duplicates
#==========================================

def next_words(fname):
    try:
        with open(fname, 'r') as newfile:
            string_of_text = newfile.read()
            list_of_lines = string_of_text.split('\n')
            
            final_list_of_words = []
            for line_index in range(len(list_of_lines)):
                list_of_words = list_of_lines[line_index].split()
                for i in range(len(list_of_words)):
                    final_list_of_words.append(list_of_words[i])
            
            dict_of_words = {}
            
            for i in range(len(final_list_of_words)):
                if i < len(final_list_of_words) - 1:
                    if final_list_of_words[i] != '.':
                        if final_list_of_words[i] in dict_of_words.keys():
                            dict_of_words[final_list_of_words[i]].append(final_list_of_words[i + 1])
                        else:
                            dict_of_words.update({final_list_of_words[i] : [final_list_of_words[i + 1]]})

            return dict_of_words
        

    except FileNotFoundError:
        print("File not found.")
            



# fanfic(fname)
#==========================================
# Purpose: produces 10 'sentances' that are randomly generated with the use of the "first_words(fname)" function and the "next_words(fname)" function
#
# Input Parameter(s):
# fname - a string representing the name of a file
#
# Return Value(s): None
#==========================================

import random

def fanfic(fname):
    list_of_first_words = first_words(fname)
    dict_of_following_words = next_words(fname)

    list_of_all_sentances = []
    
    for sentance in range(10):
        list_for_sentance = []
        word_1 = random.choice(list_of_first_words)
        following = word_1

        while following != '.':
            list_for_sentance.append(following)
            following = random.choice(dict_of_following_words[following])

        list_for_sentance.append('.')
        sentance_i = ' '.join(list_for_sentance)
        list_of_all_sentances.append(sentance_i)

    for i in range(len(list_of_all_sentances)):
        print(list_of_all_sentances[i])
        
        
        

# PROBLEM B
#==========================================
# Purpose: calculates the total memory in bytes (an integer) being used by txt files in a directory
#
# Input Parameter(s):
# directory - a nested dictionary representing adirectory 
#
# Return Value(s): the total memory in bytes (an integer) being used by txt files in the directory
#==========================================

def total_txt_size(directory):
    keys = list(directory.keys())
    total = 0

    for key in keys:
        val = directory[key]
        if type(val) == int:
            if key.endswith('.txt'):
                total += val

        else:
            total += total_txt_size(val)

    return total
    
            
        



