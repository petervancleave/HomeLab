# Van Cleave_PVC_HW9

# Program 1 - Assignment Header - Function that returns a string
def printAssignHdr():
    border = "-" * 50
    print(border)
    print(buildHdrMsg())
    print(border)

def buildHdrMsg():
    name = "Peter Van Cleave"
    date = "11/13/24"
    course = "Structured Problem Solving"
    course_section = "CIS-2110-001"
    assignment = "HW #9 Functions in Python"

    msg = (
        date + "                          " + name + "\n" +
        course_section + "            " + course + "\n" +
        "Assignment: " + assignment 
    )
    return msg

# Program 2 - Function which prints a string that is passed from another function
def printPrgmHdr():
    description = "Program 2: Function which prints a string that is passed from another function."
    inputs = "Input: N/A"
    outputs = "Output: Description of program including inputs and outputs"

    print3Args(description, inputs, outputs)

def print3Args(description, inputs, outputs):
    border = "#" * 80

    print(border)
    print(description)
    print(inputs)
    print(outputs)
    print(border)

# Program 3 - Sum, Product, and Average Functions
def mySum(num1, num2):
    return num1 + num2

def myProduct(num1, num2):
    return num1 * num2

def myAvg(sum, count):
    if count == 0:
        return 0  
    return sum // count  

def printNums(count, totalSum, totalProduct, totalAvg):
    print(f"The sum is: {totalSum} and is", end=" ")
    if totalSum == 0:
        print("zero.")
    elif totalSum % 2 == 0:
        print("even.")
    else:
        print("odd.")
    
    print(f"The product is: {totalProduct} and is", end=" ")
    if totalProduct == 0:
        print("zero.")
    elif totalProduct % 2 == 0:
        print("even.")
    else:
        print("odd.")
    
    print(f"The average is: {totalAvg} and is", end=" ")
    if totalAvg == 0:
        print("zero.")
    elif totalAvg % 2 == 0:
        print("even.")
    else:
        print("odd.")

def numberCont():
    totalSum = 0
    totalProduct = 1  
    count = 0
    
    print("A running total is being tracked, enter a number to see the total sum, total product, and total average of the numbers")
    
    while True:
        user_input = input("Enter a number or 'stop': ")
        
        if user_input.lower() == 'stop':
            break
        
        if user_input.isdigit() or (user_input.startswith('-') and user_input[1:].isdigit()):
            num = int(user_input)
            
            totalSum = mySum(totalSum, num)
            totalProduct = myProduct(totalProduct, num)
            count += 1
            
            totalAvg = myAvg(totalSum, count)
            
            printNums(count, totalSum, totalProduct, totalAvg)
        else:
            print("Error")

def runProgram1():
    numberCont()

# Program 4 - Random Functions
import random  

def randomRange():
    lower = int(input("Enter the low number: "))
    upper = int(input("Enter the high number: "))
    
    while True:
        rand_num = random.randrange(lower, upper+1)
        print(f"Your random number {rand_num} is pulled from the range {lower} to {upper}")
        
        stop = input("Type 'stop' to stop the program: ").lower()
        if stop == 'stop':
            break  

def randomChoice():
    user_string = input("Enter a string: ")
    
    while True:
        rand_letter = random.choice(user_string)  
        print(f"Your random letter '{rand_letter}' is pulled from the string '{user_string}'.")
        
        stop = input("Type 'stop' to stop the program: ").lower()
        if stop == 'stop':
            break  

def program4():
    printPrgmHdr()
    randomRange()  
    randomChoice()  

# Main 
def main():
    printAssignHdr()       # Program 1
    printPrgmHdr()         # Program 2
    runProgram1()          # Program 3
    program4()             # Program 4

if __name__ == "__main__":
    main()
