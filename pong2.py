import time
import readchar

WIDTH = 160
HEIGHT = 40 

#define left paddle coordinates
lpx = 5
lpy = 5
lph = 5

#define right paddle coordinates
rpx = 5
rpy = WIDTH - 5
rph = 5

#define ball    
bx = int(HEIGHT/2)
by = int(WIDTH/2)
bc = "o"

frame = list()
line = list()

def drawLeftPaddle(lpx, lpy, lph):
    global frame
    for i in range(lph):
        frame[lpx+i][lpy] = "|"

def drawRightPaddle(rpx, rpy, rph):
    global frame
    for i in range(rph):
        frame[rpx+i][rpy] = "|"

def drawBall(bx, by, bc):
    global frame
    frame[bx][by] = bc

def generateLine(w, char):
    line = list()
    for i in range(w):
       line.append(char)
    return line

def generateEmptyFrame(w, h):
    global frame
    for i in range(h): #loop through every row
        if i == 0:#if it is the first row
            line = generateLine(w, "_")
            frame.append(line)
        elif i == h-1:
            line = generateLine(w, "_")
            frame.append(line)
        else:
            line = generateLine(w, " ")
            frame.append(line)

def play():
    global lpx, lpy, lph, rpx, rpy, rph, bx, by, frame
    while(True):
        try: 
            key = readchar.readchar()
            if key == w:
                lpx -= 1
            elif key == s:
                lpx -= 1
        except:
            pass
            
        by += 1
        generateEmptyFrame(WIDTH, HEIGHT)
        drawLeftPaddle(lpx, lpy, lph)
        drawRightPaddle(rpx, rpy, rph)
        drawBall(bx, by, bc)
        printFrame()
        frame.clear()
        time.sleep(1)



def printFrame():
    global frame
    for i in range(len(frame)):
        line = "".join(frame[i])
        print(line)

play()
