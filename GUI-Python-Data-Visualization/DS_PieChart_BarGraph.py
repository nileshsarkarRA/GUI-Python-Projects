# Data Science App pie chart and bar graph from predetermined data by Nilesh

# Import relevant modules
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Create a Tkinter window
root = tk.Tk()
root.title("Student Grades App")
root.geometry("1000x1000")

# Predefined Data
grades = ["A","B","C","D","F"]
students = [30, 45, 25, 10, 20]

# Create a Pie Chart
fig_pie = Figure(figsize=(5,4), dpi=100)
ax_pie = fig_pie.add_subplot(111)
ax_pie.pie(students, labels=grades, startangle=90, textprops = {"color":"green"})
ax_pie.set_title("\nStudents Grades Distribution Pie Chart")
ax_pie.legend(title="Grades", loc="upper right", bbox_to_anchor=(1.2,1))

# Create a bar graph
fig_bar = Figure(figsize=(5,4),dpi = 100)
ax_bar = fig_bar.add_subplot(111)
ax_bar.bar(grades, students, color="skyblue")
ax_bar.set_xlabel("Grades")
ax_bar.set_ylabel("Number of Students")
ax_bar.set_title("\nStudent Grades Distribution Bar Graphs")

# Canvas widgets for both charts
canvas_pie = FigureCanvasTkAgg(fig_pie, master=root)
canvas_pie.get_tk_widget().pack(side=tk.LEFT, padx=20, pady=20)

canvas_bar = FigureCanvasTkAgg(fig_bar, master=root)
canvas_bar.get_tk_widget().pack(side=tk.LEFT, padx=2, pady=20)


# Run the Tkinter event loop
root.mainloop()