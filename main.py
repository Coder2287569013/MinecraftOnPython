from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app = Ursina()
pick = 1
def update():
    global pick
    if held_keys["1"]: pick = 1
    if held_keys["2"]: pick = 2
    if held_keys["3"]: pick = 3
class Voxel(Button):
    def __init__(self, position = (0,0,0), color = color.green):
        super().__init__(
            parent = scene,
            position = position,
            model = "cube",
            texture = "white_cube",
            origin_y = 0.5,
            color = color
        )
    def input(self, key):
        if self.hovered:
            if key == "right mouse down":
                if pick == 1: voxel = Voxel(position = self.position + mouse.normal)
                if pick == 2: voxel = Voxel(position = self.position + mouse.normal, color = color.brown)
                if pick == 3: voxel = Voxel(position = self.position + mouse.normal, color= color.gray)
            if key == 'left mouse down': destroy(self)
sky = Sky()
player = FirstPersonController()
for x in range(20):
    for z in range(20): voxel = Voxel(position = (x,0,z))
for x in range(20):
    for z in range(20): voxel = Voxel(position = (x,-1,z), color = color.brown)
for x in range(20):
    for z in range(20): voxel = Voxel(position = (x,-2,z), color = color.brown)
for x in range(20):
    for z in range(20): voxel = Voxel(position = (x,-3,z), color = color.gray)
for x in range(20):
    for z in range(20): voxel = Voxel(position = (x,-4,z), color = color.gray)
for x in range(20):
    for z in range(20): voxel = Voxel(position = (x,-5,z), color = color.gray)
app.run()