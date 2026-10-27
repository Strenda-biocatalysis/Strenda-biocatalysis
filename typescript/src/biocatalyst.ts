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

// Biocatalyst Specification Type definitions
/**
    A biocatalyst is an enzyme or enzyme-containing system used to
    catalyze biochemical reactions. This section defines the complete
    characterization of a biocatalyst including its identity, source,
    application conditions, immobilization status, and storage
    requirements.

    * @param identity - Essential identifying information about the biocatalyst including
             name, EC number, molecular properties, and sequence data.
    * @param source_type
    * @param source - Information about how the biocatalyst was obtained, whether purchased
             commercially or produced in-house.
    * @param application - Details about how the biocatalyst is applied in the reaction,
             including concentration, activity, and workflow
             specifics.
    * @param immobilization - Information about whether and how the biocatalyst is immobilized on a
             support material.
    * @param storage - Conditions under which the biocatalyst is stored to maintain its
             activity and stability.
    * @param notes - Additional notes or comments about the biocatalyst that don't fit in
             other categories.
**/
export interface Biocatalyst extends JsonLd {
  identity: BiocatalystIdentity;
  source_type?: BiocatalystSourceType | null;
  source?: BiocatalystSource | null;
  application?: BiocatalystApplication | null;
  immobilization?: Immobilization | null;
  storage?: StorageConditions | null;
  notes?: string | null;
}

export const BiocatalystCodec = D.lazy("Biocatalyst", () => D.struct({
    identity: BiocatalystIdentityCodec,
    source_type: D.nullable(BiocatalystSourceTypeCodec),
    source: D.nullable(BiocatalystSourceCodec),
    application: D.nullable(BiocatalystApplicationCodec),
    immobilization: D.nullable(ImmobilizationCodec),
    storage: D.nullable(StorageConditionsCodec),
    notes: D.nullable(D.string),
}));


/**
    Core identifying information and molecular characteristics of the
    biocatalyst enzyme.

    * @param name - The name of the biocatalyst, which can be the trivial name, systematic
             name, or trade name.
    * @param ec_number - The Enzyme Commission (EC) number that classifies the enzyme according
             to the reaction it catalyzes.
    * @param molecular_weight - The molecular weight of the enzyme in the specified units.
    * @param molecular_weight_unit - The unit of measurement for the molecular weight (e.g., kDa, Da).
    * @param catalyzed_reaction - Description of the specific reaction or type of reaction catalyzed by
             this enzyme.
    * @param sequences - Amino acid and/or DNA sequence information for the enzyme.
    * @param origin_organism - The organism from which the enzyme was originally derived or isolated.
    * @param production_organism - The organism used to produce the enzyme (may differ from origin
             organism for recombinant enzymes).
    * @param posttranslational_modification - Any post-translational modifications present on the enzyme that may
             affect its activity or properties.
**/
export interface BiocatalystIdentity extends JsonLd {
  name: string;
  ec_number?: string[] | null;
  molecular_weight?: number | null;
  molecular_weight_unit?: MolecularWeightUnit | null;
  catalyzed_reaction?: string[] | null;
  sequences?: SequenceInfo | null;
  origin_organism?: string | null;
  production_organism?: string | null;
  posttranslational_modification?: string[] | null;
}

export const BiocatalystIdentityCodec = D.lazy("BiocatalystIdentity", () => D.struct({
    name: D.string,
    ec_number: D.array(D.string),
    molecular_weight: D.nullable(D.number),
    molecular_weight_unit: D.nullable(MolecularWeightUnitCodec),
    catalyzed_reaction: D.array(D.string),
    sequences: D.nullable(SequenceInfoCodec),
    origin_organism: D.nullable(D.string),
    production_organism: D.nullable(D.string),
    posttranslational_modification: D.array(D.string),
}));


/**
    Sequence information for the biocatalyst at both the protein and
    nucleic acid levels.

    * @param sequence_amino_acid - The amino acid sequence of the enzyme in single-letter code format.
    * @param sequence_dna - The DNA sequence encoding the enzyme.
**/
export interface SequenceInfo extends JsonLd {
  sequence_amino_acid?: string[] | null;
  sequence_dna?: string[] | null;
}

export const SequenceInfoCodec = D.lazy("SequenceInfo", () => D.struct({
    sequence_amino_acid: D.array(D.string),
    sequence_dna: D.array(D.string),
}));


/**
    Information about the source and procurement of the biocatalyst.

    * @param source_type - Whether the biocatalyst was purchased from a supplier or produced
             in-house.
    * @param supplier - Name of the commercial supplier or source of the biocatalyst.
    * @param purchased_details - Specific details relevant to commercially purchased biocatalysts.
    * @param self_produced_details - Specific details relevant to biocatalysts produced in-house.
**/
export interface BiocatalystSource extends JsonLd {
  source_type: BiocatalystSourceType;
  supplier?: string | null;
  purchased_details?: PurchasedDetails | null;
  self_produced_details?: SelfProducedDetails | null;
}

export const BiocatalystSourceCodec = D.lazy("BiocatalystSource", () => D.struct({
    source_type: BiocatalystSourceTypeCodec,
    supplier: D.nullable(D.string),
    purchased_details: D.nullable(PurchasedDetailsCodec),
    self_produced_details: D.nullable(SelfProducedDetailsCodec),
}));


/**
    Detailed information for commercially purchased biocatalysts.

    * @param reference - Product code, catalog number, or other reference identifier from the
             supplier.
    * @param purity - Purity of the purchased biocatalyst as specified by the supplier,
             typically as a percentage.
    * @param purity_specification - Method or specification used to determine the purity (e.g., SDS-PAGE,
             activity assay).
    * @param formulation - Physical form of the purchased biocatalyst (dissolved, powder, etc.).
**/
export interface PurchasedDetails extends JsonLd {
  reference?: string | null;
  purity?: number | null;
  purity_specification?: string | null;
  formulation?: FormulationType | null;
}

export const PurchasedDetailsCodec = D.lazy("PurchasedDetails", () => D.struct({
    reference: D.nullable(D.string),
    purity: D.nullable(D.number),
    purity_specification: D.nullable(D.string),
    formulation: D.nullable(FormulationTypeCodec),
}));


/**
    Detailed information for biocatalysts produced in-house.

    * @param sequence_plasmid - Sequence of the plasmid used for enzyme expression.
    * @param plasmid_specifications - Details about the plasmid construction, including vector backbone,
             promoter, and other relevant features.
    * @param purification_method - Method(s) used to purify the enzyme after expression.
    * @param purity - Achieved purity of the self-produced biocatalyst, typically as a
             percentage.
    * @param purity_specification - Method used to determine the purity of the self-produced enzyme.
    * @param formulation - Physical form of the self-produced biocatalyst after purification
             and processing.
**/
export interface SelfProducedDetails extends JsonLd {
  sequence_plasmid?: string[] | null;
  plasmid_specifications?: string[] | null;
  purification_method?: string[] | null;
  purity?: number | null;
  purity_specification?: string | null;
  formulation?: FormulationType | null;
}

export const SelfProducedDetailsCodec = D.lazy("SelfProducedDetails", () => D.struct({
    sequence_plasmid: D.array(D.string),
    plasmid_specifications: D.array(D.string),
    purification_method: D.array(D.string),
    purity: D.nullable(D.number),
    purity_specification: D.nullable(D.string),
    formulation: D.nullable(FormulationTypeCodec),
}));


/**
    Details about how the biocatalyst is applied and used in the reaction
    system.

    * @param application_type - The form in which the biocatalyst is applied (purified enzyme, crude
             extract, whole cells, etc.).
    * @param concentration - Concentration of the biocatalyst in the reaction mixture.
    * @param activity - Measured enzymatic activity of the biocatalyst under the reaction
             conditions.
    * @param workflow_details - Specific workflow steps and methods used in applying the biocatalyst.
**/
export interface BiocatalystApplication extends JsonLd {
  application_type: BiocatalystApplicationType;
  concentration?: Concentration[] | null;
  activity?: Activity[] | null;
  workflow_details?: ApplicationWorkflowDetails | null;
}

export const BiocatalystApplicationCodec = D.lazy("BiocatalystApplication", () => D.struct({
    application_type: BiocatalystApplicationTypeCodec,
    concentration: D.array(ConcentrationCodec),
    activity: D.array(ActivityCodec),
    workflow_details: D.nullable(ApplicationWorkflowDetailsCodec),
}));


/**
    Quantitative information about biocatalyst concentration in the
    reaction.

    * @param value - Numerical value of the concentration.
    * @param unit - Unit of measurement for the concentration (e.g., mg/mL, µM, U/mL).
    * @param determination_method - Method used to determine or calculate the concentration.
**/
export interface Concentration extends JsonLd {
  value?: number | null;
  unit?: string | null;
  determination_method?: string | null;
}

export const ConcentrationCodec = D.lazy("Concentration", () => D.struct({
    value: D.nullable(D.number),
    unit: D.nullable(D.string),
    determination_method: D.nullable(D.string),
}));


/**
    Enzymatic activity measurement of the biocatalyst.

    * @param value - Numerical value of the measured activity.
    * @param unit - Unit of measurement for the activity (e.g., U/mg, µmol/min/mg).
    * @param determination_method - Assay method used to measure the enzymatic activity.
**/
export interface Activity extends JsonLd {
  value?: number | null;
  unit?: string | null;
  determination_method?: string | null;
}

export const ActivityCodec = D.lazy("Activity", () => D.struct({
    value: D.nullable(D.number),
    unit: D.nullable(D.string),
    determination_method: D.nullable(D.string),
}));


/**
    Specific workflow steps and procedures used when applying the
    biocatalyst.

    * @param cell_disruption_process - Method used to disrupt cells if working with whole cell preparations.
    * @param harvesting_method - Method used to harvest cells or enzyme from the production system.
    * @param separation_method - Method used to separate the biocatalyst from other components.
    * @param source_of_cellfree_extract - Details about the source and preparation of cell-free extracts if
             applicable.
**/
export interface ApplicationWorkflowDetails extends JsonLd {
  cell_disruption_process?: string | null;
  harvesting_method?: string | null;
  separation_method?: string | null;
  source_of_cellfree_extract?: string | null;
}

export const ApplicationWorkflowDetailsCodec = D.lazy("ApplicationWorkflowDetails", () => D.struct({
    cell_disruption_process: D.nullable(D.string),
    harvesting_method: D.nullable(D.string),
    separation_method: D.nullable(D.string),
    source_of_cellfree_extract: D.nullable(D.string),
}));


/**
    Information about biocatalyst immobilization on solid supports.

    * @param immobilized - Whether the biocatalyst is immobilized (true) or used in free form
             (false).
    * @param biocatalyst_state - Physical state of the biocatalyst during immobilization (e.g.,
             purified enzyme, crude extract).
    * @param immobilisation_chemistry - Chemical method or mechanism used for immobilization (e.g., covalent
             binding, adsorption, entrapment).
    * @param carrier_material - Material used as the solid support for immobilization.
    * @param linkers - Chemical linkers or spacers used between the enzyme and carrier
             material.
    * @param immobilisation_method - Detailed procedure used for the immobilization process.
    * @param purification_method - Method used to purify or wash the immobilized biocatalyst.
    * @param loading - Amount of enzyme loaded onto the carrier material.
    * @param notes - Additional notes about the immobilization process or properties.
**/
export interface Immobilization extends JsonLd {
  immobilized: boolean;
  biocatalyst_state?: string | null;
  immobilisation_chemistry?: string[] | null;
  carrier_material?: string[] | null;
  linkers?: string[] | null;
  immobilisation_method?: string[] | null;
  purification_method?: string[] | null;
  loading?: Concentration | null;
  notes?: string | null;
}

export const ImmobilizationCodec = D.lazy("Immobilization", () => D.struct({
    immobilized: D.boolean,
    biocatalyst_state: D.nullable(D.string),
    immobilisation_chemistry: D.array(D.string),
    carrier_material: D.array(D.string),
    linkers: D.array(D.string),
    immobilisation_method: D.array(D.string),
    purification_method: D.array(D.string),
    loading: D.nullable(ConcentrationCodec),
    notes: D.nullable(D.string),
}));


/**
    Quantitative measurement with value and unit specification.

    * @param value - Numerical value of the measurement.
    * @param unit - Unit of measurement for the value.
**/
export interface Quantity extends JsonLd {
  value?: number | null;
  unit?: string | null;
}

export const QuantityCodec = D.lazy("Quantity", () => D.struct({
    value: D.nullable(D.number),
    unit: D.nullable(D.string),
}));


/**
    Conditions under which materials (biocatalysts, components, etc.) are
    stored to maintain stability and integrity.

    * @param temperature - Storage temperature value.
    * @param temperature_unit - Unit for the storage temperature (e.g., °C, K).
    * @param storage_start - Date when storage under these conditions began or material was
             received.
    * @param additives - Any additives or stabilizers used during storage (e.g., glycerol,
             stabilizers, preservatives).
    * @param drying_method - Method used to dry the material if stored in dry form (optional,
             primarily for biocatalysts).
    * @param notes - Additional notes about storage conditions or requirements.
**/
export interface StorageConditions extends JsonLd {
  temperature?: number | null;
  temperature_unit?: string | null;
  storage_start?: string | null;
  additives?: string[] | null;
  drying_method?: string[] | null;
  notes?: string | null;
}

export const StorageConditionsCodec = D.lazy("StorageConditions", () => D.struct({
    temperature: D.nullable(D.number),
    temperature_unit: D.nullable(D.string),
    storage_start: D.nullable(D.string),
    additives: D.array(D.string),
    drying_method: D.array(D.string),
    notes: D.nullable(D.string),
}));


// Biocatalyst Specification Enum definitions
export enum BiocatalystSourceType {
  PURCHASED = 'purchased',
  SELF_PRODUCED = 'self_produced',
}

export const BiocatalystSourceTypeCodec = D.union(
  D.literal(BiocatalystSourceType.PURCHASED),
  D.literal(BiocatalystSourceType.SELF_PRODUCED),
);

export enum BiocatalystApplicationType {
  CELL_FREE = 'cell_free',
  CRUDE_CELL_EXTRACT = 'crude_cell_extract',
  PURIFIED = 'purified',
  SECRETED = 'secreted',
  WHOLE_CELL = 'whole_cell',
}

export const BiocatalystApplicationTypeCodec = D.union(
  D.literal(BiocatalystApplicationType.CELL_FREE),
  D.literal(BiocatalystApplicationType.CRUDE_CELL_EXTRACT),
  D.literal(BiocatalystApplicationType.PURIFIED),
  D.literal(BiocatalystApplicationType.SECRETED),
  D.literal(BiocatalystApplicationType.WHOLE_CELL),
);

export enum MolecularWeightUnit {
  DA = 'Da',
  KDA = 'kDa',
  OTHER = 'other',
}

export const MolecularWeightUnitCodec = D.union(
  D.literal(MolecularWeightUnit.DA),
  D.literal(MolecularWeightUnit.KDA),
  D.literal(MolecularWeightUnit.OTHER),
);

export enum FormulationType {
  DISSOLVED = 'dissolved',
  GAS = 'gas',
  LIQUID = 'liquid',
  OTHER = 'other',
  POWDER = 'powder',
  SOLUTION = 'solution',
}

export const FormulationTypeCodec = D.union(
  D.literal(FormulationType.DISSOLVED),
  D.literal(FormulationType.GAS),
  D.literal(FormulationType.LIQUID),
  D.literal(FormulationType.OTHER),
  D.literal(FormulationType.POWDER),
  D.literal(FormulationType.SOLUTION),
);

export enum PhaseType {
  GAS = 'gas',
  LIQUID = 'liquid',
  MIXED = 'mixed',
  OTHER = 'other',
  SOLID = 'solid',
}

export const PhaseTypeCodec = D.union(
  D.literal(PhaseType.GAS),
  D.literal(PhaseType.LIQUID),
  D.literal(PhaseType.MIXED),
  D.literal(PhaseType.OTHER),
  D.literal(PhaseType.SOLID),
);

export enum ReactorType {
  OTHER = 'other',
  TUBULAR_FLOW = 'tubular_flow',
  WELL_MIXED = 'well_mixed',
}

export const ReactorTypeCodec = D.union(
  D.literal(ReactorType.OTHER),
  D.literal(ReactorType.TUBULAR_FLOW),
  D.literal(ReactorType.WELL_MIXED),
);