'''
If Give an integer N . Write a program to obtain the sum of the first and last digits of this number.
'''



n = int(input())
list1 = []
i = 1
while(i <= n):
    num = int(input())
    #list1.append(num)
    num2 = str(num)
    first = int(num2[0])
    last = int(num2[-1])
    sum = first + last
    list1.append(sum)
    i = i + 1


for x in list1:
    print(x)



# print(list1)

# a = int(input())
# num = str(a)
# first = int(num[0])
# last = int(num[-1])
#
# sum = first + last
#
# print(f"Sum of {first} & {last} digit is", sum)
#
# val = "shubham"
#
# print(f"{val} is a guy. {val} is a nice guy. be like {val}")




