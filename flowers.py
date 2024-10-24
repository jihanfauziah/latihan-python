import turtle as tr

s = tr.Screen()

tr.setupz(800, 800)
s.bcolor("#262626")
tr.pencolor("#540d6e")
tr.speed(0)
tr.pensize(1)
col = ("#FF7F3F")

for i in range(3):
    for n in range(400):
        tr.color(col[n%4])
        tr.left(90)
        tr.circle(190-n/2,90)
        tr.color(col[n%4])
    tr.left(30)
    s.exitonclick()