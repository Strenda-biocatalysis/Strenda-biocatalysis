[Landing Page](/Readme.md)
# Reactants

Each additive of a reaction must be defined like substrate, cosubstrate, coenzyme, etc. Exlcuded are only [biocatalyst](https://github.com/StephanM87/Strenda-biocatalysis/blob/main/ModelExamples/Biocatalyst/Readme.md) and the [solvents](https://github.com/StephanM87/Strenda-biocatalysis/tree/main/ModelExamples/Reaction_conditions).

### Reactant

To be defined for each reactant.

- __name__
  - Type: string
  - Description: Name of the reactant

- __smiles__
  - Type: string
  - Description: Smiles code of the reactant

- __persistent_identifier_PID__
  - Type: string
  - Description: One or more identifiers that refer to the compound, such as CAS number, PubChem code, InChI code, etc.

- __concentration__
  - Type: float
  - Description: Name of the reactant

- __supplier__
  - Type: string
  - Description: Information about the source of the compound, usually a commercial supplier with perhaps product code, but could be preparation in a research lab.

- __purity__
  - Type: float
  - Description: Purity of the reactant

- __formulation__
  - Type: string
  - Description: Formulation of the reactant (powder, liquid)

<hr>

### StorageConditions

Description of how the reactants were stored.

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
 
<hr>
