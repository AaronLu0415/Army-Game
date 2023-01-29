



'''this is a game where you defend your base and invade the enemy's base.
    [w or right arrow key: Right]
    [a or left arrow key: Left  ]
    [s or down arrow key: Down  ]
    [w or up arrow key: Up      ]'''











import turtle
import math
wn = turtle.Screen()
wn.bgpic('gbackground.gif')
wn.bgcolor('gray')
wn.setup(width = 1.0, height = 1.0)
canvas = wn.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
wn.tracer(0)


class Sprite(turtle.Turtle):
    def __init__(self,shape, x , y, lives, range, bullets, damage):
        turtle.Turtle.__init__(self, shape, x, y, lives, range, bullets, damage)
        self.lives = lives
        self.range = range
        self.bullets = bullets
        self.damage = damage

    def move_left(self, speed):
        self.lt(speed)

    def move_right(self, speed):
        self.rt(speed)

    def turn_left(self, angle):
        self.left(angle)

    def turn_right(self, angle):
        self.right(angle)

    def go_forward(self, speed):
        self.forward(speed)

    def go_backward(self, speed):
        self.backward(speed)

    def is_collision(self, size1, size2, other):
        x = self.xcor()-other.xcor
        y = self.ycor()-other.ycor
        distance = math.sqrt((x**2)+(y**2))
        if distance < size1 + size2:
            return True
        else:
            return False

    def alive_check(self):
        if self.lives == 0:
            self.hideturtle()
            self.bullets = 0
            self.damage = 0
            self.range = 0
            self.goto(0 , 10000)


















wn.mainloop()