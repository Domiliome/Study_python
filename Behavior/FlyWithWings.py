from Behavior.FlyBehavior import FlyBehavior


class FlyWithWings(FlyBehavior):
    def __init__(self):
        super().__init__()

    def fly(self):
        print("Fly with wings")
