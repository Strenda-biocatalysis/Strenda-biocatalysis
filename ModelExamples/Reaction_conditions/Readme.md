[Landing Page](/Readme.md)

# Reaction conditions

The reaction conditions constitute a highly complex and extensive category. Reactions can be performed in aqueous reaction solutions, organic solvents, micro aqueous reaction solutions, gassed reaction solutions and many more. The Reaction conditions can be divided into two fundamental main categories: __monoliquid and multiphase systems__.

<img src="https://github.com/StephanM87/Strenda-biocatalysis/assets/106530250/8116078a-308b-4570-b4a1-f9540cfd736a" width="600">


# Well-mixed reaction solutions

## Monoliquid systems

A single-phase system in which only one liquid phase is present. All components are fully miscible, and there is no visible separation or boundary between different liquid phases.

<details> <Summary>Monoliquid system description</Summary>

### MonoliquidSystemDescription

To describe a monoliquid system, precise information about the solvent used and the applied system must be provided.

- __solvent_description__
  - Type: string
  - Description: The solvent used in the reaction system, e.g. a buffered aqueous solution or an organic solvent.

- __ionic_strength__
  - Type: posfloat
  - Description: Ionic strength calculated according to the dissolved ions in the solvent. (__if_applicable__)
 
- __further_additives__
  - Type: string
  - Description: Further additive like cosolvents used to increase solubility of reactants, e.g. DMSO.

<hr>
 
- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the monoliquid system that are important for reproducibility and are not described by the aforementioned           metadata, they should be explained here.

</details>

<hr>

## Multiphase systems

Two or more distinct phases coexist within the same physical space. The phases are often separated by interfaces or boundaries. Multiphase systems can include combinations of gases, liquids, and solids.

<details> <Summary>Multiphase system description</Summary>

### MultiphaseSystemDescription

To describe a multiphase system, precise information about the phases used and the applied system must be provided.

- __phases_number__
  - Type: posfloat
  - Description: Number of phases present in the system, if there is an aqueous and a gas phase present, the number is 2.

<hr>
 
- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the multiphase system that are important for reproducibility and are not described by the aforementioned           metadata, they should be explained here.

</details>

<hr/>

## Phase description

Metadata for describing the individual phases of the multiphase system in more detail. Each phase has to be descripted before mixing.

<details> <Summary>Liquid phase</Summary>

### LiquidPhase

 If more then one liquid phase exist the metadata has to be recorded according to the number of liquid phases. 

- __liquid_type__
  - Type: string
  - Description: Information about the type of liquid used, whether it's an organic solvent,a buffer solution or something else.

- __liquid_amount__
  - Type: posfloat
  - Description: Amount of the liquid added to the reaction.

- __liquid_unit__
  - Type: string
  - Description: In case of aqueous liquids, millilitre are often used as unit, in case of organic solvents, mass is applied to refer to the solvent.

</details>


<details> <Summary>Solid phase</Summary>

### SolidPhase

Definition of the solid phase used in the reaction.

- __solid_type__
  - Type: string
  - Description: Information about the type of solid used, whether it's support materials, solid catalysts, ion exchange resins, or other solids.

- __solid_amount__
  - Type: posfloat
  - Description: Mass of the solid used in the reaction solution.
 
- __solid_unit__
  - Type: string
  - Description: In the case of solids, common units like grams, milligrams, or micrograms can be used.

</details>


<details> <Summary>Gas phase</Summary>

### GasPhase

Definition of the gas phase used in the reaction. If a gas mixture is involved, this must be taken into account.

- __gas_type__
  - Type: string
  - Description: Information about the type of gas used, whether it's nitrogen dioxide, argon, oxygen or other gases.

- __gas_amount__
  - Type: posfloat
  - Description: Concentration of the gas in the gas phase. 

- __gas_unit__
  - Type: string
  - Description: In the case of gases, common units are volume percentage (Vol %), volume fraction (Vol/Vol), mole percentage (Mol %) or molar fraction (Mol/Mol).

</details>

<hr />

## Temperature conditions

Another crucial aspect is the temperature profile throughout the reaction. The temperature can stay constant, shift for example due to the chemical reaction catalysed or change e.g. due to the addition of a substrate. 

<details> <Summary>Temperature constant</Summary>

### TemperatureConstant

The temperature, if constant, must be clearly defined.

- __temperature__
  - Type: posfloat
  - Description: The temperature during the reaction.

- __temperature_unit__
  - Type: string
  - Description: The temperature can be specified in units such as K, °C, or °F.

<hr>

- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the temperature that are important for reproducibility and are not described by the aforementioned                 metadata, they should be explained here. 


</details>

<details> <Summary>Temperature shift</Summary>

### TemperatureShift

If the temperature changes with the course of the reaction, this must be documented precisely.

- __temperature_unit__
  - Type: string
  - Description: The temperature can be specified in units such as K, °C, or °F.

- __temperature_beginning__
  - Type: posfloat
  - Description: The initial temperature, prior to the start of the reaction, should be specified.

- __temperature_end__
  - Type: posfloat
  - Description: The final temperature after completion of the reaction should be specified.

- __temperature_at_XY__
  - Type: posfloat
  - Description: The temperature can also be measured at a variably chosen time point _XY_ during the reaction.

- __time_at_XY__
  - Type: posfloat
  - Description: Specification of the exact time point _XY_ at which the temperature was measured.
 
- __time_unit__
  - Type: string
  - Description: Common units for specifying time can be s (seconds) or min (minutes).

<hr>

- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the temperature that are important for reproducibility and are not described by the aforementioned                 metadata, they should be explained here. 

</details>

<details> <Summary>Event based temperature shift</Summary>

### EventBasedTemperatureShift

Description of the temperature, when an event causes the temperature change.

- __temperature_unit__
  - Type: string
  - Description: The temperature can be specified in units such as K, °C, or °F.

- __temperature_beginning__
  - Type: posfloat
  - Description: The initial temperature, prior to the start of the reaction, should be specified.

- __temperature_after_event__
  - Type: posfloat
  - Description: The temperature that is present after a specific event has occurred.

- __event_description__
  - Type: string
  - Description: Information regarding the event that caused the temperature change.

<hr>

- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the temperature that are important for reproducibility and are not described by the aforementioned                 metadata, they should be explained here. 


</details>

<hr>

## pH conditions

<details> <Summary>pH constant</Summary>

### pHConstant

Information about the pH value in the system, if the pH is constant over the course of the reaction.

- __pH_value__
  - Type: posfloat
  - Description: The value of the pH. 

- __detected_in__
  - Type: string
  - Description: Solution in which the pH was measured (e.g. in buffer before addition to reaction).
 
- __detected_when__
  - Type: string
  - Description: Timepoint at which the pH was measured (e.g. before, during or after the reaction).
 
- __detected_how__
  - Type: string
  - Description: The pH value of a reaction can be determined in various ways, such as using a pH meter, pH paper, titration, electrochemical sensors, or other methods.

<hr>

- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the pH value that are important for reproducibility and are not described by the aforementioned                    metadata, they should be explained here. 

</details>


<details> <Summary>pH shift over time</Summary>

### pHShiftOverTime

Information about the pH value in the system, if there is a time dependent pH shift.

- __pH_beginning__
  - Type: posfloat
  - Description: The initial pH, prior to the start of the reaction, should be specified.

- __pH_end__
  - Type: posfloat
  - Description: The final pH after completion of the reaction should be specified.

- __pH_at_XY__
  - Type: posfloat
  - Description: The pH can also be measured at a variably chosen time point _XY_ during the reaction.

- __time_at_XY__
  - Type: posfloat
  - Description: Specification of the exact time point _XY_ at which the pH was measured.
 
- __time_unit__
  - Type: string
  - Description: Common units for specifying time can be s (seconds) or min (minutes).

<hr>

- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the pH value that are important for reproducibility and are not described by the aforementioned                    metadata, they should be explained here. 

</details>


<details> <Summary>Event based pH shift</Summary>

### EventBasedpHShift

Information about the pH value in the system, if there is an event dependent pH shift.

- __pH_beginning__
  - Type: posfloat
  - Description: The initial pH, prior to the start of the reaction, should be specified.

- __pH_after_event__
  - Type: posfloat
  - Description: The pH that is present after a specific event has occurred.

- __event_description__
  - Type: string
  - Description: Information regarding the event that caused the pH change.

<hr>

- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the pH value that are important for reproducibility and are not described by the aforementioned                    metadata, they should be explained here. 


</details>

<hr>

# Tubular flow/continuous reactor

## Monoliquid systems

A single-phase system in which only one liquid phase is present. All components are fully miscible, and there is no visible separation or boundary between different liquid phases.

<details> <Summary>Monoliquid system description</Summary>

### MonoliqudSystemDescription

To describe a monoliquid system, precise information about the solvent used and the applied system must be provided.

- __solvent_description__
  - Type: string
  - Description: The solvent used in the reaction system, e.g. a buffered aqueous solution or an organic solvent.

- __ionic_strength__
  - Type: posfloat
  - Description: Ionic strength calculated according to the dissolved ions in the solvent. (__if_applicable__)
 
- __further_additives__
  - Type: string
  - Description: Further additive like cosolvents used to increase solubility of reactants, e.g. DMSO.
 
- __Flow_rate__
  - Type: float
  - Description: The flow rate must be specified to determine how fast a liquid or gas is flowing through a reactor or system.
 
- __Flow_rate_unit__
  - Type: string
  - Description: Common units for describing flow rate include L/min (liters per minute), mL/h (milliliters per hour), m³/h (cubic meters per hour), or other volume units per unit of time.   

<hr>
 
- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the monoliquid system that are important for reproducibility and are not described by the aforementioned           metadata, they should be explained here.


</details>

<hr>

## Multiphase systems

Two or more distinct phases coexist within the same physical space. The phases are often separated by interfaces or boundaries. Multiphase systems can include combinations of gases, liquids, and solids.

<details> <Summary>Multiphase system description</Summary>

### MultiphaseSystemDescription

To describe a multiphase system, precise information about the phases used and the applied system must be provided.

- __phases_number__
  - Type: posfloat
  - Description: Number of phases present in the system, if there is an aqueous and a gas phase present, the number is 2.
 
- __Flow_rate__
  - Type: float
  - Description: The flow rate must be specified to determine how fast a liquid or gas is flowing through a reactor or system.
 
- __Flow_rate_unit__
  - Type: string
  - Description: Common units for describing flow rate include L/min (liters per minute), mL/h (milliliters per hour), m³/h (cubic meters per hour), or other volume units per unit of time.   

<hr>
 
- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the multiphase system that are important for reproducibility and are not described by the aforementioned           metadata, they should be explained here.


</details>


<hr>


## Phase description

Metadata for describing the individual phases of the multiphase system in more detail. Each phase has to be descripted before mixing.


<details> <Summary>Liquid phase</Summary>

### LiquidPhase

 If more then one liquid phase exist the metadata has to be recorded according to the number of liquid phases. 

- __liquid_type__
  - Type: string
  - Description: Information about the type of liquid used, whether it's an organic solvent,a buffer solution or something else.

- __liquid_amount__
  - Type: posfloat
  - Description: Amount of the liquid added to the reaction.

- __liquid_unit__
  - Type: string
  - Description: In case of aqueous liquids, millilitre are often used as unit, in case of organic solvents, mass is applied to refer to the solvent.

</details>


<details> <Summary>Solid phase</Summary>

### SolidPhase

Definition of the solid phase used in the reaction.

- __solid_type__
  - Type: string
  - Description: Information about the type of solid used, whether it's support materials, solid catalysts, ion exchange resins, or other solids.

- __solid_amount__
  - Type: posfloat
  - Description: Mass of the solid used in the reaction solution.
 
- __solid_unit__
  - Type: string
  - Description: In the case of solids, common units like grams, milligrams, or micrograms can be used.


</details>


<details> <Summary>Gas phase</Summary>

### GasPhase

Definition of the gas phase used in the reaction. If a gas mixture is involved, this must be taken into account.

- __gas_type__
  - Type: string
  - Description: Information about the type of gas used, whether it's nitrogen dioxide, argon, oxygen or other gases.

- __gas_amount__
  - Type: posfloat
  - Description: Concentration of the gas in the gas phase. 

- __gas_unit__
  - Type: string
  - Description: In the case of gases, common units are volume percentage (Vol %), volume fraction (Vol/Vol), mole percentage (Mol %) or molar fraction (Mol/Mol).


</details>

<hr />


## Temperature conditions

<details> <Summary>Temperature constant</Summary>

### TemperatureConstant

The temperature, if constant, must be clearly defined.

- __temperature__
  - Type: posfloat
  - Description: The temperature during the reaction.

- __temperature_unit__
  - Type: string
  - Description: The temperature can be specified in units such as K, °C, or °F.

<hr>

- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the temperature that are important for reproducibility and are not described by the aforementioned                 metadata, they should be explained here. 


</details>


<details> <Summary>Dynamic temperature</Summary>

### DynamicTemperature

If there is a temperature gradient or different temperatures are measured in the system or over time, these must be described as well as possible.

- __temperature_beginning__
  - Type: posfloat
  - Description: The initial temperature from which the temperature gradient begins.

- __temperature_end__
  - Type: posfloat
  - Description: The target temperature reached after the temperature gradient is applied.

- __temperature_unit__
  - Type: string
  - Description: The temperature can be specified in units such as K, °C, or °F.

- __gradient_length__
  - Type: posfloat
  - Description: The distance or time span over which the temperature gradient is applied.

- __gradient_length_unit__
  - Type: string
  - Description: The gradient length can be specified either as the physical distance (e.g. in meters) or as the time span (e.g. in minutes).

- __measurement_points__
  - Type: string
  - Description: Information about the locations or time points where temperature measurements are taken to monitor the gradient. This can be important to ensure that the gradient behaves as intended.

<hr>

- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the temperature profile that are important for reproducibility and are not described by the aforementioned         metadata, they should be explained here. 


</details>

<hr>

## pH conditions

<details> <Summary>pH constant</Summary>

### pHConstant

Information about the pH value in the system, if the pH is constant over the course of the reaction.

- __pH_value__
  - Type: posfloat
  - Description: The value of the pH. 

- __detected_in__
  - Type: string
  - Description: Solution in which the pH was measured (e.g. in buffer before addition to reaction).
 
- __detected_when__
  - Type: string
  - Description: Timepoint at which the pH was measured (e.g. before, during or after the reaction).

- __detected_how__
  - Type: string
  - Description: The pH value of a reaction can be determined in various ways, such as using a pH meter, pH paper, titration, electrochemical sensors, or other methods.

<hr>

- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the pH value that are important for reproducibility and are not described by the aforementioned                    metadata, they should be explained here. 

</details>


<details> <Summary>Dynamic pH</Summary>

### DynmaicpH

If there is a pH gradient or different pHs are measured in the system or over time, these must be described as well as possible.

- __pH_beginning__
  - Type: posfloat
  - Description: The initial pH from which the pH gradient begins.

- __pH_end__
  - Type: posfloat
  - Description: The target pH reached after the pH gradient is applied.

- __gradient_length__
  - Type: posfloat
  - Description: The distance or time span over which the pH gradient is applied.

- __gradient_length_unit__
  - Type: string
  - Description: The gradient length can be specified either as the physical distance (e.g. in meters) or as the time span (e.g. in minutes).

- __measurement_points__
  - Type: string
  - Description: Information about the locations or time points where pH measurements are taken to monitor the gradient. This can be important to ensure that the gradient behaves as intended.


<hr>

- __special_treament__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the pH value that are important for reproducibility and are not described by the aforementioned                    metadata, they should be explained here. 

</details>

<hr>



