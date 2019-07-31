'''array size 3'''
size=3
array=[['N' for j in range(0,size)] for i in range(0,size)]
player1=input("player1 choose from 0 and *:")
if player1=='0':
    player2='*'
else:
    player2='0'
def check(array,num):
    flag=0
    for i in range(0,size):
        for j in range(0,size):
            count=0
            if array[i][j]==num:
                for k in range(0,size):#////////////////ROW
                    if array[i][k]==num:
                        count+=1
                if count==3:
                    flag=1
                    break
                count=0
                for k in range(0,size):#////////////COLUMN
                    if array[k][j]==num:
                        count+=1
                if count==3:
                    flag=1
                    break
                count=0#/////////////////////////DIAGONAL
                for k in range(0,size):
                    for l in range(0,size):
                        if  (k+l)==2 and array[k][l]==num:
                            count+=1
                if count==3:
                    flag=1
                    break
                count=0
                for k in range(0,size):
                    for l in range(0,size):
                        if  k==l and array[k][l]==num:
                            count+=1
                if count==3:
                    flag=1
                    break
        if flag==1:
            break
    return flag
def print_array(array):
    for i in range(0,size):
        for j in range(0,size):
            print(array[i][j],end=' ')
        print()
print_array(array)

count=0
flag=0
for i in range(0,9):
        if count==0:
            k=int(input("player 1 has to choose row he wants to enter:"))
            l=int(input("player 1 has to choose column he wants to enter:"))
            array[k][l]=player1
            count=1
            print_array(array)
            flag=check(array,player1)
            if flag==1:
                print("player1 won")
                break
        else:
            k=int(input("player 2 has to choose row he wants to enter:"))
            l=int(input("player 2 has to choose column he wants to enter:"))
            array[k][l]=player2
            count=0
            print_array(array)
            flag=check(array,player2)
            if flag==1:
                print("player2 won")
                break
if flag==0:
    print("Draw")
