from car import Car
from engine import *
from battery import *

class CarFactory:
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)

        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)

        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_is_on):
        engine = sternman_engine.SternmanEngine(warning_light_is_on)
        battery = spindler_battery.SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)

        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)

        return car

    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery = nubbin_battery.NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)

        return car