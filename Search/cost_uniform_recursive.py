from Models.Node import Node

def create_node_root(problem):
    state_root = problem.initial_state
    node_root = Node(state_root, None, None, state_root.get_actions())
    return node_root


def cost_uniform_recursive(problem):
    node_root = create_node_root(problem)
    leaf = [node_root]
    visited = set()

    while True:
        if not leaf:
            return None
        node = leaf.pop(0)
        if problem.is_goal(node.state):
            return node
        visited.add(node.state.__str__())
        if not node.state.get_actions():
            continue

        print("current state ", node.state.__str__())
        childrens_node = node.expand(problem)
        node.calculate_best_child_cost()

        print([child_node.state.__str__() for child_node in childrens_node])
        for child_node in childrens_node:
            if(child_node.state.__str__() not in visited):
                leaf.append(child_node)

        leaf.sort(key= lambda node: node.cost)
        for node in leaf:
            print(node.state)


def show_solution(goal):
    if not goal:
        print('There is not solution')
        return
    
    solution_path = []
    node = goal
    while node:
        msg= "Estado: {0}, Coste Total: {1}"
        state = node.state.__str__()
        cost_total = node.cost
        solution_path.append(msg.format(state, cost_total))
        if node.action:
            action = node.action.value
            cost_father = node.father.cost
            msg = "<--- {0} [{1}] --->"
            solution_path.append(msg.format(action, cost_father))
        node = node.father

    for step in reversed(solution_path):
        print(step)