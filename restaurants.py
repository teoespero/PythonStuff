class Restaurants():
    """ a simple restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        return f'{self.restaurant_name.title()} offers {self.cuisine_type}.'

restaurant01 = Restaurants('Jollibee', 'fastfood')
restaurant02 = Restaurants('Noodle Bar', 'Vietnamese')
restaurant03 = Restaurants('Applebees', 'fine dining')

print(restaurant01.describe_restaurant())
print(restaurant02.describe_restaurant())
print(restaurant03.describe_restaurant())