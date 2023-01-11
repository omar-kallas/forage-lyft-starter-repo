import unittest
from datetime import datetime

from battery import *

class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2025, 1, 1)
        nubbin = nubbin_battery.NubbinBattery(last_service_date, current_date)
        self.assertTrue(nubbin.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2023, 1, 1)
        nubbin = nubbin_battery.NubbinBattery(last_service_date, current_date)
        self.assertFalse(nubbin.needs_service())

    def test_engine_should_just_be_serviced(self):
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2024, 1, 2)
        nubbin = nubbin_battery.NubbinBattery(last_service_date, current_date)
        self.assertTrue(nubbin.needs_service())

class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2023, 1, 1)
        spindler = spindler_battery.SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spindler.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2021, 1, 1)
        spindler = spindler_battery.SpindlerBattery(last_service_date, current_date)
        self.assertFalse(spindler.needs_service())

    def test_engine_should_just_be_serviced(self):
        last_service_date = datetime(2020, 1, 1)
        current_date = datetime(2022, 1, 2)
        spindler = spindler_battery.SpindlerBattery(last_service_date, current_date)
        self.assertTrue(spindler.needs_service())

if __name__ == '__main__':
    unittest.main()
