import numpy as np
import pygame
import sys
import elipse
import matplotlib.pyplot as plt
from arrow import draw_arrow

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulador Ley de Coulomb")

# Unidades de conversión
metros_por_pixel = 800 / width  # Cada píxel representa metros
metros_por_segundo = 1  # Cada unidad de velocidad representa XXX metros/segundo
segundos_por_iteracion = 0.1  # Cada iteración representa 0.1 segundo

# Colores
background_color = (255, 255, 255)
ball_color1 = (255, 0, 0)  # Color de la primera esfera
ball_color2 = (0, 0, 255)  # Color de la segunda esfera

# Posiciones
posX = []
posY = []
speed = []
acc = []

# Clase para representar una esfera
class Ball:
    def __init__(self, x, y, radius, color, initial_velocity, mass, charge):
        self.position = np.array([x, y], dtype=float)  # Ensure position is represented as float
        self.mass = mass
        self.x = x
        self.y = y
        self.charge = charge
        self.radius = radius
        self.color = color
        self.velocity = np.array(initial_velocity, dtype=float)  # Velocidad en metros/segundo

    def draw(self):
        pygame.draw.circle(screen, self.color, (int(self.position[0]), int(self.position[1])), self.radius)

    def update_velocity(self, acceleration):
        # Actualizar la velocidad teniendo en cuenta la aceleración y el tiempo por iteración
        self.velocity += acceleration * segundos_por_iteracion

    def update_position(self):
        # Actualizar la posición en metros
        self.x += self.velocity[0] * segundos_por_iteracion * metros_por_segundo
        self.y += self.velocity[1] * segundos_por_iteracion * metros_por_segundo
        self.position += self.velocity * segundos_por_iteracion * metros_por_segundo
# Crear dos instancias de la esfera con velocidades iniciales en m/s
initial_velocity1 = [0, 0]  # [vx, vy] en m/s
initial_velocity2 = [0, 0]  # [vx, vy] en m/s

try:
    iniX0 = int(elipse.entry_constante1.get())
    iniY0 = int(elipse.entry_constante2.get())
    iniX1 = int(elipse.entry_constante3.get())
    iniY1 = int(elipse.entry_constante4.get())
    carga0 = float(elipse.entry_constante5.get())
    carga1 = float(elipse.entry_constante6.get())
except:
    iniX0 = elipse.constante1
    iniY0 = elipse.constante2
    iniX1 = elipse.constante3
    iniY1 = elipse.constante4
    carga0 = elipse.constante5
    carga1 = elipse.constante6

ball1 = Ball(iniX0, iniY0, 10, ball_color1 if carga0 > 0 else ball_color2, initial_velocity1, 1, carga0)
ball2 = Ball(iniX1, iniY1, 30, ball_color1 if carga1 > 0 else ball_color2, initial_velocity2, 100, carga1)

# Lista de las pelotas
balls = [ball1, ball2]

# Bucle principal
running = True
max_fps = 60  # Definimos una tasa máxima de cuadros por segundo
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False

    # Limpiar la pantalla
    screen.fill(background_color)
    posX.append(ball1.x)
    posY.append(ball1.y)
    speed.append(np.linalg.norm(ball1.velocity))

    # Calcular la dirección y magnitud de la fuerza
    distance = ball2.position - ball1.position
    distance_squared = np.dot(distance, distance)
    distance_magnitude = np.sqrt(distance_squared)

    if abs(distance_magnitude) > 20:
        force_direction = distance / distance_magnitude
        force_magnitude = (9 * 10**9) * ball1.charge * ball2.charge / distance_squared  # Magnitud de la fuerza

        # Aplicar la fuerza como un vector
        acceleration_ball1 = force_magnitude * -force_direction / ball1.mass
        acceleration_ball2 = -force_magnitude * -force_direction / ball2.mass

        # Actualizar la velocidad y posición
        ball1.update_velocity(acceleration_ball1)
        ball1.update_position()
        ball1.draw()

        ball2.update_velocity(acceleration_ball2)
        ball2.update_position()
        ball2.draw()
    else:
        running = False

    acc.append(np.linalg.norm(acceleration_ball1))
    force_draw = force_magnitude * 10

    #draw_arrow(screen, pygame.Vector2(ball1.x, ball1.y), pygame.Vector2(ball2.x, ball2.y), pygame.Color(0,255,0), force_draw, 2*force_draw, 2*force_draw)

    # Actualizar la pantalla
    pygame.display.flip()
    clock.tick(max_fps)  # Limitar la tasa de cuadros

# Salir del programa
fig, axes = plt.subplots(2, 2, figsize=(12, 12))
axes[0, 0].plot(np.linspace(0, len(posX) * segundos_por_iteracion, len(posX)), posX)
axes[0, 0].set(ylabel="PosiciónX (m)", title="PosiciónX vs Tiempo")
axes[0, 1].plot(np.linspace(0, len(posY) * segundos_por_iteracion, len(posY)), posY)
axes[0, 1].set(ylabel="PosiciónY (m)", title="PosiciónY vs Tiempo")
axes[1, 0].plot(np.linspace(0, len(speed) * segundos_por_iteracion, len(speed)), speed, color="green")
axes[1, 0].set(ylabel="Rapidez", title="Rapidez vs Tiempo")
axes[1, 1].plot(np.linspace(0, len(acc) * segundos_por_iteracion, len(acc)), acc, color="red")
axes[1, 1].set(ylabel="Aceleración", title="Aceleración vs Tiempo")
fig.supxlabel("Tiempo (s)")
fig.suptitle("Datos de la Bola 0")
plt.show()
pygame.quit()