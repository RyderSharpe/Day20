from turtle import Screen, Turtle
import time

MOVE_DISTANCE = 20
class Snake():

    # What will happen when we initialize a new snake object
    def __init__(self):
        self.segments = []
        self.x_axis = 0
        self.y_axis = 0
        self.create_snake()


    def create_snake(self):
        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(x=self.x_axis, y=self.y_axis)
            self.x_axis -= 20
            self.segments.append(new_segment)

    ## Moves snake ##
    def move(self):
        # Gets snake to automatically move forwards
        game_is_on = True
        while game_is_on:
            # Move the segments in reverse order
            for seg_num in range(len(self.segments) - 1, 0, -1):  # range(start=2, stop=0, step=-1)
                # Get the x coordinates of the segment in front.
                new_x = self.segments[seg_num - 1].xcor()
                # Get the y coordinates of the segment in front.
                new_y = self.segments[seg_num - 1].ycor()
                # Move the current segment to the position of the segment in front of it.
                self.segments[seg_num].goto(new_x, new_y)
            self.segments[0].forward(20)

