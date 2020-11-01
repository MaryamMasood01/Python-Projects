# Name: Maryam Masood


# PROBLEM A
#==========================================
# Purpose: takes in a value for the weight of a given dog and returns a
# string stating what the dog’s bark would probably sound like.
#
# Input Parameter(s):
# sound - the weight of a given dog rounded to the nearest pound.
#
# Return Value(s):
# 'Invalid input'
# 'Yip'
# 'Ruff'
# 'Bark'
# 'Boof'
#==========================================

def sound(weight):
    if weight <= 0:
        return("Invalid Input")
    elif weight < 13:
        return("Yip")
    elif weight <= 30:
        return("Ruff")
    elif weight <= 70:
        return("Bark")
    else:
        return("Boof")
    

# PROBLEM B
#==========================================
# Purpose: Requests a user to make a choice with possible options presented by the function.
#
# Input Parameter(s):
# text - a string representing the prompt for a choice in a text adventure game
# option1 - strings representing the first option
# option2 - strings representing the second option
# option3 - strings representing the third option

# Return Value(s):
# '1'
# '2'
# '3'
#==========================================

##### choice("text", "option1", "option2", "option3")

def choice(text, option1, option2, option3):
    print(text)
    print("1.", option1)
    print("2.", option2)
    print("3.", option3)
    x = input("Choose 1, 2, or 3: ")
    while (x != "1") and (x != "2") and (x != "3"):
        print("Invalid option")
        x = input("Choose 1, 2, or 3: ")
    while (x == "1") or (x == "2") or (x == "3"):
        if x == "1":
            return("1")
        elif x == "2":
            return("2")
        else:
            return("3")



# PROBLEM C
#==========================================
# Purpose: Gives the user a sequence of choices and requests that they give an answer corresponding
# to the answers given by the prompt. The series of given answers leads to one of several possible endings.
#
# Input Parameter(s): None
#
# Return Value(s): The end value from running the state1() function
#==========================================

def adventure():
    return(state1())


# State 1
#==========================================
# Purpose: Calles the choice(text, option1, option2, option3) function and either returns a boolean statement
# (True/False) or calls on another "state" function.
#
# Input Parameter(s): None
#
# Return Value(s):
# False
# The end value from running the state2() function
# The end value from running the state3() function
#==========================================
def state1():
    x = choice("Between all your classes you have +20 assignments to do in a time period of {1} week. What do you do?", "Cry.", "Procrastinate.", "Get started.")
    if x == "1":
        return(False)
    elif x == "2":
        return(state2())
    else:
        return(state3())

# State 2
#==========================================
# Purpose: Calles the choice(text, option1, option2, option3) function and either returns a boolean statement
# (True/False) or calls on another "state" function.
#
# Input Parameter(s): None
#
# Return Value(s):
# True
# The end value from running the state4() function
#==========================================
def state2():
    x = choice("Ok, procrastination. Honestly, same. But the longer you wait the more daunting the workload gets. It’s currently day three of the week. What do you do?", "Break the work down into sections for the days you have left and get started.", "Do a few assignments and give up.", "Push it, you still have time!")
    if x == "1":
        return(True)
    else:
        return(state4())

# State 3
#==========================================
# Purpose: Calles the choice(text, option1, option2, option3) function and either returns a boolean statement
# (True/False) or calls on another "state" function.
#
# Input Parameter(s): None
#
# Return Value(s):
# False
# The end value from running the state4() function
# The end value from running the state5() function
#==========================================
def state3():
    x = choice("Good job! You decided to get started. Pat yourself on the back. You have sat down at your desk and are ready to begin. How do you proceed?", "Try to do everything at once and burn out.", "Do a few assignments and forget about it.", "Break the work down into sections for the days you have left and get started.")
    if x == "1":
        return(False)
    elif x == "2":
        return(state4())
    else:
        return(state5())
        
# State 4
#==========================================
# Purpose: Calles the choice(text, option1, option2, option3) function and either returns a boolean statement
# (True/False) or calls on another "state" function.
#
# Input Parameter(s): None
#
# Return Value(s):
# True
# False
# The end value from running the state5() function
#==========================================
def state4():
    x = choice("Oof, it’s day five of your week. You only have two more days until everything is due. The pressure is up and the time left is constantly decreasing. What do you do?", "Make an action plan for the work you have left and get it done.", "Get serious. Break the work down into sections for the days you have left and get started.", "Have a breakdown")
    if x == "1":
        return(True)
    elif x == "2":
        return(state5())
    else:
        return(False)

# State 5
#==========================================
# Purpose: Calles the choice(text, option1, option2, option3) function and returns a boolean statement (True/False).
#
# Input Parameter(s): None
#
# Return Value(s):
# True
# False
#==========================================
def state5():
    x = choice("It’s around the afternoon of day six. There is only a little time left before everything is due at 11:55 pm. What do you do?", "Do my work t o the best of my ability and submit it by the 12 o’clock deadline.", "I mean, it’s too late at this point. Might as well just not do it.", "Submit it, I’m already done :)")
    if x == "2":
        return(False)
    else:
        return(True)

    

