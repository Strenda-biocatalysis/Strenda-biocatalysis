# Vessels and mixing

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        vial(Vial)
        plate(Plate)
        stirredtankreactor(StirredTankReactor)
        tubularflowcontinuousreactor(TubularFlowContinuousReactor)
        shaking(Shaking)
        mechanicallyimpelledmixing(MechanicallyImpelledMixing)
        liquidorgasimpelledmixing(LiquidOrGasImpelledMixing)

        click vial "#vial" "Go to Vial"
        click plate "#plate" "Go to Plate"
        click stirredtankreactor "#stirredtankreactor" "Go to StirredTankReactor"
        click tubularflowcontinuousreactor "#tubularflowcontinuousreactor" "Go to TubularFlowContinuousReactor"
        click shaking "#shaking" "Go to Shaking"
        click mechanicallyimpelledmixing "#mechanicallyimpelledmixing" "Go to MechanicallyImpelledMixing"
        click liquidorgasimpelledmixing "#liquidorgasimpelledmixing" "Go to LiquidOrGasImpelledMixing"
    ```


## Types


### Vial
Vials are sealable containers available in various sizes and materials, playing a crucial role in sample storage and handling, as well as serving as reaction vessels.Plate

__vial_size__* `float`

- The vial's size, which can be its volume or its dimensions.
- `Minimum`: 0.0

__vial_size_unit__* `string`

- For describing the vial size, you can use mL (milliliters) as the unit when referring to volume or cm (centimeters) when referring to dimensions.


__vial_material__* `string`

- Specify the material of the vial, such as glass or plastic, as it can influence the reaction.


__closure_type__* `string`

- Indicate the type of closure or stopper used for the vial, as it affects sealing and the course of the reaction. If no closure or seal was used for the vial, this should be noted as well.


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the vial or its preparation for the reaction that are important for reproducibility and are not                    described by the aforementioned metadata, they should be explained here.


------

### Plate
It's crucial to provide detailed information about the plate type, material, well configuration, and other relevant specifications to ensure reproducibility and accuracy of the experimental setup.Stirred Tank Reactor

__plate_type__* `string`

- The type of plate, such as microtiter plate, deep-well plate, or others.


__plate_material__* `string`

- The material from which the plate is made, such as plastic (polystyrene), glass, or metal.


__number_of_wells__* `string`

- The total number of wells or cavities in the plate.


__well_shape__* `string`

- `Descrption`: The shape of the wells, such as round, rectangular, square, etc.

__well_volume__* `string`

- The volume of each well is, usually expressed in µL (microliters).


__well_arrangement__* `string`

- The arrangement of the wells in the plate, for example, in rows and columns.


__supplier__* `string`

- Information about the supplier from which the plate was purchased.


__lot_number__* `float`

- The lot number, also known as a batch number or code, is a unique identifier assigned to a specific batch of a product. This makes it possible to check or track information on production.
- `Minimum`: 0.0

__sealing_method__* `string`

- Indicate if the wells were sealed with a sealing film or lid. (


__sealing_material__* `string`

- The material of the sealing film or lid. (


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the plate or its preparation for the reaction that are important for reproducibility and are not                    described by the aforementioned metadata, they should be explained here.


------

### StirredTankReactor
Stirred Tank Reactors (STRs) are frequently employed as versatile and controlled vessels, allowing for precise regulation of key parameters like temperature, pH, and stirring speed. All relevant specifications or attributes need to be described.Tubular flow/continuous reactor

__type__* `string`

- There are several types of Stirred Tank Reactors, differing in design and intended use. A detailed description is required.


__material__* `string`

- Material the reactor is made of, e.g. glass, polypropylene etc.


__volume__* `float`

- Indicate the total volume capacity of the Stirred Tank Reactor.
- `Minimum`: 0.0

__volume_unit__* `string`

- The volume is typically expressed in L (liters).


__geometry__* `string`

- The geometry of the reactor, in particular of interest is the ratio of height to width.


__bottom_type__* `string`

- Shape of the bottom of the reactor, e.g. a round bottom or a flat bottom.


__gas_consumption__* `string`

- Common gases that are supplied to the reactor include, e.g., air, oxygen, hydrogen, etc.


__gas_supply__* `string`

- Gas can be supplied to a Stirred Tank Reactor in various ways, such as through sparging using a tube or an aeration basket, bubbling, or direct injection into the reactor vessel.


__gas_supply_rate__* `float`

- Specification of the gas supply rate.
- `Minimum`: 0.0

__gas_supply_rate_unit__* `string`

- The units for the gas supply rate in a Stirred Tank Reactor can be L/min (liters per minute), m³/h (cubic meters per hour), or other volume units per unit of time.


__temperature_control__* `string`

- The temperature in a Stirred Tank Reactor can be controlled through various methods, typically using external heat sources or cooling systems such as heating jackets, cooling coils, or external             temperature control units.


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the Stirred Tank Reactor or its preparation for the reaction that are important for reproducibility and are        not described by the aforementioned metadata, they should be explained here.


------

### TubularFlowContinuousReactor
When conducting enzymatic reactions in tubular flow or continuous reactors, it is essential to provide detailed information about the reactor setup, e.g. plug flow reactor, and operating conditions to ensure reproducibility and transparency in reporting the experimental process.

__volume__* `float`

- Indicate the total volume capacity of the tubular flow/continuous reactor.
- `Minimum`: 0.0

__volume_unit__* `string`

- The volume is typically expressed in L (liters).


__geometry__* `string`

- The exact geometry of the tubular flow/continuous reactor.


__reactor_type__* `string`

- There are several types of tubular flow/continuous reactors, e.g. packed bed reactor, or a plug flow reactor, differing in design and intended use. A detailed description is required.


__material__* `string`

- Material the reactor is made of, e.g. glass, stainless steel or other materials.


__tubing__* `string`

- When using tubing in a tubular flow/continuous reactor, various pieces of information can be provided, such as tubing material, diameter, length, connections, etc.


__localisation_of_the_catalyst__* `string`

- Specify the exact location of the catalyst in the tubular flow/continuous reactor. The biocatalyst is typically present in the liquid phase or immobilized on a support matrix (such as particles or          membranes).


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the tubular flow/continuous reactor or its preparation for the reaction that are important for reproducibility     and are not described by the aforementioned metadata, they should be explained here.


------

### Shaking
Shaking is an essential method for ensuring uniform mixing and, consequently, recording relevant metadata is crucial for maintaining consistent reaction conditions.Mechanically impelled mixing (stirring)

__shaking_type__* `string`

- The type of shaking used to mix the reaction (e.g., horizontal, vertical, back-and-forth or circulatory).


__deflection__* `float`

- Information about the extent of deflection or bending of the agitator from its original position of the horizontal shaking system.
- `Minimum`: 0.0

__deflection_unit__* `string`

- Units such as mm (millimeters) or μm (micrometers) could be used to describe deflection in relation to the movement of the shaking system.


__speed__* `float`

- Specify the speed or frequency at which the shaking was conducted.
- `Minimum`: 0.0

__speed_unit__* `string`

- The shaking speed or frequency could be expressed in units such as rpm (rounds per minute) or Hz (cycles per second).


__position__* `string`

- Information regarding the orientation of the vessel in the shaking system relative to deflection.


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the shaking that are important for reproducibility and are not described by the aforementioned metadata, they      should be explained here.


------

### MechanicallyImpelledMixing
When utilizing mechanically impelled mixing in enzymatic reactions, it is essential to provide information about the mixing method and related parameters.Liquid or gas impelled mixing

__stirring_type__* `string`

- There are several types of stirring methods used in laboratory and industrial settings, including magnetic stirring (from vessel bottom), mechanical stirring, overhead stirring and other methods.


__stirrer_material__* `string`

- The specific composition or nature of the material should be indicated, e.g. whether it is made of magnetic material, a PTFE (polytetrafluoroethylene) coating, stainless steel or other relevant features that determine its structural or functional properties within the experimental setup.


__supplier__* `string`

- If available, details of the specific designation or manufacturer's name of the stirrer should be provided for precise identification.


__number_of_stirrers__* `float`

- The number of stirrers available in the system.
- `Minimum`: 0.0

__distance_between_stirrers__* `float`

- Information about the distance, spacing or separation between the stirring rods or impellers within a reaction vessel or container.
- `Minimum`: 0.0

__distance_between_stirrers_unit__* `string`

- The distance between stirrers can be specified in mm (millimeters), cm (centimeters), or m (meters), depending on the size and scale of the stirring system.


__stirrer_blade_pitch_angle__* `float`

- The pitch angle at which the blades or paddles of a stirring mechanism are positioned relative to the plane of rotation. It's typically expressed in ° (degrees).
- `Minimum`: 0.0

__number_of_stirrer_blades__* `float`

- The number of blades on each stirrer.
- `Minimum`: 0.0

__stirrer_blade_size__* `float`

- The size of the impeller blades in a stirred tank reactor.
- `Minimum`: 0.0

__stirrer_blade_size_unit__* `string`

- In the case of impellers in a stirred tank reactor, the diameter of the impeller blades is typically specified. This diameter can be measured in millimeters (mm) or centimeters (cm).


__stirrer_geometry__* `string`

- There are various morphologies or geometries, such as radial impellers, axial impellers, helical ribbon impellers, paddle impellers, and more, depending on its design and intended purpose.


__stirrer_speed__* `float`

- Specify the speed or frequency at which the stirring was conducted.
- `Minimum`: 0.0

__speed_unit__* `string`

- The unit for stirring speed can be expressed in RPM (revolutions per minute), Hz (Hertz), or rad/s (radians per second), depending on the measurement instruments and scientific conventions used.


__height_of_stirrer_above_vessel_base__* `float`

- The vertical distance between the bottom of the vessel or container (where the reaction takes place) and the lowest point of the stirring element or stirrer, which is usually located just above the         vessel base.
- `Minimum`: 0.0

__height_of_stirrer_above_vessel_base_unit__* `string`

- Common units for defining the vertical distance between the bottom of the vessel and the lowest point of the stirrer include: mm (millimeters), cm (centimeters) and m (meters).


__power_per_volume__* `float`

- The amount of stirring power or energy input into a system per unit volume.
- `Minimum`: 0.0

__power_per_volume_unit__* `string`

- The units commonly used for expressing the stirring power are W/L (watts per liter) or kW/m³ (kilowatts per cubic meter).


__stir_bar_size__* `float`

- `Minimum`: 0.0- `Decription`: The length, diameter, or volume of the stir bar used in the experiment. Different sizes of stir bars can affect the efficiency of mixing based on the volume of the reaction mixture and the vessel size.

__stir_bar_size_unit__* `float`

- `Minimum`: 0.0- `Decription`: The size of a stir bar can be expressed in various units such as length in cm (centimeters), mm (millimeters), m (meters), in (inches), or ft (feet); diameter in mm (millimeters), cm (centimeters), or μm (micrometers); and cm³ (volume in cubic centimeters) or mL (milliliters). The choice of unit depends on the specific dimensions being measured to describe the stir bar's size accurately within experiments.

__stir_bar_shape__* `string`

- The shape or configuration of the stir bar, whether it's cylindrical, octagonal, oval, or another shape. Different shapes can interact with the reaction mixture differently, influencing mixing patterns and efficiency.


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the mechanically impelled mixing (stirring) that are important for reproducibility and are not described by        the aforementioned metadata, they should be explained here.


------

### LiquidOrGasImpelledMixing
Detailed information about the mixing mode used, whether it involves liquid or gas impelled mixing, is essential for ensuring the reproducibility and understanding of enzymatic reactions.

__volume_of_liquid_solid_phase__* `string`

- In the context of enzymatic reactions or any chemical processes involving heterogeneous mixtures like a liquid and solid phase, essential parameters for describing the system involve the              composition of the phases, the percentage or fraction of the total volume occupied by the liquid-solid phase mixture, and further information.


__residence_time__* `float`

- The residence time, often denoted as "τ" (tau), refers to the average amount of time a substance or component spends inside a specific system or reactor and is to be specified.
- `Minimum`: 0.0

__residence_time_unit__* `string`

- The units for residence time can vary depending on the system and the units used for volume and flow rate. Common units include s (seconds), min (minutes), h (hours), or any time-related units.


__reynolds_number__* `string`

- The Reynolds number (Re) is a dimensionless quantity used in fluid dynamics to predict the flow regime of a fluid within a specific system. It helps to determine whether the flow is laminar, turbulent, or     somewhere in between.


__passive_mixing__* `string`

- The design of the coils and the flow patterns created by the geometry of the tubing can lead to passive mixing as the fluid flows through the reactor without the need for external agitation. More           detailed information must be provided to describe the process.


__active_T_or_Y_mixer__* `string`

- Key features for describing an active Y or T mixer can include inlet ports, mixer chamber, outlet port, control, materials amon others.


__pulsing__* `string`

- The pulsing process involves periodically injecting or introducing specific components, such as reactants or additives, into a reaction system at regular intervals or in a pulsatile manner. More            detailed information must be provided to describe the process.


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the liquid or gas impelled mixing that are important for reproducibility and are not described by the              aforementioned metadata, they should be explained here.