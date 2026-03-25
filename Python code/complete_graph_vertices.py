import networkx as nx
import matplotlib.pyplot as plt

def create_complete_graph():
    while True:
        try:
            n = int(input("Enter number of vertices (greater than 3): "))
            if n > 3:
                break
            else:
                print("Number must be greater than 3. Try again.")
        except ValueError:
            print("Please enter a valid integer.")

    # Create complete graph
    G = nx.complete_graph(n)

    # Draw graph
    plt.figure(figsize=(8, 8))
    pos = nx.circular_layout(G)  # Arrange nodes in a circle
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color="skyblue",
        node_size=800,
        edge_color="gray",
        font_size=12,
        font_weight="bold"
    )

    plt.title(f"Complete Graph with {n} Vertices")
    plt.show()

if __name__ == "__main__":
    create_complete_graph()
