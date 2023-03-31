# def interpret(command: str) -> str:
#     new_string = command.replace('()', 'o')
#     return new_string.replace('(al)', 'al')

# command = "G()(al)"
# print(interpret(command))

def interpret(command: str) -> str:
    new_string = command.replace('()', 'o').replace('(al)', 'al')
    return new_string

command = "G()()()()(al)"
print(interpret(command))