from typing import Optional, Union
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from pydantic.types import PositiveFloat

from .biocatalystbase import BiocatalystBase


@forge_signature
class SolubleBiocatalyst(BiocatalystBase):

    """soluble biocatlyst"""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("solublebiocatalystINDEX"),
        xml="@id",
    )
    concentration: PositiveFloat = Field(
        ...,
        description="Concentration of the biocatalyst.",
    )

    concentration_det_method: str = Field(
        ...,
        description="Method on how the concentration has been determined.",
    )

    __repo__: Optional[str] = PrivateAttr(default="None")
