class Node:

    def __init__(self, state, father = None, action = None, actions = None) -> None:
        self.state = state
        self.father = father
        self.action = action
        self.actions = actions
        self.children = []
        self.cost = 0
        self.best_child_cost = 0
    
    def __str__(self) -> str:
        return self.state
    
    
    #Method to generate new nodes based on its current node.
    def expand(self, problem):
        if not self.actions:
            return self.children
        
        for action in self.actions:
            new_state = problem.get_sucessor_state(self.state, action)
            child = Node(new_state, self, action, new_state.get_actions())
            cost = self.cost + problem.cost_action(child.state)
            child.cost = cost
            self.children.append(child)
    
        return self.children
    
    #Calculates the best cost of the child of the current node.
    def calculate_best_child_cost(self):
        if not self.children:
            return None
        
        best = self.children[0]

        for child in self.children[1:]:
            cost_best = best.cost
            child_cost = child.cost
            if(child_cost < cost_best):
                best = child

        self.best_child_cost = best.cost
