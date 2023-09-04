[Landing Page](/Readme.md)

# Biocatalyst

This category contains all information required to unambiguously identify the catalyst, its formulation and storage. 

## Source of the biocatalyst

It's important to determine whether the enzyme or biocatalyst was purchased from a company or self-produced. Different information is needed in each case to describe accurately the enzyme used.

<details> <Summary>Biocatalyst purchased</Summary>

### BiocatalystPurchased

Important information for characterizing the biocatalyst and determining its origin.

- __name__
  - Type: string
  - Description: The name of the biocatalyst can be either generic based on its function and the type of reaction it catalyzes, for example, 'Lipase' or more specific by describing the genus and species, such as           'Bacillus amyloliquefaciens alpha-amylase'.

- __ecnumber__
  - Type: string
  - Description: Numerical classification system that categorizes enzymes based on their biochemical function and reaction mechanism, such as EC 3.1.4.12.

- __chemical_reaction__
  - Type: string
  - Description: The chemical reaction catalyzed by the biocatalyst.

- __sequence__
  - Type: string
  - Description: The amino acid sequence of the biocatalyst.

- __origin_organism__
  - Type: string
  - Description: The specific species or source from which the enzyme is derived or isolated. It includes information about the genus and species of the organism.

- __supplier__
  - Type: string
  - Description: Information about the supplier from which the enzyme was purchased.

- __production_organism__
  - Type: string
  - Description: Information about the organism in which the biocatalyst was produced is crucial in the context of heterologous gene expression.

- __posttranslational_modification__
  - Type: string
  - Description: Information about any chemical modifications or alterations that occur to the biocatalyst's protein structure after translation. This may include: Phosphorylation, glycosylation, acetylation,               methylation, ubiquitination and other modifications.

- __purity__
  - Type: float
  - Description: Purity of enzymes typically expressed in percentage (%). It is usually stated as the percentage of the pure enzyme or active component relative to the total amount of the substance.

- __purity_specification__
  - Type: string
  - Description: Description of how the purity of the biocatalyst was determined. In case of purchased enzymes, this information is often available in the product specification sheet.

- __formulation__
  - Type: string
  - Description: Depending on the formulation, the biocatalyst may be in a liquid form within a solvent or as a solid powder. It defines the physical state in which the biocatalyst is used.

</details>

<details> <Summary>Biocatalyst self-produced</Summary>

### BiocatalystSelfProduced

Important information to characterize the biocatalyst and to describe it clearly.

- __name*__
  - Type: string
  - Description: Name of the biocatalyst

- __ecnumber__
  - Type: string
  - Description: Code used to determine the family of a protein

- __chemical_reaction__
  - Type: string
  - Description: reaction catalysed by the enzyme

- __sequence__
  - Type: string
  - Description: Amino acid sequence of the enzyme

- __origin_organism__
  - Type: string
  - Description: Organism from which the enzyme was extracted or identfied

- __production_organism__
  - Type: string
  - Description: Organism in which the enzyme was produced

- __postranslational_modification__
  - Type: string
  - Description: Code used to determine the family of a protein

- __purity__
  - Type: float
  - Description: purity of the enzyme

- __purity_specification__
  - Type: string
  - Description: description of how the purity of the biocatalyst was determined

- __formulation__
  - Type: string
  - Description: formulation of the biocatalyst, eg powder, solution etc.

- __purification_method__
  - Type: string
  - Description: method used for purification of the enyme

</details>

<hr>

# Formulation and immobilisation

With a enzyme purchased or self-produced it needs to be specified, how it was used in the reaction. Two categories have been identified for applying a biocatalyst to a reaction: immobilized and non immobilised.

## Non immobilised biocatalysts

<details> <Summary>Soluble biocatalyst</Summary>

### SolubleBiocatalyst [_BiocatalystSelfProduced_]

- __concentration*__
  - Type: posfloat
  - Description: Concentration of the biocatalyst

- __activity__:
  - Type: float
  - Description: Acitivity of the enzyme in U/mg or U/mL

- __concentration_determination_method*__
  - Type: string
  - Description: Method on how the concentration has been determined

- __formulation__
  - Type: string
  - Description: Formulation of the biocatalyst, eg powder, solution etc.

- __purification_procedure__
  - Type: string
  - Description: Method used to purifiy the biocatalyst

</details>

<details> <Summary>Crude cell extract</Summary>
  
### CrudeCellExtract [_BiocatalystSelfProduced_]

- __cell_disruption_process__
  - Type: string
  - Description: Method how the cells were disrupted

- __concentration__
  - Type: float
  - Description: Concentration of the biocatalyst

- __concentration_determination_method__
  - Type: string
  - Description: Method how the concentration was measured

</details>

<details> <Summary>Whole cell biocatalyst</Summary>

### WholeCellBiocatalyst [_BiocatalystSelfProduced_]

- __harvesting_method__
  - Type: string
  - Description: How were the cells harvested

- __formulation__
  - Type: string
  - Description: formulation of the catalyst (wet cells, lyophillised?)

</details>

<details> <Summary>Supernatant</Summary>

### Supernatant [_BiocatalystSelfProduced_]

- __production_organism__
  - Type: string
  - Description: Which organism was producing and secreting the biocatalyst?

- __separation_method__
  - Type: string
  - Description: The method of how the supernatant was separated from the cells

</details>

<details> <Summary>Cell-free-production</Summary>

### CellFreeProduction [_BiocatalystSelfProduced_]

- __source_of_cellfree_extract__
  - Type: string
  - Description: Specification of the organism or cell type from which the cell-free extract is derived. This could be bacterial, plant, animal, or another source.
 
- __extract_preparation__
  - Type: string
  - Description: Evaluation of the steps taken to prepare the cell-free extract, including cell disruption, cell lysis, processing, and separation of cellular components.  

</details>



## Immobilised biocatalysts

<details> <Summary>Immobilised biocatalyst</Summary>

### ImmobilisedBiocatalyst [_BiocatalystSelfProduced_]


- __purification_procedure__
  - Type: string
  - Description: Method for purifying the enzyme

- __concentration__
  - Type: float
  - Description: Concentration of the enzyme on the immobilised phase

- __concentration_determination_method__
  - Type: string
  - Description: Method how the concentration was measured

</details>

<details> <Summary>Immobilisation procedure</Summary>

### ImmobilisationProcedure [_BiocatalystSelfProduced_]

- __immobilisation_method__
  - Type: string
  - Description: Method for immobilising the enzyme. Common methods are e.g. adsorption, embedding in matrices, crosslinking, coimmobilization with carrier materials, etc.
 
- __carrier_material__
  - Type: string
  - Despription: If you a support material was used, the name of the support material must be specified. This could be e.g. a gel, a membrane or a particle. (__if_applicable__)

- __carrier_material_concentration__
  - Type: string
  - Despription: Concentration of the used carrier material. (__if_applicable__)

- __immobilisation_yield__
  - Type: string
  - Despription: Definition of how efficiently the enzyme was immobilized.  

</details>

<hr>

# Storage conditions

Describing the biocatalyst involves specifying its storage conditions before use in the reaction.

<details> <Summary>Storage conditions</Summary>

### StorageConditions [_BiocatalystSelfProduced_]

- __temperature__
  - Type: float
  - Description: Storage temperature (-20°C, -80°C)

- __storage_start__
  - Type: date
  - Description: When did storage start?

- __additives__
  - Type: string
  - Description: Were additives added, for example glycerol?

- __removing/rethawing__
  - Type: sting
  - Description: How was the catalyst removed from storage or rethawed?

- __thawing_process__
  - Type: string
  - Description: How was the catalyst frozen, any special devices or additives?

</details>

<hr>
