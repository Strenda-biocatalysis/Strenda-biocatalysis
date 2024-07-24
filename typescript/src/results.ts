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

// Results documentation Type definitions
/**
    These parameters serve as benchmarks for understanding enzyme
    kinetics. The Km and kcat value is determined by all substrates
    involved in the reaction and not just one. Therefore, the
    concentrations of all substrates must be varied and the Km
    and kcat values calculated to obtain a common value instead of
    apparent values. For a comprehensive report around the technical
    key data of the kinetic parameters, see literature for further
    information, e.g. Pesci _et al._1, Bisswanger 2 .

    * @param michaelis_constant - The Michaelis-Menten constant (Km​) represents the substrate
             concentration at which an enzyme achieves half of its
             maximum reaction rate.
    * @param michaelis_constant_unit - The unit of the Michaelis-Menten constant (Km​) is typically expressed
             as moles per liter (M or mM).
    * @param maximum_reaction_rate - Vmax, the maximum reaction rate, represents the speed at which an
             enzyme-catalyzed reaction reaches saturation, indicating
             the maximum achievable rate of product formation under
             optimal substrate concentration (where enzymes are
             predominantly saturated with substrates).
    * @param maximum_reaction_rate_unit - The unit of Vmax (maximum reaction rate) is typically represented
             as concentration per time, such as moles per liter per
             second (mol/L/s or mM/s).
    * @param turnover_number - The turnover number (kcat) measures the number of substrate molecules
             converted to product per active site of an enzyme
             per unit time when the enzyme is fully saturated with
             substrate.
    * @param turnover_number_unit - The unit of turnover number (kcat) is typically expressed as moles
             of product per mole of enzyme per second or per minute
             (time-1).
    * @param catalytic_efficiency - Catalytic efficiency (kcat/Km) is a measure of how effectively an
             enzyme converts substrate into product, often quantified
             as the ratio of the turnover number (kcat) to the
             Michaelis-Menten constant (Km).
    * @param catalytic_efficiency_unit - The typical unit for catalytic efficiency (kcat/Km) is M-1s-1.
    * @param dissociation_constant - The dissociation constant (Kd) is a measure that represents the
             equilibrium between a complex and its dissociated
             components.
    * @param dissociation_constant_unit - The dissociation constant (Kd) is typically expressed in M (mol per
             liter) or its derivatives, such as nM (nanomoles per
             liter).
    * @param inhibition_type - Enzyme inhibition encompasses various forms, including competitive,
             non-competitive, uncompetitive, mixed, and irreversible
             inhibition. Each type has different effects on the
             enzyme's function and plays a crucial role in regulating
             biochemical processes.
    * @param inhibition_constant - The inhibition constant (Ki) describes the affinity of an inhibitor
             for an enzyme. It indicates how effectively an inhibitor
             influences enzyme activity. A lower Ki value suggests a
             strong binding of the inhibitor to the enzyme.
    * @param inhibition_constant_unit - The units for the inhibition constant (Ki) are commonly expressed in M
             (mol per liter) or related units.
    * @param hill_coefficient - The Hill coefficient is a parameter used to describe cooperativity
             in the binding of molecules to proteins. It is employed
             in enzyme reactions, e.g. oxygen binding to hemoglobin,
             to indicate whether there is positive (cooperative) or
             negative (anticooperative) binding. A Hill coefficient
             greater than 1 indicates positive cooperativity, while
             a value less than 1 indicates negative cooperativity. A
             value of exactly 1 indicates no cooperativity.
    * @param enzyme_stability - The stability of enzymes is often characterized by various parameters
             such as the enzyme's half-life under specific conditions,
             the decline in activity over time, or the preservation
             of catalytic activity under different environmental
             conditions.
    * @param special_treatment - If there are any other specific metrics, parameters, characteristics
             or aspects related to the kinetics that are important
             to document the results accurately and are not described
             by the aforementioned metadata, they should be explained
             here.
**/
export interface KineticParameters extends JsonLd {
  michaelis_constant: number;
  michaelis_constant_unit: string;
  maximum_reaction_rate: number;
  maximum_reaction_rate_unit: string;
  turnover_number: number;
  turnover_number_unit: string;
  catalytic_efficiency: number;
  catalytic_efficiency_unit: string;
  dissociation_constant: number;
  dissociation_constant_unit: string;
  inhibition_type: string;
  inhibition_constant: number;
  inhibition_constant_unit: string;
  hill_coefficient: number;
  enzyme_stability: string;
  special_treatment: string;
}

export const KineticParametersCodec = D.lazy("KineticParameters", () => D.struct({
    michaelis_constant: D.number,
    michaelis_constant_unit: D.string,
    maximum_reaction_rate: D.number,
    maximum_reaction_rate_unit: D.string,
    turnover_number: D.number,
    turnover_number_unit: D.string,
    catalytic_efficiency: D.number,
    catalytic_efficiency_unit: D.string,
    dissociation_constant: D.number,
    dissociation_constant_unit: D.string,
    inhibition_type: D.string,
    inhibition_constant: D.number,
    inhibition_constant_unit: D.string,
    hill_coefficient: D.number,
    enzyme_stability: D.string,
    special_treatment: D.string,
}));


/**
    These metrics are vital for evaluating the success of a process,
    optimizing reaction conditions, and ensuring the production
    of high-quality products in biocatalytic applications. For a
    comprehensive report around the technical key data of yield and
    conversion, see literature for further information, e.g. Lies
    _et al._3.

    * @param c_yield - Yield represents the amount of the desired product obtained from a
             reaction. It is the number of synthesized molecules of
             product per number of starting molecules. The following
             formula can be used:
    * @param yield_unit - The yield is typically expressed in percentages (%), reflecting
             the ratio of the actual obtained product quantity to
             the theoretical maximum product quantity that could be
             obtained under ideal conditions.
    * @param space_time_yield - Space-time yield in biocatalysis refers to the mass of product
             obtained per unit volume of the reactor per unit time.
             Other terms commonly used in the literature are
    * @param space_time_yield_unit - Space-time yield is commonly expressed in g/L/h (grams per liter per
             hour) or mol/L/h (moles per liter per hour).
    * @param conversion - The term "conversion" refers to the percentage of substrate that
             undergoes transformation into the desired product during
             a reaction. It is the number of converted molecules per
             number of starting molecules. The following formula can
             be used:
    * @param conversion_unit - The conversion is commonly expressed as a percentage (%) to indicate
             the proportion of substrate converted to the desired
             product during a specific reaction.
    * @param special_treatment - If there are any other specific metrics, parameters, characteristics
             or aspects related to the conversion or yield that are
             important to document the results accurately and are not
             described by the aforementioned attributes, they should
             be explained here.
**/
export interface YieldAndConversion extends JsonLd {
  c_yield: number;
  yield_unit: string;
  space_time_yield: number;
  space_time_yield_unit: string;
  conversion: number;
  conversion_unit: string;
  special_treatment: string;
}

export const YieldAndConversionCodec = D.lazy("YieldAndConversion", () => D.struct({
    c_yield: D.number,
    yield_unit: D.string,
    space_time_yield: D.number,
    space_time_yield_unit: D.string,
    conversion: D.number,
    conversion_unit: D.string,
    special_treatment: D.string,
}));


/**
    * @param specific_activity - The specific activity refers to the amount of product formed or
             substrate consumed per unit of enzyme per unit of time.
    * @param specific_activity_unit - The specific activity is typically expressed in µmol/min/mg
             (micromoles per minute per milligram of protein).
    * @param initial_reaction_rate - The initial reaction rate refers to the rate at which the product is
             formed in the first 10% of the enzymatic reaction under
             specific initial substrate concentrations and reaction
             conditions.
    * @param initial_reaction_rate_unit - Typically, the initial reaction rate is expressed as mol/L/min (moles
             per liter per minute) or µmol/mL/min (micromoles per
             milliliter per minute).
    * @param special_treatment - If there are any other specific metrics, parameters, characteristics
             or aspects related to the activity or initial reaction
             rate that are important to document the results
             accurately and are not described by the aforementioned
             attributes, they should be explained here.
**/
export interface ActivityAndInitialReactionRate extends JsonLd {
  specific_activity: number;
  specific_activity_unit: string;
  initial_reaction_rate: number;
  initial_reaction_rate_unit: string;
  special_treatment: string;
}

export const ActivityAndInitialReactionRateCodec = D.lazy("ActivityAndInitialReactionRate", () => D.struct({
    specific_activity: D.number,
    specific_activity_unit: D.string,
    initial_reaction_rate: D.number,
    initial_reaction_rate_unit: D.string,
    special_treatment: D.string,
}));


/**
    These parameters directly assess a catalyst's precision in converting
    specific substrates to desired products. For a comprehensive
    report around the technical key data of the selectivity and
    specificity, see literature for further information, e.g. Faber4,
    Liese _et al._3, Schurig5.

    * @param stereoselectivity - Stereoselectivity refers to the preference of a chemical reaction to
             produce a specific stereoisomer or a particular spatial
             arrangement of atoms within a molecule. It describes
             the ability of a reaction to favor the formation of
             one stereoisomer over others or to create a specific
             stereochemical outcome.
    * @param enantioselectivity - Enantioselectivity, or enantiomeric ratio (E), defines the enzyme's
             capability to preferentially catalyze the transformation
             of one enantiomer over its mirror-image counterpart. This
             trait highlights the enzyme's ability to favor a specific
             enantiomer either as a product or as the preferred
             substrate for a reaction.
    * @param enantiomeric_excess - The enantiomeric excess (
    * @param enantiomeric_excess_unit - The primary unit used for enantiomeric excess (
    * @param diastereomeric_excess - The diasteriomeric excess (
    * @param diasteriomeric_excess_unit - The primary unit used for diasteriomeric excess (
    * @param isomeric_content - The isomeric content (
    * @param isomeric_content_unit - The primary unit used for isomeric content (
    * @param chemoselectivity - Chemoselectivity refers to the ability of a chemical reaction to
             target a specific functional group or site within a
             molecule without affecting other reactive groups present.
             It highlights the preference of a reaction for one type
             of chemical bond or functional group over others in
             a molecule.
    * @param regioselectivity - Regioselectivity refers to the preference of a reaction to occur at
             a specific site within a molecule or compound that has
             multiple potential reaction sites. It describes the
             tendency of a reaction to selectively take place at a
             particular position of the molecule, considering its
             structural arrangement of atoms or functional groups,
             rather than at other possible sites.
    * @param special_treatment - If there are any other specific metrics, parameters, characteristics
             or aspects related to the selectivity and specificity
             that are important to document the results accurately and
             are not described by the aforementioned attributes, they
             should be explained here.
**/
export interface SelectivityAndSpecificity extends JsonLd {
  stereoselectivity: string;
  enantioselectivity: number;
  enantiomeric_excess: number;
  enantiomeric_excess_unit: string;
  diastereomeric_excess: number;
  diasteriomeric_excess_unit: string;
  isomeric_content: number;
  isomeric_content_unit: string;
  chemoselectivity: string;
  regioselectivity: string;
  special_treatment: string;
}

export const SelectivityAndSpecificityCodec = D.lazy("SelectivityAndSpecificity", () => D.struct({
    stereoselectivity: D.string,
    enantioselectivity: D.number,
    enantiomeric_excess: D.number,
    enantiomeric_excess_unit: D.string,
    diastereomeric_excess: D.number,
    diasteriomeric_excess_unit: D.string,
    isomeric_content: D.number,
    isomeric_content_unit: D.string,
    chemoselectivity: D.string,
    regioselectivity: D.string,
    special_treatment: D.string,
}));


/**
    Understanding the energy dynamics and spontaneity of reactions through
    thermodynamic parameters is essential for efficient biocatalysis.
    For a comprehensive report around the technical key data of the
    kinetic parameters, see literature for further information, e.g.
    Heintz6.

    * @param gibbs_free_energy_change - The Gibbs free energy (
    * @param enthalpy_change - The enthalpy (
    * @param special_treatment - If there are any other specific metrics, parameters, characteristics
             or aspects related to the thermodynamic parameters that
             are important to document the results accurately and
             are not described by the aforementioned attributes, they
             should be explained here.
**/
export interface ThermodynamicParameters extends JsonLd {
  gibbs_free_energy_change: string;
  enthalpy_change: string;
  special_treatment: string;
}

export const ThermodynamicParametersCodec = D.lazy("ThermodynamicParameters", () => D.struct({
    gibbs_free_energy_change: D.string,
    enthalpy_change: D.string,
    special_treatment: D.string,
}));