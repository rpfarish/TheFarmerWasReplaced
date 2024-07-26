def advance_pos():
    if get_pos_y() == get_world_size() - 1:
        move(East)
    move(North)

def resetup_world(x, y):
    clear()
    for i in range(y):
        for _ in range(x):
            till()
            move(North)
        move(East)

def in_square():
    return get_pos_y() < 2 and get_pos_x() < 2

world_x = get_world_size()
world_y = world_x
     

water_thresh = 1
        
inverse_moves = {North: South, South: North, East: West, West: East}

def next_move_in_visited(visited, x, y, next_move):
    if next_move == North:       
        return  (x, y + 1) in visited
    if next_move == South:
        return (x, y - 1) in visited
    if next_move == East:
        return (x + 1, y) in visited
    if next_move == West:
        return (x - 1, y) in visited
            
    return False

def search_maze(visited, x, y):
    if get_entity_type() == Entities.Treasure:
        harvest()
        return True
    for dir in inverse_moves:
        if next_move_in_visited(visited, x, y, dir):
            continue

        move(dir)        
        if (get_pos_x() == x and get_pos_y() == y):
            continue
        visited.append((get_pos_x(), get_pos_y()))
        ret = search_maze(visited, get_pos_x(), get_pos_y())
        if ret:
            return True
        move(inverse_moves[dir])
        
while True:    
    while True:
        
        # CARROTS
       
        if not num_items(Items.Fertilizer):
                trade(Items.Fertilizer, get_world_size() * 2)
       
        if can_harvest(): 
            use_item(Items.Fertilizer) 
        plant(Entities.Bush)
        cur_x = get_pos_x()
        cur_y = get_pos_y()
        advance_pos()
        if get_pos_x() == cur_x and get_pos_y() == cur_y:
            break
     
    visited = []       
    search_maze(visited, cur_x, cur_y)   