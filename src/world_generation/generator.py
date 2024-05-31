from api.minecraft_api import MinecraftAPI 

class WorldGenerator:
    def __init__(self):
        self.api = MinecraftAPI()

    def generate_world(self, details):
        self.api.create_world()
        if 'castle' in details:
            self.api.build_castle((0, 0, 0))
        if 'forest' in details:
            self.api.plant_forest((10, 0, 10, 50, 0, 50))
        if 'river' in details:
            self.api.create_river([(5, 5), (15, 15)])
        return "Minecraft World with specified structures"