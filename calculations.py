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
    Updates current_node.area"""
    x1, y1 = current_node.area[0]
    x2, y2 = current_node.area[1]
    width, height = x2 - x1, y2 - y1

    if width >= height:
        mid_x = x1 + width // 2
        new_node_area = [[mid_x, current_node.area[0][1]], [current_node.area[1][0], current_node.area[1][1]]]
        x2 = mid_x
    else:
        mid_y = current_node.area[0][1] + height // 2
        new_node_area = [[current_node.area[0][0], mid_y], [current_node.area[1][0], current_node.area[1][1]]]
        y2 = mid_y
    
    current_node.area
    
    x1, y1 = new_node_area[0]
    x2, y2 = new_node_area[1]
    new_position = (x2 - x1, y2 - y1)
    
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
