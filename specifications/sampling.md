---
repo: "https://www.github.com/my/repo/"
prefix: "stbc"
---

[Landing Page](/Readme.md)

<div align="justify">

# Sampling

The categorisation of sampling into the two main categories, __default sampling__ and __specialised sampling__, enables the capture and documentation of either standard sampling information and/or specialised sampling data, depending on specific needs.

<img src="https://github.com/user-attachments/assets/bc54b453-996a-412d-9faa-560e849a66ab" width="400">


## Default sampling

Default sampling refers to the standard methods and procedures commonly used for sample collection in enzymatic reactions.

<details> <Summary>Sampling description</Summary>

### SamplingDescription

Information about the sampling process, used during the experiment. In some experiments no sampling is taking place at all, for example, if an experiment is monitored via a photospectrometer in a 96-well plate over time.

- __volume_per_sample__
  - Type: float
  - Minimum: 0.0
  - Description: Volume of the collected sample.

- __volume_per_sample_unit__
  - Type: string
  - Description: Common units include mL (milliliters), μl (microliters), g (grams), or other volume units, depending on whether the samples are liquid or solid.

- __mixing_during_sampling__
  - Type: string
  - Description: Provide information about whether the reaction was mixed during sampling, as this can affect the representativeness of the collected sample.

- __vessel_opened_for_sampling__
  - Type: string
  - Description: Information about whether the reaction vessel was opened for sampling or not.

- __gas_phase__
  - Type: string
  - Description: Information about the composition of the gas phase above the reaction solution, including gases such as nitrogen, carbon dioxide, argon, oxygen or other gases.

- __time__
  - Type: float
  - Description: The time at which the sample was taken.


</details>

<hr>

## Specialised sampling

If the sampling procedure is more complex than just the plain procedure of taking a sample from the reaction vessel, further details need to be provided.

<details> <Summary>Sampling from heterogeneous reaction solutions</Summary>

### SamplingFromHeterogeneousReactionSolutions

- __phase__
  - Type: string
  - Description: Information about which phase the sample was taken from must be provided.

- __biocatalyst_in_phase__
  - Type: string
  - Description: Information on whether the collected sample may be contaminated with the (bio)catalyst.

<hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the sampling that are important for reproducibility and are not described by the aforementioned                     metadata, they should be explained here.

</details>

<details> <Summary>Sample preprocessing</Summary>

### SamplePreprocessing

Sample preprocessing involves the necessary steps taken to prepare and treat collected samples before analysis or further experimentation.

- __quenching_method__
  - Type: string
  - Description: Techniques or methods used to halt the reaction, including the chemicals or procedures employed (e.g., heat treatment). Accurate documentation of quenching methods in enzymatic reactions is vital as        these methods can significantly impact subsequent analytical procedures. For instance, opting for an organic solvent as a quenching reagent can notably enhance the solubility of substrates or products, directly         influencing downstream analyses.

- __quenching_ratio__
  - Type: string
  - Description: Information about the precise ratio or volume of the quenching solution in relation to the reaction mixture. (__if_applicable__)

- __treatment_procedure__
  - Type: string
  - Description: Any further details regarding the sample processing steps that were carried out after it was collected from the reaction vessel (e.g., filtering samples).

<hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the sampling that are important for reproducibility and are not described by the aforementioned                     metadata, they should be explained here.

</details>

<hr>

</div>
