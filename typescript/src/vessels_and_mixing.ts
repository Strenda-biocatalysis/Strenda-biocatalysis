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

// Vessels and Mixing Specification Type definitions
/**
    Specification of the vessel and mixing configuration for conducting
    biocatalytic reactions.

    * @param vessel - Physical container or reactor used for the enzymatic reaction.
    * @param mixing - Mixing system and parameters employed during the reaction.
    * @param notes - Additional notes or comments about the vessel and mixing setup.
**/
export interface VesselAndMixing extends JsonLd {
  vessel: Vessel;
  mixing?: Mixing | null;
  notes?: string | null;
}

export const VesselAndMixingCodec = D.lazy("VesselAndMixing", () => D.struct({
    vessel: VesselCodec,
    mixing: D.nullable(MixingCodec),
    notes: D.nullable(D.string),
}));


/**
    Physical container or reactor specification for enzymatic reactions.

    * @param vessel_type - Type of vessel or reactor configuration used for the reaction.
    * @param material - Material composition of the vessel (e.g., glass, plastic, stainless
             steel).
    * @param size - Volume or capacity of the vessel.
    * @param size_unit - Unit of measurement for the size.
    * @param geometry - Geometric shape and dimensions of the vessel.
    * @param closure - Sealing and closure system for the vessel.
    * @param supplier - Manufacturer or supplier of the vessel.
    * @param lot_number - Batch or lot number for traceability.
    * @param reactor_specifics - Additional reactor-specific configurations and features.
    * @param notes - Additional notes about the vessel specifications.
**/
export interface Vessel extends JsonLd {
  vessel_type: VesselType;
  material?: string | null;
  size?: number | null;
  size_unit?: string | null;
  geometry?: string | null;
  closure?: Closure | null;
  supplier?: string | null;
  lot_number?: string | null;
  reactor_specifics?: ReactorSpecifics | null;
  notes?: string | null;
}

export const VesselCodec = D.lazy("Vessel", () => D.struct({
    vessel_type: VesselTypeCodec,
    material: D.nullable(D.string),
    size: D.nullable(D.number),
    size_unit: D.nullable(D.string),
    geometry: D.nullable(D.string),
    closure: D.nullable(ClosureCodec),
    supplier: D.nullable(D.string),
    lot_number: D.nullable(D.string),
    reactor_specifics: D.nullable(ReactorSpecificsCodec),
    notes: D.nullable(D.string),
}));


/**
    Sealing and closure system for reaction vessels.

    * @param closure_type - Type of closure mechanism (e.g., screw cap, septum, crimp cap).
    * @param sealing_material - Material used for sealing (e.g., PTFE, silicone, rubber).
    * @param notes - Additional notes about the closure system.
**/
export interface Closure extends JsonLd {
  closure_type?: string | null;
  sealing_material?: string | null;
  notes?: string | null;
}

export const ClosureCodec = D.lazy("Closure", () => D.struct({
    closure_type: D.nullable(D.string),
    sealing_material: D.nullable(D.string),
    notes: D.nullable(D.string),
}));


/**
    Specialized reactor configurations and operational features.

    * @param gas_handling - Gas supply and handling system for the reactor.
    * @param tubing - Tubing specifications and connections used in the reactor setup.
    * @param catalyst_localisation - Method or system for localizing or immobilizing the catalyst within
             the reactor.
    * @param temperature_control - Temperature control and regulation system employed.
**/
export interface ReactorSpecifics extends JsonLd {
  gas_handling?: GasHandling | null;
  tubing?: string | null;
  catalyst_localisation?: string | null;
  temperature_control?: string | null;
}

export const ReactorSpecificsCodec = D.lazy("ReactorSpecifics", () => D.struct({
    gas_handling: D.nullable(GasHandlingCodec),
    tubing: D.nullable(D.string),
    catalyst_localisation: D.nullable(D.string),
    temperature_control: D.nullable(D.string),
}));


/**
    Gas supply and handling system for reactor operations.

    * @param gas_type - Type of gas used (e.g., nitrogen, oxygen, argon, air).
    * @param supply_method - Method of gas supply (e.g., continuous flow, headspace purging,
             bubbling).
    * @param supply_rate - Rate of gas supply or flow into the reactor.
**/
export interface GasHandling extends JsonLd {
  gas_type?: string | null;
  supply_method?: string | null;
  supply_rate?: number | null;
}

export const GasHandlingCodec = D.lazy("GasHandling", () => D.struct({
    gas_type: D.nullable(D.string),
    supply_method: D.nullable(D.string),
    supply_rate: D.nullable(D.number),
}));


/**
    Mixing system and parameters for ensuring proper mass transfer and
    reaction homogeneity.

    * @param mixing_type - Primary type of mixing employed in the reaction system.
    * @param shaking - Shaking-based mixing parameters and configuration.
    * @param mechanical - Mechanical stirring parameters and equipment specifications.
    * @param fluid - Fluid-driven mixing parameters for flow-based systems.
    * @param notes - Additional notes about the mixing strategy and implementation.
**/
export interface Mixing extends JsonLd {
  mixing_type: MixingType;
  shaking?: ShakingMixing | null;
  mechanical?: MechanicalMixing | null;
  fluid?: FluidImpelledMixing | null;
  notes?: string | null;
}

export const MixingCodec = D.lazy("Mixing", () => D.struct({
    mixing_type: MixingTypeCodec,
    shaking: D.nullable(ShakingMixingCodec),
    mechanical: D.nullable(MechanicalMixingCodec),
    fluid: D.nullable(FluidImpelledMixingCodec),
    notes: D.nullable(D.string),
}));


/**
    Parameters for shaking-based mixing systems.

    * @param shaking_type - Type of shaking motion (e.g., orbital, linear, reciprocal).
    * @param deflection - Amplitude or deflection distance of the shaking motion.
    * @param speed - Frequency or speed of the shaking motion.
    * @param vessel_position - Orientation or position of the vessel during shaking.
    * @param notes - Additional notes about the shaking mixing setup.
**/
export interface ShakingMixing extends JsonLd {
  shaking_type?: string | null;
  deflection?: number | null;
  speed?: number | null;
  vessel_position?: string | null;
  notes?: string | null;
}

export const ShakingMixingCodec = D.lazy("ShakingMixing", () => D.struct({
    shaking_type: D.nullable(D.string),
    deflection: D.nullable(D.number),
    speed: D.nullable(D.number),
    vessel_position: D.nullable(D.string),
    notes: D.nullable(D.string),
}));


/**
    Parameters for mechanical stirring and agitation systems.

    * @param stirring_type - Type of mechanical stirring (e.g., overhead, magnetic, impeller).
    * @param stirrer_material - Material composition of the stirrer or impeller.
    * @param supplier - Manufacturer or supplier of the stirring equipment.
    * @param number_of_stirrers - Number of stirrers or impellers used in the system.
    * @param stirrer_geometry - Geometric design and shape of the stirrer or impeller.
    * @param blade_pitch_angle - Angle of the stirrer blades relative to the horizontal plane.
    * @param blade_size - Dimensions or size of the stirrer blades.
    * @param stirrer_speed - Rotational speed of the stirrer or impeller.
    * @param height_above_base - Distance of the stirrer from the bottom of the vessel.
    * @param power_per_volume - Power input per unit volume of the reaction mixture.
    * @param stir_bar - Magnetic stir bar specifications for magnetic stirring systems.
    * @param notes - Additional notes about the mechanical mixing setup.
**/
export interface MechanicalMixing extends JsonLd {
  stirring_type?: string | null;
  stirrer_material?: string | null;
  supplier?: string | null;
  number_of_stirrers?: number | null;
  stirrer_geometry?: string | null;
  blade_pitch_angle?: number | null;
  blade_size?: number | null;
  stirrer_speed?: number | null;
  height_above_base?: number | null;
  power_per_volume?: number | null;
  stir_bar?: StirBar | null;
  notes?: string | null;
}

export const MechanicalMixingCodec = D.lazy("MechanicalMixing", () => D.struct({
    stirring_type: D.nullable(D.string),
    stirrer_material: D.nullable(D.string),
    supplier: D.nullable(D.string),
    number_of_stirrers: D.nullable(D.number),
    stirrer_geometry: D.nullable(D.string),
    blade_pitch_angle: D.nullable(D.number),
    blade_size: D.nullable(D.number),
    stirrer_speed: D.nullable(D.number),
    height_above_base: D.nullable(D.number),
    power_per_volume: D.nullable(D.number),
    stir_bar: D.nullable(StirBarCodec),
    notes: D.nullable(D.string),
}));


/**
    Magnetic stir bar specifications for magnetic stirring systems.

    * @param size - Length and diameter of the magnetic stir bar.
    * @param shape - Shape of the stir bar (e.g., cylindrical, octagonal, cross-shaped).
**/
export interface StirBar extends JsonLd {
  size?: number | null;
  shape?: string | null;
}

export const StirBarCodec = D.lazy("StirBar", () => D.struct({
    size: D.nullable(D.number),
    shape: D.nullable(D.string),
}));


/**
    Parameters for fluid-driven mixing in flow-based reactor systems.

    * @param phase_volume_description - Description of phase volumes and their distribution in the flow
             system.
    * @param residence_time - Average residence time of the fluid in the mixing zone.
    * @param reynolds_number - Reynolds number characterizing the flow regime and mixing intensity.
    * @param passive_mixing - Description of passive mixing elements or structures used.
    * @param active_mixer - Description of active mixing devices or mechanisms employed.
    * @param pulsing - Pulsing or oscillatory flow patterns used to enhance mixing.
    * @param notes - Additional notes about the fluid-impelled mixing system.
**/
export interface FluidImpelledMixing extends JsonLd {
  phase_volume_description?: string | null;
  residence_time?: number | null;
  reynolds_number?: string | null;
  passive_mixing?: string | null;
  active_mixer?: string | null;
  pulsing?: string | null;
  notes?: string | null;
}

export const FluidImpelledMixingCodec = D.lazy("FluidImpelledMixing", () => D.struct({
    phase_volume_description: D.nullable(D.string),
    residence_time: D.nullable(D.number),
    reynolds_number: D.nullable(D.string),
    passive_mixing: D.nullable(D.string),
    active_mixer: D.nullable(D.string),
    pulsing: D.nullable(D.string),
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


// Vessels and Mixing Specification Enum definitions
export enum VesselType {
  OTHER = 'other',
  PLATE = 'plate',
  STIRRED_TANK = 'stirred_tank',
  TUBULAR_FLOW = 'tubular_flow',
  VIAL = 'vial',
}

export const VesselTypeCodec = D.union(
  D.literal(VesselType.OTHER),
  D.literal(VesselType.PLATE),
  D.literal(VesselType.STIRRED_TANK),
  D.literal(VesselType.TUBULAR_FLOW),
  D.literal(VesselType.VIAL),
);

export enum MixingType {
  COMBINED = 'combined',
  FLUID_IMPELLED = 'fluid_impelled',
  MECHANICAL = 'mechanical',
  NONE = 'none',
  SHAKING = 'shaking',
}

export const MixingTypeCodec = D.union(
  D.literal(MixingType.COMBINED),
  D.literal(MixingType.FLUID_IMPELLED),
  D.literal(MixingType.MECHANICAL),
  D.literal(MixingType.NONE),
  D.literal(MixingType.SHAKING),
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