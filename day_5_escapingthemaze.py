

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right()==True:
        move()
    turn_right()
    move()
    turn_right()
    move()
    while wall_on_right()==True and front_is_clear()==True:
        move()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif wall_in_front():
        if right_is_clear():
            turn_right()
        else:
            turn_left()
    else:
        move()
    

