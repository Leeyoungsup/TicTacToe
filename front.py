def box_set(C,box,size):
    x = []
    y = []
    for i in range(0,len(box)):
        x.append(0)
        y.append(0)
    for i in range(0,len(box)):
        for j in range(0,len(box)):
            C.create_rectangle(50+((size/len(box))*j),50+((size/len(box))*i),50+((size/len(box))*j)+(size/len(box)),50+((size/len(box))*i)+(size/len(box)))
            x[j] = 50+((size/len(box))*j)
        y[i] = 50+((size/len(box))*i)
    return [x,y]
class front:
    count = 0
    def __init__(self,C,box,x,y):
        self.C = C
        self.box = box
        self.x = x
        self.y = y
    def box_x_o(self,event):
        px,py = 0,0
        for i in range(0,len(self.box)):
            for j in range(0,len(self.box)):
                if self.box[i][j] == 1:
                    px , py = j , i
                    self.C.create_line(self.x[px],self.y[py],self.x[px]+(self.x[1]-self.x[0]),self.y[py]+(self.y[1]-self.y[0]))
                    self.C.create_line(self.x[px]+(self.x[1]-self.x[0]),self.y[py],self.x[px],self.y[py]+(self.y[1]-self.y[0]))         
                if self.box[i][j] == 2:
                    self.C.create_oval(self.x[j],self.y[i],self.x[j]+(self.x[1]-self.x[0]),self.y[i]+(self.y[1]-self.y[0]))

