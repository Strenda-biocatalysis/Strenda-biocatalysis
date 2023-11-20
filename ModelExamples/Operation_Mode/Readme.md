[Landing Page](/Readme.md)

<div align="justify">

# Operation Mode

The careful selection of the appropriate operation mode at the beginning of experiment planning is crucial, as it significantly influences reaction conditions, reaction kinetics, and ultimately, product quality. Considering parameters such as substrate concentrations, reaction times, and temperature within the relevant mode allows for optimal reaction control, directly impacting the efficiency and purity of the final product. Furthermore, choosing a scalable mode not only facilitates potential upscaling of the reaction but also streamlines resource management, contributing to overall process efficiency.

<img src="https://github.com/StephanM87/Strenda-biocatalysis/assets/106530250/9bb7fab2-8778-4a34-9843-1bc1c194de3a" width="550">

<hr>

### Batch

In a batch operation, the entire process occurs in a single closed vessel or batch reactor. All reactants are loaded at the beginning, and the reaction progresses without the addition of additional reactants or removal of products during the course of the reaction.

- __reactor_type__
    - Type: string

---

### Fed-Batch

In this mode, reactants are added incrementally during the reaction.

- __reactor_type__
    - Type: string

---

### Continuous

In continuous operation, reactants are continuously fed into the reactor, and products are simultaneously removed from it.

- __reactor_type__
    - Type: string

---

### CombinatorialMode

A combinatorial mode does not clearly fit into any of the aforementioned subcategories and thus represents a blend of operation modes.

- __reactor_type__
    - Type: string

---


</div>
