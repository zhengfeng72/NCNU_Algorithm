import tkinter as tk
import re
import heapq
import math
class Graph():
    def __init__(self,nodeNum,sides,direction=False):
        self.nodeNum = nodeNum #頂點
        self.amatrix = [[0]*(nodeNum) for i in range(nodeNum)]   #鄰接矩陣
        for side in sides:
            u,v,w = side
            if(direction):
                self.amatrix[u][v]=int(w)
            else:
                self.amatrix[u][v]=int(w)
                self.amatrix[v][u]=int(w)

def btnClick():
    point_number = int(input1.get())
    point_name = input2.get()
    edge_length_tmp = input4.get()
    start_point = input5.get()
    
    edge_length = re.findall("[A-Z],[A-Z],\\d",edge_length_tmp)
    
    sides = []
    for i in edge_length:
        i = i.split(',')
        sides.append([ord(i[0])-65,ord(i[1])-65,int(i[2])])
    print(sides)
    graph = Graph(point_number,sides)

    # for i in range(point_number):
    #     for j in range (point_number):
    #         print(graph.amatrix[i][j],end=" ")
    
    points = []#個點xy座標
    r = 30*int(point_number)
    maxy = 0
    miny = 0
    for i in range(int(point_number)):
        x = int(r*math.cos((2*math.pi/int(point_number))*i))
        y = int(r*math.sin((2*math.pi/int(point_number))*i))
        point = {"name":chr(65+i),"x":x,"y":y}
        maxy = max(maxy,y)
        miny = min(miny,y)
        # print(x,y)
        points.append(point)
    print('graph height',maxy-miny)

    v = ord(start_point)-65
    visitnodes = []
    minimumSpanningTree = []
    visitnodes.append(v)
    edges = []
    for j in range(graph.nodeNum):  #從節點v出發的邊入堆
        if(graph.amatrix[v][j]>0):
            ## weight, start, to
            heapq.heappush(edges,[graph.amatrix[v][j],v,j])
    k=1
    while(k < graph.nodeNum):
        w,vi,vj = heapq.heappop(edges)  #輸出權重最小的一條邊
        if (vj not in visitnodes):  #若該邊鏈接的節點未被訪問，將節點vj出發的邊插入堆中
            minimumSpanningTree.append([vi,vj,w])
            visitnodes.append(vj)
            print(minimumSpanningTree)

            #將相關線段放入
            for i in range(graph.nodeNum):
                if(graph.amatrix[vj][i]>0):
                    heapq.heappush(edges,[graph.amatrix[vj][i],vj,i])
            # draw
            adjust = 40*int(point_number)
            for p in range(len(sides)):  #畫線
                # for pnt in points:
                #     print(pnt)
                left = int(sides[p][0])
                right = int(sides[p][1])
                
                length = int(sides[p][2])

                leftx = points[left]['x']
                lefty = points[left]['y']

                rightx = points[right]['x']
                righty = points[right]['y']
                if ( [left,right,length] in minimumSpanningTree or [right,left,length] in minimumSpanningTree):
                    line = canvas2.create_line(leftx+adjust,lefty+adjust,rightx+adjust,righty+adjust,fill="red")
                else:
                    line = canvas2.create_line(leftx+adjust,lefty+adjust,rightx+adjust,righty+adjust)
                canvas2.create_text(((leftx+rightx)/2)+adjust,((lefty+righty)/2)+adjust,text=length,font=('purisa',22))  #線的長度
            for q in range(int(point_number)):  #畫英文字母
                x1 = points[q]['x']+adjust
                y1 = points[q]['y']+adjust
                circle_r = 15
                oval = canvas2.create_oval(x1-circle_r,y1-circle_r,x1+circle_r,y1+circle_r,fill='#FFCCCC')
                canvas2.create_text(x1,y1,text=point_name[q],fill='blue',font=('purisa',22))
            print(k,'.')
            for point in points:
                print(point['name'],point['y'])
                point['y'] = point['y'] + (maxy-miny+50)
                

            k=k+1
    print('final', minimumSpanningTree)
    
def clean():
    canvas2.delete("all")

window = tk.Tk()
window.title('prim\'s algorithom')
window.geometry("640x480")

label1 = tk.Label(window, text="點數:",bg="#CCCCFF",font=("標楷體",14),borderwidth=1,relief='ridge')
label1.pack()
label1.place(x=15,y=12)

input1 = tk.Entry(window,width="5",borderwidth=1)
input1.insert(0,'5')
input1.pack()
input1.place(x=60,y=10)

label2 = tk.Label(window, text="名稱:",bg="#CCCCFF",font=("標楷體",14),borderwidth=1,relief='ridge')
label2.pack()
label2.place(x=130,y=12)

input2 = tk.Entry(window,width="10",borderwidth=1)
input2.insert(0,'ABCDE')
input2.pack()
input2.place(x=180,y=10)

# label3 = tk.Label(window, text="邊數:",bg="#CCCCFF",font=("標楷體",14),borderwidth=1,relief='ridge')
# label3.pack()
# label3.place(x=15,y=42)

# input3 = tk.Entry(window,width="5",borderwidth=1)
# input3.insert(0,'5')
# input3.pack()
# input3.place(x=60,y=40)

label4 = tk.Label(window, text="內容:",bg="#CCCCFF",font=("標楷體",14),borderwidth=1,relief='ridge')
label4.pack()
label4.place(x=15,y=42)

input4 = tk.Entry(window,width="30",borderwidth=1)
input4.insert(0,'(B,A,1) (B,C,2) (C,D,3) (D,B,6) (D,E,6)')
input4.pack()
input4.place(x=60,y=40)

label5 = tk.Label(window, text="起始點:",bg="#CCCCFF",font=("標楷體",14),borderwidth=1,relief='ridge')
label5.pack()
label5.place(x=300,y=12)

input5 = tk.Entry(window,width="5",borderwidth=1)
input5.insert(0,'A')
input5.pack()
input5.place(x=350,y=10)

button1=tk.Button(window,text="按我",command=btnClick)
button1.pack()
button1.place(x=10,y=70)

button2=tk.Button(window,text="清除畫布",command=clean)
button2.pack()
button2.place(x=75,y=70)

# text=tk.Text(window,width=56,height=19,bg='#FFCCCC',font=("標楷體",16))
# text.pack()
# text.place(x=15,y=100)
#---------------------
window3 = tk.Tk()
window3.title('prim-flow')
window3.geometry("640x480")

canvas2=tk.Canvas(window3,width=1500,height=1500,bg='#FFCCCC')
canvas2.pack()
canvas2.place(x=0,y=0)


ybar = tk.Scrollbar(window3,orient=tk.VERTICAL,command=canvas2.yview)
ybar.pack(fill=tk.Y, side=tk.RIGHT)
xbar = tk.Scrollbar(window3,orient=tk.HORIZONTAL,command=canvas2.xview)#orient=tk.HORIZONTAL直的滾
xbar.pack(fill=tk.X, side=tk.BOTTOM)

canvas2.config(yscrollcommand=ybar.set,xscrollcommand=xbar.set,scrollregion=(0,0,5000,5000))

tk.mainloop() 