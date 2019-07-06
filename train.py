from Game import Environment
from Game.Agents import TabularQAgent, RandomAgent


agent_1 = TabularQAgent()
agent_2 = RandomAgent()
test_env = Environment(agent_1, agent_2)

test_env.
