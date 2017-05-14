import numpy as np
import math
from MDP.MDP import MDP
from graphics import *

class Simulator:
    
    def __init__(self, num_games=0, alpha_value=0, gamma_value=0, epsilon_value=0):
        '''
        Setup the Simulator with the provided values.
        :param num_games - number of games to be trained on.
        :param alpha_value - 1/alpha_value is the decay constant.
        :param gamma_value - Discount Factor.
        :param epsilon_value - Probability value for the epsilon-greedy approach.
        '''
        self.num_games = num_games       
        self.epsilon_value = epsilon_value       
        self.alpha_value = alpha_value       
        self.gamma_val = gamma_value
        self.Q = np.zeros((3,144,2,3,12,1))
	self.arr_states = []
        

    
    def f_function(self, mdpInstance):
        '''
        Choose action based on an epsilon greedy approach
        :return action selected
        '''
        action_selected = None #should be 0 for no move, 1 for up, or 2 for down
        x = np.random.random()
        if x < self.epsilon_value:
		action_selected = np.random.randint(low=0,high=2)	
        else:
		discrete = MDP.discretize_state(mdpInstance)
		curr_state = self.Q[:,int(discrete[0]),discrete[1],discrete[2],int(discrete[3]),discrete[4]]
		max_val = -1
        	for i in range(len(curr_state)):
			if curr_state[i] > max_val:
				max_val = curr_state[i]
				action_selected = i
				

        return action_selected

    def train_agent(self):
        '''
        Train the agent over a certain number of games.
        '''
	win = GraphWin('Pong game',500, 500)
	ball_count = 0
        for i in range(self.num_games):
        	mdpInstance = MDP(0.5, 0.5, 0.03, 0.01, 0.5 - .2/2, win)
        	self.play_game(mdpInstance)
        	ball_count += MDP.get_ball_count(mdpInstance)
	win.close()	
	
		
	print("average: ",float(ball_count)/float(self.num_games))
        pass
    
    def play_game(self, mdpInstance):
        '''
        Simulate an actual game till the agent loses.
        '''
	'''initial_state = discretize_step
	new_action = f_function()
	simulate_one_time_step(new_action)
	new_state = discretize_step()
	'''
	didLose = False
	while didLose is False:
		prev_tuple = MDP.discretize_state(mdpInstance)
		self.arr_states.append(prev_tuple)
		prev_action = self.f_function(mdpInstance)
       		shouldReward = MDP.simulate_one_time_step(mdpInstance,prev_action)
        	new_tuple = MDP.discretize_state(mdpInstance)

        	if new_tuple[4] == 1:
			error = -1 + self.gamma_val * 0 - self.Q[prev_action,int(prev_tuple[0]),prev_tuple[1],prev_tuple[2],int(prev_tuple[3]),prev_tuple[4]]
        		self.Q[prev_action,int(prev_tuple[0]),prev_tuple[1],prev_tuple[2],int(prev_tuple[3]),prev_tuple[4]] += self.alpha_value*error
			didLose = True
			break

		max_state = self.Q[:,int(new_tuple[0]),new_tuple[1],new_tuple[2],int(new_tuple[3]),new_tuple[4]]
		
		#update Q
		max_val = -1
		max_Q = 0
        	for i in range(len(max_state)):
			if max_state[i] > max_val:
				max_val = max_state[i]
				max_Q = i
		
		if shouldReward:
			error = 1 + self.gamma_val * max_val - self.Q[prev_action,int(prev_tuple[0]),prev_tuple[1],prev_tuple[2],int(prev_tuple[3]),prev_tuple[4]]
        		self.Q[prev_action,int(prev_tuple[0]),prev_tuple[1],prev_tuple[2],int(prev_tuple[3]),prev_tuple[4]] += self.alpha_value*error	
		else:
			error = 0 + self.gamma_val * max_val - self.Q[prev_action,int(prev_tuple[0]),prev_tuple[1],prev_tuple[2],int(prev_tuple[3]),prev_tuple[4]]
        		self.Q[prev_action,int(prev_tuple[0]),prev_tuple[1],prev_tuple[2],int(prev_tuple[3]),prev_tuple[4]] += self.alpha_value*error
        		

	


	pass



    def change_parameters(self,epsilon,num_games):
	self.epsilon_value = epsilon
	self.num_games = num_games



