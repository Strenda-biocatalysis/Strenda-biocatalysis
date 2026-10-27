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

// Components Specification Type definitions
/**
    Comprehensive specification of a single chemical component used in
    an enzymatic reaction, including its identity, role, quantity,
    source, and storage requirements.

    * @param identity - Chemical identification and characterization of the component.
    * @param role - What this component does in the reaction (substrate, cosubstrate,
             salt, ...).
    * @param amount - Quantity or concentration of the component used in the reaction.
    * @param provenance - Source and supplier information for the component.
    * @param solubility - Solubility characteristics of the component under reaction conditions.
    * @param storage - Storage requirements and conditions for the component.
    * @param notes - Additional notes or comments about the component.
**/
export interface ReactionComponent extends JsonLd {
  identity: ComponentIdentity;
  role?: ComponentRole | null;
  amount?: AmountConcentration | null;
  provenance?: Provenance | null;
  solubility?: SolubilityLimit | null;
  storage?: StorageConditions | null;
  notes?: string | null;
}

export const ReactionComponentCodec = D.lazy("ReactionComponent", () => D.struct({
    identity: ComponentIdentityCodec,
    role: D.nullable(ComponentRoleCodec),
    amount: D.nullable(AmountConcentrationCodec),
    provenance: D.nullable(ProvenanceCodec),
    solubility: D.nullable(SolubilityLimitCodec),
    storage: D.nullable(StorageConditionsCodec),
    notes: D.nullable(D.string),
}));


/**
    Chemical identification and characterization information for a
    component, including names, structural identifiers, and physical
    properties.

    * @param name - Common or systematic name of the component.
    * @param smiles - SMILES (Simplified Molecular Input Line Entry System) notation for the
             chemical structure.
    * @param identifiers - One or more identifiers like CAS, PubChem CID, InChI, etc.
    * @param purity - Purity of the component as a percentage or fraction.
    * @param formulation - Physical form or formulation of the component (powder, liquid,
             solution, etc.).
**/
export interface ComponentIdentity extends JsonLd {
  name: string;
  smiles?: string | null;
  identifiers?: string[] | null;
  purity?: number | null;
  formulation?: FormulationType | null;
}

export const ComponentIdentityCodec = D.lazy("ComponentIdentity", () => D.struct({
    name: D.string,
    smiles: D.nullable(D.string),
    identifiers: D.array(D.string),
    purity: D.nullable(D.number),
    formulation: D.nullable(FormulationTypeCodec),
}));


/**
    Quantitative specification of component amount or concentration used
    in the reaction.

    * @param value - Numerical value of the amount or concentration.
    * @param unit - Unit of measurement for the amount or concentration.
**/
export interface AmountConcentration extends JsonLd {
  value?: number | null;
  unit?: string | null;
}

export const AmountConcentrationCodec = D.lazy("AmountConcentration", () => D.struct({
    value: D.nullable(D.number),
    unit: D.nullable(D.string),
}));


/**
    Source and supplier information for component traceability and
    reproducibility.

    * @param supplier - Supplier/manufacturer or "prepared in lab"; include product code or
             citation if applicable.
**/
export interface Provenance extends JsonLd {
  supplier?: string | null;
}

export const ProvenanceCodec = D.lazy("Provenance", () => D.struct({
    supplier: D.nullable(D.string),
}));


/**
    Solubility characteristics of the component under specific conditions.

    * @param value - Numerical value of the solubility limit.
    * @param unit - Unit of measurement for the solubility limit.
**/
export interface SolubilityLimit extends JsonLd {
  value?: number | null;
  unit?: string | null;
}

export const SolubilityLimitCodec = D.lazy("SolubilityLimit", () => D.struct({
    value: D.nullable(D.number),
    unit: D.nullable(D.string),
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


// Components Specification Enum definitions
export enum ComponentRole {
  BUFFER = 'buffer',
  COENZYME = 'coenzyme',
  COFACTOR = 'cofactor',
  COSUBSTRATE = 'cosubstrate',
  ION = 'ion',
  OTHER = 'other',
  PRODUCT = 'product',
  SALT = 'salt',
  SOLVENT = 'solvent',
  SUBSTRATE = 'substrate',
}

export const ComponentRoleCodec = D.union(
  D.literal(ComponentRole.BUFFER),
  D.literal(ComponentRole.COENZYME),
  D.literal(ComponentRole.COFACTOR),
  D.literal(ComponentRole.COSUBSTRATE),
  D.literal(ComponentRole.ION),
  D.literal(ComponentRole.OTHER),
  D.literal(ComponentRole.PRODUCT),
  D.literal(ComponentRole.SALT),
  D.literal(ComponentRole.SOLVENT),
  D.literal(ComponentRole.SUBSTRATE),
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