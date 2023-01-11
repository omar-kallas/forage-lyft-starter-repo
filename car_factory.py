from car import Car
from engines import *
from batteries import *
from datetime import date

class CarFactory():
    def create_calliope():
        engine = capulet_engine.CapuletEngine(0, 0)
        battery = spindler_battery.SpindlerBattery(date.today(), date.today())
        car = Car(engine, battery)

        return car

    def create_glissade():
        engine = willoughby_engine.WilloughbyEngine(0, 0)
        battery = spindler_battery.SpindlerBattery(date.today(), date.today())
        car = Car(engine, battery)

        return car

    def create_palindrome():
        engine = sternman_engine.SternmanEngine(False)
        battery = spindler_battery.SpindlerBattery(date.today(), date.today())
        car = Car(engine, battery)

        return car

    def create_rorschach():
        engine = willoughby_engine.WilloughbyEngine(0, 0)
        battery = nubbin_battery.NubbinBattery(date.today(), date.today())
        car = Car(engine, battery)

        return car

    def create_thovex():
        engine = capulet_engine.CapuletEngine(0, 0)
        battery = nubbin_battery.NubbinBattery(date.today(), date.today())
        car = Car(engine, battery)

        return car