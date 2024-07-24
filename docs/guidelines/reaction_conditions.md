# Reaction conditions

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        monoliquidsystemdescription_wmrs(MonoliquidSystemDescription_WMRS)
        multiphasicsystemdescription_wmrs(MultiphasicSystemDescription_WMRS)
        liquidphase_wmrs(LiquidPhase_WMRS)
        solidphase_wmrs(SolidPhase_WMRS)
        gasphase_wmrs(GasPhase_WMRS)
        temperatureconstant_wmrs(TemperatureConstant_WMRS)
        eventbasedtemperatureshift_wmrs(EventBasedTemperatureShift_WMRS)
        phconstant_wmrs(pHConstant_WMRS)
        eventbasedphshift_wmrs(EventBasedpHShift_WMRS)
        monoliquidsystemdescription_tfcr(MonoliquidSystemDescription_TFCR)
        multiphasicsystemdescription_tfcr(MultiphasicSystemDescription_TFCR)
        liquidphase_tfcr(LiquidPhase_TFCR)
        solidphase_tfcr(SolidPhase_TFCR)
        gasphase_tfcr(GasPhase_TFCR)
        temperatureconstant_tfcr(TemperatureConstant_TFCR)
        dynamictemperature_tfcr(DynamicTemperature_TFCR)
        phconstant_tfcr(pHConstant_TFCR)
        dynamicph_tfcr(DynamicpH_TFCR)

        click monoliquidsystemdescription_wmrs "#monoliquidsystemdescription_wmrs" "Go to MonoliquidSystemDescription_WMRS"
        click multiphasicsystemdescription_wmrs "#multiphasicsystemdescription_wmrs" "Go to MultiphasicSystemDescription_WMRS"
        click liquidphase_wmrs "#liquidphase_wmrs" "Go to LiquidPhase_WMRS"
        click solidphase_wmrs "#solidphase_wmrs" "Go to SolidPhase_WMRS"
        click gasphase_wmrs "#gasphase_wmrs" "Go to GasPhase_WMRS"
        click temperatureconstant_wmrs "#temperatureconstant_wmrs" "Go to TemperatureConstant_WMRS"
        click eventbasedtemperatureshift_wmrs "#eventbasedtemperatureshift_wmrs" "Go to EventBasedTemperatureShift_WMRS"
        click phconstant_wmrs "#phconstant_wmrs" "Go to pHConstant_WMRS"
        click eventbasedphshift_wmrs "#eventbasedphshift_wmrs" "Go to EventBasedpHShift_WMRS"
        click monoliquidsystemdescription_tfcr "#monoliquidsystemdescription_tfcr" "Go to MonoliquidSystemDescription_TFCR"
        click multiphasicsystemdescription_tfcr "#multiphasicsystemdescription_tfcr" "Go to MultiphasicSystemDescription_TFCR"
        click liquidphase_tfcr "#liquidphase_tfcr" "Go to LiquidPhase_TFCR"
        click solidphase_tfcr "#solidphase_tfcr" "Go to SolidPhase_TFCR"
        click gasphase_tfcr "#gasphase_tfcr" "Go to GasPhase_TFCR"
        click temperatureconstant_tfcr "#temperatureconstant_tfcr" "Go to TemperatureConstant_TFCR"
        click dynamictemperature_tfcr "#dynamictemperature_tfcr" "Go to DynamicTemperature_TFCR"
        click phconstant_tfcr "#phconstant_tfcr" "Go to pHConstant_TFCR"
        click dynamicph_tfcr "#dynamicph_tfcr" "Go to DynamicpH_TFCR"
    ```


## Types


### MonoliquidSystemDescription_WMRS
To describe a monoliquid system, precise information about the solvent (mixture) used and the applied reaction system must be provided.

__solvent_description__* `string`

- The solvent used in the reaction system, e.g. a buffered aqueous solution or an organic solvent.


__ionic_strength__* `float`

- Ionic strength calculated according to the dissolved ions in the solvent. The following formula can be used: $$I = \frac{1}{2} \sum
- `Minimum`: 0.0

__ionic_strength_unit__* `string`

- The unit of ionic strength is usually expressed in mol/L (moles per liter), or in mmol/L (millimoles per liter). (


__further_additives__* `string`

- Further additive like cosolvents used to increase solubility of components, e.g. DMSO.


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the monoliquid system that are important for reproducibility and are not described by the aforementioned           metadata, they should be explained here.


------

### MultiphasicSystemDescription_WMRS
To describe a multiphasic system, precise information about the phases used and the applied system must be provided.

__phases_number__* `float`

- Number of phases present in the system, if there is an aqueous and a gas phase present, the number is 2.
- `Minimum`: 0.0

__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the multiphasic system that are important for reproducibility and are not described by the aforementioned           metadata, they should be explained here.


------

### LiquidPhase_WMRS
If more then one liquid phase exists the metadata has to be recorded according to the number of liquid phases.Solid phase

__liquid_type__* `string`

- Information about the type of liquid used, whether it is an organic solvent,an aqueous buffer or are mixture of both.


__liquid_amount__* `float`

- Amount of the liquid added to the reaction.
- `Minimum`: 0.0

__liquid_unit__* `string`

- In case of aqueous liquids, mL (milliliter) is often used as unit, in case of organic solvents, volume percentage (Vol %) or volume fraction (Vol/Vol) is utilized.


------

### SolidPhase_WMRS
Definition of the solid phase used in the reaction.Gas phase

__solid_type__* `string`

- Information about the type of solid used, whether it is a support material, solid catalyst, or any other solid compound.


__solid_amount__* `float`

- Mass of the solid compound used in the reaction solution.
- `Minimum`: 0.0

__solid_unit__* `string`

- In the case of a solid compound, common units like grams, milligrams, or micrograms can be used.


------

### GasPhase_WMRS
Definition of the gas phase used in the reaction. If a gas mixture is involved, this must be taken into account.

__gas_type__* `string`

- Information about the type of gas used, whether it is nitrogen, carbon dioxide, argon, oxygen or other gases.


__gas_amount__* `float`

- Concentration of the gas in the gas phase.
- `Minimum`: 0.0

__gas_unit__* `string`

- In the case of gases, common units are volume percentage (Vol %), volume fraction (Vol/Vol), mole percentage (Mol %) or molar fraction (Mol/Mol).


------

### TemperatureConstant_WMRS
The temperature, if constant, must be clearly defined.Event-based temperature shift

__temperature__* `float`

- Temperature during the reaction.
- `Minimum`: 0.0

__temperature_unit__* `string`

- The temperature can be specified in units such as K, °C, or °F.


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the temperature that are important for reproducibility and are not described by the aforementioned                 metadata, they should be explained here.


------

### EventBasedTemperatureShift_WMRS
If the temperature is changed during the course of the reaction or there is an event-based change, this must be documented precisely.

__temperature_unit__* `string`

- The temperature can be specified in units such as K, °C, or °F.


__temperature_beginning__* `float`

- The initial temperature, prior to the start of the reaction, should be specified.
- `Minimum`: 0.0

__temperature_after_event__* `float`

- The temperature that is present after a specific event has occurred.
- `Minimum`: 0.0

__event_description__* `string`

- Information regarding the event that caused the temperature change. In the case of a fed-batch reaction protocol, this event can also be the planned adjustment of the temperature to another specific        value based on the current progress of the reaction process.


__temperature_at_XY__* `float`

- The temperature can also be measured at a variably chosen time point
- `Minimum`: 0.0

__time_at_XY__* `float`

- Specification of the exact time point
- `Minimum`: 0.0

__time_unit__* `string`

- Common units for specifying time can be s (seconds), min (minutes) or h (hours).


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the temperature that are important for reproducibility and are not described by the aforementioned                 metadata, they should be explained here.


------

### pHConstant_WMRS
Information about the pH value in the system, if the pH is constant over the course of the reaction.Event-based pH shift

__pH_value__* `float`

- Value of the pH.
- `Minimum`: 0.0

__detected_when__* `string`

- Specification of the timepoint at which the pH was measured. It includes whether the pH value was measured before, during, or after the reaction and whether all components of the reaction solution were     already present or if some were added after the measurement.


__detected_how__* `string`

- The pH value of a reaction can be determined in various ways, such as using a pH meter, pH paper, titration, electrochemical sensors, or other methods.


__temperature__* `float`

- The temperature at the time of pH measurement.
- `Minimum`: 0.0

__temperature_unit__* `string`

- The temperature can be specified in units such as K, °C, or °F.


__calibration_pH_electrode__* `string`

- Usually, a pH electrode is calibrated using standard buffers at 20-25 °C. If the conditions in the reaction mixture differ from this, it should be specified. (


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the pH value that are important for reproducibility and are not described by the aforementioned                    metadata, they should be explained here.


------

### EventBasedpHShift_WMRS
If the pH is changed during the course of the reaction or there is an event-based change, this must be documented precisely. Depending on the buffer chosen, a temperature shift may also result in a pH shift.

__pH_beginning__* `float`

- The initial pH, prior to the start of the reaction, should be specified.
- `Minimum`: 0.0

__pH_after_event__* `float`

- The pH that is present after a specific event has occurred.
- `Minimum`: 0.0

__event_description__* `string`

- Information regarding the event that caused the pH change. In the case of a fed-batch reaction protocol, this event can also be the planned adjustment of the pH value to another specific value based on     the current progress of the reaction process.


__pH_at_XY__* `float`

- The pH can also be measured at a variably chosen time point
- `Minimum`: 0.0

__time_at_XY__* `float`

- Specification of the exact time point
- `Minimum`: 0.0

__time_unit__* `string`

- Common units for specifying time can be s (seconds) or min (minutes).


__detected_when__* `string`

- Specification whether all components of the reaction solution were already present or if some were added after the measurement at the timepoint of the pH measurement.


__detected_how__* `string`

- The pH value of a reaction can be determined in various ways, such as using a pH meter, pH paper, titration, electrochemical sensors, or other methods.


__temperature__* `float`

- The temperature at the time of pH measurement.
- `Minimum`: 0.0

__temperature_unit__* `string`

- The temperature can be specified in units such as K, °C, or °F.


__calibration_pH_electrode__* `string`

- Usually, a pH electrode is calibrated using standard buffers at 20-25 °C. If the conditions in the reaction mixture differ from this, it should be specified. (


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the pH value that are important for reproducibility and are not described by the aforementioned                    metadata, they should be explained here.


------

### MonoliquidSystemDescription_TFCR
To describe a monoliquid system, precise information about the solvent used and the applied system must be provided.

__solvent_description__* `string`

- The solvent used in the reaction system, e.g. a buffered aqueous solution or an organic solvent.


__ionic_strength__* `float`

- Ionic strength calculated according to the dissolved ions in the solvent. The following formula can be used: $$I = \frac{1}{2} \sum
- `Minimum`: 0.0

__ionic_strength_unit__* `string`

- The unit of ionic strength is usually expressed in mol/L (moles per liter), or in mmol/L (millimoles per liter). (


__further_additives__* `string`

- Further additive like cosolvents used to increase solubility of reactants, e.g. DMSO.


__Flow_rate__* `float`

- The flow rate must be specified to determine how fast a liquid or gas is flowing through a reactor or system.


__Flow_rate_unit__* `string`

- Common units for describing flow rate include L/min (liters per minute), mL/h (milliliters per hour), m³/h (cubic meters per hour), or other volume units per unit of time.


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the monoliquid system that are important for reproducibility and are not described by the aforementioned           metadata, they should be explained here.


------

### MultiphasicSystemDescription_TFCR
To describe a multiphasic system, precise information about the phases used and the applied system must be provided.

__phases_number__* `float`

- Number of phases present in the system, if there is an aqueous and a gas phase present, the number is 2.
- `Minimum`: 0.0

__Flow_rate__* `float`

- The flow rate must be specified to determine how fast a liquid or gas is flowing through a reactor or system.


__Flow_rate_unit__* `string`

- Common units for describing flow rate include L/min (liters per minute), mL/h (milliliters per hour), m³/h (cubic meters per hour), or other volume units per unit of time.


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the multiphasic system that are important for reproducibility and are not described by the aforementioned           metadata, they should be explained here.


------

### LiquidPhase_TFCR
If more then one liquid phase exists the metadata has to be recorded according to the number of liquid phases.Solid phase

__liquid_type__* `string`

- Information about the type of liquid used, whether it is an organic solvent, an aqueous buffer or a mixture of both.


__liquid_amount__* `float`

- Amount of the liquid added to the reaction.
- `Minimum`: 0.0

__liquid_unit__* `string`

- In case of aqueous liquids, mL (milliliter) is often used as unit, in case of organic solvents, volume percentage (Vol %) or volume fraction (Vol/Vol) is utilized.


------

### SolidPhase_TFCR
Definition of the solid phase used in the reaction.Gas phase

__solid_type__* `string`

- Information about the type of solid used, whether it is a support material, solid catalyst, or any other solid compound.


__solid_amount__* `float`

- Mass of the solid used in the reaction solution.
- `Minimum`: 0.0

__solid_unit__* `string`

- In the case of solids, common units like grams, milligrams, or micrograms can be used.


------

### GasPhase_TFCR
Definition of the gas phase used in the reaction. If a gas mixture is involved, this must be taken into account.

__gas_type__* `string`

- Information about the type of gas used, whether it's nitrogen dioxide, argon, oxygen or other gases.


__gas_amount__* `float`

- Concentration of the gas in the gas phase.
- `Minimum`: 0.0

__gas_unit__* `string`

- In the case of gases, common units are volume percentage (Vol %), volume fraction (Vol/Vol), mole percentage (Mol %) or molar fraction (Mol/Mol).


------

### TemperatureConstant_TFCR
The temperature, if constant, must be clearly defined.Dynamic temperature

__temperature__* `float`

- Temperature during the reaction.
- `Minimum`: 0.0

__temperature_unit__* `string`

- The temperature can be specified in units such as K, °C, or °F.


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the temperature that are important for reproducibility and are not described by the aforementioned                 metadata, they should be explained here.


------

### DynamicTemperature_TFCR
If there is a temperature gradient or different temperatures are measured in the system, these must be described as well as possible.

__temperature_beginning__* `float`

- The initial temperature, prior to the start of the reaction, should be specified.
- `Minimum`: 0.0

__temperature_after_event__* `float`

- The temperature that is present after a specific event has occurred.
- `Minimum`: 0.0

__event_description__* `string`

- Information regarding the event that caused the temperature change. In the case of a fed-batch reaction protocol, this event can also be the planned adjustment of the temperature to another specific        value based on the current progress of the reaction process.


__temperature_at_XY__* `float`

- The temperature can also be measured at a variably chosen time point
- `Minimum`: 0.0

__time_at_XY__* `float`

- Specification of the exact time point
- `Minimum`: 0.0

__time_unit__* `string`

- Common units for specifying time can be s (seconds), min (minutes) h (hours).


__temperature_unit__* `string`

- The temperature can be specified in units such as K, °C, or °F.


__temperature_gradient_beginning__* `float`

- The initial temperature from which the temperature gradient begins. (
- `Minimum`: 0.0

__temperature_gradient_end__* `float`

- The target temperature reached after the temperature gradient is applied. (
- `Minimum`: 0.0

__gradient_length__* `float`

- The distance or time span over which the temperature gradient is applied. (
- `Minimum`: 0.0

__gradient_length_unit__* `string`

- The gradient length can be specified either as the physical distance (e.g. in meters) or as the time span (e.g. in minutes). (


__measurement_points__* `string`

- Information about the locations or time points where temperature measurements are taken to monitor the gradient. This can be important to ensure that the gradient behaves as intended.                       (


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the temperature profile that are important for reproducibility and are not described by the aforementioned         metadata, they should be explained here.


------

### pHConstant_TFCR
Information about the pH value in the system, if the pH is constant over the course of the reaction.Dynamic pH

__pH_value__* `float`

- The value of the pH.
- `Minimum`: 0.0

__detected_when__* `string`

- Specification of the timepoint at which the pH was measured. It includes whether the pH value was measured before, during, or after the reaction and whether all components of the reaction solution were     already present or if some were added after the measurement.


__detected_how__* `string`

- The pH value of a reaction can be determined in various ways, such as using a pH meter, pH paper, titration, electrochemical sensors, or other methods.


__temperature__* `float`

- The temperature at the time of pH measurement.
- `Minimum`: 0.0

__temperature_unit__* `string`

- The temperature can be specified in units such as K, °C, or °F.


__calibration_pH_electrode__* `string`

- Usually, a pH electrode is calibrated using standard buffers at 20-25 °C. If the conditions in the reaction mixture differ from this, it should be specified. (


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the pH value that are important for reproducibility and are not described by the aforementioned                    metadata, they should be explained here.


------

### DynamicpH_TFCR
If there is a pH gradient or different pHs are measured in the system, these must be described as detailed as possible. Depending on the buffer chosen, a temperature shift may also result in a pH shift.

__pH_beginning__* `float`

- The initial pH, prior to the start of the reaction, should be specified.
- `Minimum`: 0.0

__pH_after_event__* `float`

- The pH that is present after a specific event has occurred.
- `Minimum`: 0.0

__event_description__* `string`

- Information regarding the event that caused the pH change. In the case of a fed-batch reaction protocol, this event can also be the planned adjustment of the pH value to another specific value based on     the current progress of the reaction process.


__pH_at_XY__* `float`

- The pH can also be measured at a variably chosen time point
- `Minimum`: 0.0

__time_at_XY__* `float`

- Specification of the exact time point
- `Minimum`: 0.0

__time_unit__* `string`

- Common units for specifying time can be s (seconds) or min (minutes).


__detected_when__* `string`

- Specification whether all components of the reaction solution were already present or if some were added after the measurement at the timepoint of the pH measurement.


__detected_how__* `string`

- The pH value of a reaction can be determined in various ways, such as using a pH meter, pH paper, titration, electrochemical sensors, or other methods.


__temperature__* `float`

- The temperature at the time of pH measurement.
- `Minimum`: 0.0

__temperature_unit__* `string`

- The temperature can be specified in units such as K, °C, or °F.


__calibration_pH_electrode__* `string`

- Usually, a pH electrode is calibrated using standard buffers at 20-25 °C. If the conditions in the reaction mixture differ from this, it should be specified. (


__pH_gradient_beginning__* `float`

- The initial pH from which the pH gradient begins. (
- `Minimum`: 0.0

__pH_gradient_end__* `float`

- The target pH reached after the pH gradient is applied. (
- `Minimum`: 0.0

__gradient_length__* `float`

- The distance or time span over which the pH gradient is applied. (
- `Minimum`: 0.0

__gradient_length_unit__* `string`

- The gradient length can be specified either as the physical distance (e.g. in meters) or as the time span (e.g. in minutes). (


__measurement_points__* `string`

- Information about the locations or time points where pH measurements are taken to monitor the gradient. This can be important to ensure that the gradient behaves as intended. (


__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the pH value that are important for reproducibility and are not described by the aforementioned                    metadata, they should be explained here.