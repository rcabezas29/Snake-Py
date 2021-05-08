import readchar
import os
import random

pos = [3, 1]
tail_len = 0
tail = []
map_width = 30
map_height = 20
death = False

objects = []
while len(objects) <= 5:
    new_obj_pos = [random.randint(0, map_width), random.randint(0, map_height)]
    if new_obj_pos not in objects and new_obj_pos != pos:
        objects.append(new_obj_pos)

while True:
    print("-" * (map_width + 2))
    for coor_y in range(map_height):
        print("|", end="")
        for coor_x in range(map_width):
            char_to_draw = " "
            for map_object in objects:
                if coor_x == map_object[0] and coor_y == map_object[1]:
                    char_to_draw = "*"
                    if coor_x == pos[0] and coor_y == pos[1]:
                        objects.remove(map_object)
                        new_obj_pos = [random.randint(0, map_width), random.randint(0, map_height)]
                        objects.append(new_obj_pos)
                        tail_len += 1
            if coor_x == pos[0] and coor_y == pos[1]:
                char_to_draw = "@"
            for tail_piece in tail:
                if tail_piece[0] == coor_x and tail_piece[1] == coor_y:
                    char_to_draw = "@"
                    if pos[0] == tail_piece[0] and pos[1] == tail_piece[1]:
                        death = True
            print(char_to_draw, end="")
        print("|")
    print("-" * (map_width + 2))

    direction = readchar.readchar().decode()

    tail.insert(0, pos.copy())
    tail = tail[:tail_len]

    if direction == "w":
        pos[1] -= 1
        if pos[1] < 0:
            pos[1] = map_height - 1
    elif direction == "s":
        pos[1] += 1
        if pos[1] > map_height:
            pos[1] = 1
    elif direction == "a":
        pos[0] -= 1
        if pos[0] < 0:
            pos[0] = map_width - 1
    elif direction == "d":
        pos[0] += 1
        if pos[0] > map_width:
            pos[0] = 1
    elif direction == "q":
        break
    os.system("cls")

    if death:
        print("GAME OVER")
        exit()
    if len(objects) == 0:
        print("YOU WIN!")
        exit()