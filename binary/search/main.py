from search import BinarySearch

if __name__ == '__main__':
    l = [1,2,3,4,5,6,7,8]
    has_eight: bool = BinarySearch(l=l, target=8)
    assert has_eight == True

