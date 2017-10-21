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

def atMost3(d):
    if len(d) > 3:
        return False
    else:
        return True

def testAtMost3():
    assert(atMost3({3:2, 4:4, 2:1}) == True)

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
    dist ={}


    for i in l:
        if i in dist:
            dist[i] = dist[i] + 1
        else:
            dist[i] = 1

        if atMost3(dist) == True:
            pos_end = pos_end + 1
        else:
            elem = l[pos_start]
            while atMost3(dist) == False:
                pos_start = pos_start + 1
                dist[elem] = dist[elem] - 1
                if dist[elem] == 0:
                    del dist[elem]

        if pos_end - pos_start > max_end - max_start:
            max_start = pos_start
            max_end = pos_end

    return l[max_start : max_end + 1]

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
    assert(sameList(detLongestSequence([8, 1, 3, 5, 1, 3, 4, 4, 1]), [1, 3, 5, 1, 3]) == True)


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

    testDetLongestSequence()

def run():
    print("Wlecome, stranger!\n")

    list = []
    commands = {1:[uiReadList, "1.Create a list"], 2:[uiPrintList, "2.Print list"], 3:[uiLongestSequence, "3.Print the longest sequence containing at most 3 distinct values."]}

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