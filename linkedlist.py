class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        newdata = Node(data)
        if self.head is None:
            self.head = newdata
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = newdata

    def printr(self):
        printval = self.head
        while printval:
            print(printval.val)
            printval = printval.next
        cb = []
        while self.head:
            cb.append(str(self.head.val) + " --> ")
            self.head = self.head.next
        return " ".join(cb)

    def remove(self, k):
        first = second = self.head
        for i in range(k):
            first = first.next
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next


b = LinkedList()
c = [2, 3, 4, 6]
for item in c:
    b.insert(item)
b.remove(2)
print(b.printr())
