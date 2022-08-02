# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    state = problem.getStartState()
    pila = util.Stack() # In this case we use a stack (LIFO)
    pila.push((state, [])) # We add the first state and the path to that node.
    visitados = [] # A visited node list
    while pila.isEmpty() == False:
        x = pila.pop()
        if problem.isGoalState(x[0]):
            return x[1] # If we find the goal we return the path to the goal.
        else:
            if x[0] not in visitados:
                visitados.append(x[0]) # We add the node to visited if it has not been visited already.
                successors = problem.getSuccessors(x[0]) # We obtain the successors and check if each son has not been visited.
                for hijo in successors:
                    if hijo[0] not in visitados:
                        pila.push((hijo[0], x[1] + [hijo[1]])) # if not already visited we add it to the stack.
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Same as dps, this time using a queue instead of a stack:
    state = problem.getStartState()
    cola = util.Queue() 
    cola.push((state, [])) # In this case we use a queue (FIFO) with the state and the path to that state.
    visitados = []
    while cola.isEmpty() == False: # We iterate till we find the goal or the queue is empty.
        x = cola.pop()
        if problem.isGoalState(x[0]): # When we find the goal we return the path to that node.
            return x[1]
        else:
            if x[0] not in visitados: 
                visitados.append(x[0])
                successors = problem.getSuccessors(x[0])
                for hijo in successors:
                    if hijo[0] not in visitados:
                        cola.push((hijo[0], x[1] + [hijo[1]]))
    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Same as last two, this time using a priorityqueue and adding a cost.
    state = problem.getStartState()
    prio = util.PriorityQueue()
    prio.push((state, []), 0) # priority queue with the state, path to that state and the added cost to that state.
    visitados = []
    while prio.isEmpty() == False:
        x = prio.pop()
        if problem.isGoalState(x[0]):
            return x[1]
        else:
            if x[0] not in visitados:
                visitados.append(x[0])
                successors = problem.getSuccessors(x[0])
                for hijo in successors:
                    if hijo[0] not in visitados: # If the soon is not already visited we add it to the priority queue with the cost of getting there.
                        prio.push((hijo[0], x[1] + [hijo[1]]), problem.getCostOfActions(x[1] + [hijo[1]]))
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Same as priority queue but now f(n) = g(n) + h(n) where h(n) is the heuristic function.
    state = problem.getStartState()
    prio = util.PriorityQueue()
    prio.push((state, []), 0)
    visitados = []
    while prio.isEmpty() == False:
        x = prio.pop()
        if problem.isGoalState(x[0]):
            return x[1]
        else:
            if x[0] not in visitados:
                visitados.append(x[0])
                successors = problem.getSuccessors(x[0])
                for hijo in successors:
                    if hijo[0] not in visitados:
                        # To the cost we add the heuristic given the state and the problem, in this case nullHeuristic is used (trivial)
                        prio.push((hijo[0], x[1] + [hijo[1]]), problem.getCostOfActions(x[1] + [hijo[1]]) + heuristic(hijo[0], problem))
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
