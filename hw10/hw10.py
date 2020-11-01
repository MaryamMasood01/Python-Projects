# Name: Maryam Masood
# x500: masoo013

# PROBLEM A
#==========================================
# Purpose: a class that models a complex number in the form of x+yi
#   
# Input Parameter(s):
# self
# other
# real -  the real number component
# image - the imaginary number coefficient
# new_real - a new real number component to replace the current one
# new_imag - a new imaginary number coefficient to replace the current one
#   
# Return Value:
# __str__(self) - a string of the form "x+yi"
# get_real(self) - the real number component
# get_imag(self) - the imaginary numbe coefficient
# __add__(self, other)- a string of the form "x+yi" which equals the sum of two  complex numbers
# __mul__(self, other)- a string of the form "x+yi" which equals the product of two  complex numbers
#   
#==========================================

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return str(self.real) + ' + ' + str(self.imag) + 'i '

    def get_real(self):
        return str(self.real)
    
    def get_imag(self):
        return str(self.imag)
    
    def set_real(self, new_real):
        self.real = new_real
        
    def set_imag(self, new_imag):
        self.imag = new_imag

    def __add__(self, other):
        new_x = self.real + other.real
        new_y = self.imag + other.imag
        return Complex(new_x, new_y)

    def __mul__(self, other):
        new_x = (self.real * other.real) - (self.imag * other.imag)
        new_y = (self.real * other.imag) + (other.real * self.imag)
        return Complex(new_x, new_y) 

# __eq__(self, othe)
#==========================================
# Purpose: evaluates whether two objects are equal
#   
# Input Parameter(s):
# self 
# other - another complex object
#
# Return Value:
# True if the two objects are equal
# False if the two objects are not equal
#
#==========================================

    def __eq__(self, other):
        if self.real != other.real:
            return False
        else:
            if self.imag != other.imag:
                return False
            return True
        
# PROBLEM B

# Employee Class
#==========================================
# Purpose: takes in a string and and evaluates a person's name. job title, salary, seriority, and average anual income
#   
# Input Parameter(s):
# self
# other
# line - string of the person's name. job title, salary, seriority, and average anual income
#   
# Return Value:
# __str__(self) - a string of the person's name and job title
# net_value(self) - a float representing the net value of the person
# __lt__(self, other) - True if self.net_value() is less than other.net_value() and False if it is not
#   
#==========================================

class Employee:
    def __init__(self, line):
        list_of_vals = line.split(',')
        self.name = list_of_vals[0]
        self.position = list_of_vals[1]
        self.salary = round(float(list_of_vals[2]), 2)
        self.seniority = float(list_of_vals[3])
        self.value = round(float(list_of_vals[4]), 2)

    def __str__(self):
        return str(self.name) + ", " + str(self.position)

    def net_value(self):
        return round(float(self.value - self.salary), 2)

    def __lt__(self, other):
        if self.net_value() < other.net_value():
            return True
        return False
        

# Branch Class
#==========================================
# Purpose: a class that analyzes information about each employee in a branch and ranks the employees by least profitable to most profitable
#   
# Input Parameter(s):
# self
# other
# fname -  a sting representative of a file name
# num - the number of people to cut from the company
#   
# Return Value:
# __str__(self) - a string of the location of the branch and each person and their position in the branch
# __lt__(self, other) - True if self.profit() is less than other.profit() and False if it is not
#   
#==========================================

class Branch:
    def __init__(self, fname):
        try:
            location = ''
            upkeep = 0
            team_index = 0
            team = []
            
            with open(fname, 'r') as newfile:
                string = newfile.read()
                l_s = string.split('\n')

                location = ''
                upkeep = 0
                team_index = 0
                team = []
                

                for i in range(len(l_s)):
                    list_of_words = l_s[i].split(',')
                    

                    if 'Location' in list_of_words:
                        location = list_of_words[list_of_words.index('Location') + 1]
                        
                    elif 'Upkeep' in list_of_words:
                        upkeep = float(list_of_words[list_of_words.index('Upkeep') + 1])

                    elif 'Name' in list_of_words:
                        team_index = list_of_words.index('Name')

                    else:
                        if l_s[i] != '':
                            val = Employee(l_s[i])
                            team.append(val)

                newfile.close()
                
                
            self.location = location
            self.upkeep = upkeep
            self.team = team
            
                

        except FileNotFoundError:
            print("File not found.")


    def __str__(self):
        string = str(self.location) 

        for val in self.team:
            string += '\n' + str(val)
        
        return string
        
# profit(self)
#==========================================
# Purpose: evaluates the profit of the branch
#   
# Input Parameter(s):
# self
#   
# Return Value: a float re[presenting teh profit of the branch
#   
#==========================================

    def profit(self):
        profit = 0

        for emp in self.team:
            val = emp.net_value()
            profit += val

        return round(float(profit - self.upkeep), 2)

    def __lt__(self, other):
        if self.profit() < other.profit():
            return True
        return False

    def cut(self, num):
        x = self.team.sort()
        self.team = self.team[num:]
        
        
        
    

# Company Class
#==========================================
# Purpose: a class that analyzes information about each branch in a company and cuts employees from the least profitable branch
#   
# Input Parameter(s):
# self
# name - a string reepresenting the name of company
# branches - a list of branch objects
#   
# Return Value:
# __str__(self) - a string of the name of the company and the location of each branch and each person and their position in each branch
#   
#==========================================        
        
class Company():
    def __init__(self, name, branches):
        self.name = name
        self.branches = branches

    def __str__(self):
        string = str(self.name) 

        for val in self.branches:
            string += '\n\n' + str(val)
        
        return string

    def synergize(self):
        self.branches.sort()
        x = self.branches[0]
        x.cut(len(x.team)//2)

        
        
        
            
        
        


