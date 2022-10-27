import open_json

doska = list(range(1,10))

def draw_board(board):
    for i in range(3):
        print ("|", doska[0+i*3], "|", doska[1+i*3], "|",doska[2+i*3], "|")

def stavim_hod(hod):
    valid = False
    while not valid:
        otvet = input("Введите номер клетки куда поставить значение " + hod+"? ")
        otv = int(otvet)
        if otv >= 1 and otv <= 9:
            if (str(doska[otv-1]) not in "XO"):
                doska[otv-1] = hod
                valid = True
            else:
                print ("Эта клетка занята")
def kto_viigral(doska):
    pobeda = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for x in pobeda:
        if doska[x[0]] == doska[x[1]] == doska[x[2]]:
            return doska[x[0]]
    return False

tic_tac_toe = open_json.get_data()

def igra(doska, tic_tac_toe):
    count = 0
    win = False
    while not win:
        draw_board(doska)
        if count % 2 == 0:
            stavim_hod(tic_tac_toe["cross"])
        else:
            stavim_hod(tic_tac_toe["zero"])
        count += 1
        if count > 4:
            m = kto_viigral(doska)
            if m:
                print (m, "Победил!")
                win = True
                break
        if count == 9:
            print ("Ничья!")
            break
    draw_board(doska, tic_tac_toe)

igra(doska, tic_tac_toe)