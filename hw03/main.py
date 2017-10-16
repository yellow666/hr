
import turtle
import math

def draw_polygon(aTurtle, size=50, n=3):
##    绘制正多边形
##
##    args:
##        aTurtle: turtle对象实例
##        size: int类型，正多边形的边长
##        n: int类型，是几边形        
    
    for i in range(n):
        aTurtle.forward(size)
        aTurtle.left(360.0/n)

def draw_n_angle(aTurtle, size=50, num=5, color='yellow'):
    
    if color:
        aTurtle.begin_fill()
        aTurtle.fillcolor(color)
    for i in range(num):
        aTurtle.forward(size)
        aTurtle.left(360.0/num)
        aTurtle.forward(size)
        aTurtle.right(2*360.0/num)
    if color:
        aTurtle.end_fill()

def draw_5_angle(aTurtle='yellow', start_pos=(0,0), end_pos=(0,10), radius=100, color=None):
    
    aTurtle = aTurtle or turtle.Turtle()
    size = radius * math.sin(math.pi/5)/math.sin(math.pi*2/5)
    aTurtle.left(math.degrees(math.atan2(end_pos[1]-start_pos[1], end_pos[0]-start_pos[0])))
    aTurtle.penup()
    aTurtle.goto(start_pos)
    aTurtle.fd(radius)
    aTurtle.pendown()
    aTurtle.right(math.degrees(math.pi*9/10))
    draw_n_angle(aTurtle, size, 5, color)

def draw_5_star_flag(times=20.0):
  
    width, height = 30*times, 20*times
    # 初始化屏幕和海龟
    window = turtle.Screen()
    aTurtle = turtle.Turtle()
    aTurtle.hideturtle()
    aTurtle.speed(10)
    # 画红旗
    aTurtle.penup()
    aTurtle.goto(-width/2, height/2)
    aTurtle.pendown()
    aTurtle.begin_fill()
    aTurtle.fillcolor('red')
    aTurtle.fd(width)
    aTurtle.right(90)
    aTurtle.fd(height)
    aTurtle.right(90)
    aTurtle.fd(width)
    aTurtle.right(90)
    aTurtle.fd(height)
    aTurtle.right(90)    
    aTurtle.end_fill()
    # 画大星星
    draw_5_angle(aTurtle, start_pos=(-10*times, 5*times), end_pos=(-10*times, 8*times), radius=3*times, color='yellow')  
    # 画四个小星星
    stars_start_pos = [(-5, 8), (-3, 6), (-3, 3), (-5, 1)]
    for pos in stars_start_pos:
        draw_5_angle(aTurtle, start_pos=(pos[0]*times, pos[1]*times), end_pos=(-10*times, 5*times), radius=1*times, color='yellow')  
    # 点击关闭窗口
    window.exitonclick()

if __name__ == '__main__':
        draw_5_star_flag()
