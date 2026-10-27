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

// Operation Mode Specification Type definitions
/**
    Specification of the operational mode and configuration for conducting
    biocatalytic reactions.

    * @param mode - The fundamental operation mode defining how the reaction is conducted
             (batch, fed-batch, continuous, or combinatorial).
    * @param reactor_type - Type of reactor configuration used (well-mixed, tubular flow, or
             other).
    * @param feeding - Strategy for feeding reactants into the system during the reaction.
    * @param notes - Additional notes or comments about the operation mode.
**/
export interface OperationMode extends JsonLd {
  mode: OperationModeType;
  reactor_type?: ReactorType | null;
  feeding?: FeedingStrategy | null;
  notes?: string | null;
}

export const OperationModeCodec = D.lazy("OperationMode", () => D.struct({
    mode: OperationModeTypeCodec,
    reactor_type: D.nullable(ReactorTypeCodec),
    feeding: D.nullable(FeedingStrategyCodec),
    notes: D.nullable(D.string),
}));


/**
    Specification of the feeding strategy for introducing reactants during
    non-batch operations.

    * @param feeding_type - Type of feeding approach used (none, discrete, continuous, or
             variable).
    * @param description - Detailed description of the feeding strategy implementation.
**/
export interface FeedingStrategy extends JsonLd {
  feeding_type?: FeedingType | null;
  description?: string | null;
}

export const FeedingStrategyCodec = D.lazy("FeedingStrategy", () => D.struct({
    feeding_type: D.nullable(FeedingTypeCodec),
    description: D.nullable(D.string),
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


// Operation Mode Specification Enum definitions
export enum OperationModeType {
  BATCH = 'batch',
  COMBINATORIAL = 'combinatorial',
  CONTINUOUS = 'continuous',
  FED_BATCH = 'fed_batch',
}

export const OperationModeTypeCodec = D.union(
  D.literal(OperationModeType.BATCH),
  D.literal(OperationModeType.COMBINATORIAL),
  D.literal(OperationModeType.CONTINUOUS),
  D.literal(OperationModeType.FED_BATCH),
);

export enum FeedingType {
  CONTINUOUS = 'continuous',
  DISCRETE = 'discrete',
  NONE = 'none',
  VARIABLE = 'variable',
}

export const FeedingTypeCodec = D.union(
  D.literal(FeedingType.CONTINUOUS),
  D.literal(FeedingType.DISCRETE),
  D.literal(FeedingType.NONE),
  D.literal(FeedingType.VARIABLE),
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