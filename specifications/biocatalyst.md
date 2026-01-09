---
repo: "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis"
prefix: "stbc"
imports:
    utils: ./utils.md
---

# Biocatalyst Specification

This specification defines the structure and properties of biocatalysts used in enzymatic reactions, providing comprehensive documentation for enzyme characterization, sourcing, application, and storage conditions.

## Types

### Biocatalyst

A biocatalyst is an enzyme or enzyme-containing system used to catalyze biochemical reactions. This section defines the complete characterization of a biocatalyst including its identity, source, application conditions, immobilization status, and storage requirements.

- __identity__
  - type: Biocatalyst Identity
  - description: Essential identifying information about the biocatalyst including name, EC number, molecular properties, and sequence data.

- __source__
  - type: Biocatalyst Source
  - description: Information about how the biocatalyst was obtained, whether purchased commercially or produced in-house.

- __application__
  - type: Biocatalyst Application
  - description: Details about how the biocatalyst is applied in the reaction, including concentration, activity, and workflow specifics.

- immobilization
  - type: Immobilization
  - description: Information about whether and how the biocatalyst is immobilized on a support material.

- storage
  - type: Storage Conditions
  - description: Conditions under which the biocatalyst is stored to maintain its activity and stability.

- notes
  - type: string[]
  - description: Additional notes or comments about the biocatalyst that don't fit in other categories.

### Biocatalyst Identity

Core identifying information and molecular characteristics of the biocatalyst enzyme.

- __name__
  - type: string
  - description: The name of the biocatalyst, which can be the trivial name, systematic name, or trade name.
- ec number
  - type: string[]
  - description: The Enzyme Commission (EC) number that classifies the enzyme according to the reaction it catalyzes.
- molecular weight
  - type: float
  - minimum: 0.0
  - description: The molecular weight of the enzyme in the specified units.
- molecular weight unit
  - type: Molecular Weight Unit
  - description: The unit of measurement for the molecular weight (e.g., kDa, Da).
- catalyzed reaction
  - type: string[]
  - description: Description of the specific reaction or type of reaction catalyzed by this enzyme.
- sequences
  - type: Sequence Info
  - description: Amino acid and/or DNA sequence information for the enzyme.
- origin organism
  - type: string
  - description: The organism from which the enzyme was originally derived or isolated.
- production organism
  - type: string
  - description: The organism used to produce the enzyme (may differ from origin organism for recombinant enzymes).
- posttranslational modification
  - type: string[]
  - description: Any post-translational modifications present on the enzyme that may affect its activity or properties.

### Sequence Info

Sequence information for the biocatalyst at both the protein and nucleic acid levels.

- sequence amino acid
  - type: string[]
  - description: The amino acid sequence of the enzyme in single-letter code format.
- sequence dna
  - type: string[]
  - description: The DNA sequence encoding the enzyme.

### Biocatalyst Source

Information about the source and procurement of the biocatalyst.

- __source type__
  - type: Biocatalyst Source Type
  - description: Whether the biocatalyst was purchased from a supplier or produced in-house.

- supplier
  - type: string
  - description: Name of the commercial supplier or source of the biocatalyst.

- purchased details
  - type: Purchased Details
  - description: Specific details relevant to commercially purchased biocatalysts.

- self produced details
  - type: Self Produced Details
  - description: Specific details relevant to biocatalysts produced in-house.

### Purchased Details

Detailed information for commercially purchased biocatalysts.

- reference
  - type: string
  - description: Product code, catalog number, or other reference identifier from the supplier.
- purity
  - type: float
  - description: Purity of the purchased biocatalyst as specified by the supplier, typically as a percentage.
- purity specification
  - type: string
  - description: Method or specification used to determine the purity (e.g., SDS-PAGE, activity assay).
- formulation
  - type: Formulation Type
  - description: Physical form of the purchased biocatalyst (dissolved, powder, etc.).

### Self Produced Details

Detailed information for biocatalysts produced in-house.

- sequence plasmid
  - type: string[]
  - description: Sequence of the plasmid used for enzyme expression.
- plasmid specifications
  - type: string[]
  - description: Details about the plasmid construction, including vector backbone, promoter, and other relevant features.
- purification method
  - type: string[]
  - description: Method(s) used to purify the enzyme after expression.
- purity
  - type: float
  - description: Achieved purity of the self-produced biocatalyst, typically as a percentage.
- purity specification
  - type: string
  - description: Method used to determine the purity of the self-produced enzyme.
- formulation
  - type: Formulation Type
  - description: Physical form of the self-produced biocatalyst after purification and processing.

### Biocatalyst Application

Details about how the biocatalyst is applied and used in the reaction system.

- __application type__
  - type: Biocatalyst Application Type
  - description: The form in which the biocatalyst is applied (purified enzyme, crude extract, whole cells, etc.).

- concentration
  - type: Concentration[]
  - description: Concentration of the biocatalyst in the reaction mixture.

- activity
  - type: Activity[]
  - description: Measured enzymatic activity of the biocatalyst under the reaction conditions.

- workflow details
  - type: Application Workflow Details
  - description: Specific workflow steps and methods used in applying the biocatalyst.

### Concentration

Quantitative information about biocatalyst concentration in the reaction.

- value
  - type: float
  - minimum: 0.0
  - description: Numerical value of the concentration.
- unit
  - type: Unit Definition
  - description: Unit of measurement for the concentration (e.g., mg/mL, µM, U/mL).
- determination method
  - type: string
  - description: Method used to determine or calculate the concentration.

### Activity

Enzymatic activity measurement of the biocatalyst.

- value
  - type: float
  - description: Numerical value of the measured activity.
- unit
  - type: string
  - description: Unit of measurement for the activity (e.g., U/mg, µmol/min/mg).
- determination method
  - type: string
  - description: Assay method used to measure the enzymatic activity.

### Application Workflow Details

Specific workflow steps and procedures used when applying the biocatalyst.

- cell disruption process
  - type: string[]
  - description: Method used to disrupt cells if working with whole cell preparations.
- harvesting method
  - type: string[]
  - description: Method used to harvest cells or enzyme from the production system.
- separation method
  - type: string[]
  - description: Method used to separate the biocatalyst from other components.
- source of cellfree extract
  - type: string[]
  - description: Details about the source and preparation of cell-free extracts if applicable.

### Immobilization

Information about biocatalyst immobilization on solid supports.

- __immobilized__
  - type: boolean
  - description: Whether the biocatalyst is immobilized (true) or used in free form (false).
- biocatalyst state
  - type: string
  - description: Physical state of the biocatalyst during immobilization (e.g., purified enzyme, crude extract).
- immobilisation chemistry
  - type: string[]
  - description: Chemical method or mechanism used for immobilization (e.g., covalent binding, adsorption, entrapment).
- carrier material
  - type: string[]
  - description: Material used as the solid support for immobilization.
- linkers
  - type: string[]
  - description: Chemical linkers or spacers used between the enzyme and carrier material.
- immobilisation method
  - type: string[]
  - description: Detailed procedure used for the immobilization process.
- purification method
  - type: string[]
  - description: Method used to purify or wash the immobilized biocatalyst.
- loading
  - type: Concentration
  - description: Amount of enzyme loaded onto the carrier material.
- notes
  - type: string[]
  - description: Additional notes about the immobilization process or properties.

### Biocatalyst Source Type

Enumeration of possible sources for obtaining the biocatalyst.

```python
PURCHASED = "purchased"
SELF_PRODUCED = "self_produced"
```

### Biocatalyst Application Type

Enumeration of different forms in which the biocatalyst can be applied in reactions.

```python
PURIFIED = "purified"
CRUDE_CELL_EXTRACT = "crude_cell_extract"
WHOLE_CELL = "whole_cell"
SECRETED = "secreted"
CELL_FREE = "cell_free"
```

### Molecular Weight Unit

Enumeration of units for molecular weight.

```python
KDA = "kDa"
DA = "Da"
OTHER = "other"
```
