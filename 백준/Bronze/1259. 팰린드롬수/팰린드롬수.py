import sys

# input = sys.stdin.read
flag = True
while flag:
    a = input()
    if a == '0':
        flag = False
        break
    if a == a[::-1]:
        print('yes')
    else:
        print('no')
