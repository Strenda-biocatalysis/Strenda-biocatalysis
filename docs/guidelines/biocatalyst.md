# Biocatalyst

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        biocatalystpurchased(BiocatalystPurchased)
        biocatalystselfproduced(BiocatalystSelfProduced)
        purifiedbiocatalyst(PurifiedBiocatalyst)
        crudecellextract(CrudeCellExtract)
        wholecellbiocatalyst(WholeCellBiocatalyst)
        secretedenzyme(SecretedEnzyme)
        cellfreeproduction(CellFreeProduction)
        immobilised(Immobilised)
        storageconditions(StorageConditions)
    
        click biocatalystpurchased "#biocatalystpurchased" "Go to BiocatalystPurchased"
        click biocatalystselfproduced "#biocatalystselfproduced" "Go to BiocatalystSelfProduced"
        click purifiedbiocatalyst "#purifiedbiocatalyst" "Go to PurifiedBiocatalyst"
        click crudecellextract "#crudecellextract" "Go to CrudeCellExtract"
        click wholecellbiocatalyst "#wholecellbiocatalyst" "Go to WholeCellBiocatalyst"
        click secretedenzyme "#secretedenzyme" "Go to SecretedEnzyme"
        click cellfreeproduction "#cellfreeproduction" "Go to CellFreeProduction"
        click immobilised "#immobilised" "Go to Immobilised"
        click storageconditions "#storageconditions" "Go to StorageConditions"
    ```



## Types


### BiocatalystPurchased
Important information to characterize the biocatalyst and determine its origin.Biocatalyst self-produced

__name__* `string`

- The name of the biocatalyst can be either generic based on the catalyzed reaction, for example, 'lipase' or more specifically by describing the genus and species, such as '

__ec_number__* `string`

- Numerical classification system that categorizes enzymes based on their biochemical function and reaction mechanism, such as EC 3.1.4.12.

__molecular_weight__* `float`

- The molecular weight (MW) refer to the sum of the atomic weights of the atoms in a molecule and therefore describes the mass of an enzyme.
- `Minimum`: 0.0

__molecular_weight_unit__* `string`

- The enzyme size or molar weight is typically expressed in kDa (kilodaltons).

__catalyzed_reaction__* `string`

- The reaction catalyzed by the biocatalyst.

__sequence_amino_acid__* `string`

- The amino acid sequence of the biocatalyst. The amino acid sequence can be represented in either a three-letter or one-letter code. For instance, "Ala-Ser-Gly" corresponds to the three-letter code, while "ASG" represents the same sequence in the one-letter code. One of the databases commonly used for storing and retrieving amino acid sequences is the UniProt database (https://www.uniprot.org/). UniProt provides extensive information on protein sequences, including their one-letter and three-letter amino acid codes, allowing researchers to access and analyze various protein sequences.

__sequence_DNA__* `string`

- The DNA sequence of the biocatalyst including any tags and linkers.

__origin_organism__* `string`

- The specific species or source from which the enzyme is derived or isolated. It includes information about the genus and species of the organism. However, the cell type from which the biocatalyst is        derived could be bacterial, as well as plant, animal, or other sources. (

__supplier__* `string`

- Information about the supplier from which the enzyme was purchased. If possible, a reference for the purchased biocatalyst should also be provided.

__production_organism__* `string`

- Information about the organism in which the biocatalyst was produced is crucial in the context of heterologous gene expression.

__posttranslational_modification__* `string`

- Information about any chemical modifications or alterations that occur to the biocatalyst's protein structure after translation, such as phosphorylation, glycosylation, acetylation,               methylation, ubiquitination and other modifications.

__purity__* `float`

- Purity of enzymes typically expressed in percentage (%). It is usually stated as the percentage of the pure enzyme or active component relative to the total mass of the enzyme preparation.

__purity_specification__* `string`

- Description of how the purity of the biocatalyst was determined. In case of purchased enzymes, this information is often available from the product specification sheet.

__formulation__* `string`

- Depending on the formulation, the biocatalyst can exist either in a dissolved state within a solvent or as a solid powder. It defines the physical state in which the biocatalyst is used. Additional information regarding the application or formulation in the experiment should be entered in the next subcategory.

------

### BiocatalystSelfProduced
Important information to characterize the biocatalyst and to describe it clearly.

__name__* `string`

- The name of the biocatalyst can be either generic based on the catalyzed reaction, for example, 'lipase' or more specifically by describing the genus and species, such as '

__ec_number__* `string`

- Numerical classification system that categorizes enzymes based on their biochemical function and reaction mechanism, such as EC 3.1.4.12.

__molecular_weight__* `float`

- The molecular weight (MW) refer to the sum of the atomic weights of the atoms in a molecule and therefore describes the mass of an enzyme.
- `Minimum`: 0.0

__molecular_weight_unit__* `string`

- The enzyme size or molar weight is typically expressed in kDa (kilodaltons).

__catalyzed_reaction__* `string`

- The reaction catalyzed by the biocatalyst.

__sequence_amino_acid__* `string`

- The amino acid sequence of the biocatalyst. The amino acid sequence can be represented in either a three-letter or one-letter code. For instance, "Ala-Ser-Gly" corresponds to the three-letter code, while "ASG" represents the same sequence in the one-letter code. One of the databases commonly used for storing and retrieving amino acid sequences is the UniProt database (https://www.uniprot.org/). UniProt provides extensive information on protein sequences, including their one-letter and three-letter amino acid codes, allowing researchers to access and analyze various protein sequences.

__sequence_DNA__* `string`

- The DNA sequence of the biocatalyst including any tags and linkers.

__sequence_plasmid__* `string`

- The DNA sequence of the plasmid used to produce the biocatalyst. The sequence can be provided in plain text or as a database ID.

__plasmid_specifications__* `string`

- All DNA sequence changes (e.g. codon optimization for

__origin_organism__* `string`

- The specific species or source from which the enzyme is derived or isolated. It includes information about the genus and species of the organism. (

__production_organism__* `string`

- Information about the organism in which the biocatalyst was produced is crucial in the context of heterologous gene expression. If the production strain was purchased, more detailed information on the manufacturer and the organism should be provided.

__posttranslational_modification__* `string`

- Information about any chemical modifications or alterations that occur to the biocatalyst's protein structure after translation, such as phosphorylation, glycosylation, acetylation,               methylation, ubiquitination and other modifications.

__purity__* `float`

- Purity of enzymes typically expressed in percentage (%). It is usually stated as the percentage of the pure enzyme or active component relative to the total mass of the enzyme preparation.

__purity_specification__* `string`

- The choice of method for the purity determination depends on the type of enzyme and the available resources and may include gel electrophoresis, HPLC, ELISA, Western blotting, etc.

__purification_method__* `string`

- The choice of purification methods is diverse and can impact the enzyme, with possible methods including chromatographic techniques, precipitation, HPLC, ultrafiltration, dialysis, salt fractionation,      etc.

__formulation__* `string`

- Depending on the formulation, the biocatalyst can exist either in a dissolved state within a solvent or as a solid powder. It defines the physical state in which the biocatalyst is used. Additional information regarding the application or formulation in the experiment should be entered in the next subcategory.

__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata,       they should be explained here.

------

### PurifiedBiocatalyst
The soluble enzyme refers to purified enzyme.Crude cell extract

__concentration__* `float`

- Concentration of the biocatalyst.
- `Minimum`: 0

__concentration_unit__* `string`

- Concentration of the biocatalyst is typically expressed in g/L (grams per liter).

__concentration_determination_method__* `string`

- It is important to specify the method used for concentration determination. There are various methods available for the determination of the enzyme concentration in solution e.g., the Bradford method, Lowry method, UV absorption, activity assays, ELISA, etc.

__activity__* `float`

- The activity of the biocatalyst can be expressed either as volumetric activity, which considers the total activity of the enzyme in the solution, or as specific activity, which takes into account the       enzyme's purity and indicates the activity of an enzyme per unit of enzyme protein or enzyme mass. If the biocatalyst has been purchased, it is advisable to look up more precise information (e.g. via an SOP)            regarding the activities specified by the manufacturer, as these may differ from the values determined by yourself (different activity assays can lead to different activity values). In addition, the loss of activity of the biocatalyst over the storage period should be taken into account.

__activity_unit__* `string`

- The enzyme's activity can be expressed either as specific activity [][][]

__activity_determination_method__* `string`

- Enzyme activity can be measured in various ways, including spectrophotometrically, colorimetrically, fluorometrically, assays and using biosensors, etc.

__formulation__* `string`

- Depending on the formulation, the biocatalyst can be applied dissolved in a solvent or as a dried powder. It defines the physical state in which the biocatalyst is applied in the reaction.

__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata,       they should be explained here.

------

### CrudeCellExtract
Whole cell biocatalyst

__cell_disruption_process__* `string`

- Cell disruption processes and methods include various techniques such as mechanical disruption (e.g., grinding, homogenization, ultrasonication, french press), chemical disruption (e.g., detergents, enzymes), physical techniques (e.g., electroporation, high-pressure homogenization, thermal treatment) to break cell walls and release cell contents.

__concentration__* `float`

- Concentration of the biocatalyst.
- `Minimum`: 0.0

__concentration_unit__* `string`

- Concentration of the biocatalyst is typically expressed in g/L (grams per liter).

__concentration_determination_method__* `string`

- It is important to specify the type of concentration determination. There are numerous methods available to determine protein content, yet only a few are suitable for estimating or determining the protein content of the target protein within a mixture. Some of these methods include activity assays or the Western blotting technique, which relies on prior SDS-PAGE and antibody binding for detection.

__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata,       they should be explained here.

------

### WholeCellBiocatalyst
Secreted enzyme

__harvesting_method__* `string`

- In biotechnological processes, there are various methods for harvesting cells, including centrifugation, filtration, precipitation, etc.

__concentration__* `float`

- In the case of whole-cell catalysts, the cell concentration or cell mass is commonly used as a measure.
- `Minimum`: 0.0

__concentration_unit__* `string`

- In case of lyophilized cells, the quantity of lyophilized cells can be specified in g (grams) or kg (kilograms). If wet cells are used, the cell concentration can be indicated in cells/mL (cells per milliliter) or cells/g (cells per gram) of wet cell weight. Other common indications of the concentration of wet cells as biocatalysts are the cell concentration in g/L (grams per liter) or OD (optical density).

__concentration_determination_method__* `string`

- Specify the method for cell number per cell weight determination (e.g., flow cytometry, weight of dry biomass, spectrophotometry).

__formulation__* `string`

- When applying a whole cell biocatalyst, there are various options. Cultivated cells can be lyophilized or used as wet cells after separation from the medium.

__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata,       they should be explained here.

------

### SecretedEnzyme
Cell-free-production

__separation_method__* `string`

- There are various methods to separate the supernatant from the cells, common methods include centrifugation, filtration, sedimentation, etc.

__concentration__* `float`

- Concentration of the biocatalyst.
- `Minimum`: 0.0

__concentration_unit__* `string`

- Concentration of the biocatalyst is typically expressed in g/L (grams per liter).

__concentration_determination_method__* `string`

- It is important to specify the type of concentration determination. There are numerous methods available to determine protein content, yet only a few are suitable for estimating or determining the protein content of the target protein within a mixture. Some of these methods include activity assays or the Western blotting technique, which relies on prior SDS-PAGE and antibody binding for detection.

__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata,       they should be explained here.

------

### CellFreeProduction
Cell-free enzyme production or gene expression refers to a process where the synthesis of the biocatalyst occurs outside of living cells. This technique involves extracting cellular components, such as ribosomes, DNA, RNA, and other necessary cellular machinery, and using them in a controlled environment (usually in vitro) to produce proteins or enzymes. For further information see, e.g. Khambhati _et al._1.

__source_of_cellfree_extract__* `string`

- Specifiy the organism or cell type from which the cell-free extract is derived (e.g., by describing the genus and species). These could be bacterial, plant, animal, or another sources. If available, reference can be made to an appropriate database entry.

__concentration__* `float`

- Concentration of the biocatalyst.
- `Minimum`: 0.0

__concentration_unit__* `string`

- Concentration of the biocatalyst is typically expressed in g/L (grams per liter).

__concentration_determination_method__* `string`

- It is important to specify the type of concentration determination. There are numerous methods available to determine protein content, yet only a few are suitable for estimating or determining the protein content of the target protein within a mixture. Some of these methods include activity assays or the Western blotting technique, which relies on prior SDS-PAGE and antibody binding for detection.

__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata,       they should be explained here.

------

### Immobilised


__biocatalyst__* `string`

- When it comes to the immobilization method, it is also important to mention how the biocatalyst to be immobilized is present (for example, as a purified enzyme, or as a crude cell extract, etc.).

__immobilisation_chemistry__* `string`

- This aspect denotes the specific chemical methods or techniques used to attach the enzymes onto the chosen base material. Different immobilization chemistries involve various covalent or non-covalent       bonding strategies, including crosslinking, adsorption, covalent bonding, encapsulation, specific binding via (affinity)tag, or entrapment.

__carrier_material__* `string`

- If a support material, base, or carrier was utilized, it is necessary to specify the material's name (e.g., gel, membrane, particle) along with the supplier and further product details (

__linkers__* `string`

- Linkers are chemical compounds used to establish a connection or bridge between the enzymes and the carrier material. These linkers play a vital role in stabilizing the immobilized enzymes and can           influence the efficiency and functionality of the immobilization process. They facilitate binding between the enzymes and the carrier material, promoting a stable and active biocatalyst structure. Common and            widespread linkers are spacer molecules, crosslinkers, avidin-biotin or silane coupling agents. (

__immobilisation_method__* `string`

- Specify further details regarding the immobilisation method of the enzyme. For a comprehensive report around the technical key data of the immobilization process or method, see literature for further              information, e.g. Ansorge-Schumacher2.

__purification_method__* `string`

- The purification methods can vary depending on whether it involves whole cells or free enzymes. In the case of whole cells, methods such as centrifugation, filtration, or flow cytometry can be              employed. In the case of free enzymes, methods like cell lysis, filtration, chromatography, and precipitation, among others, may be used.

__concentration__* `float`

- Concentration of the biocatalyst or the whole cells on the immobilised phase.
- `Minimum`: 0.0

__concentration_unit__* `string`

- For immobilized enzymes, the concentration is often quantified in terms of enzyme activity per volume (e.g., units per milliliter, U/mL) or weight measurements such as milligrams or grams per liter (mg/L or g/L). When referring to immobilized cells (not the enzymes themselves), units of cells/mL (cells per milliliter) or cells/g (cells per gram) are commonly utilized.

__concentration_determination_method__* `string`

- Various methods are available to determine the concentration of immobilized enzymes or cells. For immobilized enzymes, methods such as protein measurement or enzymatic activity assays can be used. The protein determination can be determined on the carrier material using a BCA test or as a differential measurement using the Bradford method, $\Delta$280 or also after detachment of the enzyme from the carrier material. An activity measurement is best suited as it provides the activity per gram of immobilized material. For immobilized cells, methods like flow cytometry or biomass measurement are applicable.

__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata,       they should be explained here.

------

### StorageConditions


__temperature__* `float`

- The temperature at which the reactant is stored.

__temperature_unit__* `string`

- The temperature can be specified in units such as K, °C, or °F.

__storage_start__* `date`

- The date since the biocatalyst has been stored.

__additives__* `string`

- Additives for the storage of biocatalyst can include antioxidants, stabilizers, drying agent, or even inert gases (argon, nitrogen), among others.

__drying_method__* `string`

- For biocatalysts, various drying methods are employed (e.g., freeze-drying, also known as lyophilization, spray-drying, a method that involves atomizing a solution into small particles before drying, or vacuum drying, which removes moisture through low-pressure conditions). (

__special_treatment__* `string`

- If there are any other specific characteristics or aspects related to the biocatalyst that are important for reproducibility and are not described by the aforementioned metadata, they should be             explained here.