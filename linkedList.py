class Node:
    def __init__(self, content=None, next=None):
        self.content = content
        self.next = next


class FibList:
    def __init__(self, n: int=100):
        if n <= 0:
            self.head = None
        elif n == 1:
            self.head = Node(content=0)
        else:
            self.head = Node(content=0, next=Node(content=1))
            a = 0
            b = 1
            i = 2
            cur = self.head.next
            while i < n:
                cur.next = Node(content=a+b)
                a, b = b, a+b
                i += 1
                cur = cur.next

    def println(self):
        if self.head is None:
            print("*** Empty list!")
            return
        cur = self.head
        output = str(cur.content)
        while cur.next is not None:
            cur = cur.next
            output += " " + str(cur.content)
        print(output)


def main():
    l1 = FibList()
    l1.println()
    l2 = FibList(10)
    l2.println()
    l3 = FibList(-5)
    l3.println()


if __name__ == "__main__":
    main()