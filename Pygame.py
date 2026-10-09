import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 30
PLAYER_SPEED = 5
TREE_SIZE = 50
TREE_COUNT = 15
FPS = 60

# Colors
GREEN = (34, 139, 34)
PLAYER_COLOR = (255, 200, 150)
TREE_COLOR = (139, 69, 19)
LEAF_COLOR = (0, 100, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Forest Explorer")
clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_SIZE, PLAYER_SIZE)
        
    def move(self, dx, dy, obstacles):
        # Move horizontal
        self.rect.x += dx
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle):
                if dx > 0:
                    self.rect.right = obstacle.left
                if dx < 0:
                    self.rect.left = obstacle.right
        
        # Move vertical
        self.rect.y += dy
        for obstacle in obstacles:
            if self.rect.colliderect(obstacle):
                if dy > 0:
                    self.rect.bottom = obstacle.top
                if dy < 0:
                    self.rect.top = obstacle.bottom

    def draw(self, surface):
        pygame.draw.rect(surface, PLAYER_COLOR, self.rect)
        # Simple head
        pygame.draw.circle(surface, (0, 0, 0), (self.rect.centerx, self.rect.top), 5)

class Tree:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TREE_SIZE, TREE_SIZE)
        
    def draw(self, surface):
        # Trunk
        trunk_rect = pygame.Rect(self.rect.x + TREE_SIZE // 3, self.rect.y + TREE_SIZE // 2, TREE_SIZE // 3, TREE_SIZE // 2)
        pygame.draw.rect(surface, TREE_COLOR, trunk_rect)
        # Leaves
        pygame.draw.circle(surface, LEAF_COLOR, (self.rect.centerx, self.rect.y + TREE_SIZE // 3), TREE_SIZE // 2)

def main():
    player = Player()
    trees = []
    
    # Generate random trees, ensuring they don't overlap with player starting position
    for _ in range(TREE_COUNT):
        while True:
            tx = random.randint(0, SCREEN_WIDTH - TREE_SIZE)
            ty = random.randint(0, SCREEN_HEIGHT - TREE_SIZE)
            tree = Tree(tx, ty)
            if not tree.rect.colliderect(player.rect.inflate(100, 100)):
                trees.append(tree)
                break
                
    tree_rects = [tree.rect for tree in trees]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        dx, dy = 0, 0
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            dx = -PLAYER_SPEED
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            dx = PLAYER_SPEED
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            dy = -PLAYER_SPEED
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            dy = PLAYER_SPEED

        # Normalize diagonal movement speed
        if dx != 0 and dy != 0:
            dx *= 0.707
            dy *= 0.707

        player.move(dx, dy, tree_rects)

        # Keep player in bounds
        player.rect.clamp_ip(screen.get_rect())

        # Draw
        screen.fill(GREEN)
        for tree in trees:
            tree.draw(screen)
        player.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
