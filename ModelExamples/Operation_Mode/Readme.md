[Landing Page](/Readme.md)

# Operation Mode

It is crucial to determine the selected operation mode for an experiment.

<img src="https://github.com/StephanM87/Strenda-biocatalysis/assets/106530250/5e3d4d79-ee59-4c8c-8597-99cd78f276b1" width="550">

<hr>

### Batch

In a batch operation, the entire process occurs in a single closed vessel or batch reactor. All reactants are loaded at the beginning, and the reaction progresses without the addition of additional reactants or removal of products during the course of the reaction.

- __reactor_type__
    - name: string

---

### Fed-Batch

In this mode, reactants are added incrementally during the reaction.

- __reactor_type__
    - name: string

---

### Continuous

In continuous operation, reactants are continuously fed into the reactor, and products are simultaneously removed from it.

- __reactor_type__
    - name: string

---

### CombinatorialMode

A combinatorial mode does not clearly fit into any of the aforementioned subcategories and thus represents a blend of operation modes.

- __reactor_type__
    - name: string

---



