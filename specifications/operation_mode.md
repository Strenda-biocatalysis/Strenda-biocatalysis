---
repo: "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis"
prefix: "stbc"
imports:
    utils: ./utils.md
---

# Operation Mode Specification

This specification defines the structure and properties of operation modes used in enzymatic reactions, providing comprehensive documentation for reactor setup, feeding strategy, and additional notes.

## Types

### Operation Mode

Specification of the operational mode and configuration for conducting biocatalytic reactions.

- **mode**
  - Type: Operation Mode Type
  - Description: The fundamental operation mode defining how the reaction is conducted (batch, fed-batch, continuous, or combinatorial).
- reactor type
  - Type: Reactor Type
  - Description: Type of reactor configuration used (well-mixed, tubular flow, or other).
- feeding
  - Type: Feeding Strategy
  - Description: Strategy for feeding reactants into the system during the reaction.
- notes
  - Type: string
  - Description: Additional notes or comments about the operation mode.

### Feeding Strategy

Specification of the feeding strategy for introducing reactants during non-batch operations.

- feeding type
  - Type: Feeding Type
  - Description: Type of feeding approach used (none, discrete, continuous, or variable).
- description
  - Type: string
  - Description: Detailed description of the feeding strategy implementation.

## Enumerations

### Operation Mode Type

```python
BATCH = "batch"
FED_BATCH = "fed_batch"
CONTINUOUS = "continuous"
COMBINATORIAL = "combinatorial"
```

### Feeding Type

```python
NONE = "none"
DISCRETE = "discrete"
CONTINUOUS = "continuous"
VARIABLE = "variable"
```
