---
hide:
    - navigation
---

# Reaction Conditions Specification

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        reactionconditions(ReactionConditions)
        reactorsetup(ReactorSetup)
        flowconditions(FlowConditions)
        reactionsystem(ReactionSystem)
        monoliquidsystem(MonoliquidSystem)
        multiphasicsystem(MultiphasicSystem)
        phase(Phase)
        temperatureprofile(TemperatureProfile)
        profilepoint(ProfilePoint)
        gradient(Gradient)
        phprofile(PHProfile)
        phpoint(PHPoint)
        phgradient(PHGradient)
        phdetection(PHDetection)
        quantity(Quantity)
        storageconditions(StorageConditions)
        systemtype(SystemType)
        profiletype(ProfileType)
        formulationtype(FormulationType)
        phasetype(PhaseType)
        reactortype(ReactorType)
        reactionconditions(ReactionConditions) --> reactorsetup(ReactorSetup)
        reactionconditions(ReactionConditions) --> reactionsystem(ReactionSystem)
        reactionconditions(ReactionConditions) --> phase(Phase)
        reactionconditions(ReactionConditions) --> temperatureprofile(TemperatureProfile)
        reactionconditions(ReactionConditions) --> phprofile(PHProfile)
        reactorsetup(ReactorSetup) --> reactortype(ReactorType)
        reactorsetup(ReactorSetup) --> flowconditions(FlowConditions)
        reactionsystem(ReactionSystem) --> systemtype(SystemType)
        reactionsystem(ReactionSystem) --> monoliquidsystem(MonoliquidSystem)
        reactionsystem(ReactionSystem) --> multiphasicsystem(MultiphasicSystem)
        phase(Phase) --> phasetype(PhaseType)
        temperatureprofile(TemperatureProfile) --> profiletype(ProfileType)
        temperatureprofile(TemperatureProfile) --> profilepoint(ProfilePoint)
        temperatureprofile(TemperatureProfile) --> gradient(Gradient)
        phprofile(PHProfile) --> profiletype(ProfileType)
        phprofile(PHProfile) --> phpoint(PHPoint)
        phprofile(PHProfile) --> phgradient(PHGradient)
        phprofile(PHProfile) --> phdetection(PHDetection)

        click reactionconditions "#reactionconditions" "Go to ReactionConditions"
        click reactorsetup "#reactorsetup" "Go to ReactorSetup"
        click flowconditions "#flowconditions" "Go to FlowConditions"
        click reactionsystem "#reactionsystem" "Go to ReactionSystem"
        click monoliquidsystem "#monoliquidsystem" "Go to MonoliquidSystem"
        click multiphasicsystem "#multiphasicsystem" "Go to MultiphasicSystem"
        click phase "#phase" "Go to Phase"
        click temperatureprofile "#temperatureprofile" "Go to TemperatureProfile"
        click profilepoint "#profilepoint" "Go to ProfilePoint"
        click gradient "#gradient" "Go to Gradient"
        click phprofile "#phprofile" "Go to PHProfile"
        click phpoint "#phpoint" "Go to PHPoint"
        click phgradient "#phgradient" "Go to PHGradient"
        click phdetection "#phdetection" "Go to PHDetection"
        click quantity "#quantity" "Go to Quantity"
        click storageconditions "#storageconditions" "Go to StorageConditions"
        click systemtype "#systemtype" "Go to SystemType"
        click profiletype "#profiletype" "Go to ProfileType"
        click formulationtype "#formulationtype" "Go to FormulationType"
        click phasetype "#phasetype" "Go to PhaseType"
        click reactortype "#reactortype" "Go to ReactorType"
    ```


## Types


### ReactionConditions
Comprehensive specification of the physical and chemical conditions under which a biocatalytic reaction is performed, including reactor setup, reaction system characteristics, temperature and pH profiles.

__reactor__* [`ReactorSetup`](#reactorsetup)

- Configuration and specifications of the reactor used for the biocatalytic reaction.


__system__* [`ReactionSystem`](#reactionsystem)

- Characterization of the reaction system as monoliquid or multiphasic.


__phases__ [`list[Phase]`](#phase)

- Individual phases present in the reaction system (liquid, solid, gas).


__temperature__ [`TemperatureProfile`](#temperatureprofile)

- Temperature conditions throughout the reaction, which can be constant, event-based, or follow a gradient.


__pH__ [`PHProfile`](#phprofile)

- pH conditions throughout the reaction, which can be constant, event-based, or follow a gradient.


__notes__ `string`

- Additional notes or comments about the reaction conditions.


------

### ReactorSetup
Configuration and operational parameters of the reactor system used for the biocatalytic reaction.

__reactor_type__* [`ReactorType`](#reactortype)

- Type of reactor configuration used (well-mixed or tubular flow).


__flow__ [`FlowConditions`](#flowconditions)

- Flow rate specifications for continuous or fed-batch operations.


__notes__ `string`

- Additional notes about the reactor setup.


------

### FlowConditions
Specifications for flow rates in continuous or fed-batch reactor operations.

__flow_rate__ `float`

- Numerical value of the flow rate.
- `Minimum`: 0

__flow_rate_unit__ `string`

- Unit of measurement for the flow rate.


------

### ReactionSystem
Characterization of the reaction system based on the number and types of phases present.

__system_type__* [`SystemType`](#systemtype)

- Classification of the system as monoliquid or multiphasic.


__monoliquid__ [`MonoliquidSystem`](#monoliquidsystem)

- Specifications for single-phase liquid systems.


__multiphasic__ [`MultiphasicSystem`](#multiphasicsystem)

- Specifications for systems containing multiple phases.


__notes__ `string`

- Additional notes about the reaction system.


------

### MonoliquidSystem
Specifications for single-phase liquid reaction systems.

__solvent_description__ `string`

- Detailed description of the solvent or solvent mixture used.


__ionic_strength__ `float`

- Ionic strength of the solution, affecting enzyme activity and stability.


__further_additives__ `string`

- Description of any additional additives present in the system.


__notes__ `string`

- Additional notes about the monoliquid system.


------

### MultiphasicSystem
Specifications for reaction systems containing multiple distinct phases.

__phases_number__ `integer`

- Total number of distinct phases present in the system.
- `Minimum`: 0

__notes__ `string`

- Additional notes about the multiphasic system.


------

### Phase
Specification of individual phases within the reaction system.

__phase_type__* [`PhaseType`](#phasetype)

- Physical state of the phase (liquid, solid, or gas).


__material_description__ `string`

- Detailed description of the materials comprising this phase.


__amount__ `float`

- Quantity of material in this phase.


__amount_unit__ `string`

- Unit of measurement for the amount.


__notes__ `string`

- Additional notes about this specific phase.


------

### TemperatureProfile
Specification of temperature conditions throughout the biocatalytic reaction, which can follow various patterns depending on the reaction requirements.

__profile_type__* [`ProfileType`](#profiletype)

- Type of temperature profile used (constant, event-based, multipoint, or gradient).


__temperature_unit__ `string`

- Unit of measurement for temperature values.


__constant_temperature__ `float`

- Temperature value for constant temperature profiles.
- `Minimum`: 0

__profile_points__ [`list[ProfilePoint]`](#profilepoint)

- Series of temperature points for event-based or multipoint profiles.


__gradient__ [`Gradient`](#gradient)

- Gradient specifications for temperature ramp profiles.


__notes__ `string`

- Additional notes about the temperature profile.


------

### ProfilePoint
Individual temperature measurement point in time-based temperature profiles.

__value__ `float`

- Temperature value at this point.
- `Minimum`: 0

__time__ `float`

- Time at which this temperature is measured or set.
- `Minimum`: 0

__time_unit__ `string`

- Unit of measurement for the time value.


__event_description__ `string`

- Description of any specific event associated with this temperature point.


------

### Gradient
Specification for temperature gradient profiles where temperature changes linearly over time or distance.

__start_value__ `float`

- Initial temperature value at the beginning of the gradient.


__end_value__ `float`

- Final temperature value at the end of the gradient.


__length__ `float`

- Duration or distance over which the gradient is applied.


__length_unit__ `string`

- Unit of measurement for the gradient length (time or distance).


__measurement_points__ `string`

- Description of how temperature is measured along the gradient.


------

### PHProfile
Specification of pH conditions throughout the biocatalytic reaction, which can follow various patterns to optimize enzyme activity and stability.

__profile_type__* [`ProfileType`](#profiletype)

- Type of pH profile used (constant, event-based, multipoint, or gradient).


__constant_pH__ `float`

- pH value for constant pH profiles.
- `Minimum`: 0

__profile_points__ [`list[PHPoint]`](#phpoint)

- Series of pH points for event-based or multipoint profiles.


__gradient__ [`PHGradient`](#phgradient)

- Gradient specifications for pH ramp profiles.


__detection__ [`PHDetection`](#phdetection)

- Methods and conditions used for pH detection and measurement.


__notes__ `string`

- Additional notes about the pH profile.


------

### PHPoint
Individual pH measurement point in time-based pH profiles.

__value__ `float`

- pH value at this point.
- `Minimum`: 0

__time__ `float`

- Time at which this pH is measured or set.
- `Minimum`: 0

__time_unit__ `string`

- Unit of measurement for the time value.


__event_description__ `string`

- Description of any specific event associated with this pH point.


------

### PHGradient
Specification for pH gradient profiles where pH changes linearly over time.

__start_value__ `float`

- Initial pH value at the beginning of the gradient.


__end_value__ `float`

- Final pH value at the end of the gradient.


__length__ `float`

- Duration over which the pH gradient is applied.


__length_unit__ `string`

- Unit of measurement for the gradient duration.


__measurement_points__ `list[float]`

- Measurement points along the gradient.


------

### PHDetection
Specifications for pH measurement methods and calibration conditions.

__detected_when__ `string`

- Timing or conditions under which pH is detected.


__detected_how__ `string`

- Method or instrument used for pH detection.


__temperature__ `float`

- Temperature at which pH measurements are calibrated or performed.


__temperature_unit__ `string`

- Unit of measurement for the calibration temperature.


__calibration_pH_electrode__ `string`

- Details about pH electrode calibration procedures and standards.


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

### SystemType

| Alias | Value |
|-------|-------|
| `MONOLIQUID` | monoliquid |
| `MULTIPHASIC` | multiphasic |

### ProfileType

| Alias | Value |
|-------|-------|
| `CONSTANT` | constant |
| `EVENT_BASED` | event_based |
| `GRADIENT` | gradient |
| `MULTIPOINT` | multipoint |

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