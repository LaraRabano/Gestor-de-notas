

if __name__ == '__main__':
    n = int(input().strip())

    # Si el número es par
    if n % 2 == 0:
        
        if n >= 2 and n <= 5:
            print("Not Weird")
        
        elif n >= 6 and n <= 20:
            print("Weird")
        
        elif n > 20:
            print("Not Weird")

    # Si el número es impar
    else:
        print("Weird")


    
   













