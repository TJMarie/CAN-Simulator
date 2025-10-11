import calculations as calc
from network import Network
import draw as d

""" 
Node locations: Dictionary of key: node ID, value: coordinates
Node neighbors: Dictionary of key: node ID, value: list of neighboring node IDs
"""

def add_a_node():
    network.add_node()

def delete_a_node():
    print("\n=================\nDELETION MODE")
    node_id = input("Type in the ID of the node you would like to delete: ")
    network.delete_node(node_id)
    print("END DELETION MODE\n=================\n")

def list_nodes():
    for node in network.nodes:
        print(node.__repr__)

def show_adjacent_nodes():
    print(network.adjacency_list)

def draw_network():
    d.draw_network(network.nodes, network.dimensions)

def find_a_node():
    x = int(input("Enter x coordinate to find nearest neighbor: "))
    y = int(input("Enter y coordinate to find nearest neighbor: "))
    target_node = (x, y)
    nearest_node = calc.find_nearest_node(target_node, network.node_locations.values())
    print(f"Nearest node to {target_node} is at {nearest_node}\n")

def help():
    print("Options:")
    for option, function in options.items():
        print(f"'{option}' ==> '{function.__name__}")

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
               "draw" : draw_network,
               "t" : show_adjacent_nodes,
               "h" : help,
               "q" : exit_simulator
    }
    
    help()

    user_input = ""
    while user_input.lower() != ("exit" or "q"):
        user_input = input("\nType something ==> ")
        try:
            options[user_input]()
        except(KeyError):
            print("Invalid command. Type 'h' for options.\n")
        
