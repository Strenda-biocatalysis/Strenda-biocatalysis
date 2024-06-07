# Results documentation

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        kineticparameters(KineticParameters)
        yieldandconversion(YieldAndConversion)
        activityandinitialreactionrate(ActivityAndInitialReactionRate)
        selectivityandspecificity(SelectivityAndSpecificity)
        thermodynamicparameters(ThermodynamicParameters)
    
        click kineticparameters "#kineticparameters" "Go to KineticParameters"
        click yieldandconversion "#yieldandconversion" "Go to YieldAndConversion"
        click activityandinitialreactionrate "#activityandinitialreactionrate" "Go to ActivityAndInitialReactionRate"
        click selectivityandspecificity "#selectivityandspecificity" "Go to SelectivityAndSpecificity"
        click thermodynamicparameters "#thermodynamicparameters" "Go to ThermodynamicParameters"
    ```



## Types


### KineticParameters
These parameters serve as benchmarks for understanding enzyme kinetics. The Km and kcat value is determined by all substrates involved in the reaction and not just one. Therefore, the concentrations of all substrates must be varied and the Km and kcat values calculated to obtain a common value instead of apparent values. For a comprehensive report around the technical key data of the kinetic parameters, see literature for further information, e.g. Pesci _et al._1, Bisswanger 2 .

__michaelis_constant__* `float`

- The Michaelis-Menten constant (Km​) represents the substrate concentration at which an enzyme achieves half of its maximum reaction rate.

__michaelis_constant_unit__* `string`

- The unit of the Michaelis-Menten constant (Km​) is typically expressed as moles per liter (M or mM).

__maximum_reaction_rate__* `float`

- Vmax, the maximum reaction rate, represents the speed at which an enzyme-catalyzed reaction reaches saturation, indicating the maximum achievable rate of product formation under optimal substrate concentration (where enzymes are predominantly saturated with substrates).

__maximum_reaction_rate_unit__* `string`

- The unit of Vmax (maximum reaction rate) is typically represented as concentration per time, such as moles per liter per second (mol/L/s or mM/s).

__turnover_number__* `float`

- The turnover number (kcat) measures the number of substrate molecules converted to product per active site of an enzyme per unit time when the enzyme is fully saturated with substrate.

__turnover_number_unit__* `string`

- The unit of turnover number (kcat) is typically expressed as moles of product per mole of enzyme per second or per minute (time-1).

__catalytic_efficiency__* `float`

- Catalytic efficiency (kcat/Km) is a measure of how effectively an enzyme converts substrate into product, often quantified as the ratio of the turnover number (kcat) to the Michaelis-Menten constant (Km).

__catalytic_efficiency_unit__* `string`

- The typical unit for catalytic efficiency (kcat/Km) is M-1s-1.

__dissociation_constant__* `float`

- The dissociation constant (Kd) is a measure that represents the equilibrium between a complex and its dissociated components.

__dissociation_constant_unit__* `string`

- The dissociation constant (Kd) is typically expressed in M (mol per liter) or its derivatives, such as nM (nanomoles per liter).

__inhibition_type__* `string`

- Enzyme inhibition encompasses various forms, including competitive, non-competitive, uncompetitive, mixed, and irreversible inhibition. Each type has different effects on the enzyme's function and plays a crucial role in regulating biochemical processes.

__inhibition_constant__* `float`

- The inhibition constant (Ki) describes the affinity of an inhibitor for an enzyme. It indicates how effectively an inhibitor influences enzyme activity. A lower Ki value suggests a strong binding of the inhibitor to the enzyme.

__inhibition_constant_unit__* `string`

- The units for the inhibition constant (Ki) are commonly expressed in M (mol per liter) or related units.

__hill_coefficient__* `float`

- The Hill coefficient is a parameter used to describe cooperativity in the binding of molecules to proteins. It is employed in enzyme reactions, e.g. oxygen binding to hemoglobin, to indicate whether there is positive (cooperative) or negative (anticooperative) binding. A Hill coefficient greater than 1 indicates positive cooperativity, while a value less than 1 indicates negative cooperativity. A value of exactly 1 indicates no cooperativity.

__enzyme_stability__* `string`

- The stability of enzymes is often characterized by various parameters such as the enzyme's half-life under specific conditions, the decline in activity over time, or the preservation of catalytic activity under different environmental conditions.

__special_treatment__* `string`

- If there are any other specific metrics, parameters, characteristics or aspects related to the kinetics that are important to document the results accurately and are not described by the aforementioned metadata, they should be explained here.

------

### YieldAndConversion
These metrics are vital for evaluating the success of a process, optimizing reaction conditions, and ensuring the production of high-quality products in biocatalytic applications. For a comprehensive report around the technical key data of yield and conversion, see literature for further information, e.g. Lies _et al._3.

__c_yield__* `float`

- Yield represents the amount of the desired product obtained from a reaction. It is the number of synthesized molecules of product per number of starting molecules. The following formula can be used:
- `Minimum`: 0.0

__yield_unit__* `string`

- The yield is typically expressed in percentages (%), reflecting the ratio of the actual obtained product quantity to the theoretical maximum product quantity that could be obtained under ideal conditions.

__space_time_yield__* `float`

- Space-time yield in biocatalysis refers to the mass of product obtained per unit volume of the reactor per unit time. Other terms commonly used in the literature are
- `Minimum`: 0.0

__space_time_yield_unit__* `string`

- Space-time yield is commonly expressed in g/L/h (grams per liter per hour) or mol/L/h (moles per liter per hour).

__conversion__* `float`

- The term "conversion" refers to the percentage of substrate that undergoes transformation into the desired product during a reaction. It is the number of converted molecules per number of starting molecules. The following formula can be used:

__conversion_unit__* `string`

- The conversion is commonly expressed as a percentage (%) to indicate the proportion of substrate converted to the desired product during a specific reaction.

__special_treatment__* `string`

- If there are any other specific metrics, parameters, characteristics or aspects related to the conversion or yield that are important to document the results accurately and are not described by the aforementioned attributes, they should be explained here.

------

### ActivityAndInitialReactionRate


__specific_activity__* `float`

- The specific activity refers to the amount of product formed or substrate consumed per unit of enzyme per unit of time.
- `Minimum`: 0.0

__specific_activity_unit__* `string`

- The specific activity is typically expressed in µmol/min/mg (micromoles per minute per milligram of protein).

__initial_reaction_rate__* `float`

- The initial reaction rate refers to the rate at which the product is formed in the first 10% of the enzymatic reaction under specific initial substrate concentrations and reaction conditions.

__initial_reaction_rate_unit__* `string`

- Typically, the initial reaction rate is expressed as mol/L/min (moles per liter per minute) or µmol/mL/min (micromoles per milliliter per minute).

__special_treatment__* `string`

- If there are any other specific metrics, parameters, characteristics or aspects related to the activity or initial reaction rate that are important to document the results accurately and are not described by the aforementioned attributes, they should be explained here.

------

### SelectivityAndSpecificity
These parameters directly assess a catalyst's precision in converting specific substrates to desired products. For a comprehensive report around the technical key data of the selectivity and specificity, see literature for further information, e.g. Faber4, Liese _et al._3, Schurig5.

__stereoselectivity__* `string`

- Stereoselectivity refers to the preference of a chemical reaction to produce a specific stereoisomer or a particular spatial arrangement of atoms within a molecule. It describes the ability of a reaction to favor the formation of one stereoisomer over others or to create a specific stereochemical outcome.

__enantioselectivity__* `float`

- Enantioselectivity, or enantiomeric ratio (E), defines the enzyme's capability to preferentially catalyze the transformation of one enantiomer over its mirror-image counterpart. This trait highlights the enzyme's ability to favor a specific enantiomer either as a product or as the preferred substrate for a reaction.
- `Minimum`: 0.0

__enantiomeric_excess__* `float`

- The enantiomeric excess (
- `Minimum`: 0.0

__enantiomeric_excess_unit__* `string`

- The primary unit used for enantiomeric excess (

__diastereomeric_excess__* `float`

- The diasteriomeric excess (
- `Minimum`: 0.0

__diasteriomeric_excess_unit__* `string`

- The primary unit used for diasteriomeric excess (

__isomeric_content__* `float`

- The isomeric content (
- `Minimum`: 0.0

__isomeric_content_unit__* `string`

- The primary unit used for isomeric content (

__chemoselectivity__* `string`

- Chemoselectivity refers to the ability of a chemical reaction to target a specific functional group or site within a molecule without affecting other reactive groups present. It highlights the preference of a reaction for one type of chemical bond or functional group over others in a molecule.

__regioselectivity__* `string`

- Regioselectivity refers to the preference of a reaction to occur at a specific site within a molecule or compound that has multiple potential reaction sites. It describes the tendency of a reaction to selectively take place at a particular position of the molecule, considering its structural arrangement of atoms or functional groups, rather than at other possible sites.

__special_treatment__* `string`

- If there are any other specific metrics, parameters, characteristics or aspects related to the selectivity and specificity that are important to document the results accurately and are not described by the aforementioned attributes, they should be explained here.

------

### ThermodynamicParameters
Understanding the energy dynamics and spontaneity of reactions through thermodynamic parameters is essential for efficient biocatalysis. For a comprehensive report around the technical key data of the kinetic parameters, see literature for further information, e.g. Heintz6.

__gibbs_free_energy_change__* `string`

- The Gibbs free energy (

__enthalpy_change__* `string`

- The enthalpy (

__special_treatment__* `string`

- If there are any other specific metrics, parameters, characteristics or aspects related to the thermodynamic parameters that are important to document the results accurately and are not described by the aforementioned attributes, they should be explained here.