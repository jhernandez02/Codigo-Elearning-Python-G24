# factorial.py

def factorial(n):
    if n < 0:
        raise ValueError('Números negativos no son aceptados')
    elif n==0 or n==1:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result

if __name__=='__main__':
    print(factorial(4))