from sdRDM import DataModel, Field
from typing import Optional


class Enzyme(DataModel):

    """Description of the biocatalyst"""

    name: str = Field(
        ...,
        description="Name of the biocatalyst",
    )

    reaction: str = Field(
        ...,
        description="Reaction in which the biocatalyst is activ.",
    )

    sequence: str = Field(
        ...,
        description="Amino acid sequence of the biocatalyst.",
    )

    host_organism: str = Field(
        ...,
        description="Organism used for expression.",
    )


new_enzyme = Enzyme(name="enz", 
                    reaction="addsa", 
                    sequence="dsadsa", 
                    host_organism="asddsa")

new_desc = new_enzyme.json()

print(new_desc[0])

