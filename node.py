class Node:
    def __init__(self, id, position):
        self.id = id
        self.position = position
        self.prev_node = None
        self.next_node = None
        self.area = [[0, 0], [0, 0]]  # Placeholder for node's area in the CAN space
        self.content = None
    
    def __repr__(self):
        return f"Node(id={self.id}, position={self.position}, area={self.area})"
    
    def add_content(self):
        content = input(f"Enter new content for {self.id}: ")
        self.content = content
        return self.content
    