

class Vial:
    '''
        small vessel for small reactions

        Attributes:

        :dimension and volume: volume of the vessel
        :stirring and mixing: how fast was the shaking

    '''

    def __init__ (self, dimension, stirring):
        self.dimension = dimension
        self.stirring=stirring