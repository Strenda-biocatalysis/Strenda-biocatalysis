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



<details> <Summary>Stirred Tank Reactor</Summary>


### StirredTankReactor

Stirred Tank Reactors (STRs) are frequently employed as versatile and controlled vessels, allowing for precise regulation of key parameters like temperature, pH, and agitation speed. All relevant specifications or attributes need to be described.


- __type__
  - Type: string
  - Description: There are several types of Stirred Tank Reactors, differing in design and intended use. A detailed description is required.

- __material__
  - Type: string
  - Description: Material the reactor is made of, e.g. glass, polypropylene etc.

- __volume__
  - Type: posfloat
  - Description: Indicate the total volume capacity of the Stirred Tank Reactor.

- __volume_unit__
  - Type: string
  - Description: The unit of the volume is typically expressed in L (liters).

- __geometry__
  - Type: string
  - Description: The geometry of the reactor, in particular of interest is the ratio of height to width.

- __bottom_type__
  - Type: string
  - Description: Shape of the bottom of the reactor, e.g. a round bottom or a flat bottom.

- __gas_consumption__
  - Type: string
  - Description: Common gases that are supplied to the reactor include, e.g., air, oxygen, hydrogen, etc.

- __gas_supply__
  - Type: string
  - Description: Gas can be supplied to a Stirred Tank Reactor in various ways, such as through sparging using a tube or an aeration basket, bubbling, or direct injection into the reactor vessel.

- __gas_supply_rate__
  - Type: posfloat
  - Description: Specification of the gas supply rate.

- __gas_supply_rate_unit__
  - Type: string
  - Description: The units for the gas supply rate in a Stirred Tank Reactor can be L/min (liters per minute), m³/h (cubic meters per hour), or other volume units per unit of time.

- __temperature_control__
  - Type: string
  - Description: The temperature in a Stirred Tank Reactor can be controlled through various methods, typically using external heat sources or cooling systems such as heating jackets, cooling coils, or external             temperature control units.

<hr>

- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the Stirred Tank Reactor or its preparation for the reaction that are important for reproducibility and are        not described by the aforementioned metadata, they should be explained here.

</details>

<details> <Summary>Tubular flow/continuous reactor</Summary>

### TubularFlowContinuousReactor

When conducting enzymatic reactions in tubular flow or continuous reactors, it is essential to provide detailed information about the reactor setup, e.g. plug flow reactor, and operating conditions to ensure reproducibility and transparency in reporting the experimental process.


- __volume__
  - Type: posfloat
  - Description: Indicate the total volume capacity of the tubular flow/continuous reactor.

- __volume_unit__
  - Type: string
  - Description: The unit of the volume is typically expressed in L (liters).

- __geometry__
  - Type: string
  - Description: The exact geometry of the tubular flow/continuous reactor.

- __reactor_type__
  - Type: string
  - Description: There are several types of tubular flow/continuous reactors, e.g. packed bed reactor, or a plug flow reactor, differing in design and intended use. A detailed description is required.

- __material__
  - Type: string
  - Description: Material the reactor is made of, e.g. glass, stainless steel or other materials.

- __tubing__
  - Type: string
  - Description: When using tubing in a tubular flow/continuous reactor, various pieces of information can be provided, such as tubing material, diameter, length, connections, etc.

- __localisation_of_the_catalyst__
  - Type: string
  - Description: Specify the exact location of the catalyst in the tubular flow/continuous reactor.

<hr>

- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the tubular flow/continuous reactor or its preparation for the reaction that are important for reproducibility     and are not described by the aforementioned metadata, they should be explained here.


</details>


## Mixing

Include all relevant information about mixing, as it plays a crucial role in ensuring homogeneous and consistent reaction conditions throughout the process.

<details> <Summary>Shaking</Summary>

### Shaking

Shaking is an essential method for ensuring uniform mixing and, consequently, recording relevant metadata is crucial for maintaining consistent reaction conditions.


- __shaking_type__
  - Type: string
  - Description: The type of shaking used to mix the reaction could be e.g. horizontal or vertical shaking.

- __deflection__
  - Type: posfloat
  - Description: Information about the extent of deflection of the horizontal shaking system.

- __deflection_unit__
  - Type: string
  - Description: Units such as mm (millimeters) or μm (micrometers) could be used to describe deflection in relation to the movement of the shaking system.

- __speed__
  - Type: posfloat
  - Description: Specify the speed or frequency at which the shaking was conducted.

- __speed_unit__
  - Type: string
  - Description: The shaking speed or frequency could be expressed in units such as rpm (rounds per minute) or Hz (cycles per second).

- __position__
  - Type: string
  - Description: Information regarding the orientation of the vessel in the shaking system relative to deflection.

<hr>

- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the shaking that are important for reproducibility and are not described by the aforementioned metadata, they      should be explained here.

</details>

<details> <Summary>Mechanically impelled mixing (stirring)</Summary>

### MechanicallyImplledmixing

When utilizing mechanically impelled mixing in enzymatic reactions, it is essential to provide information about the mixing method and related parameters.

- __stirring_type__
  - Type: string
  - Description: There are several types of stirring methods used in laboratory and industrial settings, including magnetic stirring, mechanical stirring, overhead stirring and other methods.

- __number_of_stirrers__
  - Type: posfloat
  - Description: The number of stirrers available in the system.

- __distance_between_stirrers__
  - Type: posfloat
  - Description: Information about the distance, spacing or separation between the stirring rods or impellers within a reaction vessel or container.

- __distance_between_stirrers_unit__
  - Type: string
  - Description: The distance between stirrers can be specified in units such as mm (millimeters), cm (centimeters), or m (meters), depending on the size and scale of the stirring system.

- __stirrer_blade_pitch_angle__
  - Type: posfloat
  - Description: The pitch angle at which the blades or paddles of a stirring mechanism are positioned relative to the plane of rotation. It's typically expressed in ° (degrees).

- __number_of_stirrer_blades__
  - Type: posfloat
  - Description: The number of blades on each stirrer.

- __stirrer_geometry__
  - Type: string
  - Description: There are various morphologies or geometries, such as radial impellers, axial impellers, helical ribbon impellers, paddle impellers, and more, depending on its design and intended purpose.

- __speed__
  - Type: posfloat
  - Description: Specify the speed or frequency at which the stirring was conducted.

- __speed_unit__
  - Type: string
  - Description: The unit for stirring speed can be expressed in RPM (revolutions per minute), Hz (Hertz), or rad/s (radians per second), depending on the measurement instruments and scientific conventions used.

- __height_of_stirrer_above_vessel_base__
  - Type: posfloat
  - Description: The vertical distance between the bottom of the vessel or container (where the reaction takes place) and the lowest point of the stirring element or stirrer, which is usually located just above the         vessel base. 

- __height_of_stirrer_above_vessel_base_unit__
  - Type: string
  - Description: Common units for defining the vertical distance between the bottom of the vessel and the lowest point of the stirrer include: mm (millimeters), cm (centimeters) and m (meters).

- __power_per_volume__
  - Type: posfloat
  - Description: The amount of stirring power or energy input into a system per unit volume.

- __power_per_volume_unit__
  - Type: string
  - Description: The units commonly used for expressing the stirring power are W/L (watts per liter) or kW/m³ (kilowatts per cubic meter).

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
