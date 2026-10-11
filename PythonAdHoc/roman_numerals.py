import pprint

class RomanNumeral:
    """Class representing some Roman numerals and their int 
       values.
    """
    int_values = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'X': 10}
    def __init__(self, label: str):
        self.label = label
    def __int__(self) -> int:
        return RomanNumeral.int_values[self.label]
    
rn1 = RomanNumeral('X')

print(f'\nRomanNumeral.__doc__: {RomanNumeral.__doc__}\n')
print(f'rn1.__doc__: {rn1.__doc__}\n')
print(f'RomanNumeral.__class__: {RomanNumeral.__class__}\n')
print(f'rn1.__class__: {rn1.__class__}\n')
print(f'type(RomanNumeral): {type(RomanNumeral)}\n')
print(f'type(rn1): {type(rn1)}\n')
#print(f'RomanNumeral.__dir__(): {RomanNumeral.__dir__()}') #TypeError: unbound method object.__dir__() needs an argument
print(f'rn1.__dir__(): {rn1.__dir__()}\n')
print(f'dir(RomanNumeral): {dir(RomanNumeral)}\n')
print(f'dir(rn1): {dir(rn1)}\n')
print(f'RomanNumeral.__dict__: {RomanNumeral.__dict__}\n')
print(f'rn1.__dict__: {rn1.__dict__}\n')
#print(f'RomanNumeral.__repr__(): {RomanNumeral.__repr__()}\n') #TypeError: descriptor '__repr__' of 'object' object needs an argument
print(f'rn1.__repr__(): {rn1.__repr__()}\n')
print(f'rn1.__init__: {rn1.__init__}\n')
#print(rn1.__bases__)  # AttributeError: 'RomanNumeral' object has no attribute '__bases__
#print(rn1.__name__) AttributeError: 'RomanNumeral' object has no attribute '__name__'. Did you mean: '__ne__'?
print(f'int(rn1): {int(rn1)}\n')
print(f'RomanNumeral.__name__: {RomanNumeral.__name__}\n')
print(f'RomanNumeral.__bases__: {RomanNumeral.__bases__}\n')
print(f'type(int): {type(int)}\n')
print(f'type(type): {type(type)}\n')
print(f'type(object): {type(object)}\n')
pprint.pprint(globals())