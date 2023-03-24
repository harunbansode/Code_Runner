def Remove_Vowels(address: str) -> str:
    remove_words = ['a', 'e', 'i', 'o', 'u']
    stmts = ''
    for i in range(0, len(address)):
        print(address[i])
        if address[i] in remove_words:
            continue
        else:
            stmts += address[i]
    return stmts
print(Remove_Vowels('welcome to geeksforgeeks'))