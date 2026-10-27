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

// Sampling Specification Type definitions
/**
    Specification for sampling procedures and sample collection during
    enzymatic reactions.

    * @param sampling_applied - Indicates whether physical sampling was performed at all.
    * @param strategy - Details about the sampling strategy and methodology used.
    * @param samples - Collection of individual samples taken during the reaction.
    * @param notes - Additional notes or comments about the sampling procedure.
**/
export interface Sampling extends JsonLd {
  sampling_applied: boolean;
  strategy?: SamplingStrategy | null;
  samples?: Sample[] | null;
  notes?: string | null;
}

export const SamplingCodec = D.lazy("Sampling", () => D.struct({
    sampling_applied: D.boolean,
    strategy: D.nullable(SamplingStrategyCodec),
    samples: D.array(SampleCodec),
    notes: D.nullable(D.string),
}));


/**
    Strategy and methodology for collecting samples during the reaction
    process.

    * @param strategy_type - Type of sampling strategy employed (default or specialized).
    * @param mixing_during_sampling - Description of mixing conditions maintained during sample collection.
    * @param vessel_opened - Indicates whether the reaction vessel was opened during sampling.
    * @param gas_phase - Description of gas phase conditions or handling during sampling.
    * @param notes - Additional notes about the sampling strategy.
**/
export interface SamplingStrategy extends JsonLd {
  strategy_type: SamplingStrategyType;
  mixing_during_sampling?: string | null;
  vessel_opened?: boolean | null;
  gas_phase?: string | null;
  notes?: string | null;
}

export const SamplingStrategyCodec = D.lazy("SamplingStrategy", () => D.struct({
    strategy_type: SamplingStrategyTypeCodec,
    mixing_during_sampling: D.nullable(D.string),
    vessel_opened: D.nullable(D.boolean),
    gas_phase: D.nullable(D.string),
    notes: D.nullable(D.string),
}));


/**
    Individual sample collected at a specific time point from a specific
    phase of the reaction.

    * @param time - Time point at which the sample was collected.
    * @param time_unit - Unit of measurement for the sampling time.
    * @param amount - Amount or volume of sample collected.
    * @param amount_unit - Unit of measurement for the amount.
    * @param phase - Phase from which the sample was collected (liquid, solid, gas, etc.).
    * @param biocatalyst_in_sample - Description of biocatalyst presence or handling in the sample.
    * @param preprocessing - Any preprocessing steps applied to the sample before analysis.
    * @param notes - Additional notes about the individual sample.
**/
export interface Sample extends JsonLd {
  time?: number | null;
  time_unit?: string | null;
  amount?: number | null;
  amount_unit?: string | null;
  phase?: PhaseType | null;
  biocatalyst_in_sample?: string | null;
  preprocessing?: SamplePreprocessing | null;
  notes?: string | null;
}

export const SampleCodec = D.lazy("Sample", () => D.struct({
    time: D.nullable(D.number),
    time_unit: D.nullable(D.string),
    amount: D.nullable(D.number),
    amount_unit: D.nullable(D.string),
    phase: D.nullable(PhaseTypeCodec),
    biocatalyst_in_sample: D.nullable(D.string),
    preprocessing: D.nullable(SamplePreprocessingCodec),
    notes: D.nullable(D.string),
}));


/**
    Preprocessing steps applied to samples before analysis to preserve or
    prepare them for measurement.

    * @param quenching_method - Method used to quench or stop the reaction in the sample.
    * @param quenching_ratio - Ratio or proportion of quenching agent to sample.
    * @param treatment_procedure - Additional treatment procedures applied to the sample.
    * @param notes - Additional notes about sample preprocessing.
**/
export interface SamplePreprocessing extends JsonLd {
  quenching_method?: string | null;
  quenching_ratio?: number | null;
  treatment_procedure?: string | null;
  notes?: string | null;
}

export const SamplePreprocessingCodec = D.lazy("SamplePreprocessing", () => D.struct({
    quenching_method: D.nullable(D.string),
    quenching_ratio: D.nullable(D.number),
    treatment_procedure: D.nullable(D.string),
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


// Sampling Specification Enum definitions
export enum SamplingStrategyType {
  DEFAULT = 'default',
  SPECIALISED = 'specialised',
}

export const SamplingStrategyTypeCodec = D.union(
  D.literal(SamplingStrategyType.DEFAULT),
  D.literal(SamplingStrategyType.SPECIALISED),
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