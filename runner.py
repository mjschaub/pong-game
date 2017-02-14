from Simulator.simulator import Simulator

if __name__ == "__main__":
    '''
    Runner code to start the training and game play.
    '''
    alpha_value = .4
    gamma_value = .95
    epsilon_value = .04
    num_games = 100000
    Simulator(num_games, alpha_value, gamma_value, epsilon_value)
