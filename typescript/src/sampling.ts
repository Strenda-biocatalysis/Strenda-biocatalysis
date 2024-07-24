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

// Sampling Type definitions
/**
    Information about the sampling process, used during the experiment. In
    some experiments no sampling is taking place at all, for example,
    if an experiment is monitored via a photospectrometer in a 96-well
    plate over time.

    * @param volume_per_sample - Volume of the collected sample.
    * @param volume_per_sample_unit - Common units include mL (milliliters), μl (microliters), g (grams), or
             other volume units, depending on whether the samples are
             liquid or solid.
    * @param mixing_during_sampling - Provide information about whether the reaction was mixed during
             sampling, as this can affect the representativeness of
             the collected sample.
    * @param vessel_opened_for_sampling - Information about whether the reaction vessel was opened for sampling
             or not.
    * @param gas_phase - Information about the composition of the gas phase above the reaction
             solution, including gases such as nitrogen, carbon
             dioxide, argon, oxygen or other gases.
    * @param time - The time at which the sample was taken.
**/
export interface SamplingDescription extends JsonLd {
  volume_per_sample: number;
  volume_per_sample_unit: string;
  mixing_during_sampling: string;
  vessel_opened_for_sampling: string;
  gas_phase: string;
  time: number;
}

export const SamplingDescriptionCodec = D.lazy("SamplingDescription", () => D.struct({
    volume_per_sample: D.number,
    volume_per_sample_unit: D.string,
    mixing_during_sampling: D.string,
    vessel_opened_for_sampling: D.string,
    gas_phase: D.string,
    time: D.number,
}));


/**
    Sample preprocessing

    * @param phase - Information about which phase the sample was taken from must be
             provided.
    * @param biocatalyst_in_phase - Information on whether the collected sample may be contaminated with
             the (bio)catalyst.
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the sampling that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface SamplingFromHeterogeneousReactionSolutions extends JsonLd {
  phase: string;
  biocatalyst_in_phase: string;
  special_treatment: string;
}

export const SamplingFromHeterogeneousReactionSolutionsCodec = D.lazy("SamplingFromHeterogeneousReactionSolutions", () => D.struct({
    phase: D.string,
    biocatalyst_in_phase: D.string,
    special_treatment: D.string,
}));


/**
    Sample preprocessing involves the necessary steps taken to
    prepare and treat collected samples before analysis or further
    experimentation.

    * @param quenching_method - Techniques or methods used to halt the reaction, including the
             chemicals or procedures employed (e.g., heat treatment).
             Accurate documentation of quenching methods in enzymatic
             reactions is vital as these methods can significantly
             impact subsequent analytical procedures. For instance,
             opting for an organic solvent as a quenching reagent can
             notably enhance the solubility of substrates or products,
             directly influencing downstream analyses.
    * @param quenching_ratio - Information about the precise ratio or volume of the quenching
             solution in relation to the reaction mixture. (
    * @param treatment_procedure - Any further details regarding the sample processing steps that were
             carried out after it was collected from the reaction
             vessel (e.g., filtering samples).
    * @param special_treatment - If there are any other specific methods, procedures, characteristics
             or aspects related to the sampling that are important
             for reproducibility and are not described by the
             aforementioned metadata, they should be explained here.
**/
export interface SamplePreprocessing extends JsonLd {
  quenching_method: string;
  quenching_ratio: string;
  treatment_procedure: string;
  special_treatment: string;
}

export const SamplePreprocessingCodec = D.lazy("SamplePreprocessing", () => D.struct({
    quenching_method: D.string,
    quenching_ratio: D.string,
    treatment_procedure: D.string,
    special_treatment: D.string,
}));