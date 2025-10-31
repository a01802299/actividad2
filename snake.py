# Descripcion: Juego Snake con modificaciones ligeras al gameplay
# Autores: Armando Vasquez Ambrocio | A01669283
#          Diana Karen Barrales Victorio | A018022299
# Fecha de modificacion: 30/10/2025


from turtle import *
from random import randrange, choice
from freegames import square, vector

# Configuracion de colores alteatorios para serpiente y comida
colores = ['black', 'blue', 'green', 'purple', 'orange']

snake_color= choice(colores)
food_color = choice([c for c in colores if c!= snake_color])

# Inicializacion de vectores 
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Cambia la direccion del movimiento de la serpiente
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

# Verifica si la cabeza de la serpiente se encuentra dentro de los limites. Regresa true si esta dentro del area.
def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

# Mueve a la serpiente un segmendo hacia enfrente
def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    move_food()

    clear()

    for body in snake:
        square(body.x, body.y, 9,snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)

# Desplaza la comida un paso aleatorio mientras la serpiete avanza
def move_food():
    steps = [(10, 0), (-10, 0), (0, 10), (0, -10)]
    candidates = []

    for dx, dy in steps:
        nxt = food.copy()
        nxt.move(vector(dx, dy))

        if inside(nxt) and nxt not in snake:
            candidates.append(nxt)

    if candidates:
        nxt = choice(candidates)
        food.x, food.y = nxt.x, nxt.y

# Configuracion de ventana
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()

# Controles
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
