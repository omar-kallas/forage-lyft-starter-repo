from tires.tires import Tires

class OctoprimeTires(Tires):
    def __init__(self, wear_out):
        self.wear_out = wear_out

    def needs_service(self):
        return sum(self.wear_out) >= 3