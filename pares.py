def e_par(n):
    return n%2==0
def pares():
    par=0
    impar=0
    for a in range(100):
        r=int(input(''))
        if e_par(r):
            par +=1
        else:
            impar+=1
    print(int(par))
    print(int(impar))
def main():
    pares()
if __name__=='__main__':
    main()
