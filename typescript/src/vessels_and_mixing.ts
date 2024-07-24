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

// Vessels and mixing Type definitions
/**
    Vials are sealable containers available in various sizes and
    materials, playing a crucial role in sample storage and handling,
    as well as serving as reaction vessels.Plate

    * @param vial_size - The vial's size, which can be its volume or its dimensions.
    * @param vial_size_unit - For describing the vial size, you can use mL (milliliters) as the
             unit when referring to volume or cm (centimeters) when
             referring to dimensions.
    * @param vial_material - Specify the material of the vial, such as glass or plastic, as it can
             influence the reaction.
    * @param closure_type - Indicate the type of closure or stopper used for the vial, as it
             affects sealing and the course of the reaction. If no
             closure or seal was used for the vial, this should be
             noted as well.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the vial or its preparation for the
             reaction that are important for reproducibility and are
             not described by the aforementioned metadata, they should
             be explained here.
**/
export interface Vial extends JsonLd {
  vial_size: number;
  vial_size_unit: string;
  vial_material: string;
  closure_type: string;
  special_treatment: string;
}

export const VialCodec = D.lazy("Vial", () => D.struct({
    vial_size: D.number,
    vial_size_unit: D.string,
    vial_material: D.string,
    closure_type: D.string,
    special_treatment: D.string,
}));


/**
    It's crucial to provide detailed information about the plate type,
    material, well configuration, and other relevant specifications
    to ensure reproducibility and accuracy of the experimental
    setup.Stirred Tank Reactor

    * @param plate_type - The type of plate, such as microtiter plate, deep-well plate, or
             others.
    * @param plate_material - The material from which the plate is made, such as plastic
             (polystyrene), glass, or metal.
    * @param number_of_wells - The total number of wells or cavities in the plate.
    * @param well_shape
    * @param well_volume - The volume of each well is, usually expressed in µL (microliters).
    * @param well_arrangement - The arrangement of the wells in the plate, for example, in rows and
             columns.
    * @param supplier - Information about the supplier from which the plate was purchased.
    * @param lot_number - The lot number, also known as a batch number or code, is a unique
             identifier assigned to a specific batch of a product.
             This makes it possible to check or track information
             on production.
    * @param sealing_method - Indicate if the wells were sealed with a sealing film or lid. (
    * @param sealing_material - The material of the sealing film or lid. (
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the plate or its preparation for
             the reaction that are important for reproducibility and
             are not described by the aforementioned metadata, they
             should be explained here.
**/
export interface Plate extends JsonLd {
  plate_type: string;
  plate_material: string;
  number_of_wells: string;
  well_shape: string;
  well_volume: string;
  well_arrangement: string;
  supplier: string;
  lot_number: number;
  sealing_method: string;
  sealing_material: string;
  special_treatment: string;
}

export const PlateCodec = D.lazy("Plate", () => D.struct({
    plate_type: D.string,
    plate_material: D.string,
    number_of_wells: D.string,
    well_shape: D.string,
    well_volume: D.string,
    well_arrangement: D.string,
    supplier: D.string,
    lot_number: D.number,
    sealing_method: D.string,
    sealing_material: D.string,
    special_treatment: D.string,
}));


/**
    Stirred Tank Reactors (STRs) are frequently employed as versatile
    and controlled vessels, allowing for precise regulation of key
    parameters like temperature, pH, and stirring speed. All relevant
    specifications or attributes need to be described.Tubular flow/
    continuous reactor

    * @param type - There are several types of Stirred Tank Reactors, differing in design
             and intended use. A detailed description is required.
    * @param material - Material the reactor is made of, e.g. glass, polypropylene etc.
    * @param volume - Indicate the total volume capacity of the Stirred Tank Reactor.
    * @param volume_unit - The volume is typically expressed in L (liters).
    * @param geometry - The geometry of the reactor, in particular of interest is the ratio of
             height to width.
    * @param bottom_type - Shape of the bottom of the reactor, e.g. a round bottom or a flat
             bottom.
    * @param gas_consumption - Common gases that are supplied to the reactor include, e.g., air,
             oxygen, hydrogen, etc.
    * @param gas_supply - Gas can be supplied to a Stirred Tank Reactor in various ways, such
             as through sparging using a tube or an aeration basket,
             bubbling, or direct injection into the reactor vessel.
    * @param gas_supply_rate - Specification of the gas supply rate.
    * @param gas_supply_rate_unit - The units for the gas supply rate in a Stirred Tank Reactor can be L/
             min (liters per minute), m³/h (cubic meters per hour), or
             other volume units per unit of time.
    * @param temperature_control - The temperature in a Stirred Tank Reactor can be controlled through
             various methods, typically using external heat sources or
             cooling systems such as heating jackets, cooling coils,
             or external temperature control units.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the Stirred Tank Reactor or
             its preparation for the reaction that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface StirredTankReactor extends JsonLd {
  type: string;
  material: string;
  volume: number;
  volume_unit: string;
  geometry: string;
  bottom_type: string;
  gas_consumption: string;
  gas_supply: string;
  gas_supply_rate: number;
  gas_supply_rate_unit: string;
  temperature_control: string;
  special_treatment: string;
}

export const StirredTankReactorCodec = D.lazy("StirredTankReactor", () => D.struct({
    type: D.string,
    material: D.string,
    volume: D.number,
    volume_unit: D.string,
    geometry: D.string,
    bottom_type: D.string,
    gas_consumption: D.string,
    gas_supply: D.string,
    gas_supply_rate: D.number,
    gas_supply_rate_unit: D.string,
    temperature_control: D.string,
    special_treatment: D.string,
}));


/**
    When conducting enzymatic reactions in tubular flow or continuous
    reactors, it is essential to provide detailed information
    about the reactor setup, e.g. plug flow reactor, and operating
    conditions to ensure reproducibility and transparency in reporting
    the experimental process.

    * @param volume - Indicate the total volume capacity of the tubular flow/continuous
             reactor.
    * @param volume_unit - The volume is typically expressed in L (liters).
    * @param geometry - The exact geometry of the tubular flow/continuous reactor.
    * @param reactor_type - There are several types of tubular flow/continuous reactors, e.g.
             packed bed reactor, or a plug flow reactor, differing
             in design and intended use. A detailed description is
             required.
    * @param material - Material the reactor is made of, e.g. glass, stainless steel or other
             materials.
    * @param tubing - When using tubing in a tubular flow/continuous reactor, various pieces
             of information can be provided, such as tubing material,
             diameter, length, connections, etc.
    * @param localisation_of_the_catalyst - Specify the exact location of the catalyst in the tubular flow/
             continuous reactor. The biocatalyst is typically present
             in the liquid phase or immobilized on a support matrix
             (such as particles or membranes).
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the tubular flow/continuous reactor
             or its preparation for the reaction that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface TubularFlowContinuousReactor extends JsonLd {
  volume: number;
  volume_unit: string;
  geometry: string;
  reactor_type: string;
  material: string;
  tubing: string;
  localisation_of_the_catalyst: string;
  special_treatment: string;
}

export const TubularFlowContinuousReactorCodec = D.lazy("TubularFlowContinuousReactor", () => D.struct({
    volume: D.number,
    volume_unit: D.string,
    geometry: D.string,
    reactor_type: D.string,
    material: D.string,
    tubing: D.string,
    localisation_of_the_catalyst: D.string,
    special_treatment: D.string,
}));


/**
    Shaking is an essential method for ensuring uniform mixing and,
    consequently, recording relevant metadata is crucial for
    maintaining consistent reaction conditions.Mechanically impelled
    mixing (stirring)

    * @param shaking_type - The type of shaking used to mix the reaction (e.g., horizontal,
             vertical, back-and-forth or circulatory).
    * @param deflection - Information about the extent of deflection or bending of the agitator
             from its original position of the horizontal shaking
             system.
    * @param deflection_unit - Units such as mm (millimeters) or μm (micrometers) could be used to
             describe deflection in relation to the movement of the
             shaking system.
    * @param speed - Specify the speed or frequency at which the shaking was conducted.
    * @param speed_unit - The shaking speed or frequency could be expressed in units such as rpm
             (rounds per minute) or Hz (cycles per second).
    * @param position - Information regarding the orientation of the vessel in the shaking
             system relative to deflection.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the shaking that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface Shaking extends JsonLd {
  shaking_type: string;
  deflection: number;
  deflection_unit: string;
  speed: number;
  speed_unit: string;
  position: string;
  special_treatment: string;
}

export const ShakingCodec = D.lazy("Shaking", () => D.struct({
    shaking_type: D.string,
    deflection: D.number,
    deflection_unit: D.string,
    speed: D.number,
    speed_unit: D.string,
    position: D.string,
    special_treatment: D.string,
}));


/**
    When utilizing mechanically impelled mixing in enzymatic reactions,
    it is essential to provide information about the mixing method and
    related parameters.Liquid or gas impelled mixing

    * @param stirring_type - There are several types of stirring methods used in laboratory and
             industrial settings, including magnetic stirring (from
             vessel bottom), mechanical stirring, overhead stirring
             and other methods.
    * @param stirrer_material - The specific composition or nature of the material should be
             indicated, e.g. whether it is made of magnetic material,
             a PTFE (polytetrafluoroethylene) coating, stainless steel
             or other relevant features that determine its structural
             or functional properties within the experimental setup.
    * @param supplier - If available, details of the specific designation or manufacturer's
             name of the stirrer should be provided for precise
             identification.
    * @param number_of_stirrers - The number of stirrers available in the system.
    * @param distance_between_stirrers - Information about the distance, spacing or separation between the
             stirring rods or impellers within a reaction vessel or
             container.
    * @param distance_between_stirrers_unit - The distance between stirrers can be specified in mm (millimeters), cm
             (centimeters), or m (meters), depending on the size and
             scale of the stirring system.
    * @param stirrer_blade_pitch_angle - The pitch angle at which the blades or paddles of a stirring mechanism
             are positioned relative to the plane of rotation. It's
             typically expressed in ° (degrees).
    * @param number_of_stirrer_blades - The number of blades on each stirrer.
    * @param stirrer_blade_size - The size of the impeller blades in a stirred tank reactor.
    * @param stirrer_blade_size_unit - In the case of impellers in a stirred tank reactor, the diameter of
             the impeller blades is typically specified. This diameter
             can be measured in millimeters (mm) or centimeters (cm).
    * @param stirrer_geometry - There are various morphologies or geometries, such as radial
             impellers, axial impellers, helical ribbon impellers,
             paddle impellers, and more, depending on its design and
             intended purpose.
    * @param stirrer_speed - Specify the speed or frequency at which the stirring was conducted.
    * @param speed_unit - The unit for stirring speed can be expressed in RPM (revolutions
             per minute), Hz (Hertz), or rad/s (radians per second),
             depending on the measurement instruments and scientific
             conventions used.
    * @param height_of_stirrer_above_vessel_base - The vertical distance between the bottom of the vessel or container
             (where the reaction takes place) and the lowest point of
             the stirring element or stirrer, which is usually located
             just above the vessel base.
    * @param height_of_stirrer_above_vessel_base_unit - Common units for defining the vertical distance between the bottom of
             the vessel and the lowest point of the stirrer include:
             mm (millimeters), cm (centimeters) and m (meters).
    * @param power_per_volume - The amount of stirring power or energy input into a system per unit
             volume.
    * @param power_per_volume_unit - The units commonly used for expressing the stirring power are W/L
             (watts per liter) or kW/m³ (kilowatts per cubic meter).
    * @param stir_bar_size
    * @param stir_bar_size_unit
    * @param stir_bar_shape - The shape or configuration of the stir bar, whether it's cylindrical,
             octagonal, oval, or another shape. Different shapes
             can interact with the reaction mixture differently,
             influencing mixing patterns and efficiency.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the mechanically impelled mixing
             (stirring) that are important for reproducibility and are
             not described by the aforementioned metadata, they should
             be explained here.
**/
export interface MechanicallyImpelledMixing extends JsonLd {
  stirring_type: string;
  stirrer_material: string;
  supplier: string;
  number_of_stirrers: number;
  distance_between_stirrers: number;
  distance_between_stirrers_unit: string;
  stirrer_blade_pitch_angle: number;
  number_of_stirrer_blades: number;
  stirrer_blade_size: number;
  stirrer_blade_size_unit: string;
  stirrer_geometry: string;
  stirrer_speed: number;
  speed_unit: string;
  height_of_stirrer_above_vessel_base: number;
  height_of_stirrer_above_vessel_base_unit: string;
  power_per_volume: number;
  power_per_volume_unit: string;
  stir_bar_size: number;
  stir_bar_size_unit: number;
  stir_bar_shape: string;
  special_treatment: string;
}

export const MechanicallyImpelledMixingCodec = D.lazy("MechanicallyImpelledMixing", () => D.struct({
    stirring_type: D.string,
    stirrer_material: D.string,
    supplier: D.string,
    number_of_stirrers: D.number,
    distance_between_stirrers: D.number,
    distance_between_stirrers_unit: D.string,
    stirrer_blade_pitch_angle: D.number,
    number_of_stirrer_blades: D.number,
    stirrer_blade_size: D.number,
    stirrer_blade_size_unit: D.string,
    stirrer_geometry: D.string,
    stirrer_speed: D.number,
    speed_unit: D.string,
    height_of_stirrer_above_vessel_base: D.number,
    height_of_stirrer_above_vessel_base_unit: D.string,
    power_per_volume: D.number,
    power_per_volume_unit: D.string,
    stir_bar_size: D.number,
    stir_bar_size_unit: D.number,
    stir_bar_shape: D.string,
    special_treatment: D.string,
}));


/**
    Detailed information about the mixing mode used, whether it involves
    liquid or gas impelled mixing, is essential for ensuring the
    reproducibility and understanding of enzymatic reactions.

    * @param volume_of_liquid_solid_phase - In the context of enzymatic reactions or any chemical processes
             involving heterogeneous mixtures like a liquid and solid
             phase, essential parameters for describing the system
             involve the composition of the phases, the percentage or
             fraction of the total volume occupied by the liquid-solid
             phase mixture, and further information.
    * @param residence_time - The residence time, often denoted as "τ" (tau), refers to the average
             amount of time a substance or component spends inside a
             specific system or reactor and is to be specified.
    * @param residence_time_unit - The units for residence time can vary depending on the system and the
             units used for volume and flow rate. Common units include
             s (seconds), min (minutes), h (hours), or any time-
             related units.
    * @param reynolds_number - The Reynolds number (Re) is a dimensionless quantity used in fluid
             dynamics to predict the flow regime of a fluid within a
             specific system. It helps to determine whether the flow
             is laminar, turbulent, or somewhere in between.
    * @param passive_mixing - The design of the coils and the flow patterns created by the geometry
             of the tubing can lead to passive mixing as the fluid
             flows through the reactor without the need for external
             agitation. More detailed information must be provided to
             describe the process.
    * @param active_T_or_Y_mixer - Key features for describing an active Y or T mixer can include inlet
             ports, mixer chamber, outlet port, control, materials
             amon others.
    * @param pulsing - The pulsing process involves periodically injecting or introducing
             specific components, such as reactants or additives, into
             a reaction system at regular intervals or in a pulsatile
             manner. More detailed information must be provided to
             describe the process.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the liquid or gas impelled mixing
             that are important for reproducibility and are not
             described by the aforementioned metadata, they should be
             explained here.
**/
export interface LiquidOrGasImpelledMixing extends JsonLd {
  volume_of_liquid_solid_phase: string;
  residence_time: number;
  residence_time_unit: string;
  reynolds_number: string;
  passive_mixing: string;
  active_T_or_Y_mixer: string;
  pulsing: string;
  special_treatment: string;
}

export const LiquidOrGasImpelledMixingCodec = D.lazy("LiquidOrGasImpelledMixing", () => D.struct({
    volume_of_liquid_solid_phase: D.string,
    residence_time: D.number,
    residence_time_unit: D.string,
    reynolds_number: D.string,
    passive_mixing: D.string,
    active_T_or_Y_mixer: D.string,
    pulsing: D.string,
    special_treatment: D.string,
}));