#primo.py

def es_primo(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

if __name__=='__main__':
    print(es_primo(7))
    print(es_primo(8))