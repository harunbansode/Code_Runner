from typing import List
def finalValueAfterOperations(operations: List[str]) -> int:
    x = 0
    for i in range(0, len(operations)):
        if operations[i] in 'X++' or operations[i] in '++X':
            x += 1
        else:
            x -= 1
    return x
operations = ["X++","++X","--X","X--"]
print(finalValueAfterOperations(operations))