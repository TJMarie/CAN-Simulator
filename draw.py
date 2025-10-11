import matplotlib.pyplot as plt

def draw_network(nodes, dimensions):
    plt.figure(figsize=(8, 8))
    plt.xlim(0, dimensions[0])
    plt.ylim(0, dimensions[1])
    plt.title("Network Node Distribution")
    plt.xlabel("X Coordinate")
    plt.ylabel("Y Coordinate")

    for node in nodes:
        x, y = node.position
        plt.scatter(x, y, marker='o')
        plt.text(x + 1, y + 1, node.id, fontsize=9)

    plt.grid(True)
    plt.show()