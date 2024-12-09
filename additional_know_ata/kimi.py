import tkinter as tk

class ExampleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Example App")
        self.root.geometry("300x200")

        # Create and pack a label with options
        self.label = tk.Label(self.root, text="Label 1", bg="lightblue")
        self.label.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

        # Create and pack another label with options
        self.label2 = tk.Label(self.root, text="Label 2", bg="lightgreen")
        self.label2.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=5)

# Create the main Tkinter window
root = tk.Tk()

# Create an instance of the ExampleApp class
app = ExampleApp(root)

# Start the Tkinter event loop
root.mainloop()
