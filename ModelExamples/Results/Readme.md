[Landing Page](/Readme.md)

<div align="justify">

# Results documentation

This category serves as an extension of the actual metadata catalog and deals with recommendations for the documentation and analysis of the results of biocatalytic experiments. It covers a variety of metrics and parameters based on the [STRANDA Guidelines](https://www.beilstein-institut.de/en/projects/strenda/) for improving the reproducibility of experiments within the field of biocatalysis. 

## Kinetic parameters

Kinetic parameters provide key insights into the efficiency and performance of an enzymatic reactions. Parameters like K<sub>m</sub>, V<sub>max</sub>, and k<sub>cat</sub>/K<sub>m</sub> elucidate the enzyme-substrate interaction and can further be used for optimizing reaction conditions.

<details> <Summary>Kinetic parameters</Summary>

### KineticParameters

These parameters serve as benchmarks for understanding enzyme kinetics. The K<sub>m</sub> and k<sub>cat</sub> value is determined by all substrates involved in the reaction and not just one. Therefore, the concentrations of <ins>**all**</ins> substrates must be varied and the K<sub>m</sub> and k<sub>cat</sub> values calculated to obtain a common value instead of apparent values. For a comprehensive report around the technical key data of the kinetic parameters, see literature for further information, e.g. [Pesci _et al._<sup>1</sup>](https://doi.org/10.1007/978-3-662-57619-9_4), [Bisswanger <sup>2</sup>](https://doi.org/10.1002/9783527806461) .

- __michaelis_constant__
  - Type: float
  - Description: The Michaelis-Menten constant (K<sub>m</sub>​) represents the substrate concentration at which an enzyme achieves half of its maximum reaction rate.
 
- __michaelis_constant_unit__
  - Type: string
  - Description: The unit of the Michaelis-Menten constant (K<sub>m</sub>​) is typically expressed as moles per liter (M or mM).
 
- __maximum_reaction_rate__
  - Type: float
  - Description: V<sub>max</sub>, the maximum reaction rate, represents the speed at which an enzyme-catalyzed reaction reaches saturation, indicating the maximum achievable rate of product formation under optimal substrate concentration (where enzymes are predominantly saturated with substrates).

- __maximum_reaction_rate_unit__
  - Type: string
  - Description: The unit of V<sub>max</sub> (maximum reaction rate) is typically represented as concentration per time, such as moles per liter per second (mol/L/s or mM/s).
 
- __turnover_number__
  - Type: float
  - Description: The turnover number (k<sub>cat</sub>) measures the number of substrate molecules converted to product per active site of an enzyme per unit time when the enzyme is fully saturated with substrate.

- __turnover_number_unit__
  - Type: string
  - Description: The unit of turnover number (k<sub>cat</sub>) is typically expressed as moles of product per mole of enzyme per second or per minute (time<sup>-1</sup>).
 
- __catalytic_efficiency__
  - Type: float
  - Description: Catalytic efficiency (k<sub>cat</sub>/K<sub>m</sub>) is a measure of how effectively an enzyme converts substrate into product, often quantified as the ratio of the turnover number (k<sub>cat</sub>) to the Michaelis-Menten constant (K<sub>m</sub>).
 
- __catalytic_efficiency_unit__
  - Type: string
  - Description: The typical unit for catalytic efficiency (k<sub>cat</sub>/K<sub>m</sub>) is M<sup>-1</sup>s<sup>-1</sup>.
 
- __dissociation_constant__
  - Type: float
  - Description: The dissociation constant (K<sub>d</sub>) is a measure that represents the equilibrium between a complex and its dissociated components.
 
- __dissociation_constant_unit__
  - Type: string
  - Description: The dissociation constant (K<sub>d</sub>) is typically expressed in M (mol per liter) or its derivatives, such as nM (nanomoles per liter).
 
- __inhibition_type__
  - Type: string
  - Description: Enzyme inhibition encompasses various forms, including competitive, non-competitive, uncompetitive, mixed, and irreversible inhibition. Each type has different effects on the enzyme's function and plays a crucial role in regulating biochemical processes.

- __inhibition_constant__
  - Type: float
  - Description: The inhibition constant (K<sub>i</sub>) describes the affinity of an inhibitor for an enzyme. It indicates how effectively an inhibitor influences enzyme activity. A lower K<sub>i</sub> value suggests a strong binding of the inhibitor to the enzyme.

- __inhibition_constant_unit__
  - Type: string
  - Description: The units for the inhibition constant (K<sub>i</sub>) are commonly expressed in M (mol per liter) or related units.
 
- __hill_coefficient__
  - Type: float
  - Description: The Hill coefficient is a parameter used to describe cooperativity in the binding of molecules to proteins. It is employed in enzyme reactions, e.g. oxygen binding to hemoglobin, to indicate whether there is positive (cooperative) or negative (anticooperative) binding. A Hill coefficient greater than 1 indicates positive cooperativity, while a value less than 1 indicates negative cooperativity. A value of exactly 1 indicates no cooperativity.
  
- __enzyme_stability__
  - Type: string
  - Description: The stability of enzymes is often characterized by various parameters such as the enzyme's half-life under specific conditions, the decline in activity over time, or the preservation of catalytic activity under different environmental conditions. 


<hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific metrics, parameters, characteristics or aspects related to the kinetics that are important to document the results accurately and are not described by the aforementioned metadata, they should be explained here.

</details>


<hr>

## Yield and conversion

The documentation of yield and conversion provides essential insights into the efficiency of a reaction and the amount of desired product obtained. 

<details> <Summary>Yield and conversion</Summary>

### YieldAndConversion

These metrics are vital for evaluating the success of a process, optimizing reaction conditions, and ensuring the production of high-quality products in biocatalytic applications. For a comprehensive report around the technical key data of yield and conversion, see literature for further information, e.g. [Lies _et al._<sup>3</sup>](https://doi.org/10.1007/978-3-662-57619-9_4).


- __yield__
  - Type: posfloat
  - Description: Yield represents the amount of the desired product obtained from a reaction. It is the number of synthesized molecules of product per number of starting molecules. The following formula can be used:
    $$Y_p = \frac{n_p - n_{p0}}{n_{s0}} \cdot \frac{|v_s|}{|v_p|}$$

    where, *Y<sub>p</sub>* - yield of the product *p* (-), *n<sub>p0</sub>* - amount of product *p* at the start of the reaction (mol), *n<sub>p</sub>* - amount of product *p* at the end of the reaction (mol), *v<sub>s</sub>* - stoichiometric factor for the substrate *s* (-), *v<sub>p</sub>* - stoichiometric factor for the product *p* (-). Note: The reported yield relies on analytical findings. Typically, the isolated yield is more common in practice as it reflects the precise quantity of product acquired post downstream processing (DSP).
 
- __yield_unit__
  - Type: string
  - Description: The yield is typically expressed in percentages (%), reflecting the ratio of the actual obtained product quantity to the theoretical maximum product quantity that could be obtained under ideal conditions.
 
- __space_time_yield__
  - Type: posfloat
  - Description: Space-time yield in biocatalysis refers to the mass of product obtained per unit volume of the reactor per unit time. Other terms commonly used in the literature are *volumetric productivity* or the *reactor productivity*. The following formula can be used: $$STY = \frac{m_p}{𝜏 \cdot V_R}$$
 
    where, *STY* - space-time yield (g L<sup>-1</sup> h<sup>-1</sup>), *m<sub>p</sub>* - mass of the synthesized product (g), 𝜏 - residence time r reaction time (h), *V<sub>R</sub>* - reactor volume.  
 
- __space_time_yield_unit__
  - Type: string
  - Description: Space-time yield is commonly expressed in g/L/h (grams per liter per hour) or mol/L/h (moles per liter per hour).

- __conversion__
  - Type: float
  - Description: The term "conversion" refers to the percentage of substrate that undergoes transformation into the desired product during a reaction. It is the number of converted molecules per number of starting molecules. The following formula can be used:
    $$X_s = \frac{n_{s0} - n_s}{n_{s0}}$$

    where, *X<sub>s</sub>* - conversion of the substrate *s* (-), *n<sub>s0</sub>* - amount of substrate *s* at the start of the reaction (mol), *n<sub>s</sub>* - amount of substrate *s* at the end of the reaction (mol).
 
- __conversion_unit__
  - Type: string
  - Description: The conversion is commonly expressed as a percentage (%) to indicate the proportion of substrate converted to the desired product during a specific reaction.
 
<hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific metrics, parameters, characteristics or aspects related to the conversion or yield that are important to document the results accurately and are not described by the aforementioned attributes, they should be explained here.
  
</details>


<hr>

## Activity and initial reaction rate

This parameter aids in understanding the velocity at which the substrate is converted into products, offering vital information for assessing the enzyme's efficiency and the reaction kinetics.

<details> <Summary>Activity and initial reaction rate</Summary>

### ActivityAndInitialReactionRate

- __specific_activity__
  - Type: posfloat
  - Description: The specific activity refers to the amount of product formed or substrate consumed per unit of enzyme per unit of time.
 
- __specific_activity_unit__
  - Type: string
  - Description: The specific activity is typically expressed in µmol/min/mg (micromoles per minute per milligram of protein).

- __initial_reaction_rate__
  - Type: float
  - Description: The initial reaction rate refers to the rate at which the product is formed in the first 10% of the enzymatic reaction under specific initial substrate concentrations and reaction conditions.
 
- __initial_reaction_rate_unit__
  - Type: string
  - Description: Typically, the initial reaction rate is expressed as mol/L/min (moles per liter per minute) or µmol/mL/min (micromoles per milliliter per minute).


<hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific metrics, parameters, characteristics or aspects related to the activity or initial reaction rate that are important to document the results accurately and are not described by the aforementioned attributes, they should be explained here.

</details>


<hr>


## Selectivity and specificity

The inclusion of selectivity and specificity data offers insights into the precision and efficiency of a catalyst's performance. These parameters determine the catalyst's ability to favorably convert specific substrates into desired products.

<details> <Summary>Selectivity and specificity</Summary>

### SelectivityAndSpecificity

These parameters directly assess a catalyst's precision in converting specific substrates to desired products. For a comprehensive report around the technical key data of the selectivity and specificity, see literature for further information, e.g. [Faber<sup>4</sup>](https://doi.org/10.1007/978-3-642-17393-6_2), [Liese _et al._<sup>3</sup>](https://doi.org/10.1002/3527608184), [Schurig<sup>5</sup>](https://doi.org/10.1007/128_2013_454). 

- __stereoselectivity__
  - Type: string
  - Description: Stereoselectivity refers to the preference of a chemical reaction to produce a specific stereoisomer or a particular spatial arrangement of atoms within a molecule. It describes the ability of a reaction to favor the formation of one stereoisomer over others or to create a specific stereochemical outcome.
 
- __enantioselectivity__
  - Type: posfloat
  - Description: Enantioselectivity, or enantiomeric ratio (E), defines the enzyme's capability to preferentially catalyze the transformation of one enantiomer over its mirror-image counterpart. This trait highlights the enzyme's ability to favor a specific enantiomer either as a product or as the preferred substrate for a reaction.

- __enantiomeric_excess__
  - Type: posfloat
  - Description: The enantiomeric excess (_ee_) measures the degree of purity and efficiency in a chiral catalysis process, representing the excess of one enantiomer over the other in a reaction product. The following formula can be used: $$ee_R = \frac{n_R - n_S}{n_R + n_S}$$
    
    where, *ee<sub>R</sub>* - enantiomeric excess of the (*R*)-enantiomer (-), *n<sub>R</sub>* - amount of the (*R*)-enatiomer (mol) and *n<sub>S</sub>* - amount of the (*S*)-enatiomer (mol).
 
- __enantiomeric_excess_unit__
  - Type: string
  - Description: The primary unit used for enantiomeric excess (_ee_) is percent (%).
 
- __diastereomeric_excess__
  - Type: posfloat
  - Description: The diasteriomeric excess (_de_) represents the difference in the concentration of one diastereomer over another in a reaction product. The following formula can be used: $$de_1 = \frac{n_1 - n_2}{n_1 + n_2}$$
    
    where, *de* - diasteriomeric excess of the major diasteriomer (-), *n<sub>1</sub>* - amount of the major diasteriomer (mol) and *n<sub>2</sub>* - amount of the minor diasteriomer (mol).
 
- __diasteriomeric_excess_unit__
  - Type: string
  - Description: The primary unit used for diasteriomeric excess (_ee_) is percent (%).
 
- __isomeric_content__
  - Type: posfloat
  - Description: The isomeric content (_ic_) refers to the percentage distribution or ratio of different isomers within a mixture resulting from a reaction or process. It describes how various isomers are represented in a product or mixture. The following formula can be used: $$ic = I_1 / \sum_{i=1}^n I_i$$
    
    where, *ic* - proportion of a specific isomer in a mixture of isomers (-), *I<sub>1</sub>* - amount of the specific isomer (mol) and *I<sub>i</sub>* - quantity of all isomers (mol).

- __isomeric_content_unit__
  - Type: string
  - Description: The primary unit used for isomeric content (_ic_) is percent (%).

- __chemoselectivity__
  - Type: string
  - Description: Chemoselectivity refers to the ability of a chemical reaction to target a specific functional group or site within a molecule without affecting other reactive groups present. It highlights the preference of a reaction for one type of chemical bond or functional group over others in a molecule.
 
- __regioselectivity__
  - Type: string
  - Description: Regioselectivity refers to the preference of a reaction to occur at a specific site within a molecule or compound that has multiple potential reaction sites. It describes the tendency of a reaction to selectively take place at a particular position of the molecule, considering its structural arrangement of atoms or functional groups, rather than at other possible sites.
 

<hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific metrics, parameters, characteristics or aspects related to the selectivity and specificity that are important to document the results accurately and are not described by the aforementioned attributes, they should be explained here.

</details>

<hr>


## Thermodynamic parameters

These parameters offer insights into energy changes occurring during the reaction and assist in estimating reaction heat, entropy, and free energy. Understanding the thermodynamic properties of a reaction is essential to determine reaction direction, stability of intermediates, and the level of spontaneity or enforcement of a reaction, but is beyond the scope of the current project phase. 

<details> <Summary>Thermodynamic parameters</Summary>

### ThermodynamicParameters

Understanding the energy dynamics and spontaneity of reactions through thermodynamic parameters is essential for efficient biocatalysis. For a comprehensive report around the technical key data of the kinetic parameters, see literature for further information, e.g. [Heintz<sup>6</sup>](https://doi.org/10.1007/978-3-662-49922-1).


- __gibbs_free_energy_change__
  - Type: string
  - Description: The Gibbs free energy (__G__) represents the portion of energy capable of performing work in a reaction under constant temperature and pressure, providing insights into the spontaneity of the reaction. While the absolute value of the free energy cannot be measured directly, the change in free energy (Δ**G**) throughout the reaction, known as free reaction enthalpy, is measurable. As indicated by the Gibbs-Helmholtz equation, it depends on changes in enthalpy (heat content) and entropy (system disorder) during the reaction. <br>
Δ**G** < 0: The reaction proceeds spontaneously; it is __exergonic__. <br>
Δ**G** = 0: The system is at equilibrium; no work is performed. <br>
Δ**G** > 0: The reaction does not proceed spontaneously; it is __endergonic__. A supply of free energy is required to drive the reaction.
 
- __enthalpy_change__
  - Type: string 
  - Description: The enthalpy (**H**) represents the heat content within a system, expressing the quantity and nature of chemical bonds. This thermodynamic property cannot be measured independently. However, measurable is the change in enthalpy (Δ**H**), which refers to the amount of heat absorbed or released during a chemical reaction (under constant pressure), also known as the reaction enthalpy. <br>
Δ**H** > 0: Heat energy is supplied; the reaction is __endothermic__. <br>
Δ**H** < 0: Heat energy is released; the reaction is __exothermic__.

- __entropy_change__
  - Type: string
  - Description: The entropy (**S**) is a measure of the degree of disorder in a system or the likelihood of a state. Systems inherently tend towards maximum disorder. Every natural process involves an increase in entropy (disorder). If entropy decreases in one area, it must increase elsewhere correspondingly. The increase in entropy can act as a driving force. <br>
Δ**S** > 0: The disorder of the system increases. <br>
Δ**S** < 0: The disorder of the system decreases.
 
<hr>

- __special_treatment__
  - Type: string
  - Description: If there are any other specific metrics, parameters, characteristics or aspects related to the thermodynamic parameters that are important to document the results accurately and are not described by the aforementioned attributes, they should be explained here.

</details>


<hr>

### Literature

[1] Pesci, L., Kara, S., Liese, A. (2018). Enzymkinetik. In: Jaeger, KE., Liese, A., Syldatk, C. (eds) Einführung in die Enzymtechnologie. Springer Spektrum, Berlin, Heidelberg. https://doi.org/10.1007/978-3-662-57619-9_4 <br>
[2] Faber, K. (2011). Biocatalytic Applications. In: Biotransformations in Organic Chemistry. Springer, Berlin, Heidelberg. https://doi.org/10.1007/978-3-642-17393-6_2 <br>
[3] Bisswanger, H. (2017). Enzyme Kinetics: Principles and Methods. John Wiley & Sons. https://doi.org/10.1002/9783527806461 <br>
[4] Liese, A., Seelbach, K., Wandrey, C. (2006). Basics of Bioreaction Engineering. In: Liese, A., Seelbach, K., Wandrey, C. (eds) Industrial biotransformations. John Wiley & Sons. https://doi.org/10.1002/3527608184 <br>
[5] Schurig, V. (2013). Terms for the Quantitation of a Mixture of Stereoisomers. In: Schurig, V. (eds) Differentiation of Enantiomers I. Topics in Current Chemistry, vol 340. Springer, Cham. https://doi.org/10.1007/128_2013_454 <br>
[6] Heintz, A. (2017). Thermodynamik. Springer Spektrum, Berlin, Heidelberg. https://doi.org/10.1007/978-3-662-49922-1 <br>

</div>
