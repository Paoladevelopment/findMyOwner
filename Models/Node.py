class Node:

    def __init__(self, state, father = None, action = None, actions = None) -> None:
        self.state = state,
        self.father = father
        self.action = action
        self.actions = actions
        self.children = []
    
    def __str__(self) -> str:
        return self.state
    
    
    #Method to generate new nodes based on its current node.
    def expand(self, problem):
        if not self.actions:
            return self.children
        
        for action in self.actions:
            new_state = problem.get_sucessor_state(self.state, action)
            child = Node(new_state, self, action, new_state.get_actions())
            self.children.append(child)
    
        return self.children

