---
hide:
    - navigation
---

# Components Specification

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        reactioncomponent(ReactionComponent)
        componentidentity(ComponentIdentity)
        amountconcentration(AmountConcentration)
        provenance(Provenance)
        solubilitylimit(SolubilityLimit)
        quantity(Quantity)
        storageconditions(StorageConditions)
        componentrole(ComponentRole)
        formulationtype(FormulationType)
        phasetype(PhaseType)
        reactortype(ReactorType)
        reactioncomponent(ReactionComponent) --> componentidentity(ComponentIdentity)
        reactioncomponent(ReactionComponent) --> componentrole(ComponentRole)
        reactioncomponent(ReactionComponent) --> amountconcentration(AmountConcentration)
        reactioncomponent(ReactionComponent) --> provenance(Provenance)
        reactioncomponent(ReactionComponent) --> solubilitylimit(SolubilityLimit)
        reactioncomponent(ReactionComponent) --> storageconditions(StorageConditions)
        componentidentity(ComponentIdentity) --> formulationtype(FormulationType)

        click reactioncomponent "#reactioncomponent" "Go to ReactionComponent"
        click componentidentity "#componentidentity" "Go to ComponentIdentity"
        click amountconcentration "#amountconcentration" "Go to AmountConcentration"
        click provenance "#provenance" "Go to Provenance"
        click solubilitylimit "#solubilitylimit" "Go to SolubilityLimit"
        click quantity "#quantity" "Go to Quantity"
        click storageconditions "#storageconditions" "Go to StorageConditions"
        click componentrole "#componentrole" "Go to ComponentRole"
        click formulationtype "#formulationtype" "Go to FormulationType"
        click phasetype "#phasetype" "Go to PhaseType"
        click reactortype "#reactortype" "Go to ReactorType"
    ```


## Types


### ReactionComponent
Comprehensive specification of a single chemical component used in an enzymatic reaction, including its identity, role, quantity, source, and storage requirements.

__identity__* [`ComponentIdentity`](#componentidentity)

- Chemical identification and characterization of the component.


__role__ [`ComponentRole`](#componentrole)

- What this component does in the reaction (substrate, cosubstrate, salt, ...).


__amount__ [`AmountConcentration`](#amountconcentration)

- Quantity or concentration of the component used in the reaction.


__provenance__ [`Provenance`](#provenance)

- Source and supplier information for the component.


__solubility__ [`SolubilityLimit`](#solubilitylimit)

- Solubility characteristics of the component under reaction conditions.


__storage__ [`StorageConditions`](#storageconditions)

- Storage requirements and conditions for the component.


__notes__ `string`

- Additional notes or comments about the component.


------

### ComponentIdentity
Chemical identification and characterization information for a component, including names, structural identifiers, and physical properties.

__name__* `string`

- Common or systematic name of the component.


__smiles__ `string`

- SMILES (Simplified Molecular Input Line Entry System) notation for the chemical structure.


__identifiers__ `list[string]`

- One or more identifiers like CAS, PubChem CID, InChI, etc.


__purity__ `float`

- Purity of the component as a percentage or fraction.


__formulation__ [`FormulationType`](#formulationtype)

- Physical form or formulation of the component (powder, liquid, solution, etc.).


------

### AmountConcentration
Quantitative specification of component amount or concentration used in the reaction.

__value__ `float`

- Numerical value of the amount or concentration.
- `Minimum`: 0

__unit__ `string`

- Unit of measurement for the amount or concentration.


------

### Provenance
Source and supplier information for component traceability and reproducibility.

__supplier__ `string`

- Supplier/manufacturer or "prepared in lab"; include product code or citation if applicable.


------

### SolubilityLimit
Solubility characteristics of the component under specific conditions.

__value__ `float`

- Numerical value of the solubility limit.
- `Minimum`: 0

__unit__ `string`

- Unit of measurement for the solubility limit.


------

### Quantity
Quantitative measurement with value and unit specification.

__value__ `float`

- Numerical value of the measurement.
- `Minimum`: 0

__unit__ `string`

- Unit of measurement for the value.


------

### StorageConditions
Conditions under which materials (biocatalysts, components, etc.) are stored to maintain stability and integrity.

__temperature__ `float`

- Storage temperature value.


__temperature_unit__ `string`

- Unit for the storage temperature (e.g., °C, K).


__storage_start__ `date`

- Date when storage under these conditions began or material was received.


__additives__ `list[string]`

- Any additives or stabilizers used during storage (e.g., glycerol, stabilizers, preservatives).


__drying_method__ `list[string]`

- Method used to dry the material if stored in dry form (optional, primarily for biocatalysts).


__notes__ `string`

- Additional notes about storage conditions or requirements.


## Enumerations

### ComponentRole

| Alias | Value |
|-------|-------|
| `BUFFER` | buffer |
| `COENZYME` | coenzyme |
| `COFACTOR` | cofactor |
| `COSUBSTRATE` | cosubstrate |
| `ION` | ion |
| `OTHER` | other |
| `PRODUCT` | product |
| `SALT` | salt |
| `SOLVENT` | solvent |
| `SUBSTRATE` | substrate |

### FormulationType

| Alias | Value |
|-------|-------|
| `DISSOLVED` | dissolved |
| `GAS` | gas |
| `LIQUID` | liquid |
| `OTHER` | other |
| `POWDER` | powder |
| `SOLUTION` | solution |

### PhaseType

| Alias | Value |
|-------|-------|
| `GAS` | gas |
| `LIQUID` | liquid |
| `MIXED` | mixed |
| `OTHER` | other |
| `SOLID` | solid |

### ReactorType

| Alias | Value |
|-------|-------|
| `OTHER` | other |
| `TUBULAR_FLOW` | tubular_flow |
| `WELL_MIXED` | well_mixed |