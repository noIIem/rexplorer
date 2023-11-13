import os
import subprocess
import tkinter as tk

# Function to close the window
def close_window():
    root.destroy()

# Function to update the timer label
def update_timer():
    global time_remaining
    time_remaining -= 1
    timer_label.config(text=f"Window will close in: {time_remaining}", fg='#ECF0F1', bg='#2C3E50')  # Dark theme colors
    if time_remaining > 0:
        root.after(1000, update_timer)
    else:
        close_window()

# Find and terminate the existing explorer.exe process
os.system('taskkill /f /im explorer.exe')

# Start a new explorer.exe process
subprocess.Popen('explorer.exe')

# Create a GUI window
root = tk.Tk()
root.title("Windows Explorer Restarted")
root.configure(bg='#2C3E50')  # Dark theme background color

# Initialize timer value
time_remaining = 6

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate center position
x = (screen_width - 300) / 2
y = (screen_height - 150) / 2

# Set the window size and position
root.geometry(f"300x150+{int(x)}+{int(y)}")

# Create a label with the message
label = tk.Label(root, text="Windows Explorer Restarted!", font=("Helvetica", 16), fg='#ECF0F1', bg='#2C3E50')  # Dark theme colors
label.pack(pady=20)

# Create a label to display the timer
timer_label = tk.Label(root, text=f"Window will close in: {time_remaining}", fg='#ECF0F1', bg='#2C3E50')  # Dark theme colors
timer_label.pack()

# Start the timer
update_timer()

# Create a button to close the window
button = tk.Button(root, text="OK", command=close_window, fg='#2C3E50', bg='#1ABC9C')  # Dark theme colors
button.pack()

# Run the GUI main loop
root.mainloop()
