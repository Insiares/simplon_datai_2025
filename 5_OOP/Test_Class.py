
class Pizza:
    
    def __init__(self, topping, base, crust):
        self._topping = topping
        self._base = base
        self._crust = crust

    @property
    def crust(self):
        return self._crust
    
    @crust.setter
    def crust(self, value):
        self._crust = value

    @property
    def topping(self):
        return self._topping
    
    @topping.setter
    def topping(self, value):
        self._topping = value

    @property
    def base(self):
        return self._base
    
    @base.setter
    def base(self, value):
        self._base = value
    
    def __add__(self, ajout):
        self._topping = (self._topping) + ' et ' + (ajout)

    def __str__(self):
        return f'Base {self._base}, croûte {self._crust}, garnie de {self._topping}'
    


ma_pizza = Pizza('Chorizo', 'Tomate', 'croustillante')

print(ma_pizza)

ma_pizza + 'Jambon'

print(ma_pizza)