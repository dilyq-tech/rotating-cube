import math
import time

def rotate_point(x,y, angle_degrees):
    angle_rad = math.radians(angle_degrees)


    new_x = x * math.cos(angle_rad) - y * math.sin(angle_rad)
    new_y = x * math.sin(angle_rad) + y * math.cos(angle_rad)
    return new_x,new_y

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

def rotate_3d(x, y, z, angle_x, angle_y):
    rad_x = math.radians(angle_x)
    rad_y = math.radians(angle_y)

    new_y = y * math.cos(rad_x) - z * math.sin(rad_x)
    new_z = y * math.sin(rad_x) + z * math.cos(rad_x)

    new_x = x*math.cos(rad_y) - new_z*math.sin(rad_y)
    new_z2 = x*math.sin(rad_y) + new_z*math.cos(rad_y)

    return (new_x, new_y, new_z2)

old_x,old_y = 10, 0
new_x, new_y = rotate_point(old_x,old_y,90)
print(f"Было: ({old_x}, {old_y}) ===> Стало: ({new_x:.2f}, {new_y:.2f})")

angle=0
while True:
    print("\033c", end="")
    print(f"=== Угол: {angle}° ===\n")


    for x,y,z in cub:
        new_x,new_y = rotate_point(x,y,angle)
        px, py = project_3d_to_2d(new_x, new_y, z)    
    
        print(f"Точка ({x:3}, {y:3}, {z:4}) ==> ({px:6.2f}, {py:6.2f})")  
    
    time.sleep(0.1)
    angle += 5 