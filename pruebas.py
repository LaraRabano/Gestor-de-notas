from logging import raiseExceptions


if __name__ == '__main__':
    n = int(input())
    
    y = ""
    
    for x in range(1, n + 1):
        if x != 3:
            y = y + str(x)
        
        else: 
            try:
                raise Exception()
            except:
                print("Drama")

                continue


    print(y)

        


numeros=[1, 2, 3, 4, 5, 6]

n = ""

for i in numeros:
    if i % 2 == 0:
        n = n + str(i)
    print(n)
    
    
