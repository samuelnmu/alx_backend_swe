import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background to black

# Create a turtle for writing text
t = turtle.Turtle()
t.hideturtle()  # Hide the turtle cursor
t.color("white")  # Set the text color to white
t.penup()  # Don't draw lines, just write text

# Move the turtle to the top of the screen
t.goto(0, 300)  # Set starting position (x=0, y=300)
t.write("Samuel Ngige", align="center", font=("Arial", 24, "normal"))

# Animation to move the name down to the center
for y in range(300, 0, -10):  # Move from 300 to 0 with steps of 10
    t.clear()  # Clear previous text
    t.goto(0, y)  # Update position
    t.write("Samuel Ngige", align="center", font=("Arial", 24, "normal"))

# Finish
screen.mainloop()
