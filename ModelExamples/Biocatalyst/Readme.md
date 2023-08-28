[Landing Page](/Readme.md)

# Biocatalyst

This document contains all information required to unambiguously identify the catalyst and its formulation. 

At first, it needs to be identified if the enzyme or biocatalyst was obtained by purchasing it from a company or if it was produced by yourself or a colleague. In every case different metadata are required to describe the enzyme unambiguously.


<details> <Summary>Biocatalyst purchased</Summary>

### BiocatalystPurchased

basic info about the biocatalyst

- __name*__
  - Type: string
  - Description: Name of the biocatalyst
- __ecnumber__
  - Type: string
  - Description: Code used to determine the family of a protein.

- __chemical_reaction__
  - Type: string
  - Description: reactio catalysed by the enzyme

- __sequence__
  - Type: string
  - Description: Amono acid sequence of the enzyme

- __origin_organism__
  - Type: string
  - Description: Organism from which the enzyme was extracted or identfied

- __production_organism__
  - Type: string
  - Description: Organism in which the enzyme was produced

- __postranslational_modification__
  - Type: string
  - Description: Code used to determine the family of a protein.

- __supplier__
  - Type: string
  - Company from which the enzyme was purchased

- __purity__
  - Type: float
  - Description: purity of the enzyme

- __purity_specification__
  - Type: string
  - Description: description of how the purity of the biocatalyst was determined. In case of purchased enzymes, this information is often available in the product specification sheet.

- __formulation__
  - Type: string
  - Description: formulation of the biocatlyst, eg powder, solution etc.

</details>

<details> <Summary>Biocatalyst self-produced</Summary>

### BiocatalystSelfProduced

basic info about the self producted biocatalyst

- __name*__
  - Type: string
  - Description: Name of the biocatalyst

- __ecnumber__
  - Type: string
  - Description: Code used to determine the family of a protein

- __chemical_reaction__
  - Type: string
  - Description: reaction catalysed by the enzyme

- __sequence__
  - Type: string
  - Description: Amino acid sequence of the enzyme

- __origin_organism__
  - Type: string
  - Description: Organism from which the enzyme was extracted or identfied

- __production_organism__
  - Type: string
  - Description: Organism in which the enzyme was produced

- __postranslational_modification__
  - Type: string
  - Description: Code used to determine the family of a protein

- __supplier__
  - Type: string
  - Company from which the enzyme was purchased

- __purity__
  - Type: float
  - Description: purity of the enzyme

- __purity_specification__
  - Type: string
  - Description: description of how the purity of the biocatalyst was determined

- __formulation__
  - Type: string
  - Description: formulation of the biocatalyst, eg powder, solution etc.


- __purification_method__
  - Type: string
  - Description: method used for purification of the enyme

</details>


# Formulation and immobilisation

With a enzyme purchased or self-produced it needs to be specified, how it was used in the reaction. We have identified two categories in which a biocatalyst can be applied to a reaction: immobilised, or non immobilised.

## Non immobilised biocatalysts

<details> <Summary>Soluble biocatalyst</Summary>

### SolubleBiocatalyst [_BiocatalystselfProduced_]

soluble biocatlyst

- __concentration*__
  - Type: posfloat
  - Description: Concentration of the biocatalyst

- __activity__:
  - Type: float
  - Description: Acitivity of the enzyme in U/mg or U/mL

- __concentration_det_method*__
  - Type: string
  - Description: Method on how the concentration has been determined

- __formulation__
  - Type: string
  - Description: Formulation of the biocatalyst, eg powder, solution etc.

- __purification_procedure__
  - Type: string
  - Description: Method used to purifiy the biocatalyst

</details>

<details> <Summary>Crude cell extract</Summary>
### CrudeCellExtract [_BiocatalystselfProduced_]

- __cell_disruption_process__
  - Type: string
  - Description: Method how the cells were disrupted

- __concentration__
  - Type: float
  - Description: Concentration of the enzyme on the immobilised phase

- __concentration_determination_method__
  - Type: string
  - Description: Method how the concentration was measured

</details>

<details> <Summary>Whole cell biocatalyst</Summary>

### WholeCellBiocatalyst [_BiocatalystselfProduced_]

- __harvesting_method__
  - Type: string
  - Description: How were the cells harvested

- __formulation__
  - Type: string
  - Description: formulation of the catalyst (wet cells, lyophillised?)

</details>

<details> <Summary>Supernatant</Summary>

### Supernatant [_BiocatalystselfProduced_]

- __production_organism__
  - Type: string
  - Description: Which organism was producing and secreting the biocatalyst?

- __separation_method__
  - Type: string
  - Description: The method of how the supernatant was separated from the cells

</details>

<details> <Summary>Cell-free-production</Summary>

### Cell free production [_BiocatalystselfProduced_]

????

</details>



## Immobilised biocatalysts

<details> <Summary>immobilised biocatalyst</Summary>

### ImmobilisedBiocatalyst [_BiocatalystselfProduced_]


- __purification_procedure__
  - Type: string
  - Description: Method for purifying the enzyme

- __immobilisation_procedure__
  - Type: string
  - Description: Procedure for immobilising the enzyme

- __concentration__
  - Type: float
  - Description: Concentration of the enzyme on the immobilised phase

- __concentration_determination_method__
  - Type: string
  - Description: Method how the concentration was measured

</details>

<details> <Summary>Immobilisation procedure</Summary>

### Immobilisation_procedure [_BiocatalystselfProduced_]

???

</details>

# Storage conditions

The last question to be answered for decribing the biocatalyst is how it has been stored until it was used in the reaction.


<details> <Summary>storage conditions</Summary>

### StorageConditions [_BiocatalystselfProduced_]

- __temperature__
  - Type: float
  - Description: Storage temperature (-20°C, -80°C)

- __storage_start__
  - Type: date
  - Description: When did storage start?

- __additives__
  - Type: string
  - Description: Were additives added, for example glycerol?

- __removing/rethawing__
  - Type: sting
  - Description: How was the catalyst removed from storage or rethawed?

- __thawing_process__
  - Type: string
  - Description: How was the catalyst frozen, any special devices or additives?

</details>
