[Landing Page](/Readme.md)

# Components

__Each additive__ of a reaction must be defined like substrate, cosubstrate, coenzyme, salts, ions, etc. The [biocatalyst](https://github.com/StephanM87/Strenda-biocatalysis/blob/main/ModelExamples/Biocatalyst/Readme.md) and comprehensive description of the [various states or conditions](https://github.com/StephanM87/Strenda-biocatalysis/tree/main/ModelExamples/Reaction_conditions) during the reaction are not included among the listed reaction components.

<img src="https://github.com/StephanM87/Strenda-biocatalysis/assets/106530250/516ebcfd-5610-4660-8a0c-8cb3d1405c9b" width="375" >


### Components

Each component present in the planned reaction must be defined.

- __name__
  - Type: string
  - Description: The name of the reactant can be either the trivial or trade name, the systematic designation according to IUPAC nomenclature, or any other means of identifying the substance.

- __smiles__
  - Type: string
  - Description: SMILES (Simplified Molecular Input Line Entry System) is a chemical notation used to represent and describe molecular structures in a simplified and human-readable format.

- __persistent_identifier_PID__
  - Type: string
  - Description: One or more identifiers that refer to the compound, such as CAS number, PubChem code, InChI code, etc.

- __concentration__
  - Type: posfloat
  - Description: The concentration of the reactant.

- __concentration_unit__
  - Type: string
  - Description: The concentration of the reactant is typically expressed in M (Molar), mmol/L (millimoles per liter), or µmol/L (micromoles per liter).

- __supplier__
  - Type: string
  - Description: Information about the source of the compound, usually a commercial supplier with perhaps product code, but could be preparation in a research lab.

- __purity__
  - Type: float
  - Description: Purity of a substance typically expressed in percentage (%). It is commonly defined as the percentage of the pure or desired compound relative to the total mass or volume of the substance.

- __formulation__
  - Type: string
  - Description: The formulation encompass the nature of the reactant, whether it is in powder, liquid, gaseous form, or any other form, as well as the specific conditions under which it is presented.

<hr>

# Storage conditions

Describing the components in the reaction mixture involve specifying their storage conditions before use in the reaction.

### StorageConditions

- __temperature__
  - Type: float
  - Description: The temperature at which the reactant is stored.
 
- __temperature_unit__
  - Type: string
  - Description: The temperature can be specified in units such as K, °C, or °F.

- __storage_start__
  - Type: date
  - Description: The date since the reactant has been stored.

- __additives__
  - Type: string
  - Description: Additives for the storage of reactants can include antioxidants, stabilizers, drying agent, or even inert gases (argon, nitrogen), among others.

- __removing/rethawing__
  - Type: sting
  - Description: For specific applications, it may be crucial to track how often the reactant has been removed from storage and, if applicable, thawed.

- __thawing_process__
  - Type: string
  - Description: If the reactant needs to be frozen, it is also important to know how this was carried out.

<hr>
 
- __special_treatment__
  - Type: string
  - Description: If there are any other specific characteristics or aspects related to the reactant that are important for reproducibility and are not described by the aforementioned metadata, they should be explained       here.

 <hr>
