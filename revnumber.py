'''
Reverse the number
Input    Output
4
12345    54321
31203    30213
2123     3212
2300     32
'''

num = int(input())

for i in range(num):
    a = input()
    str = ""
    for i in a:
        str = i+str
    print(int(str))



