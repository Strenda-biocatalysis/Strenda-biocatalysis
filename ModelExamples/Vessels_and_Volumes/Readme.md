[Landing Page](/Readme.md)

# Vessels and volumes


## Vessel definition

This description contains all information nessecary to describe the reaction vessel. 


<details> <Summary>Vial or plate</Summary>

### Vial

These attributes describe all reactions happening in vials.


- __type__
  - Type: string
  - Description: Description of the reaction vessel, is it a glass vial, an microcentrifuge tube or a multiwell plate?
- __volume__
  - Type: posfloat
  - Description: Volume of the reaction vessel
- __material__
  - Type: string
  - Description: Material the reaction vessel is made of, e.g. glass, polypropylene etc.

- __closure__
  - Type: string
  - Description: Is the reaction vessel open or closed?

- __shape_and_dimensions__
  - Type: string
  - Description: The shape of the reaction vessel, does it have a round or flat bottom, is it conical or cylindrical?

</details>

<details> <Summary>Stirred tank reactor</Summary>

### StirredTankReactor

These attributes describe all reactions happening in vials.


- __type__
  - Type: string
  - Description: Description of the reactor
- __volume__
  - Type: posfloat
  - Description: Volume of the reaction vessel

- __volume_unit__
  - Type: string
  - Description: Volume unit of the reaction vessel

- __geometry__
  - Type: string
  - Description: What is the geometry of the reactor, in particular of interest is the ratio of height to width


- __bottom_type__
  - Type: string
  - Description: How is the bottom of the reactor shaped, is it a round bottom or a flat bottom?

- __material__
  - Type: string
  - Description: Material the reactor is made of, e.g. glass, polypropylene etc.

- __gas_consumption__
  - Type: What kind of gas is added to the reactor for gassing purposes? Is it air, oxygen, hydrogen?


- __gas_supply_rate__
  - Type: posfloat
  - Description: With which ?speed? is the gas added to the reactor

- __gas_supply_rate_unit__
  - Type: string
  - Description: What is the unit of the added gas (e.g. ml/min)?


- __gas_supply__
  - Type: string
  - Description: What is used to add the gas to the reaction vessel? A tube, an aeration basket?

- __temperature_exchange_unit__
  - Type: string
  - Description: How is the temperature controlled in the reactor, by a double walled reactor or a heating jacket?

</details>

<details> <Summary>Flow reactor</Summary>

### FlowReactor

Description of flow reactors for, for example plug flow reactors


- __volume_reactor__
  - Type: posfloat
  - Description: The volume of the flow reactor

- __volume_unit__
  - Type: string
  - Description: The volume unit of the flow reactor

- __geometry__
  - Type: string
  - Description: The exact geometry of the flow reactor

- __reactor_type__
  - Type: string
  - Description: What kind of reactor is applied in the experiment, is it a packed bed reactor, or a plug flow reactor?

- __material__
  - Type: string
  - Description: Material the reactor is made of, e.g. glass, polypropylene etc.

- __tubing__
  - Type: string
  - Description: Which tubing is connected to the reactor, transporting the reaction solution?

- __localisation_of_the_catalyst__
  - Type: string
  - Description: Where is the catalyst localised in the flow reactor?

</details>


## Mixing

<details> <Summary>Shaking</Summary>

### Shaking

Describes the shaked mixing of a reaction vessel


- __shaking_type__
  - Type: string
  - Description: What kind of shaking was applied to mix the reaction, was it a horizontal or vertically shaken system?

- __deflection__
  - Type: posfloat
  - Description: How big is the deflection of the horizontally shaken system?

- __deflection_unit__
  - Type: string
  - Description: Unit of the deflection

- __speed__
  - Type: posfloat
  - Description: How fast was the system shaken?

- __speed_unit__
  - Type: string
  - Description: Unit of the shaking, for example rounds per minute (rpm)

- __position__
  - Type: string
  - Description: How was the to be shaken vessel positioned relatively to the deflection

</details>

<details> <Summary>Mechanically impelled mixing (stirring)</Summary>

### MechanicallyImplledmixing

Description of a by stirring mechanically mixed system


- __stirring_type__
  - Type: string
  - Description: What kind of impelling was applied? A magnetic stirrer? A Stirrer blade?

- __number_of_stirrers__
  - Type: posfloat
  - Description: How many stirrers are available in the system?

- __distance_between_stirrers__
  - Type: posfloat
  - Description: How much distance is between the stirrers?

- __distance_between_stirrers_unit__
  - Type: string
  - Description: Unit of the distance between the stirrers

- __stirrer_blade_pitch_angle__
  - Type: posfloat
  - Description: The Pitch angle of the stirrers (in °)

- __number_of_stirrer_blades__
  - Type: posfloat
  - Description: How many stirrer blades are on the stirrer?

- __stirrer_geometry__
  - Type: string
  - Description: Description of the stirrer morphology

- __speed__
  - Type: posfloat
  - Description: Stirring speed used in the experiment

- __speed_unit__
  - Type: string
  - Description: Unit of the stirring speed

- __height_of_stirrer_above_vessel_base__
  - Type: posfloat
  - Description: How much space is between the stirrer and the base of the vessel?

- __height_of_stirrer_above_vessel_base_unit__
  - Type: string
  - Description: Speed of the height_of_stirrer_above_vessel_base_unit

- __power_per_volume__
  - Type: posfloat
  - Description: Stirring power added to the system due to the mixing

- __power_per_volume_unit__
  - Type: string
  - Description: Stirring power unit

  </details>

  <details> <Summary>Liquid or gas impelled mixing</Summary>

### LiquidOrGasImpelledMixing

Describes the shaked mixing of a reaction vessel


- __volume_of_liquid_solid_phase???__
  - Type: string
  - Description: What kind of shaking was applied to mix the reaction, was it a horizontal or vertically shaken system?

- __residence_time__
  - Type: posfloat
  - Description: How big is the deflection of the horizontally shaken system?

- __reynolds_number__
  - Type: string
  - Description: Unit of the deflection

- __passive_mixing__
  - Type: String
  - Description: What is the morphology of the coils

- __active_T_or_Y_mixer__
  - Type: String
  - Description: Description of the T or Y mixer

- __pulsing__
  - Type: String
  - Description: Description of the pulsing process



</details>