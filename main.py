"""
Author: Weijie Zhang

Date: 12/25/2021

Title: Christmas Tree
"""

import turtle
import random
import math

# constant #
BASE_ANGLE_START = 40
BASE_ANGLE_END = 55
BASE_DISTANCE_START = 5
BASE_DISTANCE_END = 10
BASE_INCREMENT = 15

NUM_OF_TRIANGLE = 7
HYP_OF_TRIANGLE = 50

STARTING_X_COOD = 0
STARTING_Y_COOD = 150

DISTANCE_BETWEEN_EACH_TRIANGLE = 40
DISTANCE_BETWEEN_EACH_HYP = (HYP_OF_TRIANGLE - BASE_INCREMENT * 2) / 2

LENGTH_OF_STAR = 20
STAR_STARTING_LENGTH = (math.cos(math.radians(72)) * LENGTH_OF_STAR + LENGTH_OF_STAR) / (math.cos(math.radians(18)))

LENGTH_OF_TRUNK = 60



t = turtle.Turtle()
t.speed(0)


def run():

  # go to the top of the tree first
  t.penup()
  t.goto(STARTING_X_COOD, STARTING_Y_COOD)

  # set up variables #
  hyp = HYP_OF_TRIANGLE
  midpoint_y_cood = STARTING_Y_COOD
  base_increment = 0

  # draw the tree #
  for i in range(NUM_OF_TRIANGLE):

    t.penup()
    t.goto(STARTING_X_COOD, midpoint_y_cood)

    tree_layer(hyp, base_increment)

    base_increment += BASE_INCREMENT

    midpoint_y_cood -= DISTANCE_BETWEEN_EACH_TRIANGLE

  # draw the tree trunk #
  t.penup()
  t.goto(STARTING_X_COOD, STARTING_Y_COOD - (NUM_OF_TRIANGLE * DISTANCE_BETWEEN_EACH_TRIANGLE))

  tree_trunk()

  # draw the star #
  t.penup()
  t.goto(STARTING_X_COOD, STARTING_Y_COOD)

  t.pendown()
  tree_star(LENGTH_OF_STAR)




# draw the base of the tree triangle #
def base(len, toward_left):

  current_len = 0;

  while (current_len < len):

    # move the turtle up #

    if (toward_left):
      angle = random.randint(BASE_ANGLE_START + 90, BASE_ANGLE_END + 90)

    else:
      angle = random.randint(BASE_ANGLE_START, BASE_ANGLE_END)

    distance = random.randint(BASE_DISTANCE_START, BASE_DISTANCE_END)

    t.setheading(angle)
    t.fd(distance)


    # calculate the horizontal distance #

    if (toward_left):
      h_distance = distance * math.cos(math.radians(180 - angle))
    
    else:
      h_distance = distance * math.cos(math.radians(angle))

    current_len += h_distance

    # move the turtle down #

    if (toward_left):
      angle = random.randint(BASE_ANGLE_START + 180, BASE_ANGLE_END + 180)

    else:
      angle = random.randint(BASE_ANGLE_START + 270, BASE_ANGLE_END + 270)

    distance = random.randint(BASE_DISTANCE_START, BASE_DISTANCE_END)

    t.setheading(angle)
    t.fd(distance)

    # calculate the horizontal distance #

    if (toward_left):
      h_distance = distance * math.cos(math.radians(angle - 180))
    
    else:
      h_distance = distance * math.cos(math.radians(360 - angle))

    current_len += h_distance



# draw each layer of the tree # 
def tree_layer(hyp, base_inc):

  # midpoint position #

  pos = t.position()

  # the left side #
  
  t.goto(pos[0] - base_inc, pos[1])
  
  t.pendown()

  t.setheading(240)
  t.fd(hyp)

  t.penup()

  # the right side #

  t.goto(pos[0] + base_inc, pos[1])

  t.pendown()

  t.setheading(300)
  t.fd(hyp)

  # draw the base #

  midpoint_to_edge_length = base_inc + DISTANCE_BETWEEN_EACH_HYP

  t.penup()
  t.goto(pos[0], pos[1] - DISTANCE_BETWEEN_EACH_TRIANGLE)

  # the right side of the base #

  t.pendown()
  base(midpoint_to_edge_length, False)

  t.penup()
  t.goto(pos[0], pos[1] - DISTANCE_BETWEEN_EACH_TRIANGLE)

  # the left side of the base #

  t.pendown()
  base(midpoint_to_edge_length, True)



# draw the star on top of the tree #
def tree_star(length):

  t.penup()

  t.setheading(18)
  t.fd(STAR_STARTING_LENGTH)

  t.pendown()

  #t.fillcolor("yellow")

  #t.begin_fill()
  

  t.setheading(216)
  t.fd(length)

  t.setheading(288)
  t.fd(length)

  t.setheading(144)
  t.fd(length)

  t.setheading(216)
  t.fd(length)

  t.setheading(72)
  t.fd(length)

  t.setheading(144)
  t.fd(length)

  t.setheading(0)
  t.fd(length)

  t.setheading(72)
  t.fd(length)

  t.setheading(288)
  t.fd(length)

  t.setheading(0)
  t.fd(length)

  #t.end_fill()



# draw the tree trunk at the bottom of the tree #
def tree_trunk():

  pos = t.position()

  t.penup()
  t.goto(pos[0] - BASE_INCREMENT, pos[1])
  
  t.pendown()
  t.setheading(270)
  t.fd(LENGTH_OF_TRUNK)

  t.penup()
  t.goto(pos[0] + BASE_INCREMENT, pos[1])

  t.pendown()
  t.setheading(270)
  t.fd(LENGTH_OF_TRUNK)
  

run()