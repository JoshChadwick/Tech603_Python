import math
print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def giveFactors(num) -> list:
    factors = [i for i in range(1,num+1) if num%i==0]
    return factors

print(giveFactors(12))


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def isFactor(num1, num2):
    if num1 in giveFactors(num2) or num2 in giveFactors(num1):
        return True
    else:
        return False


print(isFactor(12,3))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
#
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
def posInAlphabet(letter):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"," "]
    return alphabet.index(letter)

print(posInAlphabet("c"))


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:
def nameCode(name):
    code = ""
    for i in [posInAlphabet(i) for i in name]:
        code += str(i)

    return code

print(nameCode("bob"))


print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def createPass(name):
    codeName = nameCode(name)
    return int(codeName) - sum([int(i) for i in codeName])

print(createPass("bob"))
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:
def isPrime(num):
    try:
        if len(giveFactors(num)) != 2:
            return False
        else:
            return True

    except TypeError:
        return "Thats not a number!"

print(isPrime(1))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:
print(isPrime("a"))

# -------------------------------------------------------------------------------------- #
print("\nQ4a\n")

