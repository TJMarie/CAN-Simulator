class Node:
    def __init__(self, id, position):
        self.id = id
        self.position = position
        self.neighbors = []
        self.routing_table = {}
        self.area = [[0, 0], [0, 0]]  # Placeholder for node's area in the CAN space
        self.content = None
    
    def __repr__(self):
        return f"Node(id={self.id}, position={self.position}, area={self.area})"
    
    def add_neighbor(self, neighbor_id):
        if neighbor_id not in self.neighbors:
            self.neighbors.append(neighbor_id)
        return self.neighbors
    
    def delete_neighbor(self, neighbor_id):
        if neighbor_id in self.neighbors:
            self.neighbors.remove(neighbor_id)
        return self.neighbors
    
    def add_content(self):
        content = input(f"Enter new content for {self.id}: ")
        self.content = content
        return self.content
    