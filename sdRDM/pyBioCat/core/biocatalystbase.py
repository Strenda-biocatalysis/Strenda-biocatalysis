import sdRDM


from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from pydantic import Field
from typing import Optional


class BiocatalystBase(sdRDM.DataModel):

    """Do fugiat mollit sit duis deserunt dolor ex. Quis do occaecat dolor consectetur nostrud occaecat eu sint aute. Laboris commodo laborum proident id laboris cupidatat amet commodo tempor laborum sint occaecat mollit velit."""

    name: str = Field(
        ...,
        description="Name of the biocatalyst",
    )

    ecnumber: Optional[str] = Field(
        description="Code used to determine the family of a protein.",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(default="None")


new_enzyme = BiocatalystBase(name="enzyme", ecnumber="1232")

print(new_enzyme.json())
