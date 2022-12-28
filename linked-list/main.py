from single import LinkedList

if __name__ == '__main__':
    l = LinkedList()
    l.add(1)
    l.add(42)
    l.add(3)
    l.print()
    print("should print 1 42 3")
    print("popping off the first element")
    l.popleft()
    l.print()
    print("and another")
    l.popleft()
    l.print()

