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
        self.adjacency_list[id] = new_node.neighbors

    
    def add_node(self):
        """Node to split: Node object"""

        id = calc.generate_hex_id()
        position = calc.generate_random_position(self.dimensions)

        for n in self.nodes:
            if calc.in_area(position, n):
                node_to_split = n
            break

        node_to_split = calc.find_nearest_node(position, self.nodes) 

        new_position, new_node_area = calc.split_node(node_to_split) 
        new_node = Node(id=id, position=new_position if new_position else position)
        new_node.add_content()

        self.nodes.append(new_node)
        self.node_locations[id] = position
        self.adjacency_list[id] = new_node.neighbors
        print(f"Node added at position: {new_position}")
        return 
    
    def delete_node(self, node_id):
        if node_id in self.node_locations.keys():
            # del self.nodes[node_id]
            del self.node_locations[node_id]
            # if node_id in self.adjacency_list:
            #    del self.adjacency_list[node_id]
            # for neighbors in self.adjacency_list.values():
            #     if node_id in neighbors:
            #         neighbors.remove(node_id)
            print(f"Node {node_id} deleted.\n")
            print(f"New list: {self.node_locations}")
        else:
            print(f"Node {node_id} not found.")
        return self.nodes
    

    
