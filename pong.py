import tkinter as tk

#window size and setup
WIDTH,HEIGHT,PADDLEHEIGHT,PADDLEWIDTH=900,500,50, 2
BG,PADDLECOLOR="black","white"
MOVESPEED,FRAMELENGTH_MS=10,250

#set initial paddle positions and variables
Lx,Ly= 10, 10
Rx,Ry=WIDTH-10, 4

#ball initial position and size
Bx, By, = WIDTH/2, HEIGHT/2
BALLSIZE,BALLSPEED = 10, 25
BALLCOLOR = "white"
ballDirection=[-1,0]

p1score,p2score = 0,0

#create window and attach keys
root = tk.Tk()
root.title("Pong")
root.bind("<space>", lambda e: start())
root.bind("<Escape>", lambda e: end())
keys_held = set()
root.bind("<KeyPress>", lambda e: keys_held.add(e.keysym))
root.bind("<KeyRelease>", lambda e: keys_held.discard(e.keysym))

#create canvas and place on window
canvas=tk.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG)
canvas.pack()

canvas.create_text(WIDTH/2, HEIGHT/2, text="PLAY PONG Press space", fill=PADDLECOLOR, font=("Arial", 32)) 

def moveBall(direction):
    global Bx, By

    # set ball x speed
    if(direction[0]==1):
        Bx+=BALLSPEED
    elif(direction[0]==-1):
        Bx-=BALLSPEED

    #set ball y speed
    if(direction[1] == 1):
        By+=BALLSPEED
    elif(direction[1] ==-1):
        By-=BALLSPEED

    return

def animate():
    global ballDirection, p1score, p2score, Ly, Ry
    if "q" in keys_held:
        Ly -= MOVESPEED
    if "a" in keys_held:
        Ly += MOVESPEED
    if "p" in keys_held:
        Ry -= MOVESPEED
    if "l" in keys_held:
        Ry += MOVESPEED
    canvas.delete("all")

    #draw paddles
    canvas.create_rectangle(Lx, Ly, Lx+PADDLEWIDTH, Ly+PADDLEHEIGHT, fill=PADDLECOLOR)
    canvas.create_rectangle(Rx, Ry, Rx+PADDLEWIDTH, Ry+PADDLEHEIGHT, fill=PADDLECOLOR)  

    score = "GAME OVER!!! Player 1:" + str(p1score) + "Player 2: " + str(p2score)
    #check for loss
    if (Bx < PADDLEWIDTH or Bx > WIDTH): #ball is outside left or right. Game Ends
        score = "GAME OVER!!! Player 1:" + str(p1score) + "Player 2: " + str(p2score)
        canvas.create_text(WIDTH/2, HEIGHT/2, text=score, fill=PADDLECOLOR, font=("Arial", 32)) 
        return

    #check for paddle hit
    if (Bx == Lx and By > Ly and By < Ly + PADDLEHEIGHT): # check leftPaddle
        if (By < Ly + PADDLEHEIGHT/3):
            ballDirection=[1,-1]
        elif (By > Ly + (PADDLEHEIGHT/3)*2):
            ballDirection=[1,1]
        else:
            ballDirection=[1,0]

        moveBall(ballDirection)
        p1score+=1
    elif(Bx == Rx and By > Ry and By < Ry + PADDLEHEIGHT):# check right paddle
        if (By < Ry + PADDLEHEIGHT/3):
            ballDirection=[-1,-1]
        elif (By > Ry + (PADDLEHEIGHT/3)*2):
            ballDirection=[-1,1]
        else:
            ballDirection=[-1,0]

        moveBall(ballDirection)
        p2score+=1
    else: #continue moving
        moveBall(ballDirection)
    
    canvas.create_rectangle(Bx, By, Bx+BALLSIZE, By+BALLSIZE, fill=BALLCOLOR)

    #continue loop
    root.after(FRAMELENGTH_MS, animate)

def start():
    Bx, By, = WIDTH/2, HEIGHT/2
    ballDirection=[-1,0]
    p1score,p2score = 0,0
    animate()

def end():
    root.destroy()

root.mainloop()

