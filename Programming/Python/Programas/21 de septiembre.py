import turtle as t

# Configuración inicial
t.speed(0)  # Velocidad más rápida
t.bgcolor("skyblue")  # Fondo azul claro

# Dibuja el tallo
t.color("green")
t.penup()
t.goto(0, -200)
t.pendown()
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(200)
t.end_fill()

# Dibuja el capullo del tulipán
t.penup()
t.goto(0, 0)
t.pendown()
t.color("yellow")
t.begin_fill()
t.circle(50)
t.end_fill()

# Dibuja los pétalos del tulipán
t.color("red")
t.penup()
t.goto(0, 50)
t.pendown()
for _ in range(6):
    t.begin_fill()
    t.circle(25, 180)
    t.right(180)
    t.forward(25)
    t.right(180)
    t.circle(25, 180)
    t.end_fill()
    t.right(60)

# Cierra la ventana haciendo clic en ella
t.exitonclick()