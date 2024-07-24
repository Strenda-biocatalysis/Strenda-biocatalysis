import * as D from 'io-ts/Decoder';
import { isLeft } from "fp-ts/Either";

// Generic validate function
export function validate<T>(codec: D.Decoder<unknown, T>, value: unknown): T {
  const result = codec.decode(value);
  if (isLeft(result)) {
    throw new Error(D.draw(result.left));
  }
  return result.right;
}

// JSON-LD Types
export interface JsonLdContext {
  [key: string]: any;
}

export interface JsonLd {
  '@context'?: JsonLdContext;
  '@id'?: string;
  '@type'?: string;
}

// Biocatalyst Type definitions
/**
    Important information to characterize the biocatalyst and determine
    its origin.Biocatalyst self-produced

    * @param name - The name of the biocatalyst can be either generic based on the
             catalyzed reaction, for example, 'lipase' or more
             specifically by describing the genus and species, such
             as '
    * @param ec_number - Numerical classification system that categorizes enzymes based on
             their biochemical function and reaction mechanism, such
             as EC 3.1.4.12.
    * @param molecular_weight - The molecular weight (MW) refer to the sum of the atomic weights of
             the atoms in a molecule and therefore describes the mass
             of an enzyme.
    * @param molecular_weight_unit - The enzyme size or molar weight is typically expressed in kDa
             (kilodaltons).
    * @param catalyzed_reaction - The reaction catalyzed by the biocatalyst.
    * @param sequence_amino_acid - The amino acid sequence of the biocatalyst. The amino acid sequence
             can be represented in either a three-letter or one-
             letter code. For instance, "Ala-Ser-Gly" corresponds
             to the three-letter code, while "ASG" represents
             the same sequence in the one-letter code. One of the
             databases commonly used for storing and retrieving
             amino acid sequences is the UniProt database (https://
             www.uniprot.org/). UniProt provides extensive information
             on protein sequences, including their one-letter and
             three-letter amino acid codes, allowing researchers to
             access and analyze various protein sequences.
    * @param sequence_DNA - The DNA sequence of the biocatalyst including any tags and linkers.
    * @param origin_organism - The specific species or source from which the enzyme is derived or
             isolated. It includes information about the genus and
             species of the organism. However, the cell type from
             which the biocatalyst is derived could be bacterial, as
             well as plant, animal, or other sources. (
    * @param supplier - Information about the supplier from which the enzyme was purchased.
             If possible, a reference for the purchased biocatalyst
             should also be provided.
    * @param production_organism - Information about the organism in which the biocatalyst was
             produced is crucial in the context of heterologous gene
             expression.
    * @param posttranslational_modification - Information about any chemical modifications or alterations that occur
             to the biocatalyst's protein structure after translation,
             such as phosphorylation, glycosylation, acetylation,
             methylation, ubiquitination and other modifications.
    * @param purity - Purity of enzymes typically expressed in percentage (%). It is usually
             stated as the percentage of the pure enzyme or active
             component relative to the total mass of the enzyme
             preparation.
    * @param purity_specification - Description of how the purity of the biocatalyst was determined. In
             case of purchased enzymes, this information is often
             available from the product specification sheet.
    * @param formulation - Depending on the formulation, the biocatalyst can exist either in a
             dissolved state within a solvent or as a solid powder.
             It defines the physical state in which the biocatalyst
             is used. Additional information regarding the application
             or formulation in the experiment should be entered in the
             next subcategory.
**/
export interface BiocatalystPurchased extends JsonLd {
  name: string;
  ec_number: string;
  molecular_weight: number;
  molecular_weight_unit: string;
  catalyzed_reaction: string;
  sequence_amino_acid: string;
  sequence_DNA: string;
  origin_organism: string;
  supplier: string;
  production_organism: string;
  posttranslational_modification: string;
  purity: number;
  purity_specification: string;
  formulation: string;
}

export const BiocatalystPurchasedCodec = D.lazy("BiocatalystPurchased", () => D.struct({
    name: D.string,
    ec_number: D.string,
    molecular_weight: D.number,
    molecular_weight_unit: D.string,
    catalyzed_reaction: D.string,
    sequence_amino_acid: D.string,
    sequence_DNA: D.string,
    origin_organism: D.string,
    supplier: D.string,
    production_organism: D.string,
    posttranslational_modification: D.string,
    purity: D.number,
    purity_specification: D.string,
    formulation: D.string,
}));


/**
    Important information to characterize the biocatalyst and to describe
    it clearly.

    * @param name - The name of the biocatalyst can be either generic based on the
             catalyzed reaction, for example, 'lipase' or more
             specifically by describing the genus and species, such
             as '
    * @param ec_number - Numerical classification system that categorizes enzymes based on
             their biochemical function and reaction mechanism, such
             as EC 3.1.4.12.
    * @param molecular_weight - The molecular weight (MW) refer to the sum of the atomic weights of
             the atoms in a molecule and therefore describes the mass
             of an enzyme.
    * @param molecular_weight_unit - The enzyme size or molar weight is typically expressed in kDa
             (kilodaltons).
    * @param catalyzed_reaction - The reaction catalyzed by the biocatalyst.
    * @param sequence_amino_acid - The amino acid sequence of the biocatalyst. The amino acid sequence
             can be represented in either a three-letter or one-
             letter code. For instance, "Ala-Ser-Gly" corresponds
             to the three-letter code, while "ASG" represents
             the same sequence in the one-letter code. One of the
             databases commonly used for storing and retrieving
             amino acid sequences is the UniProt database (https://
             www.uniprot.org/). UniProt provides extensive information
             on protein sequences, including their one-letter and
             three-letter amino acid codes, allowing researchers to
             access and analyze various protein sequences.
    * @param sequence_DNA - The DNA sequence of the biocatalyst including any tags and linkers.
    * @param sequence_plasmid - The DNA sequence of the plasmid used to produce the biocatalyst. The
             sequence can be provided in plain text or as a database
             ID.
    * @param plasmid_specifications - All DNA sequence changes (e.g. codon optimization for
    * @param origin_organism - The specific species or source from which the enzyme is derived or
             isolated. It includes information about the genus and
             species of the organism. (
    * @param production_organism - Information about the organism in which the biocatalyst was
             produced is crucial in the context of heterologous gene
             expression. If the production strain was purchased, more
             detailed information on the manufacturer and the organism
             should be provided.
    * @param posttranslational_modification - Information about any chemical modifications or alterations that occur
             to the biocatalyst's protein structure after translation,
             such as phosphorylation, glycosylation, acetylation,
             methylation, ubiquitination and other modifications.
    * @param purity - Purity of enzymes typically expressed in percentage (%). It is usually
             stated as the percentage of the pure enzyme or active
             component relative to the total mass of the enzyme
             preparation.
    * @param purity_specification - The choice of method for the purity determination depends on the type
             of enzyme and the available resources and may include gel
             electrophoresis, HPLC, ELISA, Western blotting, etc.
    * @param purification_method - The choice of purification methods is diverse and can impact the
             enzyme, with possible methods including chromatographic
             techniques, precipitation, HPLC, ultrafiltration,
             dialysis, salt fractionation, etc.
    * @param formulation - Depending on the formulation, the biocatalyst can exist either in a
             dissolved state within a solvent or as a solid powder.
             It defines the physical state in which the biocatalyst
             is used. Additional information regarding the application
             or formulation in the experiment should be entered in the
             next subcategory.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the biocatalyst that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface BiocatalystSelfProduced extends JsonLd {
  name: string;
  ec_number: string;
  molecular_weight: number;
  molecular_weight_unit: string;
  catalyzed_reaction: string;
  sequence_amino_acid: string;
  sequence_DNA: string;
  sequence_plasmid: string;
  plasmid_specifications: string;
  origin_organism: string;
  production_organism: string;
  posttranslational_modification: string;
  purity: number;
  purity_specification: string;
  purification_method: string;
  formulation: string;
  special_treatment: string;
}

export const BiocatalystSelfProducedCodec = D.lazy("BiocatalystSelfProduced", () => D.struct({
    name: D.string,
    ec_number: D.string,
    molecular_weight: D.number,
    molecular_weight_unit: D.string,
    catalyzed_reaction: D.string,
    sequence_amino_acid: D.string,
    sequence_DNA: D.string,
    sequence_plasmid: D.string,
    plasmid_specifications: D.string,
    origin_organism: D.string,
    production_organism: D.string,
    posttranslational_modification: D.string,
    purity: D.number,
    purity_specification: D.string,
    purification_method: D.string,
    formulation: D.string,
    special_treatment: D.string,
}));


/**
    The soluble enzyme refers to purified enzyme.Crude cell extract

    * @param concentration - Concentration of the biocatalyst.
    * @param concentration_unit - Concentration of the biocatalyst is typically expressed in g/L (grams
             per liter).
    * @param concentration_determination_method - It is important to specify the method used for concentration
             determination. There are various methods available for
             the determination of the enzyme concentration in solution
             e.g., the Bradford method, Lowry method, UV absorption,
             activity assays, ELISA, etc.
    * @param activity - The activity of the biocatalyst can be expressed either as volumetric
             activity, which considers the total activity of the
             enzyme in the solution, or as specific activity, which
             takes into account the enzyme's purity and indicates
             the activity of an enzyme per unit of enzyme protein
             or enzyme mass. If the biocatalyst has been purchased,
             it is advisable to look up more precise information
             (e.g. via an SOP) regarding the activities specified by
             the manufacturer, as these may differ from the values
             determined by yourself (different activity assays can
             lead to different activity values). In addition, the loss
             of activity of the biocatalyst over the storage period
             should be taken into account.
    * @param activity_unit - The enzyme's activity can be expressed either as specific activity []
             [][]
    * @param activity_determination_method - Enzyme activity can be measured in various ways, including
             spectrophotometrically, colorimetrically,
             fluorometrically, assays and using biosensors, etc.
    * @param formulation - Depending on the formulation, the biocatalyst can be applied dissolved
             in a solvent or as a dried powder. It defines the
             physical state in which the biocatalyst is applied in
             the reaction.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the biocatalyst that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface PurifiedBiocatalyst extends JsonLd {
  concentration: number;
  concentration_unit: string;
  concentration_determination_method: string;
  activity: number;
  activity_unit: string;
  activity_determination_method: string;
  formulation: string;
  special_treatment: string;
}

export const PurifiedBiocatalystCodec = D.lazy("PurifiedBiocatalyst", () => D.struct({
    concentration: D.number,
    concentration_unit: D.string,
    concentration_determination_method: D.string,
    activity: D.number,
    activity_unit: D.string,
    activity_determination_method: D.string,
    formulation: D.string,
    special_treatment: D.string,
}));


/**
    Whole cell biocatalyst

    * @param cell_disruption_process - Cell disruption processes and methods include various techniques such
             as mechanical disruption (e.g., grinding, homogenization,
             ultrasonication, french press), chemical disruption
             (e.g., detergents, enzymes), physical techniques (e.g.,
             electroporation, high-pressure homogenization, thermal
             treatment) to break cell walls and release cell contents.
    * @param concentration - Concentration of the biocatalyst.
    * @param concentration_unit - Concentration of the biocatalyst is typically expressed in g/L (grams
             per liter).
    * @param concentration_determination_method - It is important to specify the type of concentration determination.
             There are numerous methods available to determine protein
             content, yet only a few are suitable for estimating or
             determining the protein content of the target protein
             within a mixture. Some of these methods include activity
             assays or the Western blotting technique, which relies on
             prior SDS-PAGE and antibody binding for detection.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the biocatalyst that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface CrudeCellExtract extends JsonLd {
  cell_disruption_process: string;
  concentration: number;
  concentration_unit: string;
  concentration_determination_method: string;
  special_treatment: string;
}

export const CrudeCellExtractCodec = D.lazy("CrudeCellExtract", () => D.struct({
    cell_disruption_process: D.string,
    concentration: D.number,
    concentration_unit: D.string,
    concentration_determination_method: D.string,
    special_treatment: D.string,
}));


/**
    Secreted enzyme

    * @param harvesting_method - In biotechnological processes, there are various methods for
             harvesting cells, including centrifugation, filtration,
             precipitation, etc.
    * @param concentration - In the case of whole-cell catalysts, the cell concentration or cell
             mass is commonly used as a measure.
    * @param concentration_unit - In case of lyophilized cells, the quantity of lyophilized cells can
             be specified in g (grams) or kg (kilograms). If wet
             cells are used, the cell concentration can be indicated
             in cells/mL (cells per milliliter) or cells/g (cells per
             gram) of wet cell weight. Other common indications of the
             concentration of wet cells as biocatalysts are the cell
             concentration in g/L (grams per liter) or OD (optical
             density).
    * @param concentration_determination_method - Specify the method for cell number per cell weight determination
             (e.g., flow cytometry, weight of dry biomass,
             spectrophotometry).
    * @param formulation - When applying a whole cell biocatalyst, there are various options.
             Cultivated cells can be lyophilized or used as wet cells
             after separation from the medium.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the biocatalyst that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface WholeCellBiocatalyst extends JsonLd {
  harvesting_method: string;
  concentration: number;
  concentration_unit: string;
  concentration_determination_method: string;
  formulation: string;
  special_treatment: string;
}

export const WholeCellBiocatalystCodec = D.lazy("WholeCellBiocatalyst", () => D.struct({
    harvesting_method: D.string,
    concentration: D.number,
    concentration_unit: D.string,
    concentration_determination_method: D.string,
    formulation: D.string,
    special_treatment: D.string,
}));


/**
    Cell-free-production

    * @param separation_method - There are various methods to separate the supernatant from the cells,
             common methods include centrifugation, filtration,
             sedimentation, etc.
    * @param concentration - Concentration of the biocatalyst.
    * @param concentration_unit - Concentration of the biocatalyst is typically expressed in g/L (grams
             per liter).
    * @param concentration_determination_method - It is important to specify the type of concentration determination.
             There are numerous methods available to determine protein
             content, yet only a few are suitable for estimating or
             determining the protein content of the target protein
             within a mixture. Some of these methods include activity
             assays or the Western blotting technique, which relies on
             prior SDS-PAGE and antibody binding for detection.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the biocatalyst that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface SecretedEnzyme extends JsonLd {
  separation_method: string;
  concentration: number;
  concentration_unit: string;
  concentration_determination_method: string;
  special_treatment: string;
}

export const SecretedEnzymeCodec = D.lazy("SecretedEnzyme", () => D.struct({
    separation_method: D.string,
    concentration: D.number,
    concentration_unit: D.string,
    concentration_determination_method: D.string,
    special_treatment: D.string,
}));


/**
    Cell-free enzyme production or gene expression refers to a process
    where the synthesis of the biocatalyst occurs outside of living
    cells. This technique involves extracting cellular components,
    such as ribosomes, DNA, RNA, and other necessary cellular
    machinery, and using them in a controlled environment (usually
    in vitro) to produce proteins or enzymes. For further information
    see, e.g. Khambhati _et al._1.

    * @param source_of_cellfree_extract - Specifiy the organism or cell type from which the cell-free extract
             is derived (e.g., by describing the genus and species).
             These could be bacterial, plant, animal, or another
             sources. If available, reference can be made to an
             appropriate database entry.
    * @param concentration - Concentration of the biocatalyst.
    * @param concentration_unit - Concentration of the biocatalyst is typically expressed in g/L (grams
             per liter).
    * @param concentration_determination_method - It is important to specify the type of concentration determination.
             There are numerous methods available to determine protein
             content, yet only a few are suitable for estimating or
             determining the protein content of the target protein
             within a mixture. Some of these methods include activity
             assays or the Western blotting technique, which relies on
             prior SDS-PAGE and antibody binding for detection.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the biocatalyst that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface CellFreeProduction extends JsonLd {
  source_of_cellfree_extract: string;
  concentration: number;
  concentration_unit: string;
  concentration_determination_method: string;
  special_treatment: string;
}

export const CellFreeProductionCodec = D.lazy("CellFreeProduction", () => D.struct({
    source_of_cellfree_extract: D.string,
    concentration: D.number,
    concentration_unit: D.string,
    concentration_determination_method: D.string,
    special_treatment: D.string,
}));


/**
    * @param biocatalyst - When it comes to the immobilization method, it is also important to
             mention how the biocatalyst to be immobilized is present
             (for example, as a purified enzyme, or as a crude cell
             extract, etc.).
    * @param immobilisation_chemistry - This aspect denotes the specific chemical methods or techniques
             used to attach the enzymes onto the chosen base
             material. Different immobilization chemistries involve
             various covalent or non-covalent bonding strategies,
             including crosslinking, adsorption, covalent bonding,
             encapsulation, specific binding via (affinity)tag, or
             entrapment.
    * @param carrier_material - If a support material, base, or carrier was utilized, it is necessary
             to specify the material's name (e.g., gel, membrane,
             particle) along with the supplier and further product
             details (
    * @param linkers - Linkers are chemical compounds used to establish a connection or
             bridge between the enzymes and the carrier material.
             These linkers play a vital role in stabilizing the
             immobilized enzymes and can influence the efficiency
             and functionality of the immobilization process. They
             facilitate binding between the enzymes and the carrier
             material, promoting a stable and active biocatalyst
             structure. Common and widespread linkers are spacer
             molecules, crosslinkers, avidin-biotin or silane coupling
             agents. (
    * @param immobilisation_method - Specify further details regarding the immobilisation method of the
             enzyme. For a comprehensive report around the technical
             key data of the immobilization process or method,
             see literature for further information, e.g. Ansorge-
             Schumacher2.
    * @param purification_method - The purification methods can vary depending on whether it involves
             whole cells or free enzymes. In the case of whole cells,
             methods such as centrifugation, filtration, or flow
             cytometry can be employed. In the case of free enzymes,
             methods like cell lysis, filtration, chromatography, and
             precipitation, among others, may be used.
    * @param concentration - Concentration of the biocatalyst or the whole cells on the immobilised
             phase.
    * @param concentration_unit - For immobilized enzymes, the concentration is often quantified
             in terms of enzyme activity per volume (e.g., units
             per milliliter, U/mL) or weight measurements such
             as milligrams or grams per liter (mg/L or g/L).
             When referring to immobilized cells (not the enzymes
             themselves), units of cells/mL (cells per milliliter) or
             cells/g (cells per gram) are commonly utilized.
    * @param concentration_determination_method - Various methods are available to determine the concentration of
             immobilized enzymes or cells. For immobilized enzymes,
             methods such as protein measurement or enzymatic activity
             assays can be used. The protein determination can be
             determined on the carrier material using a BCA test or
             as a differential measurement using the Bradford method,
             $\Delta$280 or also after detachment of the enzyme
             from the carrier material. An activity measurement is
             best suited as it provides the activity per gram of
             immobilized material. For immobilized cells, methods like
             flow cytometry or biomass measurement are applicable.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the biocatalyst that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface Immobilised extends JsonLd {
  biocatalyst: string;
  immobilisation_chemistry: string;
  carrier_material: string;
  linkers: string;
  immobilisation_method: string;
  purification_method: string;
  concentration: number;
  concentration_unit: string;
  concentration_determination_method: string;
  special_treatment: string;
}

export const ImmobilisedCodec = D.lazy("Immobilised", () => D.struct({
    biocatalyst: D.string,
    immobilisation_chemistry: D.string,
    carrier_material: D.string,
    linkers: D.string,
    immobilisation_method: D.string,
    purification_method: D.string,
    concentration: D.number,
    concentration_unit: D.string,
    concentration_determination_method: D.string,
    special_treatment: D.string,
}));


/**
    * @param temperature - The temperature at which the reactant is stored.
    * @param temperature_unit - The temperature can be specified in units such as K, °C, or °F.
    * @param storage_start - The date since the biocatalyst has been stored.
    * @param additives - Additives for the storage of biocatalyst can include antioxidants,
             stabilizers, drying agent, or even inert gases (argon,
             nitrogen), among others.
    * @param drying_method - For biocatalysts, various drying methods are employed (e.g., freeze-
             drying, also known as lyophilization, spray-drying, a
             method that involves atomizing a solution into small
             particles before drying, or vacuum drying, which removes
             moisture through low-pressure conditions). (
    * @param special_treatment - If there are any other specific characteristics or aspects related to
             the biocatalyst that are important for reproducibility
             and are not described by the aforementioned metadata,
             they should be explained here.
**/
export interface StorageConditions extends JsonLd {
  temperature: number;
  temperature_unit: string;
  storage_start: string;
  additives: string;
  drying_method: string;
  special_treatment: string;
}

export const StorageConditionsCodec = D.lazy("StorageConditions", () => D.struct({
    temperature: D.number,
    temperature_unit: D.string,
    storage_start: D.string,
    additives: D.string,
    drying_method: D.string,
    special_treatment: D.string,
}));