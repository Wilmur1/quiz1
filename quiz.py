import pgzrun
import time
WIDTH = 600
HEIGHT = 450



welcome = Rect(90,5,485,50)
question = Rect(20,60,470,50)
answers1 = Rect(20,125,250,130)
answers2 = Rect(320,125,250,130)
answers3 = Rect(20,270,250,130)
answers4 = Rect(320,270,250,130)
skip = Rect(500,65,65,40)
timer = Rect(7,5,76,50)

time_limit = 10
questions = []

answers = [answers1,answers2,answers3,answers4]

def draw():
    screen.draw.filled_rect(welcome,"white")
    screen.draw.filled_rect(question,"white")
    i = 1
    for ans in answers:
       screen.draw.filled_rect(ans,"light blue")
       screen.draw.textbox(readnext1[i],ans,color = "dark blue")
       i = i + 1
    screen.draw.filled_rect(skip,"lime green")
    screen.draw.filled_rect(timer,"blue")
    screen.draw.textbox("Welcome to our Quiz!",welcome,color = "blue")
    screen.draw.textbox(readnext1[0],question,color = "green")
    screen.draw.textbox("SKIP",skip,color = "black")
    screen.draw.textbox(str(time_limit),timer,color = "white")

def read():
    global add
    global summm
    global questions
    questionsss = open("Quiz Game/Questions.txt", "r")
    for que in questionsss:
        questions.append(que)
    questionsss.close()
    print(questions)

read()
def on_mouse_down(pos):
    box = 1
    for ans in answers:
        if ans.collidepoint(pos):
            if box == int(readnext1[5]):
                correct()
            else:
                 wrong()
        box = box + 1
def correct():
    global readnext1
    global time_limit
    if questions:
       readnext1 = readnext()
       time_limit = 10
    else:
        finish()
def finish():
    global readnext1
    readnext1 = ["You Won","-","-","-","-","afs"]    

def wrong():
   global readnext1
   readnext1 = ["Game Over","-","-","-","-","afs"]    

def timeleft():
    global time_limit
    if time_limit:
      time_limit = time_limit -1
clock.schedule_interval(timeleft,1)

def readnext():
    return questions.pop(0).split(",")
readnext1 = readnext()
print(readnext1)



pgzrun.go()