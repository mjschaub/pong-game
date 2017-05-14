from Simulator.simulator import Simulator


if __name__ == "__main__":
    '''
    Runner code to start the training and game play.
    '''
    alpha_value = .05
    gamma_value = .95
    epsilon_value = .01
    num_games = 100000
    mySim = Simulator(num_games, alpha_value, gamma_value, epsilon_value)
    Simulator.train_agent(mySim,False)
    

    
    num_games = 5
    Simulator.change_parameters(mySim,0,num_games)
    Simulator.train_agent(mySim,True)

    num_games = 5
    Simulator.change_parameters(mySim,0,num_games)
    Simulator.train_agent(mySim,True)

    num_games = 5
    Simulator.change_parameters(mySim,0,num_games)
    Simulator.train_agent(mySim,True)
 
    num_games = 10
    Simulator.change_parameters(mySim,0,num_games)
    Simulator.train_agent(mySim,True)

    num_games = 10
    Simulator.change_parameters(mySim,0,num_games)
    Simulator.train_agent(mySim,True)


    num_games = 50
    Simulator.change_parameters(mySim,0,num_games)
    Simulator.train_agent(mySim,True)

    num_games = 100
    Simulator.change_parameters(mySim,0,num_games)
    Simulator.train_agent(mySim,True)

    '''
    num_games = 1000
    Simulator.change_parameters(mySim,0,num_games)
    Simulator.train_agent(mySim)
    '''
   
