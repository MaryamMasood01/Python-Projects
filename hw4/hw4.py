# Maryam Masood

# Problem A: find_password
#==========================================
# Purpose:
#   Given an encrypted file, tries every possible four letter lowercase
#   password for that file until one works, and then returns the password.
# Input Parameter(s):
#   filename is a string representing the name of the encrypted file.
#   The file must be in the same folder as this script.
# Return Value:
#   Returns the password that successfully decrypts the given file
#==========================================

def find_password(filename):
    fp = open(filename)
    data = fp.read()

    #TODO: Try all possible four letter passwords, not just 'pwnd'
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for w in letters:
        for x in letters:
            for y in letters:
                for z in letters:
                    password = w + x + y + z
                    if decrypt(data,password):
                        return password


# Problem B: count_primes
#==========================================
# Purpose:
#   Prints out all prime numbers between low and high, inclusve, and
#   returns a count of how many there were.
# Input Parameter(s):
#   low is a positive integer 
#   high is a positive integer, which should be >= low
# Return Value:
#   Returns the number of prime numbers between low and high, inclusive
#==========================================

def count_primes(low, high):
    count = 0
    h = high + 1
    for x in range(low, h):
        z = prime_single(x)
        if z == True:
            print(x, " is prime")
            count += 1
    print(count)


# prime_single
#==========================================
# Purpose: determines whether a single integer is prime
#
# Input Parameter(s):
# x - a single positive integer
#
# Return Value(s):
# False if x is less than or equal to 1
# False if the remainder of (x / i) is zero
# True if the remainder of (x / i) is not zero
#
#==========================================

def prime_single(x):
    y = int(x ** 0.5)
    if x > 1:
        for i in range(2, (y + 1)):
            if (x % i) == 0:
                return(False)
        return(True)
    else:
        return(False)


# Problem C: population
#==========================================
# Purpose:
#   Simulates the population of smallfish, middlefish, and bigfish over time
# Input Parameter(s):
#   small is an integer, the initial number of smallfish in the lake
#   middle is an integer, the initial number of middlefish in the lake
#   big is an integer, the initial number of bigfish in the lake
# Return Value:
#   Returns the number of weeks required for one of the populations to
#   fall below 10, or 100 if the populations are all still >= 10 after
#   100 weeks
#==========================================

def population(small, middle, big):
    weeks = 0
    while (small >= 10) and (middle >= 10) and (big >= 10) and (weeks < 100):
        s = small
        m = middle
        b = big
        small = (s * 1.1) - (0.0002 * s * m)  
        middle = (m * 0.95) - (0.00025 * m * b) + ((0.0002 * s * m) * 0.5)
        big = (b * 0.9) + ((0.00025 * m * b) * 0.8)
        weeks += 1
        print("Week", weeks, "- Small:", int(small), " Middle:", int(middle), " Big:", int(big))
    if weeks <= 100:
        return(weeks)
    else:
        return(100)



#DO NOT EDIT ANYTHING BELOW THIS LINE
#Below are helper functions used for decrypting the text files.
#You don't have to understand how any of these work.

# decrypt
#==========================================
# Purpose:
#   Check whether the password is correct for a given encrypted
#   file, and print out the decrypted contents if it is.
# Input Parameter(s):
#   data is a string, representing the contents of an encrypted file.
#   password is a four letter lowercase string, representing the password
#   used to encrypt/decrypt the file contents.
# Return Value:
#   Returns True if the password is correct and the file contents
#   were printed.  Returns False and prints nothing otherwise.
#==========================================
def decrypt(data, password):
    data = data.split('\n')
    if encode(password) == int(data[0]):
        print(vigenere(data[1],password))
        return True
    return False

# encode
#==========================================
# Purpose:
#   Turn a password into a ~9 digit number
# Input Parameter(s):
#   key is a four letter string representing a password
# Return Value:
#   Returns a number between 0 and 547120140, using modular exponentiation
#   to make it difficult to reverse engineer the password from the number.
#==========================================
def encode(key):
    total = 0
    for ltr in key:
        total += ord(ltr)
        total *= 123
    return pow(total,2011,547120141)

# vigenere
#==========================================
# Purpose:
#   Decipher a message using the Vigenere cipher
# Input Parameter(s):
#   msg a string, representing the encrypted message
#   key is a four letter string, representing the cipher key
# Return Value:
#   Returns a string representing the deciphered text
#==========================================
def vigenere(msg,key):
    i = 0
    out_msg = ''
    for ltr in msg:
        out_msg += chr((ord(ltr)-ord(key[i]))%28 +97)
        i = (i+1)%len(key)
    return out_msg.replace('{',' ').replace('|','.')


