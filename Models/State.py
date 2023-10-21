class State:
    
    #State receives a list of actions that can be performed being in that  current state. 
    def __init__(self, row, column, actions) -> None:
        self.row = row
        self.column = column
        self.actions = actions
    
    def __str__(self) -> str:
        return f"({self.row}, {self.column})"
    
    
    def set_actions(self,actions):
        self.actions= actions
    
    def get_actions(self):
        return self.actions