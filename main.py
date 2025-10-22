import calculations as calc
from network import Network
import draw as d

""" 
Node locations: Dictionary of key: node ID, value: coordinates
Node neighbors: Dictionary of key: node ID, value: list of neighboring node IDs
"""

def add_a_node():
    try:
        num_nodes = int(input("\nHow many nodes would you like to add? ==> ").strip())
    except(ValueError):
        print("I don't know that number.")
        return
    
    print("\n=================\nADDING NODES\n")
    for _ in range(num_nodes):
        network.add_node()
    print("\nEND ADDING NODES\n=================\n")

def delete_a_node():
    if len(network.nodes) <= 1:
        print("\nIssue: Cannot delete last node!")
        return
    
    print("\n=================\nDELETION MODE")
    node = choose_find_method()

    if node:
        network.delete_node(node)
        print(f"\nNode 0x{node.id} deleted.")
    else:
        print("\nCould not find node.")

    print("END DELETION MODE\n=================\n")

def list_nodes():
    for node in network.nodes:
        print(f"Node 0x{node.id} | position: {node.position}")

def draw_network():
    d.draw_network(network.nodes, network.dimensions)

def find_a_node():
    """Allows user to find a node by hex ID or coordinates, then print, write, or delete it."""
    print("\n=================\nFIND MODE")
    node = choose_find_method()

    if not node: 
        print("END FIND MODE\n=================\n")
        return
    
    find_options = "\n'p' ==> print its content\
                    \n'w' ==> write content\
                    \n'del' ==> delete this node\
                    \n'q' ==> cancel find mode\n\n==> "
    user_input = ""

    while user_input != "q":
        print(f"\nWhat would you like to do with Node 0x{node.id}?\n")
        user_input = input(find_options).lower().strip()

        if user_input == "p":
            print(f"\nNode 0x{node.id}'s Content:")
            print(f"\n{node.content}\n")
        elif user_input == "w":
            node.content = input(f"\nWrite to node 0x{node.id}:\n\n==> ")
        elif user_input == "del":
            network.delete_node(node)
        elif user_input == 'q':
            print("\nCanceling find mode...\n")
            break
        else:
            print(f"\nI can't do that. Enter 'h' for options.\n")
    
    print("\nEND FIND MODE\n=================\n")
    return

def restructure():
    print("\n=================\nRESTRUCTURING NETWORK\n")
    network.restructure_network()
    print("\nEND RESTRUCTURING NETWORK\n=================\n")

def choose_find_method():
    # Choose search method
    choose_options = {
        'coord' : find_by_coordinates,
        'hex' : find_by_hex,
        'q' : lambda: print("\nCanceling...\n\n")
    }
    user_input = input("'coord' ==> find node by coordinates\
                       \n'hex' ==> find node by hex ID\
                       \n'q' ==> cancel\n\n==> ").lower().strip()
    node = None
    
    try:
        node = choose_options[user_input]()
    except(KeyError):
        print("\nI don't recognize that command.\n")

    return node

def find_by_hex():
    node_id = input("Type in the hex ID of the node you would like to find: ").lower().strip() 

    for n in network.nodes:
        if n.id == node_id:
            return n
    
    print(f"\nSorry, I couldn't find node 0x{node_id}")

def find_by_coordinates():
    """ Returns: nearest_node = Node object"""
    print("Find nearest neighbor:\n")
    x, y = 0, 0
    try:
        x = int(input("Enter x coordinate: ==> ").strip())
        y = int(input("Enter y coordinate: ==> ").strip())
    except(ValueError):
        print("I don't know that number.")
        return
    target_node = (x, y)
    nearest_node, sorted_nodes = calc.find_nearest_node(target_node, network.nodes)
    print(f"The nearest node to {target_node} is:\
        Node 0x{nearest_node.id} | Position: {nearest_node.position} | Area: {nearest_node.area}\n")
    return nearest_node

def help():
    print("Options:")
    for option, function in options.items():
        print(f"'{option}' ==> {function.__name__}")

def exit_simulator():
    exit()


if __name__ == "__main__":
    network_dimensions = (100, 100)
    network = Network(network_dimensions)
    network.initialize()
    print("Welcome to my CAN Simulator.\n")
    print("Initializing network simulation...\n")
    print(f"Network dimensions: {network_dimensions[0]} x {network_dimensions[1]}\n")
    print(f"Initial node added at {network.nodes[0].position}\n")

    options = {"a" : add_a_node,
               "del" : delete_a_node,
               "l": list_nodes,
               "f" : find_a_node,
               "dr" : draw_network,
               'r' : restructure,
               "h" : help,
               "q" : exit_simulator
    }
    
    help()

    user_input = ""
    while user_input.lower() != ("exit" or "q"):
        user_input = input("\nType something ==> ").strip()
        try:
            options[user_input]()
        except(KeyError):
            print("\nInvalid command. Type 'h' for options.\n")
        
