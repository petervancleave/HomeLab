# Van_Cleave_PVC_HW10

# Assignment Header
def printAssignHdr():
    border = "-" * 60
    print(border)
    print(buildHdrMsg())
    print(border)

def buildHdrMsg():
    name = "Peter Van Cleave"
    date = "11/20/24"
    course = "Structured Problem Solving"
    course_section = "CIS-2110-001"
    assignment = "HW #10 Lists and Loops in Python"

    msg = (
        date + "                          " + name + "\n" +
        course_section + "            " + course + "\n" +
        "Assignment: " + assignment 
    )
    return msg

# Program 1: List of 7 Unique Integers
def printProgram1Header():
    print("#" * 80)
    print("Program 1: List of 7 Unique integers")
    print("#" * 80)

def program1():
    numList = []
    while len(numList) < 7:
        num = int(input("Type an Integer: "))
        if num not in numList:
            numList.append(num)
        else:
            print("Try ahain.")

    print("Your list of numbers is:", numList)
    total = 0
    for num in numList:
        total += num
    print("The sum of the numbers is:", total)
    print("The average of the numbers is:", total / len(numList))



# Program 2: Counting Characters
def printProgram2Header():
    print("#" * 80)
    print("Program 2: Counting characters")
    print("#" * 80)

def program2():
    string = input("type a string: ")
    count = 0
    index = 0
    while index < len(string):
        count += 1
        index += 1
    print(f"The string is '{string}' and has this many characters: {count} .")


# Program 3: Make a New Number List
def printProgram3Header():
    print("#" * 80)
    print("Program 3: Make a new number list")
    print("#" * 80)

def program3():
    numList2 = []
    while True:
        num2 = input("Type a number or 'stop': ")
        if num2.lower() == 'stop':
            break
        numList2.append(float(num2))

    print("The numbers in the list are:", numList2)
    print("The numbers in the list in a column are:")
    for num2 in numList2:
        print("\t", num2)


# Program 4: Count the Negative Numbers in List
def printProgram4Header():
    print("#" * 80)
    print("Program 4: Count the negative numbers in the list")
    print("#" * 80)

def program4():
    numList3 = []
    while True:
        num3 = input("type a number or 'stop': ")
        if num3.lower() == 'stop':
            break
        numList3.append(float(num3))

    negativeNums = 0
    for num3 in numList3:
        if num3 < 0:
            negativeNums += 1

    print("The inputs are:", numList3)
    print(f"With {negativeNums} negative numbers entered.")


# Program 5: Delete Negative Numbers from a List
def printProgram5Header():
    print("#" * 80)
    print("Program 5: Delete negative numbers from a list")
    print("#" * 80)

def program5():
    numList4 = []
    while True:
        num4 = input("Type a number or 'stop': ")
        if num4.lower() == 'stop':
            break
        numList4.append(float(num4))

    positiveNums = []
    for num4 in numList4:
        if num4 >= 0:
            positiveNums.append(num4)

    print("The inputs are:", numList4)
    print("List of the inputs without the negative numbers:", positiveNums)


# Assignment Footer
def assignmentFooter():
    border2 = "-" * 80
    print(border2)
    print(buildFooterMsg())
    print(border2)

def buildFooterMsg():
    footerSay = "Assignment Completed: HW #10 Lists and Loops in Python"
    footerEnd = "--- End of Code ---"

    footer = (
        footerSay + "\n" +
        footerEnd 
    )

    return footer

# Main
def main():
    printAssignHdr()  
    printProgram1Header()
    program1()
    printProgram2Header()
    program2()
    printProgram3Header()
    program3()
    printProgram4Header()
    program4()
    printProgram5Header()
    program5()
    assignmentFooter()  

if __name__ == "__main__":
    main()
