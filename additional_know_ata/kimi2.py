import tkinter as tk

class ExampleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Button Size Example")
        self.root.geometry("300x200")

        # Create a small button with specific width and height
        self.small_button = tk.Button(self.root, text="Small Button", width=10, height=2)
        self.small_button.pack(pady=20)

# Create the main Tkinter window
root = tk.Tk()

# Create an instance of the ExampleApp class
app = ExampleApp(root)

# Start the Tkinter event loop
root.mainloop()
