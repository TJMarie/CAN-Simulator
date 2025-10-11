import random

def generate_hex_id():
    id = (hex(random.randint(0, 0xFFFFFF))[2:])
    return id

def calculate_distance(node_1, node_2):
    return ((node_1[0] - node_2[0]) ** 2 + (node_1[1] - node_2[1]) ** 2) ** 0.5

def generate_random_position(dimensions):
    x = random.randint(0, dimensions[0] - 1)
    y = random.randint(0, dimensions[1] - 1)
    return (x, y)

def find_nearest_node(node, nodes):
    """ Parameters: node=List(x, y), nodes=List(Node objects)
    Returns: closest_node=Node object"""
    sorted_nodes = sorted(nodes, key=lambda n: calculate_distance(node, n.position))
    closest_node = sorted_nodes[0]
    print(closest_node)
    return closest_node

def split_node(current_node):
    """Returns Tuple(new_position, new_node_area)
    Updates current_node.area and current_node.position"""
    x1, y1 = current_node.area[0]
    x2, y2 = current_node.area[1]
    width, height = x2 - x1, y2 - y1
    x_mid = x1 + width // 2
    y_mid = y1 + height // 2

    if width >= height:  # Cut area in half vertically
        # Current to left
        current_node.area = [[x1, y1], [x_mid, y2]]   
        current_pos_x = x1 + (width // 4)
        current_pos_y = y1 + (height // 2) 

        # New to right
        new_area_start = (x_mid, y1)
        new_area_end = (x2, y2)
        new_node_area = (new_area_start, new_area_end)

    else:  # Cut area in half horizontally
        # Current to top
        current_node.area = [[x1, y_mid], [x2, y2]] 
        current_pos_x = x1 + width // 2
        current_pos_y = y1 + (height * 3 // 4) 

        # New to bottom
        new_area_start = (x1, y1)
        new_area_end = (x2, y_mid)
        new_node_area = (new_area_start, new_area_end)
    
    # Find new node positions
    new_width = new_area_end[0] - new_area_start[0]
    new_height = new_area_end[1] - new_area_start[1]
    new_x = new_area_start[0] + new_width // 2
    new_y = new_area_start[1] + new_height // 2
    new_position = (new_x, new_y)
    current_node.position = (current_pos_x, current_pos_y)
    
    
    return new_position, new_node_area

def in_area(node_1, node_2):
    """Parameters: node_1=List(x, y), node_2=Node object
    Returns: Boolean"""
    area_2 = node_2.area
    xn, yn = node_1
    x1, y1 = area_2[0]
    x2, y2 = area_2[1]

    if (x1 <= xn & xn <= x2 & y1 < yn & yn < y2):
        return True
    else:
        return False
