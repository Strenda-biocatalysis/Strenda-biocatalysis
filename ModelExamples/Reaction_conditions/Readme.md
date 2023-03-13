# Reaction conditions

<details><Summary>Introductory remarks</Summary>

The reaction conditions were identified by the STRENDA-biocatalysis team as the most complex metadata category to describe. Biocatalysis is a highly divers field with many different reaction conditions. Experiments are perfomed in aqueous reaction solutions, organic solvents, micro aqueous reaction solutions, gassed reaction solutions and many more. Nevertheless, we managed to categorise the reaction conditions in two major categories: __monoliquid and multiphase systems__.

</details>

# Monoliquid systems

## 1. Solvent description

<details> <Summary>Solvent description</Summary>

### Solvent

basic information about the solvent used

- __name*__
  - Type: string
  - Description: The solvent used in the reaction system, for example a buffered aqueous solution or an organic solvent 

</details>

# Multiphase systems

## System description

<details> <Summary>Multiphase system description</Summary>

### Phases

Information about the phases in the multiphase system

- __number_of_phases__
  - Type: posfloat
  - Description: Number of phases present in the system, if there is an aqueous and a gas phase present, the number is 2 

- __phase_definition__
  - Type: phase_description
  - Description: Definition of the respective phase added to the system 

</details>

## Phase description

<details> <Summary>Liquid phase</Summary>

### Liquid phase

Here, metadata are present, describing the individual phases of the multiphase system

- __type_of_liquid__
  - Type: string
  - Description: Description of the phase used in the reaction system 

- __amount_of_liquid__
  - Type: posfloat
  - Description: Which liquid amount is added to the reaction

- __unit_of_liquid__
  - Type: string
  - Description: unit of the added liquid, in case of aqueous liquids, millilitre are often used as unit, in case of organic solvents, mass is applied to refer to the solvent

- __pH__
  - Type: pH description
  - Description: Definition of the pH in the respective phase (__if applicable__)

</details>


<details> <Summary>Solid phase</Summary>

### Solid phase

Definition of the solid phase used in the reaction

- __type_of_solid__
  - Type: string
  - Description: Description of the phase used in the reaction system 

- __mass__
  - Type: posfloat
  - Description: mass of the solid used in the reaction solution
</details>


<details> <Summary>Gas phase</Summary>

### Solid phase

Definition of the solid phase used in the reaction

- __type_of_gas__
  - Type: string
  - Description: Description of the gas used in the system

- __amount__
  - Type: posfloat
  - Description: mass of the solid used in the reaction solution

- __unit__
  - Type: string
  - Description: unit of the gas, added to the reaction, for example as partial pressure

</details>

<hr />

## 2. Temperature

With the type of liquid described, the next question is how does the temperature behave along the reaction, it can stay constant, shift for example due to the chemical reaction catalysed or change e.g. due to the addition of a substrate. 

<details> <Summary>Temperature constant</Summary>

### Temperature constant

basic information about the solvent used

- __temperature__
  - Type: posfloat
  - Description: The temperature during the reaction

- __temperature_unit__
  - Type: string
  - Description: The unit of the temperature, for example °C or K


</details>

<details> <Summary>Temperature shift</Summary>

### Temperature shift

<a id="temperature-shift"></a>


basic information about the solvent used

- __temperature_unit__
  - Type: string
  - Description: The unit of the temperature, for example °C or K

- __temperature_beginning__
  - Type: posfloat
  - Description: The initial temperature of the reaction in the beginning

- __temperature_beginning__
  - Type: posfloat
  - Description: The initial temperature at the end of the reaction

- __temperature_at_XY__
  - Type: posfloat
  - Description: The temperature at a variable time point _XY_

- __time_at_XY__
  - Type: posfloat
  - Description: The time point of a respective temperature at a time _XY_

</details>

<details> <Summary>Event based temperature shift</Summary>

### Event based temperature shift

Description of the temperature, when an event causes the temperature change

- __temperature_unit__
  - Type: string
  - Description: The unit of the temperature, for example °C or K

- __temperature_beginning__
  - Type: posfloat
  - Description: The initial temperature of the reaction in the beginning

- __temperature_at_Event__
  - Type: posfloat
  - Description: The temperature which is present after a certain event has occured

- __event_description__
  - Type: string
  - Description: The event which caused the temperature changve

- __time_at_XY__
  - Type: posfloat
  - Description: The time point of a respective temperature at a time _XY_

- __time_at_XY__
  - Type: posfloat
  - Description: The time point of a respective temperature at a time _XY_

</details>






