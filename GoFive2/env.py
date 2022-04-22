import gym
import numpy as np
from game import draw
import pygame

black_color = [0, 0, 0]
white_color = [255, 255, 255]
filled_color = [125,95,24]


EMPTY = 0
BLACK = 2
WHITE = 1


class Env(gym.Env):
    def __init__(self, display=True) -> None:
        self._board = [[]] * 15
        self.reset()
        self.reward_n = 3

        self.state_dim = 15*15
        self.action_dim = 2
        self.observation_space = gym.spaces.Box(
            low=0, high=1, shape=(self.state_dim,), dtype=np.float32
        )
        self.action_space = gym.spaces.Box(
            low=0, high=14, shape=(self.action_dim,), dtype=np.float32
        )
        self.display = display
        if self.display:
            pygame.init()
            pygame.display.set_caption("Go Five >>>>>") 

            self.screen = pygame.display.set_mode((640, 640))    # pygame.display.set_mode()表示建立个窗口，左上角为坐标原点，往右为x正向，往下为y轴正向
            self.screen.fill(filled_color)                        # 给窗口填充颜色，颜色用三原色数字列表表示
            draw(self, self.screen)          
            pygame.display.flip()                           # 刷新窗口显示
    
    def step(self, action):
        action = (round(action[0]), round(action[1]))
        if self.legal(action[0], action[1]):
            print("move rationally.")
            self.move(action[0], action[1], self.is_black)
            self.is_black = not self.is_black
            reward = self.reward()
            if self.display:
                self.screen.fill(filled_color)
                draw(self, self.screen)

                pygame.display.flip()
                pygame.time.wait(500)
                
        else:
            print("move randomly.")
            random_action = self.legal_moves[np.random.randint(len(self.legal_moves))]
            self.move(random_action[0], random_action[1], self.is_black)
            self.is_black = not self.is_black
            reward = -100
            if self.display:
                self.screen.fill(filled_color)
                draw(self, self.screen)

                pygame.display.flip()
                pygame.time.wait(500)

        # 对手走
        random_action = self.legal_moves[np.random.randint(len(self.legal_moves))]
        self.move(random_action[0], random_action[1], self.is_black)
        self.is_black = not self.is_black
        reward = -self.reward()
        if self.display:
            self.screen.fill(filled_color)
            draw(self, self.screen)

            pygame.display.flip()
            pygame.time.wait(500)


        return np.array(self._board).flatten(), reward, self.done(), dict()
    
    def reward(self):
        if self.done():
            return 10000
        else:
            return 1
    
    def reset(self):
        self.legal_moves = [(x, y) for x in range(15) for y in range(15)]
        self.is_black = True        # agent is black，黑棋先手
        for row in range(len(self._board)):
            self._board[row] = [EMPTY] * 15
        
        return np.array(self._board).flatten()



    def move(self, row, col, is_black):
        self._board[row][col] = BLACK if is_black else WHITE
        self.legal_moves.remove((row, col))

    
    def legal(self, row, col):
        return self._board[row][col] == EMPTY

    # 定义函数，传入当前棋盘上的棋子列表，输出结果，不管黑棋白棋胜，都是传回True，未出结果则为False
    def done(self, n_in_row=3):
        for n in range(15):
            # 判断垂直方向胜利
            flag = 0
            # flag是一个标签，表示连续相同颜色棋子的数量
            for b in self._board:
                if b[n] == BLACK:
                    flag += 1
                    if flag == n_in_row:
                        print('黑棋胜')
                        return True
                else:
                # else表示此时没有连续相同的棋子，标签flag重置为0
                    flag = 0
    
            flag = 0
            for b in self._board:
                if b[n] == WHITE:
                    flag += 1
                    if flag == n_in_row:
                        print('白棋胜')
                        return True
                else:
                    flag = 0
    
            # 判断水平方向胜利
            flag = 0
            for b in self._board[n]:
                if b == BLACK:
                    flag += 1
                    if flag == n_in_row:
                        print('黑棋胜')
                        return True
                else:
                    flag = 0
    
            flag = 0
            for b in self._board[n]:
                if b == WHITE:
                    flag += 1
                    if flag == n_in_row:
                        print('白棋胜')
                        return True
                else:
                    flag = 0
    
            # 判断正斜方向胜利
    
            for x in range(4, 25):
                flag = 0
                for i,b in enumerate(self._board):
                    if 14 >= x - i >= 0 and b[x - i] == BLACK:
                        flag += 1
                        if flag == n_in_row:
                            print('黑棋胜')
                            return True
                    else:
                        flag = 0
    
            for x in range(4, 25):
                flag = 0
                for i,b in enumerate(self._board):
                    if 14 >= x - i >= 0 and b[x - i] == WHITE:
                        flag += 1
                        if flag == n_in_row:
                            print('白棋胜')
                            return True
                    else:
                        flag = 0
    
            #判断反斜方向胜利
            for x in range(11, -11, -1):
                flag = 0
                for i,b in enumerate(self._board):
                    if 0 <= x + i <= 14 and b[x + i] == BLACK:
                        flag += 1
                        if flag == n_in_row:
                            print('黑棋胜')
                            return True
                    else:
                        flag = 0
    
            for x in range(11, -11, -1):
                flag = 0
                for i,b in enumerate(self._board):
                    if 0 <= x + i <= 14 and b[x + i] == WHITE:
                        flag += 1
                        if flag == n_in_row:
                            print('白棋胜')
                            return True
                    else:
                        flag = 0
    
        return False
 


        