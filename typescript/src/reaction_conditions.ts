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

// Reaction conditions Type definitions
/**
    To describe a monoliquid system, precise information about the solvent
    (mixture) used and the applied reaction system must be provided.

    * @param solvent_description - The solvent used in the reaction system, e.g. a buffered aqueous
             solution or an organic solvent.
    * @param ionic_strength - Ionic strength calculated according to the dissolved ions in the
             solvent. The following formula can be used: $$I =
             \frac{1}{2} \sum
    * @param ionic_strength_unit - The unit of ionic strength is usually expressed in mol/L (moles per
             liter), or in mmol/L (millimoles per liter). (
    * @param further_additives - Further additive like cosolvents used to increase solubility of
             components, e.g. DMSO.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the monoliquid system that are
             important for reproducibility and are not described by
             the aforementioned metadata, they should be explained
             here.
**/
export interface MonoliquidSystemDescription_WMRS extends JsonLd {
  solvent_description: string;
  ionic_strength: number;
  ionic_strength_unit: string;
  further_additives: string;
  special_treatment: string;
}

export const MonoliquidSystemDescription_WMRSCodec = D.lazy("MonoliquidSystemDescription_WMRS", () => D.struct({
    solvent_description: D.string,
    ionic_strength: D.number,
    ionic_strength_unit: D.string,
    further_additives: D.string,
    special_treatment: D.string,
}));


/**
    To describe a multiphasic system, precise information about the phases
    used and the applied system must be provided.

    * @param phases_number - Number of phases present in the system, if there is an aqueous and a
             gas phase present, the number is 2.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the multiphasic system that are
             important for reproducibility and are not described by
             the aforementioned metadata, they should be explained
             here.
**/
export interface MultiphasicSystemDescription_WMRS extends JsonLd {
  phases_number: number;
  special_treatment: string;
}

export const MultiphasicSystemDescription_WMRSCodec = D.lazy("MultiphasicSystemDescription_WMRS", () => D.struct({
    phases_number: D.number,
    special_treatment: D.string,
}));


/**
    If more then one liquid phase exists the metadata has to be recorded
    according to the number of liquid phases.Solid phase

    * @param liquid_type - Information about the type of liquid used, whether it is an organic
             solvent,an aqueous buffer or are mixture of both.
    * @param liquid_amount - Amount of the liquid added to the reaction.
    * @param liquid_unit - In case of aqueous liquids, mL (milliliter) is often used as unit, in
             case of organic solvents, volume percentage (Vol %) or
             volume fraction (Vol/Vol) is utilized.
**/
export interface LiquidPhase_WMRS extends JsonLd {
  liquid_type: string;
  liquid_amount: number;
  liquid_unit: string;
}

export const LiquidPhase_WMRSCodec = D.lazy("LiquidPhase_WMRS", () => D.struct({
    liquid_type: D.string,
    liquid_amount: D.number,
    liquid_unit: D.string,
}));


/**
    Definition of the solid phase used in the reaction.Gas phase

    * @param solid_type - Information about the type of solid used, whether it is a support
             material, solid catalyst, or any other solid compound.
    * @param solid_amount - Mass of the solid compound used in the reaction solution.
    * @param solid_unit - In the case of a solid compound, common units like grams, milligrams,
             or micrograms can be used.
**/
export interface SolidPhase_WMRS extends JsonLd {
  solid_type: string;
  solid_amount: number;
  solid_unit: string;
}

export const SolidPhase_WMRSCodec = D.lazy("SolidPhase_WMRS", () => D.struct({
    solid_type: D.string,
    solid_amount: D.number,
    solid_unit: D.string,
}));


/**
    Definition of the gas phase used in the reaction. If a gas mixture is
    involved, this must be taken into account.

    * @param gas_type - Information about the type of gas used, whether it is nitrogen, carbon
             dioxide, argon, oxygen or other gases.
    * @param gas_amount - Concentration of the gas in the gas phase.
    * @param gas_unit - In the case of gases, common units are volume percentage (Vol %),
             volume fraction (Vol/Vol), mole percentage (Mol %) or
             molar fraction (Mol/Mol).
**/
export interface GasPhase_WMRS extends JsonLd {
  gas_type: string;
  gas_amount: number;
  gas_unit: string;
}

export const GasPhase_WMRSCodec = D.lazy("GasPhase_WMRS", () => D.struct({
    gas_type: D.string,
    gas_amount: D.number,
    gas_unit: D.string,
}));


/**
    The temperature, if constant, must be clearly defined.Event-based
    temperature shift

    * @param temperature - Temperature during the reaction.
    * @param temperature_unit - The temperature can be specified in units such as K, °C, or °F.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the temperature that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface TemperatureConstant_WMRS extends JsonLd {
  temperature: number;
  temperature_unit: string;
  special_treatment: string;
}

export const TemperatureConstant_WMRSCodec = D.lazy("TemperatureConstant_WMRS", () => D.struct({
    temperature: D.number,
    temperature_unit: D.string,
    special_treatment: D.string,
}));


/**
    If the temperature is changed during the course of the reaction or
    there is an event-based change, this must be documented precisely.

    * @param temperature_unit - The temperature can be specified in units such as K, °C, or °F.
    * @param temperature_beginning - The initial temperature, prior to the start of the reaction, should
             be specified.
    * @param temperature_after_event - The temperature that is present after a specific event has occurred.
    * @param event_description - Information regarding the event that caused the temperature change.
             In the case of a fed-batch reaction protocol, this event
             can also be the planned adjustment of the temperature to
             another specific value based on the current progress of
             the reaction process.
    * @param temperature_at_XY - The temperature can also be measured at a variably chosen time point
    * @param time_at_XY - Specification of the exact time point
    * @param time_unit - Common units for specifying time can be s (seconds), min (minutes) or
             h (hours).
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the temperature that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface EventBasedTemperatureShift_WMRS extends JsonLd {
  temperature_unit: string;
  temperature_beginning: number;
  temperature_after_event: number;
  event_description: string;
  temperature_at_XY: number;
  time_at_XY: number;
  time_unit: string;
  special_treatment: string;
}

export const EventBasedTemperatureShift_WMRSCodec = D.lazy("EventBasedTemperatureShift_WMRS", () => D.struct({
    temperature_unit: D.string,
    temperature_beginning: D.number,
    temperature_after_event: D.number,
    event_description: D.string,
    temperature_at_XY: D.number,
    time_at_XY: D.number,
    time_unit: D.string,
    special_treatment: D.string,
}));


/**
    Information about the pH value in the system, if the pH is constant
    over the course of the reaction.Event-based pH shift

    * @param pH_value - Value of the pH.
    * @param detected_when - Specification of the timepoint at which the pH was measured. It
             includes whether the pH value was measured before,
             during, or after the reaction and whether all components
             of the reaction solution were already present or if some
             were added after the measurement.
    * @param detected_how - The pH value of a reaction can be determined in various ways, such as
             using a pH meter, pH paper, titration, electrochemical
             sensors, or other methods.
    * @param temperature - The temperature at the time of pH measurement.
    * @param temperature_unit - The temperature can be specified in units such as K, °C, or °F.
    * @param calibration_pH_electrode - Usually, a pH electrode is calibrated using standard buffers at 20-25
             °C. If the conditions in the reaction mixture differ from
             this, it should be specified. (
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the pH value that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface pHConstant_WMRS extends JsonLd {
  pH_value: number;
  detected_when: string;
  detected_how: string;
  temperature: number;
  temperature_unit: string;
  calibration_pH_electrode: string;
  special_treatment: string;
}

export const pHConstant_WMRSCodec = D.lazy("pHConstant_WMRS", () => D.struct({
    pH_value: D.number,
    detected_when: D.string,
    detected_how: D.string,
    temperature: D.number,
    temperature_unit: D.string,
    calibration_pH_electrode: D.string,
    special_treatment: D.string,
}));


/**
    If the pH is changed during the course of the reaction or there is an
    event-based change, this must be documented precisely. Depending
    on the buffer chosen, a temperature shift may also result in a
    pH shift.

    * @param pH_beginning - The initial pH, prior to the start of the reaction, should be
             specified.
    * @param pH_after_event - The pH that is present after a specific event has occurred.
    * @param event_description - Information regarding the event that caused the pH change. In the
             case of a fed-batch reaction protocol, this event can
             also be the planned adjustment of the pH value to another
             specific value based on the current progress of the
             reaction process.
    * @param pH_at_XY - The pH can also be measured at a variably chosen time point
    * @param time_at_XY - Specification of the exact time point
    * @param time_unit - Common units for specifying time can be s (seconds) or min (minutes).
    * @param detected_when - Specification whether all components of the reaction solution
             were already present or if some were added after the
             measurement at the timepoint of the pH measurement.
    * @param detected_how - The pH value of a reaction can be determined in various ways, such as
             using a pH meter, pH paper, titration, electrochemical
             sensors, or other methods.
    * @param temperature - The temperature at the time of pH measurement.
    * @param temperature_unit - The temperature can be specified in units such as K, °C, or °F.
    * @param calibration_pH_electrode - Usually, a pH electrode is calibrated using standard buffers at 20-25
             °C. If the conditions in the reaction mixture differ from
             this, it should be specified. (
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the pH value that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface EventBasedpHShift_WMRS extends JsonLd {
  pH_beginning: number;
  pH_after_event: number;
  event_description: string;
  pH_at_XY: number;
  time_at_XY: number;
  time_unit: string;
  detected_when: string;
  detected_how: string;
  temperature: number;
  temperature_unit: string;
  calibration_pH_electrode: string;
  special_treatment: string;
}

export const EventBasedpHShift_WMRSCodec = D.lazy("EventBasedpHShift_WMRS", () => D.struct({
    pH_beginning: D.number,
    pH_after_event: D.number,
    event_description: D.string,
    pH_at_XY: D.number,
    time_at_XY: D.number,
    time_unit: D.string,
    detected_when: D.string,
    detected_how: D.string,
    temperature: D.number,
    temperature_unit: D.string,
    calibration_pH_electrode: D.string,
    special_treatment: D.string,
}));


/**
    To describe a monoliquid system, precise information about the solvent
    used and the applied system must be provided.

    * @param solvent_description - The solvent used in the reaction system, e.g. a buffered aqueous
             solution or an organic solvent.
    * @param ionic_strength - Ionic strength calculated according to the dissolved ions in the
             solvent. The following formula can be used: $$I =
             \frac{1}{2} \sum
    * @param ionic_strength_unit - The unit of ionic strength is usually expressed in mol/L (moles per
             liter), or in mmol/L (millimoles per liter). (
    * @param further_additives - Further additive like cosolvents used to increase solubility of
             reactants, e.g. DMSO.
    * @param Flow_rate - The flow rate must be specified to determine how fast a liquid or gas
             is flowing through a reactor or system.
    * @param Flow_rate_unit - Common units for describing flow rate include L/min (liters per
             minute), mL/h (milliliters per hour), m³/h (cubic meters
             per hour), or other volume units per unit of time.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the monoliquid system that are
             important for reproducibility and are not described by
             the aforementioned metadata, they should be explained
             here.
**/
export interface MonoliquidSystemDescription_TFCR extends JsonLd {
  solvent_description: string;
  ionic_strength: number;
  ionic_strength_unit: string;
  further_additives: string;
  Flow_rate: number;
  Flow_rate_unit: string;
  special_treatment: string;
}

export const MonoliquidSystemDescription_TFCRCodec = D.lazy("MonoliquidSystemDescription_TFCR", () => D.struct({
    solvent_description: D.string,
    ionic_strength: D.number,
    ionic_strength_unit: D.string,
    further_additives: D.string,
    Flow_rate: D.number,
    Flow_rate_unit: D.string,
    special_treatment: D.string,
}));


/**
    To describe a multiphasic system, precise information about the phases
    used and the applied system must be provided.

    * @param phases_number - Number of phases present in the system, if there is an aqueous and a
             gas phase present, the number is 2.
    * @param Flow_rate - The flow rate must be specified to determine how fast a liquid or gas
             is flowing through a reactor or system.
    * @param Flow_rate_unit - Common units for describing flow rate include L/min (liters per
             minute), mL/h (milliliters per hour), m³/h (cubic meters
             per hour), or other volume units per unit of time.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the multiphasic system that are
             important for reproducibility and are not described by
             the aforementioned metadata, they should be explained
             here.
**/
export interface MultiphasicSystemDescription_TFCR extends JsonLd {
  phases_number: number;
  Flow_rate: number;
  Flow_rate_unit: string;
  special_treatment: string;
}

export const MultiphasicSystemDescription_TFCRCodec = D.lazy("MultiphasicSystemDescription_TFCR", () => D.struct({
    phases_number: D.number,
    Flow_rate: D.number,
    Flow_rate_unit: D.string,
    special_treatment: D.string,
}));


/**
    If more then one liquid phase exists the metadata has to be recorded
    according to the number of liquid phases.Solid phase

    * @param liquid_type - Information about the type of liquid used, whether it is an organic
             solvent, an aqueous buffer or a mixture of both.
    * @param liquid_amount - Amount of the liquid added to the reaction.
    * @param liquid_unit - In case of aqueous liquids, mL (milliliter) is often used as unit, in
             case of organic solvents, volume percentage (Vol %) or
             volume fraction (Vol/Vol) is utilized.
**/
export interface LiquidPhase_TFCR extends JsonLd {
  liquid_type: string;
  liquid_amount: number;
  liquid_unit: string;
}

export const LiquidPhase_TFCRCodec = D.lazy("LiquidPhase_TFCR", () => D.struct({
    liquid_type: D.string,
    liquid_amount: D.number,
    liquid_unit: D.string,
}));


/**
    Definition of the solid phase used in the reaction.Gas phase

    * @param solid_type - Information about the type of solid used, whether it is a support
             material, solid catalyst, or any other solid compound.
    * @param solid_amount - Mass of the solid used in the reaction solution.
    * @param solid_unit - In the case of solids, common units like grams, milligrams, or
             micrograms can be used.
**/
export interface SolidPhase_TFCR extends JsonLd {
  solid_type: string;
  solid_amount: number;
  solid_unit: string;
}

export const SolidPhase_TFCRCodec = D.lazy("SolidPhase_TFCR", () => D.struct({
    solid_type: D.string,
    solid_amount: D.number,
    solid_unit: D.string,
}));


/**
    Definition of the gas phase used in the reaction. If a gas mixture is
    involved, this must be taken into account.

    * @param gas_type - Information about the type of gas used, whether it's nitrogen dioxide,
             argon, oxygen or other gases.
    * @param gas_amount - Concentration of the gas in the gas phase.
    * @param gas_unit - In the case of gases, common units are volume percentage (Vol %),
             volume fraction (Vol/Vol), mole percentage (Mol %) or
             molar fraction (Mol/Mol).
**/
export interface GasPhase_TFCR extends JsonLd {
  gas_type: string;
  gas_amount: number;
  gas_unit: string;
}

export const GasPhase_TFCRCodec = D.lazy("GasPhase_TFCR", () => D.struct({
    gas_type: D.string,
    gas_amount: D.number,
    gas_unit: D.string,
}));


/**
    The temperature, if constant, must be clearly defined.Dynamic
    temperature

    * @param temperature - Temperature during the reaction.
    * @param temperature_unit - The temperature can be specified in units such as K, °C, or °F.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the temperature that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface TemperatureConstant_TFCR extends JsonLd {
  temperature: number;
  temperature_unit: string;
  special_treatment: string;
}

export const TemperatureConstant_TFCRCodec = D.lazy("TemperatureConstant_TFCR", () => D.struct({
    temperature: D.number,
    temperature_unit: D.string,
    special_treatment: D.string,
}));


/**
    If there is a temperature gradient or different temperatures are
    measured in the system, these must be described as well as
    possible.

    * @param temperature_beginning - The initial temperature, prior to the start of the reaction, should
             be specified.
    * @param temperature_after_event - The temperature that is present after a specific event has occurred.
    * @param event_description - Information regarding the event that caused the temperature change.
             In the case of a fed-batch reaction protocol, this event
             can also be the planned adjustment of the temperature to
             another specific value based on the current progress of
             the reaction process.
    * @param temperature_at_XY - The temperature can also be measured at a variably chosen time point
    * @param time_at_XY - Specification of the exact time point
    * @param time_unit - Common units for specifying time can be s (seconds), min (minutes)
             h (hours).
    * @param temperature_unit - The temperature can be specified in units such as K, °C, or °F.
    * @param temperature_gradient_beginning - The initial temperature from which the temperature gradient begins. (
    * @param temperature_gradient_end - The target temperature reached after the temperature gradient is
             applied. (
    * @param gradient_length - The distance or time span over which the temperature gradient is
             applied. (
    * @param gradient_length_unit - The gradient length can be specified either as the physical distance
             (e.g. in meters) or as the time span (e.g. in minutes). (
    * @param measurement_points - Information about the locations or time points where temperature
             measurements are taken to monitor the gradient. This
             can be important to ensure that the gradient behaves as
             intended. (
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the temperature profile that are
             important for reproducibility and are not described by
             the aforementioned metadata, they should be explained
             here.
**/
export interface DynamicTemperature_TFCR extends JsonLd {
  temperature_beginning: number;
  temperature_after_event: number;
  event_description: string;
  temperature_at_XY: number;
  time_at_XY: number;
  time_unit: string;
  temperature_unit: string;
  temperature_gradient_beginning: number;
  temperature_gradient_end: number;
  gradient_length: number;
  gradient_length_unit: string;
  measurement_points: string;
  special_treatment: string;
}

export const DynamicTemperature_TFCRCodec = D.lazy("DynamicTemperature_TFCR", () => D.struct({
    temperature_beginning: D.number,
    temperature_after_event: D.number,
    event_description: D.string,
    temperature_at_XY: D.number,
    time_at_XY: D.number,
    time_unit: D.string,
    temperature_unit: D.string,
    temperature_gradient_beginning: D.number,
    temperature_gradient_end: D.number,
    gradient_length: D.number,
    gradient_length_unit: D.string,
    measurement_points: D.string,
    special_treatment: D.string,
}));


/**
    Information about the pH value in the system, if the pH is constant
    over the course of the reaction.Dynamic pH

    * @param pH_value - The value of the pH.
    * @param detected_when - Specification of the timepoint at which the pH was measured. It
             includes whether the pH value was measured before,
             during, or after the reaction and whether all components
             of the reaction solution were already present or if some
             were added after the measurement.
    * @param detected_how - The pH value of a reaction can be determined in various ways, such as
             using a pH meter, pH paper, titration, electrochemical
             sensors, or other methods.
    * @param temperature - The temperature at the time of pH measurement.
    * @param temperature_unit - The temperature can be specified in units such as K, °C, or °F.
    * @param calibration_pH_electrode - Usually, a pH electrode is calibrated using standard buffers at 20-25
             °C. If the conditions in the reaction mixture differ from
             this, it should be specified. (
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the pH value that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface pHConstant_TFCR extends JsonLd {
  pH_value: number;
  detected_when: string;
  detected_how: string;
  temperature: number;
  temperature_unit: string;
  calibration_pH_electrode: string;
  special_treatment: string;
}

export const pHConstant_TFCRCodec = D.lazy("pHConstant_TFCR", () => D.struct({
    pH_value: D.number,
    detected_when: D.string,
    detected_how: D.string,
    temperature: D.number,
    temperature_unit: D.string,
    calibration_pH_electrode: D.string,
    special_treatment: D.string,
}));


/**
    If there is a pH gradient or different pHs are measured in the system,
    these must be described as detailed as possible. Depending on the
    buffer chosen, a temperature shift may also result in a pH shift.

    * @param pH_beginning - The initial pH, prior to the start of the reaction, should be
             specified.
    * @param pH_after_event - The pH that is present after a specific event has occurred.
    * @param event_description - Information regarding the event that caused the pH change. In the
             case of a fed-batch reaction protocol, this event can
             also be the planned adjustment of the pH value to another
             specific value based on the current progress of the
             reaction process.
    * @param pH_at_XY - The pH can also be measured at a variably chosen time point
    * @param time_at_XY - Specification of the exact time point
    * @param time_unit - Common units for specifying time can be s (seconds) or min (minutes).
    * @param detected_when - Specification whether all components of the reaction solution
             were already present or if some were added after the
             measurement at the timepoint of the pH measurement.
    * @param detected_how - The pH value of a reaction can be determined in various ways, such as
             using a pH meter, pH paper, titration, electrochemical
             sensors, or other methods.
    * @param temperature - The temperature at the time of pH measurement.
    * @param temperature_unit - The temperature can be specified in units such as K, °C, or °F.
    * @param calibration_pH_electrode - Usually, a pH electrode is calibrated using standard buffers at 20-25
             °C. If the conditions in the reaction mixture differ from
             this, it should be specified. (
    * @param pH_gradient_beginning - The initial pH from which the pH gradient begins. (
    * @param pH_gradient_end - The target pH reached after the pH gradient is applied. (
    * @param gradient_length - The distance or time span over which the pH gradient is applied. (
    * @param gradient_length_unit - The gradient length can be specified either as the physical distance
             (e.g. in meters) or as the time span (e.g. in minutes). (
    * @param measurement_points - Information about the locations or time points where pH measurements
             are taken to monitor the gradient. This can be important
             to ensure that the gradient behaves as intended. (
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the pH value that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface DynamicpH_TFCR extends JsonLd {
  pH_beginning: number;
  pH_after_event: number;
  event_description: string;
  pH_at_XY: number;
  time_at_XY: number;
  time_unit: string;
  detected_when: string;
  detected_how: string;
  temperature: number;
  temperature_unit: string;
  calibration_pH_electrode: string;
  pH_gradient_beginning: number;
  pH_gradient_end: number;
  gradient_length: number;
  gradient_length_unit: string;
  measurement_points: string;
  special_treatment: string;
}

export const DynamicpH_TFCRCodec = D.lazy("DynamicpH_TFCR", () => D.struct({
    pH_beginning: D.number,
    pH_after_event: D.number,
    event_description: D.string,
    pH_at_XY: D.number,
    time_at_XY: D.number,
    time_unit: D.string,
    detected_when: D.string,
    detected_how: D.string,
    temperature: D.number,
    temperature_unit: D.string,
    calibration_pH_electrode: D.string,
    pH_gradient_beginning: D.number,
    pH_gradient_end: D.number,
    gradient_length: D.number,
    gradient_length_unit: D.string,
    measurement_points: D.string,
    special_treatment: D.string,
}));