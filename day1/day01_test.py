import unittest
from .day01 import counter_fuel, counter_fuel_with_fuel

class Day01TestCase(unittest.TestCase):
    def test_counter_fuel(self):
        self.assertEqual(counter_fuel(0,12), 2)
        self.assertEqual(counter_fuel(0,14), 2)
        self.assertEqual(counter_fuel(0,1969), 654)
        self.assertEqual(counter_fuel(0,100756), 33583)

    def test_counter_fuel_with_fuel(self):
        self.assertEqual(counter_fuel_with_fuel(0,14), 2)
        self.assertEqual(counter_fuel_with_fuel(0,1969), 966)
        self.assertEqual(counter_fuel_with_fuel(0,100756), 50346)

if __name__ == "__main__":
    unittest.main()
