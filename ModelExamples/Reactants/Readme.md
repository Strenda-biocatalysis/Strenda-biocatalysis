[Landing Page](/Readme.md)
# Reactants

This document contains all information about the attributes required to describe reactants


### Reactant

basic info about the reactant

- __name__
  - Type: string
  - Description: Name of the reactant

- __smiles__
  - Type: string
  - Description: Smiles code of the reactant

- __database_url__
  - Type: string
  - Description: Url or identifier (DOI) of the reactant

- __concentration__
  - Type: float
  - Description: Name of the reactant

- __origin__
  - Type: string
  - Description: Supplier of the reactant

- __purity__
  - Type: float
  - Description: Purity of the reactant

- __formulation__
  - Type: string
  - Description: Formulation of the reactant (powder, liquid)

### StorageConditions

- __temperature__
  - Type: float
  - Description: Storage tmeperature (-20°C, -80°C)

- __storage_start__
  - Type: date
  - Description: When was the reactant stored?

- __additives__
  - Type: string
  - Description: Were additives added, for example glycerol?

- __removing/rethawing__
  - Type: sting
  - Description: Was the reactant removed from storage or rethawed?

- __thawing_process__
  - Type: string
  - Description: How was the reactant frozen, any special device?
