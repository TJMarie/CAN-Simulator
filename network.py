from node import Node
import calculations as calc

class Network:
    def __init__(self, dimensions):
        self.dimensions = dimensions
        self.node_locations = {}
        self.adjacency_list = {}
        self.nodes = []

    def initialize(self):
        area = [[0, 0], self.dimensions]
        id = calc.generate_hex_id()
        position = calc.generate_random_position(self.dimensions)
        new_node = Node(id=id, position=position)
        new_node.area = area
        self.nodes.append(new_node)
        self.node_locations[id] = position

    
    def add_node(self):
        """Node to split: Node object"""

        id = calc.generate_hex_id()
        position = calc.generate_random_position(self.dimensions)

        for n in self.nodes:
            if calc.in_area(position, n):
                node_to_split = n
            break

        node_to_split, sorted_nodes = calc.find_nearest_node(position, self.nodes) 

        new_position, new_node_area = calc.split_node(node_to_split) 
        new_node = Node(id=id, position=new_position if new_position else position)
        new_node.area = new_node_area # type: ignore

        self.nodes.append(new_node)
        self.node_locations[id] = position
        print(f"Node added at position: {new_position}")
        return new_node
    
    def delete_node(self, node):
        """ Parameter: node = Node object
            Returns: List(Node)"""
        if len(self.nodes) <= 1:
            print("Issue: Cannot delete last node!\n")
            return

        calc.merge_nodes(node, self.nodes)
        
        if node in self.nodes:
            self.nodes.remove(node)
            print(f"Removed node 0x{node.id} from node list\n")
        else:
            print(f"Could not find node 0x{node.id} in node list\n")

        if node.id in self.node_locations.keys():
            del self.node_locations[node.id]
            print(f"Node {node.id} deleted.\n")
            print(f"New list: {self.node_locations}")
        else:
            print(f"Node {node.id} not found.")

        return self.nodes
    

    
