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

// Reaction Conditions Specification Type definitions
/**
    Comprehensive specification of the physical and chemical conditions
    under which a biocatalytic reaction is performed, including
    reactor setup, reaction system characteristics, temperature and
    pH profiles.

    * @param reactor - Configuration and specifications of the reactor used for the
             biocatalytic reaction.
    * @param system - Characterization of the reaction system as monoliquid or multiphasic.
    * @param phases - Individual phases present in the reaction system (liquid, solid, gas).
    * @param temperature - Temperature conditions throughout the reaction, which can be constant,
             event-based, or follow a gradient.
    * @param pH - pH conditions throughout the reaction, which can be constant, event-
             based, or follow a gradient.
    * @param notes - Additional notes or comments about the reaction conditions.
**/
export interface ReactionConditions extends JsonLd {
  reactor: ReactorSetup;
  system: ReactionSystem;
  phases?: Phase[] | null;
  temperature?: TemperatureProfile | null;
  pH?: PHProfile | null;
  notes?: string | null;
}

export const ReactionConditionsCodec = D.lazy("ReactionConditions", () => D.struct({
    reactor: ReactorSetupCodec,
    system: ReactionSystemCodec,
    phases: D.array(PhaseCodec),
    temperature: D.nullable(TemperatureProfileCodec),
    pH: D.nullable(PHProfileCodec),
    notes: D.nullable(D.string),
}));


/**
    Configuration and operational parameters of the reactor system used
    for the biocatalytic reaction.

    * @param reactor_type - Type of reactor configuration used (well-mixed or tubular flow).
    * @param flow - Flow rate specifications for continuous or fed-batch operations.
    * @param notes - Additional notes about the reactor setup.
**/
export interface ReactorSetup extends JsonLd {
  reactor_type: ReactorType;
  flow?: FlowConditions | null;
  notes?: string | null;
}

export const ReactorSetupCodec = D.lazy("ReactorSetup", () => D.struct({
    reactor_type: ReactorTypeCodec,
    flow: D.nullable(FlowConditionsCodec),
    notes: D.nullable(D.string),
}));


/**
    Specifications for flow rates in continuous or fed-batch reactor
    operations.

    * @param flow_rate - Numerical value of the flow rate.
    * @param flow_rate_unit - Unit of measurement for the flow rate.
**/
export interface FlowConditions extends JsonLd {
  flow_rate?: number | null;
  flow_rate_unit?: string | null;
}

export const FlowConditionsCodec = D.lazy("FlowConditions", () => D.struct({
    flow_rate: D.nullable(D.number),
    flow_rate_unit: D.nullable(D.string),
}));


/**
    Characterization of the reaction system based on the number and types
    of phases present.

    * @param system_type - Classification of the system as monoliquid or multiphasic.
    * @param monoliquid - Specifications for single-phase liquid systems.
    * @param multiphasic - Specifications for systems containing multiple phases.
    * @param notes - Additional notes about the reaction system.
**/
export interface ReactionSystem extends JsonLd {
  system_type: SystemType;
  monoliquid?: MonoliquidSystem | null;
  multiphasic?: MultiphasicSystem | null;
  notes?: string | null;
}

export const ReactionSystemCodec = D.lazy("ReactionSystem", () => D.struct({
    system_type: SystemTypeCodec,
    monoliquid: D.nullable(MonoliquidSystemCodec),
    multiphasic: D.nullable(MultiphasicSystemCodec),
    notes: D.nullable(D.string),
}));


/**
    Specifications for single-phase liquid reaction systems.

    * @param solvent_description - Detailed description of the solvent or solvent mixture used.
    * @param ionic_strength - Ionic strength of the solution, affecting enzyme activity and
             stability.
    * @param further_additives - Description of any additional additives present in the system.
    * @param notes - Additional notes about the monoliquid system.
**/
export interface MonoliquidSystem extends JsonLd {
  solvent_description?: string | null;
  ionic_strength?: number | null;
  further_additives?: string | null;
  notes?: string | null;
}

export const MonoliquidSystemCodec = D.lazy("MonoliquidSystem", () => D.struct({
    solvent_description: D.nullable(D.string),
    ionic_strength: D.nullable(D.number),
    further_additives: D.nullable(D.string),
    notes: D.nullable(D.string),
}));


/**
    Specifications for reaction systems containing multiple distinct
    phases.

    * @param phases_number - Total number of distinct phases present in the system.
    * @param notes - Additional notes about the multiphasic system.
**/
export interface MultiphasicSystem extends JsonLd {
  phases_number?: number | null;
  notes?: string | null;
}

export const MultiphasicSystemCodec = D.lazy("MultiphasicSystem", () => D.struct({
    phases_number: D.nullable(D.number),
    notes: D.nullable(D.string),
}));


/**
    Specification of individual phases within the reaction system.

    * @param phase_type - Physical state of the phase (liquid, solid, or gas).
    * @param material_description - Detailed description of the materials comprising this phase.
    * @param amount - Quantity of material in this phase.
    * @param amount_unit - Unit of measurement for the amount.
    * @param notes - Additional notes about this specific phase.
**/
export interface Phase extends JsonLd {
  phase_type: PhaseType;
  material_description?: string | null;
  amount?: number | null;
  amount_unit?: string | null;
  notes?: string | null;
}

export const PhaseCodec = D.lazy("Phase", () => D.struct({
    phase_type: PhaseTypeCodec,
    material_description: D.nullable(D.string),
    amount: D.nullable(D.number),
    amount_unit: D.nullable(D.string),
    notes: D.nullable(D.string),
}));


/**
    Specification of temperature conditions throughout the biocatalytic
    reaction, which can follow various patterns depending on the
    reaction requirements.

    * @param profile_type - Type of temperature profile used (constant, event-based, multipoint,
             or gradient).
    * @param temperature_unit - Unit of measurement for temperature values.
    * @param constant_temperature - Temperature value for constant temperature profiles.
    * @param profile_points - Series of temperature points for event-based or multipoint profiles.
    * @param gradient - Gradient specifications for temperature ramp profiles.
    * @param notes - Additional notes about the temperature profile.
**/
export interface TemperatureProfile extends JsonLd {
  profile_type: ProfileType;
  temperature_unit?: string | null;
  constant_temperature?: number | null;
  profile_points?: ProfilePoint[] | null;
  gradient?: Gradient | null;
  notes?: string | null;
}

export const TemperatureProfileCodec = D.lazy("TemperatureProfile", () => D.struct({
    profile_type: ProfileTypeCodec,
    temperature_unit: D.nullable(D.string),
    constant_temperature: D.nullable(D.number),
    profile_points: D.array(ProfilePointCodec),
    gradient: D.nullable(GradientCodec),
    notes: D.nullable(D.string),
}));


/**
    Individual temperature measurement point in time-based temperature
    profiles.

    * @param value - Temperature value at this point.
    * @param time - Time at which this temperature is measured or set.
    * @param time_unit - Unit of measurement for the time value.
    * @param event_description - Description of any specific event associated with this temperature
             point.
**/
export interface ProfilePoint extends JsonLd {
  value?: number | null;
  time?: number | null;
  time_unit?: string | null;
  event_description?: string | null;
}

export const ProfilePointCodec = D.lazy("ProfilePoint", () => D.struct({
    value: D.nullable(D.number),
    time: D.nullable(D.number),
    time_unit: D.nullable(D.string),
    event_description: D.nullable(D.string),
}));


/**
    Specification for temperature gradient profiles where temperature
    changes linearly over time or distance.

    * @param start_value - Initial temperature value at the beginning of the gradient.
    * @param end_value - Final temperature value at the end of the gradient.
    * @param length - Duration or distance over which the gradient is applied.
    * @param length_unit - Unit of measurement for the gradient length (time or distance).
    * @param measurement_points - Description of how temperature is measured along the gradient.
**/
export interface Gradient extends JsonLd {
  start_value?: number | null;
  end_value?: number | null;
  length?: number | null;
  length_unit?: string | null;
  measurement_points?: string | null;
}

export const GradientCodec = D.lazy("Gradient", () => D.struct({
    start_value: D.nullable(D.number),
    end_value: D.nullable(D.number),
    length: D.nullable(D.number),
    length_unit: D.nullable(D.string),
    measurement_points: D.nullable(D.string),
}));


/**
    Specification of pH conditions throughout the biocatalytic reaction,
    which can follow various patterns to optimize enzyme activity
    and stability.

    * @param profile_type - Type of pH profile used (constant, event-based, multipoint, or
             gradient).
    * @param constant_pH - pH value for constant pH profiles.
    * @param profile_points - Series of pH points for event-based or multipoint profiles.
    * @param gradient - Gradient specifications for pH ramp profiles.
    * @param detection - Methods and conditions used for pH detection and measurement.
    * @param notes - Additional notes about the pH profile.
**/
export interface PHProfile extends JsonLd {
  profile_type: ProfileType;
  constant_pH?: number | null;
  profile_points?: PHPoint[] | null;
  gradient?: PHGradient | null;
  detection?: PHDetection | null;
  notes?: string | null;
}

export const PHProfileCodec = D.lazy("PHProfile", () => D.struct({
    profile_type: ProfileTypeCodec,
    constant_pH: D.nullable(D.number),
    profile_points: D.array(PHPointCodec),
    gradient: D.nullable(PHGradientCodec),
    detection: D.nullable(PHDetectionCodec),
    notes: D.nullable(D.string),
}));


/**
    Individual pH measurement point in time-based pH profiles.

    * @param value - pH value at this point.
    * @param time - Time at which this pH is measured or set.
    * @param time_unit - Unit of measurement for the time value.
    * @param event_description - Description of any specific event associated with this pH point.
**/
export interface PHPoint extends JsonLd {
  value?: number | null;
  time?: number | null;
  time_unit?: string | null;
  event_description?: string | null;
}

export const PHPointCodec = D.lazy("PHPoint", () => D.struct({
    value: D.nullable(D.number),
    time: D.nullable(D.number),
    time_unit: D.nullable(D.string),
    event_description: D.nullable(D.string),
}));


/**
    Specification for pH gradient profiles where pH changes linearly over
    time.

    * @param start_value - Initial pH value at the beginning of the gradient.
    * @param end_value - Final pH value at the end of the gradient.
    * @param length - Duration over which the pH gradient is applied.
    * @param length_unit - Unit of measurement for the gradient duration.
    * @param measurement_points - Measurement points along the gradient.
**/
export interface PHGradient extends JsonLd {
  start_value?: number | null;
  end_value?: number | null;
  length?: number | null;
  length_unit?: string | null;
  measurement_points?: number[] | null;
}

export const PHGradientCodec = D.lazy("PHGradient", () => D.struct({
    start_value: D.nullable(D.number),
    end_value: D.nullable(D.number),
    length: D.nullable(D.number),
    length_unit: D.nullable(D.string),
    measurement_points: D.array(D.number),
}));


/**
    Specifications for pH measurement methods and calibration conditions.

    * @param detected_when - Timing or conditions under which pH is detected.
    * @param detected_how - Method or instrument used for pH detection.
    * @param temperature - Temperature at which pH measurements are calibrated or performed.
    * @param temperature_unit - Unit of measurement for the calibration temperature.
    * @param calibration_pH_electrode - Details about pH electrode calibration procedures and standards.
**/
export interface PHDetection extends JsonLd {
  detected_when?: string | null;
  detected_how?: string | null;
  temperature?: number | null;
  temperature_unit?: string | null;
  calibration_pH_electrode?: string | null;
}

export const PHDetectionCodec = D.lazy("PHDetection", () => D.struct({
    detected_when: D.nullable(D.string),
    detected_how: D.nullable(D.string),
    temperature: D.nullable(D.number),
    temperature_unit: D.nullable(D.string),
    calibration_pH_electrode: D.nullable(D.string),
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


// Reaction Conditions Specification Enum definitions
export enum SystemType {
  MONOLIQUID = 'monoliquid',
  MULTIPHASIC = 'multiphasic',
}

export const SystemTypeCodec = D.union(
  D.literal(SystemType.MONOLIQUID),
  D.literal(SystemType.MULTIPHASIC),
);

export enum ProfileType {
  CONSTANT = 'constant',
  EVENT_BASED = 'event_based',
  GRADIENT = 'gradient',
  MULTIPOINT = 'multipoint',
}

export const ProfileTypeCodec = D.union(
  D.literal(ProfileType.CONSTANT),
  D.literal(ProfileType.EVENT_BASED),
  D.literal(ProfileType.GRADIENT),
  D.literal(ProfileType.MULTIPOINT),
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