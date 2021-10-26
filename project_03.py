# Cyrus Straley
# Last updated 10/24/21
# Sarah Saturday's Shape Printer 
# This app prompts user to enter a shape as a command in the command prompt, then takes certain parameters that defines the size of the shape(s).

def box(printType, rows, cols):
    if rows > 0 and cols > 0 and cols < 50:
        if printType == 'filled' or printType == 'Filled':
            for i in range(rows):
                print('*' * cols)
        elif printType == 'outline' or printType == 'Outline':
            for i in range(rows):
                for j in range(cols):
                    if (i == 0 or i == rows-1) or (j == 0 or j == cols-1):
                        print('*', end=" ")
                    else:
                        print(" ", end=" ")
                print()
        else:
            print("Enter a valid print type.")
            promptUser()
    else:
        print("Enter valid number of columns/rows.")

    promptUser()


def right(printType, length):
    if length > 0 and length < 50:
        if printType == 'filled' or printType == 'Filled':
            for i in range(length + 1):
                print('*' * i)
        elif printType == 'outline' or printType == 'Outline':
            for i in range(1, length+1):
                for j in range(1, i+1):
                    if i == 1 or i == length or j == 1 or j == i:
                        print('*', end=" ")
                    else:
                        print(" ", end=" ")
                print()
        else:
            print("Enter valid print type.")
            promptUser()
    else:
        print("Enter valid length.")

    promptUser()
                                               

def iso(printType, length): 
    if length > 0 and length < 50 and (length % 2 == 1):
        if printType == 'filled' or printType == 'Filled':
            for i in range(length):
                for j in range(length-1-i):
                    print(end=" ")
                for j in range(i+1):
                    print('*', end=" ")
                print()
        elif printType == 'outline' or printType == 'Outline':
            for i in range(length):
                for j in range(length+i):
                    if (i+j == length-1) or (j == length+i-1):
                        print("*", end='')
                    elif i == length-1 and j % 2 == 0:
                        print("*", end="")
                    else:
                        print(end=" ")
                print()

        else:
            print("Enter valid print type")
            promptUser()
    else:
        print("Enter valid length.")

    promptUser()


# main help function; includes information for all commands and parameters
def help(args=None):
    if args == 'box' or args == 'Box':
        print("The 'box' command prints a rectangle.")
        print()
        print("Parameters: ")
        print("     type: Print type; 'filled' or 'outline'")
        print("     rows: Number of rows, integer greater than 0")
        print("     cols: Number of cols, integer between 0 and 50")
        promptUser()
    elif args == 'iso' or args == 'Iso':
        print("The 'iso' command prints an Isosceles triangle.")
        print()
        print("Parameters: ")
        print("     type: Print type; 'filled' or 'outline'")
        print("     length: Length of base; odd integer between 0 and 50")
        promptUser()
    elif args == 'right' or args == 'Right':
        print("The 'right' command prints a Right triangle.")
        print()
        print("Parameters: ")
        print("     type: Print type; 'filled' or 'outline'")
        print("     length: Length of base; integer between 0 and 50")
        promptUser()
    elif args == 'quit' or args == 'Quit':
        print("The 'quit' command exits the terminal.")
        print()
        print("Parameters: ")
        print("     none")
        promptUser()
    else:
        print("Welcome to Sarah Saturday's Shape Printer.")
        print()
        print("The following shapes are available.")
        print("Type 'help' followed by any command for more information on a shape." )
        print()
        print("1. Box (command: box)")
        print("2. Right triangle (command: right)")
        print("3. Isosceles triangle (command: iso)")
        print("4. Quit (command: quit)")
        promptUser()


def getCommand(cmd, helpArg=None, pType=None, row=None, cols=None, length=None):
    if cmd == 'help' or cmd == 'Help':
        if helpArg:
            help(helpArg)
        else:
            help()
    elif cmd == 'quit' or cmd == 'Quit':
        quit()
    elif cmd == 'box' or cmd == 'Box':
        box(pType, row, cols)
    elif cmd == 'right' or cmd == 'Right':
        right(pType, length)
    elif cmd == 'iso' or cmd == 'Iso':
        iso(pType, length)
    else:
        print('Please enter a valid command.')
        promptUser()


# main function for accepting commands. 
def promptUser():
    print()
    command = str(input('>>> '))
    print()
    args = command.split(' ')
    try:
        # calls different functions based on numbers of parameters; accepts errors if parameter(s) invalid. 
        if len(args) == 1:
            getCommand(command)
        elif len(args) == 2:
            getCommand(args[0], args[1])
        elif len(args) == 3:
            getCommand(args[0], pType=args[1], length=int(args[2]))
        else:
            getCommand(args[0], pType=args[1], row=int(args[2]), cols=int(args[3]))
    except ValueError:
        print(f"Enter valid parameters for '{args[0]}' command.")
        promptUser()
    except TypeError:
        print(f"Enter valid parameters for '{args[0]}' command.")
        promptUser()


print("Sarah Saturday's Shape Printer 1.0.0 (Oct 24 2021)")
print("Type 'help' for more information")

if __name__ == '__main__':
    promptUser()


