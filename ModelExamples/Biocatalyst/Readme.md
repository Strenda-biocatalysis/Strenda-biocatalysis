[Landing Page](/Readme.md)

# Biocatalyst

This category contains all information required to unambiguously identify the catalyst, its formulation and storage. 

<img src="https://github.com/StephanM87/Strenda-biocatalysis/assets/106530250/47b53655-0c1c-4518-abc7-c2b8c550f55c" width="500">

## Source of the biocatalyst

It's important to determine whether the enzyme or biocatalyst was purchased from a company or self-produced. Different information is needed in each case to describe accurately the enzyme used.

<details> <Summary>Biocatalyst purchased</Summary>

### BiocatalystPurchased

Important information for characterizing the biocatalyst and determining its origin.

- __name__
  - Type: string
  - Description: The name of the biocatalyst can be either generic based on its function and the type of reaction it catalyzes, for example, 'Lipase' or more specific by describing the genus and species, such as            'Bacillus amyloliquefaciens alpha-amylase'.

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
  - Description: The specific species or source from which the enzyme is derived or isolated. It includes information about the genus and species of the organism. However, the cell type from which the biocatalyst is        derived could be bacterial, as well as plant, animal, or other sources.

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
  - Description: Depending on the formulation, the biocatalyst may be in a liquid form within a solvent or as a solid powder. It defines the physical state in which the biocatalyst is used. Additional information           regarding the application or formulation in the experiment should be entered in the next subcategory.

</details>

<details> <Summary>Biocatalyst self-produced</Summary>

### BiocatalystSelfProduced

Important information to characterize the biocatalyst and to describe it clearly.

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
  - Description: The choice of method for the purity determination depends on the type of enzyme and the available resources and may include gel electrophoresis, HPLC, ELISA, Western blotting, etc.

- __purification_method__
  - Type: string
  - Description: The choice of purification methods is diverse and can impact the enzyme, with possible methods including chromatographic techniques, precipitation, HPLC, ultrafiltration, dialysis, salt fractionation,      etc.

- __formulation__
  - Type: string
  - Description: Depending on the formulation, the biocatalyst may be in a liquid form within a solvent or as a solid powder. It defines the physical state in which the biocatalyst is used. Additional information           regarding the application or formulation in the experiment should be entered in the next subcategory.

<hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata,       they should be explained here.

</details>

<hr>

# Immobilisation and formulation

With a enzyme purchased or self-produced it needs to be specified, how it was used in the reaction. Two categories have been identified for applying a biocatalyst to a reaction: non immobilized and immobilised.

## Non immobilised biocatalysts

<details> <Summary>Soluble biocatalyst</Summary>

### SolubleBiocatalyst

- __concentration__
  - Type: posfloat
  - Description: The concentration of the biocatalyst.
 
- __concentration_unit__
  - Type: string
  - Description: The concentration of the biocatalyst is typically expressed in g/L (grams per liter).

- __concentration_determination_method__
  - Type: string
  - Description: It is important to specify the type of concentration determination. Various methods for determining the concentration of enzymes can be distinguished, including the Bradford method, Lowry method, UV        absorption, activity assays, ELISA, etc.

- __activity__:
  - Type: float
  - Description: The activity of the biocatalyst can be expressed either as volumetric activity, which considers the total activity of the enzyme in the solution, or as specific activity, which takes into account the       enzyme's purity and indicates the activity of an enzyme per unit of enzyme protein or enzyme mass.

- __activity_unit__
  - Type: string
  - Description: In the case of specific activity, the enzyme's activity is expressed in U/mg (Units per milligram), while in the case of volumetric activity, it's expressed in U/mL (Units per milliliter).

- __activity_determination_method__
  - Type: string
  - Description: Enzyme activity can be measured in various ways, including spectrophotometrically, colorimetrically, fluorometrically, using biosensors, etc.

- __formulation__
  - Type: string
  - Description: Depending on the formulation, the biocatalyst may be in a liquid form within a solvent or as a solid powder. It defines the physical state in which the biocatalyst is applied in the reaction.
 
<hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata,       they should be explained here.
  
</details>

<details> <Summary>Crude cell extract</Summary>
  
### CrudeCellExtract

- __cell_disruption_process__
  - Type: string
  - Description: Cell disruption methods include various techniques such as mechanical disruption (e.g., ultrasound), chemical disruption (e.g., detergents), thermal disruption, etc.

- __concentration__
  - Type: posfloat
  - Description: The concentration of the biocatalyst.
 
- __concentration_unit__
  - Type: string
  - Description: The concentration of the biocatalyst is typically expressed in g/L (grams per liter).

- __concentration_determination_method__
  - Type: string
  - Description: It is important to specify the type of concentration determination. Various methods for determining the concentration of enzymes can be distinguished, including the Bradford method, Lowry method, UV        absorption, activity assays, ELISA, etc.
 
 <hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata,       they should be explained here.

</details>

<details> <Summary>Whole cell biocatalyst</Summary>

### WholeCellBiocatalyst

- __harvesting_method__
  - Type: string
  - Description: In biotechnological processes, there are various methods for harvesting cells, including centrifugation, filtration, precipitation, etc.
 
- __concentration__
  - Type: posfloat
  - Description: Typically, in the case of whole-cell catalysts, the cell concentration or cell mass is used as a measure of the quantity of cells used.
 
- __concentration_unit__
  - Type: string
  - Description: When the cells are lyophilized, the quantity of lyophilized cells can be specified in grams or kilograms. If wet cells are used, the cell concentration can be indicated in cells per milliliter              (cells/mL) or cells per gram (cells/g) of wet cell weight.

- __concentration_determination_method__
  - Type: string
  - Description: It is important to specify the type of concentration determination. Various methods for determining the concentration of enzymes can be distinguished, including flow cytometry or the measurement of the     dry weight of biomass, etc.
 
- __formulation__
  - Type: string
  - Description: When applying a whole cell biocatalyst, there are various options. For example, the cells can be cultivated and then lyophilized or used directly as wet cells.

 <hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata,       they should be explained here.

</details>

<details> <Summary>Supernatant</Summary>

### Supernatant

- __separation_method__
  - Type: string
  - Description: There are various methods to separate the supernatant from the cells, common methods include centrifugation, filtration, sedimentation, flow cytometry, etc.

- __concentration__
  - Type: posfloat
  - Description: The concentration of the biocatalyst.
 
- __concentration_unit__
  - Type: string
  - Description: The concentration of the biocatalyst is typically expressed in g/L (grams per liter).

- __concentration_determination_method__
  - Type: string
  - Description: It is important to specify the type of concentration determination. Various methods for determining the concentration of enzymes can be distinguished, including the Bradford method, Lowry method, UV        absorption, activity assays, ELISA, etc.
 
 <hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata,       they should be explained here.

</details>

<details> <Summary>Cell-free-production</Summary>

### CellFreeProduction

- __source_of_cellfree_extract__
  - Type: string
  - Description: Specification of the organism or cell type from which the cell-free extract is derived. This could be bacterial, plant, animal, or another sources.
 
- __concentration__
  - Type: posfloat
  - Description: The concentration of the biocatalyst.
 
- __concentration_unit__
  - Type: string
  - Description: The concentration of the biocatalyst is typically expressed in g/L (grams per liter).

- __concentration_determination_method__
  - Type: string
  - Description: It is important to specify the type of concentration determination. Various methods for determining the concentration of enzymes can be distinguished, including the Bradford method, Lowry method, UV        absorption, activity assays, ELISA, etc.  
 
<hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata,       they should be explained here.

</details>


## Immobilised biocatalysts

<details> <Summary>Immobilised biocatalyst</Summary>

### ImmobilisedBiocatalyst

- __purification_method__
  - Type: string
  - Description: The purification methods can vary depending on whether it involves whole cells or free enzymes. In the case of whole cells, methods such as centrifugation, filtration, or flow cytometry can be              employed. In the case of free enzymes, methods like cell lysis, filtration, chromatography, and precipitation, among others, may be used.

- __concentration__
  - Type: posfloat
  - Description: The concentration of the biocatalyst or the whole cells on the immobilised phase.
 
- __concentration_unit__
  - Type: string
  - Description: For immobilized enzymes, the concentration can be expressed in units such as mg/mL (milligrams of enzyme per milliliter) or g/L (grams of enzyme per liter). When it comes to immobilized cells, units        such as cells/mL (cells per milliliter) or cells/g (cells per gram) of the carrier material or immobilizing matrix can be used.

- __concentration_determination_method__
  - Type: string
  - Description: Various methods are available to determine the concentration of immobilized enzymes or cells. For immobilized enzymes, methods such as protein measurement or enzymatic activity assays can be used. For      immobilized cells, methods like flow cytometry or biomass measurement are applicable.

<hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata,       they should be explained here.

</details>

<details> <Summary>Immobilisation procedure</Summary>

### ImmobilisationProcedure

- __immobilisation_method__
  - Type: string
  - Description: Method for immobilising the enzyme. Common methods are e.g. adsorption, embedding in matrices, crosslinking, coimmobilization with carrier materials, etc. For a comprehensive report of the technical        key data of the immobilization process or method, there is literature for further information, e.g. [Ansorge-Schuhmacher _et_ _al._<sup>1</sup>](https://doi.org/10.1007/978-3-662-57619-9_11) 
 
- __carrier_material__
  - Type: string
  - Despription: If a support material was used, the name of the support material must be specified. This could be e.g. a gel, a membrane or a particle. (__if_applicable__)

<hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata,       they should be explained here.

</details>

<hr>

# Storage conditions

Describing the biocatalyst involves specifying its storage conditions before use in the reaction.

<details> <Summary>Storage conditions</Summary>

### StorageConditions 

- __temperature__
  - Type: float
  - Description: The temperature at which the reactant is stored.
 
- __temperature_unit__
  - Type: string
  - Description: The temperature can be specified in units such as K, °C, or °F.

- __storage_start__
  - Type: date
  - Description: The date since the reactant has been stored.

- __additives__
  - Type: string
  - Description: Additives for the storage of reactants can include antioxidants, stabilizers, drying agent, or even inert gases (argon, nitrogen), among others.

- __removing/rethawing__
  - Type: sting
  - Description: For specific applications, it may be crucial to track how often the reactant has been removed from storage and, if applicable, thawed.

- __thawing_process__
  - Type: string
  - Description: If the reactant needs to be frozen, it is also important to know how this was carried out.

<hr>
 
- __special_treatment__
  - Type: string
  - Description: If there are any other specific characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata, they should be             explained here.


</details>

<hr>

### Literature

[1] B. Ansorge-Schumacher, M. (2018). Enzymimmobilisierung. In: Jaeger, KE., Liese, A., Syldatk, C. (eds) Einführung in die Enzymtechnologie. Springer Spektrum, Berlin, Heidelberg. https://doi.org/10.1007/978-3-662-57619-9_11
