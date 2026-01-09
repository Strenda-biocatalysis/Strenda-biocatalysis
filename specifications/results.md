---
repo: "https://github.com/Strenda-biocatalysis/Strenda-biocatalysis"
prefix: "stbc"
imports:
    utils: ./utils.md
---

# Results Specification

This specification defines the structure and properties of results used in enzymatic reactions, providing comprehensive documentation for kinetic parameters, yield and conversion, activity, selectivity, thermodynamics, and additional notes.

## Types

### Experimental Results

Comprehensive collection of experimental results from enzymatic reactions.

- kinetics
  - Type: Kinetic Results
  - Description: Kinetic parameters and enzyme behavior characteristics.
- yield and conversion
  - Type: Yield And Conversion Results
  - Description: Product yield and substrate conversion measurements.
- activity
  - Type: Activity Results
  - Description: Enzyme activity and initial reaction rate data.
- selectivity
  - Type: Selectivity Results
  - Description: Selectivity measurements including stereoselectivity and enantioselectivity.
- thermodynamics
  - Type: Thermodynamic Results
  - Description: Thermodynamic parameters of the reaction.
- notes
  - Type: string
  - Description: Additional notes or comments about the experimental results.

### Kinetic Results

Kinetic parameters characterizing enzyme behavior and reaction mechanisms.

- michaelis constant
  - Type: Quantity
  - Description: Michaelis constant (Km) representing the substrate concentration at half-maximum reaction rate.
- maximum reaction rate
  - Type: Quantity
  - Description: Maximum reaction rate (Vmax) achieved under saturating substrate conditions.
- turnover number
  - Type: Quantity
  - Description: Turnover number (kcat) representing the maximum number of substrate molecules converted per enzyme molecule per unit time.
- catalytic efficiency
  - Type: Quantity
  - Description: Catalytic efficiency (kcat/Km) indicating the enzyme's effectiveness at low substrate concentrations.
- dissociation constant
  - Type: Quantity
  - Description: Dissociation constant (Kd) for enzyme-substrate or enzyme-inhibitor binding.
- inhibition
  - Type: Inhibition Parameters
  - Description: Parameters describing enzyme inhibition characteristics.
- hill coefficient
  - Type: float
  - Description: Hill coefficient indicating cooperativity in substrate binding or enzyme kinetics.
- enzyme stability
  - Type: string
  - Description: Qualitative or quantitative description of enzyme stability under reaction conditions.
- notes
  - Type: string
  - Description: Additional notes about kinetic measurements or observations.

### Inhibition Parameters

Parameters describing enzyme inhibition characteristics and mechanisms.

- inhibition type
  - Type: Inhibition Type
  - Description: Type of inhibition mechanism observed.
- inhibition constant
  - Type: Quantity
  - Description: Inhibition constant (Ki) quantifying the strength of inhibitor binding.

### Yield And Conversion Results

Product yield and substrate conversion measurements from enzymatic reactions.

- yield
  - Type: Quantity
  - Description: Product yield as percentage or fraction of theoretical maximum.
- space time yield
  - Type: Quantity
  - Description: Space-time yield representing product formation rate per unit reactor volume.
- conversion
  - Type: Quantity
  - Description: Substrate conversion as percentage or fraction of initial substrate consumed.
- notes
  - Type: string
  - Description: Additional notes about yield and conversion measurements.

### Activity Results

Enzyme activity measurements and initial reaction rate data.

- specific activity
  - Type: Quantity
  - Description: Specific activity representing enzyme activity per unit mass of enzyme protein.
- initial reaction rate
  - Type: Quantity
  - Description: Initial reaction rate measured at the beginning of the reaction.
- notes
  - Type: string
  - Description: Additional notes about activity measurements.

### Selectivity Results

Selectivity measurements including stereoselectivity, enantioselectivity, and other selectivity parameters.

- stereoselectivity
  - Type: string
  - Description: Qualitative or quantitative description of stereoselectivity in the reaction.
- enantioselectivity
  - Type: float
  - Description: Enantioselectivity ratio (E-value) indicating preference for one enantiomer over another.
- enantiomeric excess
  - Type: Quantity
  - Description: Enantiomeric excess (ee) as percentage indicating optical purity of the product.
- diastereomeric excess
  - Type: Quantity
  - Description: Diastereomeric excess (de) as percentage for reactions producing diastereomers.
- isomeric content
  - Type: Quantity
  - Description: Content or ratio of specific isomers in the product mixture.
- chemoselectivity
  - Type: string
  - Description: Description of chemoselectivity when multiple reaction pathways are possible.
- regioselectivity
  - Type: string
  - Description: Description of regioselectivity indicating preference for specific reaction sites.
- notes
  - Type: string
  - Description: Additional notes about selectivity measurements.

### Thermodynamic Results

Thermodynamic parameters characterizing the energetics of the enzymatic reaction.

- gibbs free energy change
  - Type: string
  - Description: Gibbs free energy change (ΔG) for the reaction.
- enthalpy change
  - Type: string
  - Description: Enthalpy change (ΔH) for the reaction.
- entropy change
  - Type: string
  - Description: Entropy change (ΔS) for the reaction.
- notes
  - Type: string
  - Description: Additional notes about thermodynamic measurements.

## Enumerations

### Inhibition Type

```python
COMPETITIVE = "competitive"
NONCOMPETITIVE = "non_competitive"
UNCOMPETITIVE = "uncompetitive"
MIXED = "mixed"
IRREVERSIBLE = "irreversible"
OTHER = "other"
```
