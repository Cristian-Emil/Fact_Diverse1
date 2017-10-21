def showMenu(commands):
    print("Options: ")
    print("0.Exit")
    for cmd in commands.values():
        print(cmd[1])
    print("\n")

def readInt(str):
    '''
        Verifies if the input is an integer, returning it in that case and otherwise
        asking for another
    '''
    while True:
        try:
            x = int(input(str))
            return x
        except ValueError:
            print("You should enter an integer value!")

def isValid(str):
    '''
        This function checks if the list was typed in a valid format
        I data: String containing the numbers entered
        O data: True if the string is ok
                False otherwise
    '''

    last_c = ''
    for c in str:
        if (c < '0' or c > '9') and c != ' ':
            return False
        #if last_c == ' ' and c == ' ':
            #return False
        last_c = c

    return True


def uiReadList(l):
    list_str = input("Type the elements of the list, each being separated by exactly 1 space:\n")

    while not isValid(list_str):
        list_str = input("Invalid format. Try again:\n")

    for elem in list_str.split(" "):
        elem = elem.strip(' ')
        if elem != "":
            l.append(int(elem))

def uiPrintList(l):
    print("Your list:")
    for x in l:
        if x != " ":
            print(x)

def isInRange(x, a, b):
    '''
        The function checks if x is in range [a, b]
        I data:The number a and the limits of the range a and b
        O data:Returns True if x is in range [a, b]
                False if it isn't
    '''
    if x >= a and x <= b:
        return True
    else:
        return False

def testInRange():
    assert(isInRange(-2, 0, 10) == False)
    assert(isInRange(0, 0, 10) == True)
    assert(isInRange(10, 0, 10) == True)
    assert(isInRange(121, 120, 122) == True)
    assert(isInRange(12, 0, 10) == False)

def detLongestSequence(l):
    '''
        Returns a list containing the longest sequence
        whith elements in rang [0, 10]
    '''

    max = 0
    max_start = 0
    max_end = 0
    pos_start = 0
    pos_end = 0

    for i in range(len(l)):
        if isInRange(l[i], 0, 10):
            if pos_start == pos_end:
                pos_start = i
                pos_end = i + 1
            else:
                pos_end = pos_end + 1

        if not isInRange(l[i], 0, 10):
            if pos_end - pos_start > max_end - max_start:
                max_start = pos_start
                max_end = pos_end
            pos_start = pos_end

    if pos_end - pos_start > max_end - max_start:
        max_start = pos_start
        max_end = pos_end

    return l[max_start : max_end]

def sameList(l1, l2):
    '''
        This function checks if 2 lists have the same elemets, in the same order
    '''

    if len(l1) != len(l2):
        return False
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            return False

    return True

def testSameList():
    assert(sameList([31, 32, 12], [31, 32, 12]) == True)
    assert (sameList([31, 32, 12], [31, 32, 12, 5]) == False)
    assert (sameList([31, 32, 12, 2], [31, 32, 12]) == False)
    assert (sameList([31, 32, 12], [31, 2, 12]) == False)

def testDetLongestSequence():
    assert(sameList(detLongestSequence([13, 3, 4, 32, 31, 3, 4, 1, 42]), [3, 4, 1]) == True)
    assert(sameList(detLongestSequence([13, 3, 4, 32, 31, 3, 10, 1, 42, 0, 3, 4]), [3, 10, 1]) == True)
    assert(sameList(detLongestSequence([5, 3, 4, 32, 31, 3, 4, 1, 42]), [5, 3, 4]) == True)
    assert(sameList(detLongestSequence([13, 3, 4, 32, 31, 3, 4, 1, 42, 3, 6, 1, 0, 10]), [3, 6, 1, 0, 10]) == True)
    assert(sameList(detLongestSequence([3, 4, 8, 10, 342, 12, 0, 13, 34, 32, 11, 3, 7, 8, 1, 0]), [3, 7, 8, 1, 0]) == True)
    assert(sameList(detLongestSequence([23, 24, 23]), []))

def uiLongestSequence(l):
    print("Yout sequence:")

    sq = detLongestSequence(l)

    if sq == []:
        print("There are no elements in range [0, 10]")
    else:
        for x in sq:
            print(x)

        print("There may be some other sequences which have the same lenght.\nThis is the first one discovered.")

def runTests():
    testInRange()
    testDetLongestSequence()

def run():
    print("Wlecome, stranger!\n")

    list = []
    commands = {1:[uiReadList, "1.Create a list"], 2:[uiPrintList, "2.Print list"], 3:[uiLongestSequence, "3.Print the longest sequence containing only numbers in range [0, 10]"]}

    while True:
        showMenu(commands)

        cmd = readInt("Enter your option: ")

        if cmd == 0:
            return
        elif cmd in commands:
            commands[cmd][0](list)
            print("\n")
        else:
            print("Invalid command!\n")

runTests()
run()