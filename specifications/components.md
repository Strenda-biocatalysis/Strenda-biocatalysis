---
repo: "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis"
prefix: "stbc"
imports:
    utils: ./utils.md
---

# Components Specification

This specification defines the structure and properties of components used in enzymatic reactions, providing comprehensive documentation for component characterization, sourcing, application, and storage conditions.

## Types

### Reaction Component

Comprehensive specification of a single chemical component used in an enzymatic reaction, including its identity, role, quantity, source, and storage requirements.

- **identity**
  - Type: Component Identity
  - Description: Chemical identification and characterization of the component.
- role
  - Type: Component Role
  - Description: What this component does in the reaction (substrate, cosubstrate, salt, ...).
- amount
  - Type: Amount Concentration
  - Description: Quantity or concentration of the component used in the reaction.
- provenance
  - Type: Provenance
  - Description: Source and supplier information for the component.
- solubility
  - Type: Solubility Limit
  - Description: Solubility characteristics of the component under reaction conditions.
- storage
  - Type: Storage Conditions
  - Description: Storage requirements and conditions for the component.
- notes
  - Type: string[]
  - Description: Additional notes or comments about the component.

### Component Identity

Chemical identification and characterization information for a component, including names, structural identifiers, and physical properties.

- **name**
  - Type: string
  - Description: Common or systematic name of the component.
- smiles
  - Type: string
  - Description: SMILES (Simplified Molecular Input Line Entry System) notation for the chemical structure.
- identifiers
  - Type: Identifier[]
  - Description: One or more identifiers like CAS, PubChem CID, InChI, etc.
- purity
  - Type: float
  - Description: Purity of the component as a percentage or fraction.
- formulation
  - Type: Formulation Type
  - Description: Physical form or formulation of the component (powder, liquid, solution, etc.).

### Amount Concentration

Quantitative specification of component amount or concentration used in the reaction.

- value
  - Type: float
  - minimum: 0.0
  - Description: Numerical value of the amount or concentration.
- unit
  - Type: Unit Definition
  - Description: Unit of measurement for the amount or concentration.

### Provenance

Source and supplier information for component traceability and reproducibility.

- supplier
  - Type: string
  - Description: Supplier/manufacturer or "prepared in lab"; include product code or citation if applicable.

### Solubility Limit

Solubility characteristics of the component under specific conditions.

- value
  - Type: float
  - minimum: 0.0
  - Description: Numerical value of the solubility limit.
- unit
  - Type: Unit Definition
  - Description: Unit of measurement for the solubility limit.

## Enumerations

### Component Role

```python
SUBSTRATE = "substrate"
COSUBSTRATE = "cosubstrate"
COENZYME = "coenzyme"
COFACTOR = "cofactor"
SALT = "salt"
ION = "ion"
SOLVENT = "solvent"
BUFFER = "buffer"
OTHER = "other"
```
