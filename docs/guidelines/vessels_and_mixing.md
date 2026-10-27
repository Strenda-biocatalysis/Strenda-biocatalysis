---
hide:
    - navigation
---

# Vessels and Mixing Specification

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        vesselandmixing(VesselAndMixing)
        vessel(Vessel)
        closure(Closure)
        reactorspecifics(ReactorSpecifics)
        gashandling(GasHandling)
        mixing(Mixing)
        shakingmixing(ShakingMixing)
        mechanicalmixing(MechanicalMixing)
        stirbar(StirBar)
        fluidimpelledmixing(FluidImpelledMixing)
        quantity(Quantity)
        storageconditions(StorageConditions)
        vesseltype(VesselType)
        mixingtype(MixingType)
        formulationtype(FormulationType)
        phasetype(PhaseType)
        reactortype(ReactorType)
        vesselandmixing(VesselAndMixing) --> vessel(Vessel)
        vesselandmixing(VesselAndMixing) --> mixing(Mixing)
        vessel(Vessel) --> vesseltype(VesselType)
        vessel(Vessel) --> closure(Closure)
        vessel(Vessel) --> reactorspecifics(ReactorSpecifics)
        reactorspecifics(ReactorSpecifics) --> gashandling(GasHandling)
        mixing(Mixing) --> mixingtype(MixingType)
        mixing(Mixing) --> shakingmixing(ShakingMixing)
        mixing(Mixing) --> mechanicalmixing(MechanicalMixing)
        mixing(Mixing) --> fluidimpelledmixing(FluidImpelledMixing)
        mechanicalmixing(MechanicalMixing) --> stirbar(StirBar)

        click vesselandmixing "#vesselandmixing" "Go to VesselAndMixing"
        click vessel "#vessel" "Go to Vessel"
        click closure "#closure" "Go to Closure"
        click reactorspecifics "#reactorspecifics" "Go to ReactorSpecifics"
        click gashandling "#gashandling" "Go to GasHandling"
        click mixing "#mixing" "Go to Mixing"
        click shakingmixing "#shakingmixing" "Go to ShakingMixing"
        click mechanicalmixing "#mechanicalmixing" "Go to MechanicalMixing"
        click stirbar "#stirbar" "Go to StirBar"
        click fluidimpelledmixing "#fluidimpelledmixing" "Go to FluidImpelledMixing"
        click quantity "#quantity" "Go to Quantity"
        click storageconditions "#storageconditions" "Go to StorageConditions"
        click vesseltype "#vesseltype" "Go to VesselType"
        click mixingtype "#mixingtype" "Go to MixingType"
        click formulationtype "#formulationtype" "Go to FormulationType"
        click phasetype "#phasetype" "Go to PhaseType"
        click reactortype "#reactortype" "Go to ReactorType"
    ```


## Types


### VesselAndMixing
Specification of the vessel and mixing configuration for conducting biocatalytic reactions.

__vessel__* [`Vessel`](#vessel)

- Physical container or reactor used for the enzymatic reaction.


__mixing__ [`Mixing`](#mixing)

- Mixing system and parameters employed during the reaction.


__notes__ `string`

- Additional notes or comments about the vessel and mixing setup.


------

### Vessel
Physical container or reactor specification for enzymatic reactions.

__vessel_type__* [`VesselType`](#vesseltype)

- Type of vessel or reactor configuration used for the reaction.


__material__ `string`

- Material composition of the vessel (e.g., glass, plastic, stainless steel).


__size__ `float`

- Volume or capacity of the vessel.


__size_unit__ `string`

- Unit of measurement for the size.


__geometry__ `string`

- Geometric shape and dimensions of the vessel.


__closure__ [`Closure`](#closure)

- Sealing and closure system for the vessel.


__supplier__ `string`

- Manufacturer or supplier of the vessel.


__lot_number__ `string`

- Batch or lot number for traceability.


__reactor_specifics__ [`ReactorSpecifics`](#reactorspecifics)

- Additional reactor-specific configurations and features.


__notes__ `string`

- Additional notes about the vessel specifications.


------

### Closure
Sealing and closure system for reaction vessels.

__closure_type__ `string`

- Type of closure mechanism (e.g., screw cap, septum, crimp cap).


__sealing_material__ `string`

- Material used for sealing (e.g., PTFE, silicone, rubber).


__notes__ `string`

- Additional notes about the closure system.


------

### ReactorSpecifics
Specialized reactor configurations and operational features.

__gas_handling__ [`GasHandling`](#gashandling)

- Gas supply and handling system for the reactor.


__tubing__ `string`

- Tubing specifications and connections used in the reactor setup.


__catalyst_localisation__ `string`

- Method or system for localizing or immobilizing the catalyst within the reactor.


__temperature_control__ `string`

- Temperature control and regulation system employed.


------

### GasHandling
Gas supply and handling system for reactor operations.

__gas_type__ `string`

- Type of gas used (e.g., nitrogen, oxygen, argon, air).


__supply_method__ `string`

- Method of gas supply (e.g., continuous flow, headspace purging, bubbling).


__supply_rate__ `float`

- Rate of gas supply or flow into the reactor.


------

### Mixing
Mixing system and parameters for ensuring proper mass transfer and reaction homogeneity.

__mixing_type__* [`MixingType`](#mixingtype)

- Primary type of mixing employed in the reaction system.


__shaking__ [`ShakingMixing`](#shakingmixing)

- Shaking-based mixing parameters and configuration.


__mechanical__ [`MechanicalMixing`](#mechanicalmixing)

- Mechanical stirring parameters and equipment specifications.


__fluid__ [`FluidImpelledMixing`](#fluidimpelledmixing)

- Fluid-driven mixing parameters for flow-based systems.


__notes__ `string`

- Additional notes about the mixing strategy and implementation.


------

### ShakingMixing
Parameters for shaking-based mixing systems.

__shaking_type__ `string`

- Type of shaking motion (e.g., orbital, linear, reciprocal).


__deflection__ `float`

- Amplitude or deflection distance of the shaking motion.


__speed__ `float`

- Frequency or speed of the shaking motion.


__vessel_position__ `string`

- Orientation or position of the vessel during shaking.


__notes__ `string`

- Additional notes about the shaking mixing setup.


------

### MechanicalMixing
Parameters for mechanical stirring and agitation systems.

__stirring_type__ `string`

- Type of mechanical stirring (e.g., overhead, magnetic, impeller).


__stirrer_material__ `string`

- Material composition of the stirrer or impeller.


__supplier__ `string`

- Manufacturer or supplier of the stirring equipment.


__number_of_stirrers__ `integer`

- Number of stirrers or impellers used in the system.


__stirrer_geometry__ `string`

- Geometric design and shape of the stirrer or impeller.


__blade_pitch_angle__ `float`

- Angle of the stirrer blades relative to the horizontal plane.


__blade_size__ `float`

- Dimensions or size of the stirrer blades.


__stirrer_speed__ `float`

- Rotational speed of the stirrer or impeller.


__height_above_base__ `float`

- Distance of the stirrer from the bottom of the vessel.


__power_per_volume__ `float`

- Power input per unit volume of the reaction mixture.


__stir_bar__ [`StirBar`](#stirbar)

- Magnetic stir bar specifications for magnetic stirring systems.


__notes__ `string`

- Additional notes about the mechanical mixing setup.


------

### StirBar
Magnetic stir bar specifications for magnetic stirring systems.

__size__ `float`

- Length and diameter of the magnetic stir bar.


__shape__ `string`

- Shape of the stir bar (e.g., cylindrical, octagonal, cross-shaped).


------

### FluidImpelledMixing
Parameters for fluid-driven mixing in flow-based reactor systems.

__phase_volume_description__ `string`

- Description of phase volumes and their distribution in the flow system.


__residence_time__ `float`

- Average residence time of the fluid in the mixing zone.


__reynolds_number__ `string`

- Reynolds number characterizing the flow regime and mixing intensity.


__passive_mixing__ `string`

- Description of passive mixing elements or structures used.


__active_mixer__ `string`

- Description of active mixing devices or mechanisms employed.


__pulsing__ `string`

- Pulsing or oscillatory flow patterns used to enhance mixing.


__notes__ `string`

- Additional notes about the fluid-impelled mixing system.


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

### VesselType

| Alias | Value |
|-------|-------|
| `OTHER` | other |
| `PLATE` | plate |
| `STIRRED_TANK` | stirred_tank |
| `TUBULAR_FLOW` | tubular_flow |
| `VIAL` | vial |

### MixingType

| Alias | Value |
|-------|-------|
| `COMBINED` | combined |
| `FLUID_IMPELLED` | fluid_impelled |
| `MECHANICAL` | mechanical |
| `NONE` | none |
| `SHAKING` | shaking |

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