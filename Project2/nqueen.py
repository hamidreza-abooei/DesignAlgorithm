import numpy as np
from numpy.lib.function_base import copy
import matplotlib.pyplot as plt

class Board:

    def __init__(self,n):
        self.n = n
        self.board = np.zeros(shape=(n,n),dtype="int8")
        self.answers = []
        self.answer_numbers = 0

    def is_wallable(self,a,b):
        if (self.board[a,b] == 1):
            return False
        return True

    def add_wall(self,a,b):
        self.board[a,b] = 1 # 1 for wall
    
    def add_random_walls(self,number_of_random_walls):
        for i in range(number_of_random_walls):
            while (True):
                a,b = np.random.randint(0,self.n-1,2)
                if (self.is_wallable(a,b)):
                    self.add_wall(a,b)
                    break

    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
                print(self.board[i][j],end=" ")
            print("",end="\n")

    def queen_placement_success(self,a,b):
        if (self.board[a,b] != 0): ## Wall or sth
            return False
        return True
    def add_queen(self, a,b):
        if (self.queen_placement_success==False):
            return False
        self.board[a,b] = 2 # 2 for queen 
        for i in range(a+1,self.n): ## down
            if (self.board[i,b] == 1):
                break
            self.board[i,b] = 3 

        for i in range(a-1,-1,-1): ## up
            if (self.board[i,b] == 1):
                break
            self.board[i,b] = 3 

        for j in range(b+1,self.n): ## right
            if (self.board[a,j] == 1):
                break
            self.board[a,j] = 3 

        for j in range(b-1,-1,-1): ## left
            if (self.board[a,j] == 1):
                break
            self.board[a,j] = 3 
        for i in range(1,self.n): ## right down
            if ( a+i >= self.n):
                break
            if ( b+i >= self.n):
                break
            if (self.board[a+i,b+i] == 1):
                break
            self.board[a+i,b+i] = 4

        for i in range(1,self.n): ## left up
            if ( a-i < 0):
                break
            if ( b-i < 0):
                break
            if (self.board[a-i,b-i] == 1):
                break
            self.board[a-i,b-i] = 4

        for i in range(1,self.n): ## right up
            if ( a-i < 0):
                break
            if ( b+i >= self.n):
                break
            if (self.board[a-i,b+i] == 1):
                break
            self.board[a-i,b+i] = 4
        
        for i in range(1,self.n): ## left down
            if ( a+i >= self.n):
                break
            if ( b-i < 0):
                break
            if (self.board[a+i,b-i] == 1):
                break
            self.board[a+i,b-i] = 4
        return True
        
    def get_state(self):
        return copy(self.board)
    
    def set_state(self , state):
        self.board = state

    def place_queen(self,queen_number):
        if (queen_number == self.n):
            for i in range(self.n):
                for j in range(self.n):
                    if (self.queen_placement_success(i,j)):
                        state = self.get_state()
                        self.add_queen(i,j)
                        flag = False
                        for k in range (self.answer_numbers):
                            if (((self.get_state()*(self.get_state()==2)) ==( self.answers[k]*(self.answers[k]==2))).all()):
                                # print("a")
                                flag = True
                                break
                        if (flag == False):
                            self.answers.append(self.get_state())
                            self.answer_numbers +=1
                            self.print_board()
                            print(self.answer_numbers)
                        self.set_state(state)

        if ((queen_number < self.n) & (queen_number > 1)):
            for i in range(self.n): 
                for j in range(self.n):
                    if (self.queen_placement_success(i,j)):
                        state = self.get_state()
                        self.add_queen(i,j)
                        self.place_queen(queen_number+1)
                        self.set_state(state)

        if (queen_number == 1):             # this is for limiting the number of total searches 
            for i in range(self.n): 
                for j in range(self.n):
                    if (self.queen_placement_success(i,j)):
                        state = self.get_state()
                        self.add_queen(i,j)
                        self.place_queen(queen_number+1)
                        self.set_state(state)

    def look_for_answer(self):
        self.place_queen(1)

    def get_number_of_answers(self):
        return self.answer_numbers

    def get_answers(self):
        return copy(self.answers)
    def display_answer(self,state,title_text):
        plt.figure()
        plt.imshow(-0.5*state*(state == 2)+-2*state * (state == 1),cmap = "gray")
        plt.title(title_text)
        ax = plt.gca()
        ax.set_xticks(np.arange(-.5, self.n, 1), minor=True)
        ax.set_yticks(np.arange(-.5, self.n, 1), minor=True)
        ax.grid(which='minor')

    def display(self):
        plt.show()

    def random_answer_display(self,number_displayed_answers):
        if (self.get_number_of_answers()<number_displayed_answers): # display all 
            for i in range(self.get_number_of_answers()):
                self.display_answer(self.get_answers()[i],"answer number: " + str(i))
            self.display()
        else:
            counter = 0
            answer = []
            while (counter < number_displayed_answers): # display random answers 
                a = np.random.randint(0,self.get_number_of_answers()-1)
                if a not in answer:
                    answer.append(a)
                    counter += 1
            for i in answer:
                self.display_answer(self.get_answers()[i],"answer number: " + str(i))
            self.display()



a = Board(8)
# a.add_random_walls(4)
a.print_board()

a.look_for_answer()
# print(a.get_number_of_answers())
a.random_answer_display(5)



