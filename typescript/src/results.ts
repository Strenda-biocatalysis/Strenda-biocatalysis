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

// Results Specification Type definitions
/**
    Comprehensive collection of experimental results from enzymatic
    reactions.

    * @param kinetics - Kinetic parameters and enzyme behavior characteristics.
    * @param yield_and_conversion - Product yield and substrate conversion measurements.
    * @param activity - Enzyme activity and initial reaction rate data.
    * @param selectivity - Selectivity measurements including stereoselectivity and
             enantioselectivity.
    * @param thermodynamics - Thermodynamic parameters of the reaction.
    * @param notes - Additional notes or comments about the experimental results.
**/
export interface ExperimentalResults extends JsonLd {
  kinetics?: KineticResults | null;
  yield_and_conversion?: YieldAndConversionResults | null;
  activity?: ActivityResults | null;
  selectivity?: SelectivityResults | null;
  thermodynamics?: ThermodynamicResults | null;
  notes?: string | null;
}

export const ExperimentalResultsCodec = D.lazy("ExperimentalResults", () => D.struct({
    kinetics: D.nullable(KineticResultsCodec),
    yield_and_conversion: D.nullable(YieldAndConversionResultsCodec),
    activity: D.nullable(ActivityResultsCodec),
    selectivity: D.nullable(SelectivityResultsCodec),
    thermodynamics: D.nullable(ThermodynamicResultsCodec),
    notes: D.nullable(D.string),
}));


/**
    Kinetic parameters characterizing enzyme behavior and reaction
    mechanisms.

    * @param michaelis_constant - Michaelis constant (Km) representing the substrate concentration at
             half-maximum reaction rate.
    * @param maximum_reaction_rate - Maximum reaction rate (Vmax) achieved under saturating substrate
             conditions.
    * @param turnover_number - Turnover number (kcat) representing the maximum number of substrate
             molecules converted per enzyme molecule per unit time.
    * @param catalytic_efficiency - Catalytic efficiency (kcat/Km) indicating the enzyme's effectiveness
             at low substrate concentrations.
    * @param dissociation_constant - Dissociation constant (Kd) for enzyme-substrate or enzyme-inhibitor
             binding.
    * @param inhibition - Parameters describing enzyme inhibition characteristics.
    * @param hill_coefficient - Hill coefficient indicating cooperativity in substrate binding or
             enzyme kinetics.
    * @param enzyme_stability - Qualitative or quantitative description of enzyme stability under
             reaction conditions.
    * @param notes - Additional notes about kinetic measurements or observations.
**/
export interface KineticResults extends JsonLd {
  michaelis_constant?: number | null;
  maximum_reaction_rate?: number | null;
  turnover_number?: number | null;
  catalytic_efficiency?: number | null;
  dissociation_constant?: number | null;
  inhibition?: InhibitionParameters | null;
  hill_coefficient?: number | null;
  enzyme_stability?: string | null;
  notes?: string | null;
}

export const KineticResultsCodec = D.lazy("KineticResults", () => D.struct({
    michaelis_constant: D.nullable(D.number),
    maximum_reaction_rate: D.nullable(D.number),
    turnover_number: D.nullable(D.number),
    catalytic_efficiency: D.nullable(D.number),
    dissociation_constant: D.nullable(D.number),
    inhibition: D.nullable(InhibitionParametersCodec),
    hill_coefficient: D.nullable(D.number),
    enzyme_stability: D.nullable(D.string),
    notes: D.nullable(D.string),
}));


/**
    Parameters describing enzyme inhibition characteristics and
    mechanisms.

    * @param inhibition_type - Type of inhibition mechanism observed.
    * @param inhibition_constant - Inhibition constant (Ki) quantifying the strength of inhibitor
             binding.
**/
export interface InhibitionParameters extends JsonLd {
  inhibition_type?: InhibitionType | null;
  inhibition_constant?: number | null;
}

export const InhibitionParametersCodec = D.lazy("InhibitionParameters", () => D.struct({
    inhibition_type: D.nullable(InhibitionTypeCodec),
    inhibition_constant: D.nullable(D.number),
}));


/**
    Product yield and substrate conversion measurements from enzymatic
    reactions.

    * @param product_yield - Product yield as percentage or fraction of theoretical maximum.
    * @param space_time_yield - Space-time yield representing product formation rate per unit reactor
             volume.
    * @param conversion - Substrate conversion as percentage or fraction of initial substrate
             consumed.
    * @param notes - Additional notes about yield and conversion measurements.
**/
export interface YieldAndConversionResults extends JsonLd {
  product_yield?: number[] | null;
  space_time_yield?: number | null;
  conversion?: number | null;
  notes?: string | null;
}

export const YieldAndConversionResultsCodec = D.lazy("YieldAndConversionResults", () => D.struct({
    product_yield: D.array(D.number),
    space_time_yield: D.nullable(D.number),
    conversion: D.nullable(D.number),
    notes: D.nullable(D.string),
}));


/**
    Enzyme activity measurements and initial reaction rate data.

    * @param specific_activity - Specific activity representing enzyme activity per unit mass of enzyme
             protein.
    * @param initial_reaction_rate - Initial reaction rate measured at the beginning of the reaction.
    * @param notes - Additional notes about activity measurements.
**/
export interface ActivityResults extends JsonLd {
  specific_activity?: number | null;
  initial_reaction_rate?: number | null;
  notes?: string | null;
}

export const ActivityResultsCodec = D.lazy("ActivityResults", () => D.struct({
    specific_activity: D.nullable(D.number),
    initial_reaction_rate: D.nullable(D.number),
    notes: D.nullable(D.string),
}));


/**
    Selectivity measurements including stereoselectivity,
    enantioselectivity, and other selectivity parameters.

    * @param stereoselectivity - Qualitative or quantitative description of stereoselectivity in the
             reaction.
    * @param enantioselectivity - Enantioselectivity ratio (E-value) indicating preference for one
             enantiomer over another.
    * @param enantiomeric_excess - Enantiomeric excess (ee) as percentage indicating optical purity of
             the product.
    * @param diastereomeric_excess - Diastereomeric excess (de) as percentage for reactions producing
             diastereomers.
    * @param isomeric_content - Content or ratio of specific isomers in the product mixture.
    * @param chemoselectivity - Description of chemoselectivity when multiple reaction pathways are
             possible.
    * @param regioselectivity - Description of regioselectivity indicating preference for specific
             reaction sites.
    * @param notes - Additional notes about selectivity measurements.
**/
export interface SelectivityResults extends JsonLd {
  stereoselectivity?: string | null;
  enantioselectivity?: number | null;
  enantiomeric_excess?: number | null;
  diastereomeric_excess?: number | null;
  isomeric_content?: number | null;
  chemoselectivity?: string | null;
  regioselectivity?: string | null;
  notes?: string | null;
}

export const SelectivityResultsCodec = D.lazy("SelectivityResults", () => D.struct({
    stereoselectivity: D.nullable(D.string),
    enantioselectivity: D.nullable(D.number),
    enantiomeric_excess: D.nullable(D.number),
    diastereomeric_excess: D.nullable(D.number),
    isomeric_content: D.nullable(D.number),
    chemoselectivity: D.nullable(D.string),
    regioselectivity: D.nullable(D.string),
    notes: D.nullable(D.string),
}));


/**
    Thermodynamic parameters characterizing the energetics of the
    enzymatic reaction.

    * @param gibbs_free_energy_change - Gibbs free energy change (ΔG) for the reaction.
    * @param enthalpy_change - Enthalpy change (ΔH) for the reaction.
    * @param entropy_change - Entropy change (ΔS) for the reaction.
    * @param notes - Additional notes about thermodynamic measurements.
**/
export interface ThermodynamicResults extends JsonLd {
  gibbs_free_energy_change?: string | null;
  enthalpy_change?: string | null;
  entropy_change?: string | null;
  notes?: string | null;
}

export const ThermodynamicResultsCodec = D.lazy("ThermodynamicResults", () => D.struct({
    gibbs_free_energy_change: D.nullable(D.string),
    enthalpy_change: D.nullable(D.string),
    entropy_change: D.nullable(D.string),
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


// Results Specification Enum definitions
export enum InhibitionType {
  COMPETITIVE = 'competitive',
  IRREVERSIBLE = 'irreversible',
  MIXED = 'mixed',
  NONCOMPETITIVE = 'non_competitive',
  OTHER = 'other',
  UNCOMPETITIVE = 'uncompetitive',
}

export const InhibitionTypeCodec = D.union(
  D.literal(InhibitionType.COMPETITIVE),
  D.literal(InhibitionType.IRREVERSIBLE),
  D.literal(InhibitionType.MIXED),
  D.literal(InhibitionType.NONCOMPETITIVE),
  D.literal(InhibitionType.OTHER),
  D.literal(InhibitionType.UNCOMPETITIVE),
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