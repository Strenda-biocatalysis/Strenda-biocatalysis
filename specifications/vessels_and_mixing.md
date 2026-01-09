---
repo: "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis"
prefix: "stbc"
imports:
    utils: ./utils.md
---

# Vessels and Mixing Specification

This specification defines the structure and properties of vessels and mixing systems used in enzymatic reactions, providing comprehensive documentation for reactor configuration, mixing strategies, and operational parameters.

## Types

### Vessel And Mixing

Specification of the vessel and mixing configuration for conducting biocatalytic reactions.

- **vessel**
  - Type: Vessel
  - Description: Physical container or reactor used for the enzymatic reaction.
- mixing
  - Type: Mixing
  - Description: Mixing system and parameters employed during the reaction.
- notes
  - Type: string
  - Description: Additional notes or comments about the vessel and mixing setup.

### Vessel

Physical container or reactor specification for enzymatic reactions.

- **vessel type**
  - Type: Vessel Type
  - Description: Type of vessel or reactor configuration used for the reaction.
- material
  - Type: string
  - Description: Material composition of the vessel (e.g., glass, plastic, stainless steel).
- size
  - Type: Quantity
  - Description: Volume or capacity of the vessel.
- geometry
  - Type: string
  - Description: Geometric shape and dimensions of the vessel.
- closure
  - Type: Closure
  - Description: Sealing and closure system for the vessel.
- supplier
  - Type: string
  - Description: Manufacturer or supplier of the vessel.
- lot number
  - Type: string
  - Description: Batch or lot number for traceability.
- reactor specifics
  - Type: Reactor Specifics
  - Description: Additional reactor-specific configurations and features.
- notes
  - Type: string
  - Description: Additional notes about the vessel specifications.

### Closure

Sealing and closure system for reaction vessels.

- closure type
  - Type: string
  - Description: Type of closure mechanism (e.g., screw cap, septum, crimp cap).
- sealing material
  - Type: string
  - Description: Material used for sealing (e.g., PTFE, silicone, rubber).
- notes
  - Type: string
  - Description: Additional notes about the closure system.

### Reactor Specifics

Specialized reactor configurations and operational features.

- gas handling
  - Type: Gas Handling
  - Description: Gas supply and handling system for the reactor.
- tubing
  - Type: string
  - Description: Tubing specifications and connections used in the reactor setup.
- catalyst localisation
  - Type: string
  - Description: Method or system for localizing or immobilizing the catalyst within the reactor.
- temperature control
  - Type: string
  - Description: Temperature control and regulation system employed.

### Gas Handling

Gas supply and handling system for reactor operations.

- gas type
  - Type: string
  - Description: Type of gas used (e.g., nitrogen, oxygen, argon, air).
- supply method
  - Type: string
  - Description: Method of gas supply (e.g., continuous flow, headspace purging, bubbling).
- supply rate
  - Type: Quantity
  - Description: Rate of gas supply or flow into the reactor.

### Mixing

Mixing system and parameters for ensuring proper mass transfer and reaction homogeneity.

- **mixing type**
  - Type: Mixing Type
  - Description: Primary type of mixing employed in the reaction system.
- shaking
  - Type: Shaking Mixing
  - Description: Shaking-based mixing parameters and configuration.
- mechanical
  - Type: Mechanical Mixing
  - Description: Mechanical stirring parameters and equipment specifications.
- fluid
  - Type: Fluid Impelled Mixing
  - Description: Fluid-driven mixing parameters for flow-based systems.
- notes
  - Type: string
  - Description: Additional notes about the mixing strategy and implementation.

### Shaking Mixing

Parameters for shaking-based mixing systems.

- shaking type
  - Type: string
  - Description: Type of shaking motion (e.g., orbital, linear, reciprocal).
- deflection
  - Type: Quantity
  - Description: Amplitude or deflection distance of the shaking motion.
- speed
  - Type: Quantity
  - Description: Frequency or speed of the shaking motion.
- vessel position
  - Type: string
  - Description: Orientation or position of the vessel during shaking.
- notes
  - Type: string
  - Description: Additional notes about the shaking mixing setup.

### Mechanical Mixing

Parameters for mechanical stirring and agitation systems.

- stirring type
  - Type: string
  - Description: Type of mechanical stirring (e.g., overhead, magnetic, impeller).
- stirrer material
  - Type: string
  - Description: Material composition of the stirrer or impeller.
- supplier
  - Type: string
  - Description: Manufacturer or supplier of the stirring equipment.
- number of stirrers
  - Type: integer
  - Description: Number of stirrers or impellers used in the system.
- stirrer geometry
  - Type: string
  - Description: Geometric design and shape of the stirrer or impeller.
- blade pitch angle
  - Type: float
  - Description: Angle of the stirrer blades relative to the horizontal plane.
- blade size
  - Type: Quantity
  - Description: Dimensions or size of the stirrer blades.
- stirrer speed
  - Type: Quantity
  - Description: Rotational speed of the stirrer or impeller.
- height above base
  - Type: Quantity
  - Description: Distance of the stirrer from the bottom of the vessel.
- power per volume
  - Type: Quantity
  - Description: Power input per unit volume of the reaction mixture.
- stir bar
  - Type: StirBar
  - Description: Magnetic stir bar specifications for magnetic stirring systems.
- notes
  - Type: string
  - Description: Additional notes about the mechanical mixing setup.

### StirBar

Magnetic stir bar specifications for magnetic stirring systems.

- size
  - Type: Quantity
  - Description: Length and diameter of the magnetic stir bar.
- shape
  - Type: string
  - Description: Shape of the stir bar (e.g., cylindrical, octagonal, cross-shaped).

### Fluid Impelled Mixing

Parameters for fluid-driven mixing in flow-based reactor systems.

- phase volume description
  - Type: string
  - Description: Description of phase volumes and their distribution in the flow system.
- residence time
  - Type: Quantity
  - Description: Average residence time of the fluid in the mixing zone.
- reynolds number
  - Type: string
  - Description: Reynolds number characterizing the flow regime and mixing intensity.
- passive mixing
  - Type: string
  - Description: Description of passive mixing elements or structures used.
- active mixer
  - Type: string
  - Description: Description of active mixing devices or mechanisms employed.
- pulsing
  - Type: string
  - Description: Pulsing or oscillatory flow patterns used to enhance mixing.
- notes
  - Type: string
  - Description: Additional notes about the fluid-impelled mixing system.

## Enumerations

### Vessel Type

```python
VIAL = "vial"
PLATE = "plate"
STIRRED_TANK = "stirred_tank"
TUBULAR_FLOW = "tubular_flow"
OTHER = "other"
```

### Mixing Type

```python
NONE = "none"
SHAKING = "shaking"
MECHANICAL = "mechanical"
FLUID_IMPELLED = "fluid_impelled"
COMBINED = "combined"
```
