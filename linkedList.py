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

    def reverse(self):
        # need three pointers
        prev = None
        cur = self.head
        next = None
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev


def main():
    small = FibList(10)
    small.println()
    small.reverse()
    small.println()

    full = FibList()
    full.println()
    full.reverse()
    full.println()


if __name__ == "__main__":
    main()
