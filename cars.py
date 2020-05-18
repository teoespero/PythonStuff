class Cars():

    def __init__(self, make, model, year):
        self.model = model
        self.make = make
        self.year = year
        self.odometerreading = 0

    def get_decriptive_name(self):

        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return  long_name.title()

    def read_odometer(self):
        print(f'This car has {self.odometerreading} miles on it')

    def update_odometer_reading(self, mileage):
        self.odometerreading = mileage


car01 = Cars('Toyota', 'Corolla', 2016)
print(car01.get_decriptive_name())
car01.update_odometer_reading(54)
car01.read_odometer()