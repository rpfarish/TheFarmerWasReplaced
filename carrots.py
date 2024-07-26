def advance_pos():
    if get_pos_y() == get_world_size() - 1:
        move(East)
    move(North)

def plant_tree():
    if (get_pos_y() - get_pos_x()) % 2 == 0:
        plant(Entities.Tree)
        advance_pos()
def plant_carrots():
        if not Grounds.Soil:
            till()
        if not num_items(Items.Carrot_Seed):
            trade(Items.Carrot_Seed, get_world_size() * 2)   
        plant(Entities.Carrots)
        advance_pos()
            
def plant_pumkins():
        if not Grounds.Soil:
            till()
        if not num_items(Items.Pumpkin_Seed):
            trade(Items.Pumpkin_Seed)   
        plant(Entities.Pumpkin)
        advance_pos()

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
     
resetup_world(world_x, world_y)
water_thresh = 1
        
while True:
    
    # CARROTS
    if Grounds.Turf:
        
        if can_harvest():
            harvest()
        
        if get_water() < water_thresh:
            use_item(Items.Water_Tank)
    
        plant_carrots()
   
    
    