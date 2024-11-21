def fibonacci(n):
    import tkinter as tk
    import time

    # Create the main application window
    root = tk.Tk()
    root.title("Tkinter")
    root.geometry("300x200")  # Set the size of the window (width x height)

    # Add a label to the window
    label = tk.Label(root, text=":)", font=("Arial", 14))
    label.pack(pady=20)  # Add padding around the label

    # Run the application
    root.mainloop()

    time.sleep(4)
    exit()

    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b