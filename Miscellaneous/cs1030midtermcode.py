# Program that asks for a number. If the number is less than 5, it is written out, but if it is greater than or equal to 5, twice that number is written out.

def numIn():
    number = int(input("Enter a number: "))
    if number < 5:
        print(number)
    else:
        result = number * 2
        print(result)

numIn()