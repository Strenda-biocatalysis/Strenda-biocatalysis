# Components

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        components(Components)
        storageconditions(StorageConditions)
    
        click components "#components" "Go to Components"
        click storageconditions "#storageconditions" "Go to StorageConditions"
    ```



## Types


### Components
Each component present in the planned reaction must be defined.

__name__* `string`

- The name of the component can be either the trivial or trade name, the systematic designation according to IUPAC nomenclature, or any other means of identifying the substance.

__smiles__* `string`

- SMILES (Simplified Molecular Input Line Entry System) is a chemical notation used to represent and describe molecular structures in a simplified and human-readable format.

__persistent_identifier_PID__* `string`

- One or more identifiers that refer to the compound, such as CAS number, PubChem code, InChI code, etc.

__concentration__* `float`

- Concentration of the component.
- `Minimum`: 0.0

__concentration_unit__* `string`

- The concentration of the component is typically expressed in M (Molar), mmol/L (millimoles per liter), or µmol/L (micromoles per liter).

__supplier__* `string`

- Information about the source of the compound, usually a commercial supplier with perhaps product code, but could be preparation in a research lab. Should the component have been synthesized internally,      please include a literature reference detailing its synthesis.

__purity__* `float`

- Purity of a substance typically expressed in percentage (%). It is commonly defined as the percentage of the pure or desired compound relative to the total mass or volume of the substance.

__formulation__* `string`

- The formulation encompass the nature of the component, whether it is in powder, liquid, gaseous form, or any other form, as well as the specific conditions under which it is presented.

__solubility_limit__* `float`

- This limit represents the maximum concentration of a component, which might include gases, that can dissolve in a solution or gas phase. (
- `Minimum`: 0.0

__solubility_limit_unit__* `string`

- The solubility limit of a component can be expressed in various units, including M (moles per liter), g/L (grams per liter), % (percentage concentration), or particles per volume, depending on the         type of component and the solvent used. (

------

### StorageConditions


__temperature__* `float`

- Temperature at which the component is stored.

__temperature_unit__* `string`

- The temperature can be specified in units such as K, °C, or °F.

__storage_start__* `date`

- The date since the component has been stored.

__additives__* `string`

- Additives for the storage of components can include antioxidants, stabilizers, drying agent, or even inert gases (argon, nitrogen), among others.

__special_treatment__* `string`

- If there are any other specific characteristics or aspects related to a component that are important for reproducibility and are not described by the aforementioned metadata, they should be explained       here.