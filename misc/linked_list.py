class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    def append(self,item):
        # make a node of the item
        temp = Node(item)
        # start at the head of the LL
        current = self.head
        previous = None
        # traverse through the entire LL and look for 'None'
        while current != None:
            previous = current
            current = current.getNext()
            # if 'None' is found, this means that we have reached the end of the list
            # or the list is empty
            if current == None:
                previous.setNext(temp)
    def insert(self,pos,item):
        iNode = Node(item)
        i = 0
        current_node = self.head
        next_node = None
        while i < self.size():
            next_node = current_node.getNext()
            
            if i == pos:
                temp = current_node
                temp.setData(iNode)
                temp.setNext(current_node)
                next_node = current_node
                


def main():
    mylist = UnorderedList()
    mylist.add(31)
    mylist.add(77)
    mylist.insert(2,54)
    mylist.append(42)
    print(mylist.size())
    print(mylist.search(54))

main()


