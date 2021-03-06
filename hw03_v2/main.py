import turtle as t
t.speed(10)
#画国旗背景
def draw_rectangle(start_x,start_y,rec_x,rec_y):
    t.goto(start_x,start_y)
    t.color('red')
    t.fillcolor('red')
    t.begin_fill()
    for i in range(2):
        t.forward(rec_x)
        t.left(90)
        t.forward(rec_y)
        t.left(90)
    t.end_fill()
    
def draw_star(center_x,center_y,radius):
    t.setpos(center_x,center_y)
    pt1=t.pos()
    t.circle(-radius,72)
    pt2=t.pos()
    t.circle(-radius,72)
    pt3=t.pos()
    t.circle(-radius,72)
    pt4=t.pos()
    t.circle(-radius,72)
    pt5=t.pos()
#画五角星
    t.color('yellow','yellow')
    t.begin_fill()
    t.goto(pt3)
    t.goto(pt1)
    t.goto(pt4)
    t.goto(pt2)
    t.goto(pt5)
    t.end_fill()
t.penup()
#画长方形
star_x=-320
star_y=-260
len_x=600
len_y=400
draw_rectangle(star_x,star_y,len_x,len_y)
#大五角星
pice=len_x /30
big_center_x=star_x+5*pice
big_center_y=star_y+len_y-pice*5
t.goto(big_center_x,big_center_y)
t.left(90)
t.forward(pice*3)
t.right(90)
draw_star(t.xcor(),t.ycor(),pice*3)
#第一个小五角星
t.goto(star_x+10*pice,star_y+len_y-pice*2)
t.left(t.towards(big_center_x,big_center_y)-t.heading())
t.forward(pice)
t.right(90)
draw_star(t.xcor(),t.ycor(),pice)
#第二个小五角星
t.goto(star_x+pice*12,star_y+len_y-pice*4)
t.left(t.towards(big_center_x,big_center_y)-t.heading())
t.forward(pice)
t.right(90)
draw_star(t.xcor(),t.ycor(),pice)
#第三个小五角星
t.goto(star_x+pice*12,star_y+len_y-7*pice)
t.left(t.towards(big_center_x,big_center_y)-t.heading())
t.forward(pice)
t.right(90)
draw_star(t.xcor(),t.ycor(),pice)
#第四个小五角星
t.goto(star_x+pice*10,star_y+len_y-9*pice)
t.left(t.towards(big_center_x,big_center_y)-t.heading())
t.forward(pice)
t.right(90)
draw_star(t.xcor(),t.ycor(),pice)
