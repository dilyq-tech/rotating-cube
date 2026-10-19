import pygame
import math
pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Мой первый 3D куб")

cub = [
    
    (100, 100, 100),
    (-100, 100, 100),
    (-100, -100, 100),
    (100, -100, 100),
    
    
    (100, 100, -100),
    (-100, 100, -100),
    (-100, -100, -100),
    (100, -100, -100)
]


def project_3d_to_2d(x, y, z):
    scale = 400/(400+z)
    projected_x = x*scale+400
    projected_y = y*scale+300
    return projected_x,projected_y


edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),   
    (4, 5), (5, 6), (6, 7), (7, 4),   
    (0, 4), (1, 5), (2, 6), (3, 7)    
]  
faces = [
    [0, 1, 2, 3],  
    [4, 5, 6, 7],   
    [0, 1, 5, 4],   
    [3, 2, 6, 7],   
    [1, 2, 6, 5],   
    [0, 3, 7, 4],   
]

def rotate_3d(x, y, z, angle_x, angle_y):
    rad_x = math.radians(angle_x)
    rad_y = math.radians(angle_y)

    new_y = y * math.cos(rad_x) - z * math.sin(rad_x)
    new_z = y * math.sin(rad_x) + z * math.cos(rad_x)

    new_x = x * math.cos(rad_y) - new_z * math.sin(rad_y)
    new_z2 = x * math.sin(rad_y) + new_z * math.cos(rad_y)

    return (new_x, new_y, new_z2)
angle_x = 0
angle_y = 0
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False
    
    screen.fill((0, 0, 0))


    projected = []
    rotated = []   
    for x, y, z in cub:
        rx, ry, rz = rotate_3d(x, y, z, angle_x, angle_y)
        rotated.append((rx, ry, rz)) 
        px, py = project_3d_to_2d(rx, ry, rz)
        projected.append((px, py))

    faces_with_depth = []
    for face in faces:
        z_sum = 0
        for i in face:
            z_sum += rotated[i][2]    
        faces_with_depth.append((z_sum / 4, face))
    faces_with_depth.sort(reverse=True)
    for depth, face in faces_with_depth:
        points = [projected[i] for i in face]
        pygame.draw.polygon(screen, (100, 150, 250), points)
    for a,b in edges:
        pygame.draw.line(screen, (255, 255, 255), projected[a], projected[b], 2)
    pygame.display.flip()
    angle_x += 1
    angle_y += 2
    clock.tick(60)
pygame.quit()