###############################
# Homework 1 - Group 8: Scaravetti Alessio, Sterpin Enrico, Radinovic Jovana
# Part 1 Exercise 3
# We want to implement a simple reflex agent for the vacuum enironment and run
# all the possible configurations and agent locations.
# We want to keep track of the performance of the agent and calculate the average 
# performance for each configuration.
# We'll start with the agent at location A and run all the possible environment 
# configurations
###############################

from agents import *
from notebook import psource

from itertools import product

# Definition of the possible states
states = ['Dirty', 'Clean']

# Creation of a list with all the posssible combinations
possible_configurations = list(product(states, repeat=2))

#Modified class of TrvialVacuumEnvironment
class FixedVacuumEnvironment(Environment):
    """This environment has two locations, A and B. Each can be Dirty
    or Clean. The agent perceives its location and the location's
    status. This serves as an example of how to implement a simple
    Environment."""

    def __init__(self):
        super().__init__()

    def thing_classes(self):
        return [Wall, Dirt, ReflexVacuumAgent, RandomVacuumAgent, TableDrivenVacuumAgent, ModelBasedVacuumAgent]

    def percept(self, agent):
        """Returns the agent's location, and the location status (Dirty/Clean)."""
        return agent.location, self.status[agent.location]

    def execute_action(self, agent, action):
        """Change agent's location and/or location's status; track performance.
        Score 10 for each dirt cleaned; -1 for each move."""
        if action == 'Right':
            agent.location = loc_B
            agent.performance -= 1
        elif action == 'Left':
            agent.location = loc_A
            agent.performance -= 1
        elif action == 'Suck':
            if self.status[agent.location] == 'Dirty':
                agent.performance += 10
            self.status[agent.location] = 'Clean'
    
#Definition of the possible locations
loc_A = (0, 0)
loc_B = (1, 0)

#Definiton of the simple reflex agent
def SimpleReflexAgentProgram():
    """This agent takes action based solely on the percept."""
    
    def program(percept):
        loc, status = percept
        return ('Suck' if status == 'Dirty' 
                else'Right' if loc == loc_A 
                            else'Left')
    return program

#Simple reflex agent the two-state environment
program = SimpleReflexAgentProgram()
simple_reflex_agent = Agent(program)

vacuum_env=FixedVacuumEnvironment()
vacuum_env.add_thing(simple_reflex_agent)
#Variable used for the average performance
perf=0

#We set loc_A as the initial location and we run all the possible environment combinations
print("++++++LOCATION A++++++")

for i in possible_configurations:
    vacuum_env.status={loc_A: (i[0]), loc_B:(i[1])}
    #Check the current state of the environment
    print("State of the Environment: {}.".format(vacuum_env.status))
    
    simple_reflex_agent.location= loc_A
    #Check the current state of the agent
    print("SimpleReflexVacuumAgent is located at {}.".format(simple_reflex_agent.location))

    # Run the environment until the agent checked all locations and cleaned them
    while(vacuum_env.status[loc_A]=='Dirty' or vacuum_env.status[loc_B]=='Dirty' or simple_reflex_agent.location == loc_A):
        vacuum_env.step()

    # Check the current state of the environment
    print("State of the Environment: {}.".format(vacuum_env.status))

    #Check the current state of the agent
    print("SimpleReflexVacuumAgent is located at {}.".format(simple_reflex_agent.location))

    perf+=simple_reflex_agent.performance
    #Print out the performance
    print("Performance {}.".format(simple_reflex_agent.performance))
    simple_reflex_agent.performance=0
    print("----------------")

#Average performance
print("Average performance A: ", perf/len(possible_configurations) )

print("\n")
#We set loc_B as the initial location and we run all the possible environment combinations
print("++++++LOCATION B++++++")
perf=0

for i in possible_configurations:
    vacuum_env.status={loc_A: (i[0]), loc_B:(i[1])}
    #Check the current state of the environment
    print("State of the Environment: {}.".format(vacuum_env.status))
    
    simple_reflex_agent.location= loc_B
    #Check the current state of the agent
    print("SimpleReflexVacuumAgent is located at {}.".format(simple_reflex_agent.location))

    # Run the environment until the agent checked all locations and cleaned them
    while(vacuum_env.status[loc_A]=='Dirty' or vacuum_env.status[loc_B]=='Dirty' or simple_reflex_agent.location == loc_B):
        vacuum_env.step()

    # Check the current state of the environment
    print("State of the Environment: {}.".format(vacuum_env.status))
    #Check the current state of the agent
    print("SimpleReflexVacuumAgent is located at {}.".format(simple_reflex_agent.location))

    perf+=simple_reflex_agent.performance
    #Print out the performance
    print("Performance {}.".format(simple_reflex_agent.performance))
    simple_reflex_agent.performance=0
    print("----------------")

#Average performance
print("Average performance B: ", perf/len(possible_configurations) )