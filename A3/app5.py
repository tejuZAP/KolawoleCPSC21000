def calculate_paint(wall_length,wall_width,wall_height, ceiling_length, ceiling_width):
    #calculate the area of the wall
    wall_area = 2 * (wall_length * wall_width + wall_width*wall_height)
    #calculate the area of the ceiling
    ceiling_area = ceiling_length * ceiling_width
    #calculate total area
    total_area = wall_area + ceiling_area
    #calculate gallons of paint needed
    gallons_needed = total_area / 350
    
    return gallons_needed

#Get input from the user
wall_length = float(input("length of wall in feet:"))
wall_width = float(input("width of wall in feet:"))
wall_height = float(input("height of wall in feet:"))
ceiling_length = float(input("length of ceiling in feet:"))
ceiling_width = float(input("width of ceiling in feet:"))
#Calculate and print the amount of paint needed plus the cost 
paint_needed = calculate_paint(wall_length,wall_width,wall_height, ceiling_length, ceiling_width)
cost = paint_needed * 37.5 #average cost of paint
print(f"You will need {paint_needed:.2f} gallons of paint which will cost around {cost:.2f}")    