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

#
# '''
#
# n = int(input())
# for _ in range(n):
#     num = input()
#     sum = 0
#     for i in num:
#         sum += int(i)
#     print(sum)



def change(coin):
    return '1' if (coin == '0') else '0'

def flipStartChar(str,expected):
    flips = 0
    for i in range(len(str)):

        if (str[i] != expected):
            flips = flips + 1
        expected = change(expected)

    return flips

def solution(str):
    # write your code in Python 3.6
    return min(flipStartChar(str, '0'),flipStartChar(str,'1'))


if __name__ == "__main__":
    str = "010"
    print(solution(str))
    
