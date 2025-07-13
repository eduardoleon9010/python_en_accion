# main.py (código del juego):
import pygame
import random

# Inicialización de Pygame
pygame.init()

# Dimensiones de la pantalla
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Configuración de la pantalla
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Juego de Invasion")

# Reloj para controlar los FPS
clock = pygame.time.Clock()

# Cargar imágenes
player_image = pygame.image.load("assets/player.png")
enemy_image = pygame.image.load("assets/enemy.png")

# Ajuste de tamaño para la nave del jugador
player_image = pygame.transform.scale(player_image, (50, 50))  # Ajuste de tamaño para visualizar correctamente

# Cargar sonidos
try:
    shoot_sound = pygame.mixer.Sound("assets/shoot.wav")
    explosion_sound = pygame.mixer.Sound("assets/explosion.wav")
except pygame.error as e:
    print(f"Error al cargar el sonido: {e}")

# Función para mostrar texto
def show_text(text, size, color, x, y):
    font = pygame.font.SysFont(None, size)
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x, y))

# Función del menú
def game_menu():
    menu = True
    while menu:
        screen.fill(BLACK)
        show_text("Bienvenido al Juego de la Invasion", 50, WHITE, 100, 200)
        show_text("Presiona ESPACIO para iniciar", 30, WHITE, 200, 300)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    menu = False

# Función principal del juego
def game_loop():
    player_x = SCREEN_WIDTH // 2
    player_y = SCREEN_HEIGHT - 70
    player_speed = 10
    player_lives = 3  # Vidas del jugador

    # Lista de enemigos
    enemies = []
    enemy_spawn_time = 500  # Tiempo en milisegundos para que aparezca un nuevo enemigo
    enemy_last_spawn = pygame.time.get_ticks()

    # Ajuste de la velocidad de los enemigos
    enemy_speed = 5

    running = True
    score = 0
    max_score = 10  # Número de enemigos para ganar

    # Inicialización para disparos
    bullets = []  # Lista de balas disparadas por el jugador
    last_shot = pygame.time.get_ticks()  # Tiempo del último disparo
    bullet_cooldown = 300  # Tiempo de espera entre disparos

    paused = False  # Estado del juego pausado

    while running:
        screen.fill(BLACK)

        # Comprobación de pausa
        if paused:
            show_text("PAUSA", 50, WHITE, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                    paused = False  # Quitar pausa
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Comprobar si se pausa o no
            if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = True

        # Movimiento del jugador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - 50:
            player_x += player_speed

        # Dibuja el jugador
        screen.blit(player_image, (player_x, player_y))

        # Control de disparos
        current_time = pygame.time.get_ticks()
        if keys[pygame.K_SPACE] and current_time - last_shot > bullet_cooldown:
            bullet_x = player_x + player_image.get_width() // 2 - 2  # Centrado de la bala en el jugador
            bullet_y = player_y
            bullets.append([bullet_x, bullet_y])  # Añadir la bala a la lista
            shoot_sound.play()  # Reproducir sonido de disparo
            last_shot = current_time  # Actualizar el tiempo del último disparo

        # Movimiento de las balas
        for bullet in bullets:
            bullet[1] -= 10  # Velocidad de las balas
            if bullet[1] < 0:
                bullets.remove(bullet)  # Eliminar la bala si sale de la pantalla
            pygame.draw.rect(screen, WHITE, [bullet[0], bullet[1], 5, 10])  # Dibujar la bala

        # Aparición de nuevos enemigos
        if pygame.time.get_ticks() - enemy_last_spawn > enemy_spawn_time:
            enemy_x = random.randint(0, SCREEN_WIDTH - 50)
            enemy_y = random.randint(-150, -50)
            enemies.append([enemy_x, enemy_y])
            enemy_last_spawn = pygame.time.get_ticks()

        # Movimiento de los enemigos
        for enemy in enemies:
            enemy[1] += enemy_speed
            if enemy[1] > SCREEN_HEIGHT:
                enemies.remove(enemy)  # Eliminar el enemigo si sale de la pantalla
            
            # Colisión con el jugador
            if player_x < enemy[0] + 50 and player_x + 50 > enemy[0] and player_y < enemy[1] + 50 and player_y + 50 > enemy[1]:
                enemies.remove(enemy)
                player_lives -= 1  # El jugador pierde una vida
                if player_lives == 0:
                    running = False

            # Colisión entre enemigos y balas
            for bullet in bullets:
                if bullet[0] < enemy[0] + 50 and bullet[0] + 5 > enemy[0] and bullet[1] < enemy[1] + 50 and bullet[1] + 10 > enemy[1]:
                    enemies.remove(enemy)  # Eliminar el enemigo si lo golpea una bala
                    bullets.remove(bullet)  # Eliminar la bala
                    explosion_sound.play()  # Reproducir sonido de explosión
                    score += 1  # Incrementar puntuación
                    if score >= max_score:
                        running = False  # Ganar si alcanza la puntuación máxima
                    break

            # Dibuja enemigos
            screen.blit(enemy_image, (enemy[0], enemy[1]))

        # Mostrar puntuación y vidas
        show_text(f"Puntuación: {score}", 30, WHITE, 10, 10)
        show_text(f"Vidas: {player_lives}", 30, WHITE, SCREEN_WIDTH - 150, 10)

        pygame.display.update()
        clock.tick(60)

    # Pantalla de fin del juego
    if score >= max_score:
        show_win_screen()
    else:
        game_over()

# Función de pantalla de Game Over
def game_over():
    over = True
    while over:
        screen.fill(BLACK)
        show_text("Game Over", 50, RED, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50)
        show_text("Presiona ENTER para reiniciar", 30, WHITE, SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    over = False
                    game_menu()
                    game_loop()

# Función de pantalla de ganador
def show_win_screen():
    win = True
    while win:
        screen.fill(BLACK)
        show_text("¡Ganaste!", 50, GREEN, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 50)
        show_text("Presiona ENTER para reiniciar", 30, WHITE, SCREEN_WIDTH // 2 - 200, SCREEN_HEIGHT // 2 + 50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    win = False
                    game_menu()
                    game_loop()

# Iniciar el menú del juego
game_menu()
game_loop()

# Salir de Pygame
pygame.quit()
quit()
