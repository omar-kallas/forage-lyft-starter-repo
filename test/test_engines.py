import unittest

from engine import *

class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_milage = 10000
        current_milage = 50000
        capulet = capulet_engine.CapuletEngine(last_service_milage, current_milage)
        self.assertTrue(capulet.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_milage = 10000
        current_milage = 30000
        capulet = capulet_engine.CapuletEngine(last_service_milage, current_milage)
        self.assertFalse(capulet.needs_service())

    def test_engine_should_just_be_serviced(self):
        last_service_milage = 10000
        current_milage = 40001
        capulet = capulet_engine.CapuletEngine(last_service_milage, current_milage)
        self.assertTrue(capulet.needs_service())

class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_milage = 10000
        current_milage = 80000
        willoughby = willoughby_engine.WilloughbyEngine(last_service_milage, current_milage)
        self.assertTrue(willoughby.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_milage = 10000
        current_milage = 50000
        willoughby = willoughby_engine.WilloughbyEngine(last_service_milage, current_milage)
        self.assertFalse(willoughby.needs_service())

    def test_engine_should_just_be_serviced(self):
        last_service_milage = 10000
        current_milage = 70001
        willoughby = willoughby_engine.WilloughbyEngine(last_service_milage, current_milage)
        self.assertTrue(willoughby.needs_service())

class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        sternman = sternman_engine.SternmanEngine(warning_light_is_on)
        self.assertTrue(sternman.needs_service())
    
    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        sternman = sternman_engine.SternmanEngine(warning_light_is_on)
        self.assertFalse(sternman.needs_service())

if __name__ == '__main__':
    unittest.main()
