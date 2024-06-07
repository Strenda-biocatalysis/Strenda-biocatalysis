# Sampling

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        samplingdescription(SamplingDescription)
        samplingfromheterogeneousreactionsolutions(SamplingFromHeterogeneousReactionSolutions)
        samplepreprocessing(SamplePreprocessing)
    
        click samplingdescription "#samplingdescription" "Go to SamplingDescription"
        click samplingfromheterogeneousreactionsolutions "#samplingfromheterogeneousreactionsolutions" "Go to SamplingFromHeterogeneousReactionSolutions"
        click samplepreprocessing "#samplepreprocessing" "Go to SamplePreprocessing"
    ```



## Types


### SamplingDescription
Information about the sampling process, used during the experiment. In some experiments no sampling is taking place at all, for example, if an experiment is monitored via a photospectrometer in a 96-well plate over time.

__volume_per_sample__* `float`

- Volume of the collected sample.
- `Minimum`: 0.0

__volume_per_sample_unit__* `string`

- Common units include mL (milliliters), μl (microliters), g (grams), or other volume units, depending on whether the samples are liquid or solid.

__mixing_during_sampling__* `string`

- Provide information about whether the reaction was mixed during sampling, as this can affect the representativeness of the collected sample.

__vessel_opened_for_sampling__* `string`

- Information about whether the reaction vessel was opened for sampling or not.

__gas_phase__* `string`

- Information about the composition of the gas phase above the reaction solution, including gases such as nitrogen, carbon dioxide, argon, oxygen or other gases.

__time__* `float`

- The time at which the sample was taken.

------

### SamplingFromHeterogeneousReactionSolutions
Sample preprocessing

__phase__* `string`

- Information about which phase the sample was taken from must be provided.

__biocatalyst_in_phase__* `string`

- Information on whether the collected sample may be contaminated with the (bio)catalyst.

__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the sampling that are important for reproducibility and are not described by the aforementioned                     metadata, they should be explained here.

------

### SamplePreprocessing
Sample preprocessing involves the necessary steps taken to prepare and treat collected samples before analysis or further experimentation.

__quenching_method__* `string`

- Techniques or methods used to halt the reaction, including the chemicals or procedures employed (e.g., heat treatment). Accurate documentation of quenching methods in enzymatic reactions is vital as        these methods can significantly impact subsequent analytical procedures. For instance, opting for an organic solvent as a quenching reagent can notably enhance the solubility of substrates or products, directly         influencing downstream analyses.

__quenching_ratio__* `string`

- Information about the precise ratio or volume of the quenching solution in relation to the reaction mixture. (

__treatment_procedure__* `string`

- Any further details regarding the sample processing steps that were carried out after it was collected from the reaction vessel (e.g., filtering samples).

__special_treatment__* `string`

- If there are any other specific methods, procedures, characteristics or aspects related to the sampling that are important for reproducibility and are not described by the aforementioned                     metadata, they should be explained here.