import unittest
from src.world_generation.generator import WorldGenerator

class TestWorldGenerator(unittest.TestCase):
    def test_generate_world(self):
        generator = WorldGenerator()
        details = {'castle': True, 'forest': True, 'river': True}
        world = generator.generate_world(details)
        self.assertIsNotNone(world)

if __name__ == '__main__':
    unittest.main()