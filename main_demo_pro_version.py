import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Giải trí với trò chơi chém những người bạn")

# Color
BACKGROUND = (214, 214, 214) # Màu background
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (147, 153, 35)
PURPLE = (255,0,255)
SKY = (0,255,255)
ORANGE = (255,125,25)
GRAPE = (100,25,125)
GRASS = (55,155,65)

running = True
clock = pygame.time.Clock() # Tạo FPS

bowl_x = 250
apple_y = 0
apple_x = random.randint(0, 600)
apple_drop = 3
score = 0

font = pygame.font.SysFont('Time New Roman', 50)
font_over = pygame.font.SysFont('Time New Roman', 100)

pygame.display.set_caption('Help Aquarius') # Tên chương trình

icon = pygame.image.load('fruit.png')
pygame.display.set_icon(icon) # Set logo

# Load hình ảnh nền
background_image = pygame.image.load("background.jpg")
background_image = pygame.transform.scale(background_image, (800, 600))  # Thay đổi kích thước hình ảnh

# Trái cây
image_fruit = "fruit.png"
image_fruit = pygame.image.load(image_fruit)
image_fruit = pygame.transform.scale(image_fruit, (50, 50))

image_fruit_die = "fruit_die.png"
image_fruit_die = pygame.image.load(image_fruit_die)
image_fruit_die = pygame.transform.scale(image_fruit_die, (50, 50))

shit = "ground_.png"
shit = pygame.image.load(shit)
shit = pygame.transform.scale(shit, (200, 40))

# Khởi tạo mixer
pygame.mixer.init()

# Load nhạc vào mixer
music = pygame.mixer.Sound("music_background.mp3")
music_sucess = pygame.mixer.Sound("success.mp3")
music_fail = pygame.mixer.Sound("fail.mp3")

# Phát nhạc (lặp lại -1 để phát vô tận)
music.play(-1)
                                                                        
while running:
	clock.tick(60)
	screen.fill(BACKGROUND)
	screen.blit(background_image, (0, 0))

	# ---- Draw interface ---- #


	# Vẽ máy chém
	bowl = pygame.draw.rect(screen, BLACK, (bowl_x, 550, 200, 1))
	screen.blit(shit, (bowl_x, 550-25))
	# Vẽ trái cây

	apple = pygame.draw.rect(screen, GREEN, (apple_x, apple_y, 5, 5))

	screen.blit(image_fruit, (apple_x-10, apple_y-25))


	# Giới hạn máy chém
	if bowl_x <= 0:
		bowl_x = 0
	if bowl_x >= 600:
		bowl_x = 600

	apple_y += apple_drop
	apple_x += random.randint(-10, 10)
	if apple_x <= 0:
		apple_x += 10
	if apple_x >= 600:
		apple_x -= 10

	# Rớt liên tục
	if apple_y > 700:
		apple_y = 0
		apple_x = random.randint(0, 600)


	# Vẽ nền
	ground = pygame.draw.rect(screen, BLACK, (0, 580, 800, 1))

	# Tính điểm
	if apple.colliderect(bowl):
		score += 1
		apple_y = 0
		apple_x = random.randint(0, 600)
		music_sucess.play()
	
	if apple.colliderect(ground):
		apple_drop = 0
		over_text = font_over.render('Game over', True, WHITE)
		music_fail.play()
		screen.blit(image_fruit_die, (apple_x-10, apple_y-25))
		screen.blit(over_text, (200, 200))

	score_text1 = font.render('Score:' + str(score), True, WHITE)
	screen.blit(score_text1, (5, 5))

	for event in pygame.event.get(): # Sự kiện

		# Đóng chương trình
		if event.type == pygame.QUIT:
			print('Quit program')
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				bowl_x -= 60
			if event.key == pygame.K_RIGHT:
				bowl_x += 60


	pygame.display.flip() # Show chương trình
pygame.quit()