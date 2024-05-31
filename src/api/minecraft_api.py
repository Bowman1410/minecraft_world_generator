from mcpi.minecraft import Minecraft

class MinecraftAPI:
    def __init__(self, address='localhost', port=25565):
        self.mc = Minecraft.create(address, port)

    def create_world(self):
        # Logic to initialize a new world (optional)
        self.mc.postToChat("Creating a new world")

    def build_castle(self, position):
        # Example: Build a simple castle at the given position
        x, y, z = position
        self.mc.setBlocks(x, y, z, x+10, y+5, z+10, 4)  # Stone base
        self.mc.setBlocks(x+1, y, z+1, x+9, y+4, z+9, 0)  # Hollow space
        self.mc.setBlocks(x+4, y+5, z+4, x+6, y+7, z+6, 4)  # Towers

    def plant_forest(self, area):
        x1, y1, z1, x2, y2, z2 = area
        for x in range(x1, x2):
            for z in range(z1, z2):
                self.mc.setBlock(x, y1, z, 6)  # Sapling

    def create_river(self, path):
        for (x, z) in path:
            self.mc.setBlocks(x, 63, z, x, 61, z, 9)  # Water blocks

    