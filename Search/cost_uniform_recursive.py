from Models.Node import Node

def create_node_root(problem):
    state_root = problem.initial_state
    node_root = Node(state_root, None, None, state_root.get_actions())
    return node_root


def cost_uniform_recursive(problem):
    node_root = create_node_root(problem)
    leaf = [node_root]
    visited = set()
    visited_times = {}
    for i in range(43):

        if not leaf:
            return None
        node = leaf.pop(0)
        print("current state ", node.state.__str__())
        if problem.is_goal(node.state):
            return node

        if not node.state.get_actions():
            continue
        
        update_visited_times(node, visited, visited_times)
        visited.add(node.state.__str__())

        print("Nodos visitados " ,visited)
        new_nodes = node.expand(problem)
        if(visited_times[node.state.__str__()] > 1):
            if (node.best_child != None):
                visited.add(node.best_child.state.__str__())
                remove_node(new_nodes, node.best_child)
                nodes_best_child = node.best_child.expand(problem)
                add_nodes(nodes_best_child, new_nodes, visited)


        print([new_node.state.__str__() for new_node in new_nodes])
        update_leaf(node, new_nodes, leaf, visited, visited_times)

        print("Leaf ahora mismo: ")
        print([node.state.__str__() for node in leaf])
        ordering_leaf(leaf)


#Decides how to update new nodes to the leaf based on two conditions:
def update_leaf(current_node,nodes, leaf, visited, visited_times):
    if len(leaf) == 0:
        add_nodes(nodes, leaf, visited)
        return
    next_node = leaf[0]
    if(should_forget_branch(next_node,nodes) and visited_times[current_node.state.__str__()] <= 1):
        current_node.calculate_best_child_cost()
        current_node.cost = current_node.best_child.original_cost
        current_node.children = []
        leaf.append(current_node)
        return
    
    add_nodes(nodes, leaf, visited)


#Adds new nodes to an existing list of node.
def add_nodes(new_nodes, nodes, visited):
    for node in new_nodes:
        if(not was_visited(node, visited)):
             nodes.append(node)

#Returns if the cost of the next_node is lower that the costs of children nodes of the current one. 
def should_forget_branch(next_node, nodes):
    decision = False
    for node in nodes:
        if node.cost > next_node.cost:
            decision = True
            break
    return decision


#Returns if a node has been visited
def was_visited(node, visited):
    return node.state.__str__() in visited

#Increments the times of a revisited node. 

def update_visited_times(node, visited, visited_times):
    if(was_visited(node, visited)):
        visited_times[node.state.__str__()] +=1
    else:
        visited_times[node.state.__str__()] = 1

#Removes a node from the recent created new nodes list

def remove_node(new_nodes, node_to_delete):

    for node in new_nodes:
        if node_to_delete.state.__str__() == node.state.__str__():
            new_nodes.remove(node)


# Show the solution that el perro cobarde should take to find his owner
def show_solution(goal):
    if not goal:
        print('There is not solution')
        return
    
    solution_path = []
    node = goal
    while node:
        msg= "Estado: {0}, Coste Total: {1}"
        state = node.state.__str__()
        cost_total = node.original_cost
        solution_path.append(msg.format(state, cost_total))
        if node.action:
            action = node.action.value
            cost_father = node.father.original_cost
            msg = "<--- {0} [{1}] --->"
            solution_path.append(msg.format(action, cost_father))
        node = node.father

    for step in reversed(solution_path):
        print(step)


#Returns a dictionary with a tuple of the coordinates of the next position of the dog cobarde.
def steps_solution(goal):
    if not goal:
        print('There is not solution')
        return
    
    number_step = 0
    steps = {}
    node = goal
    while node:
        state = node.state
        steps[number_step] = [state.row, state.column]
        number_step+=1
        node = node.father
    
    return traverse_steps(steps)


def traverse_steps(steps):
    number_step = 0
    traverse_steps = {}
    size_steps = len(steps) - 1
    for step in range(size_steps, -1, -1):
        traverse_steps[number_step] = steps[step]
        number_step+=1
    
    return traverse_steps


#Orders a list of nodes in place based on their 'cost' attribute.
def ordering_leaf(leaf):
    leaf.sort(key= lambda node: node.cost)