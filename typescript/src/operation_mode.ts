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

// Operation Mode Type definitions
/**
    The batch operation mode represents a fundamental approach
    in biocatalysis, where all reaction components are mixed
    simultaneously within a closed system, and the reaction proceeds
    until a predetermined endpoint is reached. This mode is easy to
    control and well-suited for producing small batches of products.

    * @param reactor_type
**/
export interface Batch extends JsonLd {
  reactor_type: string;
}

export const BatchCodec = D.lazy("Batch", () => D.struct({
    reactor_type: D.string,
}));


/**
    In the fed-batch operation mode, additional compounds (e.g.,
    substrates, acid/base for pH regulation, etc.) are gradually added
    during the reaction to control reaction conditions or enhance
    product formation. This mode allows for better control of the
    reaction progress and can increase productivity.

    * @param reactor_type
**/
export interface FedBatch extends JsonLd {
  reactor_type: string;
}

export const FedBatchCodec = D.lazy("FedBatch", () => D.struct({
    reactor_type: D.string,
}));


/**
    In the continuous operation mode, the reaction operates continuously
    with substrates continuously supplied and products continuously
    removed. This mode enables uniform product formation and is
    particularly suitable for large-scale production.

    * @param reactor_type
**/
export interface Continuous extends JsonLd {
  reactor_type: string;
}

export const ContinuousCodec = D.lazy("Continuous", () => D.struct({
    reactor_type: D.string,
}));


/**
    A combinatorial mode does not clearly fit into any of the
    aforementioned subcategories and thus represents a mixture of
    operation modes. This kind of experiment design could be used to
    systematically explore various reaction conditions or components
    in a combined manner. This approach allows the exploration of
    multiple options, such as varying substrate concentrations,
    catalysts, or reaction conditions. The goal is to identify
    the optimal conditions or combinations that most efficiently
    facilitate desired reactions in biocatalysis.

    * @param reactor_type
**/
export interface CombinatorialMode extends JsonLd {
  reactor_type: string;
}

export const CombinatorialModeCodec = D.lazy("CombinatorialMode", () => D.struct({
    reactor_type: D.string,
}));