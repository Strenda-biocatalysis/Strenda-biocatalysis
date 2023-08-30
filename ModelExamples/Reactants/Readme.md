[Landing Page](/Readme.md)
# Reactants

Each additive of a reaction must be defined like substrate, cosubstrate, cofator, etc. Exlcuded are only biocatalyst (Biocatalyst) and the solvents (Reaction conditions).

### Reactant

To be defined for each reactant.

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
  - Description: Start of storage

- __additives__
  - Type: string
  - Description: Were additives added, for example argon?

- __removing/rethawing__
  - Type: sting
  - Description: Was the reactant removed from storage or rethawed?

- __thawing_process__
  - Type: string
  - Description: How was the reactant frozen, any special device?
