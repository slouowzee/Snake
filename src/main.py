import pygame
import sys
from game.constants import *
from game.snake import Snake
from game.food import Food

def draw_grid(screen):
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
                pygame.draw.line(screen, BORDER_COLOR, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
                pygame.draw.line(screen, BORDER_COLOR, (0, y), (WINDOW_WIDTH, y))

def show_score(screen, score):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'Score: {score}', True, SCORE_COLOR)
        screen.blit(score_text, (10, 10))

def game_over_screen(screen, score):
        font = pygame.font.Font(None, 74)
        text = font.render('Game Over!', True, SCORE_COLOR)
        score_text = font.render(f'Score: {score}', True, SCORE_COLOR)
        screen.blit(text, (WINDOW_WIDTH//2 - text.get_width()//2, WINDOW_HEIGHT//2 - 100))
        screen.blit(score_text, (WINDOW_WIDTH//2 - score_text.get_width()//2, WINDOW_HEIGHT//2 - 40))
        restart_rect, quit_rect = draw_buttons(screen)
        pygame.display.flip()
        return restart_rect, quit_rect

def draw_buttons(screen):
        font = pygame.font.Font(None, 36)
        restart_text = font.render('Restart', True, BACKGROUND_COLOR)
        quit_text = font.render('Quit', True, BACKGROUND_COLOR)
        restart_rect = pygame.Rect(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 + 50, 100, 50)
        quit_rect = pygame.Rect(WINDOW_WIDTH // 2 - 50, WINDOW_HEIGHT // 2 + 120, 100, 50)
        pygame.draw.rect(screen, SCORE_COLOR, restart_rect)
        pygame.draw.rect(screen, SCORE_COLOR, quit_rect)
        screen.blit(restart_text, (restart_rect.x + (restart_rect.width - restart_text.get_width()) // 2, restart_rect.y + (restart_rect.height - restart_text.get_height()) // 2))
        screen.blit(quit_text, (quit_rect.x + (quit_rect.width - quit_text.get_width()) // 2, quit_rect.y + (quit_rect.height - quit_text.get_height()) // 2))
        return restart_rect, quit_rect

def handle_events(snake, game_over, restart_rect=None, quit_rect=None):
        key_mapping = {
                pygame.K_UP: [0, -1],
                pygame.K_DOWN: [0, 1],
                pygame.K_LEFT: [-1, 0],
                pygame.K_RIGHT: [1, 0]
        }
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.KEYDOWN:
                        if not game_over and event.key in key_mapping:
                                snake.change_direction(key_mapping[event.key])
                        elif game_over and event.key == pygame.K_RETURN:
                                return 'restart'
                if event.type == pygame.MOUSEBUTTONDOWN and game_over:
                        mouse_pos = event.pos
                        if restart_rect and quit_rect:
                                if restart_rect.collidepoint(mouse_pos):
                                        return 'restart'
                                elif quit_rect.collidepoint(mouse_pos):
                                        pygame.quit()
                                        sys.exit()
        return None

def main():
        pygame.init()
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption('Snake Game')
        clock = pygame.time.Clock()
        restart_rect, quit_rect = None, None

        while True:
                snake = Snake(GRID_WIDTH // 4, GRID_HEIGHT // 2)
                foods = [Food()]
                score = 0
                game_over = False

                while not game_over:
                        action = handle_events(snake, game_over, restart_rect, quit_rect)
                        if action == 'restart':
                                break

                        snake.move()
                        snake.wrap_around()

                        for food in foods:
                                if snake.check_food_collision(food):
                                        score += 1
                                        if score % 25 == 0:
                                                foods.append(Food())

                        if snake.check_self_collision():
                                game_over = True

                        snake_speed = max(8 - (len(snake.body) // 25), 6)

                        screen.fill(BACKGROUND_COLOR)
                        draw_grid(screen)
                        snake.draw(screen)
                        for food in foods:
                                food.draw(screen)
                        if not game_over:
                                show_score(screen, score)
                        pygame.display.flip()
                        clock.tick(snake_speed)

                restart_rect, quit_rect = game_over_screen(screen, score)
                while True:
                        action = handle_events(snake, game_over, restart_rect, quit_rect)
                        if action == 'restart':
                                break

if __name__ == '__main__':
        main()