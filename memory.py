import random
import time

successes = 0
theKeys='1 2 3 4 5 6 7 8 9 10 11 12'.split()
theValues='apple apple grape grape melon melon kiwi kiwi orange orange peach peach'.split()
random.shuffle(theValues)
di = {}

for i in range(12):
    di[theKeys[i]] = theValues[i]

board = [theKeys[i] for i in range(12)]
print(board[0]+'   '+board[1]+'   '+board[2]+'   '+board[3]+'\n'+board[4]+'   '+board[5]+'   '+board[6]+'   '+board[7]+'\n'+board[8]+'   '+board[9]+'  '+board[10]+'  '+board[11]+'\n')

while successes < 6:
    print('Enter two card numbers: ')

    a = input()
    while a not in '1 2 3 4 5 6 7 8 9 10 11 12' or board[int(a)-1]!=theKeys[int(a)-1]:
        if a not in '1 2 3 4 5 6 7 8 9 10 11 12':
            print('The first number was not valid. Enter a valid card number.')
        else:
            print('The first card number is already revealed. Enter another number.')
        a = input()
    
    b = input()
    while b not in '1 2 3 4 5 6 7 8 9 10 11 12' or board[int(b)-1]!=theKeys[int(b)-1] or a==b:
        if b not in '1 2 3 4 5 6 7 8 9 10 11 12':
            print('The second number was not valid. Enter a valid card number.')
        elif a==b:
            print('You can\'t enter a card number twice.')
        else:
            print('The second card number is already revealed. Enter another number.')
        b = input()

    x = int(a)
    y = int(b)

    board[x-1] = di[theKeys[x-1]]
    board[y-1] = di[theKeys[y-1]]
    print('\n'+board[0]+'   '+board[1]+'   '+board[2]+'   '+board[3]+'\n'+board[4]+'   '+board[5]+'   '+board[6]+'   '+board[7]+'\n'+board[8]+'   '+board[9]+'  '+board[10]+'  '+board[11]+'\n')
    
    if di[theKeys[x-1]]!=di[theKeys[y-1]]:
        board[x-1] = theKeys[x-1]
        board[y-1] = theKeys[y-1]
        time.sleep(4)
        print(50*'\n')
        print(board[0]+'   '+board[1]+'   '+board[2]+'   '+board[3]+'\n'+board[4]+'   '+board[5]+'   '+board[6]+'   '+board[7]+'\n'+board[8]+'   '+board[9]+'  '+board[10]+'  '+board[11]+'\n')
    else:
        time.sleep(2)
        successes+=1
        if successes > 5:
            print('Well done! You solved it!')
