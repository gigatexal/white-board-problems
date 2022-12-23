from random import randint

LOWER_BOUND: int = -10**5
UPPER_BOUND: int = 10**5
NUM_CANDIDATES: int = 3000

TRIPLET_TARGET: int = 0

DATA = [randint(LOWER_BOUND, UPPER_BOUND) for _ in range(NUM_CANDIDATES)]

def find_triplets(d: list[int])->list[list[int]]:
        solutions: set[tuple[(int,int, int)]] = set()
        sorted_input: list[int] = sorted(d)
        for current_index in range(len(sorted_input)):
            target: int = -sorted_input[ current_index ]
            start, end = current_index +1, len(sorted_input)-1
            while start < end:
                candidate: int = sorted_input[start]+sorted_input[end]
                if candidate < target:
                    start = start + 1
                elif candidate > target:
                    end = end - 1
                else:
                    if start != end and start != current_index and end != current_index :
                        solution: tuple[int, int, int] = (sorted_input[ current_index ],sorted_input[start], sorted_input[end])
                        if solution not in solutions:
                            solutions.add(solution)
                    end = end - 1
                    start = start + 1
        return [list(x) for x in solutions]    
    
if __name__ == '__main__':
    print(find_triplets(DATA))
