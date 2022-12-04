
[back to main](/Readme.md)
# Reactants

This document contains all information about the attributes required to describe reactants


### Reactant

basic info about the reactant

- __name__
  - Type: string
  - Description: name of the reactant

- __smiles__
  - Type: string
  - Description: smiles code of the reactant

- __database_url__
  - Type: string
  - Description: url or identifier (doi) of the reactant

- __concentration__
  - Type: float
  - Description: Name of the reactant

- __origin__
  - Type: string
  - Description: supplier of the enzyme

- __purity__
  - Type: float
  - Description: purity of the reactant

- __formulation__
  - Type: string
  - Description: formulation of the reactant (powder, liquid)

### StorageConditions [_Reactant_]

- __temperature__
  - Type: float
  - Description: storage tmeperature (-20°C, -80°C)

- __storage_start__
  - Type: date
  - Description: when was the reactant stored

- __removing/rethawing__
  - Type: sting
  - Description: was the reactant removed from storage or rethawed?

- __thawing_process__
  - Type: string
  - Description: how was the reactant frozen, any special deviced