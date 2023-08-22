class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next




class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

    def insert_values(self, list_values):
        self.head = None
        for data in list_values:
            self.insert_at_begining(data)

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next

        return  count

    def remove_at(self, index):
        if index< 0 or index >= self.get_length():
            raise  Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            count += 1
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return
        count = 0
        itr = self.head
        while itr:
            count += 1
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next

    def print(self):
        if self.head is None:
            print("Empty list")
            return
        else:
            itr = self.head
            list_data = ""
            while itr:
                list_data += str(itr.data)
                itr = itr.next
                if itr is not None:
                    list_data +=  "------>"
            print(list_data)



if __name__ == "__main__":
    list = LinkedList()
    list.insert_at_begining(30)
    list.insert_at_begining(66)
    list.insert_at_begining(50)
    list.insert_at_begining(12)
    list.insert_at_begining(25)
    list.insert_at_begining(45)
    list.insert_at_begining(400)

    list.remove_at(4)
    list.remove_at(2)

    list.insert_at(4, 450)
    list.insert_at(2,9999)

    print("length of the linkedList is {}".format(list.get_length()))
    list.print()