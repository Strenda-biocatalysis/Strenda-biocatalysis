```mermaid
classDiagram
    BiocatalystBase <-- SolubleBiocatalyst
    
    class BiocatalystBase {
        +string name*
        +string ecnumber
    }
    
    class SolubleBiocatalyst {
        +posfloat concentration*
        +string concentration_det_method*
    }
    
```