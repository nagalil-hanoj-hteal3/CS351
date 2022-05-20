#In case the following below does not work, I will provide the random walk, but will be commented out in between the code and "BUST"

import random
my_dots = {}

def init():
    return("m")#🗿m

def getLocation(temp, newDot):
    if(newDot - temp > 0):#if the coordinates are positive go right
        x = 1
    elif(newDot - temp < 0):#if the coordinates are positive go right
        x = -1
    else:
        x = 0
    return x

def run(db_cursor, state):
    global my_dots
    rows = db_cursor.execute(f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")
    for row in rows.fetchall():
        foods = db_cursor.execute(f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = (select owner_id from owner where name='Food') and owner.name = 'Food' order by sqrt(pow({row[0]}-x,2)+pow({row[1]}-y,2))asc")#closest location to find the food
        food = foods.fetchone()#fetch one food at a time in the game field
        if(row[0], row[1]) not in my_dots:
          try:
            my_dots[(row[0], row[1])] = (getLocation(row[0], food[0]), getLocation(row[1], food[1]))
          except:
            my_dots[ (row[0],row[1]) ] = ( random.choice([1,-1]) , random.choice([1,-1]) )
        else:
            my_dots[(row[0], row[1])] = (getLocation(row[0], food[0]), getLocation(row[1], food[1]))
        offset = my_dots[(row[0], row[1])]
        db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0]}, {row[1] + offset[1]}, 'MOVE')")
        del my_dots[(row[0], row[1])]
        my_dots[(row[0] + offset[0], row[1] + offset[1])] = offset

#----------------------------------------------------RANDOM WALK--------------------------------------------------------------

#def run(db_cursor, state):
#    global my_dots
#    #get all my dots
#    rows = db_cursor.execute(f"select x,y from main_game_field as gf, owner  where is_flag = FALSE and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")
#    for row in rows.fetchall():
#        if (row[0],row[1]) not in my_dots or (random.random() > .95) :
#            my_dots[ (row[0],row[1]) ] = ( random.choice([1,-1]) , random.choice([1,-1]) )
#        offset = my_dots[ (row[0],row[1]) ]
#        db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE')")
#        del my_dots[ (row[0],row[1]) ]
#        my_dots[ (row[0] + offset[0], row[1] + offset[1]) ] = offset

#--------------------------------------------------------- BUST --------------------------------------------------------------
#def sleep():
#return my_dots
#def wake(state):
#state = my_dots
#import random

#def eatFood(temp, newDot):
    #use distance formula to find the closest dot --> sqrt((x_0 - x_1)^2 + (y_0 - y_1)^2)
    #sqrt(pow(row[0]-x,2) + pow(row[1]-y,2)) used to collect foods that are near it
#    return sqrt((temp[0] + newDot[0])^2 - (temp[1] - newDot[1])^2)

#def runAway(temp, newDot):
#    return #distance formula

#    x = 0 #x-axis of the graph
#    y = 0 #y-axis of the graph
#if (row[0] > x and row[1] < y):
             #db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1}, {row[1] - 1}, 'MOVE')")
#if (row[0] < x and row[1] > y):
           #db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1}, {row[1] - 1}, 'MOVE')")
#if (row[0] > x and row[1] > y):
#                db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1}, {row[1] - 1}, 'MOVE')") #goes left diagonally up

#        elif (row[0] > x and row[1] > y):
#            db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] - 1}, {row[1] + 1}, 'MOVE')") #goes left diagonally down
#        elif (row[0] > x and row[1] > y):
#            db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 1}, {row[1] - 1}, 'MOVE')") #goes right diagonally up
#        elif (row[0] > x and row[1] > y):
#            db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + 1}, {row[1] + 1}, 'MOVE')") #goes right diagonally down
#        offset = my_dots[ (row[0],row[1]) ]
#        db_cursor.execute(f"insert into engine_orders values( {row[0]}, {row[1]}, {row[0] + offset[0] }, {row[1] + offset[1] }, 'MOVE')")
#        del my_dots[ (row[0],row[1]) ]
#        my_dots[ (row[0] + offset[0], row[1] + offset[1]) ] = offset
#        del my_dots[ (row[0],row[1]) ]
#        my_dots[ (row[0] + offset[0], row[1] + offset[1]) ] = offset
