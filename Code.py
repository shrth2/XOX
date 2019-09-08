def printing(a):
    i = 0
    print(a[i], a[i + 1], a[i + 2])
    print(a[i + 3], a[i + 4], a[i + 5])
    print(a[i + 6], a[i + 7], a[i + 8])
def player1(a):
    print("Player 1 enter the cell number where you want X")
    A = int(input())
    if A == 1:
        a[A - 1] = 'X'
    else:
        a[A - 1] = 'X'
    return (a)
def player2(a):
    print("Player 2 enter the cell number where you want O")
    A = int(input())
    if A == 1:
        a[A - 1] = 'O'
    else:
        a[A - 1] = 'O'
    return (a)
def result(a):
    if a[0] == a[1] == 'X' and a[1] == a[2] == 'X' or a[0] == a[4] == 'X' and a[4] == a[8] == 'X' or a[0] == a[
        3] == 'X' and a[3] == a[6] == 'X' or a[2] == a[5] == 'X' and a[5] == a[8] == 'X' or a[2] == a[4] == 'X' and a[
        4] == a[6] == 'X' or a[6] == a[7] == 'X' and a[7] == a[8] == 'X' or a[1] == a[4] == 'X' and a[4] == a[
        7] == 'X' or a[3] == a[4] == 'X' and a[4] == a[5] == 'X':
        return (1)
    elif a[0] == a[1] == 'O' and a[1] == a[2] == 'O' or a[0] == a[4] == 'O' and a[4] == a[8] == 'O' or a[0] == a[
        3] == 'O' and a[3] == a[6] == 'O' or a[2] == a[5] == 'O' and a[5] == a[8] == 'O' or a[2] == a[4] == 'O' and a[
        4] == a[6] == 'O' or a[6] == a[7] == 'O' and a[7] == a[8] == 'O' or a[1] == a[4] == 'O' and a[4] == a[
        7] == 'O' or a[3] == a[4] == 'O' and a[4] == a[5] == 'O':
        return (2)
res='y'
while(res!='n'):
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(5):
        printing(a)
        a = player1(a)
        z = result(a)
        if i == 4 or z == 1:
            break
        printing(a)
        a = player2(a)
        z = result(a)
        if z == 2:
            break
    if z == 1:
        printing(a)
        print("Player 1 wins")
    elif z == 2:
        printing(a)
        print("Player 2 wins")
    else:
        print("The game ends in a TIE!!!!!")
    print("Do you want to play again???? (y/n)")
    res=input()
print("Thank you for playing:)")
