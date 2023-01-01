"""
implement binary search

return index: int or None
index: is the index in the original list of the target
return None if not found
"""

def exists(l: list, target)->bool:
    midpoint: int = len(l) // 2
    if target > l[midpoint]:
        # print(f"{target=} is larger than the {midpoint=}, so now the list is: {l[midpoint:]}")
        return exists(l=l[midpoint:], target=target)
    if target < l[midpoint]:
        # print(f"{target=} is smaller than the {midpoint=}, so now the list is: {l[0:midpoint]}")
        return exists(l=l[0:midpoint], target=target) 
    elif target == l[midpoint]:
        # print(f"{target=} and {midpoint=}, so now the list is: {l[midpoint:]}")
        return True
    else:
        return False

def find_index(l: list, target)->int|None:
    if len(l):
        if len(l) == 1:
            if l[0] == target:
                return 0
            else:
                return None
        lower, upper = 0, len(l) - 1
        if lower == target:
            return lower
        if upper == target:
            return upper
        
        while lower <= upper:
            midpoint = ( lower + upper ) // 2
            if target == l[midpoint]:
                return midpoint
            elif target < l[midpoint]:
                upper = upper - 1
            elif target > l[midpoint]:
                lower = lower + 1
    return None


