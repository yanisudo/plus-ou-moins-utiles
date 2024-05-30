import matplotlib.pyplot as plt

def create_plot(data):
    plt.figure(figsize=(10, 5))
    plt.plot(data['x'], data['y'], marker='o')
    plt.title('Sample Plot')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    data = {'x': [1, 2, 3, 4, 5], 'y': [10, 20, 15, 25, 30]}
    create_plot(data)
