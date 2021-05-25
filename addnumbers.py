'''
Program is very simple, given two integers A and B, write a program to add these two numbers.

Input
This section tells you the format in which your program should receive the input.
The first line contains an integer T, the total number of test cases. Then follow T lines, each line contains two Integers A and B.

Output
This section tells us the format in which our program should give the output
For each test case, add A and B and display it in a new line.

'''


print("Enter the total number of test cases")
test = int(input())
n = 0
l = []
out = f"Enter two integers for {test} lines"
print(out)
while (n <= test):
    n = n+1
    if n > test:
        break
    a, b = map(int, input().split())
    sum = a + b
    l.append(sum)


for elem in l:
    print(elem)





