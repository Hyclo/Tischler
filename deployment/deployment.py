class deployment():
    def __init__(self):
        self.stopper = 1

    def get_stopper(self):
        return self.stopper
    
    def set_stopper(self, newValue):
        self.stopper = newValue
        