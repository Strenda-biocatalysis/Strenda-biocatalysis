[Landing Page](/Readme.md)

# Reaction conditions

The reaction conditions constitute a highly complex and extensive category. Reactions can be performed in aqueous reaction solutions, organic solvents, micro aqueous reaction solutions, gassed reaction solutions and many more. The Reaction conditions can be divided into two fundamental main categories: __monoliquid and multiphase systems__.

# Well mixed reaction solutions

## Monoliquid systems

A single-phase system in which only one liquid phase is present. All components are fully miscible, and there is no visible separation or boundary between different liquid phases.

<details> <Summary>Monoliquid system description</Summary>

### MonoliquidSystemDescription

Information on the characterisation of the liquid phase.

- __description__
  - Type: string
  - Description: The solvent used in the reaction system, e.g. a buffered aqueous solution or an organic solvent.

- __ionic_strength__
  - Type: posfloat
  - Description: Ionic strength calculated according to the dissolved ions in the solvent. (__if_applicable__)
 
- __further_additives__
  - Type: string
  - Description: Further additive like cosolvents used to increase solubility of reactants, e.g. DMSO.  

</details>

<hr>

## Multiphase systems

Two or more distinct phases coexist within the same physical space. The phases are often separated by interfaces or boundaries. Multiphase systems can include combinations of gases, liquids, and solids.

<details> <Summary>Multiphase system description</Summary>

### MultiphaseSystemDescription

Information about how many phases are present in the multiphase system.

- __phases_number__
  - Type: posfloat
  - Description: Number of phases present in the system, if there is an aqueous and a gas phase present, the number is 2.

</details>

<hr/>

## Phase description

Metadata for describing the individual phases of the multiphase system. Each phase has to be descripted before mixing.

<details> <Summary>Liquid phase</Summary>

### LiquidPhase

 If more then one liquid phase exist the metadata has to be recorded according to the number of liquid phases. 

- __liquid_type__
  - Type: string
  - Description: Description of the phase used in the reaction system. 

- __liquid_amount__
  - Type: posfloat
  - Description: Which liquid amount is added to the reaction?

- __liquid_unit__
  - Type: string
  - Description: Unit of the added liquid, in case of aqueous liquids, millilitre are often used as unit, in case of organic solvents, mass is applied to refer to the solvent

</details>


<details> <Summary>Solid phase</Summary>

### SolidPhase

Definition of the solid phase used in the reaction.

- __solid_type__
  - Type: string
  - Description: Description of the phase used in the reaction system 

- __solid_amount__
  - Type: posfloat
  - Description: Mass of the solid used in the reaction solution
 
- __solid_unit__
  - Type: string
  - Description: Unit of the added solid. Grams, milligrams or microgram are often used as a unit.


</details>


<details> <Summary>Gas phase</Summary>

### GasPhase

Definition of the gas phase used in the reaction. If a gas mixture is involved, this must be taken into account.

- __gas_type__
  - Type: string
  - Description: Description of the gas used in the system

- __gas_amount__
  - Type: posfloat
  - Description: Concentration of the gas in the gas phase. 

- __gas_unit__
  - Type: string
  - Description: Unit of the gas. Common units are volume percentage (Vol %), volume fraction (Vol/Vol), mole percentage (Mol %) or molar fraction (Mol/Mol).

</details>

<hr />

## Temperature conditions

With the type of liquid described, the next question is how does the temperature behave along the reaction, it can stay constant, shift for example due to the chemical reaction catalysed or change e.g. due to the addition of a substrate. 

<details> <Summary>Temperature constant</Summary>

### TemperatureConstant

The temperature, if constant, must be clearly defined.

- __temperature__
  - Type: posfloat
  - Description: The temperature during the reaction

- __temperature_unit__
  - Type: string
  - Description: The unit of the temperature, for example °C or K


</details>

<details> <Summary>Temperature shift</Summary>

### TemperatureShift

<a id="temperature-shift"></a>


If the temperature changes with the course of the reaction, this must be documented precisely.

- __temperature_unit__
  - Type: string
  - Description: The unit of the temperature, for example °C or K

- __temperature_beginning__
  - Type: posfloat
  - Description: The initial temperature of the reaction in the beginning

- __temperature_end__
  - Type: posfloat
  - Description: The temperature at the end of the reaction

- __temperature_at_XY__
  - Type: posfloat
  - Description: The temperature at a variable time point _XY_

- __time_at_XY__
  - Type: posfloat
  - Description: The time point of a respective temperature at a time _XY_

</details>

<details> <Summary>Event based temperature shift</Summary>

### EventBasedTemperatureShift

Description of the temperature, when an event causes the temperature change.

- __temperature_unit__
  - Type: string
  - Description: The unit of the temperature, for example °C or K

- __temperature_beginning__
  - Type: posfloat
  - Description: The initial temperature of the reaction in the beginning

- __temperature_at_event__
  - Type: posfloat
  - Description: The temperature which is present after a certain event has occured

- __event_description__
  - Type: string
  - Description: The event which caused the temperature change

- __time_at_XY__
  - Type: posfloat
  - Description: The time point of a respective temperature at a time _XY_

- __time_at_XY__
  - Type: posfloat
  - Description: The time point of a respective temperature at a time _XY_

</details>

<hr>

## pH conditions

<details> <Summary>pH constant</Summary>

### pHConstant

<a id="pH-shift"></a>


Information about the pH value in the system, if the pH is constant over the course of the reaction.

- __pH_value__
  - Type: posfloat
  - Description: The value of the pH 

- __detected_in__
  - Type: string
  - Description: Solution in which the pH was measured (e.g. in buffer before addition to reaction)
 
- __detected_when__
  - Type: string
  - Description: Timepoint at which the pH was measured (e.g. at before, during or after the reaction)

</details>


<details> <Summary>pH shift over time</Summary>

### pHTimeDependentShift

<a id="pH-shift-time"></a>


Information about the pH value in the system, if there is a time dependent pH shift.

- __pH_start__
  - Type: posfloat
  - Description: The initial pH value

- __pH_end__
  - Type: string
  - Description: The final pH value

- __pH_at_XY__
  - Type: string
  - Description: The pH value at a certain point in time

</details>


<details> <Summary>pH shift event based</Summary>

### pHEventDependentShift

<a id="pH-shift-event"></a>


Information about the pH value in the system, if there is an event dependent pH shift.

- __pH_beginning__
  - Type: posfloat
  - Description: The initial pH value

- __pH_before_event__
  - Type: posfloat
  - Description: The pH which is present before a certain event has occured

- __pH_after_event__
  - Type: posfloat
  - Description: The pH which is present after a certain event has occured

- __event_description__
  - Type: string
  - Description: Description of the event causing the pH-shift

</details>

<hr>

# Flow/Continuous/Tubular reactor

## Monoliquid systems

A single-phase system in which only one liquid phase is present. All components are fully miscible, and there is no visible separation or boundary between different liquid phases.

<details> <Summary>Monoliquid system description</Summary>

### MonoliqudSystemDescription

Information on the characterization of the liquid phase.

- __description__
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

</details>

<hr>

## Multiphase systems

Two or more distinct phases coexist within the same physical space. The phases are often separated by interfaces or boundaries. Multiphase systems can include combinations of gases, liquids, and solids.

<details> <Summary>Multiphase system description</Summary>

### MultiphaseSystemDescription

Information about the phases in the multiphase system.

- __phases_number__
  - Type: posfloat
  - Description: Number of phases present in the system, if there is an aqueous and a gas phase present, the number is 2.
 
- __Flow_rate__
  - Type: float
  - Description: The flow rate must be specified to determine how fast a liquid or gas is flowing through a reactor or system.
 
- __Flow_rate_unit__
  - Type: string
  - Description: Common units for describing flow rate include L/min (liters per minute), mL/h (milliliters per hour), m³/h (cubic meters per hour), or other volume units per unit of time.   

</details>


<hr>


## Phase description

Metadata for describing the individual phases of the multiphase system.

<details> <Summary>Liquid phase</Summary>

### LiquidPhase

 If more then one liquid phase exist the metadata has to be recorded according to the number of liquid phases. 

- __liquid_type__
  - Type: string
  - Description: Description of the phase used in the reaction system.

- __liquid_amount__
  - Type: posfloat
  - Description: Which liquid amount is added to the reaction?

- __liquid_unit__
  - Type: string
  - Description: Unit of the added liquid, in case of aqueous liquids, millilitre are often used as unit, in case of organic solvents, mass is applied to refer to the solvent.

</details>


<details> <Summary>Solid phase</Summary>

### SolidPhase

Definition of the solid phase used in the reaction.

- __solid_type__
  - Type: string
  - Description: Description of the phase used in the reaction system. 

- __solid_amount__
  - Type: posfloat
  - Description: Mass of the solid used in the reaction solution.
 
- __solid_unit__
  - Type: string
  - Description: Unit of the added solid. Grams, milligrams or microgram are often used as a unit.


</details>


<details> <Summary>Gas phase</Summary>

### GasPhase

Definition of the gas phase used in the reaction. If a gas mixture is involved, this must be taken into account.

- __gas_type__
  - Type: string
  - Description: Description of the gas used in the system.

- __gas_amount__
  - Type: posfloat
  - Description: Concentration of the gas in the gas phase. 

- __gas_unit__
  - Type: string
  - Description: Unit of the gas. Common units are volume percentage (Vol %), volume fraction (Vol/Vol), mole percentage (Mol %) or molar fraction (Mol/Mol).

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
  - Description: The unit of the temperature, for example °C or K.


</details>


<details> <Summary>Dynamic temperature</Summary>

### DynamicTemperature

If there is a temperature gradient or different temperatures are measured in the system or over time, these must be described as well as possible.

- __temperature_at_distance__
  - Type: posfloat
  - Description: The temperature during the reaction.

- __temperature_unit__
  - Type: string
  - Description: The unit of the temperature, for example °C or K

- __distance__
  - Type: posfloat
  - Description: The distance at which the temperature was measured.

- __distance_unit__
  - Type: posfloat
  - Description: The unit of the distance.

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
  - Description: Timepoint at which the pH was measured (e.g. at before, during or after the reaction).

</details>


<details> <Summary>Dynamic pH</Summary>

### DynmaicpH

If there is a pH gradient or different pHs are measured in the system or over time, these must be described as well as possible.

- __pH_at_distance__
  - Type: posfloat
  - Description: The pH during the reaction.

- __distance__
  - Type: posfloat
  - Description: The distance at which the pH was measured.

- __distance_unit__
  - Type: posfloat
  - Description: The unit of the distance.

</details>

<hr>



