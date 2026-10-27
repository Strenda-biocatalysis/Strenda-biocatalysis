---
hide:
    - navigation
---

# Operation Mode Specification

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        operationmode(OperationMode)
        feedingstrategy(FeedingStrategy)
        quantity(Quantity)
        storageconditions(StorageConditions)
        operationmodetype(OperationModeType)
        feedingtype(FeedingType)
        formulationtype(FormulationType)
        phasetype(PhaseType)
        reactortype(ReactorType)
        operationmode(OperationMode) --> operationmodetype(OperationModeType)
        operationmode(OperationMode) --> reactortype(ReactorType)
        operationmode(OperationMode) --> feedingstrategy(FeedingStrategy)
        feedingstrategy(FeedingStrategy) --> feedingtype(FeedingType)

        click operationmode "#operationmode" "Go to OperationMode"
        click feedingstrategy "#feedingstrategy" "Go to FeedingStrategy"
        click quantity "#quantity" "Go to Quantity"
        click storageconditions "#storageconditions" "Go to StorageConditions"
        click operationmodetype "#operationmodetype" "Go to OperationModeType"
        click feedingtype "#feedingtype" "Go to FeedingType"
        click formulationtype "#formulationtype" "Go to FormulationType"
        click phasetype "#phasetype" "Go to PhaseType"
        click reactortype "#reactortype" "Go to ReactorType"
    ```


## Types


### OperationMode
Specification of the operational mode and configuration for conducting biocatalytic reactions.

__mode__* [`OperationModeType`](#operationmodetype)

- The fundamental operation mode defining how the reaction is conducted (batch, fed-batch, continuous, or combinatorial).


__reactor_type__ [`ReactorType`](#reactortype)

- Type of reactor configuration used (well-mixed, tubular flow, or other).


__feeding__ [`FeedingStrategy`](#feedingstrategy)

- Strategy for feeding reactants into the system during the reaction.


__notes__ `string`

- Additional notes or comments about the operation mode.


------

### FeedingStrategy
Specification of the feeding strategy for introducing reactants during non-batch operations.

__feeding_type__ [`FeedingType`](#feedingtype)

- Type of feeding approach used (none, discrete, continuous, or variable).


__description__ `string`

- Detailed description of the feeding strategy implementation.


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

### OperationModeType

| Alias | Value |
|-------|-------|
| `BATCH` | batch |
| `COMBINATORIAL` | combinatorial |
| `CONTINUOUS` | continuous |
| `FED_BATCH` | fed_batch |

### FeedingType

| Alias | Value |
|-------|-------|
| `CONTINUOUS` | continuous |
| `DISCRETE` | discrete |
| `NONE` | none |
| `VARIABLE` | variable |

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