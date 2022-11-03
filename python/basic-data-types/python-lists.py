if __name__ == '__main__':
    N = int(input())
    L = []
    for i in range(N):
        comando = input().split()
        if comando[0]=='insert':
            L.insert(int(comando[1]),int(comando[2]))
        elif comando[0]=='print':
            print(L)
        elif comando[0]=='remove':
            L.remove(int(comando[1]))
        elif comando[0]=='append':
            L.append(int(comando[1]))
        elif comando[0]=='sort':
            L.sort()
        elif comando[0]=='pop':
            L.pop()
        elif comando[0]=='reverse':
            L.reverse()