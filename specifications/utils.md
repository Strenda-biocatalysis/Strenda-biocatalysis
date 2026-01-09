---
repo: "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis"
prefix: "stbc"
---

# Shared Utility Types

This specification defines shared types and enumerations used across multiple specifications in the Strenda-biocatalysis project.

## Types

### Quantity

Quantitative measurement with value and unit specification.

- value
  - Type: float
  - Minimum: 0.0
  - Description: Numerical value of the measurement.
- unit
  - Type: Unit Definition
  - Description: Unit of measurement for the value.

### Storage Conditions

Conditions under which materials (biocatalysts, components, etc.) are stored to maintain stability and integrity.

- temperature
  - Type: float
  - Description: Storage temperature value.
- temperature unit
  - Type: Unit Definition
  - Description: Unit for the storage temperature (e.g., °C, K).
- storage start
  - Type: date
  - Description: Date when storage under these conditions began or material was received.
- additives
  - Type: string[]
  - Description: Any additives or stabilizers used during storage (e.g., glycerol, stabilizers, preservatives).
- drying method
  - Type: string[]
  - Description: Method used to dry the material if stored in dry form (optional, primarily for biocatalysts).
- notes
  - Type: string[]
  - Description: Additional notes about storage conditions or requirements.

## Enumerations

### Formulation Type

Enumeration of physical formulations in which materials can be obtained or stored.

```python
DISSOLVED = "dissolved"
POWDER = "powder"
LIQUID = "liquid"
GAS = "gas"
SOLUTION = "solution"
OTHER = "other"
```

### Phase Type

Enumeration of physical phases present in reaction systems or samples.

```python
LIQUID = "liquid"
SOLID = "solid"
GAS = "gas"
MIXED = "mixed"
OTHER = "other"
```

### Reactor Type

Enumeration of reactor configurations used for biocatalytic reactions.

```python
WELL_MIXED = "well_mixed"
TUBULAR_FLOW = "tubular_flow"
OTHER = "other"
```
