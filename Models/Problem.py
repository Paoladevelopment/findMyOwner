from Models.State import State

class Problem:

    def __init__(self, initial_state, goal_state, actions, enviroment, costs) -> None:
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.actions = actions
        self.enviroment = enviroment
        self.costs = costs

        self.initial_state.set_actions(self._get_allowed_actions(self.initial_state))
    
    def __str__(self) -> str:
        msg = "Estado inicial: {0} -> Objetivo: {1}"
        return msg.format(self.initial_state, self.goal_state)
    

    #Method used to know if we have reached our goal state

    def is_goal(self, state): 
        return state.row == self.goal_state.row and state.column == self.goal_state.column


    #Method used to obtain a new state based on a current state and an action.
    def get_sucessor_state(self, state, action):
        if action.value == "Go up":
            new_state = State(state.row-1, state.column, [])
            new_state.set_actions(self._get_allowed_actions(new_state))
            return new_state
        
        if action.value == "Go right":
            new_state = State(state.row, state.column + 1, [])
            new_state.set_actions(self._get_allowed_actions(new_state))
            return new_state
        
        if action.value == "Go down":
            new_state = State(state.row+1, state.column, [])
            new_state.set_actions(self._get_allowed_actions(new_state))
            return new_state
        
        if action.value == "Go left":
            new_state = State(state.row, state.column - 1, [])
            new_state.set_actions(self._get_allowed_actions(new_state))
            return new_state
    

    #Method used to obtain the allowed actions of the agent based on its current state
    def _get_allowed_actions(self,state):
        allowed_actions = []

        if state.row > 0:
            if(self.enviroment[state.row-1][state.column] != 5):
                allowed_actions.append(self.actions[0])
        
        if state.column < len(self.enviroment[0]) - 1 :
            if(self.enviroment[state.row][state.column+1] != 5):
                allowed_actions.append(self.actions[1])
        
        if state.row < len(self.enviroment) - 1:
            if(self.enviroment[state.row+1][state.column] !=5):
                allowed_actions.append(self.actions[2])
        
        if state.column > 0:
            if(self.enviroment[state.row][state.column-1] != 5):
                allowed_actions.append(self.actions[3])
        
        return allowed_actions
    
    #Returns the cost of the current state, how much did it take to get to the current state.
    def cost_action(self, state):
        return self.costs[self.enviroment[state.row][state.column]]

    #Returns the cost of the road from the current node to its root node
    def cost_road(self, node):
        total = 0
        while node.father:
            total += self.cost_action(node.state)
            node = node.father
        return total
