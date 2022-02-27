even_finder = []
for odd in range(1,100,2):
    even_finder.append(odd)

odd_finder = []
for even in range(0,100,2):
    odd_finder.append(even)


def roundsf(x,y):
    import math
    return round(x,y-int(math.floor((math.log10(abs(x)))))-1)
#round numer to y significant figure


def fibonacci(x):
    y,z = 0,1

    for i in range(x):
        print(y)
        y,z = z,y+z
    return z

#display fibonaci of x range

def even(x):
    for i in range(0,x,2):
        print(i)

    return ""

#display even numbers from start to  x range

def even_range(x,y):
    for i in range(x,y,2):
        if i in even_finder:
            for z in range(x+1, y, 2):
                print(z)
            break
        else:
            print(i)

    return ""
#display even numbers from start x to stop y



def odd(x):
    for i in range(1,x,2):
        print(i)

    return ""

#display odd numbers from start to x range

def odd_range(x,y):
    for i in range(x,y,2):
        if i in odd_finder:
            for z in range(x+1, y, 2):
                print(z)
            break
        else:
            print(i)

    return ""

#display odd numbers from start x to stop y

def max_number(numbers):
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum

#return maximum value in a list

def vowel():
    return['a','i','e','o','u']

#return vowel letters

def const():
    import  string
    alphabets = list(string.ascii_letters)
    constant_restrict = ('a', 'e', 'i', 'o', 'u')
    consonant = []
    for letter in alphabets:
        if letter not in constant_restrict:
            consonant.append(letter)
    return consonant

#return consonant letter

def Laschar():
    for number in range(97,123):
        print(chr(number),':',number)
    return ""

#return lowercase letters and their char values

def Uaschar():
    for number in range(65,91):
        print(chr(number),':',number)
    return ""

#return uppercase letters and their char values







