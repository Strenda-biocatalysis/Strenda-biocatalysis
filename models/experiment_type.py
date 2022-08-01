from vessels import Vial


class BatchExperiment():
    '''
        Batch experiments contain all the reactants at the start of the experiment, do not get fed by substrates or other reactants and end after the experiment has been performed

        important attributes to describe batch experiments:

        Attributes:
            total_volume: Reaction volume
            reactor_type: Reaction vessel type 

        .. raw:: html

            <hr>
    '''

    

    def __init__(self, total_volume, working_volume):
        self.total_volume = total_volume
        self.working_volume = working_volume
        self.reactor_type = Vial


class ContinuousExperiment():
    '''
        Batch experiments contain all the reactants at the start of the experiment, do not get fed by substrates or other reactants and end after the experiment has been performed

        Attributes:
            Reactor_type: Reaction vessel type
            initial_volume: Starting volume
            final_volume: Volume at the end of the reaction
            resistance_time: ime one reactant stays in the system

    '''

    def __init__(self, total_volume, working_volume):
        self.total_volume = total_volume
        self.working_volume = working_volume
        self.reactor_type = Vial    