from tkinter import *
root=Tk()
def record():
    pass
def restart_func():
    global state,boad,stop,cont
    stop=False
    cont=0
    state=[[0,0,0],[0,0,0],[0,0,0]]
    for i in range(3):
        for a in range(3):
            boad[i][a].configure(text="",bg="#00a")
            state[i][a]=0
            
            
def check_winner():
    global stop
    for v in range(3):
         if state[v][0]==state[v][1]==state[v][2] !=0:
             stop=True
             boad[v][0].configure(bg="#a00")
             boad[v][1].configure(bg="#a00")
             boad[v][2].configure(bg="#a00")
    for h in range(3):
        if state[0][h]==state[1][h]==state[2][h] !=0:
            

             stop=True
             boad[0][h].configure(bg="#a00")
             boad[1][h].configure(bg="#a00")
             boad[2][h].configure(bg="#a00")
    if state[0][0]==state[1][1]==state[2][2] !=0:
        stop=True
        boad[0][0].configure(bg="#a00")
        boad[1][1].configure(bg="#a00")
        boad[2][2].configure(bg="#a00")
    if state[0][2]==state[1][1]==state[2][0] !=0:
        stop=True
        boad[2][0].configure(bg="#a00")
        boad[1][1].configure(bg="#a00")
        boad[0][2].configure(bg="#a00")

def count():
    global player
    count=0
    for a in range(3):
        for b in range(3):
            if state[a][b]==player:
                count+=1
    return count
    
    
def funct(r,c):
    global boad,state,cont,player,P1_score,P2_score,stop,move
    if count()<3 and state[r][c]==0 and stop==False and cont==0:
        boad[r][c].configure(text=player)
        state[r][c]=player
        if player=="X":
            player="O"
        else:
            player="X"
        check_winner()
    elif state[r][c]==player and stop==False:
        boad[r][c].configure(text="")
        state[r][c]=0
        move.append((r,c))
        check_winner()
    if stop==True and cont==0:
        global score
        cont=1
        if player=="O":
           P1_score+=1
        elif player=="X":
            P2_score+=1
        score.configure(text=str(P1_score)+"----"+str(P2_score),font=("Times New Roman",10,"italic bold"))
        root.update()
   

state=[[0,0,0],[0,0,0],[0,0,0]]
boad=[[0,0,0],[0,0,0],[0,0,0]]
label=Label(text="3 Dam",font=("Arial",19,"italic bold underline")).grid(row=0,columnspan=3,column=0)
for r in range(len(boad)):
    for c in range(len(boad[0])):
        boad[r][c]=Button(width=28,height=7,bg="#00b",highlightcolor="#000",command=lambda rr=r,cc=c:funct(rr,cc),fg="gold")
        boad[r][c].grid(row=r+1,column=c)
player="X"
con=0
stop=False
restart=Button(width=28,text="RESTART",bg="#a00",command=restart_func).grid(row=5,column=1)
P1_score=0
P2_score=0
score=Label(root,bg="#0a0",text=str(P1_score)+"----"+str(P2_score))
score.place(x=360,y=27)
cont=0
move=[]
root.geometry("500x600")
root.mainloop()



