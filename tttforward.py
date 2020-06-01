from backend import *
from front import *

if __name__ == "__main__":
    print("게임설명")
    print("마우스를 이용하여 좌표를 클릭하면 그순간 좌표를 인식받아 x자를 그립니다.")
    n = int(input("칸의 계수를 입력해 주세요 : "))
    size = int(input("판의 크기를 적어주세요 : "))
    x = []
    y = []
    box = [[0]*n for i in range(0,n)]
    strsize = str(size+100)+"x"+str(size+100)
    pan = [[0]*3 for i in range(0,3)]
    ttt = Tk()
    ttt.geometry(strsize)
    C = Canvas(ttt,width = size+100,height = size+100)
    x, y = box_set(C,box,size)
    ft = front(C,box,x,y)
    game = ttt_back(ttt,x,y,box)
    
    C.bind("<Button-1>",game.play)
    C.bind("<ButtonRelease-1>",ft.box_x_o)
    C.pack()
    ttt.mainloop()
