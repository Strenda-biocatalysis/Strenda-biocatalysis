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

// Components Type definitions
/**
    Each component present in the planned reaction must be defined.

    * @param name - The name of the component can be either the trivial or trade name, the
             systematic designation according to IUPAC nomenclature,
             or any other means of identifying the substance.
    * @param smiles - SMILES (Simplified Molecular Input Line Entry System) is a chemical
             notation used to represent and describe molecular
             structures in a simplified and human-readable format.
    * @param persistent_identifier_PID - One or more identifiers that refer to the compound, such as CAS
             number, PubChem code, InChI code, etc.
    * @param concentration - Concentration of the component.
    * @param concentration_unit - The concentration of the component is typically expressed in M
             (Molar), mmol/L (millimoles per liter), or µmol/L
             (micromoles per liter).
    * @param supplier - Information about the source of the compound, usually a commercial
             supplier with perhaps product code, but could be
             preparation in a research lab. Should the component have
             been synthesized internally, please include a literature
             reference detailing its synthesis.
    * @param purity - Purity of a substance typically expressed in percentage (%). It is
             commonly defined as the percentage of the pure or desired
             compound relative to the total mass or volume of the
             substance.
    * @param formulation - The formulation encompass the nature of the component, whether it
             is in powder, liquid, gaseous form, or any other form,
             as well as the specific conditions under which it is
             presented.
    * @param solubility_limit - This limit represents the maximum concentration of a component, which
             might include gases, that can dissolve in a solution or
             gas phase. (
    * @param solubility_limit_unit - The solubility limit of a component can be expressed in various units,
             including M (moles per liter), g/L (grams per liter),
             % (percentage concentration), or particles per volume,
             depending on the type of component and the solvent used.
             (
**/
export interface Components extends JsonLd {
  name: string;
  smiles: string;
  persistent_identifier_PID: string;
  concentration: number;
  concentration_unit: string;
  supplier: string;
  purity: number;
  formulation: string;
  solubility_limit: number;
  solubility_limit_unit: string;
}

export const ComponentsCodec = D.lazy("Components", () => D.struct({
    name: D.string,
    smiles: D.string,
    persistent_identifier_PID: D.string,
    concentration: D.number,
    concentration_unit: D.string,
    supplier: D.string,
    purity: D.number,
    formulation: D.string,
    solubility_limit: D.number,
    solubility_limit_unit: D.string,
}));


/**
    * @param temperature - Temperature at which the component is stored.
    * @param temperature_unit - The temperature can be specified in units such as K, °C, or °F.
    * @param storage_start - The date since the component has been stored.
    * @param additives - Additives for the storage of components can include antioxidants,
             stabilizers, drying agent, or even inert gases (argon,
             nitrogen), among others.
    * @param special_treatment - If there are any other specific characteristics or aspects related to
             a component that are important for reproducibility and
             are not described by the aforementioned metadata, they
             should be explained here.
**/
export interface StorageConditions extends JsonLd {
  temperature: number;
  temperature_unit: string;
  storage_start: string;
  additives: string;
  special_treatment: string;
}

export const StorageConditionsCodec = D.lazy("StorageConditions", () => D.struct({
    temperature: D.number,
    temperature_unit: D.string,
    storage_start: D.string,
    additives: D.string,
    special_treatment: D.string,
}));