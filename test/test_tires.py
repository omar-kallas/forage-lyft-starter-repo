import unittest
from datetime import datetime

from tires import *

class TestCarrigan(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        wear_out = [0, 0, 0, 0.9]
        carrigan = carrigan_tires.CarriganTires(wear_out)
        self.assertTrue(carrigan.needs_service())

        wear_out = [0, 0, 0.9, 0]
        carrigan = carrigan_tires.CarriganTires(wear_out)
        self.assertTrue(carrigan.needs_service())

        wear_out = [0, 0.9, 0, 0]
        carrigan = carrigan_tires.CarriganTires(wear_out)
        self.assertTrue(carrigan.needs_service())

        wear_out = [0.9, 0, 0, 0]
        carrigan = carrigan_tires.CarriganTires(wear_out)
        self.assertTrue(carrigan.needs_service())

    def test_engine_should_not_be_serviced(self):
        wear_out = [0.8, 0.8, 0.8, 0.8]
        carrigan = carrigan_tires.CarriganTires(wear_out)
        self.assertFalse(carrigan.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        wear_out = [0.9, 0.9, 0.3, 0.9]
        octoprime = octoprime_tires.OctoprimeTires(wear_out)
        self.assertTrue(octoprime.needs_service())

    def test_engine_should_not_be_serviced(self):
        wear_out = [0.9, 0.8, 0.3, 0.9]
        octoprime = octoprime_tires.OctoprimeTires(wear_out)
        self.assertFalse(octoprime.needs_service())

if __name__ == '__main__':
    unittest.main()
