from python.car import Car


class UberVan(Car):

    ypercaraccept = []
    seatsmaterial = []

    def __init__(self, license, driver, typercaraccept, seatsmaterial):
        super(UberVan, self).__init__(license, driver)

        self.typercaraccept = typercaraccept
        self.seatsmaterial = seatsmaterial
