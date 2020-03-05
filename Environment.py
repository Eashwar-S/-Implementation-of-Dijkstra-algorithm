

import pygame
import pygame.gfxdraw
import math


import time

pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

scale = 1
width= 300
height = 200

gameDisplay = pygame.display.set_mode((width*scale,height*scale))
gameDisplay.fill(black)
display_surface = pygame.display.get_surface()
display_surface.blit(pygame.transform.flip(display_surface, False, True), dest=(0, 0))

# pixAr = pygame.PixelArray(gameDisplay)
# pixAr[10][20] = green

# pygame.draw.line(gameDisplay, blue, (100,200), (300,450),5)
#
# pygame.draw.rect(gameDisplay, white, (90*scale,40*scale,20*scale,20*scale))
# #
pygame.draw.circle(gameDisplay, white, (225*scale, height-150*scale), 25*scale)

pygame.draw.polygon(gameDisplay, white, ((20,height-120),(25,height-185),(75,height-185),(100,height-150),(75,height-120),(50,height-150)))

pygame.draw.polygon(gameDisplay, white, ((225,height-10),(200,height-25),(225,height-40),(250,height-25)))

pygame.draw.polygon(gameDisplay, white, ((30,height-67),(35,height-76),(100,height-38),(95,height-30)))

pygame.draw.ellipse(gameDisplay, white, (110,80,80,40))

# def check_Obstacle(x, y):
# #   For square
#     if x>=90 and x<=110 and y>=40 and y<=60:
#         print("Obstacle Detected")
#         return  True
# #   For Circle
#     if (x-160)**2 + (y-50)**2 < 15**2:
#         print("Obstacle Detected")
#         return True
#     else:
#         print("No Obstacle Detected")
#         return False

# if check_Obstacle(109,60):
#     print("Obstacle detected!!")
# else:
#     print("No Obstacle!!")
def draw_Start_and_Goal_Nodes(x,y):
    pygame.gfxdraw.pixel(gameDisplay,x,y,red)
    pygame.display.update()

def draw_Explored_Nodes(x,y):
    pygame.gfxdraw.pixel(gameDisplay,x,y,green)
    pygame.display.update()

def draw_Optimal_Nodes(x, y):
    pygame.gfxdraw.pixel(gameDisplay, x, y, blue)
    pygame.display.update()
    # return None
# for  x in range (50):
#     for y in range (100):
#         draw_Explored_Nodes(x,y)
        # time.sleep()

###############     Get color
# gameDisplay.get_at(x,y)


def calculate_Triangle_Area(x1,y1,x2,y2,x3,y3):
    area_of_whole_triangle = (abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2)
    return area_of_whole_triangle

def get_Line_Equation(A,B,x,y):
    x1,y1 = A
    x2,y2 = B
    # print("x1", x1)
    # print("x2", x2)
    # print("y1", y1)
    # print("y2", y2)
    # print("x", x)
    # print("y", y)
    if y1==y2:
        line_equation = y - y2
        return line_equation
    if x1==x2:
        line_equation = x - x2
        return line_equation
    line_equation = (y-y2)-((x-x2)*(y1-y2))/(x1-x2)
    # print("en3############3",(y-50)-((x-100)*(15-50))/(75-100))
    return line_equation

def check_Obstacle(x,y):
    ########################  For circle  #############################
    if (x - 225) ** 2 + ( height-y- 150) ** 2 <= 25 ** 2:
        print("Obstacle Detected in circle")
        return True
    #########################  For ellipse  #############################
    # p=0
    # checking the equation of
    # ellipse with the given point
    p = ((math.pow((x - 150), 2) / math.pow(40, 2)) +
         (math.pow(( height - y - 100), 2) / math.pow(20, 2)))
    print("P:",p)
    if p<=1:
        print("Obstacle Detected in ellipse")
        return True


    # polygon_coordinates = [(20,height - 120),(25,height - 185),(75,height-185),(100,height-150),(75,height-120),(50,height - 150)]
    parallelogram_coordinates = [(200,height-25),(225,height-40),(250,height-25),(225,height-10)]
    rectangle_coordinates = [(30,height-67),(35,height-76),(100,height-38),(95,height- 30)]

    triangle_1_coordinates = [(20,height - 120),(25,height - 185), (50, height - 150)]
    triangle_2_coordinates = [(25,height - 185),(75,height - 185), (50, height - 150)]
    triangle_3_coordinates = [(75,height - 185),(100,height -150), (50, height - 150)]
    triangle_4_coordinates = [(100,height-150), (75,height-120),   (50, height - 150)]

    half_plane_val_tri1= []
    for i in range(len(triangle_1_coordinates)):
        if i == len(triangle_1_coordinates)-1:
            half_plane_val_tri1.append(get_Line_Equation(triangle_1_coordinates[i], triangle_1_coordinates[0], x, y))
            break
        half_plane_val_tri1.append(get_Line_Equation(triangle_1_coordinates[i],triangle_1_coordinates[i+1],x,y))

    if (half_plane_val_tri1[0]>=0 and half_plane_val_tri1[1]>=0  and
        half_plane_val_tri1[2]<=0 ):
        print("Obstacle Detected in triangle 1 of polygon.")
        return True


    half_plane_val_tri2 = []
    for i in range(len(triangle_2_coordinates)):
        if i == len(triangle_2_coordinates) - 1:
            half_plane_val_tri2.append(get_Line_Equation(triangle_2_coordinates[i], triangle_2_coordinates[0], x, y))
            break
        half_plane_val_tri2.append(get_Line_Equation(triangle_2_coordinates[i], triangle_2_coordinates[i + 1], x, y))

    if (half_plane_val_tri2[0] >= 0 and half_plane_val_tri2[1] <= 0 and
            half_plane_val_tri2[2] <= 0):
        print("Obstacle Detected in triangle 2 of polygon.")
        return True


    half_plane_val_tri3 = []
    for i in range(len(triangle_3_coordinates)):
        if i == len(triangle_3_coordinates) - 1:
            half_plane_val_tri3.append(get_Line_Equation(triangle_3_coordinates[i], triangle_3_coordinates[0], x, y))
            break
        half_plane_val_tri3.append(get_Line_Equation(triangle_3_coordinates[i], triangle_3_coordinates[i + 1], x, y))

    if (half_plane_val_tri3[0] >= 0 and half_plane_val_tri3[1] <= 0 and
            half_plane_val_tri3[2] >= 0):
        print("Obstacle Detected in triangle 3 of polygon.")
        return True


    half_plane_val_tri4 = []
    for i in range(len(triangle_4_coordinates)):
        if i == len(triangle_4_coordinates) - 1:
            half_plane_val_tri4.append(get_Line_Equation(triangle_4_coordinates[i], triangle_4_coordinates[0], x, y))
            break
        half_plane_val_tri4.append(get_Line_Equation(triangle_4_coordinates[i], triangle_4_coordinates[i + 1], x, y))

    if (half_plane_val_tri4[0] <= 0 and half_plane_val_tri4[1] <= 0 and
            half_plane_val_tri4[2] >= 0):
        print("Obstacle Detected in triangle 4 of polygon.")
        return True


    half_plane_val_parallelogram = []
    for i in range(len(parallelogram_coordinates)):
        if i == len(parallelogram_coordinates) - 1:
            half_plane_val_parallelogram.append(get_Line_Equation(parallelogram_coordinates[i], parallelogram_coordinates[0], x, y))
            break
        half_plane_val_parallelogram.append(get_Line_Equation(parallelogram_coordinates[i], parallelogram_coordinates[i + 1], x, y))
    if (half_plane_val_parallelogram[0] >= 0 and half_plane_val_parallelogram[1] >= 0 and
        half_plane_val_parallelogram[2] <= 0 and half_plane_val_parallelogram[3] <= 0 ):
        print("Obstacle Detected in parallelogram")
        return True


    half_plane_val_rectangle = []
    for i in range(len(rectangle_coordinates)):
        if i == len(rectangle_coordinates) - 1:
            half_plane_val_rectangle.append(
                get_Line_Equation(rectangle_coordinates[i], rectangle_coordinates[0], x, y))
            break
        half_plane_val_rectangle.append(
            get_Line_Equation(rectangle_coordinates[i], rectangle_coordinates[i + 1], x, y))
    if (half_plane_val_rectangle[0] >= 0 and half_plane_val_rectangle[1] >= 0 and
            half_plane_val_rectangle[2] <= 0 and half_plane_val_rectangle[3] <= 0):
        print("Obstacle Detected in rectangle")
        return True
    else:
        print("No Obstacle Detected")
        return False



# def check_Obstacle(x,y):
#  #########################  For circle  #############################
#     if (x - 225) ** 2 + ( height-y- 150) ** 2 <= 25 ** 2:
#         print("Obstacle Detected in circle")
#         return True
#  #########################  For ellipse  #############################
#     # p=0
#     # checking the equation of
#     # ellipse with the given point
#     p = ((math.pow((x - 150), 2) / math.pow(40, 2)) +
#          (math.pow(( height - y - 100), 2) / math.pow(20, 2)))
#     print("P:",p)
#     if p<=1:
#         print("Obstacle Detected in ellipse")
#         return True
#
#     #########################  For Polygon  ############################
#     totalArea1 = calculate_Triangle_Area(20,height - 120,50,height - 150,25,height - 185)
#     area11= calculate_Triangle_Area(x,y,50,height - 150,25,height - 185)
#     area21 = calculate_Triangle_Area(20,height - 120,x, y, 25, height - 185)
#     area31 = calculate_Triangle_Area( 20,height - 120,50, height - 150, x, y)
#     if area11+area21+area31 == totalArea1:
#         print("Obstacle Detected in polygon1")
#         return True
#     totalArea2 = calculate_Triangle_Area(75, height - 185, 50, height - 150, 25, height - 185)
#     area12 = calculate_Triangle_Area(x, y, 50, height - 150, 25, height - 185)
#     area22 = calculate_Triangle_Area(75, height - 185, x, y, 25, height - 185)
#     area32 = calculate_Triangle_Area(75, height - 185, 50, height - 150, x, y)
#     if area12 + area22 + area32 == totalArea2:
#         print("Obstacle Detected in polygon2")
#         return True
#     totalArea3 = calculate_Triangle_Area(75, height - 185, 50, height - 150, 100, height - 150)
#     area13 = calculate_Triangle_Area(x, y, 50, height - 150, 100, height - 150)
#     area23 = calculate_Triangle_Area(75, height - 185, x, y, 100, height - 150)
#     area33 = calculate_Triangle_Area(75, height - 185, 50, height - 150, x, y)
#     if area13 + area23 + area33 == totalArea3:
#         print("Obstacle Detected in polygon3")
#         return True
#     totalArea4 = calculate_Triangle_Area(75, height - 120, 50, height - 150, 100, height - 150)
#     area14 = calculate_Triangle_Area(x, y, 50, height - 150, 100, height - 150)
#     area24 = calculate_Triangle_Area(75, height - 120, x, y, 100, height - 150)
#     area34 = calculate_Triangle_Area(75, height - 120, 50, height - 150, x, y)
#     if area14 + area24 + area34 == totalArea4:
#         print("Obstacle Detected in polygon4")
#         return True
# ############################## For Parallelogram    ###############################
#     totalArea5 = calculate_Triangle_Area(200, height - 25, 225, height - 40, 225, height - 10)
#     area15 = calculate_Triangle_Area(x, y, 225, height - 40, 225, height - 10)
#     area25 = calculate_Triangle_Area(200, height - 25, x, y, 225, height - 10)
#     area35 = calculate_Triangle_Area(200, height - 25, 225, height - 40, x, y)
#     if area15 + area25 + area35 == totalArea5:
#         print("Obstacle Detected in parallel1")
#         return True
#     totalArea6 = calculate_Triangle_Area(250, height - 25, 225, height - 40, 225, height - 10)
#     area16 = calculate_Triangle_Area(x, y, 225, height - 40, 225, height - 10)
#     area26 = calculate_Triangle_Area(250, height - 25, x, y, 225, height - 10)
#     area36 = calculate_Triangle_Area(250, height - 25, 225, height - 40, x, y)
#     if area16 + area26 + area36 == totalArea6:
#         print("Obstacle Detected in parallel2")
#         return True
#
# ########################### For Inclined Rectangle   ###############################
#
#     totalArea7 = calculate_Triangle_Area(30, height - 67, 35, height - 76, 100, height - 38)
#     area17 = calculate_Triangle_Area(x, y, 35, height - 76, 100, height - 38)
#     area27 = calculate_Triangle_Area(30, height - 67, x, y, 100, height - 38)
#     area37 = calculate_Triangle_Area(30, height - 67, 35, height - 76, x, y)
#     if area17 + area27 + area37 == totalArea7:
#         print("Obstacle Detected in rect 1")
#         return True
#     totalArea8 = calculate_Triangle_Area(30, height - 67, 95, height - 30, 100, height - 38)
#     area18 = calculate_Triangle_Area(x, y, 95, height - 30, 100, height - 38)
#     area28 = calculate_Triangle_Area(30, height - 67, x, y, 100, height - 38)
#     area38 = calculate_Triangle_Area(30, height - 67, 95, height - 30, x, y)
#     if area18 + area28 + area38 == totalArea8:
#         print("Obstacle Detected in rect 2")
#         return True
#     else:
#         print("No Obstacle Detected")
#         return False



