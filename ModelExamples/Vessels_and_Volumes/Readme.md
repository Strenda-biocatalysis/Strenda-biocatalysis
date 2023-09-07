[Landing Page](/Readme.md)

# Vessels and volumes

To ensure the reproducibility and accuracy of research results, detailed information about the vessel or reaction container used in experiments is essential. The description and precise specification of this vessel are of importance, as it significantly influences the course and outcome of our enzymatic reactions.

## Vessel definition

The following section requests detailed descriptions of the reaction vessels used in the experiment.

<details> <Summary>Vial</Summary>

### Vial

Vials are sealable containers available in various sizes and materials, playing a crucial role in sample storage and handling, as well as serving as reaction vessels.


- __vial_size__
  - Type: posfloat
  - Description: The vial's size, which can be its volume or its dimensions.
 
- __vial_size_unit__
  - Type: string
  - Description: For describing the vial size, you can use mL (milliliters) as the unit when referring to volume or cm (centimeters) when referring to dimensions.

- __vial_material__
  - Type: string
  - Description: Specify the material of the vial, such as glass or plastic, as it can influence the reaction.

- __closure_type__
  - Type: string
  - Description: Indicate the type of closure or stopper used for the vial, as it affects sealing and the course of the reaction. If no closure or seal was used for the vial, it should be noted as well.

<hr>

- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the vial or its preparation for the reaction that are important for reproducibility and are not                    described by the aforementioned metadata, they should be explained here.



</details>

<details> <Summary>Plate</Summary>

### Plate

It's crucial to provide detailed information about the plate type, material, well configuration, and other relevant specifications to ensure reproducibility and accuracy of the experimental setup.

- __plate_type__
  - Type: string
  - Description: The type of plate, such as microtiter plate, deep-well plate, or others.
 
- __plate_material__
  - Type: string
  - Description: The material from which the plate is made, such as plastic (polystyrene), glass, or metal.

- __number_of_wells__
  - Type: string
  - Description: The total number of wells or cavities in the plate.

- __well_shape__
  - Type: string
  - Descrption: The shape of the wells, such as round, rectangular, square, etc.
 
- __well_volume__
  - Type: string
  - Description: The volume that each well can hold, usually expressed in µL (microliters).
 
- __well_arrangement__
  - Type: string
  - Description: The arrangement of the wells in the plate, for example, in rows and columns.
 
- __sealing_method__
  - Type: string
  - Description: If the wells were sealed with a sealing film or cover, this should be indicated. (__if_applicable__)

- __sealing_material__
  - Type: string
  - Description: The material of the sealing film or cover. (__if_applicable__)

  <hr>

- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the plate or its preparation for the reaction that are important for reproducibility and are not                    described by the aforementioned metadata, they should be explained here.


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

<details> <Summary>Tubular flow/continuous reactor</Summary>

### TubularFlowContinuousReactor

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
  - Description: Unit of the shaking speed, for example rounds per minute (rpm)

- __position__
  - Type: string
  - Description: How was the to be shaken vessel positioned relatively to the deflection

</details>

<details> <Summary>Mechanically impelled mixing (stirring)</Summary>

### MechanicallyImplledmixing

Description of a by stirring mechanically mixed system


- __stirring_type__
  - Type: string
  - Description: What kind of impelling was applied? A magnetic stirrer? A stirrer blade?

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
  - Description: Speed of the height of stirrer above vessel base unit

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
  - Description: ???

- __residence_time__
  - Type: posfloat
  - Description: What is the residence time of the reaction solution in the reactor?

- __reynolds_number__
  - Type: string
  - Description: What is the reynolds number?

- __passive_mixing__
  - Type: String
  - Description: What is the morphology of the coils??

- __active_T_or_Y_mixer__
  - Type: String
  - Description: Description of the T or Y mixer

- __pulsing__
  - Type: String
  - Description: Description of the pulsing process



</details>
