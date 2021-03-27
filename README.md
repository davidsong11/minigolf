# minigolf
A game of mini golf built in Python with Pygame

By using pygame.draw, I drew the ball using the coordinates xball and yball. Then, I used mouse.get_pos() to draw a line from (xball,yball) to the cursor. This line shows the pathway of the ball and when the user clicks, the ball's speed, xspeed and yspeed, is changed accordingly. Next, obstacles like sand and water were added, and they affected the ball's speed and coordinates respectively. Finally, when the user has reached the end and the ball is in the hole, the program checks the ball's speed and if the ball has stopped moving, it displays text saying, "Nice! x strokes". X is a integer that acts as a counter for the amount of times the user has "hit" the ball. 
