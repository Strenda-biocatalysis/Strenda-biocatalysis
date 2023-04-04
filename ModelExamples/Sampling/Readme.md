[Landing Page](/Readme.md)

# Sampling


<img src="Sampling procedure.png" width=250>


<details> <Summary>Sampling from homogeneous reaction mixtures</Summary>

### SamplingFromHomogeneousAqueousReactionMixtures


Information about the sampling process, used during the experiment. In some experiments no sampling is taking place at all, for example if an experiment is monitored via a photospectrometer in a 96-well plate over time. In this case, of course, no sampling was done during the experiment

- __volume_per_sample__
  - Type: posfloat
  - Description: What volume was taken from the reaction per sample?

- __volume_per_sample_unit__
  - Type: string
  - Description: Unit of the sample volume

- __reaction_stop__
  - Type: TreatmentToStopReaction
  - Description: Process how the reaction was stopped

</details>


<details> <Summary>Sampling from homogeneous organic reaction mixtures</Summary>

### SamplingFromHomogeneousOrganicReactionMixtures


Information about the sampling process, used during the experiment. In some experiments no sampling is taking place at all, for example if an experiment is monitored via a photospectrometer in a 96-well plate over time. In this case, of course, no sampling was done during the experiment

- __volume_per_sample__
  - Type: posfloat
  - Description: What volume was taken from the reaction per sample?

- __volume_per_sample_unit__
  - Type: string
  - Description: Unit of the sample volume

- __vessel_opened_for_sampling__
  - Type: string
  - Description: Was the vessel opened for the sampling procedure?

- __gas_phase__
  - Type: string
  - Description: What is the gas phase above the reaction solution?

- __reaction_stop__
  - Type: TreatmentToStopReaction
  - Description: Process how the reaction was stopped


</details>

<details> <Summary>Sampling from heterogeneous reaction mixtures</Summary>

### SamplingFromHeterogeneousReactionMixtures


Information about the sampling process, used during the experiment. In some experiments no sampling is taking place at all, for example if an experiment is monitored via a photospectrometer in a 96-well plate over time. In this case, of course, no sampling was done during the experiment

- __volume_per_sample__
  - Type: posfloat
  - Description: What volume was taken from the reaction per sample?

- __volume_per_sample_unit__
  - Type: string
  - Description: Unit of the sample volume

- __sample_taken_from_phase__
  - Type: String
  - Description: Phase from which the sample was taken from

- __mixing_during_sampling__
  - Type: string 
  - Description: Was the reaction solution mixed during the sampling procedure?

- __vessel_opened_for_sampling__
  - Type: string
  - Description: Was the vessel opened for the sampling procedure?

- __gas_phase__
  - Type: string
  - Description: What is the gas phase above the reaction solution?

- __reaction_stop__
  - Type: TreatmentToStopReaction
  - Description: Process how the reaction was stopped





</details>

<details><Summary>Specialised sampling</Summary>

## Specialised sampling

If the sampling procedure is more complex than just the plain procedure of taking a sample from the reaction vessel.


<details> <Summary>Sampling from heterogeneous reaction solutions</Summary>


### SamplingProcedureFromHeterogeneousReactionMixtures

- __phase__
  - Type: string
  - Description: From which phase was the sample taken?

- __biocatalyst_in_phase__
  - Type: string
  - Description: Is the phase from which the sample was taken, containing the (bio)catalyst?

</details>

## Sample processing

<details> <Summary>Treatment to stop reaction</Summary>

### TreatmentToStopReaction

Information about the sampling process, if a pre-processing did take place

- __treatment_procedure__
  - Type: string
  - Description: How was the sample processed, once it was taken from the reaction vessel?

</details>

</details>


