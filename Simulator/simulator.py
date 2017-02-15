import numpy as np
import Math

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
        self.Q = zeros(3,12,2,3,12,1)
        

    
    def f_function(self):
        '''
        Choose action based on an epsilon greedy approach
        :return action selected
        '''
        action_selected = None #should be 0 for no move, 1 for up, or 2 for down
        x = np.random()
        if x < self.epsilon_value:
		action_selected = np.random.randint(low=0,high=2)	
        else:
	    #discretize step here?
		discrete = discretize_step()
		curr_state = Q[:,discrete[0],discrete[1],discrete[2],discrete[3],discrete[4]]
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
        for i in range(num_games):
            MDP(0.5, 0.5, 0.03, 0.01, 0.5 - paddle_height / 2)
            play_game()
            self.Q = zeros(3,12,2,3,12,1)

        pass
    
    def play_game(self):
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
			prev_tuple = discretize_step()
			prev_action = f_function()
        		shouldReward = simulate_one_time_step(prev_action)
        		new_tuple = discretize_step()
			#new_action = f_function()
        		if new_state[4] == 1:
				didLose = True
			
			max_state = Q[:,new_tuple[0],new_tuple[1],new_tuple[2],new_tuple[3],new_tuple[4]]
			#update Q
			max_val = -1
			max_Q = 0
        		for i in range(len(max_state)):
				if max_state[i] > max_val:
					max_val = max_state[i]
					max_Q = i
			
			if shouldReward:
				error = 1 + self.gamma_val * max_state[max_val] - Q[prev_action,prev_tuple[0],prev_tuple[1],prev_tuple[2],prev_tuple[3],prev_tuple[4]]
        			Q_new = self.Q + self.alpha_value*error
				self.Q = Q_new
			else:
				error = 0 + self.gamma_val * max_state[max_val] - Q[prev_action,prev_tuple[0],prev_tuple[1],prev_tuple[2],prev_tuple[3],prev_tuple[4]]
        			Q_new = self.Q + self.alpha_value*error
        			self.Q = Q_new




	pass
