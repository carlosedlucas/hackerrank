def swap_case(s):
    letras = []
    for i in s:
        if i == i.lower():
            letras.append(i.upper())
        else:
            letras.append(i.lower())
    return ''.join(letras)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)