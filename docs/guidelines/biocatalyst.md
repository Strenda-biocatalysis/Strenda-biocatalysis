---
hide:
    - navigation
---

# Biocatalyst Specification

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        biocatalyst(Biocatalyst)
        biocatalystidentity(BiocatalystIdentity)
        sequenceinfo(SequenceInfo)
        biocatalystsource(BiocatalystSource)
        purchaseddetails(PurchasedDetails)
        selfproduceddetails(SelfProducedDetails)
        biocatalystapplication(BiocatalystApplication)
        concentration(Concentration)
        activity(Activity)
        applicationworkflowdetails(ApplicationWorkflowDetails)
        immobilization(Immobilization)
        quantity(Quantity)
        storageconditions(StorageConditions)
        biocatalystsourcetype(BiocatalystSourceType)
        biocatalystapplicationtype(BiocatalystApplicationType)
        molecularweightunit(MolecularWeightUnit)
        formulationtype(FormulationType)
        phasetype(PhaseType)
        reactortype(ReactorType)
        biocatalyst(Biocatalyst) --> biocatalystidentity(BiocatalystIdentity)
        biocatalyst(Biocatalyst) --> biocatalystsourcetype(BiocatalystSourceType)
        biocatalyst(Biocatalyst) --> biocatalystsource(BiocatalystSource)
        biocatalyst(Biocatalyst) --> biocatalystapplication(BiocatalystApplication)
        biocatalyst(Biocatalyst) --> immobilization(Immobilization)
        biocatalyst(Biocatalyst) --> storageconditions(StorageConditions)
        biocatalystidentity(BiocatalystIdentity) --> molecularweightunit(MolecularWeightUnit)
        biocatalystidentity(BiocatalystIdentity) --> sequenceinfo(SequenceInfo)
        biocatalystsource(BiocatalystSource) --> biocatalystsourcetype(BiocatalystSourceType)
        biocatalystsource(BiocatalystSource) --> purchaseddetails(PurchasedDetails)
        biocatalystsource(BiocatalystSource) --> selfproduceddetails(SelfProducedDetails)
        purchaseddetails(PurchasedDetails) --> formulationtype(FormulationType)
        selfproduceddetails(SelfProducedDetails) --> formulationtype(FormulationType)
        biocatalystapplication(BiocatalystApplication) --> biocatalystapplicationtype(BiocatalystApplicationType)
        biocatalystapplication(BiocatalystApplication) --> concentration(Concentration)
        biocatalystapplication(BiocatalystApplication) --> activity(Activity)
        biocatalystapplication(BiocatalystApplication) --> applicationworkflowdetails(ApplicationWorkflowDetails)
        immobilization(Immobilization) --> concentration(Concentration)

        click biocatalyst "#biocatalyst" "Go to Biocatalyst"
        click biocatalystidentity "#biocatalystidentity" "Go to BiocatalystIdentity"
        click sequenceinfo "#sequenceinfo" "Go to SequenceInfo"
        click biocatalystsource "#biocatalystsource" "Go to BiocatalystSource"
        click purchaseddetails "#purchaseddetails" "Go to PurchasedDetails"
        click selfproduceddetails "#selfproduceddetails" "Go to SelfProducedDetails"
        click biocatalystapplication "#biocatalystapplication" "Go to BiocatalystApplication"
        click concentration "#concentration" "Go to Concentration"
        click activity "#activity" "Go to Activity"
        click applicationworkflowdetails "#applicationworkflowdetails" "Go to ApplicationWorkflowDetails"
        click immobilization "#immobilization" "Go to Immobilization"
        click quantity "#quantity" "Go to Quantity"
        click storageconditions "#storageconditions" "Go to StorageConditions"
        click biocatalystsourcetype "#biocatalystsourcetype" "Go to BiocatalystSourceType"
        click biocatalystapplicationtype "#biocatalystapplicationtype" "Go to BiocatalystApplicationType"
        click molecularweightunit "#molecularweightunit" "Go to MolecularWeightUnit"
        click formulationtype "#formulationtype" "Go to FormulationType"
        click phasetype "#phasetype" "Go to PhaseType"
        click reactortype "#reactortype" "Go to ReactorType"
    ```


## Types


### Biocatalyst
A biocatalyst is an enzyme or enzyme-containing system used to catalyze biochemical reactions. This section defines the complete characterization of a biocatalyst including its identity, source, application conditions, immobilization status, and storage requirements.

__identity__* [`BiocatalystIdentity`](#biocatalystidentity)

- Essential identifying information about the biocatalyst including name, EC number, molecular properties, and sequence data.


__source_type__ [`BiocatalystSourceType`](#biocatalystsourcetype)


__source__ [`BiocatalystSource`](#biocatalystsource)

- Information about how the biocatalyst was obtained, whether purchased commercially or produced in-house.


__application__ [`BiocatalystApplication`](#biocatalystapplication)

- Details about how the biocatalyst is applied in the reaction, including concentration, activity, and workflow specifics.


__immobilization__ [`Immobilization`](#immobilization)

- Information about whether and how the biocatalyst is immobilized on a support material.


__storage__ [`StorageConditions`](#storageconditions)

- Conditions under which the biocatalyst is stored to maintain its activity and stability.


__notes__ `string`

- Additional notes or comments about the biocatalyst that don't fit in other categories.


------

### BiocatalystIdentity
Core identifying information and molecular characteristics of the biocatalyst enzyme.

__name__* `string`

- The name of the biocatalyst, which can be the trivial name, systematic name, or trade name.


__ec_number__ `list[string]`

- The Enzyme Commission (EC) number that classifies the enzyme according to the reaction it catalyzes.


__molecular_weight__ `float`

- The molecular weight of the enzyme in the specified units.
- `Minimum`: 0

__molecular_weight_unit__ [`MolecularWeightUnit`](#molecularweightunit)

- The unit of measurement for the molecular weight (e.g., kDa, Da).


__catalyzed_reaction__ `list[string]`

- Description of the specific reaction or type of reaction catalyzed by this enzyme.


__sequences__ [`SequenceInfo`](#sequenceinfo)

- Amino acid and/or DNA sequence information for the enzyme.


__origin_organism__ `string`

- The organism from which the enzyme was originally derived or isolated.


__production_organism__ `string`

- The organism used to produce the enzyme (may differ from origin organism for recombinant enzymes).


__posttranslational_modification__ `list[string]`

- Any post-translational modifications present on the enzyme that may affect its activity or properties.


------

### SequenceInfo
Sequence information for the biocatalyst at both the protein and nucleic acid levels.

__sequence_amino_acid__ `list[string]`

- The amino acid sequence of the enzyme in single-letter code format.


__sequence_dna__ `list[string]`

- The DNA sequence encoding the enzyme.


------

### BiocatalystSource
Information about the source and procurement of the biocatalyst.

__source_type__* [`BiocatalystSourceType`](#biocatalystsourcetype)

- Whether the biocatalyst was purchased from a supplier or produced in-house.


__supplier__ `string`

- Name of the commercial supplier or source of the biocatalyst.


__purchased_details__ [`PurchasedDetails`](#purchaseddetails)

- Specific details relevant to commercially purchased biocatalysts.


__self_produced_details__ [`SelfProducedDetails`](#selfproduceddetails)

- Specific details relevant to biocatalysts produced in-house.


------

### PurchasedDetails
Detailed information for commercially purchased biocatalysts.

__reference__ `string`

- Product code, catalog number, or other reference identifier from the supplier.


__purity__ `float`

- Purity of the purchased biocatalyst as specified by the supplier, typically as a percentage.


__purity_specification__ `string`

- Method or specification used to determine the purity (e.g., SDS-PAGE, activity assay).


__formulation__ [`FormulationType`](#formulationtype)

- Physical form of the purchased biocatalyst (dissolved, powder, etc.).


------

### SelfProducedDetails
Detailed information for biocatalysts produced in-house.

__sequence_plasmid__ `list[string]`

- Sequence of the plasmid used for enzyme expression.


__plasmid_specifications__ `list[string]`

- Details about the plasmid construction, including vector backbone, promoter, and other relevant features.


__purification_method__ `list[string]`

- Method(s) used to purify the enzyme after expression.


__purity__ `float`

- Achieved purity of the self-produced biocatalyst, typically as a percentage.


__purity_specification__ `string`

- Method used to determine the purity of the self-produced enzyme.


__formulation__ [`FormulationType`](#formulationtype)

- Physical form of the self-produced biocatalyst after purification and processing.


------

### BiocatalystApplication
Details about how the biocatalyst is applied and used in the reaction system.

__application_type__* [`BiocatalystApplicationType`](#biocatalystapplicationtype)

- The form in which the biocatalyst is applied (purified enzyme, crude extract, whole cells, etc.).


__concentration__ [`list[Concentration]`](#concentration)

- Concentration of the biocatalyst in the reaction mixture.


__activity__ [`list[Activity]`](#activity)

- Measured enzymatic activity of the biocatalyst under the reaction conditions.


__workflow_details__ [`ApplicationWorkflowDetails`](#applicationworkflowdetails)

- Specific workflow steps and methods used in applying the biocatalyst.


------

### Concentration
Quantitative information about biocatalyst concentration in the reaction.

__value__ `float`

- Numerical value of the concentration.
- `Minimum`: 0

__unit__ `string`

- Unit of measurement for the concentration (e.g., mg/mL, µM, U/mL).


__determination_method__ `string`

- Method used to determine or calculate the concentration.


------

### Activity
Enzymatic activity measurement of the biocatalyst.

__value__ `float`

- Numerical value of the measured activity.


__unit__ `string`

- Unit of measurement for the activity (e.g., U/mg, µmol/min/mg).


__determination_method__ `string`

- Assay method used to measure the enzymatic activity.


------

### ApplicationWorkflowDetails
Specific workflow steps and procedures used when applying the biocatalyst.

__cell_disruption_process__ `string`

- Method used to disrupt cells if working with whole cell preparations.


__harvesting_method__ `string`

- Method used to harvest cells or enzyme from the production system.


__separation_method__ `string`

- Method used to separate the biocatalyst from other components.


__source_of_cellfree_extract__ `string`

- Details about the source and preparation of cell-free extracts if applicable.


------

### Immobilization
Information about biocatalyst immobilization on solid supports.

__immobilized__* `boolean`

- Whether the biocatalyst is immobilized (true) or used in free form (false).


__biocatalyst_state__ `string`

- Physical state of the biocatalyst during immobilization (e.g., purified enzyme, crude extract).


__immobilisation_chemistry__ `list[string]`

- Chemical method or mechanism used for immobilization (e.g., covalent binding, adsorption, entrapment).


__carrier_material__ `list[string]`

- Material used as the solid support for immobilization.


__linkers__ `list[string]`

- Chemical linkers or spacers used between the enzyme and carrier material.


__immobilisation_method__ `list[string]`

- Detailed procedure used for the immobilization process.


__purification_method__ `list[string]`

- Method used to purify or wash the immobilized biocatalyst.


__loading__ [`Concentration`](#concentration)

- Amount of enzyme loaded onto the carrier material.


__notes__ `string`

- Additional notes about the immobilization process or properties.


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

### BiocatalystSourceType

| Alias | Value |
|-------|-------|
| `PURCHASED` | purchased |
| `SELF_PRODUCED` | self_produced |

### BiocatalystApplicationType

| Alias | Value |
|-------|-------|
| `CELL_FREE` | cell_free |
| `CRUDE_CELL_EXTRACT` | crude_cell_extract |
| `PURIFIED` | purified |
| `SECRETED` | secreted |
| `WHOLE_CELL` | whole_cell |

### MolecularWeightUnit

| Alias | Value |
|-------|-------|
| `DA` | Da |
| `KDA` | kDa |
| `OTHER` | other |

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