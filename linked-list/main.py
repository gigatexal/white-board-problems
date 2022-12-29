from single import LinkedList

if __name__ == '__main__':
    l = LinkedList()
    l.add(1)
    l.add(42)
    l.add(3)
    l.print()
    print("popping off the first element")
    l.popleft()
    l.print()
    print("popping the last element")
    l.pop()
    l.print()

