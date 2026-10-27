---
hide:
    - navigation
---

# Sampling Specification

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        sampling(Sampling)
        samplingstrategy(SamplingStrategy)
        sample(Sample)
        samplepreprocessing(SamplePreprocessing)
        quantity(Quantity)
        storageconditions(StorageConditions)
        samplingstrategytype(SamplingStrategyType)
        formulationtype(FormulationType)
        phasetype(PhaseType)
        reactortype(ReactorType)
        sampling(Sampling) --> samplingstrategy(SamplingStrategy)
        sampling(Sampling) --> sample(Sample)
        samplingstrategy(SamplingStrategy) --> samplingstrategytype(SamplingStrategyType)
        sample(Sample) --> phasetype(PhaseType)
        sample(Sample) --> samplepreprocessing(SamplePreprocessing)

        click sampling "#sampling" "Go to Sampling"
        click samplingstrategy "#samplingstrategy" "Go to SamplingStrategy"
        click sample "#sample" "Go to Sample"
        click samplepreprocessing "#samplepreprocessing" "Go to SamplePreprocessing"
        click quantity "#quantity" "Go to Quantity"
        click storageconditions "#storageconditions" "Go to StorageConditions"
        click samplingstrategytype "#samplingstrategytype" "Go to SamplingStrategyType"
        click formulationtype "#formulationtype" "Go to FormulationType"
        click phasetype "#phasetype" "Go to PhaseType"
        click reactortype "#reactortype" "Go to ReactorType"
    ```


## Types


### Sampling
Specification for sampling procedures and sample collection during enzymatic reactions.

__sampling_applied__* `boolean`

- Indicates whether physical sampling was performed at all.


__strategy__ [`SamplingStrategy`](#samplingstrategy)

- Details about the sampling strategy and methodology used.


__samples__ [`list[Sample]`](#sample)

- Collection of individual samples taken during the reaction.


__notes__ `string`

- Additional notes or comments about the sampling procedure.


------

### SamplingStrategy
Strategy and methodology for collecting samples during the reaction process.

__strategy_type__* [`SamplingStrategyType`](#samplingstrategytype)

- Type of sampling strategy employed (default or specialized).


__mixing_during_sampling__ `string`

- Description of mixing conditions maintained during sample collection.


__vessel_opened__ `boolean`

- Indicates whether the reaction vessel was opened during sampling.


__gas_phase__ `string`

- Description of gas phase conditions or handling during sampling.


__notes__ `string`

- Additional notes about the sampling strategy.


------

### Sample
Individual sample collected at a specific time point from a specific phase of the reaction.

__time__ `float`

- Time point at which the sample was collected.


__time_unit__ `string`

- Unit of measurement for the sampling time.


__amount__ `float`

- Amount or volume of sample collected.


__amount_unit__ `string`

- Unit of measurement for the amount.


__phase__ [`PhaseType`](#phasetype)

- Phase from which the sample was collected (liquid, solid, gas, etc.).


__biocatalyst_in_sample__ `string`

- Description of biocatalyst presence or handling in the sample.


__preprocessing__ [`SamplePreprocessing`](#samplepreprocessing)

- Any preprocessing steps applied to the sample before analysis.


__notes__ `string`

- Additional notes about the individual sample.


------

### SamplePreprocessing
Preprocessing steps applied to samples before analysis to preserve or prepare them for measurement.

__quenching_method__ `string`

- Method used to quench or stop the reaction in the sample.


__quenching_ratio__ `float`

- Ratio or proportion of quenching agent to sample.


__treatment_procedure__ `string`

- Additional treatment procedures applied to the sample.


__notes__ `string`

- Additional notes about sample preprocessing.


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

### SamplingStrategyType

| Alias | Value |
|-------|-------|
| `DEFAULT` | default |
| `SPECIALISED` | specialised |

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