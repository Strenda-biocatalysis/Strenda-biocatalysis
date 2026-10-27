---
hide:
    - navigation
---

# Results Specification

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        experimentalresults(ExperimentalResults)
        kineticresults(KineticResults)
        inhibitionparameters(InhibitionParameters)
        yieldandconversionresults(YieldAndConversionResults)
        activityresults(ActivityResults)
        selectivityresults(SelectivityResults)
        thermodynamicresults(ThermodynamicResults)
        quantity(Quantity)
        storageconditions(StorageConditions)
        inhibitiontype(InhibitionType)
        formulationtype(FormulationType)
        phasetype(PhaseType)
        reactortype(ReactorType)
        experimentalresults(ExperimentalResults) --> kineticresults(KineticResults)
        experimentalresults(ExperimentalResults) --> yieldandconversionresults(YieldAndConversionResults)
        experimentalresults(ExperimentalResults) --> activityresults(ActivityResults)
        experimentalresults(ExperimentalResults) --> selectivityresults(SelectivityResults)
        experimentalresults(ExperimentalResults) --> thermodynamicresults(ThermodynamicResults)
        kineticresults(KineticResults) --> inhibitionparameters(InhibitionParameters)
        inhibitionparameters(InhibitionParameters) --> inhibitiontype(InhibitionType)

        click experimentalresults "#experimentalresults" "Go to ExperimentalResults"
        click kineticresults "#kineticresults" "Go to KineticResults"
        click inhibitionparameters "#inhibitionparameters" "Go to InhibitionParameters"
        click yieldandconversionresults "#yieldandconversionresults" "Go to YieldAndConversionResults"
        click activityresults "#activityresults" "Go to ActivityResults"
        click selectivityresults "#selectivityresults" "Go to SelectivityResults"
        click thermodynamicresults "#thermodynamicresults" "Go to ThermodynamicResults"
        click quantity "#quantity" "Go to Quantity"
        click storageconditions "#storageconditions" "Go to StorageConditions"
        click inhibitiontype "#inhibitiontype" "Go to InhibitionType"
        click formulationtype "#formulationtype" "Go to FormulationType"
        click phasetype "#phasetype" "Go to PhaseType"
        click reactortype "#reactortype" "Go to ReactorType"
    ```


## Types


### ExperimentalResults
Comprehensive collection of experimental results from enzymatic reactions.

__kinetics__ [`KineticResults`](#kineticresults)

- Kinetic parameters and enzyme behavior characteristics.


__yield_and_conversion__ [`YieldAndConversionResults`](#yieldandconversionresults)

- Product yield and substrate conversion measurements.


__activity__ [`ActivityResults`](#activityresults)

- Enzyme activity and initial reaction rate data.


__selectivity__ [`SelectivityResults`](#selectivityresults)

- Selectivity measurements including stereoselectivity and enantioselectivity.


__thermodynamics__ [`ThermodynamicResults`](#thermodynamicresults)

- Thermodynamic parameters of the reaction.


__notes__ `string`

- Additional notes or comments about the experimental results.


------

### KineticResults
Kinetic parameters characterizing enzyme behavior and reaction mechanisms.

__michaelis_constant__ `float`

- Michaelis constant (Km) representing the substrate concentration at half-maximum reaction rate.


__maximum_reaction_rate__ `float`

- Maximum reaction rate (Vmax) achieved under saturating substrate conditions.


__turnover_number__ `float`

- Turnover number (kcat) representing the maximum number of substrate molecules converted per enzyme molecule per unit time.


__catalytic_efficiency__ `float`

- Catalytic efficiency (kcat/Km) indicating the enzyme's effectiveness at low substrate concentrations.


__dissociation_constant__ `float`

- Dissociation constant (Kd) for enzyme-substrate or enzyme-inhibitor binding.


__inhibition__ [`InhibitionParameters`](#inhibitionparameters)

- Parameters describing enzyme inhibition characteristics.


__hill_coefficient__ `float`

- Hill coefficient indicating cooperativity in substrate binding or enzyme kinetics.


__enzyme_stability__ `string`

- Qualitative or quantitative description of enzyme stability under reaction conditions.


__notes__ `string`

- Additional notes about kinetic measurements or observations.


------

### InhibitionParameters
Parameters describing enzyme inhibition characteristics and mechanisms.

__inhibition_type__ [`InhibitionType`](#inhibitiontype)

- Type of inhibition mechanism observed.


__inhibition_constant__ `float`

- Inhibition constant (Ki) quantifying the strength of inhibitor binding.


------

### YieldAndConversionResults
Product yield and substrate conversion measurements from enzymatic reactions.

__product_yield__ `list[float]`

- Product yield as percentage or fraction of theoretical maximum.


__space_time_yield__ `float`

- Space-time yield representing product formation rate per unit reactor volume.


__conversion__ `float`

- Substrate conversion as percentage or fraction of initial substrate consumed.


__notes__ `string`

- Additional notes about yield and conversion measurements.


------

### ActivityResults
Enzyme activity measurements and initial reaction rate data.

__specific_activity__ `float`

- Specific activity representing enzyme activity per unit mass of enzyme protein.


__initial_reaction_rate__ `float`

- Initial reaction rate measured at the beginning of the reaction.


__notes__ `string`

- Additional notes about activity measurements.


------

### SelectivityResults
Selectivity measurements including stereoselectivity, enantioselectivity, and other selectivity parameters.

__stereoselectivity__ `string`

- Qualitative or quantitative description of stereoselectivity in the reaction.


__enantioselectivity__ `float`

- Enantioselectivity ratio (E-value) indicating preference for one enantiomer over another.


__enantiomeric_excess__ `float`

- Enantiomeric excess (ee) as percentage indicating optical purity of the product.


__diastereomeric_excess__ `float`

- Diastereomeric excess (de) as percentage for reactions producing diastereomers.


__isomeric_content__ `float`

- Content or ratio of specific isomers in the product mixture.


__chemoselectivity__ `string`

- Description of chemoselectivity when multiple reaction pathways are possible.


__regioselectivity__ `string`

- Description of regioselectivity indicating preference for specific reaction sites.


__notes__ `string`

- Additional notes about selectivity measurements.


------

### ThermodynamicResults
Thermodynamic parameters characterizing the energetics of the enzymatic reaction.

__gibbs_free_energy_change__ `string`

- Gibbs free energy change (ΔG) for the reaction.


__enthalpy_change__ `string`

- Enthalpy change (ΔH) for the reaction.


__entropy_change__ `string`

- Entropy change (ΔS) for the reaction.


__notes__ `string`

- Additional notes about thermodynamic measurements.


------

### Quantity
Quantitative measurement with value and unit specification.

__value__ `float`

- Numerical value of the measurement.
- `Minimum`: 0

__unit__ `string`

- Unit of measurement for the value.


------

### StorageConditions
Conditions under which materials (biocatalysts, components, etc.) are stored to maintain stability and integrity.

__temperature__ `float`

- Storage temperature value.


__temperature_unit__ `string`

- Unit for the storage temperature (e.g., °C, K).


__storage_start__ `date`

- Date when storage under these conditions began or material was received.


__additives__ `list[string]`

- Any additives or stabilizers used during storage (e.g., glycerol, stabilizers, preservatives).


__drying_method__ `list[string]`

- Method used to dry the material if stored in dry form (optional, primarily for biocatalysts).


__notes__ `string`

- Additional notes about storage conditions or requirements.


## Enumerations

### InhibitionType

| Alias | Value |
|-------|-------|
| `COMPETITIVE` | competitive |
| `IRREVERSIBLE` | irreversible |
| `MIXED` | mixed |
| `NONCOMPETITIVE` | non_competitive |
| `OTHER` | other |
| `UNCOMPETITIVE` | uncompetitive |

### FormulationType

| Alias | Value |
|-------|-------|
| `DISSOLVED` | dissolved |
| `GAS` | gas |
| `LIQUID` | liquid |
| `OTHER` | other |
| `POWDER` | powder |
| `SOLUTION` | solution |

### PhaseType

| Alias | Value |
|-------|-------|
| `GAS` | gas |
| `LIQUID` | liquid |
| `MIXED` | mixed |
| `OTHER` | other |
| `SOLID` | solid |

### ReactorType

| Alias | Value |
|-------|-------|
| `OTHER` | other |
| `TUBULAR_FLOW` | tubular_flow |
| `WELL_MIXED` | well_mixed |