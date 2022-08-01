



class StirredTankReactor:
    '''
        Stirred tank reactors are
        
        .. image:: assets/str.png
        
        
        Attributes:
            volume: maximal filling volume of the reactor
            height: height of the reactor
            width: width of the reactor
            bottom_type: has the reactor a flat bottom, a round bottom?
            working_volume: what was the working volume
        
        There are many attributes still missing

        .. raw:: html

            <hr>
    '''
    def __init__(self, volume, height,width, bootom_type, working_volume ):
        self.volume = volume
        self.height = height
        self.width = width
        self.bottom_type = bootom_type
        self.working_volume = working_volume


class Vial:
    '''
        vials are commoly used for small reaction volumes and simple reaction setups

        .. image:: assets/vial.png

        **The following attributes are needed to describe a vial reactor**

        Attributes:
            dimension_and_volume: volume of the vessel
            stirring_and_mixing: how fast was the shaking

        .. raw:: html

            <hr>
    '''

    def __init__(self, dimension, stirring):
        self.dimension = dimension
        self.stirring = stirring