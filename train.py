from Game.Environment import Environment
from Game.Agents.TabularQAgent import TabularQAgent
from Game.Agents.RandomAgent import RandomAgent


agent_1 = TabularQAgent(side='X')
agent_2 = RandomAgent(side='O')
test_env = Environment(agent_1, agent_2)

test_env.train()
