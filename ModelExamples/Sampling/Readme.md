[Landing Page](/Readme.md)

<div align="justify">

# Sampling

The categorisation of sampling into the two main categories, __default sampling__ and __specialised sampling__, enables the capture and documentation of either standard sampling information and/or specialised sampling data, depending on specific needs.

<img src="https://github.com/StephanM87/Strenda-biocatalysis/assets/106530250/d5a2492a-c279-489f-b393-07a8146a5e69" width="400">


## Default sampling

Default sampling refers to the standard methods and procedures commonly used for sample collection in enzymatic reactions.

<details> <Summary>Sampling description</Summary>

### SamplingDescription

Information about the sampling process, used during the experiment. In some experiments no sampling is taking place at all, for example if an experiment is monitored via a photospectrometer in a 96-well plate over time. In this case, of course, no sampling was done during the experiment.

- __volume_per_sample__
  - Type: posfloat
  - Description: The volume of the collected sample.

- __volume_per_sample_unit__
  - Type: string
  - Description: Common units include mL (milliliters), μl (microliters), g (grams), or other volume units, depending on whether the samples are liquid or solid.

- __mixing_during_sampling__
  - Type: string 
  - Description: Provide information about whether the sample was mixed during sampling, as this can affect the representativeness of the collected sample.

- __vessel_opened_for_sampling__
  - Type: string
  - Description: Information about whether the reaction vessel was opened for sampling or not.

- __gas_phase__
  - Type: string
  - Description: Information about the gas phase above the reaction solution.

- __time__
  - Type: time
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
  - Description: Information on whether the collected sample may have contaminations in the form of an (bio)catalyst.

<hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the sampling that are important for reproducibility and are not described by the aforementioned                     metadata, they should be explained here.

</details>

<details> <Summary>Sample preprocessing</Summary>

### SamplePreprocessing

Sample preprocessing involves the necessary steps taken to prepare and treat collected samples before analysis or further experimentation.

- __treatment_procedure__
  - Type: string
  - Description: Details regarding the sample processing steps that were carried out after it was collected from the reaction vessel.

<hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific methods, procedures, characteristics or aspects related to the sampling that are important for reproducibility and are not described by the aforementioned                     metadata, they should be explained here.

</details>

<hr>

</div>
