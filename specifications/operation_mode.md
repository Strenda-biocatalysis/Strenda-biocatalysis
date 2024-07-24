---
repo: "https://www.github.com/my/repo/"
prefix: "stbc"
---

[Landing Page](/Readme.md)

<div align="justify">

# Operation Mode

The careful selection of the appropriate operation mode at the beginning of the experimental planning is crucial, as it significantly influences reaction conditions, reaction kinetics, and ultimately, product quality. Considering parameters such as substrate concentration, reaction time, and temperature within the respective mode allows for optimal reaction control, directly impacting the process efficiency and purity of the final product. Furthermore, choosing a scalable mode not only facilitates potential upscaling of the reaction but also streamlines resource management, contributing to overall process efficiency.

<img src="https://github.com/StephanM87/Strenda-biocatalysis/assets/106530250/4cd798dc-7ee3-4600-b163-3159cea5c2f7" width="550">


<hr>

### Batch

The batch operation mode represents a fundamental approach in biocatalysis, where all reaction components are mixed simultaneously within a closed system, and the reaction proceeds until a predetermined endpoint is reached. This mode is easy to control and well-suited for producing small batches of products.

- __reactor_type__
    - Type: string

---

### FedBatch

In the fed-batch operation mode, additional compounds (e.g., substrates, acid/base for pH regulation, etc.) are gradually added during the reaction to control reaction conditions or enhance product formation. This mode allows for better control of the reaction progress and can increase productivity.

- __reactor_type__
    - Type: string

---

### Continuous

In the continuous operation mode, the reaction operates continuously with substrates continuously supplied and products continuously removed. This mode enables uniform product formation and is particularly suitable for large-scale production.

- __reactor_type__
    - Type: string

---

### CombinatorialMode

A combinatorial mode does not clearly fit into any of the aforementioned subcategories and thus represents a mixture of operation modes. This kind of experiment design could be used to systematically explore various reaction conditions or components in a combined manner. This approach allows the exploration of multiple options, such as varying substrate concentrations, catalysts, or reaction conditions. The goal is to identify the optimal conditions or combinations that most efficiently facilitate desired reactions in biocatalysis.

- __reactor_type__
    - Type: string

---


</div>
