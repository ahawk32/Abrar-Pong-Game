import pygame
import sys

pygame.init()
pygame.font.init()

# Game constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
BALL_SIZE = 10
PADDLE_SPEED = 6
BALL_SPEED = 4

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()

# Text rendering
font = pygame.font.Font(None, 36)
text = font.render("Abrar's Pong Game", True, (255, 255, 255))
text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 20))

def draw_paddle(paddle_rect):
    pygame.draw.rect(screen, (255, 255, 255), paddle_rect)

def draw_ball(ball_rect):
    pygame.draw.ellipse(screen, (255, 255, 255), ball_rect)

def main():
    player_paddle = pygame.Rect(10, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    cpu_paddle = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = pygame.Rect(SCREEN_WIDTH // 2 - BALL_SIZE // 2, SCREEN_HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

    ball_speed_x = BALL_SPEED
    ball_speed_y = BALL_SPEED

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_paddle.top > 0:
            player_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and player_paddle.bottom < SCREEN_HEIGHT:
            player_paddle.y += PADDLE_SPEED

        # CPU paddle AI
        if cpu_paddle.centery < ball.centery and cpu_paddle.bottom < SCREEN_HEIGHT:
            cpu_paddle.y += PADDLE_SPEED
        if cpu_paddle.centery > ball.centery and cpu_paddle.top > 0:
            cpu_paddle.y -= PADDLE_SPEED

        # Ball collision
        if ball.colliderect(player_paddle) or ball.colliderect(cpu_paddle):
            ball_speed_x = -ball_speed_x
        if ball.top <= 0 or ball.bottom >= SCREEN_HEIGHT:
            ball_speed_y = -ball_speed_y

        ball.x += ball_speed_x
        ball.y += ball_speed_y

        if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
            ball.x = SCREEN_WIDTH // 2 - BALL_SIZE // 2
            ball.y = SCREEN_HEIGHT // 2 - BALL_SIZE // 2
            ball_speed_x = -ball_speed_x

        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)
        draw_paddle(player_paddle)
        draw_paddle(cpu_paddle)
        draw_ball(ball)
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
