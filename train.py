from Environment.Environment import Environment
from Environment.Agents.TabularQAgent import TabularQAgent
from Environment.Agents.RandomAgent import RandomAgent


agent_1 = RandomAgent(side='X')
agent_2 = TabularQAgent(side='O')
test_env = Environment(agent_1, agent_2)

test_env.train(1000)
# agent_2.save_values()
