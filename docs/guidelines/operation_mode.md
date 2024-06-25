# Operation Mode

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        batch(Batch)
        fedbatch(FedBatch)
        continuous(Continuous)
        combinatorialmode(CombinatorialMode)

        click batch "#batch" "Go to Batch"
        click fedbatch "#fedbatch" "Go to FedBatch"
        click continuous "#continuous" "Go to Continuous"
        click combinatorialmode "#combinatorialmode" "Go to CombinatorialMode"
    ```


## Types


### Batch
The batch operation mode represents a fundamental approach in biocatalysis, where all reaction components are mixed simultaneously within a closed system, and the reaction proceeds until a predetermined endpoint is reached. This mode is easy to control and well-suited for producing small batches of products.

__reactor_type__* `string`


------

### FedBatch
In the fed-batch operation mode, additional compounds (e.g., substrates, acid/base for pH regulation, etc.) are gradually added during the reaction to control reaction conditions or enhance product formation. This mode allows for better control of the reaction progress and can increase productivity.

__reactor_type__* `string`


------

### Continuous
In the continuous operation mode, the reaction operates continuously with substrates continuously supplied and products continuously removed. This mode enables uniform product formation and is particularly suitable for large-scale production.

__reactor_type__* `string`


------

### CombinatorialMode
A combinatorial mode does not clearly fit into any of the aforementioned subcategories and thus represents a mixture of operation modes. This kind of experiment design could be used to systematically explore various reaction conditions or components in a combined manner. This approach allows the exploration of multiple options, such as varying substrate concentrations, catalysts, or reaction conditions. The goal is to identify the optimal conditions or combinations that most efficiently facilitate desired reactions in biocatalysis.

__reactor_type__* `string`