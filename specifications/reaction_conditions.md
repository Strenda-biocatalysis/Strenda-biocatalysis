---
repo: "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis"
prefix: "stbc"
imports:
    utils: ./utils.md
---


# Reaction Conditions Specification

This specification defines the structure and properties of reaction conditions used in enzymatic reactions, providing comprehensive documentation for reactor setup, reaction system characteristics, temperature and pH profiles.

## Types

### Reaction Conditions

Comprehensive specification of the physical and chemical conditions under which a biocatalytic reaction is performed, including reactor setup, reaction system characteristics, temperature and pH profiles.

- **reactor**
  - Type: Reactor Setup
  - Description: Configuration and specifications of the reactor used for the biocatalytic reaction.
- **system**
  - Type: Reaction System
  - Description: Characterization of the reaction system as monoliquid or multiphasic.
- phases
  - Type: Phase[]
  - Description: Individual phases present in the reaction system (liquid, solid, gas).
- temperature
  - Type: Temperature Profile
  - Description: Temperature conditions throughout the reaction, which can be constant, event-based, or follow a gradient.
- pH
  - Type: pH Profile
  - Description: pH conditions throughout the reaction, which can be constant, event-based, or follow a gradient.
- notes
  - Type: string
  - Description: Additional notes or comments about the reaction conditions.

### Reactor Setup

Configuration and operational parameters of the reactor system used for the biocatalytic reaction.

- **reactor type**
  - Type: Reactor Type
  - Description: Type of reactor configuration used (well-mixed or tubular flow).
- flow
  - Type: Flow Conditions
  - Description: Flow rate specifications for continuous or fed-batch operations.
- notes
  - Type: string
  - Description: Additional notes about the reactor setup.

### Flow Conditions

Specifications for flow rates in continuous or fed-batch reactor operations.

- flow rate
  - Type: float
  - Minimum: 0.0
  - Description: Numerical value of the flow rate.
- flow rate unit
  - Type: Unit Definition
  - Description: Unit of measurement for the flow rate.

---

## Reaction system (mono vs multiphasic)

### Reaction System

Characterization of the reaction system based on the number and types of phases present.

- **system type**
  - Type: SystemType
  - Description: Classification of the system as monoliquid or multiphasic.
- monoliquid
  - Type: Monoliquid System
  - Description: Specifications for single-phase liquid systems.
- multiphasic
  - Type: Multiphasic System
  - Description: Specifications for systems containing multiple phases.
- notes
  - Type: string
  - Description: Additional notes about the reaction system.

### Monoliquid System

Specifications for single-phase liquid reaction systems.

- solvent description
  - Type: string
  - Description: Detailed description of the solvent or solvent mixture used.
- ionic strength
  - Type: Quantity
  - Description: Ionic strength of the solution, affecting enzyme activity and stability.
- further additives
  - Type: string
  - Description: Description of any additional additives present in the system.
- notes
  - Type: string
  - Description: Additional notes about the monoliquid system.

### Multiphasic System

Specifications for reaction systems containing multiple distinct phases.

- phases number
  - Type: integer
  - Minimum: 0
  - Description: Total number of distinct phases present in the system.
- notes
  - Type: string
  - Description: Additional notes about the multiphasic system.

### Phase

Specification of individual phases within the reaction system.

- **phase type**
  - Type: Phase Type
  - Description: Physical state of the phase (liquid, solid, or gas).
- material description
  - Type: string
  - Description: Detailed description of the materials comprising this phase.
- amount
  - Type: Quantity
  - Description: Quantity of material in this phase.
- notes
  - Type: string
  - Description: Additional notes about this specific phase.

---

## Temperature profile (constant, event-based, dynamic, gradient)

### Temperature Profile

Specification of temperature conditions throughout the biocatalytic reaction, which can follow various patterns depending on the reaction requirements.

- **profile type**
  - Type: Profile Type
  - Description: Type of temperature profile used (constant, event-based, multipoint, or gradient).
- temperature unit
  - Type: Unit Definition
  - Description: Unit of measurement for temperature values.
- constant temperature
  - Type: float
  - Minimum: 0.0
  - Description: Temperature value for constant temperature profiles.
- profile points
  - Type: Profile Point[]
  - Description: Series of temperature points for event-based or multipoint profiles.
- gradient
  - Type: Gradient
  - Description: Gradient specifications for temperature ramp profiles.
- notes
  - Type: string
  - Description: Additional notes about the temperature profile.

### Profile Point

Individual temperature measurement point in time-based temperature profiles.

- value
  - Type: float
  - Minimum: 0.0
  - Description: Temperature value at this point.
- time
  - Type: float
  - Minimum: 0.0
  - Description: Time at which this temperature is measured or set.
- time unit
  - Type: Unit Definition
  - Description: Unit of measurement for the time value.
- event description
  - Type: string
  - Description: Description of any specific event associated with this temperature point.

### Gradient

Specification for temperature gradient profiles where temperature changes linearly over time or distance.

- start value
  - Type: float
  - Description: Initial temperature value at the beginning of the gradient.
- end value
  - Type: float
  - Description: Final temperature value at the end of the gradient.
- length
  - Type: float
  - Description: Duration or distance over which the gradient is applied.
- length unit
  - Type: Unit Definition
  - Description: Unit of measurement for the gradient length (time or distance).
- measurement points
  - Type: string
  - Description: Description of how temperature is measured along the gradient.

---

## pH profile (constant, event-based, dynamic, gradient)

### pH Profile

Specification of pH conditions throughout the biocatalytic reaction, which can follow various patterns to optimize enzyme activity and stability.

- **profile type**
  - Type: Profile Type
  - Description: Type of pH profile used (constant, event-based, multipoint, or gradient).
- constant pH
  - Type: float
  - Minimum: 0.0
  - Description: pH value for constant pH profiles.
- profile points
  - Type: pH Point[]
  - Description: Series of pH points for event-based or multipoint profiles.
- gradient
  - Type: pH Gradient
  - Description: Gradient specifications for pH ramp profiles.
- detection
  - Type: pH Detection
  - Description: Methods and conditions used for pH detection and measurement.
- notes
  - Type: string
  - Description: Additional notes about the pH profile.

### pH Point

Individual pH measurement point in time-based pH profiles.

- value
  - Type: float
  - Minimum: 0.0
  - Description: pH value at this point.
- time
  - Type: float
  - Minimum: 0.0
  - Description: Time at which this pH is measured or set.
- time unit
  - Type: Unit Definition
  - Description: Unit of measurement for the time value.
- event description
  - Type: string
  - Description: Description of any specific event associated with this pH point.

### pH Gradient

Specification for pH gradient profiles where pH changes linearly over time.

- start value
  - Type: float
  - Description: Initial pH value at the beginning of the gradient.
- end value
  - Type: float
  - Description: Final pH value at the end of the gradient.
- length
  - Type: float
  - Description: Duration over which the pH gradient is applied.
- length unit
  - Type: Unit Definition
  - Description: Unit of measurement for the gradient duration.
- measurement points
  - Type: float[]
  - Description: Measurement points along the gradient.

### pH Detection

Specifications for pH measurement methods and calibration conditions.

- detected when
  - Type: string
  - Description: Timing or conditions under which pH is detected.
- detected how
  - Type: string
  - Description: Method or instrument used for pH detection.
- temperature
  - Type: float
  - Description: Temperature at which pH measurements are calibrated or performed.
- temperature unit
  - Type: Unit Definition
  - Description: Unit of measurement for the calibration temperature.
- calibration pH electrode
  - Type: string
  - Description: Details about pH electrode calibration procedures and standards.

## Enumerations

### System Type

```python
MONOLIQUID = "monoliquid"
MULTIPHASIC = "multiphasic"
```

### Profile Type

```python
CONSTANT = "constant"
EVENT_BASED = "event_based"
MULTIPOINT = "multipoint"
GRADIENT = "gradient"
```
