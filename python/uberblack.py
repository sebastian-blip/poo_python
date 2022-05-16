from python.car import Car


class UberBlack(Car):
    typercaraccept = []
    seatsmaterial = []

    def __init__(self, license, driver, typercaraccept, seatsmaterial):
        super(UberBlack, self).__init__(license, driver)

        self.typercaraccept = typercaraccept
        self.seatsmaterial = seatsmaterial