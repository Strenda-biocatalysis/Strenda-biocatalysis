---
repo: "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis"
prefix: "stbc"
imports:
    utils: ./utils.md
---

# Sampling Specification

This specification defines the structure and properties of sampling procedures and sample collection during enzymatic reactions, providing comprehensive documentation for sampling strategy, sample collection, and additional notes.

## Types

### Sampling

Specification for sampling procedures and sample collection during enzymatic reactions.

- **sampling applied**
  - Type: boolean
  - Description: Indicates whether physical sampling was performed at all.
- strategy
  - Type: Sampling Strategy
  - Description: Details about the sampling strategy and methodology used.
- samples
  - Type: Sample[]
  - Description: Collection of individual samples taken during the reaction.
- notes
  - Type: string
  - Description: Additional notes or comments about the sampling procedure.

### Sampling Strategy

Strategy and methodology for collecting samples during the reaction process.

- **strategy type**
  - Type: Sampling Strategy Type
  - Description: Type of sampling strategy employed (default or specialized).
- mixing during sampling
  - Type: string
  - Description: Description of mixing conditions maintained during sample collection.
- vessel opened
  - Type: boolean
  - Description: Indicates whether the reaction vessel was opened during sampling.
- gas phase
  - Type: string
  - Description: Description of gas phase conditions or handling during sampling.
- notes
  - Type: string
  - Description: Additional notes about the sampling strategy.

## Individual sample (time-resolved, phase-aware)

### Sample

Individual sample collected at a specific time point from a specific phase of the reaction.

- time
  - Type: float
  - Description: Time point at which the sample was collected.
- time unit
  - Type: Unit Definition
  - Description: Unit of measurement for the sampling time.
- amount
  - Type: Quantity
  - Description: Amount or volume of sample collected.
- phase
  - Type: Phase Type
  - Description: Phase from which the sample was collected (liquid, solid, gas, etc.).
- biocatalyst in sample
  - Type: string
  - Description: Description of biocatalyst presence or handling in the sample.
- preprocessing
  - Type: Sample Preprocessing
  - Description: Any preprocessing steps applied to the sample before analysis.
- notes
  - Type: string
  - Description: Additional notes about the individual sample.

### Sample Preprocessing

Preprocessing steps applied to samples before analysis to preserve or prepare them for measurement.

- quenching method
  - Type: string
  - Description: Method used to quench or stop the reaction in the sample.
- quenching ratio
  - Type: float
  - Description: Ratio or proportion of quenching agent to sample.
- treatment procedure
  - Type: string
  - Description: Additional treatment procedures applied to the sample.
- notes
  - Type: string
  - Description: Additional notes about sample preprocessing.

## Enumerations

### Sampling Strategy Type

```python
DEFAULT = "default"
SPECIALISED = "specialised"
```
