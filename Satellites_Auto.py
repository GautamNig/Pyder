import bpy 
import random
import os
import array
import math

os.system('cls')

bpy.ops.object.select_all(action='DESELECT')
for o in bpy.data.objects:
    if o.name not in ('Lamp', 'Camera', 'Earth', 'Moon', 'Sat1', 'Sat2', 'Sat3', 'Asteroids'):
        bpy.data.objects[o.name].select = True
        
    bpy.ops.object.delete() 

for a in bpy.data.actions:
    bpy.data.actions.remove(a)
    
satArray = ['Sat1','Sat2','Sat3']

    
for r in range(1, 4, 1):
    print('In loop')
    bpy.ops.curve.primitive_bezier_circle_add(
    view_align=False, location=(0, 0, 0))
    
    print('Active obj is : ' + str(bpy.context.active_object))
    
    path = bpy.context.active_object
    
    resizeRandomRadius = random.uniform(11.5, 17.9)
    
    bpy.ops.transform.resize(value=(resizeRandomRadius, 
    resizeRandomRadius, 
    resizeRandomRadius), 
    constraint_axis=(False, False, False))

   
    zTranslate = random.uniform(1.2, 5.9)
    bpy.ops.transform.translate(value=(0, 0,zTranslate ), 
    constraint_axis=(False, False, True))
    
    
    rndAngle = random.randint(0, 360)
    x = 0 + resizeRandomRadius * math.cos(math.radians(rndAngle))
    y = 0 + resizeRandomRadius * math.sin(math.radians(rndAngle))
    
    rnX = x 
    rnY = y 
    rnZ = zTranslate
    
    rndNum = random.randint(0,len(satArray) - 1)
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[satArray[rndNum]].select = True
    
    ob = bpy.data.objects[satArray[rndNum]].copy() # duplicate linked
    ob.data = bpy.data.objects[satArray[rndNum]].data.copy() # optional: make this a        real duplicate (not linked)
    bpy.context.scene.objects.link(ob) # add to scene

    
    ob.location.x = rnX
    ob.location.y = rnY
    ob.location.z = rnZ      
    print( str(ob.location.x) + ':' + str(ob.location.y) + ':' + str(ob.location.z))  
    
    bpy.context.scene.objects.active = path #parent

    bpy.ops.object.parent_set(type='FOLLOW') #follow path
    
    bpy.context.object.data.path_duration = 250
    
    print('Active obj is : ' + str(bpy.context.active_object))
    
    


import bpy 
import random
import os
import array
import math

os.system('cls')

bpy.ops.object.select_all(action='DESELECT')
for o in bpy.data.objects:
    if o.name not in ('Lamp', 'Camera', 'Earth', 'Moon', 'Sat1', 'Sat2', 'Sat3', 'Asteroids'):
        bpy.data.objects[o.name].select = True
        
    bpy.ops.object.delete() 


satArray = ['Sat1','Sat2','Sat3']

    
for r in range(1, 4, 1):
    print('In loop')
    bpy.ops.curve.primitive_bezier_circle_add(
    view_align=False, location=(0, 0, 0))
    
    print('Active obj is : ' + str(bpy.context.active_object))
    
    path = bpy.context.active_object
    
    resizeRandomRadius = random.uniform(11.5, 17.9)
    
    bpy.ops.transform.resize(value=(resizeRandomRadius, 
    resizeRandomRadius, 
    resizeRandomRadius), 
    constraint_axis=(False, False, False))

   
    zTranslate = random.uniform(1.2, 5.9)
    bpy.ops.transform.translate(value=(0, 0,zTranslate ), 
    constraint_axis=(False, False, True))
    
    
    rndAngle = random.randint(0, 360)
    x = 0 + resizeRandomRadius * math.cos(math.radians(rndAngle))
    y = 0 + resizeRandomRadius * math.sin(math.radians(rndAngle))
    
    rnX = x 
    rnY = y 
    rnZ = zTranslate
    
    rndNum = random.randint(0,len(satArray) - 1)
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[satArray[rndNum]].select = True
    
    ob = bpy.data.objects[satArray[rndNum]].copy() # duplicate linked
    ob.data = bpy.data.objects[satArray[rndNum]].data.copy() # optional: make this a        real duplicate (not linked)
    bpy.context.scene.objects.link(ob) # add to scene

    
    ob.location.x = rnX
    ob.location.y = rnY
    ob.location.z = rnZ      
    print( str(ob.location.x) + ':' + str(ob.location.y) + ':' + str(ob.location.z))  
    
    bpy.ops.object.select_all(action='DESELECT')
    ob.select = True
    bpy.context.scene.objects.active = ob

# --------------- Working but sattelites are in straight line
#    ob.location.x = rnX
#    ob.location.y = rnY
#    ob.location.z = rnZ  

# make above as 0 0 0

#    obConstraints = ob.constraints.new('FOLLOW_PATH')
#    obConstraints.target = path
# OR
#    bpy.ops.object.constraint_add(type='FOLLOW_PATH')
#    bpy.context.object.constraints["Follow Path"].target = path

#    override={'constraint':ob.constraints["Follow Path"]}
#    bpy.ops.constraint.followpath_path_animate(override,constraint='Follow Path')                 
# --------------- Working but sattelites are in straight line


    bpy.context.scene.objects.active = path #parent

    bpy.ops.object.parent_set(type='FOLLOW') #follow path
    
    bpy.context.object.data.path_duration = 250
    
    area = bpy.context.area
    old_type = area.type
    
    bpy.ops.object.select_all(action='DESELECT')
    path.select = True
        
    bpy.context.area.type = "GRAPH_EDITOR"
    KEYFRAME_POINTS_ARRAY = []
    
    for act in bpy.data.actions:        
        for fc in act.fcurves:                                
            fc.keyframe_points.insert(1, 1)
            fc.keyframe_points.insert(100, 250)
        for m in fc.modifiers:
           if (m.type == 'GENERATOR'): 
               fc.modifiers.remove(m)

    bpy.ops.graph.fmodifier_add(type='CYCLES')
    
    area.type = old_type

    print('Active obj is : ' + str(bpy.context.active_object))
    
    


