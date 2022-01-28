import numpy as np
from numpy import random
from enum import Enum
from numpy.core.arrayprint import set_printoptions

from numpy.core.fromnumeric import shape, sort

# 0 <=> 1
# 2 <=> 3
# 4 <=> 5
class Color(Enum):
    Aqua = 0
    Red = 1 
    Blue = 2
    Green = 3
    White = 4
    Black = 5 
    Yellow = 6
    Purple = 7
    Brown = 8
    Pink = 9
    # Gray = 10
    # Orange = 11

class Cell:
    def __init__(self):
        self.number = 0
        self.cube = None
        self.opposite_cube = None
        self.opposite_color = None
        self.preveus_cell = None

    
    def __str__(self) :
        return self.number


class Cube:
    def __init__(self,weight):
        self.weight = weight
        self.colors = []
        self.set_colors()

    def set_colors(self):
        counter = 0
        # selected_color = random.choice(Color)
        selected_color = Color.Aqua
        while(counter < 6):
            flag = False
            # for i in self.colors:
            #     if (i == selected_color):
            #         flag= True
            if (flag == False):
                self.colors.append(selected_color)
                counter += 1

    def get_side(self,Color):
        for i in range(6):
            if (self.colors[i] == Color):
                return i

    def get_opposite_side(self , side_number):
        if (side_number == 0):
            return 1
        if (side_number == 1):
            return 0
        if (side_number == 2):
            return 3
        if (side_number == 3):
            return 2
        if (side_number == 4):
            return 5
        if (side_number == 5):
            return 4

    def get_color(self,side_number):
        return self.colors[side_number]

    def get_opposite_color(self,color):
        return self.get_color(self.get_opposite_side(self.get_side(color)))

    def print_cube(self):
        print("weight: " + str(self.weight),self.colors)
    
            
class Cube_Tower:
    def __init__(self,number_of_cubes):
        self.n = number_of_cubes
        self.cubes = []
        for i in range(number_of_cubes):
            self.cubes.append(Cube(random.randint(1,number_of_cubes*2)))
        random.shuffle(self.cubes)
        self.ground = self.set_ground()
        self.answer = [self.ground]
        self.storage = [[Cell() for i in range(len(Color))] for j in range(number_of_cubes) ]
        self.max_length = 0
        self.max_answer_cubes = []
        self.max_colors = []
        self.max_cube_sequence = []


    def print_cubes(self):
        for i in self.cubes:
            i.print_cube()
        print()

    def solve(self):
        self.cubes.sort( key = lambda x : x.weight)
        self.print_cubes()
        for i in range(self.n):
            for j in range(6):   # 6 sides
                flag = False
                max_index = 0
                max_magnutude = 0
                op_color = self.cubes[i].get_opposite_color(self.cubes[i].get_color(j)).value
                for k in range(i):
                    if (self.storage[k][op_color].number>max_magnutude):
                        max_magnutude = self.storage[k][op_color].number
                        max_index = k
                        flag = True
                if (flag == True):
                    self.storage[i][self.cubes[i].get_color(j).value].number = max_magnutude + 1 
                    self.storage[i][self.cubes[i].get_color(j).value].cube = self.cubes[i]
                    self.storage[i][self.cubes[i].get_color(j).value].opposite_cube = self.cubes[max_index]
                    self.storage[i][self.cubes[i].get_color(j).value].opposite_color = op_color
                    self.storage[i][self.cubes[i].get_color(j).value].preveus_cell = max_index

                else:
                    self.storage[i][self.cubes[i].get_color(j).value].number = 1
                    self.storage[i][self.cubes[i].get_color(j).value].cube = self.cubes[i]
        max_index_x = 0
        max_index_y = 0
        for i in range (len(Color)):
            for j in range(self.n):
                if (self.storage[j][i].number > self.max_length):
                    self.max_length = self.storage[j][i].number
                    max_index_x = i
                    max_index_y = j
        cell = self.storage[max_index_y][max_index_x]
        self.max_answer_cubes.append(cell.cube)
        self.max_colors.append((max_index_x))
        self.max_cube_sequence.append(max_index_y)
        for i in range(self.max_length-1):
            self.max_colors.append(cell.opposite_color)
            self.max_cube_sequence.append(cell.preveus_cell)
            cell = self.storage[cell.preveus_cell][cell.opposite_color]
            self.max_answer_cubes.append(cell.cube)


    def show_results(self):
        print("maximum length is: ", self.max_length)
        for i in range(self.max_length):
            print ("cube ",self.max_cube_sequence[i],"\tweight: ",self.max_answer_cubes[i].weight,"\tcolor: ", Color(self.max_colors[i]))

    def print_storage(self):
        for i in range (len(Color)):
            for j in range(self.n):
                print(self.storage[j][i].number , end ="\t")
            print()

    def print_answer(self):
        for i in self.answer:
            print(i)

    def set_ground(self):
        return random.choice(Color)





game = Cube_Tower(10)
game.print_cubes()
game.solve()
game.print_storage()
game.show_results()