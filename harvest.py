############
# Part 1   #
############

class MelonType(object):
    """A species of melon at a melon farm."""
    # all_melon_types = []

    def __init__(self, code, name, first_harvest, color, is_seedless, is_bestseller):
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        self.pairings = []

    


    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
                
        # fido = Animal()
        # fido.name = 'Fido'

        # self.pairings = 'mint'
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


all_melon_types = [] 

def make_melon_types():
    """Returns a list of current melon types."""

    
    
    musk = MelonType('musk', 'Muskmelon', 1998, 'green',
                     True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 'Casaba', 2003, 'orange',
                     False, False)
    cas.add_pairing('mint')
    cas.add_pairing('strawberries')
    all_melon_types.append(cas)

    cren = MelonType('cren', 'Crenshaw', 1996, 'green',
                     False, False)
    cren.add_pairing('proscuitto')
    all_melon_types.append(cren)

    yw = MelonType('yw', 'Yellow Watermelon', 2013, 'yellow',
                   False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)
    
    print(all_melon_types)
    return all_melon_types
    
def print_pairing_info(self):
    """Prints information about each melon type's pairings."""

    print(f'{self.name} pairs with {self.pairings}')

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # dict_melons = {
    # MelonType.code : MelonType.name
    # }

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 



