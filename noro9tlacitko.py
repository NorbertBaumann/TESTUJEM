import tkinter as tk
from matplotlib import pyplot as plt
from matplotlib import style


def create_chart():
    # Set the style
    style.use('ggplot')

    # Data
    x = [5, 8, 10]
    y = [12, 16, 6]
    x2 = [6, 9, 11]
    y2 = [6, 15, 7]

    # Create the bar chart
    plt.bar(x, y, align='center')
    plt.bar(x2, y2, color='g', align='center')

    # Add labels and title
    plt.title('Info')
    plt.ylabel('Y axis')
    plt.xlabel('X axis')

    # Save the chart
    # plt.savefig('barchart.png')
    plt.show()
    # Close the plot to free memory
    plt.close()

    # Optional: Update a label to show the chart was generated
    status_label.config(text="Chart generated and saved as 'barchart.png'")


# Create the main window
root = tk.Tk()
root.title("Chart Generator")
root.geometry("300x200")

# Create a button
generate_button = tk.Button(root,
                            text="Generate Chart",
                            command=create_chart,
                            padx=10,
                            pady=5)
generate_button.pack(pady=20)

# Create a status label
status_label = tk.Label(root, text="")
status_label.pack(pady=10)

# Start the application
root.mainloop()