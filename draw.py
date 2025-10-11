import matplotlib.pyplot as plt

def draw_network(nodes, dimensions):
    plt.figure(figsize=(8, 8))
    plt.xlim(0, dimensions[0])
    plt.ylim(0, dimensions[1])
    plt.title("CAN Network Node Distribution")
    plt.xlabel("X")
    plt.ylabel("Y")

    for node in nodes:
        # Draw node address
        x, y = node.position
        plt.scatter(x, y, marker='o')
        plt.text(x + 1, y + 1, node.id, fontsize=9)

        # Draw box around node
        x1, y1 = node.area[0]
        x2, y2 = node.area[1]
        x = [x1, x2, x2, x1, x1]
        y = [y1, y1, y2, y2, y1]

        plt.plot(x, y)


    plt.grid(True)
    plt.show()