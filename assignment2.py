import turtle as t
t.pen()
t.bgcolor("black")
colors=["red","green","yellow","blue","gray","purple","aqua","brown"] 
name=t.textinput("enter your name","enter your name")
location=t.textinput("enter your address", "enter your address")
age=t.textinput("enter your age", "enter your age")
sides=int(t.numinput("number of sides","how many sides you want(1-20)",10,1,20)) 
for words in range(100):
    t.pencolor(colors[words%sides%5])
    t.penup()
    t.forward(words*5) 
    t.pendown()
    t.write(name,font=("",int((words*2+4)/4),"bold"))
    t.write(location,font=("", int((words*2+4)/4),"bold"))
    t.write(age, font=("", int((words*2+4)/4),"bold"))
    t.left(360/sides+12) 