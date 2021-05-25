'''
Input
3
12345
31203
2123
Output
15
9
8


'''

n = int(input())
for _ in range(n):
    num = input()
    sum = 0
    for i in num:
        sum += int(i)
    print(sum)




