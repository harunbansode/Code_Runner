def defangIPaddr(address: str) -> str:
    replaces = '[.]'
    def1 = ''
    print(len(address))
    for i in range(0, len(address)):
        if address[i] in ".":
            # print(address[i])
            def1 += replaces
        else:
            def1 += address[i]
    return def1
print(defangIPaddr( "255.100.50.0"))