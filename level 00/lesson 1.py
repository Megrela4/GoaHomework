from turtle import *

#we want to paint a house

#step 1: draw a square
speed(30)
width(7)
color("purple")

begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

end_fill()

#end of square

#drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)    #height
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


#drawing a window

color("purple")
goto(0, 0)
color("purple")


#window 1 
begin_fill()
left(90)
left(90)
left(30)
forward(110)
color("blue")
right(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()


#window 2
color("purple")
goto(0, 0)




left(90)
forward(200)
left(90)
forward(110)
color("blue")

begin_fill()
left(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()


#drawing a field

left(90)
right(90)
color("purple")
forward(110)
right(90)
goto(0, 0)
color("green")

begin_fill()
forward(475)
right(90)
right(90)
forward(940)
right(90)
forward(390)
right(90)
forward(945)
right(90)
forward(390)
end_fill()


#drawing a tree

goto (0, 0)
color ("green")
left(90)
forward(220)
color("brown")
right(90)

width(25)
forward(100)
color("dark green")

begin_fill()
left(90)
forward(40)
right(90)
forward(50)
forward(50)
right(90)
forward(40)
forward(40)
right(90)
forward(50)
forward(50)
right(90)
forward(40)
end_fill()


#drawing a flowers

color("red")
left(90)
color("dark green")
forward(5)
color ("brown")
forward(99)
color ("green")
forward(70)
color("pink")
forward(1)
left(90)
color("green")
width(1)

forward(50)
color("pink")
width(25)
right(90)
forward(1)

left(90)
color("green")
width(1)

forward(50)
color("pink")
width(25)
right(90)
forward(1)

left(90)
color("green")
width(1)

forward(50)
color("pink")
width(25)
right(90)
forward(1)

left(90)
color("green")
width(1)

forward(50)
color("pink")
width(25)
right(90)
forward(1)


left(90)
color("green")
width(1)

forward(50)
color("pink")
width(25)
right(90)
forward(1)


left(90)
color("green")
width(1)

forward(50)
color("pink")
width(25)
right(90)
forward(1)


left(90)
color("green")
width(1)

forward(50)
color("pink")
width(25)
right(90)
forward(1)


left(90)
color("green")
width(1)

forward(50)
color("pink")
width(25)
right(90)
forward(1)



left(90)
color("green")
width(1)

forward(50)
color("pink")
width(25)
right(90)
forward(1)


left(90)
color("green")
width(1)

forward(50)
color("pink")
width(25)
right(90)
forward(1)


left(90)
color("green")
width(1)

forward(50)
color("pink")
width(25)
right(90)
forward(1) 




















exitonclick()