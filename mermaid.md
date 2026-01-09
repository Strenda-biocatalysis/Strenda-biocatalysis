```mermaid
classDiagram
    %% Class definitions with attributes
    class StrendaBiocatalysis {
        +biocatalyst?: Biocatalyst
        +reaction_components?: ReactionComponent
        +operation_mode?: OperationMode
        +reaction_conditions?: ReactionConditions
        +results?: ExperimentalResults
        +sampling?: Sampling
        +vessels_and_mixing?: VesselAndMixing
    }

    class Biocatalyst {
        +identity: BiocatalystIdentity
        +source: BiocatalystSource
        +application: BiocatalystApplication
        +immobilization?: Immobilization
        +storage?: StorageConditions
        +notes[0..*]: string
    }

    class BiocatalystIdentity {
        +name: string
        +ec_number[0..*]: string
        +molecular_weight?: float
        +molecular_weight_unit?: MolecularWeightUnit
        +catalyzed_reaction[0..*]: string
        +sequences?: SequenceInfo
        +origin_organism?: string
        +production_organism?: string
        +posttranslational_modification[0..*]: string
    }

    class SequenceInfo {
        +sequence_amino_acid[0..*]: string
        +sequence_dna[0..*]: string
    }

    class BiocatalystSource {
        +source_type: BiocatalystSourceType
        +supplier?: string
        +purchased_details?: PurchasedDetails
        +self_produced_details?: SelfProducedDetails
    }

    class PurchasedDetails {
        +reference?: string
        +purity?: float
        +purity_specification?: string
        +formulation?: FormulationType
    }

    class SelfProducedDetails {
        +sequence_plasmid[0..*]: string
        +plasmid_specifications[0..*]: string
        +purification_method[0..*]: string
        +purity?: float
        +purity_specification?: string
        +formulation?: FormulationType
    }

    class BiocatalystApplication {
        +application_type: BiocatalystApplicationType
        +concentration[0..*]: Concentration
        +activity[0..*]: Activity
        +workflow_details?: ApplicationWorkflowDetails
    }

    class Concentration {
        +value?: float
        +unit?: UnitDefinition
        +determination_method?: string
    }

    class Activity {
        +value?: float
        +unit?: string
        +determination_method?: string
    }

    class ApplicationWorkflowDetails {
        +cell_disruption_process[0..*]: string
        +harvesting_method[0..*]: string
        +separation_method[0..*]: string
        +source_of_cellfree_extract[0..*]: string
    }

    class Immobilization {
        +immobilized: boolean
        +biocatalyst_state?: string
        +immobilisation_chemistry[0..*]: string
        +carrier_material[0..*]: string
        +linkers[0..*]: string
        +immobilisation_method[0..*]: string
        +purification_method[0..*]: string
        +loading?: Concentration
        +notes[0..*]: string
    }

    class UnitDefinition {
        +id?: string
        +name?: string
        +base_units[0..*]: BaseUnit
    }

    class BaseUnit {
        +kind: UnitType
        +exponent: integer
        +multiplier?: float
        +scale?: float
    }

    class Quantity {
        +value?: float
        +unit?: UnitDefinition
    }

    class StorageConditions {
        +temperature?: float
        +temperature_unit?: UnitDefinition
        +storage_start?: date
        +additives[0..*]: string
        +drying_method[0..*]: string
        +notes[0..*]: string
    }

    class VesselAndMixing {
        +vessel: Vessel
        +mixing?: Mixing
        +notes?: string
    }

    class Vessel {
        +vessel_type: VesselType
        +material?: string
        +size?: Quantity
        +geometry?: string
        +closure?: Closure
        +supplier?: string
        +lot_number?: string
        +reactor_specifics?: ReactorSpecifics
        +notes?: string
    }

    class Closure {
        +closure_type?: string
        +sealing_material?: string
        +notes?: string
    }

    class ReactorSpecifics {
        +gas_handling?: GasHandling
        +tubing?: string
        +catalyst_localisation?: string
        +temperature_control?: string
    }

    class GasHandling {
        +gas_type?: string
        +supply_method?: string
        +supply_rate?: Quantity
    }

    class Mixing {
        +mixing_type: MixingType
        +shaking?: ShakingMixing
        +mechanical?: MechanicalMixing
        +fluid?: FluidImpelledMixing
        +notes?: string
    }

    class ShakingMixing {
        +shaking_type?: string
        +deflection?: Quantity
        +speed?: Quantity
        +vessel_position?: string
        +notes?: string
    }

    class MechanicalMixing {
        +stirring_type?: string
        +stirrer_material?: string
        +supplier?: string
        +number_of_stirrers?: integer
        +stirrer_geometry?: string
        +blade_pitch_angle?: float
        +blade_size?: Quantity
        +stirrer_speed?: Quantity
        +height_above_base?: Quantity
        +power_per_volume?: Quantity
        +stir_bar?: StirBar
        +notes?: string
    }

    class StirBar {
        +size?: Quantity
        +shape?: string
    }

    class FluidImpelledMixing {
        +phase_volume_description?: string
        +residence_time?: Quantity
        +reynolds_number?: string
        +passive_mixing?: string
        +active_mixer?: string
        +pulsing?: string
        +notes?: string
    }

    class ReactionConditions {
        +reactor: ReactorSetup
        +system: ReactionSystem
        +phases[0..*]: Phase
        +temperature?: TemperatureProfile
        +pH?: PHProfile
        +notes?: string
    }

    class ReactorSetup {
        +reactor_type: ReactorType
        +flow?: FlowConditions
        +notes?: string
    }

    class FlowConditions {
        +flow_rate?: float
        +flow_rate_unit?: UnitDefinition
    }

    class ReactionSystem {
        +system_type: SystemType
        +monoliquid?: MonoliquidSystem
        +multiphasic?: MultiphasicSystem
        +notes?: string
    }

    class MonoliquidSystem {
        +solvent_description?: string
        +ionic_strength?: Quantity
        +further_additives?: string
        +notes?: string
    }

    class MultiphasicSystem {
        +phases_number?: integer
        +notes?: string
    }

    class Phase {
        +phase_type: PhaseType
        +material_description?: string
        +amount?: Quantity
        +notes?: string
    }

    class TemperatureProfile {
        +profile_type: ProfileType
        +temperature_unit?: UnitDefinition
        +constant_temperature?: float
        +points[0..*]: ProfilePoint
        +gradient?: Gradient
        +notes?: string
    }

    class ProfilePoint {
        +value?: float
        +time?: float
        +time_unit?: UnitDefinition
        +event_description?: string
    }

    class Gradient {
        +start_value?: float
        +end_value?: float
        +length?: float
        +length_unit?: UnitDefinition
        +measurement_points?: string
    }

    class PHProfile {
        +profile_type: ProfileType
        +constant_pH?: float
        +points[0..*]: PHPoint
        +gradient?: PHGradient
        +detection?: PHDetection
        +notes?: string
    }

    class PHPoint {
        +value?: float
        +time?: float
        +time_unit?: UnitDefinition
        +event_description?: string
    }

    class PHGradient {
        +start_value?: float
        +end_value?: float
        +length?: float
        +length_unit?: UnitDefinition
        +measurement_points?: string
    }

    class PHDetection {
        +detected_when?: string
        +detected_how?: string
        +temperature?: float
        +temperature_unit?: UnitDefinition
        +calibration_pH_electrode?: string
    }

    class OperationMode {
        +mode: OperationModeType
        +reactor_type?: ReactorType
        +feeding?: FeedingStrategy
        +notes?: string
    }

    class FeedingStrategy {
        +feeding_type?: FeedingType
        +description?: string
    }

    class ExperimentalResults {
        +kinetics?: KineticResults
        +yield_and_conversion?: YieldAndConversionResults
        +activity?: ActivityResults
        +selectivity?: SelectivityResults
        +thermodynamics?: ThermodynamicResults
        +notes?: string
    }

    class KineticResults {
        +michaelis_constant?: Quantity
        +maximum_reaction_rate?: Quantity
        +turnover_number?: Quantity
        +catalytic_efficiency?: Quantity
        +dissociation_constant?: Quantity
        +inhibition?: InhibitionParameters
        +hill_coefficient?: float
        +enzyme_stability?: string
        +notes?: string
    }

    class InhibitionParameters {
        +inhibition_type?: InhibitionType
        +inhibition_constant?: Quantity
    }

    class YieldAndConversionResults {
        +yield?: Quantity
        +space_time_yield?: Quantity
        +conversion?: Quantity
        +notes?: string
    }

    class ActivityResults {
        +specific_activity?: Quantity
        +initial_reaction_rate?: Quantity
        +notes?: string
    }

    class SelectivityResults {
        +stereoselectivity?: string
        +enantioselectivity?: float
        +enantiomeric_excess?: Quantity
        +diastereomeric_excess?: Quantity
        +isomeric_content?: Quantity
        +chemoselectivity?: string
        +regioselectivity?: string
        +notes?: string
    }

    class ThermodynamicResults {
        +gibbs_free_energy_change?: string
        +enthalpy_change?: string
        +entropy_change?: string
        +notes?: string
    }

    class ReactionComponent {
        +components[0..*]: Component
    }

    class Component {
        +identity: ComponentIdentity
        +role?: ComponentRole
        +amount?: AmountConcentration
        +provenance?: Provenance
        +solubility?: SolubilityLimit
        +storage?: StorageConditions
        +notes[0..*]: string
    }

    class ComponentIdentity {
        +name: string
        +smiles?: string
        +identifiers[0..*]: string
        +purity?: float
        +formulation?: FormulationType
    }

    class AmountConcentration {
        +value?: float
        +unit?: UnitDefinition
    }

    class Provenance {
        +supplier?: string
    }

    class SolubilityLimit {
        +value?: float
        +unit?: UnitDefinition
    }

    class Sampling {
        +sampling_applied: boolean
        +strategy?: SamplingStrategy
        +samples[0..*]: Sample
        +notes?: string
    }

    class SamplingStrategy {
        +strategy_type: SamplingStrategyType
        +mixing_during_sampling?: string
        +vessel_opened?: boolean
        +gas_phase?: string
        +notes?: string
    }

    class Sample {
        +time?: float
        +time_unit?: UnitDefinition
        +amount?: Quantity
        +phase?: PhaseType
        +biocatalyst_in_sample?: string
        +preprocessing?: SamplePreprocessing
        +notes?: string
    }

    class SamplePreprocessing {
        +quenching_method?: string
        +quenching_ratio?: float
        +treatment_procedure?: string
        +notes?: string
    }

    %% Enum definitions
    class BiocatalystSourceType {
        <<enumeration>>
        PURCHASED
        SELF_PRODUCED
    }

    class BiocatalystApplicationType {
        <<enumeration>>
        CELL_FREE
        CRUDE_CELL_EXTRACT
        PURIFIED
        SECRETED
        WHOLE_CELL
    }

    class MolecularWeightUnit {
        <<enumeration>>
        DA
        KDA
        OTHER
    }

    class UnitType {
        <<enumeration>>
        AMPERE
        AVOGADRO
        BECQUEREL
        CANDELA
        CELSIUS
        COULOMB
        DIMENSIONLESS
        FARAD
        GRAM
        GRAY
        HENRY
        HERTZ
        ITEM
        JOULE
        KATAL
        KELVIN
        KILOGRAM
        LITRE
        LUMEN
        LUX
        METRE
        MOLE
        NEWTON
        OHM
        PASCAL
        RADIAN
        SECOND
        SIEMENS
        SIEVERT
        STERADIAN
        TESLA
        VOLT
        WATT
        WEBER
    }

    class FormulationType {
        <<enumeration>>
        DISSOLVED
        GAS
        LIQUID
        OTHER
        POWDER
        SOLUTION
    }

    class PhaseType {
        <<enumeration>>
        GAS
        LIQUID
        MIXED
        OTHER
        SOLID
    }

    class ReactorType {
        <<enumeration>>
        OTHER
        TUBULAR_FLOW
        WELL_MIXED
    }

    class VesselType {
        <<enumeration>>
        OTHER
        PLATE
        STIRRED_TANK
        TUBULAR_FLOW
        VIAL
    }

    class MixingType {
        <<enumeration>>
        COMBINED
        FLUID_IMPELLED
        MECHANICAL
        NONE
        SHAKING
    }

    class FlowRateUnit {
        <<enumeration>>
        L_PER_MIN
        M3_PER_H
        ML_PER_H
        OTHER
    }

    class SystemType {
        <<enumeration>>
        MONOLIQUID
        MULTIPHASIC
    }

    class ProfileType {
        <<enumeration>>
        CONSTANT
        EVENT_BASED
        GRADIENT
        MULTIPOINT
    }

    class OperationModeType {
        <<enumeration>>
        BATCH
        COMBINATORIAL
        CONTINUOUS
        FED_BATCH
    }

    class FeedingType {
        <<enumeration>>
        CONTINUOUS
        DISCRETE
        NONE
        VARIABLE
    }

    class InhibitionType {
        <<enumeration>>
        COMPETITIVE
        IRREVERSIBLE
        MIXED
        NONCOMPETITIVE
        OTHER
        UNCOMPETITIVE
    }

    class ComponentRole {
        <<enumeration>>
        BUFFER
        COENZYME
        COFACTOR
        COSUBSTRATE
        ION
        OTHER
        SALT
        SOLVENT
        SUBSTRATE
    }

    class SamplingStrategyType {
        <<enumeration>>
        DEFAULT
        SPECIALISED
    }

    %% Relationships
    StrendaBiocatalysis "1" <|-- "1" Biocatalyst
    StrendaBiocatalysis "1" <|-- "1" ReactionComponent
    StrendaBiocatalysis "1" <|-- "1" OperationMode
    StrendaBiocatalysis "1" <|-- "1" ReactionConditions
    StrendaBiocatalysis "1" <|-- "1" ExperimentalResults
    StrendaBiocatalysis "1" <|-- "1" Sampling
    StrendaBiocatalysis "1" <|-- "1" VesselAndMixing
    Biocatalyst "1" <|-- "1" BiocatalystIdentity
    Biocatalyst "1" <|-- "1" BiocatalystSource
    Biocatalyst "1" <|-- "1" BiocatalystApplication
    Biocatalyst "1" <|-- "1" Immobilization
    Biocatalyst "1" <|-- "1" StorageConditions
    BiocatalystIdentity "1" <|-- "1" MolecularWeightUnit
    BiocatalystIdentity "1" <|-- "1" SequenceInfo
    BiocatalystSource "1" <|-- "1" BiocatalystSourceType
    BiocatalystSource "1" <|-- "1" PurchasedDetails
    BiocatalystSource "1" <|-- "1" SelfProducedDetails
    PurchasedDetails "1" <|-- "1" FormulationType
    SelfProducedDetails "1" <|-- "1" FormulationType
    BiocatalystApplication "1" <|-- "1" BiocatalystApplicationType
    BiocatalystApplication "1" <|-- "*" Concentration
    BiocatalystApplication "1" <|-- "*" Activity
    BiocatalystApplication "1" <|-- "1" ApplicationWorkflowDetails
    Concentration "1" <|-- "1" UnitDefinition
    Immobilization "1" <|-- "1" Concentration
    UnitDefinition "1" <|-- "*" BaseUnit
    BaseUnit "1" <|-- "1" UnitType
    Quantity "1" <|-- "1" UnitDefinition
    StorageConditions "1" <|-- "1" UnitDefinition
    VesselAndMixing "1" <|-- "1" Vessel
    VesselAndMixing "1" <|-- "1" Mixing
    Vessel "1" <|-- "1" VesselType
    Vessel "1" <|-- "1" Quantity
    Vessel "1" <|-- "1" Closure
    Vessel "1" <|-- "1" ReactorSpecifics
    ReactorSpecifics "1" <|-- "1" GasHandling
    GasHandling "1" <|-- "1" Quantity
    Mixing "1" <|-- "1" MixingType
    Mixing "1" <|-- "1" ShakingMixing
    Mixing "1" <|-- "1" MechanicalMixing
    Mixing "1" <|-- "1" FluidImpelledMixing
    ShakingMixing "1" <|-- "1" Quantity
    ShakingMixing "1" <|-- "1" Quantity
    MechanicalMixing "1" <|-- "1" Quantity
    MechanicalMixing "1" <|-- "1" Quantity
    MechanicalMixing "1" <|-- "1" Quantity
    MechanicalMixing "1" <|-- "1" Quantity
    MechanicalMixing "1" <|-- "1" StirBar
    StirBar "1" <|-- "1" Quantity
    FluidImpelledMixing "1" <|-- "1" Quantity
    ReactionConditions "1" <|-- "1" ReactorSetup
    ReactionConditions "1" <|-- "1" ReactionSystem
    ReactionConditions "1" <|-- "*" Phase
    ReactionConditions "1" <|-- "1" TemperatureProfile
    ReactionConditions "1" <|-- "1" PHProfile
    ReactorSetup "1" <|-- "1" ReactorType
    ReactorSetup "1" <|-- "1" FlowConditions
    FlowConditions "1" <|-- "1" UnitDefinition
    ReactionSystem "1" <|-- "1" SystemType
    ReactionSystem "1" <|-- "1" MonoliquidSystem
    ReactionSystem "1" <|-- "1" MultiphasicSystem
    MonoliquidSystem "1" <|-- "1" Quantity
    Phase "1" <|-- "1" PhaseType
    Phase "1" <|-- "1" Quantity
    TemperatureProfile "1" <|-- "1" ProfileType
    TemperatureProfile "1" <|-- "1" UnitDefinition
    TemperatureProfile "1" <|-- "*" ProfilePoint
    TemperatureProfile "1" <|-- "1" Gradient
    ProfilePoint "1" <|-- "1" UnitDefinition
    Gradient "1" <|-- "1" UnitDefinition
    PHProfile "1" <|-- "1" ProfileType
    PHProfile "1" <|-- "*" PHPoint
    PHProfile "1" <|-- "1" PHGradient
    PHProfile "1" <|-- "1" PHDetection
    PHPoint "1" <|-- "1" UnitDefinition
    PHGradient "1" <|-- "1" UnitDefinition
    PHDetection "1" <|-- "1" UnitDefinition
    OperationMode "1" <|-- "1" OperationModeType
    OperationMode "1" <|-- "1" ReactorType
    OperationMode "1" <|-- "1" FeedingStrategy
    FeedingStrategy "1" <|-- "1" FeedingType
    ExperimentalResults "1" <|-- "1" KineticResults
    ExperimentalResults "1" <|-- "1" YieldAndConversionResults
    ExperimentalResults "1" <|-- "1" ActivityResults
    ExperimentalResults "1" <|-- "1" SelectivityResults
    ExperimentalResults "1" <|-- "1" ThermodynamicResults
    KineticResults "1" <|-- "1" Quantity
    KineticResults "1" <|-- "1" Quantity
    KineticResults "1" <|-- "1" Quantity
    KineticResults "1" <|-- "1" Quantity
    KineticResults "1" <|-- "1" Quantity
    KineticResults "1" <|-- "1" InhibitionParameters
    InhibitionParameters "1" <|-- "1" InhibitionType
    InhibitionParameters "1" <|-- "1" Quantity
    YieldAndConversionResults "1" <|-- "1" Quantity
    YieldAndConversionResults "1" <|-- "1" Quantity
    YieldAndConversionResults "1" <|-- "1" Quantity
    ActivityResults "1" <|-- "1" Quantity
    ActivityResults "1" <|-- "1" Quantity
    SelectivityResults "1" <|-- "1" Quantity
    SelectivityResults "1" <|-- "1" Quantity
    SelectivityResults "1" <|-- "1" Quantity
    ReactionComponent "1" <|-- "*" Component
    Component "1" <|-- "1" ComponentIdentity
    Component "1" <|-- "1" ComponentRole
    Component "1" <|-- "1" AmountConcentration
    Component "1" <|-- "1" Provenance
    Component "1" <|-- "1" SolubilityLimit
    Component "1" <|-- "1" StorageConditions
    ComponentIdentity "1" <|-- "1" FormulationType
    AmountConcentration "1" <|-- "1" UnitDefinition
    SolubilityLimit "1" <|-- "1" UnitDefinition
    Sampling "1" <|-- "1" SamplingStrategy
    Sampling "1" <|-- "*" Sample
    SamplingStrategy "1" <|-- "1" SamplingStrategyType
    Sample "1" <|-- "1" UnitDefinition
    Sample "1" <|-- "1" Quantity
    Sample "1" <|-- "1" PhaseType
    Sample "1" <|-- "1" SamplePreprocessing
```