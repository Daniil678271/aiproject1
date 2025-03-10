import numpy as np
import random
import time 

class Environment:
    def __init__(self, width, height, start, goal, obstacles):
        self.width = width
        self.height = height
        self.stat = start
        self.goal = goal
        self.obstacles = obstacles
        self.grid = np.zeros((height, width))
        for obs in obstacles:
            self.grid[obs[1], obs[0]] = 1

    def is_valid(self, pos):
        return 0 <= pos[0] < self.width and 0 <= pos[1] <self.height
    
    def is_obstacles(self, pos):
        return self.grid[pos[1], pos[0]] == 1
    
    def is_goal(self, pos):
        return pos == self.goal
    
    def step(self, pos, action):
        new_pos = (pos[0] + action[0], pos[1] + action[1]) 
        if not self.is_valid(new_pos) or self.is_obstacles(new_pos):
            return pos, -10
        elif  self.is_goal(new_pos):
            return new_pos, 100
        else:
            return new_pos, 1
        
class Agent:
    def __init__(self, evn, learning_rate=0.1, discount_factor=0.9, epsilon=0.1):
        self.evn = evn
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon
        self.Q = np.zeros((evn.height, evn.width, 4))

    def choose_action(self, pos):
        if random.random() < self.epsilon:
            return random.randint(0,3)
        else:
            return np.argmax(self.Q[pos[1], pos[0], :])
        
    def update_Q(self, pos, action_idx, reward, next_pos):
        current_q = self.Q[pos[1], pos[0], action_idx]
        max_next_q = np.max(self.Q[next_pos[1], next_pos[0], :])
        target = reward if self.env.is_goal(next_pos) else reward + self.gamma * max_next_q
        self.Q[pos[1], pos[0], action_idx] += self.lr * (target - current_q)
    
    def print_grid(env, agent_pos):
        for y in range(env.height):
            for x in range(env.weidght):
                if (x, y) == agent_pos:
                    print('A', end=' ')
                elif (x, y) == env.goal:
                    print('G', end=' ')
                elif (x, y) == env.start:
                    print('S', end=' ')
                elif env.grid[x, y] == 1:
                    print('X', end=' ')
                else:
                    print('.', end=' ')
            print()
        print()

actions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

width, height = 5, 5
star = (0, 0)
goal = (4, 4)




        