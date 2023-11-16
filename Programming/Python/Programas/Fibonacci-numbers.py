perfectSquares = []
for num in range(1,201):
    perfectSquares.append(num**2)

def isFibonacci(n):
    if( (5*(n**2) + 4) in perfectSquares or (5*(n**2) - 4) in perfectSquares):
        return True
    else:
        return False

for i in range(0, 101):
    if(isFibonacci(i)):
        print(f"El numero {i} es fibonacci")