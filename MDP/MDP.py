import Math

class MDP:
    
    def __init__(self, 
                 ball_x=None,
                 ball_y=None,
                 velocity_x=None,
                 velocity_y=None,
                 paddle_y=None):
        '''
        Setup MDP with the initial values provided.
        '''
        self.create_state(
            ball_x=ball_x,
            ball_y=ball_y,
            velocity_x=velocity_x,
            velocity_y=velocity_y,
            paddle_y=paddle_y
        )
        
        # the agent can choose between 3 actions - stay, up or down respectively.
        self.actions = [0, 0.04, -0.04]
        self.isInFailState = False
    
    def create_state(self,
              ball_x=None,
              ball_y=None,
              velocity_x=None,
              velocity_y=None,
              paddle_y=None):
        '''
        Helper function for the initializer. Initialize member variables with provided or default values.
        '''
        self.paddle_height = 0.2
        self.ball_x = ball_x if ball_x != None else 0.5
        self.ball_y = ball_y if ball_y != None else 0.5
        self.velocity_x = velocity_x if velocity_x != None else 0.03
        self.velocity_y = velocity_y if velocity_y != None else 0.01
        self.paddle_y = 0.5
	self.shouldReward = False
    
    def simulate_one_time_step(self, action_selected):
        '''
        :param action_selected - Current action to execute.
        Perform the action on the current continuous state.
        '''

	self.shouldReward = False
	self.paddle_y+= actions[action_selected]
		
	if self.paddle_y < 0:
		self.paddle_y = 0
	elif self.paddle_y > 1-self.paddle_height:
		self.paddle_y = 1-self.paddle_height


        self.ball_x += self.velocity_x
        self.ball_y += self.velocity_y

        if ball_y < 0:
          ball_y = -1 * ball_y
          velocity_y = -1 * velocity_y
        elif ball_y > 1:
          ball_y = 2 - ball_y
          velocity_y = -1 * velocity_y
        if ball_x < 0:
          ball_x = -1 * ball_x
          velocity_x = -1 * velocity_x
        elif ball_x > 1 and ball_y-paddle_y < .2 :
        	#ball hit paddle, increment the reward by one
        	ball_x = 2 * paddle_x - ball_x
        	U = Math.random(-.015,.015)
        	V = Math.random(-.03,.03)
        	velocity_x = -velocity_x + U
        	velocity_y = velocity_y + V
		self.shouldReward = True
        	if Math.abs(velocity_x) < .03:
        		if velocity_x < 0:
            			velocity_x = -.03
          		else:
              			velocity_x = .03
	elif ball_x > 1: 
		#paddle missed ball and is in fail state
		self.isInFailState = True
        return self.shouldReward
    
    def discretize_state(self):
        '''
        Convert the current continuous state to a discrete state.
        '''

        '''
        Treat the entire board as a 12x12 grid, and let two states be considered the same if the
ball lies within the same cell in this table. Therefore there are 144 possible ball locations.
● Discretize the X-velocity of the ball to have only two possible values: +1 or -1 (the exact
value does not matter, only the sign).
● Discretize the Y-velocity of the ball to have only three possible values: +1, 0, or -1. It
should map to Zero if |velocity_y| < 0.015.
● Finally, to convert your paddle's location into a discrete value, use the following equation:
discrete_paddle = floor(12 * paddle_y / (1 - paddle_height)). In cases where paddle_y =
1 - paddle_height, set discrete_paddle = 11. As can be seen, this discrete paddle
location can take on 12 possible values.
● Add one special state for all cases when the ball has passed your paddle (ball_x > 1). This
special state needn't differentiate among any of the other variables listed above, i.e., as
long as ball_x > 1, the game will always be in this state, regardless of the ball's velocity
or the paddle's location. This is the only state with a reward of -1.
● Therefore, the total size of the state space for this problem is (144)(2)(3)(12)+1 = 10369.
        '''

	final_state = 0
	discretized_x = floor(self.ball_x * 12)
	discretized_y = floor(self.ball_y * 12)
	discrete_pos = discretized_x*discretized_y
	if self.velocity_x > 0:
		discrete_x_velocity = 0
	else:
		discrete_x_velocity = 1
	if Math.abs(self.velocity_y) < .015:
		discrete_y_velocity = 0
	elif self.velocity_y < 0:
		discrete_y_velocity = 1
	else:
		discrete_y_velocity = 2
	if self.paddle_y == 1-self.paddle_height:
		discrete_paddle = 11
	else:
		discrete_paddle = floor(12 * paddle_y / (1 - paddle_height))
	if isInFailState:
		discrete_fail = 1
	else:
		discrete_fail = 0	

	return (discrete_pos, discrete_x_velocity, discrete_y_velocity, discrete_paddle, discrete_fail)

