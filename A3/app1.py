'''
robot move forward through and obstacle course
'''

class Robot:
   def _init_(self): 
       pass
   def move_forward(self, distance):
       pass
   def turn(self, angle):
       pass
   def sense_obstacles(self):
       pass
   def navigate_obstacle_course(self, sensors):
       while True:
        # Get sensor readings
        distances = [sensor.get_distance() for sensor in sensors]

        # Check for obstacles
        obstacle_detected = False
        for distance in distances:
            if distance < 30:  # threshold distance
                obstacle_detected = True
                break
            
        if obstacle_detected:
            # Implement obstacle avoidance strategy
            self.turn_left(-90)  # left turn
            self.move_forward(1)  
            self.turn_right(90) # right turn
        else:
            # Move forward if no obstacle is detected
            self.move_forward(40)  # move distance

        # Check for goal condition
        def goal_reached(self):
            break