from search import exists, find_index

if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8]
    has_eight: bool = exists(l=l, target=8)
    assert has_eight == True

    index_of_eight: int|None = find_index(l=l, target=8)
    assert index_of_eight == l.index(8)
