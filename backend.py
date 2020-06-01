from tkinter import *
import random as r
def Victory_condition(box,tk):
    win = 0
    number1 = []
    number2 = []
    for i in range(0,4):
        number1.append(0)
        number2.append(0)
    for i in range(0,len(box)):
        for j in range(0,len(box)):
            if box[i][j] == 1:
                number1[0]+=1
            if box[i][j] == 2:
                number2[0]+= 1
        for j in range(0,len(box)):
            if box[j][i] == 1:
                number1[1] += 1
            if box[j][i] == 2:
                number2[1] += 1
        for j in range(0,len(box)):
            if i == j and box[i][j] == 1:
                number1[2] +=1
            if i == j and box[i][j] == 2:
                number2[2] +=1
            if i +j == (len(box)-1) and box[i][j] == 1:
                number1[3] +=1
            if i +j == (len(box)-1) and box[i][j] == 2:
                number2[3] +=1
        if number1[0] >= 3 or number1[1] >= 3 or number2[0] >= 3 or number2[1] >= 3:
            break
        else:
            number1[0] = 0
            number1[1] = 0
            number2[0] = 0
            number2[1] = 0
    for i in range(0,len(number1)):
        if number1[i] == len(box):
            print("승자는 플레이어입니다.")
            tk.quit()
            tk.destroy()
            return 1
        if number2[i] == len(box):
            print("승자는 컴퓨터입니다.")
            tk.quit()
            tk.destroy()
            return 1
    return 0
def draw(box,tk):
    count = 0
    for i in range(0,len(box)):
        for j in range(0,len(box)):
            if box[i][j] == 0:
                count +=1
    if count == 0:
        print("비겼습니다.")
        tk.quit()
        tk.destroy()
        return  1
        
class ttt_back:
    count = 0
    nt = 0
    def __init__(self,tk,xsize,ysize,pan):
        self.tk = tk
        self.x = xsize
        self.y = ysize
        self.box = pan
    def play(self,event):
        End = 0
        px,py = 0,0
        for i in range(0,len(self.box)):
            for j in range(0,len(self.box)):
                if event.x > self.x[j] and event.x < self.x[j]+(self.x[1]-50) and event.y >self.y[i] and event.y < self.y[i]+(self.y[1]-50):
                    px , py = j , i
        if self.box[py][px] == 1 or self.box[py][px] == 2:
            print("다른곳을 클릭해주세요.")
            self.nt = 1
            return 0
        else:
            self.box[py][px] = (self.count%2+1)
            self.count+=1
            for i in range(0,len(self.box)):
                print(self.box[i])
            End = Victory_condition(self.box,self.tk)
            if End != 1:
                End =  draw(self.box,self.tk)
                
            if End == 1:
                return 0
        if self.nt == 1:
            self.nt =0
            return 0
        n = []
        cpt = 0
        while True:
            cpt = r.randrange(0,pow(len(self.box),2))
            n = [cpt//len(self.box),cpt%len(self.box)]
            if self.box[n[0]][n[1]] == 1 or self.box[n[0]][n[1]] == 2:
                print("다시고르는 중입니다.")
            else:
                break
        End = 0
        self.box[n[0]][n[1]] = (self.count%2)+1
        self.count+=1
        for i in range(0,len(self.box)):
            print(self.box[i])
        Victory_condition(self.box,self.tk)
        if End != 1:
            draw(self.box,self.tk)
                
        
