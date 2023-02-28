from turtle import *
left(90)
pensize(10)
penup()
forward(100)
pendown()
pencolor("red")
begin_fill()
circle(70,230)
pensize(10)
pencolor("red")

pencolor("red",)
forward(140)
seth(40)
forward(135)
pencolor("red")
right(5)
circle(70,210)
pencolor("black")

seth(30)
fillcolor("red")
end_fill()
seth(-90)
pencolor("red")
pensize(3)
forward(50)
pencolor("black")

right(90)
forward(100)


write("mctf{Th3_0s1nt_m@stEr}", move=False, align="left", font=("Arial", 14, "normal"))

hideturtle()
done()