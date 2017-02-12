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
        self.Q = zeros(3,10369)
        

    
    def f_function(self):
        '''
        Choose action based on an epsilon greedy approach
        :return action selected
        '''
        action_selected = None
        x = random()
        if x < self.epsilon_value:
            #act randomly
        else:
            #be greedy using current Q

        #update Q
        #Q_new = Q_old + self.alpha_value*error
        #error = R(s) + gamma * max Q(a',s') - Q(a,s)


        # Your Code Goes Here!
        
        return action_selected

    def train_agent(self):
        '''
        Train the agent over a certain number of games.
        '''
        for i in range(num_games):
            MDP(0.5, 0.5, 0.03, 0.01, 0.5 - paddle_height / 2)
            play_game()
            self.Q = zeros(3,10369)

        pass
    
    def play_game(self):
        '''
        Simulate an actual game till the agent loses.
        '''
        simulate_one_time_step()
        #discretize_step()
        pass