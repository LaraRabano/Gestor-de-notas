"""Task
The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
"""


if __name__ == '__main__':
    a = int(input())
    b = int(input())

    suma = a + b
    resta = a - b
    division = a % b 

    print(f"{a} + {b} = {suma}")

    print(f"{a} - {b} = {resta}")

    print(f"{a} / {b} = {division}")



