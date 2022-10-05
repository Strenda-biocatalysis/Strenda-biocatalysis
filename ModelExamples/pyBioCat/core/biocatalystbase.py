import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional


@forge_signature
class BiocatalystBase(sdRDM.DataModel):

    """basic info about the biocatalyst"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("biocatalystbaseINDEX"),
        xml="@id",
    )
    name: str = Field(
        ...,
        description="Name of the biocatalyst",
    )

    ecnumber: Optional[str] = Field(
        description="Code used to determine the family of a protein.",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(default="None")


new_biocatalyst = BiocatalystBase(id="e1", name="ADH", ecnumber="1.1.1.1")

print(new_biocatalyst.dict())
