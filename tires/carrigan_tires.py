from tires.tires import Tires

class CarriganTires(Tires):
    def __init__(self, wear_out):
        self.wear_out = wear_out

    def needs_service(self):
        for m in self.wear_out:
            if m >= 0.9:
                return True
        
        return False