from Simulator.simulator import Simulator


if __name__ == "__main__":
    '''
    Runner code to start the training and game play.
    '''
    alpha_value = .8
    gamma_value = .95
    epsilon_value = 0#.08
    num_games = 1000
    mySim = Simulator(num_games, alpha_value, gamma_value, epsilon_value)
    Simulator.train_agent(mySim)
