# You can remove 'pass' if you written code in the function
# Each node is a list: [Data, Pointer]. A pointer of -1 means "points to nothing".

LinkedList = []
FirstNode = -1
FirstEmpty = 0


# Exercise 1
def Initialise():
    # Write your code here
    global LinkedList,FirstEmpty,FirstNode
    for x in range(10):
        LinkedList.append([-1, x + 1])
    LinkedList[9][1] = -1
    FirstEmpty=0
    FirstNode=-1
    pass
def IsEmpty():
    # Write your code here
    if FirstNode == -1:
        return True
    return False
    pass

def IsFull():
    # Write your code here
    if FirstEmpty == -1:
        return True
    return False
    pass


def OutputNodes():
    # Write your code here
    global LinkedList, FirstNode
    cur_pointer = FirstNode
    try:
        while cur_pointer != -1:
            print((LinkedList[cur_pointer][0]))
            cur_pointer = LinkedList[cur_pointer][1]
    except
        return "Linked list is empty"

    pass


# Exercise 2
def InsertInOrder(Item):
    # Write your code here
    pass


# Exercise 3
def Delete(Item):
    # Write your code here
    pass


# Exercise 4
def LoadFromFile(FileName):
    # Write your code here
    pass


# Exercise 5
def Reverse():
    # Write your code here
    pass
