'''
You're given an integer N. Write a program to calculate the sum of all the digits of N.
In this section example of input and output are given in the expected format.
Input
3
1 2
100 200
10 40

Output
3
300
50
'''


'''
The first line contains an integer T, the total number of testcases. Then follow T lines, each line contains an integer N.
'''


tests = int(input())
done = []

i =1

while (i<= tests):
   A,B=input().split(" ")
   A=int(A)
   B=int(B)
   c = A+B
   done.append(c)
   i=i+1


for number in done:
    print(number)
