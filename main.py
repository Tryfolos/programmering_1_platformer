#Importing stuff.
import pygame
import sys

#Initializing pygame.
pygame.init()


#Variables.
game_location = "main_menu"


#Main surface variables.
camera_cords = [0, 0]
room_size = [20000, 20000]
camera_size = [1920, 1080]
window_size = [1280, 720]

#Setting window icon.
icon = pygame.image.load("icon.jpg")
pygame.display.set_icon(icon)


#Setting up fonts.
font_antonio = pygame.font.Font("fonts/Antonio-Regular.ttf", 24)


#Main menu content
main_menu = pygame.Surface(camera_size)
main_menu.fill((100, 100, 255))


#Creating the three main surfaces.
room = pygame.Surface(room_size)
camera = pygame.Surface(camera_size)
window = pygame.display.set_mode(window_size)

#Time tracking object.
clock = pygame.time.Clock()

#Beginning of main game loop.
while True:

#Checking the time spent between frames.
	delta = clock.tick(100)

#Setting the window caption
	pygame.display.set_caption(f"Generic Platformer          Framerate: {clock.get_fps()}")


#Resetting camera surfaces each frame so that there will be no diplicates of frames.
	camera.fill((0, 0, 0))


#Event queue. Inputs are handeled here.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()


#Main menu.
	if game_location == "main_menu":

		

		#Blitting all the main menu content to camera.
		camera.blit(main_menu, (0, 0))


#Blitting the camera surface to the window surface.
	window.blit(pygame.transform.scale(camera, window_size), (0, 0))

#Updating the display
	pygame.display.update()