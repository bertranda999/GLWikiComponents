import json

DEFAULT = "Default"
RESEARCHED = "Research"
ARTIFACT = "Artifact: "
CORRUPTION_MARKET = "Corruption Market"
ULDRI_MARKET = "Uldrinan Market"
RAIX_MARKET = "Raix Market"
MISSION_MARKET = "Mission Market"
PRISMODYNE_MARKET = "Prismodyne Energy Network"
AEON_MARKET = "Aeon Market"
BAINAR_NODES = "Bainar, Systems Cracker"
PRISMATIC_DOMAIN = "Prismatic Transcendance#Prismatic Domain Ability"
BATTLE_MARKET = "Battle Market"
GP_MARKET = "Artifact Market"

RANDOM_PLACEMENT_NOTE = 1
RANDOM_VERSION_NOTE = 2
BAHREEN_DOMAIN_NOTE = 3
PREJORAN_BARRIER_NOTE = 4
BIOSHIP_PLATFORM_NOTE = 5
LOCK_NOTE = 6
XC1_NOTE = 7
GENOLINK_NOTE = 8
SHIP_SIZE_NOTE = 9
RAIX_BUNKER_NOTE = 10
MORPHO_INHIBITOR_NOTE = 11
UNOBTAINABLE_NOTE = 12
SPIRE_NOTE = 13
SHADIN_STRUCTURE_NOTE = 14
STRYLL_INTERROGATION_LIMIT = 15
BANE_HALL_LIMIT = 16

class Structure:
    def __init__(self, name: str, size: int, limit: int, limited: bool, extract: bool, nameAdd: str = "", mp: int = 0, mpp: int = 0, mps: int = 0, ap: int = 0, app: int = 0, aps: int = 0, rp: int = 0, rpp: int = 0, rps: int = 0, ip: int = 0,
                 ipp: int = 0, ips: int = 0, d: int = 0, dp: int = 0, at: int = 0, atp: int = 0, c: int = 0, cp: int = 0, p: int = 0, pp: int = 0, id: int = 0, esp: int = 0, ic: int = 0, acq: str = "",
                 nameNotes: list[int] = [], cloakNotes: list[int] = [], limitNotes: list[int] = [], defenseNotes: list[int] = [], alternatePageName: str = "", formDescription: str = ""):
        self.name = name
        self. size = size
        self.limit = limit
        self.limited = limited
        self.extract = extract
        self.nameAdd = nameAdd
        self.mp = mp
        self.mpp = mpp
        self.mps = mps
        self.ap = ap
        self.app = app
        self.aps = aps
        self.rp = rp
        self.rpp = rpp
        self.rps = rps
        self.ip = ip
        self.ipp = ipp
        self.ips = ips
        self.d = d
        self.dp = dp
        self.at = at
        self.atp = atp
        self.c = c
        self.cp = cp
        self.p = p
        self.pp = pp
        self.id = id
        self.esp = esp
        self.ic = ic
        self.acq = acq
        self.nameNotes = nameNotes
        self.cloakNotes = cloakNotes
        self.limitNotes = limitNotes
        self.defenseNotes = defenseNotes
        self.alternatePageName = alternatePageName
        self.formDescription = formDescription
        self.ability = None

    def addAbility(self, ability):
        self.ability = ability

def fromBlueprint(blueprintName: str):
    #return "Blueprint: [[" + blueprintName + "]]"
    #return "[[" + blueprintName + "]]"
    return "[[" + blueprintName + "|Blueprint]]"

def ability(abilityName: str):
    #return "Placed using the [[" + abilityName + "]] ability"
    #return "[[" + abilityName + "]]"
    return "[[" + abilityName + "|Ability]]"

def mission(name: str):
    #return "[[" + name + "]]"
    return "[[" + name + "|Mission]]"

def structurePlacement(name: str):
    #return "[[" + name + "]]"
    return "[[" + name + "|Structure]]"

def market(name: str):
    return "[[" + name + "|Market]]"

def lm(name: str):
    return "[[" + name + "|Legion Mission]]"

def dr():
    return "[[Daily Reward]]"

def sb():
    return "[[Supporter Bonus]]"

def zone(name: str):
    return "[[" + name + "|Influence Zone]]"

def scanning(name: str):
    return "[[" + name + "|Scanning]]"

def baseCrate():
    return "[[Base_Combat#Base_Crates|Base Crates]]"

def common():
    return "[[Artifacts#Common_Artifacts|Standard]]" + market(GP_MARKET)

def evo():
    return "[[Evolution Trees]]"

def medal():
    return "[[Medals]]"

def npc(name: str):
    return "[[" + name + "|NPC]]"

def blockade(name: str):
    return "[[" + name + "|Blockade]]"

def ct():
    return "[[Collective Theory Lab]]"

def event():
    return "[[Planetary Events]]"

structures: list[Structure] = [
    Structure("Surface Mine", 4, 0, False, False, mp=1, acq=DEFAULT),
    Structure("Extraction Drones", 7, 0, False, False, mp=2, acq=RESEARCHED),
    Structure("Nanite Disassemblers", 9, 0, False, False, mp=3, acq=RESEARCHED),
    Structure("Deep Core Mine", 11, 0, False, False, mp=4, acq=RESEARCHED),
    Structure("Mesh Extractor", 13, 0, False, False, mp=5, acq=RESEARCHED),
    Structure("Quantum Reassembler", 15, 0, False, False, mp=6, acq=RESEARCHED),
    Structure("Gravitonic Teleporter", 16, 0, False, False, mp=8, acq=RESEARCHED),
    Structure("Stellar Converter", 17, 0, False, False, mp=10, acq=RESEARCHED),
    Structure("Star Lifter", 18, 0, False, False, mp=12, acq=RESEARCHED),
    Structure("Proto-Matter Extractor", 19, 0, False, False, mp=16, acq=RESEARCHED),
    Structure("Surface Scanner", 4, 0, False, False, ap=1, acq=DEFAULT),
    Structure("Analyzer Drones", 7, 0, False, False, ap=2, acq=RESEARCHED),
    Structure("Subterranean Probes", 9, 0, False, False, ap=3, acq=RESEARCHED),
    Structure("Deep Scan Harmonizer", 11, 0, False, False, ap=4, acq=RESEARCHED),
    Structure("Mesh Probes", 13, 0, False, False, ap=5, acq=RESEARCHED),
    Structure("Quantum Analyzer Engine", 15, 0, False, False, ap=6, acq=RESEARCHED),
    Structure("Gravitonic Revealer", 16, 0, False, False, ap=8, acq=RESEARCHED),
    Structure("Stellar Replicator", 17, 0, False, False, ap=10, acq=RESEARCHED),
    Structure("Hyperforge Fabricator", 18, 0, False, False, ap=12, acq=RESEARCHED),
    Structure("Proto-Matter Synthesizer", 19, 0, False, False, ap=16, acq=RESEARCHED),
    Structure("Research Station", 4, 0, False, False, rp=1, acq=DEFAULT),
    Structure("Robotics Lab", 7, 0, False, False, rp=2, acq=RESEARCHED),
    Structure("Nanite Lab", 9, 0, False, False, rp=3, acq=RESEARCHED),
    Structure("Theory Engine", 11, 0, False, False, rp=4, acq=RESEARCHED),
    Structure("AI Network", 13, 0, False, False, rp=5, acq=RESEARCHED),
    Structure("Quantum Computer Grid", 15, 0, False, False, rp=6, acq=RESEARCHED),
    Structure("Gravshell Brain", 16, 0, False, False, rp=8, acq=RESEARCHED),
    Structure("Matrioshka Brain", 17, 0, False, False, rp=10, acq=RESEARCHED),
    Structure("Hypernode Brain", 18, 0, False, False, rp=12, acq=RESEARCHED),
    Structure("Proto-Matter Cognitor", 19, 0, False, False, rp=16, acq=RESEARCHED),
    Structure("Surface Bunkers", 2, 0, False, False, d=25, acq=DEFAULT),
    Structure("Structural Shield", 2, 0, False, False, d=50, acq=RESEARCHED),
    Structure("City Shield", 2, 0, False, False, d=100, acq=RESEARCHED),
    Structure("Regional Shield", 2, 0, False, False, d=200, acq=RESEARCHED),
    Structure("Mass Shield", 2, 0, False, False, d=450, acq=RESEARCHED),
    Structure("Structural Shield", 2, 0, False, False, d=750, acq=RESEARCHED),
    Structure("Obviation Barrier", 2, 0, False, False, d=1200, acq=RESEARCHED),
    Structure("Orbital Minefield", 2, 0, False, False, at=25, acq=DEFAULT),
    Structure("Ion Minefield", 2, 0, False, False, at=50, acq=RESEARCHED),
    Structure("Plasma Minefield", 2, 0, False, False, at=75, acq=RESEARCHED),
    Structure("Graviton Minefield", 2, 0, False, False, at=150, acq=RESEARCHED),
    Structure("Disruption Minefield", 2, 0, False, False, at=200, acq=RESEARCHED),
    Structure("Quantum Minefield", 2, 0, False, False, at=300, acq=RESEARCHED),
    Structure("Singularity Minefield", 2, 0, False, False, at=450, acq=RESEARCHED),
    Structure("Antimatter Minefield", 2, 0, False, False, at=600, acq=RESEARCHED),
    Structure("Null Minefield", 2, 0, False, False, at=750, acq=RESEARCHED),
    Structure("Thetacron Rift Field", 2, 0, False, False, at=1000, acq=RESEARCHED),
    Structure("Quasi-Chaos Minefield", 2, 0, False, False, at=1200, acq=RESEARCHED),
    Structure("Jammer Satellites", 2, 0, False, False, c=25, acq=RESEARCHED),
    Structure("Shroud Satellites", 3, 0, False, False, c=75, acq=RESEARCHED),
    Structure("Stealth Satellites", 4, 0, False, False, c=150, acq=RESEARCHED),
    Structure("Cloaking Satellites", 5, 0, False, False, c=250, acq=RESEARCHED),
    Structure("Anti-Tachyon Satellites", 6, 0, False, False, c=500, acq=RESEARCHED),
    Structure("Inverse-Flux Satellites", 7, 0, False, False, c=800, acq=RESEARCHED),
    Structure("Habitation Modules", 2, 0, False, False, p=20, acq=RESEARCHED),
    Structure("Arcology", 2, 0, False, False, p=75, acq=RESEARCHED),
    Structure("Hypersphere Habitat", 3, 0, False, False, p=200, acq=RESEARCHED),
    Structure("Astrocore Habitat", 4, 0, False, False, p=400, acq=RESEARCHED),
    Structure("Trans-Hub Habitat", 5, 0, False, False, p=650, acq=RESEARCHED),
    Structure("Topopolis", 6, 0, False, False, p=1000, acq=RESEARCHED),
    Structure("Sulcation Portal", 2, 1, False, False, mp=2, p=200, acq=mission("Portal Prototypes"), alternatePageName="Sulcation Portal Blueprints"),
    Structure("Exotic Lab", 1, 1, False, False, rp=1, acq=mission("Exotic Innovation"), alternatePageName="Exotic Lab Blueprints"),
    Structure("Exotic Barrier", 2, 2, False, False, d=250, acq=mission("Exotic Revelations"), alternatePageName="Exotic Barrier Blueprints"),
    Structure("Exotic Turret", 2, 2, False, False, at=250, acq=mission("Exotic Endeavours"), alternatePageName="Exotic Turret Blueprints"),
    Structure("Prejoran Slave Barrier", 20, 0, False, False, d=6000, acq=("Slaves to the Cause"), alternatePageName="Prejoran Slave Barrier Blueprint", nameNotes=[PREJORAN_BARRIER_NOTE]),
    Structure("Anti-Resistance Base", 3, 0, False, False, d=200, c=100, acq=mission("Attack on the Resistance"), alternatePageName="Anti-Resistance Base Blueprints"),
    Structure("Exo-Pulse Disruptor", 1, 2, False, False, mp=2, atp=22, c=1222, acq=mission("Exotic Disruptions"), alternatePageName="Exo-Pulse Disruptor Blueprint"),
    Structure("Exo-Wave Generator", 2, 2, False, False, mpp=2, ap=2, app=2, rp=4, rpp=2, ipp=2, acq=mission("Exotic Realities"), alternatePageName="Exo-Wave Generator Blueprint"),
    Structure("Exo-Rift Membrane Blueprint", 2, 2, False, False, ap=4, dp=33, cp=12, acq=mission("Exotic Isolations"), alternatePageName="Exo-Rift Membrane Blueprint"),
    Structure("Entropy Repulsor Pylon", 2, -1, False, False, mpp=4, ap=3, c=800, esp=250, acq=mission("Neutronic Principles"), alternatePageName="Entropy Repulsor Pylon Blueprint"),
    Structure("Council Base", 2, 1, False, False, p=100, id=500, acq="Mission Tiers"),
    Structure("Soldier Outpost", 2, 0, False, False, id=300, acq="Mission Tiers"),
    Structure("Phase Cutter", 1, 2, False, True, mp=1, at=100, acq=common(), alternatePageName="Phase Cutter Chassis"),
    Structure("Processing Core", 1, 1, False, True, mp=1, ap=1, acq=common(), alternatePageName="Processing Core Chassis"),
    Structure("Refining Lab", 1, 1, False, True, mp=1, rp=1, acq=common(), alternatePageName="Refining Lab Chassis"),
    Structure("Relay Tower", 1, 1, False, True, ap=1, rp=1, acq=common(), alternatePageName="Relay Tower Chassis"),
    Structure("Space Elevator", 1, 2, False, True, ap=1, p=50, acq=common(), alternatePageName="Space Elevator Chassis"),
    Structure("Spy Uplink", 1,2, False, True, rp=1, c=40, acq=common(), alternatePageName="Spy Uplink Chassis"),
    Structure("Warp Gate", 1, 1, False, True, mp=1, ap=1, rp=1, acq=common(), alternatePageName="Warp Gate Chassis"),
    Structure("Omnibase", 5, 1, True, True, mp=3, ap=3, rp=3, d=1000, at=1000, acq="Mission Tiers"),
    Structure("M.O.T.H.E.R.", 2, 1, True, True, p=250, acq=dr(), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("M.O.T.H.E.R. 2.0", 1, 1, True, True, d=200, p=400, acq=dr(), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Caretaker's Villa", 1, 1, False, False, mp=1, mpp=1, ap=1, app=1, rp=1, rpp=1, ipp=1, acq=sb()),
    Structure("Conductor's Villa", 1, 1, False, False, mp=3, ap=1, rp=2, acq=sb()),
    Structure("Custodian's Villa", 1, 1, False, False, mpp=3, app=3, rpp=3, ipp=3, acq=sb()),
    Structure("Diplomat's Villa", 1, 1, False, False, rp=2, ip=1, ipp=2, acq=sb()),
    Structure("Guardian's Villa", 1, 1, False, False, ap=1, rp=2, cp=22, acq=sb()),
    Structure("Overseer's Villa", 1, 1, False, False, mp=2, rp=3, dp=30, acq=sb()),
    Structure("Steward's Villa", 1, 1, False, False, ap=2, app=2, acq=sb()),
    Structure("Litheor Deep-Phase Probe", 1, 2, False, False, mp=2, ap=2, rp=2, c=150, p=900, acq=ability("Deep-Phase Probe")),
    Structure("Litheor Deep-Phase Sanctuary", 1, 2, False, False, mp=4, ap=4, rp=4, ip=1, c=300, p=1800, acq=ability("Deep-Phase Probe")),
    Structure("Ring of Ascendance", 1, 1, False, False, mp=3, mpp=3, ap=1, app=3, rp=3, rpp=3, ipp=3, dp=30, atp=30, p=3000, acq=ability("Drone Ascent")),
    Structure("Bainar", 1, 1, False, False, "A-Node - Basic", ap=1, acq=ability("Core Access"), nameNotes=[RANDOM_VERSION_NOTE], alternatePageName=BAINAR_NODES),
    Structure("Bainar", 1, 1, False, False, "A-Node - Advanced", ap=2, acq=ability("Core Access"), nameNotes=[RANDOM_VERSION_NOTE], alternatePageName=BAINAR_NODES),
    Structure("Bainar", 1, 1, False, False, "A-Node - Prime", ap=3, acq=ability("Core Access"), nameNotes=[RANDOM_VERSION_NOTE], alternatePageName=BAINAR_NODES),
    Structure("Bainar", 1, 1, False, False, "M-Node - Basic", mp=1, acq=ability("Core Access"), nameNotes=[RANDOM_VERSION_NOTE], alternatePageName=BAINAR_NODES),
    Structure("Bainar", 1, 1, False, False, "M-Node - Advanced", mp=2, acq=ability("Core Access"), nameNotes=[RANDOM_VERSION_NOTE], alternatePageName=BAINAR_NODES),
    Structure("Bainar", 1, 1, False, False, "M-Node - Prime", mp=3, acq=ability("Core Access"), nameNotes=[RANDOM_VERSION_NOTE], alternatePageName=BAINAR_NODES),
    Structure("Bainar", 1, 1, False, False, "R-Node - Basic", rp=1, acq=ability("Core Access"), nameNotes=[RANDOM_VERSION_NOTE], alternatePageName=BAINAR_NODES),
    Structure("Bainar", 1, 1, False, False, "R-Node - Advanced", rp=2, acq=ability("Core Access"), nameNotes=[RANDOM_VERSION_NOTE], alternatePageName=BAINAR_NODES),
    Structure("Bainar", 1, 1, False, False, "R-Node - Prime", rp=3, acq=ability("Core Access"), nameNotes=[RANDOM_VERSION_NOTE], alternatePageName=BAINAR_NODES),
    Structure("Bainar", 1, 1, False, False, "X-Node", mp=1, ap=1, rp=1, acq=ability("Core Access"), nameNotes=[RANDOM_VERSION_NOTE], alternatePageName=BAINAR_NODES),
    Structure("Galaxy Overseers", 0, 8, False, False, mp=1, acq=ability("Prismatic Domain"), limitNotes=[BAHREEN_DOMAIN_NOTE], nameNotes=[RANDOM_PLACEMENT_NOTE, RANDOM_VERSION_NOTE], alternatePageName=PRISMATIC_DOMAIN),
    Structure("Galaxy Elitists", 0, 8, False, False, ap=1, acq=ability("Prismatic Domain"), limitNotes=[BAHREEN_DOMAIN_NOTE], nameNotes=[RANDOM_PLACEMENT_NOTE, RANDOM_VERSION_NOTE], alternatePageName=PRISMATIC_DOMAIN),
    Structure("Galaxy Technocrats", 0, 8, False, False, rp=1, acq=ability("Prismatic Domain"), limitNotes=[BAHREEN_DOMAIN_NOTE], nameNotes=[RANDOM_PLACEMENT_NOTE, RANDOM_VERSION_NOTE], alternatePageName=PRISMATIC_DOMAIN),
    Structure("Galaxy Inquisitors", 0, 8, False, False, c=100, acq=ability("Prismatic Domain"), limitNotes=[BAHREEN_DOMAIN_NOTE], nameNotes=[RANDOM_PLACEMENT_NOTE, RANDOM_VERSION_NOTE], alternatePageName=PRISMATIC_DOMAIN),
    Structure("Tranquil Monolith", 1, 1, False, False, mp=2, ap=2, cp=5, acq=ability("Transcendent Focus")),
    Structure("Tranquil Monolith", 1, 1, False, False, "(10%)", mp=2, ap=2, cp=10, acq=ability("Transcendent Focus")),
    Structure("Tranquil Monolith", 1, 1, False, False, "(15%)", mp=2, ap=2, cp=15, acq=ability("Transcendent Focus")),
    Structure("Tranquil Monolith", 1, 1, False, False, "(20%)", mp=2, ap=2, cp=20, acq=ability("Transcendent Focus")),
    Structure("Tranquil Monolith", 1, 1, False, False, "(25%)", mp=2, ap=2, cp=25, acq=ability("Transcendent Focus")),
    Structure("Tranquil Monolith", 1, 1, False, False, "(30%)", mp=2, ap=2, cp=30, acq=ability("Transcendent Focus")),
    Structure("Tranquil Monolith", 1, 1, False, False, "(35%)", mp=2, ap=2, cp=35, acq=ability("Transcendent Focus")),
    Structure("Tranquil Monolith", 1, 1, False, False, "(40%)", mp=2, ap=2, cp=40, acq=ability("Transcendent Focus")),
    Structure("Tranquil Monolith", 1, 1, False, False, "(45%)", mp=2, ap=2, cp=45, acq=ability("Transcendent Focus")),
    Structure("Tranquil Monolith", 1, 1, False, False, "(50%)", mp=2, ap=2, cp=50, acq=ability("Transcendent Focus")),
    Structure("Bahreen Duodecix", 1, 2, False, False, "(1)", mp=1, ap=6, rp=1, acq=ability("Bahreen Duodecix"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Bahreen Duodecix", 1, 2, False, False, "(2)", mp=2, ap=5, rp=2, acq=ability("Bahreen Duodecix"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Bahreen Duodecix", 1, 2, False, False, "(3)", mp=2, ap=4, rp=2, acq=ability("Bahreen Duodecix"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Bahreen Duodecix", 1, 2, False, False, "(4)", mp=2, ap=3, rp=2, acq=ability("Bahreen Duodecix"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Bahreen Duodecix", 1, 2, False, False, "(5)", mp=4, ap=2, rp=4, acq=ability("Bahreen Duodecix"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Bahreen Duodecix", 1, 2, False, False, "(6)", mp=3, ap=2, rp=3, acq=ability("Bahreen Duodecix"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Bahreen Duodecix", 1, 2, False, False, "(7)", mp=2, ap=2, rp=2, acq=ability("Bahreen Duodecix"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Bralkir Altar", 1, 1, False, False, mp=1, ap=1, rp=1, id=2500, acq=ability("Mercenary Call")),
    Structure("Shrine of B'elna", 1, 1, False, False, ap=1, app=2, c=300, acq=ability("Mercenary Call")),
    Structure("Xephius Portal", 1, 1, False, False, mp=3, ap=1, c=404, cp=6, acq=ability("Xephius, Aeon Portalier"), alternatePageName="Xephius, Aeon Portalier"),
    Structure("Thavix Reactor", 1, 1, False, False, mp=5, ap=2, rp=4, acq=ability("Evolution Trees: Lazuli"), alternatePageName="Evolution Trees: Lazuli"),
    Structure("Caustic Pit-Spire", 1, 1, False, False, mp=3, mpp=3, mps=360, ip=1, acq=ability("Caustic Pit-Spire")),
    Structure("Uldri Spacial Mega-Folder", 1, 1, False, False, mp=2, ap=2, rp=3, c=600, acq=ability("Evolution Trees: Uldrinan"), alternatePageName="Evolution Trees: Uldrinan"),
    Structure("Uldri Spacial Mega-Crystal Field", 1, 1, False, False, mpp=7, app=7, rpp=7, ipp=7, d=1000, acq=ability("Evolution Trees: Uldrinan"), alternatePageName="Evolution Trees: Uldrinan"),
    Structure("Uldri Power Mega-Node", 1, 1, False, False, app=7, rp=2, acq=ability("Evolution Trees: Uldrinan"), alternatePageName="Evolution Trees: Uldrinan"),
    Structure("Ancestral Gene-Bank", 1, 1, False, False, ap=1, rp=2, rps=2200, ip=1, acq=ability("Evolution Trees")),
    Structure("Ancestral Gene-Bank", 1, 1, False, False, "v2", ap=2, rp=2, rps=3200, ip=1, ips=150, acq=ability("Evolution Trees")),
    Structure("Ancestral Gene-Bank", 1, 1, False, False, "v3", ap=3, rp=2, rps=4200, ip=2, ips=150, acq=ability("Evolution Trees")),
    Structure("Ancestral Gene-Bank", 1, 1, False, False, "v4", ap=4, rp=2, rps=5200, ip=3, ips=300, acq=ability("Evolution Trees")),
    Structure("Prejor Beacon Jammer", 1, 3, True, True, c=75, acq=mission("The Beacon Search")),
    Structure("Intraphasic Hoveroid", 1, 1, True, True, mpp=5, app=5, rpp=5, ipp=5, acq=mission("Unfamiliar Remnants")),
    Structure("Trellith Comm Relay", 1, 1, True, False, ap=2, rp=2, acq=mission("The Trellith Emergence"), alternatePageName="Relay Tower Chassis", formDescription="Upgrade with [[Trellith Comm Relay Upgrade]]:"),
    Structure("Symbiont Test Lab", 1, 1, True, False, mp=2, rp=2, pp=20, acq=mission("The Trellith Symbiosis"), alternatePageName="Processing Core Chassis", formDescription="Upgrade with [[Symbiont Test Lab Upgrade]]:"),
    Structure("Crimson Phase Launcher", 1, 2, True, True, at=250, acq=mission("Crimson Confrontation")),
    Structure("Captured Crimson Base", 5, 1, True, True, mp=2, ap=2, rp=2, d=250, at=250, acq=mission("Crimson Operations")),
    Structure("Void Barrier", 1, 1, False, True, c=110, acq=mission("Darkness Falls"), alternatePageName="Void Barrier Chassis"),
    Structure("Void-Field Enclave", 1, 1, True, False, mp=1, ap=1, rp=3, c=808, acq=mission("Darkness Surrounds")),
    Structure("Void-Field Enclave", 1, 1, True, False, "(Doubled)", mp=2, ap=2, rp=6, c=1616, acq=mission("Darkness Surrounds")),
    Structure("Void-Field Enclave", 1, 1, True, False, "(Tripled)", mp=3, ap=3, rp=9, c=2424, acq=mission("Darkness Surrounds")),
    Structure("T.O. Grid Barrier", 1, 2, True, True, d=400, acq=mission("\'Restructuring\' the Council")),
    Structure("Bioship Landing Platform", 1, 1, True, True, p=200, acq=mission("Imminent Conflict"), cloakNotes=[BIOSHIP_PLATFORM_NOTE]),
    Structure("Bioship Gene Lab", 1, 1, True, True, "(AR)", ap=1, rp=2, p=200, acq=mission("Uncertain Opportunity")),
    Structure("Bioship Gene Lab", 1, 1, True, True, "(R)", rp=2, p=200, acq=mission("Imminent Conflict")),
    Structure("Voliir Transgenic Lock", 2, 1, True, True, mp=1, ap=1, rp=2, acq=mission("Delivering the Treatment"), limitNotes=[LOCK_NOTE]),
    Structure("Stryll Bioresearch Bay", 1, 1, True, False, ap=2, rp=4, pp=25, acq=mission("Unexpected Ties")),
    Structure("Stryll Bioresearch Bay", 1, 1, True, False, "(Upgraded)", ap=4, rp=4, pp=25, acq=mission("Unexpected Ties"), formDescription="If you are a Biologist when this is FIRST built, it also provides double the artifact bonus"),
    Structure("XC1 Transport Probe", 1, 1, True, False, mp=3, ap=2, acq=mission("Intercepted Tarriance"), cloakNotes=[XC1_NOTE]),
    Structure("Terran-Stryll Interrogation Cell", 1, 1, True, False, ap=1, rp=1, rpp=6, acq=mission("Sileena's Signal")),
    Structure("Terran-Stryll Interrogation Cell", 1, 1, True, False, "(Upgraded)", ap=2, rp=2, rpp=12, acq=mission("Sileena's Signal"), formDescription="If this structure is built on a planet that has 5 or more T.O. and/or Stryll structures, the structure's bonuses double."),
    Structure("Strazi Genolink Probe", 1, 1, True, False, mp=3, mpp=5, ap=1, acq=mission("The Vvarix Truth"), nameNotes=[GENOLINK_NOTE]),
    Structure("Strazi Link Anchor", 0, 0, True, False, "(1)", ap=1, c=110, acq=structurePlacement("Strazi Genolink Probe"), nameNotes=[RANDOM_PLACEMENT_NOTE, RANDOM_VERSION_NOTE]),
    Structure("Strazi Link Anchor", 0, 0, True, False, "(2)", ap=1, rp=1, acq=structurePlacement("Strazi Genolink Probe"), nameNotes=[RANDOM_PLACEMENT_NOTE, RANDOM_VERSION_NOTE]),
    Structure("Strazi Link Anchor", 0, 0, True, False, "(3)", mp=1, ap=1, acq=structurePlacement("Strazi Genolink Probe"), nameNotes=[RANDOM_PLACEMENT_NOTE, RANDOM_VERSION_NOTE]),
    Structure("Vvarix Flux Conduit", 1, 1, True, False, ap=1, rp=2, acq=mission("An Uncomfortable Decision"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Vvarix Flux Conduit", 1, 1, True, False, "(4,400)", ap=2, rp=2, acq=mission("An Uncomfortable Decision"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Vvarix Flux Conduit", 1, 1, True, False, "(4,695)", ap=2, rp=3, acq=mission("An Uncomfortable Decision"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Vvarix Flux Conduit", 1, 1, True, False, "(5,000)", ap=2, rp=4, acq=mission("An Uncomfortable Decision"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Vvarix Flux Conduit", 1, 1, True, False, "(5,700)", ap=2, rp=4, c=300, acq=mission("An Uncomfortable Decision"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Vvarix Flux Conduit", 1, 1, True, False, "(6,200)", ap=2, rp=4, c=600, acq=mission("An Uncomfortable Decision"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Vvarix Flux Conduit", 1, 1, True, False, "(6,500)", ap=2, rp=4, rpp=2, c=600, acq=mission("An Uncomfortable Decision"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Vvarix Flux Conduit", 1, 1, True, False, "(7,099)", ap=2, rp=4, rpp=4, c=600, acq=mission("An Uncomfortable Decision"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Vvarix Flux Conduit", 1, 1, True, False, "(8,002)", ap=2, rp=4, rpp=8, rps=500, c=600, acq=mission("An Uncomfortable Decision"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Vvarix Flux Conduit", 1, 1, True, False, "(8,500)", ap=2, rp=4, rpp=8, rps=1000, c=600, acq=mission("An Uncomfortable Decision"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Vvarix Flux Conduit", 1, 1, True, False, "(9,000)", ap=2, rp=4, rpp=8, rps=2000, c=600, acq=mission("An Uncomfortable Decision"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Alarri Comm Tower", 1, 1, True, False, ap=1, rp=1, c=100, acq=mission("The Alarri Sojourn")),
    Structure("Alarri Comm Tower", 1, 1, True, False, "- Mark II", ap=1, rp=2, c=200, acq=mission("The Alarri Sojourn"), formDescription="Must be a Hacker/Physicist/Spy to upgrade to Alarri Comm Tower - Mark II:"),
    Structure("Alarri Comm Tower", 1, 1, True, False, "- Mark III", ap=2, rp=2, c=350, acq=mission("The Alarri Sojourn"), formDescription="Must be Builder/Fixer/Explorer to upgrade to Alarri Comm Tower - Mark III:"),
    Structure("Alarri Compound Turret", 1, 1, True, False, mp=2, ap=1, atp=15, acq=mission("Breaching the Compound")),
    Structure("Alarri Signaling Drone", 1, 1, True, False, mp=1, ap=1, acq=mission("A Trap for Ja'kell")),
    Structure("XTS-10 Injector", 1, 1, True, True, mp=3, p=-150, acq=mission("Building the Injector")),
    Structure("RSL Data Uplink", 3, -1, True, True, rp=3, d=50, c=100, acq=mission("Network of Secrets"), alternatePageName="RSL Data Uplink (artifact)"),
    Structure("Sha'jha Uplink", 1, 2, True, True, rp=2, c=120, acq=mission("The Sha'jha Approach")),
    Structure("Raix Bunker", 1, 1, True, False, ap=1, rp=1, acq=mission("The Strain of Conflict"), defenseNotes=[RAIX_BUNKER_NOTE]),
    Structure("Raix Bunker", 1, 1, True, False, "II", ap=2, rp=2, acq=mission("The Strain of Conflict"), defenseNotes=[RAIX_BUNKER_NOTE]),
    Structure("Tejiar Ally HQ", 1, 1, True, False, mp=2, ap=1, acq=mission("A Choice of Sides")),
    Structure("Tejiar Ally HQ", 1, 1, True, False, "II", mp=2, ap=2, cp=5, acq=mission("A Choice of Sides")),
    Structure("Raix Refinery", 1, 1, True, False, mp=2, ap=1, c=300, acq=mission("The Garathon Offensive")),
    Structure("Raix Refinery", 1, 1, True, False, "(Specialized)", mp=2, ap=2, c=300, acq=mission("The Garathon Offensive"), formDescription="If built on a planet that already has a Raix Bunker constructed"),
    Structure("Raix Refinery", 1, 1, True, False, "II", mp=3, ap=2, c=400, acq=mission("The Garathon Offensive"), formDescription="After using the Raix Transformation"),
    Structure("Raix Refinery", 1, 1, True, False, "II (Specialized)", mp=3, ap=3, c=400, acq=mission("The Garathon Offensive"), formDescription="If built on a planet that already has a Raix Bunker constructed AND After using the Raix Transformation"),
    Structure("Tej-Brask Refueling Depot", 1, 1, True, False, mp=4, d=500, acq=mission("The Crimson Bait")),
    Structure("Tej-Brask Refueling Depot", 1, 1, True, False, "II", mp=6, ap=1, d=1000, acq=mission("Tej-Brask Refueling Depot"), formDescription="After using the Raix Transformation"),
    Structure("Meta-Tuned Jammer", 1, 1, True, True, "(1)", rp=2, cp=25, acq=mission("The Crimson Defector"), formDescription="Option 1"),
    Structure("Meta-Tuned Jammer", 1, 1, True, True, "(2)", rp=4, cp=10, acq=mission("The Crimson Defector"), formDescription="Option 2"),
    Structure("Rikthar's War Forge", 2, 1, True, True, "(1)", mp=2, ap=2, atp=30, acq=mission("Vengeful Deeds"), formDescription="Option 1"),
    Structure("Rikthar's War Forge", 2, 1, True, True, "(2)", mp=1, ap=3, atp=10, acq=mission("Vengeful Deeds"), formDescription="Option 2"),
    Structure("NSX Tracking Matrix", 1, 1, True, False, mp=2, ap=1, rp=2, d=3000, acq=mission("Dark Pursuit")),
    Structure("NSX Tracking Matrix", 1, 1, True, False, "(2)", mp=2, ap=2, rp=3, d=6000, acq=mission("Dark Pursuit"), formDescription="Can only be used if the planet has 3 NSX crate effects on it"),
    Structure("NSX Tracking Matrix", 1, 1, True, False, "(3)", mp=2, ap=3, rp=4, d=9000, acq=mission("Dark Pursuit"), formDescription="Can only be used if the planet does NOT have any NSX crate effects on it"),
    Structure("Sub-Tachyonic Axis", 1, 1, True, False, mp=3, ap=1, c=200, acq=mission("The Oruas Eye (mission)")),
    Structure("Sub-Tachyonic Axis", 1, 1, True, False, "(Upgraded)", mp=4, ap=2, c=300, acq=mission("The Oruas Eye (mission)"), formDescription="If none of your planets have sub tachyonic detection active when deployed"),
    Structure("Oruas Eye Chamber", 1, 1, True, False, ap=2, aps=1000, rp=2, dp=25, acq=mission("The Great Elders")),
    Structure("Lutuma Command Module", 1, 1, True, False, mp=1, ap=1, rp=1, d=8000, acq=mission("The Lutuma Coup")),
    Structure("Oruas Predictive Disjector", 1, 1, False, False, ap=1, atp=20, c=400, acq=mission("Vision of Oruas") + ", " + market(CORRUPTION_MARKET)),
    Structure("Oruas Corrupted Disjector", 1, 1, False, False, ap=2, atp=40, c=800, acq=mission("Vision of Oruas") + ", " + market(CORRUPTION_MARKET), alternatePageName="Oruas Predictive Disjector", formDescription="Activated ability:"),
    Structure("Tri-Ocular Inhibitor", 1, 1, True, False, mp=4, ap=1, cp=10, acq=mission("Chamber of Lies")),
    Structure("Zolazin Analyzer", 1, 2, True, True, ap=1, rp=1, acq=mission("The Zolazin Pursuit")),
    Structure("Zolazin Void Tower", 1, 1, True, True, c=100, acq=mission("Spoils of War")),
    Structure("Ergosphere Filter", 1, 1, True, True, c=150, cp=20, acq=mission("The Aevax Experiment")),
    Structure("Quantum Hydro-Meliorator", 1, 1, True, True, ap=1, p=100, acq=mission("Octafari Distress")),
    Structure("Quantum Hydro-Meliorator", 1, 1, True, True, "(Pop Doubled)", ap=1, p=200, acq=mission("Octafari Distress"), formDescription="If placed on Terra, Gaia, or Dyson planet:"),
    Structure("Quantum Hydro-Meliorator", 1, 1, True, True, "(Pop Tripled)", ap=1, p=300, acq=mission("Octafari Distress"), formDescription="If placed on Oceanic planet:"),
    Structure("Mylarai Stripcore Mine", 1, 1, True, False, mp=4, ap=-2, acq=mission("The Mylarai Embargo")),
    Structure("Modified Grid-Pylon", 2, 1, True, True, rp=2, d=200, c=150, acq=mission("Embattled Retreat")),
    Structure("Convoy Heat Seeker", 1, 1, True, True, mp=1, p=75, acq=mission("A Stryll Target")),
    Structure("Volcanic Heat Seeker", 1, 1, True, True, mp=2, p=150, acq=mission("A Stryll Target"), alternatePageName="Convoy Heat Seeker", formDescription="If placed on a Volcanic planet:"),
    Structure("Adaptive Spire", 1, 2, True, True, "(M)", mp=2, acq=mission("A Station Adrift"), formDescription="If placed on a Barren, Crystal, Demon, Irradiated, Sentient, Shattered, Toxic, or Volcanic planet:"),
    Structure("Adaptive Spire", 1, 2, True, True, "(A)", ap=2, acq=mission("A Station Adrift"), formDescription="If placed on a Crystal, Desert, Gaia, Icy, Oceanic, Relic, or Terra planet:"),
    Structure("Adaptive Spire", 1, 2, True, True, "(R)", rp=2, acq=mission("A Station Adrift"), formDescription="If placed on an Aphotic, Ecumenopolis, Gas, Metallic, or Plasma planet:"),
    Structure("Adaptive Spire", 1, 2, True, True, "(X)", mp=1, ap=1, rp=1, acq=mission("A Station Adrift"), formDescription="If placed on a Chthonian, Dyson, Exotic, Luminous, Machine, Rift, or Void planet:"),
    Structure("Xectiphage Tower", 2, 1, True, True, d=300, acq=mission("Influence of the Broodmind"), limitNotes=[LOCK_NOTE]),
    Structure("Xecti Signal Repeater", 1, 1, True, True, rpp=10, acq=mission("The Broodmind Hunt")),
    Structure("Extracted Lithovoric Stem", 1, 1, True, True, mpp=10, acq=mission("Cold Evasion")),
    Structure("Orbital Stabilizer", 1, 1, True, True, mpp=7, ap=1, acq=mission("Tremors From Below")),
    Structure("Orbital Stabilizer", 1, 1, True, True, "(Doubled)", mpp=14, ap=2, acq=mission("Tremors From Below"), formDescription="If the planet has moon(s) or rings) when built:"),
    Structure("Vaash Holomatrix", 1, 1, True, True, rp=2, c=100, acq=mission("The Message Within")),
    Structure("Vaash Holomatrix", 1, 1, True, True, "(Upgraded)", rp=2, rpp=7, c=100, acq=mission("The Message Within"), formDescription="If you are a Zolazin, Vygoid, or Hacker when this is first built:"),
    Structure("Litheor Core-Tunnel", 1, 1, True, False, "(1)", mp=2, cp=15, acq=mission("Reaching the Core"), formDescription="Option 1:"),
    Structure("Litheor Core-Tunnel", 2, 1, True, False, "(2)", mp=3, cp=23, acq=mission("Reaching the Core"), formDescription="Option 2:"),
    Structure("Litheor Core-Tunnel Shrine", 1, 1, True, False, "(1)", mp=2, ap=2, cp=15),
    Structure("Litheor Core-Tunnel Shrine", 2, 1, True, False, "(2)", mp=3, ap=2, cp=23, ip=1),
    Structure("Litheor Transmutative Locator", 1, 1, True, True, "(1)", app=6, dp=10, acq=mission("Silent Extraction")),
    Structure("Litheor Transmutative Locator", 1, 1, True, True, "(2)", app=5, dp=20, acq=mission("Silent Extraction")),
    Structure("Litheor Transmutative Locator", 1, 1, True, True, "(3)", app=4, dp=30, acq=mission("Silent Extraction")),
    Structure("Uldri Spacial Marker", 1, 1, False, False, mp=1, ap=1, d=300, acq=mission("Necessary Precautions") + ", " + market(ULDRI_MARKET)),
    Structure("Uldri Spacial Marker", 1, 1, False, False, "II", mp=2, ap=1, d=600, acq=mission("Necessary Precautions") + ", " + market(ULDRI_MARKET), formDescription="Upgrade after 1 week of calm:"),
    Structure("Uldri Spacial Marker", 1, 1, False, False, "III", mp=2, ap=2, d=1200, acq=mission("Necessary Precautions") + ", " + market(ULDRI_MARKET), formDescription="Upgrade after 1 month of calm:"),
    Structure("Uldri Anomaly Crystal", 1, 1, True, False, ap=1, rp=1, acq=mission("Passage of Risks") + ", " + market(ULDRI_MARKET)),
    Structure("Uldri Anomaly Crystal", 1, 1, True, False, "(Upgraded)", ap=1, rp=1, rpp=5, c=200, acq=mission("Passage of Risks") + ", " + market(ULDRI_MARKET), formDescription="If built on a planet scanned by at least 2 other ships:"),
    Structure("Ventar Field Collapser", 1, 1, True, False, ap=1, rp=2, cp=10, acq=mission("Slip-Field Debris")),
    Structure("Uldri Recovery Capsule", 1, 1, True, False, mp=2, rp=1, p=500, acq=mission("Solemn Reflections")),
    Structure("Uldri Recovery Capsule", 1, 1, True, False, "(2)", mp=2, ap=1, rp=1, p=1500, acq=mission("Solemn Reflections"), formDescription="Must be calm for 1 week to upgrade to mark 2 (Costs 1000 exotic matter and 1 charge):"),
    Structure("Uldri Recovery Capsule", 1, 1, True, False, "(3)", mp=2, ap=1, rp=2, p=2500, acq=mission("Solemn Reflections"), formDescription="Must be calm for 1 month to upgrade to mark 3 (Costs 10,000 exotic matter and 1 charge):"),
    Structure("Uldri Recovery Capsule", 1, 1, True, False, "(4)", mp=2, ap=2, rp=2, p=3500, acq=mission("Solemn Reflections"), formDescription="Must be calm for 2 months to upgrade to mark 4 (Costs 20,000 exotic matter and 1 charge):"),
    Structure("Drannik Databank", 5, 1, True, True, ap=2, rp=3, d=100, at=100, acq=mission("Ultimate Betrayal"), alternatePageName="Drannik Databank (artifact)"),
    Structure("Cloning Center", 1, 2, True, True, p=275, acq=mission("Drannik Rebirth")),
    Structure("X-Pulse Tower", 1, 2, True, True, d=350, at=350, acq=mission("Protecting the Colonies")),
    Structure("Antimatter Drill", 1, 1, True, True, mp=1, ap=1, at=400, acq=mission("Drill Capture")),
    Structure("Archaic Stasis Cells", 1, 1, True, True, p=200, id=500, acq=mission("Empty Arrival")),
    Structure("Taltherian Archives", 1, 2, True, False, rp=1, rps=1000, acq=mission("Echoes from Taltheria")),
    Structure("Chron Shifter", 1, 2, True, True, c=300, acq=mission("The Dark Theft")),
    Structure("Statue of the Magnus", 2, 3, True, True, id=1000, acq=mission("Journey of the Magnus")),
    Structure("Guarded Memorial", 2, 1, True, True, rp=1, d=250, acq=mission("Honoring the Fallen"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Neutron-Lift Processor", 1, 1, True, False, mp=6, mps=4200, acq=mission("Neutron-Lift Applications")),
    Structure("Hyperluminal Satellite", 1, 1, False, True, ap=1, rp=3, c=200, acq=mission("The Q-Pedd Catalyst")),
    Structure("Hyperluminal Sat-Grid", 1, 1, True, False, ap=3, rp=9, ip=1, c=600, acq=mission("Streveldan Ascendancy"), alternatePageName="Hyperluminal Satellite", formDescription="Upgrade using Hyperluminal Sat-Grid:"),
    Structure("Hyperluminal Sat-Grid Mesh", 1, 1, True, False, ap=4, rp=12, ip=1, c=800, acq=mission("Streveldan Ascendancy"), alternatePageName="Hyperluminal Satellite", formDescription="Upgrade using Hyperluminal Sat-Grid:"),
    Structure("Lepus Hatchery", 1, 1, True, False, dp=10, p=250, acq=mission("The Lepus Cluster")),
    Structure("Lepus Growth Hatchery", 1, 1, True, False, dp=20, p=500, acq=mission("The Lepus Cluster"), alternatePageName="Lepus Hatchery", formDescription="If at least 1 Lepus Drone is already constructed on the planet:"),
    Structure("Supel Comm Tower", 1, 1, True, False, rp=4, c=420, acq=mission("Supel Adaptations")),
    Structure("Elios Solar Drill", 1, 1, False, False, mp=3, ap=1, acq=mission("The Elios Migration")),
    Structure("Elios Solar Drill", 1, 1, False, False, "(Heliacal)", mp=3, ap=2, acq=mission("The Elios Migration"), formDescription="If built on a planet that has an [[Elios Heliacal Plant]]:"),
    Structure("Elios Solar Drill", 1, 1, False, False, "(Inverter)", mp=4, ap=2, acq=mission("The Elios Migration"), formDescription="Upgrade with [[Elios Solar Inverter]]:"),
    Structure("Elios Solar Drill", 1, 1, False, False, "(Inverter + Heliacal)", mp=4, ap=3, acq=mission("The Elios Migration"), formDescription="If built on a planet that has an Elios Heliacal Plant and upgrade with [[Elios Solar Inverter]]"),
    Structure("Elios Corethune Shell", 2, 1, False, False, mp=6, ap=2, ip=1, dp=20, c=620, acq=mission("The Corethune Assembly")),
    Structure("Elios Corethune Shell", 2, 1, False, False, "v2", mp=6, ap=3, ip=2, dp=30, c=920, acq=mission("The Corethune Assembly")),
    Structure("Elios Corethune Shell", 2, 1, False, False, "v3", mp=6, ap=4, ip=3, dp=40, c=1220, acq=mission("The Corethune Assembly")),
    Structure("Elios Corethune Shell", 2, 1, False, False, "v4", mp=6, ap=6, ip=5, dp=60, c=1620, acq=mission("The Corethune Assembly")),
    Structure("Vaash Cron-Stabilizer", 1, 1, True, False, ap=2, rp=2, rpp=4, rps=420, acq=mission("The Farselle Merging")),
    Structure("Chuhn Trading Post", 1, 1, False, False, mp=1, ap=1, rp=1, p=2000, acq=mission("The Chuhn")),
    Structure("Chuhn Trading Post", 1, 1, False, False, "(Doubled)", mp=2, ap=2, rp=2, p=4000, acq=mission("The Chuhn"), formDescription="If built on a planet that has a [[Galactic Trade Hub]] effect or a [[Chuhn Trading Forum]]"),
    Structure("Bane Psybeacon", 1, 1, False, False, mp=1, ap=1, rp=2, acq=mission("The Hallows Bane (Daily Mission)")),
    Structure("Bane Psybeacon", 1, 1, False, False, "- Mark II", mp=1, ap=2, rp=2, id=1000, acq=mission("The Hallows Bane (Daily Mission)"), formDescription="Upgrade after 1 week of calm to mark II (Costs 4 green badges and 1 charge or a [[Bane Ritual Mask]]):"),
    Structure("Bane Psybeacon", 1, 1, False, False, "- Mark III", mp=3, ap=2, rp=3, id=1000, acq=mission("The Hallows Bane (Daily Mission)"), formDescription="Upgrade after 2 weeks of calm to mark III (Costs 4 green badges and 1 charge or a [[Bane Ritual Mask]]):"),
    Structure("Bane Psybeacon", 1, 1, False, False, "- Mark IV", mp=3, ap=3, rp=3, id=3000, acq=mission("The Hallows Bane (Daily Mission)"), formDescription="Upgrade after 1 month of calm to mark IV (Costs 10 green badges and 1 charge or a [[Bane Ritual Mask]]):"),
    Structure("Bane Psybeacon", 1, 1, False, False, "- Mark V", mp=3, ap=4, rp=3, id=5000, acq=mission("The Hallows Bane (Daily Mission)"), formDescription="Upgrade with a [[Bane Ritual Mask]]):"),
    Structure("Bane Psybeacon", 1, 1, False, False, "- Mark VI", mp=4, ap=5, rp=4, id=6666),
    Structure("Bane Nether-Seal", 10, 1, False, False, mp=6, ap=6, rp=6, c=666, acq=mission("The Bane Bargain")),
    Structure("Bane Nether-Seal", 8, 1, False, False, "(2)", mp=6, ap=6, rp=6, c=666, acq=mission("The Bane Bargain"), formDescription="Upgrade after 6 days of calm (costs ??? energy and 1 charge):"),
    Structure("Bane Nether-Seal", 6, 1, False, False, "(3)", mp=6, ap=6, rp=6, c=666, acq=mission("The Bane Bargain"), formDescription="Upgrade after 12 days of calm (costs ??? energy and 1 charge):"),
    Structure("Bane Nether-Seal", 4, 1, False, False, "(4)", mp=6, ap=6, rp=6, c=666, acq=mission("The Bane Bargain"), formDescription="Upgrade after 18 days of calm (costs ??? energy and 1 charge):"),
    Structure("Bane Nether-Seal", 2, 1, False, False, "(5)", mp=6, ap=6, rp=6, c=666, acq=mission("The Bane Bargain"), formDescription="Upgrade after 28 days of calm (costs ??? energy and 1 charge):"),
    Structure("Bane Nether-Seal", 1, 1, False, False, "(6)", mp=6, ap=6, rp=6, c=666, acq=mission("The Bane Bargain"), formDescription="Upgrade after 42 days of calm (costs ??? energy and 1 charge):"),
    Structure("Perimeter Station", 1, 2, False, False, ap=2, d=200, p=100, acq=mission("The Era of Harvest"), alternatePageName="Space Elevator Chassis", formDescription="Upgrade using [[Perimeter Station Upgrade]]:"),
    Structure("Perimeter Station", 1, 2, False, False, "- Upgraded", ap=2, rp=1, p=1000, d=1000, acq=mission("The Era of Harvest"), alternatePageName="Space Elevator Chassis", formDescription="Upgrade Perimeter Stations using [[Archotage Amplifier]]:"),
    Structure("Scruuge Lab", 1, 1, False, False, mp=1, ap=1, rp=2, at=300, acq=mission("Gifts Unraveled"), alternatePageName="Refining Lab Chassis", formDescription="Upgrade using [[Gift of the Mind]]:"),
    Structure("Permafrost Sub-Network", 1, 1, True, False, rp=1, c=50, p=50, acq=mission("Beneath the Snow")),
    Structure("Permafrost Sub-Network", 1, 1, True, False, "(Doubled)", rp=2, c=100, p=100, acq=mission("Beneath the Snow"), formDescription="If built on an Icy planet:"),
    Structure("Ardyne Hypergate", 3, 1, True, False, mp=5, ap=5, ip=1, acq=mission("Ardyne Expansions")),
    Structure("Ardyne Hypergate", 3, 1, True, False, "(Upgraded)", mp=5, mpp=3, ap=5, app=3, rpp=3, ip=2, ipp=3, acq=mission("Ardyne Expansions"), formDescription="If built on a planet with an [[Ardyne Transfer Conduit]]:"),
    Structure("Seat of the Exarch", 2, 1, True, False, ap=3, ip=2, acq=mission("Will of the Exarch")),
    Structure("Seat of the Exarch", 2, 1, True, False, "(Upgraded)", ap=3, ip=2, ips=111, acq=mission("Will of the Exarch"), formDescription="If built on a planet with a [[Court of Oracles]]:"),
    Structure("Vygos Aquaseeker", 3, 2, True, False, mp=4, ap=4, ip=1, pp=22, acq=mission("The Vygos No-Mods")),
    Structure("Temple of Radiance", 2, 1, True, False, ap=3, rp=3, ipp=7, c=777, acq=mission("The Prismoda Incursion")),
    Structure("Cognitor Forum", 3, 1, True, False, ap=3, rp=6, rpp=8, ip=2, acq=mission("The Sill Routes")),
    Structure("Sirocco Sandspire", 2, 1, True, False, mp=3, app=3, rp=3, ip=1, acq=mission("The Sill Routes")),
    Structure("Cryonic Xynapse", 3, 2, True, False, rp=8, ip=2, ic=2, acq=mission("The Sill Routes")),
    Structure("Litheor Deep-Ember Keep", 2, 1, True, False, mp=4, mpp=5, ip=1, acq=mission("")),
    Structure("Litheor Deep-Ember Keep", 2, 1, True, False, "v2", mp=6, mpp=6, ip=2, acq=mission(""), formDescription="Upgrade ???"),
    Structure("Litheor Deep-Ember Keep", 2, 1, True, False, "v3", mp=8, mpp=7, ip=3, acq=mission(""), formDescription="Upgrade ???"),
    Structure("Atrium of Secrets", 2, 1, True, False, rp=2, ip=1, c=1100, cp=11, acq=mission("Rise of the Drahj Milieu")),
    Structure("Xecti Brood-Nest", 2, 2, True, False, mp=6, ip=1, atp=30, ic=2, acq=mission("The Broodmind Covenant")),
    Structure("War Foundry Plant", 1, 1, False, True, mp=1, ap=1, rp=1, at=500, atp=20, acq=lm("Foundry of War")),
    Structure("Galakis Transport", 1, 1, False, False, mp=1, mps=400, ap=1, aps=400, rp=1, rps=400, acq=lm("Galakis, City of Deals")),
    Structure("Galakis Entry Port", 1, 1, False, True, mp=1, ap=2, dp=10, p=1000, acq=lm("Galakis, City of Deals")),
    Structure("T.O. Omnispanner", 1, 1, False, False, rp=2, dp=10, c=100, acq=lm("Illegal Excavation")),
    Structure("Siladon Suppressor", 1, 1, False, True, rp=2, d=1500, c=200, acq=lm("The Siladon Event")),
    Structure("Xathe Inhibitor", 1, 1, False, True, ap=1, rp=2, cp=15, acq=lm("The Xathe Vortex")),
    Structure("Vorean Habitat", 1, 1, False, True, mp=1, ap=1, p=2000, acq=lm("Vorean Extinction")),
    Structure("Vorean Habitat", 1, 1, False, True, "(Upgraded)", mp=2, ap=2, p=2000, acq=lm("Vorean Extinction"), formDescription="If you are a Biologist when this is built:"),
    Structure("Vorean Biostasis Lab", 1, 1, False, True, ap=1, rp=1, pp=50, acq=lm("Vorean Extinction")),
    Structure("Vorean Biostasis Lab", 1, 1, False, True, "(Upgraded)", ap=2, rp=2, pp=50, acq=lm("Vorean Extinction"), formDescription="If you are a Biologist when this is first built:"),
    Structure("Ryelis Analyzer", 1, 1, False, True, ap=2, rp=2, cp=5, acq=lm("Disturbance at Ryelis")),
    Structure("Anti-Grav Repulsor", 1, 1, False, True, mp=1, ap=1, dp=15, cp=15, acq=lm("Cleanup at Ryelis")),
    Structure("Genome Modifier Tubes", 1, 1, False, True, mp=2, ap=2, id=2000, acq=lm("The Ardyne Sabotage")),
    Structure("Ardyne Transfer Conduit", 1, 1, False, False, mp=2, ap=1, rp=1, c=200, acq=lm("Incursion into Gartith")),
    Structure("Ardyne Transfer Conduit", 1, 1, False, False, "(Doubled)", mp=4, ap=2, rp=2, c=400, acq=lm("Incursion into Gartith"), formDescription="If the planet has an [[Ardyne Gateway Link]] when this is built:"),
    Structure("Roathir Listening Post", 1, 1, False, False, ap=1, rp=4, cp=5, acq=lm("The Cerulean Conclave (Mission)")),
    Structure("Cerulean Flow Converter", 1, 1, False, False, mp=5, ap=1, dp=25, acq=lm("Roathir: Hostile Takeover")),
    Structure("Cerulean Hyperstation", 1, 1, False, False, mp=2, ap=2, rp=2, pp=60, acq=lm("Roathir: Diplomatic Resolution")),
    Structure("Aerlen Rescue Transport", 1, 1, False, False, ap=1, rp=2, p=3000, acq=lm("Roathir: Diplomatic Resolution")),
    Structure("Aerlen Rescue Transport", 1, 1, False, False, "(Doubled)", ap=2, rp=4, p=6000, acq=lm("Roathir: Diplomatic Resolution"), formDescription="If your race is Aerlen when this is built:"),
    Structure("Dormant Tenebris Relic", 1, 1, False, False, mp=1, rp=2, acq=lm("The Tenebris Discovery")),
    Structure("Active Tenebris Relic", 1, 1, False, False, mp=1, ap=2, rp=2, c=200, acq=lm("The Tenebris Discovery"), alternatePageName="Dormant Tenebris Relic", formDescription="Upgrade with ability (costs 250 energy and 90,000 Exotic Matter):"),
    Structure("B'elna's Altar", 1, 1, False, False, ap=2, c=250, acq=lm("The Tenebris Discovery (Late Timeline)")),
    Structure("B'elna's Altar", 1, 1, False, False, "(Upgraded)", ap=2, app=3, c=500, acq=lm("The Tenebris Discovery (Late Timeline)"), formDescription="If built on a planet that already has a [[Shrine of B'elna]]:"),
    Structure("Darmos Nerve Turret", 1, 1, False, False, mp=2, ap=1, rp=2, at=30, acq=lm("Arenas of the Darmos Games")),
    Structure("Vearon Casino", 1, 1, False, False, mp=4, ap=1, p=2000, acq=lm("The Hunt for Mawks")),
    Structure("Morphogenic Inhibitor", 1, 4, False, False, ap=1, rp=3, c=300, acq=lm("The Hunt for Mawks"), nameNotes=[MORPHO_INHIBITOR_NOTE]),
    Structure("Silthion Gas Vesicle", 1, 1, False, False, "II", rp=4, c=300, acq=lm("Encounter at Nabai"), formDescription="Upgrade with [[Silthion Vesicle Evolution]]:"),
    Structure("Silthion T-Plasma Vesicle", 1, 1, False, False, "II", ap=2, rp=6, c=600, acq=lm("Encounter at Nabai"), formDescription="Upgrade with [[Silthion Vesicle Evolution]]:"),
    Structure("Sentiox Uplink", 1, 1, False, False, ap=2, rp=4, acq=lm("The TitanCore Rebirth")),
    Structure("Sentiox Trilink Node", 1, 3, False, False, ap=2, app=2, rp=3, acq=lm("Rise of the Sentiox")),
    Structure("Stryll Ghost-Uplink", 2, 1, False, False, rp=3, ip=1, c=1100, cp=11, acq=lm("Operation Shadow's Sleep")),
    Structure("Scruuge Calibration Plant", 1, 1, False, False, mp=2, ap=2, c=400, acq=zone("Scruuge Perimeter"), alternatePageName="Scruuge Calibration Chamber", formDescription="Upgrade with [[Scruuge Calibration Plant]]:"),
    Structure("Scruuge Calibration Plant", 1, 1, False, False, "(Upgraded)", mp=2, ap=2, c=800, acq=zone("Scruuge Perimeter"), alternatePageName="Scruuge Calibration Chamber", formDescription="Upgrade with [[Scruuge Calibration Plant]] when the Chamber already had the Thraccti bonus:"),
    Structure("Scruuge Cargo Launcher", 1, 1, False, False, mp=4, ap=2, d=2000, dp=15, acq=zone("Scruuge Perimeter"), alternatePageName="Scruuge Cargo Pad", formDescription="Upgrade with [[Scruuge Cargo Launcher]]:"),
    Structure("Scruuge Cargo Launcher", 1, 1, False, False, mp=6, ap=3, d=4000, dp=15, acq=zone("Scruuge Perimeter"), alternatePageName="Scruuge Cargo Pad", formDescription="Upgrade with [[Scruuge Cargo Launcher]] when the Pad also had the Chamber bonus:"),
    Structure("Scruuge Frost Tribunal", 2, 2, False, False, ap=3, aps=300, ip=1, acq=zone("Scruuge Perimeter")),
    Structure("Scruuge Growth Replivats", 1, 1, False, False, ap=2, rp=4, p=5000, pp=15, acq=zone("Scruuge Perimeter"), alternatePageName="Scruuge Growth Vats", formDescription="Upgrade with [[Scruuge Growth Replivats]]:"),
    Structure("Scruuge Growth Replivats", 1, 1, False, False, "(Upgraded)", ap=3, rp=6, p=10000, pp=15, acq=zone("Scruuge Perimeter"), alternatePageName="Scruuge Growth Vats", formDescription="Upgrade with [[Scruuge Growth Replivats]] when the Vats also had the Vault bonus::"),
    Structure("Scruuge Refinery-Lab", 1, 1, False, False, mp=2, ap=2, rp=4, at=600, acq=zone("Scruuge Perimeter"), alternatePageName="Refining Lab Chassis", formDescription="Upgrade Scruuge Lab using [[Scruuge Refinery-Lab]]:"),
    Structure("Streveldan Autoform Habitat", 1, 1, False, False, "A", mp=6, ap=1, c=350, p=5000, acq=zone("Streveldan Refuge")),
    Structure("Streveldan Autoform Habitat", 1, 1, False, False, "B", ap=1, rp=6, c=350, p=5000, acq=zone("Streveldan Refuge")),
    Structure("Streveldan Autoform Habitat", 1, 1, False, False, "C", mp=2, ap=2, rp=2, c=200, p=2500, acq=zone("Streveldan Refuge")),
    Structure("Streveldan Autoform Habitat", 1, 1, False, False, "D", mp=1, ap=1, rp=1, ip=1, c=200, p=2500, acq=zone("Streveldan Refuge")),
    Structure("Supel Microhaven", 1, 1, False, False, mp=2, ap=1, rp=2, p=2000, pp=5, acq=zone("Lepus Cluster"), formDescription="If the planet is Average or larger when constructed:"),
    Structure("Supel Microhaven", 1, 1, False, False, "(S)", mp=2, ap=1, rp=3, p=3000, pp=7, acq=zone("Lepus Cluster"), formDescription="If the planet is Small when constructed:"),
    Structure("Supel Microhaven", 1, 1, False, False, "(VS)", mp=2, ap=1, rp=3, ip=1, p=4000, pp=9, acq=zone("Lepus Cluster"), formDescription="If the planet is Very Small when constructed:"),
    Structure("Supel Microhaven", 1, 1, False, False, "(T)", mp=2, ap=1, rp=3, ip=2, p=5000, pp=12, acq=zone("Lepus Cluster"), formDescription="If the planet is Tiny when constructed:"),
    Structure("Supel Microhaven", 1, 1, False, False, "(VT)", mp=3, ap=2, rp=3, ip=2, p=6000, pp=15, acq=zone("Lepus Cluster"), formDescription="If the planet is Very Tiny when constructed:"),
    Structure("Arx Genetica", 1, 1, False, False, rp=4, rps=321, ip=1, cp=11, acq=zone("Genoform Surge") + ", " + mission("The Genoform Surge")),
    Structure("Elios Pulse-Compressor", 1, 1, False, False, mp=4, ap=2, ip=1, ips=88, acq=zone("Elios Nexus")),
    Structure("NSX Crate: Diamond", 1, 1, False, False, mp=2, ap=1, rp=2, dp=10, acq=scanning("Nanoshearing Sensor")),
    Structure("Lepus Bio-Nest", 1, 1, False, False, "(1)", ap=1, p=1000, acq=scanning("Lepus (seasonal event)"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Lepus Bio-Nest", 1, 1, False, False, "(2)", ap=1, p=2000, acq=scanning("Lepus (seasonal event)"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Lepus Bio-Nest", 1, 1, False, False, "(3)", ap=1, p=3000, acq=scanning("Lepus (seasonal event)"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Lepus Bio-Nest", 1, 1, False, False, "(4)", ap=1, p=4000, acq=scanning("Lepus (seasonal event)"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Lepus Bio-Nest", 1, 1, False, False, "(5)", ap=1, p=5000, acq=scanning("Lepus (seasonal event)"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Lepus Bio-Nest", 1, 1, False, False, "(6)", ap=1, p=6000, acq=scanning("Lepus (seasonal event)"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Lepus Bio-Nest", 1, 1, False, False, "(7)", ap=2, p=1000, acq=scanning("Lepus (seasonal event)"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Lepus Bio-Nest", 1, 1, False, False, "(8)", ap=2, p=2000, acq=scanning("Lepus (seasonal event)"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Lepus Bio-Nest", 1, 1, False, False, "(9)", ap=2, p=3000, acq=scanning("Lepus (seasonal event)"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Lepus Bio-Nest", 1, 1, False, False, "(10)", ap=2, p=4000, acq=scanning("Lepus (seasonal event)"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Lepus Bio-Nest", 1, 1, False, False, "(11)", ap=2, p=5000, acq=scanning("Lepus (seasonal event)"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Lepus Bio-Nest", 1, 1, False, False, "(12)", ap=2, p=6000, acq=scanning("Lepus (seasonal event)"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Auric Lepus Bio-Nest", 1, 1, False, False, "(1)", ap=2, p=5000, acq=scanning("Lepus (seasonal event)"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Auric Lepus Bio-Nest", 1, 1, False, False, "(2)", ap=3, p=2000, acq=scanning("Lepus (seasonal event)"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Auric Lepus Bio-Nest", 1, 1, False, False, "(3)", ap=3, p=10000, acq=scanning("Lepus (seasonal event)"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Elios Orbital Conduit", 1, 1, False, False, ap=1, rp=5, rpp=10, acq=scanning("Elios (seasonal event)")),
    Structure("Elios Core Mine", 1, 1, False, False, mp=4, mpp=10, ap=2, acq=scanning("Elios (seasonal event)")),
    Structure("Elios Core Mine", 1, 1, False, False, "(Upgraded)", mp=5, mpp=15, ap=2, acq=scanning("Elios (seasonal event)"), formDescription="Upgrade with [[Elios Heliosyne]]:"),
    Structure("Psyshade Arsenal", 1, 1, False, False, mp=2, ap=1, at=3000, acq=scanning("Bane (seasonal event)")),
    Structure("Psyshade Arsenal", 1, 1, False, False, "II", mp=3, ap=2, at=6000, acq=scanning("Bane (seasonal event)"), formDescription="Upgrade using ability (costs 8 [[Green Badges]] and 500 energy, or a [[Bane Ritual Mask]]):"),
    Structure("Psyshade Arsenal", 1, 1, False, False, "III", mp=4, ap=3, at=12000, acq=scanning("Bane (seasonal event)"), formDescription="Upgrade using ability (costs 15 [[Green Badges]] and 1000 energy, or a [[Bane Ritual Mask]]):"),
    Structure("Psyshade Arsenal", 1, 1, False, False, "IV", mp=5, ap=4, at=24000, acq=scanning("Bane (seasonal event)"), formDescription="Upgrade with a [[Bane Ritual Mask]]:"),
    Structure("Psyshade Arsenal", 1, 1, False, False, "V", mp=6, ap=5, at=42000, acq=scanning("Bane (seasonal event)"), formDescription="Upgrade with a [[Bane Ritual Mask]]:"),
    Structure("Scruuge Keystone", 1, 1, False, False, ap=1, rp=3, atp=10, acq=scanning("Scruuge (seasonal event)")),
    Structure("Scruuge Keystone", 1, 1, False, False, "II", ap=2, rp=4, atp=20, acq=scanning("Scruuge (seasonal event)"), formDescription="Upgrade with [[Scruuge Keystone II Upgrade]]:"),
    Structure("Scruuge Keystone", 1, 1, False, False, "III", mp=2, ap=2, rp=6, atp=30, acq=scanning("Scruuge (seasonal event)"), formDescription="Upgrade with [[Scruuge Keystone III Upgrade]]:"),
    Structure("Scruuge Keystone", 1, 1, False, False, "IV", mp=4, ap=3, rp=8, atp=40, acq=scanning("Scruuge (seasonal event)"), formDescription="Upgrade with [[Scruuge Keystone IV Upgrade]]:"),
    Structure("Scruuge Keystone", 1, 1, False, False, "V", mp=6, ap=4, rp=10, atp=50, acq=scanning("Scruuge (seasonal event)"), formDescription="Upgrade with [[Scruuge Keystone V Upgrade]]:"),
    Structure("Scruuge Keystone", 1, 1, False, False, "VI", mp=8, ap=5, rp=12, atp=60, acq=scanning("Scruuge (seasonal event)"), formDescription="Upgrade with [[Scruuge Keystone VI Upgrade]]:"),
    Structure("Scruuge Keystone", 1, 1, False, False, "VII", mp=10, ap=6, rp=14, atp=70, acq=scanning("Scruuge (seasonal event)"), formDescription="Upgrade with [[Scruuge Keystone VII Upgrade]]:"),
    Structure("Gene-Root Pavilion", 2, 2, False, False, ap=1, rp=3, ip=1, c=770, acq=scanning("Quilu Circle")),
    Structure("T.O. Capitol Dome", 2, 1, False, False, rp=2, ip=2, dp=20, acq=scanning("Terran Outsiders Perimeter")),
    Structure("T.O. Capitol Dome", 2, 1, False, False, "- Upgraded", rp=4, ip=3, dp=30, acq=scanning("Terran Outsiders Perimeter"), formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("Tri-Phase Cutter", 1, 2, False, True, mp=3, at=300, acq=baseCrate(), alternatePageName="Phase Cutter Chassis", formDescription=("Upgrade with [[Tri-Phase Cutter Upgrade]]:")),
    Structure("Adumbrate Station", 1, 2, False, False, ap=1, rp=1, c=200, acq=baseCrate()),
    Structure("Adumbrate Station", 1, 2, False, False, "(Doubled)", ap=2, rp=2, c=400, acq="[[The Oruas Eye (ally)|Vision of Bounty]]", formDescription="Upgrade with [[Adumbrate Station Upgrade]]:"),
    Structure("Adumbrate Junction", 1, 2, False, False, ap=1, rp=3, cp=18, acq=baseCrate()),
    Structure("Farselle Paravault", 1, 1, False, False, mps=200, app=2, aps=200, rps=200, acq=baseCrate()),
    Structure("Uldri Spacial Folder", 1, 1, False, False, mp=1, ap=1, rp=2, c=300, acq=market(ULDRI_MARKET)),
    Structure("Uldri Crystal Field", 1, 1, False, False, mpp=5, app=5, rpp=5, ipp=5, d=1000, acq=market(ULDRI_MARKET)),
    Structure("Uldri Power Node", 1, 1, False, False, app=5, rp=1, acq=market(ULDRI_MARKET)),
    Structure("Uldri Prism Haven", 1, 1, False, False, mp=2, ap=2, rp=2, rpp=7, rps=7, acq=market(ULDRI_MARKET)),
    Structure("Raix Stasis Hold", 1, 1, False, False, mp=2, mps=1400, ap=1, aps=1400, cp=11, acq=market(RAIX_MARKET)),
    Structure("Raix Stasis Hold", 1, 1, False, False, "II", mp=2, mps=1900, ap=2, aps=1900, cp=16, acq=market(RAIX_MARKET), formDescription="Upgrade with [[Raix Structural Enhancement]]:"),
    Structure("Raix Stasis Hold", 1, 1, False, False, "III", mp=3, mps=2400, ap=2, aps=2400, cp=21, acq=market(RAIX_MARKET), formDescription="Upgrade with [[Raix Structural Enhancement]] again:"),
    Structure("Corrupted Edifice", 1, 1, False, False, ap=1, aps=2000, cp=20, acq=market(CORRUPTION_MARKET)),
    Structure("Corrupted Portal", 1, 1, False, False, mp=3, ap=2, aps=600, c=400, acq=market(CORRUPTION_MARKET)),
    Structure("Corrupted Portal", 1, 1, False, False, "II", mp=4, ap=3, aps=1200, c=800, acq=market(CORRUPTION_MARKET), formDescription="Upgrade with ability (costs 4 [[Corruption]], 5,555 [[Energy]], 1 charge):"),
    Structure("Corrupted Portal", 1, 1, False, False, "III", mp=5, ap=4, aps=1800, c=1200, acq=market(CORRUPTION_MARKET), formDescription="Upgrade with ability (costs 5 [[Corruption]], 5,555 [[Energy]], 1 charge):"),
    Structure("Corrupted Portal", 1, 1, False, False, "IV", mp=6, ap=5, aps=2400, c=1600, acq=market(CORRUPTION_MARKET), formDescription="Upgrade with ability (costs 6 [[Corruption]], 5,555 [[Energy]], 1 charge):"),
    Structure("Corrupted Portal", 1, 1, False, False, "V", mp=7, ap=6, aps=3000, c=2000, acq=market(CORRUPTION_MARKET), formDescription="Upgrade with ability (costs 7 [[Corruption]], 5,555 [[Energy]], 1 charge):"),
    Structure("Cognizant Omniforge", 1, 1, False, True, mp=1, mpp=5, ap=1, app=5, rp=1, rpp=5, ipp=5, acq=market(MISSION_MARKET)),
    Structure("Cognizant Omniforge Grid", 1, 1, False, False, mp=2, mpp=7, ap=2, app=7, rp=2, rpp=7, ipp=7, acq=market(MISSION_MARKET), formDescription="Upgrade with [[Cognizant Omniforge Grid Upgrade]]:"),
    Structure("Hall of Law", 3, 5, False, False, ap=1, rp=2, ip=1, acq=market(MISSION_MARKET)),
    Structure("Cognizant Omni-Bank", 1, 2, False, False, mp=3, mps=2222, ap=2, aps=2222, acq=market(MISSION_MARKET)),
    Structure("Cognizant Omni-Plant", 1, 1, False, False, ap=3, rp=4, acq=market(MISSION_MARKET)),
    Structure("Aeon Tower", 3, 2, False, False, ap=3, rp=6, ip=2, c=550, cp=16, acq=market(AEON_MARKET)),
    Structure("Aeon Relay Tower", 1, 1, False, False, mp=1, ap=2, rp=2, ip=1, acq=market(AEON_MARKET), alternatePageName="Relay Tower Chassis", formDescription="Upgrade with [[Aeon Chassis Calibrator]]:"),
    Structure("Aeon Processor Core", 1, 1, False, False, mp=2, ap=2, rp=1, ip=1, acq=market(AEON_MARKET), alternatePageName="Processing Core Chassis", formDescription="Upgrade with [[Aeon Chassis Calibrator]]:"),
    Structure("Galaxy Interrogators", 0, 8, False, False, rps=500, c=200, acq="[[Prismodyne Gene Splicer]]", limitNotes=[BAHREEN_DOMAIN_NOTE], alternatePageName=PRISMATIC_DOMAIN, formDescription="Galaxy Inquisitors upgraded with Prismodyne Gene Splicer:"),
    Structure("Galaxy Pedants", 0, 8, False, False, rp=2, acq="[[Prismodyne Gene Splicer]]", limitNotes=[BAHREEN_DOMAIN_NOTE], alternatePageName=PRISMATIC_DOMAIN, formDescription="Galaxy Technocrats upgraded with Prismodyne Gene Splicer:"),
    Structure("Galaxy Administrators", 0, 8, False, False, mp=2, acq="[[Prismodyne Gene Splicer]]", limitNotes=[BAHREEN_DOMAIN_NOTE], alternatePageName=PRISMATIC_DOMAIN, formDescription="Galaxy Overseers upgraded with Prismodyne Gene Splicer:"),
    Structure("Galaxy Aristocrats", 0, 8, False, False, ap=2, acq="[[Prismodyne Gene Splicer]]", limitNotes=[BAHREEN_DOMAIN_NOTE], alternatePageName=PRISMATIC_DOMAIN, formDescription="Galaxy Elitists upgraded with Prismodyne Gene Splicer:"),
    Structure("Galaxy Surrogates", 0, 8, False, False, mp=1, ap=1, rp=1, acq="[[Prismodyne Gene Splicer]]", limitNotes=[BAHREEN_DOMAIN_NOTE], alternatePageName=PRISMATIC_DOMAIN, formDescription="Chance for any base Official when upgraded with Prismodyne Gene Splicer:"),
    Structure("Galaxy Celestials", 0, 8, False, False, mp=2, ap=2, rp=2, c=400, acq="[[Prismodyne Gene Splicer]]", limitNotes=[BAHREEN_DOMAIN_NOTE], alternatePageName=PRISMATIC_DOMAIN, formDescription="Chance for any base Official when upgraded with Prismodyne Gene Splicer:"),
    Structure("Counter-Intelligence Nexus", 2, 1, False, True, rp=2, c=150, acq=market(BATTLE_MARKET)),
    Structure("Nexus Command Center", 2, 1, False, False, rp=4, c=300, acq=market(BATTLE_MARKET), alternatePageName=("Counter-Intelligence Nexus"), formDescription="Upgrade with [[Nexus Command Center Upgrade]]:"),
    Structure("Nexus Spy Fortress", 2, 1, False, False, rp=8, c=600, acq=market(BATTLE_MARKET), alternatePageName=("Counter-Intelligence Nexus"), formDescription="Upgrade with [[Nexus Spy Fortress Upgrade]]:"),
    Structure("Nexus Recon Spy-Hub", 2, 1, False, False, ap=3, rp=12, c=1200, acq=market(BATTLE_MARKET), alternatePageName=("Counter-Intelligence Nexus"), formDescription="Upgrade with [[Nexus Recon Spy-Hub]]:"),
    Structure("OmniVote Terminal", 5, 2, False, False, rp=4, ip=2, acq=market(BATTLE_MARKET)),
    Structure("OmniVote Nexus", 5, 2, False, False, rp=16, ip=8),
    Structure("Heist Dispatch Center", 2, 1, False, True, mp=1, ap=1, at=150, acq=market(BATTLE_MARKET)),
    Structure("Heist Dispatch Station", 2, 1, False, False, mp=2, ap=2, at=300, atp=10, acq=market(BATTLE_MARKET), alternatePageName="Heist Dispatch Center", formDescription="Upgrade with [[Heist Dispatch Station Upgrade]]:"),
    Structure("Propaganda Plex", 6, 1, False, False, ap=7, ip=3, pp=20, acq=market(BATTLE_MARKET)),
    Structure("Propaganda Plex", 6, 1, False, False, "v2", ap=9, ip=4, pp=30, acq=market(BATTLE_MARKET), formDescription="Upgrade using ability (costs 2200 Influence and 55 Yellow Badges):"),
    Structure("Propaganda Plex", 6, 1, False, False, "v3", ap=11, ip=5, pp=40, acq=market(BATTLE_MARKET), formDescription="Upgrade using ability (costs 5500 Influence and 77 Yellow Badges):"),
    Structure("Assimilation Locus", 2, 1, False, True, mp=2, p=100, acq=market(BATTLE_MARKET)),
    Structure("Assimilation Locus", 2, 1, False, True, "50%", mp=3, p=150, acq=market(BATTLE_MARKET), formDescription="Upgrade with [[Subjugation Protocols]] when the Locus did not have the 'recently invaded' bonus:"),
    Structure("Assimilation Locus", 2, 1, False, True, "100%", mp=4, p=300, acq=market(BATTLE_MARKET), formDescription="Upgrade with [[Subjugation Protocols]] again when the Locus did not have the 'recently invaded' bonus:"),
    Structure("Assimilation Locus", 2, 1, False, True, "(Doubled)", mp=4, p=300, acq=market(BATTLE_MARKET), formDescription="If the planet has 'New Colony' status and was recently invaded by you when constructed:"),
    Structure("Assimilation Locus", 2, 1, False, True, "(Doubled) 50%", mp=6, p=450, acq=market(BATTLE_MARKET), formDescription="Upgrade with [[Subjugation Protocols]] when the Locus had the 'recently invaded' bonus:"),
    Structure("Assimilation Locus", 2, 1, False, True, "(Doubled) 100%", mp=8, p=600, acq=market(BATTLE_MARKET), formDescription="Upgrade with [[Subjugation Protocols]] again when the Locus had the 'recently invaded' bonus:"),
    Structure("Luring Cynosure", 1, 1, False, False, ap=1, atp=20, acq=market(BATTLE_MARKET)),
    Structure("Luring Cynosure", 1, 1, False, False, "(Upgraded)", mp=2, ap=1, atp=40, acq=market(BATTLE_MARKET), formDescription="If the planet has the Insurgent Uprising or Enslaved Prisoners effect when this is constructed:"),
    Structure("Forgestone Prison Colony", 1, 1, False, False, mp=3, mpp=3, mps=404, ap=1, acq=market(BATTLE_MARKET)),
    Structure("Forgestone Prison Colony", 1, 1, False, False, "v2", mp=5, mpp=5, mps=606, ap=2, acq=market(BATTLE_MARKET), formDescription="Upgrade with ability (costs 22 Green Badges):"),
    Structure("Forgestone Prison Colony", 1, 1, False, False, "v3", mp=7, mpp=7, mps=808, ap=3, acq=market(BATTLE_MARKET), formDescription="Upgrade using ability (costs 33 Green Badges):"),
    Structure("Forgestone Prison Colony", 1, 1, False, False, "v4", mp=9, mpp=9, mps=1010, ap=4, acq=market(BATTLE_MARKET), formDescription="Upgrade using ability (costs 44 Green Badges):"),
    Structure("Paralyxis Diffuser", 2, 2, False, False, mp=4, ap=3, rp=2, dp=33, ic=3, acq=market(BATTLE_MARKET)),
    Structure("Barrier Nexus", 1, 2, False, True, ap=1, d=300, dp=20, acq=market(BATTLE_MARKET)),
    Structure("Barrier HyperNexus", 1, 2, False, False, ap=1, d=600, dp=30, acq=market(BATTLE_MARKET), alternatePageName="Barrier Nexus", formDescription="Upgrade with [[Barrier HyperNexus Upgrade]]:"),
    Structure("Orbisbarrier HyperNexus", 1, 2, False, False, ap=2, d=1200, dp=40, acq=market(BATTLE_MARKET), alternatePageName="Barrier Nexus", formDescription="Upgrade with [[Orbisbarrier HyperNexus Upgrade]]:"),
    Structure("Arcobarrier PulseNexus", 1, 2, False, False, ap=3, rp=1, d=2400, dp=50, acq=market(BATTLE_MARKET), alternatePageName="Barrier Nexus", formDescription="Upgrade with [[Arcobarrier HyperNexus Upgrade]]:"),
    Structure("Argent Consulate", 2, 1, False, False, ap=2, rp=2, pp=40, acq=market(BATTLE_MARKET)),
    Structure("Argent Sector-Embassy", 2, 1, False, False, ap=4, rp=4, pp=60, acq=market(BATTLE_MARKET), alternatePageName="Argent Consulate", formDescription="Upgrade with [[Argent Sector-Embassy]]:"),
    Structure("Argent Galactic-Embassy", 2, 1, False, False, ap=6, rp=6, pp=80, acq=market(BATTLE_MARKET), alternatePageName="Argent Consulate", formDescription="Upgrade with [[Argent Galactic-Embassy]]:"),
    Structure("Quantum Accelerator", 2, 2, False, True, "(M)", mp=2, c=150, acq=market(BATTLE_MARKET)),
    Structure("Quantum Accelerator", 2, 2, False, False, "(M) 50%", mp=3, c=225, acq=market(BATTLE_MARKET), formDescription="Upgrade mining version with [[Acceleration Protocols]]:"),
    Structure("Quantum Accelerator", 2, 2, False, False, "(M) 100%", mp=4, c=300, acq=market(BATTLE_MARKET), formDescription="Upgrade mining version again with [[Acceleration Protocols]]:"),
    Structure("Quantum Accelerator", 2, 2, False, True, "(A)", ap=2, c=150, acq=market(BATTLE_MARKET)),
    Structure("Quantum Accelerator", 2, 2, False, False, "(A) 50%", ap=3, c=225, acq=market(BATTLE_MARKET), formDescription="Upgrade artifact version with [[Acceleration Protocols]]:"),
    Structure("Quantum Accelerator", 2, 2, False, False, "(A) 100%", ap=4, c=300, acq=market(BATTLE_MARKET), formDescription="Upgrade artifact version again with [[Acceleration Protocols]]:"),
    Structure("Quantum Accelerator", 2, 2, False, True, "(R)", rp=2, c=150, acq=market(BATTLE_MARKET)),
    Structure("Quantum Accelerator", 2, 2, False, False, "(R) 50%", rp=3, c=225, acq=market(BATTLE_MARKET), formDescription="Upgrade research version with [[Acceleration Protocols]]:"),
    Structure("Quantum Accelerator", 2, 2, False, False, "(R) 100%", rp=4, c=300, acq=market(BATTLE_MARKET), formDescription="Upgrade research version again with [[Acceleration Protocols]]:"),
    Structure("Dark Supercollider", 1, 1, False, False, mpp=4, app=4, rpp=4, ipp=4, c=800, acq=market(BATTLE_MARKET)),
    Structure("Dark Supercollider", 1, 1, False, False, "(Upgraded)", mpp=6, app=6, rpp=6, ipp=6, c=1200, acq=market(BATTLE_MARKET), formDescription="If the planet has 2 maxed [[Quantum Accelerator|Quantum Accelerators]] when this is constructed:"),
    Structure("Dark Mega-Strider", 1, 1, False, False, mp=2, ap=2, atp=22, acq=market(BATTLE_MARKET)),
    Structure("Dark Mega-Strider", 1, 1, False, False, "v2", mp=4, ap=3, atp=44, acq=market(BATTLE_MARKET), formDescription="Upgrade with ability (costs 900 Dark Badges):"),
    Structure("Dark Mega-Strider", 1, 1, False, False, "v3", mp=6, ap=4, atp=66, acq=market(BATTLE_MARKET), formDescription="Upgrade with ability (costs 2000 Dark Badges):"),
    Structure("Dark Mega-Strider", 1, 1, False, False, "v4", mp=8, ap=5, atp=88, acq=market(BATTLE_MARKET), formDescription="Upgrade with ability (costs 5000 Dark Badges):"),
    Structure("Mineral Storage Tower", 2, 5, False, True, mps=2000, acq=market(GP_MARKET)),
    Structure("Artifact Warehouse", 2, 5, False, True, aps=4000, acq=market(GP_MARKET)),
    Structure("Research Data Archive", 2, 5, False, True, rps=2000, acq=market(GP_MARKET)),
    Structure("Weather Controller", 2, 1, False, True, rp=2, p=200, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Omni-Weather Controller", 2, 2, False, False, ap=2, rp=5, d=3333, cp=33, acq=market(GP_MARKET)),
    Structure("Sillixx Starport", 3, 1, False, True, mp=2, ap=2, p=300, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Sillixx Starport Hub", 2, 2, False, False, mp=3, ap=3, p=3333, pp=33, acq=market(GP_MARKET)),
    Structure("Human Training Barracks", 1, 1, False, True, d=250, at=250, p=500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Human Tactical Barracks", 2, 2, False, False, ap=3, rps=1111, dp=33, atp=33, p=5000, acq=market(GP_MARKET)),
    Structure("Library of Celestial Registry", 2, 1, False, False, ap=4, rp=4, rps=1001, ip=2, ips=101, acq=market(GP_MARKET)),
    Structure("Council Chamber", 1, 2, False, False, ap=3, ip=1, acq=market(GP_MARKET)),
    Structure("Court of Oracles", 2, 1, False, False, ip=3, acq=market(GP_MARKET)),
    Structure("Q-Pedd Science Station", 2, 2, False, True, rp=3, rps=2000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Available 2012:"),
    Structure("Q-Pedd Science Station", 2, 2, False, True, "2.0", rp=3, rps=3000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Available 2013:"),
    Structure("Q-Pedd Science Station", 2, 2, False, True, "3.0", rp=3, rps=4000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Available 2014 (or upgrade with [[]):"),
    Structure("Q-Pedd Science Station", 2, 2, False, False, "4.0", rp=4, rps=5000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Available 2015 (or upgrade with [[]):"),
    Structure("Q-Pedd Science Station", 2, 2, False, False, "5.0", rp=4, rps=6000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Available 2016 (or upgrade with [[]):"),
    Structure("Q-Pedd Science Station", 2, 2, False, False, "6.0", rp=5, rps=7000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Available 2017 (or upgrade with [[]):"),
    Structure("Q-Pedd Science Station", 2, 2, False, False, "7.0", rp=6, rps=8000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Available 2018 (or upgrade with [[]):"),
    Structure("Q-Pedd Science Station", 2, 2, False, False, "8.0", rp=7, rps=9000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Available 2019 (or upgrade with [[]):"),
    Structure("Q-Pedd Science Station", 2, 2, False, False, "9.0", rp=8, rps=10000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Available 2020 (or upgrade with [[]):"),
    Structure("Q-Pedd Science Station", 2, 2, False, False, "10.0", rp=9, rps=11000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Available 2021 (or upgrade with [[]):"),
    Structure("Q-Pedd Science Station", 2, 2, False, False, "11.0", rp=10, rps=12000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Available 2022 (or upgrade with [[]):"),
    Structure("Q-Pedd Science Station", 2, 2, False, False, "12.0", rp=11, rps=13000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Available 2023 (or upgrade with [[]):"),
    Structure("Q-Pedd Science Station", 2, 2, False, False, "13.0", rp=12, rps=14000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Available 2024 (or upgrade with [[]):"),
    Structure("Q-Pedd Science Station", 2, 2, False, False, "14.0", rp=14, rps=15000, c=1200, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Available 2025 (or upgrade with [[]):"),
    Structure("Q-Pedd Science Station", 2, 2, False, False, "15.0", rp=15, rps=16000, c=1400, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Streveldan Convocation Nexus", 3, 1, False, False, ap=6, rp=6, ip=3, ips=202, c=800, acq=market(GP_MARKET)),
    Structure("Lepus Drone", 1, 2, False, True, ap=1, d=100, at=100, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Lepus Drone (artifact)", formDescription="Available 2011:"),
    Structure("Lepus Drone", 1, 2, False, True, "2.0", ap=2, d=200, at=200, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Lepus Drone (artifact)", formDescription="Available 2012:"),
    Structure("Lepus Drone", 1, 2, False, True, "3.0", ap=2, d=500, at=500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Lepus Drone (artifact)", formDescription="Available 2013:"),
    Structure("Lepus Drone", 1, 2, False, False, "4.0", mp=1, ap=2, rp=1, d=1000, at=1000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Lepus Drone (artifact)", formDescription="Available 2014:"),
    Structure("Lepus Drone", 1, 2, False, False, "5.0", mp=1, ap=2, rp=2, d=2000, at=2000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Lepus Drone (artifact)", formDescription="Available 2015:"),
    Structure("Lepus Drone", 1, 2, False, False, "6.0", mp=2, ap=2, rp=2, d=3000, at=3000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Lepus Drone (artifact)", formDescription="Available 2016:"),
    Structure("Lepus Drone", 1, 2, False, False, "7.0", mp=2, ap=3, rp=2, d=4000, at=4000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Lepus Drone (artifact)", formDescription="Available 2017:"),
    Structure("Lepus Drone", 1, 2, False, False, "8.0", mp=2, ap=3, rp=3, d=5000, at=5000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Lepus Drone (artifact)", formDescription="Available 2018:"),
    Structure("Lepus Drone", 1, 2, False, False, "9.0", mp=3, ap=3, rp=3, d=6000, at=6000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Lepus Drone (artifact)", formDescription="Available 2019:"),
    Structure("Lepus Drone", 1, 2, False, False, "10.0", mp=3, ap=4, rp=3, d=7000, at=7000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Lepus Drone (artifact)", formDescription="Available 2020:"),
    Structure("Lepus Drone", 1, 2, False, False, "11.0", mp=3, ap=4, rp=4, d=8000, at=8000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Lepus Drone (artifact)", formDescription="Available 2021:"),
    Structure("Lepus Drone", 1, 2, False, False, "12.0", mp=4, ap=4, rp=4, d=9000, at=9000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Lepus Drone (artifact)", formDescription="Available 2022:"),
    Structure("Lepus Drone", 1, 2, False, False, "13.0", mp=4, ap=5, rp=4, d=10000, at=10000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Lepus Drone (artifact)", formDescription="Available 2023:"),
    Structure("Lepus Drone", 1, 2, False, False, "14.0", mp=4, ap=5, rp=5, d=11000, at=11000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Lepus Drone (artifact)", formDescription="Available 2024:"),
    Structure("Lepus Drone", 1, 2, False, False, "15.0", mp=5, ap=5, rp=5, d=12000, at=12000, c=200, acq=market(GP_MARKET), alternatePageName="Lepus Drone (artifact)", formDescription="Available 2025:"),
    Structure("Lepus Drone", 1, 2, False, False, "16.0", mp=5, ap=6, rp=5, d=13000, at=13000, c=200, acq=market(GP_MARKET)),
    Structure("Auric Lepus Drone", 1, 2, False, True, ap=2, d=250, at=250, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Auric Lepus Drone (artifact)", formDescription="Available 2011:"),
    Structure("Auric Lepus Drone", 1, 2, False, True, "2.0", ap=3, d=400, at=400, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Auric Lepus Drone (artifact)", formDescription="Available 2012:"),
    Structure("Auric Lepus Drone", 1, 2, False, True, "3.0", ap=3, rp=1, d=1500, at=1500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Auric Lepus Drone (artifact)", formDescription="Available 2013:"),
    Structure("Auric Lepus Drone", 1, 2, False, False, "4.0", mp=1, ap=3, rp=2, d=3000, at=3000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Auric Lepus Drone (artifact)", formDescription="Available 2014:"),
    Structure("Auric Lepus Drone", 1, 2, False, False, "5.0", mp=2, ap=3, rp=2, d=5000, at=5000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Auric Lepus Drone (artifact)", formDescription="Available 2015:"),
    Structure("Auric Lepus Drone", 1, 2, False, False, "6.0", mp=3, ap=3, rp=3, d=7000, at=7000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Auric Lepus Drone (artifact)", formDescription="Available 2016:"),
    Structure("Auric Lepus Drone", 1, 2, False, False, "7.0", mp=3, ap=4, rp=3, d=10000, at=10000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Auric Lepus Drone (artifact)", formDescription="Available 2017:"),
    Structure("Auric Lepus Drone", 1, 2, False, False, "8.0", mp=3, ap=4, rp=4, d=14000, at=14000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Auric Lepus Drone (artifact)", formDescription="Available 2018:"),
    Structure("Auric Lepus Drone", 1, 2, False, False, "9.0", mp=4, ap=4, rp=4, d=18000, at=18000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Auric Lepus Drone (artifact)", formDescription="Available 2019:"),
    Structure("Auric Lepus Drone", 1, 2, False, False, "10.0", mp=4, ap=5, rp=4, d=22000, at=22000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Auric Lepus Drone (artifact)", formDescription="Available 2020:"),
    Structure("Auric Lepus Drone", 1, 2, False, False, "11.0", mp=4, ap=5, rp=5, d=26000, at=26000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Auric Lepus Drone (artifact)", formDescription="Available 2021:"),
    Structure("Auric Lepus Drone", 1, 2, False, False, "12.0", mp=5, ap=5, rp=5, d=28000, at=28000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Auric Lepus Drone (artifact)", formDescription="Available 2022:"),
    Structure("Auric Lepus Drone", 1, 2, False, False, "13.0", mp=5, ap=6, rp=5, d=30000, at=30000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Auric Lepus Drone (artifact)", formDescription="Available 2023:"),
    Structure("Auric Lepus Drone", 1, 2, False, False, "14.0", mp=5, ap=6, rp=6, d=32000, at=32000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], alternatePageName="Auric Lepus Drone (artifact)", formDescription="Available 2024:"),
    Structure("Auric Lepus Drone", 1, 2, False, False, "15.0", mp=6, ap=6, rp=6, d=34000, at=34000, c=400, acq=market(GP_MARKET), alternatePageName="Auric Lepus Drone (artifact)", formDescription="Available 2025:"),
    Structure("Auric Lepus Drone", 1, 2, False, False, "16.0", mp=6, ap=7, rp=6, d=36000, at=36000, c=400, acq=market(GP_MARKET)),
    Structure("Supel Interphase Portal", 3, 1, False, False, ap=6, rp=6, ip=3, ips=202, c=800, acq=market(GP_MARKET)),
    Structure("Supel Chromavault", 1, 1, False, False, mpp=5, mps=7700, app=5, aps=7700, rpp=5, rps=7700, ipp=5, acq=market(GP_MARKET)),
    Structure("Supel Chromavault", 1, 1, False, False, "2.0", mpp=6, mps=8400, app=6, aps=8400, rpp=6, rps=8400, ipp=6, c=700, acq=market(GP_MARKET), formDescription="Upgrade using [[Chromavault Exolock]]:"),
    Structure("Supel Chromavault", 1, 1, False, False, "3.0", mpp=7, mps=9100, app=7, aps=9100, rpp=7, rps=9100, ipp=7, c=1400, acq=market(GP_MARKET)),
    Structure("Genoform Reservoir", 1, 1, False, False, ap=2, rps=3500, ip=1, acq=market(GP_MARKET)),
    Structure("Genoform Reservoir", 1, 1, False, False, "II", ap=3, rp=1, rps=3500, ip=2, ips=180, acq=market(GP_MARKET)),
    Structure("Phylogenetic Core", 1, 1, False, False, rpp=8, ip=1, acq=market(GP_MARKET)),
    Structure("Phylogenetic Core", 1, 1, False, False, "II", ap=1, rp=1, rpp=8, ip=2, ips=180, acq=market(GP_MARKET)),
    Structure("Elios Heliacal Plant", 1, 1, False, False, mp=4, ap=1, acq=market(GP_MARKET)),
    Structure("Elios Heliacal Plant", 1, 1, False, False, "(Upgraded)", mp=5, ap=2, acq=market(GP_MARKET), formDescription="Upgrade using [[Heliacal Solar Boost]]:"),
    Structure("Elios Ignis Tower", 1, 1, False, False, mp=2, ap=1, rp=3, cp=22, acq=market(GP_MARKET)),
    Structure("Chuhn Exo-Logistics Center", 1, 1, False, False, ap=4, acq=market(GP_MARKET)),
    Structure("Chuhn Exo-Logistics Gridport", 1, 1, False, False, mp=2, ap=6, acq=market(GP_MARKET), alternatePageName="Chuhn Exo-Logistics Center", formDescription="Upgrade with Chuhn Exo-Logistics Gridport"),
    Structure("Chuhn Scrapyard", 1, 1, False, False, mp=4, ap=2, acq=market(GP_MARKET)),
    Structure("Chuhn Scrap Depot", 1, 1, False, False, mp=6, ap=3, acq=market(GP_MARKET), alternatePageName="Chuhn Scrapyard", formDescription="Upgrade with Chuhn Scrapyard Upgrade:"),
    Structure("Chuhn Trading Hub", 1, 1, False, False, mp=2, ap=2, rp=1, p=7000, acq=market(GP_MARKET), alternatePageName="Chuhn Trading Post", formDescription="Upgrade using a Chuhn Trading Post on a version that was not doubled:"),
    Structure("Chuhn Trading Hub", 1, 1, False, False, "(Upgraded)", mp=3, ap=3, rp=2, p=9000, acq=market(GP_MARKET), alternatePageName="Chuhn Trading Post", formDescription="Upgrade using a Chuhn Trading Post on a version that was doubled:"),
    Structure("Chuhn Trading MegaHub", 1, 1, False, False, mp=3, ap=3, rp=2, ip=1, p=12000, acq=market(GP_MARKET), alternatePageName="Chuhn Trading Post"),
    Structure("Chuhn Trading MegaHub", 1, 1, False, False, "(Upgraded)", mp=4, ap=4, rp=3, p=14000, acq=market(GP_MARKET), alternatePageName="Chuhn Trading Post"),
    Structure("Chuhn InterMarket Caster", 1, 1, False, False, ap=1, app=1, rp=1, acq=market(GP_MARKET)),
    Structure("Chuhn InterMarket Caster", 1, 1, False, False, "v2", ap=2, app=1, rp=3, acq=market(GP_MARKET)),
    Structure("Chuhn InterMarket Caster", 1, 1, False, False, "v3", ap=3, app=2, rp=3, acq=market(GP_MARKET)),
    Structure("Chuhn InterMarket Caster", 1, 1, False, False, "v4", ap=4, app=3, rp=5, acq=market(GP_MARKET)),
    Structure("Bane Generator", 2, 1, False, True, mp=3, ap=2, at=500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Bane Generator", 2, 1, False, True, "II", mp=3, ap=3, at=800, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Bane Generator", 2, 1, False, True, "III", mp=4, ap=3, at=1200, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Bane Generator", 2, 1, False, True, "IV", mp=5, ap=3, at=1600, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Bane Generator", 2, 1, False, True, "V", mp=6, ap=3, at=3000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Bane Generator", 2, 1, False, False, "VI", mp=7, ap=4, at=6000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Bane Generator", 2, 1, False, False, "VII", mp=8, ap=4, at=12000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Bane Generator", 2, 1, False, False, "VIII", mp=9, ap=4, at=20000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Bane Generator", 2, 1, False, False, "IX", mp=10, ap=5, at=30000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Bane Generator", 2, 1, False, False, "X", mp=12, ap=5, at=42000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Bane Generator", 2, 1, False, False, "XI", mp=13, ap=6, at=55000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Bane Generator", 2, 1, False, False, "XII", mp=15, ap=6, at=70000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Bane Generator", 2, 1, False, False, "XIII", mp=16, ap=7, at=88000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Bane Generator", 2, 1, False, False, "XIV", mp=18, ap=7, at=100000, c=1800, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Bane Generator", 2, 1, False, False, "XV", mp=19, ap=8, at=120000, c=2200, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Bane Dark-Kiln", 0, 1, False, False, mp=3, ap=1, c=666),
    Structure("HyperNexus Power Shunt", 1, 1, False, False, mpp=6, app=6, rpp=6, ipp=6, dp=20, acq=market(GP_MARKET)),
    Structure("T.O. Harvest Vault", 2, 2, False, False, mp=3, mps=2000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "- Upgraded", mp=4, mps=2500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "II", mp=3, mps=3000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "II - Upgraded", mp=4, mps=3500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "III", mp=3, mps=4000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "III - Upgraded", mp=4, mps=4500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "IV", mp=4, mps=5000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "IV - Upgraded", mp=5, mps=5500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "V", mp=6, mps=6000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "V - Upgraded", mp=7, mps=6500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "VI", mp=8, mps=7000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "VI - Upgraded", mp=9, mps=7500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "VII", mp=10, mps=8000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "VII - Upgraded", mp=11, mps=8500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "VIII", mp=12, mps=9000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "VIII - Upgraded", mp=13, mps=9500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "IX", mp=13, mps=10000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "IX - Upgraded", mp=14, mps=10500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "X", mp=16, mps=11000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "X - Upgraded", mp=17, mps=11500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "XI", mp=18, mps=12000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "XI - Upgraded", mp=19, mps=12500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "XII", mp=20, mps=13000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "XII - Upgraded", mp=21, mps=13500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "XIII", mp=22, mps=14000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "XIII - Upgraded", mp=23, mps=14500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "XIII", mp=22, mps=14000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "XIII - Upgraded", mp=23, mps=14500, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE], formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "XIV", mp=24, mps=15000, c=1100, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "XV", mp=26, mps=16000, c=1500, pp=20),
    Structure("T.O. Harvest Vault", 2, 2, False, False, "XV - Upgraded", mp=27, mps=16500, c=1700, pp=24),
    Structure("Scruuge Hoarding Vault", 2, 2, False, True, ap=3, aps=4000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, True, "II", ap=3, aps=5000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, True, "III", ap=3, aps=6000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, True, "IV", ap=3, aps=7000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, True, "IV", ap=3, aps=7000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, True, "V", ap=3, aps=8000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, False, "VI", ap=4, aps=9000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, False, "VII", ap=4, aps=10000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, False, "VIII", ap=4, aps=11000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, False, "IX", ap=4, aps=12000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, False, "X", ap=5, aps=13000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, False, "XI", ap=5, aps=14000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, False, "XII", ap=6, aps=15000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, False, "XIII", ap=6, aps=16000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, False, "XIII", ap=6, aps=16000, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, False, "XIV", ap=7, aps=17000, c=1100, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Hoarding Vault", 2, 2, False, False, "XV", ap=7, aps=18000, c=1300, acq=market(GP_MARKET), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Scruuge Plunderhaven", 2, 2, False, False, ap=6, ip=1, cp=22),
    Structure("Scruuge Toll-Station", 0, 1, False, False, mp=1, mpp=1, app=1, rpp=1, ip=1, ipp=1),
    Structure("Scruuge Toll-Station", 0, 1, False, False, "v2", mp=1, mpp=1, ap=2, app=1, rpp=1, ip=1, ipp=1),
    Structure("Scruuge Toll-Station", 0, 1, False, False, "v3", mp=1, mpp=2, ap=2, app=2, rpp=2, ip=1, ipp=2),
    Structure("Scruuge Toll-Station", 0, 1, False, False, "v4", mp=3, mpp=2, ap=2, app=2, rpp=2, ip=2, ipp=2),
    Structure("Mineral Storage Silo-Tower", 2, 5, False, False, mps=2300, c=200, acq=evo(), alternatePageName="Mineral Storage Tower", formDescription="When upgraded with a Mineral Silo-Tower Upgrade"),
    Structure("Artifact Relic-Warehouse", 2, 5, False, False, aps=4300, c=200, acq=evo(), alternatePageName="Artifact Warehouse"),
    Structure("Polychoron RelicVault", 1, 1, False, False, mps=1000, aps=2000, rps=1000, acq=evo(), alternatePageName="Polychoron Vault", formDescription="If artifact storage boosted with [[Polychoron Adapter]]:"),
    Structure("Polychoron DataVault", 1, 1, False, False, mps=1000, aps=1000, rps=2000, acq=evo(), alternatePageName="Polychoron Vault", formDescription="If research storage boosted with [[Polychoron Adapter]]:"),
    Structure("Polychoron OreVault", 1, 1, False, False, mps=2000, aps=1000, rps=1000, acq=evo(), alternatePageName="Polychoron Vault", formDescription="If research storage boosted with [[Polychoron Adapter]]:"),
    Structure("Dais of Deceit", 1, 1, False, False, mpp=2, app=2, rpp=2, ip=1, ipp=2, c=900, acq=evo()),
    Structure("Micro-Raix Cyclotron", 1, 1, False, False, mpp=2, app=2, rpp=2, rps=2000, ipp=2, ips=200, acq=evo()),
    Structure("Micro-Raix Cyclotron", 1, 1, False, False, "2", mpp=2, app=2, rpp=2, rps=2600, ipp=2, ips=260, acq=evo()),
    Structure("Micro-Raix Cyclotron", 1, 1, False, False, "3", mpp=3, app=3, rpp=3, rps=3200, ipp=3, ips=320, acq=evo()),
    Structure("Bio-Luminous Orb", 1, 1, False, False, mpp=3, app=3, rpp=3, ip=1, ipp=3, cp=22, acq=evo()),
    Structure("Spire of Dominion", 2, 1, True, False, ip=4, ips=400, acq=medal(), limitNotes=[SPIRE_NOTE]),
    Structure("Spire of High Dominion", 2, 1, True, False, ip=6, ips=600, acq=medal(), limitNotes=[SPIRE_NOTE]),
    Structure("Spire of Scruuge Dominion", 2, 1, True, False, ap=4, aps=1500, ip=4, acq=medal(), limitNotes=[SPIRE_NOTE]),
    Structure("Spire of Cybernetic Dominion", 2, 1, True, False, rp=8, ip=4, ips=500, c=800, acq=medal(), limitNotes=[SPIRE_NOTE]),
    Structure("Spire of Supel Dominion", 2, 1, True, False, mp=8, ip=5, ips=500, acq=medal(), limitNotes=[SPIRE_NOTE]),
    Structure("Exalted DarkForge", 3, 1, True, False, mp=8, ap=6, ip=3, cp=22, acq=medal()),
    Structure("Xenoform Drone", 0, 1, True, False, mpp=1, app=1, rpp=1, ipp=1, acq=medal()),
    Structure("Xenoform Drone", 0, 1, True, False, "(Tripled)", mpp=3, app=3, rpp=3, ipp=3, acq=medal()),
    Structure("Vault of Terra", 1, 1, True, False, mps=2000, aps=2000, rps=2000, acq=medal()),
    Structure("Vault of Terra", 1, 1, True, False, "(Doubled)", mps=4000, aps=4000, rps=4000, acq=medal()),
    Structure("Species Evolution Lab", 3, 1, True, False, ap=5, rp=8, ip=3, pp=42, acq=medal()),
    Structure("Q-Pedd Docking Station", 1, 1, True, False, mp=3, ap=2, rp=2, acq=medal()),
    Structure("Omnistream Gateway", 2, 1, True, True, mp=3, ap=3, rp=3, acq=medal()),
    Structure("Throne of the Revered", 1, 1, True, False, mp=4, mpp=4, ap=4, app=4, rp=4, rpp=4, ipp=4, acq=medal()),
    Structure("Throne of the Revered", 1, 1, True, False, "- Mark 2", mp=5, mpp=8, ap=5, app=8, rp=5, rpp=8, ipp=8, acq=medal(), formDescription="Upgrade using ability (costs 50,000 [[Exotic Matter]] and 1 charge):"),
    Structure("Throne of the Revered", 1, 1, True, False, "- Mark 3", mp=7, mpp=16, ap=7, app=16, rp=7, rpp=16, ipp=16, acq=medal(), formDescription="Upgrade using ability (costs 100,000 [[Exotic Matter]] and 1 charge after a 3 month wait):"),
    Structure("Throne of the Revered", 1, 1, True, False, "- Mark 4", mp=9, mpp=30, ap=9, app=30, rp=9, rpp=30, ipp=30, acq=medal(), formDescription="Upgrade using ability (costs 250,000 [[Exotic Matter]] and 1 charge after another 6 month wait):"),
    Structure("XTS-9 Silo", 1, 1, True, True, mp=5, mps=1000, p=-400, acq=medal()),
    Structure("Astrometrics Orrery", 1, 1, True, False, ap=1, rp=3, acq=medal()),
    Structure("Astrometrics Orrery", 1, 1, True, False, "v2", ap=2, rp=5, rps=500, acq=medal(), formDescription="Upgrade using ability (costs 1111 [[Complex Tech Parts]] and requires 1500+ planets scanned in database):"),
    Structure("Astrometrics Orrery", 1, 1, True, False, "v3", ap=3, rp=7, rps=1100, acq=medal(), formDescription="Upgrade using ability (costs 2222 [[Complex Tech Parts]] and requires 2200+ planets scanned in database):"),
    Structure("Astrometrics Orrery", 1, 1, True, False, "v4", ap=4, rp=9, rps=1800, acq=medal(), formDescription="Upgrade using ability (costs 3333 [[Complex Tech Parts]] and requires 2900+ planets scanned in database):"),
    Structure("Astrometrics Orrery", 1, 1, True, False, "v5", ap=6, rp=11, rps=2600, acq=medal(), formDescription="Upgrade using ability (costs 4444 [[Complex Tech Parts]] and requires 3500+ planets scanned in database):"),
    Structure("Miser's Gift-Bunker", 2, 1, False, False, mps=4400, ap=4, aps=4400, c=1100, cp=22),
    Structure("Elios Flare Probe", 0, 1, True, False, "II", mpp=2, ap=2, ip=1, ips=101, acq=medal()),
    Structure("Xiphos Heist Outpost", 1, 1, False, False, "(1)", mp=1, rp=1, acq=npc("Crimson Xiphos"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Xiphos Heist Outpost", 1, 1, False, False, "(5,785)", mp=2, ap=1, rp=2, acq=npc("Crimson Xiphos"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Xiphos Heist Outpost", 1, 1, False, False, "(7,022)", mp=3, ap=1, rp=2, acq=npc("Crimson Xiphos"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Xiphos Heist Outpost", 1, 1, False, False, "(9,000)", mp=3, mps=303, ap=1, rp=2, c=303, acq=npc("Crimson Xiphos"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Xiphos Heist Outpost", 1, 1, False, False, "(10,000)", mp=3, mps=303, ap=2, rp=2, rps=303, c=303, acq=npc("Crimson Xiphos"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Xiphos Heist Outpost", 1, 1, False, False, "(20,000)", mp=4, mps=303, ap=2, aps=303, rp=2, rps=303, c=303, acq=npc("Crimson Xiphos"), nameNotes=[SHIP_SIZE_NOTE]),
    Structure("Crimson Rift Aperture", 1, 1, False, True, ap=1, at=400, c=200, acq=npc("Kelethor, Crimson Hauler")),
    Structure("Crimson Rift Aperture", 1, 1, False, True, "(Doubled)", ap=2, at=800, c=400, acq=npc("Kelethor, Crimson Hauler")),
    Structure("Dark Pylon Shifter", 1, 1, False, False, d=400, c=90, acq=npc("Dark MegaComplex")),
    Structure("Dark Anti-Beacon", 1, 1, False, True, d=500, c=150, acq=npc("Dark Command Nexus")),
    Structure("Dark Null Beacon", 1, 1, False, False, d=1000, dp=10, c=300, acq=npc("Pevreon, Dark Specialist"), alternatePageName=("Dark Anti-Beacon"), formDescription=("Upgrade with Dark Null Beacon Upgrade:")),
    Structure("Dark Void Beacon", 1, 1, False, False, ap=1, rp=1, d=2000, dp=20, c=600, acq=npc("Mythrax, Dark Messenger"), alternatePageName="Dark Anti-Beacon", formDescription="Upgrade with Dark Void Beacon Upgrade:"),
    Structure("Dark Smugglers Vault", 1, 1, False, False, mps=3300, aps=3300, acq=npc("Mythrax, Dark Messenger")),
    Structure("Lazuli Pylon", 1, 3, False, True, id=600, acq=npc("Renegar, Lazuli Station")),
    Structure("Lazuli Darkmines", 1, 2, False, True, at=600, atp=25, acq=npc("Rethion, Lazuli Superhauler")),
    Structure("Lazuli Darkmines", 1, 2, False, True, "(Aeon)", at=600, atp=25, cp=15),
    Structure("Lazuli Darkmine Cluster", 1, 2, False, True, at=1200, atp=30, acq=npc("Attiroth, Lazuli Carrier")),
    Structure("Lazuli Darkmine Cluster", 1, 2, False, True, "(Aeon)", at=1200, atp=30, cp=15),
    Structure("Lazuli Shipyard", 1, 1, False, False, ap=1, rp=3, dp=20, acq=npc("Balthion, Lazuli Flagship")),
    Structure("Obscura Lab", 1, 1, False, False, ap=1, rp=2, c=420, acq=npc("RSL Obscura-Shaper")),
    Structure("Obscura Lab", 1, 1, False, False, "v2", ap=2, rp=4, c=840, acq=npc("RSL Obscura-Shaper"), formDescription="Upgarde using ability (costs 42 [[Blue Badges]] and 1 charge, and requires Hacker / Physicist / Spy profession):"),
    Structure("Obscura Lab", 1, 1, False, False, "v3", ap=2, rp=6, c=1260, acq=npc("RSL Obscura-Shaper"), formDescription="Upgarde using ability (costs 42 [[Blue Badges]] and 1 charge, and requires Hacker / Physicist / Spy profession):"),
    Structure("Obscura Lab", 1, 1, False, False, "v4", ap=3, rp=7, rps=420, c=1260, acq=npc("RSL Obscura-Shaper"), formDescription="Upgarde using ability (costs 88 [[Blue Badges]] and 1 charge):"),
    Structure("Sha'din Grid Network", 1, 1, False, True, rp=2, acq=npc("Sha'din AI Matrix"), limitNotes=[SHADIN_STRUCTURE_NOTE]),
    Structure("Sha'din Hypergrid Network", 1, 1, False, True, rp=2, d=200, acq=npc("Sha'din Hypergrid"), limitNotes=[SHADIN_STRUCTURE_NOTE]),
    Structure("Sha'din Hyperport Network", 1, 1, False, True, rp=3, d=400, acq=npc("Sha'din Hyperport"), limitNotes=[SHADIN_STRUCTURE_NOTE]),
    Structure("Interrogation Center", 1, 1, False, True, rp=2, d=200, acq=npc("Svax, Stryll Punisher"), limitNotes=[STRYLL_INTERROGATION_LIMIT]),
    Structure("Interrogation Stronghold", 1, 1, False, True, rp=2, d=300, acq=npc("Xavox, Stryll Punisher"), limitNotes=[STRYLL_INTERROGATION_LIMIT]),
    Structure("Silthion Gas Vesicle", 1, 1, False, True, rp=2, c=150, acq=npc("Silthion Queen")),
    Structure("Silthion T-Plasma Vesicle", 1, 1, False, True, ap=1, rp=3, c=300, acq=npc("Silthion Hybrid Cluster")),
    Structure("Assembly of Tri-Unity", 2, 2, False, False, ap=2, rp=2, ip=1, acq=npc("Empyreal Envoy")),
    Structure("Empyreal Fire-Citadel", 5, 2, False, False, mp=5, ap=3, rp=1, ip=3, acq=npc("Empyreal Envoy")),
    Structure("Empyreal Fire-Citadel", 5, 2, False, False, "II", mp=5, ap=3, rp=1, ip=5, ips=200),
    Structure("Empyreal Garden-Citadel", 5, 2, False, False, ap=5, ip=3, acq=npc("Empyreal Envoy")),
    Structure("Empyreal Garden-Citadel", 5, 2, False, False, "II", ap=5, ip=5, ips=200),
    Structure("Empyreal Ice-Citadel", 5, 2, False, False, mp=1, ap=3, rp=5, ip=3, acq=npc("Empyreal Envoy")),
    Structure("Empyreal Ice-Citadel", 5, 2, False, False, "II", mp=1, ap=3, rp=5, ip=5, ips=200),
    Structure("Elios Power Junction", 1, 1, False, False, mp=2, mpp=5, ap=1, acq=npc("Cosmiren, Elios Luminary")),
    Structure("Elios Powervault", 1, 1, False, False, mp=1, mps=1000, ap=1, acq=npc("Cosmiren, Elios Luminary")),
    Structure("Elios Phoenix Powervault", 1, 1, False, False, mp=2, mps=2000, ap=2, acq=npc("Elios Phoenix"), alternatePageName="Elios Powervault", formDescription="Upgrade with Elios Phoenix Powervault Upgrade:"),
    Structure("Elios Flare Probe", 0, 1, False, False, mpp=1, ap=1, acq=npc("Elios Phoenix")),
    Structure("Aurelios Star-Plant", 1, 1, False, False, mp=3, ap=1, app=2, acq=npc("Aurelios, Helio-Flare")),
    Structure("Aurelios Star-Plant", 1, 1, False, False, "II", mp=4, ap=2, app=3, acq=npc("Coronethis, Elios Forge")),
    Structure("Aurelios Voltarium", 1, 1, False, False, mp=4, mpp=3, mps=1500, ap=1, acq=npc("Aurelios, Helio-Flare")),
    Structure("Aurelios Voltarium", 1, 1, False, False, "II", mp=6, mpp=5, mps=1700, ap=2, acq=npc("Coronethis, Elios Forge")),
    Structure("Elios Micro-Star Cradle", 2, 1, False, False, mp=5, mpp=2, app=2, rpp=2, ipp=2, acq=npc("Coronethis, Elios Forge")),
    Structure("Fornax Jewel", 1, 1, False, False, mp=2, mpp=5, acq=npc("Chuhn Merchant")),
    Structure("Fornax Jewel", 1, 1, False, False, "(Doubled)", mp=4, mpp=10, acq=npc("Chuhn Merchant"), formDescription="If the planet has moon(s) or rings when built:"),
    Structure("Orion Menagerie", 1, 1, False, False, ap=2, p=5000, acq=npc("Chuhn Merchant")),
    Structure("Triangulum Sparkmatter", 1, 1, False, False, "(1)", ap=1, acq=npc("Chuhn Merchant"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Triangulum Sparkmatter", 1, 1, False, False, "(2)", ap=1, rp=2, acq=npc("Chuhn Merchant"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Triangulum Sparkmatter", 1, 1, False, False, "(3)", ap=2, rp=1, acq=npc("Chuhn Merchant"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Triangulum Sparkmatter", 1, 1, False, False, "(4)", rp=2, acq=npc("Chuhn Merchant"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Quadrigulum Sparkmatter", 1, 1, False, False, "(1)", mp=3, rp=1, acq=npc("Chuhn Merchant"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Quadrigulum Sparkmatter", 1, 1, False, False, "(2)", ap=3, rp=1, acq=npc("Chuhn Merchant"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Quadrigulum Sparkmatter", 1, 1, False, False, "(3)", mp=1, rp=3, acq=npc("Chuhn Merchant"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Pentragulum Sparkmatter", 1, 1, False, False, "(1)", mp=3, rp=2, acq=npc("Chuhn Merchant"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Pentragulum Sparkmatter", 1, 1, False, False, "(2)", ap=4, rp=1, acq=npc("Chuhn Merchant"), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Bane Krow Probe", 0, 5, False, False, "- Type 1", ap=1, dp=-5, acq=npc("Bane Krow"), nameNotes=[RANDOM_PLACEMENT_NOTE]),
    Structure("Bane Krow Probe", 0, 5, False, False, "- Type 2", mp=1, rp=1, dp=-10, acq=npc("Bane Krow"), nameNotes=[RANDOM_PLACEMENT_NOTE]),
    Structure("Bane Krow Probe", 0, 5, False, False, "- Type 3", mp=1, ap=1, rp=1, dp=-15, acq=npc("Bane Krow"), nameNotes=[RANDOM_PLACEMENT_NOTE]),
    Structure("Hall of Torment", 1, 1, False, True, atp=25, p=-200, id=1000, acq=npc("Ephemerar, Bane Stalker"), limitNotes=[BANE_HALL_LIMIT]),
    Structure("Hall of Extreme Torment", 1, 1, False, True, atp=30, p=-500, id=2000, acq=npc("Ghastius, Bane Fiend"), limitNotes=[BANE_HALL_LIMIT]),
    Structure("Hall of Unrelenting Torment", 1, 1, False, True, atp=40, p=-1000, id=4000, acq=npc("Illuciar, Bane Phantasm"), limitNotes=[BANE_HALL_LIMIT]),
    Structure("Hall of Unfathomable Torment", 1, 1, False, True, mp=2, ap=2, atp=60, p=-9000, acq=npc("Abyssiod, Infernal Carrier"), limitNotes=[BANE_HALL_LIMIT]),
    Structure("Bane Quad-Phase Inhibitor", 1, 2, False, False, ap=1, rp=2, id=4000, ic=4, acq=npc("Illuciar, Bane Phantasm")),
    Structure("Bane Dark-Infernum", 2, 1, False, False, mp=3, ap=2, dp=42, acq=npc("Abyssiod, Infernal Effigy")),
    Structure("Bane Dark-Infernum", 2, 1, False, False, "(Upgraded)", mp=5, ap=5, dp=42, acq=npc("Abyssiod, Infernal Effigy")),
    Structure("Bane Doom Silo", 1, 1, False, False, "(1)", mp=1, ap=2, aps=666, rp=1, c=666, acq=npc("Abyssiod, Infernal Effigy")),
    Structure("Bane Doom Silo", 1, 1, False, False, "(2)", ap=1, rp=4, rps=666, c=666, acq=npc("Abyssiod, Infernal Effigy")),
    Structure("Bane Doom Silo", 1, 1, False, False, "(3)", mp=4, mps=666, ap=1, c=666, acq=npc("Abyssiod, Infernal Effigy")),
    Structure("Lepus Gateway", 1, 1, False, True, mp=1, rp=1, pp=20, acq=npc("Bio-Con Minor, Lepus Elite")),
    Structure("Lepus Chromatic Gateway", 1, 1, False, True, mp=1, ap=1, rp=1, pp=30, acq=npc("Bio-Con Alpha, Lepus Elite")),
    Structure("Lepus Bio-Mech Gateway", 1, 1, False, True, mp=2, ap=1, rp=2, pp=40, acq=npc("Bio-Con Prime, Lepus Base")),
    Structure("Lepus Bio-Mech Hypergate", 1, 1, False, False, mp=3, ap=1, rp=3, pp=60, acq=npc("Bio-Con X32, Lepus Elite")),
    Structure("Lepus C-34 Gateway", 1, 1, False, False, mp=4, ap=1, rp=4, pp=80, acq=npc("C-34 Hypersync, Lepus Base")),
    Structure("Lepus C-34 Hypergate", 1, 1, False, False, mp=5, ap=2, rp=5, pp=90, acq=npc("C-34 Hypersync, Lepus Base"), alternatePageName="Lepus C-34 Gateway", formDescription="Upgrade with C-34 Hypergate Upgrade:"),
    Structure("Lepus C-34 Fluxgate", 1, 1, False, False, mp=6, ap=3, rp=6, pp=100, acq=npc("C-34 Hypersync, Lepus Base"), alternatePageName="Lepus C-34 Gateway", formDescription="Upgrade with C-34 Fluxgate Upgrade:"),
    Structure("Lepus C-34 Chromatic Fluxgate", 1, 1, False, False, mp=7, ap=4, rp=7, pp=120, acq=npc("C-34 Hypersync, Lepus Base"), alternatePageName="Lepus C-34 Gateway", formDescription="Upgrade with Lepus C-34 Chromatic Fluxgate Upgrade:"),
    Structure("Farselle Psi-Drone", 1, 1, False, True, mp=1, mps=200, ap=1, aps=200, rp=1, rps=200, acq=npc("Chromathis, Lepus Agent")),
    Structure("Lepus Clone-Program Tank", 1, 1, False, False, mpp=3, app=3, rpp=3, ipp=3, pp=50, acq=npc("Chromathis, Lepus Agent")),
    Structure("Auric Lepus Clone-Program Tank", 1, 1, False, False, mpp=6, app=6, rpp=6, ipp=6, pp=100, acq=npc("Chromathis, Lepus Agent")),
    Structure("Affection Disseminator", 1, 2, False, True, d=200, p=200, acq=npc("Q-Pedd Escapee"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Affection Disseminator", 1, 2, False, True, "2.0", rp=1, d=250, p=250, acq=npc("Q-Pedd Escapee"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Affection Disseminator", 1, 2, False, True, "3.0", rp=1, d=500, p=500, acq=npc("Q-Pedd Escapee"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Affection Disseminator", 1, 2, False, True, "4.0", rp=1, d=800, p=800, acq=npc("Q-Pedd Escapee"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Affection Disseminator", 1, 2, False, True, "5.0", rp=1, d=1200, p=1200, acq=npc("Q-Pedd Escapee"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Affection Disseminator", 1, 2, False, True, "6.0", rp=1, d=1600, p=1600, acq=npc("Q-Pedd Escapee"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Affection Disseminator", 1, 2, False, True, "7.0", rp=1, d=2500, p=2500, acq=npc("Q-Pedd Escapee"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Affection Disseminator", 1, 2, False, True, "8.0", rp=1, d=3700, p=3700, acq=npc("Q-Pedd Escapee"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Affection Disseminator", 1, 2, False, True, "9.0", rp=1, d=5000, p=5000, acq=npc("Q-Pedd Escapee"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Affection Disseminator", 1, 2, False, True, "10.0", rp=1, d=6500, p=6500, acq=npc("Q-Pedd Escapee"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Affection Disseminator", 1, 2, False, True, "11.0", rp=1, d=8500, p=8500, acq=npc("Q-Pedd Escapee"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Affection Disseminator", 1, 2, False, True, "12.0", rp=1, d=10000, p=10000, acq=npc("Q-Pedd Escapee")),
    Structure("Affection Disseminator Ultracore", 1, 2, False, False, rp=2, d=20000, p=20000, acq=npc("Affection Disseminator"), alternatePageName="Affection Disseminator", formDescription="Upgrade with Dissemination Ultracore:"),
    Structure("Affection Disseminator Megacore", 1, 2, False, False, ap=1, rp=3, d=30000, p=30000, acq=npc("Affection Disseminator"), alternatePageName="Affection Disseminator", formDescription="Upgrade with Dissemination Megacore:"),
    Structure("Q-Pedd Probe", 0, 2, False, False, rp=1, rpp=1, acq=npc("Q-Pedd 1 0V3 Probe")),
    Structure("Streveldan Probe-Bay", 0, 2, False, False, ap=1, rp=2, rpp=2, acq=scanning("QPedd (seasonal event)"), alternatePageName="Q-Pedd Probe", formDescription="Upgrade with Streveldan Probe-Bay (costs 4444 [[Exotic Matter]])"),
    Structure("A.I. Emotion Core", 1, 1, False, True, ap=1, rp=2, at=500, acq=npc("QPP1-L05, Q-Pedd Prototype")),
    Structure("A.I. Emotion Bi-Core", 1, 1, False, False, ap=2, rp=3, at=500, acq=scanning("QPedd (seasonal event)"), alternatePageName="A.I. Emotion Core", formDescription="Upgrade with A.I. Emotion Bi-Core"),
    Structure("Scruuge Calibration Chamber", 1, 1, False, False, mp=1, ap=1, c=200, acq=npc("Scruuge Vicar")),
    Structure("Scruuge Calibration Chamber", 1, 1, False, False, "(Upgraded)", mp=1, ap=1, c=400, acq=npc("Scruuge Vicar"), formDescription="If placed while you have the [[Thraccti, Scruuge Defector]] ally:"),
    Structure("Scruuge Hovertank", 1, 1, False, False, ap=1, dp=15, atp=15, acq=npc("Zebeeren, Scruuge Despot")),
    Structure("T.O. TerraFounder", 1, 1, False, False, mpp=5, app=5, rpp=5, ipp=5, p=3000, acq=npc("T.O. Gridrunner")),
    Structure("T.O. TerraFounder", 1, 1, False, False, "- Upgraded", mp=1, mpp=5, ap=1, app=5, rp=1, rpp=5, ipp=5, p=6000, acq=npc("T.O. Gridrunner"), formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("Archotage Transmitter", 1, 1, False, False, ap=1, c=200, pp=40, acq=npc("Archotage Transmitter (NPC)"), alternatePageName="Archotage Transmitter (artifact)"),
    Structure("Archotage Transmitter", 1, 1, False, False, "- Upgraded", mp=1, ap=1, c=400, pp=50, acq=npc("Archotage Transmitter (NPC)"), alternatePageName="Archotage Transmitter (artifact)", formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("Sarkonis Hardshell", 1, 1, False, False, mp=1, mpp=5, dp=5, acq=npc("Sarkonis, Harvest Leader")),
    Structure("Sarkonis Hardshell", 1, 1, False, False, "- Upgraded", mp=2, mpp=8, dp=8, acq=npc("Sarkonis, Harvest Leader"), formDescription="Upgrade with [[Archotage Amplifier]]:"),
    Structure("Sarkonis Headquarters", 1, 1, False, True, rp=1, dp=10, p=500, acq=npc("Sarkonis, Harvest Leader")),
    Structure("Sarkonis Headquarters", 1, 1, False, False, "- Upgraded", rp=2, dp=15, p=1000, acq=npc("Sarkonis, Harvest Leader")),
    Structure("Sarkonis Omnipod", 1, 1, False, True, ap=1, atp=10, acq=npc("Sarkonis, Harvest Leader")),
    Structure("Sarkonis Omnipod", 1, 1, False, False, "- Upgraded", ap=1, rp=1, atp=20, acq=npc("Sarkonis, Harvest Leader")),
    Structure("Cygnusis AI-Core", 1, 1, False, False, ap=1, rp=3, rpp=3, d=4444, acq=npc("Cygnusis, Harvest Source-Base")),
    Structure("Cygnusis AI-Core", 1, 1, False, False, "(Doubled)", ap=2, rp=6, rpp=6, d=8888, acq=npc("Cygnusis, Harvest Source-Base"), formDescription="If built on a Terra / Gaia planet:"),
    Structure("Captured T.O. Harvester", 2, 1, False, True, mp=2, ap=1, p=160, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, True, "II", mp=2, ap=1, p=300, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, True, "III", mp=2, ap=1, p=600, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, True, "IV", mp=2, ap=1, p=1000, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, True, "V", mp=2, ap=1, p=2000, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, True, "VI", mp=2, ap=1, p=3500, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, True, "VII", mp=3, ap=1, p=5000, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, True, "VIII", mp=3, ap=1, p=8000, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, False, "IX", mp=4, ap=1, p=12000, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, False, "X", mp=5, ap=1, p=16000, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, False, "XI", mp=6, ap=1, p=20000, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, False, "XII", mp=7, ap=1, p=24000, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, False, "XIII", mp=8, ap=1, p=26000, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, False, "XIV", mp=9, ap=1, p=32000, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, False, "XV", mp=10, ap=1, p=36000, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, False, "XVI", mp=11, ap=1, p=40000, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("Captured T.O. Harvester", 2, 1, False, False, "XVI - Upgraded", mp=11, ap=1, p=80000, acq=npc("Captured T.O. Harvester"), nameNotes=[UNOBTAINABLE_NOTE]),
    Structure("T.O. Manufacturing Core", 1, 1, False, False, mp=2, ap=2, acq=blockade("T.O. HyperSeeker"), alternatePageName="Processing Core Chassis", formDescription="Upgrade with [[T.O. Manufacturing Core Upgrade]]:"),
    Structure("T.O. Fortisphere", 2, 1, False, False, ap=3, ip=1, dp=22, cp=9, acq=blockade("Valcaron, Harvest Colonizer")),
    Structure("Valcaron-Cygnusis AI-Core", 1, 1, False, False, ap=1, rp=6, rpp=3, ip=1, d=4444, acq=blockade("Valcaron, Harvest Colonizer"), formDescription="If upgraded with a Valcaron-Cygnusis Core Upgrade:", alternatePageName="Valcaron-Cygnusis Core Upgrade"),
    Structure("Valcaron-Cygnusis AI-Core", 1, 1, False, False, "(Upgraded)", ap=2, rp=9, rpp=6, ip=1, d=8888, acq=blockade("Valcaron, Harvest Colonizer"), formDescription="If built on a Terra / Gaia planet and upgraded with a Valcaron-Cygnusis Core Upgrade:", alternatePageName="Valcaron-Cygnusis Core Upgrade"),
    Structure("Akulan Gas Ingestor", 1, 1, False, True, ap=-2, rp=3, acq=blockade("Akulan Entity")),
    Structure("Gauss Chain", 2, 1, False, True, mp=1, ap=1, rp=2, d=300, acq=blockade("Allovore Entity")),
    Structure("Gauss Chain", 2, 1, False, True, "II", mp=2, ap=2, rp=4, d=600, acq=blockade("Allovore Entity"), formDescription="If you occupy 10+ Metallic, Dyson, and/or Ecumenopolis planets when this is built:"),
    Structure("ArcRift Tower", 1, 2, False, False, app=6, acq=blockade("Chaotic ArcRift Entity")),
    Structure("Scruuge Cargo Pad", 1, 1, False, False, mp=2, ap=1, d=2000, acq=blockade("Scruuge Hijacker")),
    Structure("Scruuge Cargo Pad", 1, 1, False, False, "(Doubled)", mp=4, ap=2, d=4000, acq=blockade("Scruuge Hijacker"), formDescription="If the planet has a Scruuge Calibration Center when this is built:"),
    Structure("Scruuge Growth Vats", 1, 1, False, False, ap=1, rp=2, p=5000, acq=blockade("Scruuge Hijacker")),
    Structure("Scruuge Growth Vats", 1, 1, False, False, "(Doubled)", ap=2, rp=4, p=10000, acq=blockade("Scruuge Hijacker"), formDescription="If the planet already has a [[Scruuge Hoarding Vault|Scruuge Hoarding Vault VII (or greater)]] when this is built:"),
    Structure("DM79 Datacenter", 1, 1, False, True, rp=4, acq=ct()),
    Structure("DM79 Datacenter", 1, 1, False, True, "(Upgraded)", rp=6, acq=ct(), formDescription="If the planet is not Gas:"),
    Structure("Domain Walker", 1, 2, False, True, d=600, at=600, acq=ct()),
    Structure("HyperSensor Satellite", 2, 1, False, True, ap=2, rp=2, acq=ct()),
    Structure("Hypergate", 1, 1, False, True, mp=2, ap=2, rp=2, acq=ct(), alternatePageName="Warp Gate Chassis", formDescription="Upgrade with [[Hypergate Upgrade]]:"),
    Structure("Polychoron Vault", 1, 1, False, True, mps=1000, aps=1000, rps=1000, acq=ct()),
    Structure("Resonance Inhibitor", 1, 2, False, True, c=250, id=500, acq=ct()),
    Structure("Astrobiology Ward", 1, 1, False, False, p=500, pp=50, acq=ct()),
    Structure("Galactic Concord Station", 1, 1, False, True, mp=1, ap=1, dp=10, acq=ct()),
    Structure("Galactic Concord Station", 1, 1, False, True, "II", mp=2, ap=2, dp=20, acq=ct()),
    Structure("Isolation Bureau", 2, 1, False, True, mp=1, ap=1, rp=1, c=200, acq=ct()),
    Structure("Isolation Bureau", 2, 1, False, True, "(Doubled)", mp=2, ap=2, rp=2, c=400, acq=ct(), formDescription="If the planet has no other scanners when this is built:"),
    Structure("Toxic Processing Plant", 2, 1, False, True, mp=3, ap=2, atp=30, acq=ct()),
    Structure("Toxic Processing Plant", 2, 1, False, True, "(Mining)", mp=5, atp=30, acq=ct(), formDescription="If the planet is Toxic, Shattered, or Irradiated:"),
    Structure("Polaron Emitter", 1, 1, False, True, rp=1, c=100, cp=15, acq=ct()),
    Structure("Polaron Emitter", 1, 1, False, True, "(Upgraded)", mp=1, ap=1, rp=1, c=100, cp=15, acq=ct(), formDescription="If the planet has a Small Moon, Large Moons, or Planetary Rings when this is built:"),
    Structure("Perpetual HyperTurbine", 1, 1, False, False, ap=2, app=1, acq=ct()),
    Structure("Perpetual HyperTurbine", 1, 1, False, False, "II", ap=2, app=2, acq=ct(), formDescription="After completing a daily Mission:"),
    Structure("Perpetual HyperTurbine", 1, 1, False, False, "III", ap=2, app=3, acq=ct(), formDescription="After completing another daily Mission:"),
    Structure("Perpetual HyperTurbine", 1, 1, False, False, "IV", ap=2, app=4, acq=ct(), formDescription="After completing another daily Mission:"),
    Structure("Perpetual HyperTurbine", 1, 1, False, False, "V", ap=2, app=5, acq=ct(), formDescription="After completing another daily Mission:"),
    Structure("Seismic Shattermine", 1, 1, False, False, mp=2, mpp=2, ap=1, atp=6, acq=ct()),
    Structure("Seismic Shattermine", 1, 1, False, False, "(Quadrupled)", mp=8, mpp=8, ap=4, atp=24, acq=ct(), formDescription="If built on a Shattered planet:"),
    Structure("Aethercron Hold", 1, 1, False, False, ap=1, app=6, rp=3, dp=22, acq=ct()),
    Structure("Adumbrate Starport", 2, 1, False, False, mp=2, mpp=2, ap=2, app=2, rp=2, rpp=2, ipp=2, c=222, acq=ct()),
    Structure("SubVoid Darkdrone", 2, 1, False, False, "A", mp=2, ap=2, cp=22, acq=ct(), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("SubVoid Darkdrone", 2, 1, False, False, "B", mp=1, ap=3, cp=11, acq=ct(), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("SubVoid Darkdrone", 2, 1, False, False, "C", mp=4, ap=1, cp=33, acq=ct(), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("SubVoid Darkdrone", 2, 1, False, False, "D", ap=4, c=1111, cp=6, acq=ct(), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("SubVoid Darkdrone", 2, 1, False, False, "E", mp=1, ap=3, c=2222, acq=ct(), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("SubVoid Darkdrone", 2, 1, False, False, "F", ap=5, c=555, acq=ct(), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("SubVoid Darkdrone", 2, 1, False, False, "G", ap=6, c=111, acq=ct(), nameNotes=[RANDOM_VERSION_NOTE]),
    Structure("Nova-Stasis Unit", 1, 1, False, False, mp=2, mps=2222, ap=1, aps=1111, acq=ct()),
    Structure("Morphogenic Shift-Gate", 3, 1, False, False, ap=4, ip=1, c=900, acq=ct()),
    Structure("Morphogenic Shift-Gate", 3, 1, False, False, "(2)", ap=4, ip=2, c=1200, acq=ct(), formDescription="Upgrade with ability (costs 15 [[Green Badges]] and must be a Diplomat with 4400+ [[Influence]] contributed):"),
    Structure("Morphogenic Shift-Gate", 3, 1, False, False, "(3)", ap=6, ip=2, c=1200, acq=ct(), formDescription="Upgrade with ability (costs 18 [[Green Badges]] and requires Governor with 8800+ [[Influence]] contributed):"),
    Structure("Krionite Absorption Net", 2, 4, False, False, mp=4, ap=2, c=550, esp=150, acq=ct()),
    Structure("Monolith of Miracles", 2, 1, False, False, mp=3, ap=2, rp=3, acq=ct()),
    Structure("Monolith of Miracles", 2, 1, False, False, "v2", mp=3, mpp=2, ap=2, app=2, rp=3, rpp=2, ip=1, ipp=2, acq=ct(), formDescription="Upgrade with ability (costs 6 Aeon Badges and 4,200 Influence, and requires the planet be Large or smaller):"),
    Structure("Monolith of Miracles", 2, 1, False, False, "v3", mp=3, mpp=4, ap=2, app=4, rp=3, rpp=4, ip=2, ipp=4, acq=ct(), formDescription="Upgrade with ability (costs 9 Aeon Badges and 9,000 Influence, and requires the planet be Average or smaller):"),
    Structure("Monolith of Miracles", 2, 1, False, False, "v4", mp=3, mpp=7, ap=2, app=7, rp=3, rpp=7, ip=3, ipp=7, acq=ct(), formDescription="Upgrade with ability (costs 12 Aeon Badges and 12,000 Influence, and requires the planet be Small or smaller):"),
    Structure("Cryo-Foundry Ice Drill", 0, 1, False, False, mpp=2, acq=event()),
    Structure("Cryo-Foundry Ice Drill", 0, 1, False, False, "(Doubled)", mpp=4, acq=event()),
    Structure("Xenotypic Mutants", 0, 2, False, False, mp=2, ap=1, rp=2, acq=event()),
    Structure("Cryo-Foundry Battery", 0, 1, False, False, app=1, acq=event()),
    Structure("Cryo-Foundry Battery", 0, 1, False, False, "(Doubled)", app=2, acq=event()),
    Structure("Visage of the Dark One", 0, 1, False, False, mpp=2, app=2, rpp=2, ipp=2, pp=-80, acq=event()),
    Structure("Chuhn Shipyard", 1, 1, False, False, mp=2, ap=2, atp=33, acq=event() + ", " + npc("Chuhn Trade Liner")),
    Structure("Galakis Monument", 0, 1, False, False, ip=1, pp=9),
    Structure("Galakis Monument", 0, 1, False, False, "(Doubled)", ip=2, pp=18),
    Structure("Kaen MicroVault", 0, 1, False, False, mps=404, aps=404, rps=404),
    Structure("Kaen MicroVault", 0, 1, False, False, "(Doubled)", mps=808, aps=808, rps=808),
    Structure("T.O. Genesis Loom", 1, 1, False, False, ap=2, rp=4, c=411, pp=33),
    Structure("T.O. Colony Ark", 0, 1, False, False, ap=1, app=2, ip=1, p=4400),
    Structure("T.O. Colony Ark", 0, 1, False, False, "v2", mp=1, ap=2, app=2, ip=1, p=4400),
    Structure("T.O. Colony Ark", 0, 1, False, False, "v3", mp=1, ap=3, app=2, ip=2, p=8800),
    Structure("T.O. Colony Ark", 0, 1, False, False, "v4", mp=1, ap=4, app=2, ip=2, ipp=2, p=8800),
    Structure("Verdant Estate", 1, 1, False, False, ap=3, ip=1),
    Structure("Verdant Estate", 1, 1, False, False, "v2", ap=4, rp=2, ip=1),
    Structure("Verdant Estate", 1, 1, False, False, "v3", ap=5, rp=2, ip=2),
    Structure("Verdant Estate", 1, 1, False, False, "v4", ap=6, aps=1800, rp=2, ip=2),
    Structure("T.O. Frontier Habidome", 1, 1, False, False, mp=2, ap=2, rp=2, ip=1, pp=42),
    Structure("T.O. Seed-Lab", 1, 1, False, False, ap=1, rp=5, rpp=3, rps=1800),
    Structure("Vault of Gaia", 2, 1, False, True, mps=7000, aps=7000, rps=7000, ips=700, c=700),
    Structure("Vault of Gaia", 2, 1, False, True, "(Doubled)", mps=14000, aps=14000, rps=14000, ips=1400, c=1400),
    Structure("Spire of Edenic Dominion", 2, 1, False, True, mp=3, ap=3, rp=3, ip=4, ips=500, pp=55),
    Structure("Biosphere Gyre", 1, 1, False, False, mp=2, ap=1),
    Structure("Biosphere Gyre", 1, 1, False, False, "v2", mp=2, mps=4400, ap=1),
    Structure("Biosphere Gyre", 1, 1, False, False, "v3", mp=2, mps=4400, ap=2, aps=4400),
    Structure("Biosphere Gyre", 1, 1, False, False, "v4", mp=4, mps=6600, ap=2, aps=4400, c=440),
    Structure("Biosphere Gyre", 1, 1, False, False, "v5", mp=4, mps=6600, ap=2, aps=6600, c=660),
    Structure("Chuhn Star-Emporium", 1, 1, False, False, mp=2, ap=2, rp=2, ip=1),
    Structure("Chuhn Star-Emporium", 1, 1, False, False, "v2", mp=3, ap=2, rp=3, ip=1),
    Structure("Chuhn Star-Emporium", 1, 1, False, False, "v3", mp=4, ap=3, rp=3, ip=1),
    Structure("Chuhn Star-Emporium", 1, 1, False, False, "v4", mp=4, ap=4, rp=3, ip=2),
    Structure("Chuhn Star-Emporium", 1, 1, False, False, "v5", mp=4, ap=6, rp=3, ip=2),
    Structure("Scruuge Resupply Depot", 1, 1, False, False, mp=2, mpp=5, ap=1),
    Structure("Scruuge Resupply Depot", 1, 1, False, False, "II", mp=3, mpp=7, ap=1),
    Structure("Scruuge Resupply Depot", 1, 1, False, False, "III", mp=4, mpp=10, ap=2),
    Structure("Scruuge Thavix-Snare", 1, 1, False, False, ap=2, dp=33),
    Structure("Sentarch Seeker-Drones", 0, 2, False, False, mp=2, ap=2),
    Structure("Sentarch Mind-Drones", 0, 2, False, False, rp=2, ip=1),
    Structure("Divergent Entity", 1, 1, False, False, mp=1, ap=1, rp=1, ipp=2),
    Structure("Dark Temple of Woe", 1, 1, False, False, ap=2, rp=2, ip=1, ic=2),
    Structure("Dark Temple of Woe", 1, 1, False, False, "v2", ap=3, rp=3, ip=1, ic=4),
    Structure("Dark Temple of Woe", 1, 1, False, False, "v3", ap=3, rp=4, ip=2, ic=6),
    Structure("Dark Temple of Woe", 1, 1, False, False, "v4", ap=3, rp=4, ip=3, ic=9),
    Structure("Supel Biomech Hangar", 0, 1, False, False, mp=2, ap=1, app=2),
    Structure("Supel Biomech Hangar", 0, 1, False, False, "v2", mp=4, ap=1, app=2, ipp=1),
    Structure("Supel Biomech Hangar", 0, 1, False, False, "v3", mp=6, ap=3, app=2, ipp=1),
    Structure("Supel Biomech Hangar", 0, 1, False, False, "v4", mp=6, ap=3, app=3, ipp=1),
    Structure("Supel Dark-Warren", 1, 1, True, False, mp=2, ap=1, rp=2, ip=1, cp=16),
    Structure("Q-Pedd Affinity Tunnel", 0, 1, False, False, ap=1, rp=2, rpp=3, ip=1),
    Structure("Q-Pedd Affinity Tunnel", 0, 1, False, False, "v2", ap=1, rp=4, rpp=5, ip=1),
    Structure("Q-Pedd Affinity Tunnel", 0, 1, False, False, "v3", ap=2, rp=4, rpp=6, ip=2),
    Structure("Q-Pedd Affinity Tunnel", 0, 1, False, False, "v4", ap=2, rp=4, rpp=7, ip=3),
    Structure("Q-Pedd Ballroom", 1, 1, False, False, ap=2, rp=2, ip=1, ips=202, esp=50),
    Structure("Streveldan CogNode", 1, 1, False, False, ap=2, rp=4, c=404, cp=14, dp=22),
    Structure("Strevelan Cohesion Pit", 1, 1, False, False, mp=4, mps=1001, rps=1001, atp=33),
    Structure("Supel Incubator", 1, 1, False, False, mp=1, ap=1, rp=5, ip=1, p=11000),
    Structure("Veon Singularium", 0, 1, False, False, mp=1, ap=1, rp=1, c=404),
    Structure("Veon Singularium", 0, 1, False, False, "v2", mp=2, ap=1, rp=2, c=404),
    Structure("Veon Singularium", 0, 1, False, False, "v3", mp=3, ap=2, rp=3, c=404),
    Structure("Veon Singularium", 0, 1, False, False, "v4", mp=4, ap=3, rp=4, c=808),
    Structure("Synesthetic Fuse", 0, 1, False, True, mpp=2, app=2, rpp=2, ipp=2),
    Structure("Synesthetic Fuse", 0, 1, False, True, "v2", mpp=3, app=3, rpp=3, ipp=3),
    Structure("Synesthetic Fuse", 0, 1, False, True, "v3", mpp=4, app=4, rpp=4, ipp=4),
    Structure("Synesthetic Fuse", 0, 1, False, True, "v4", mpp=5, app=5, rpp=5, ipp=5),
    Structure("Font of Vitalis", 3, 1, False, True, ap=8, ip=4, ipp=6),
    Structure("Thavix Geneworks", 1, 1, False, False, ap=2, rp=7, rps=5200),
    Structure("Thavix Geneworks", 1, 1, False, False, "v2", ap=2, rp=7, rpp=2, rps=5200),
    Structure("Thavix Geneworks", 1, 1, False, False, "v3", ap=3, rp=8, rpp=2, rps=5200, ips=250),
    Structure("Thavix Geneworks", 1, 1, False, False, "v4", ap=2, app=2, rp=8, rpp=2, rps=5200, ips=400),
    Structure("Covert Legation", 1, 1, True, False, rp=4, c=850),
    Structure("Covert Legation", 1, 1, True, False, "II", rp=6, ip=1, c=850, esp=42),
    Structure("Antigrav Citadel", 0, 1, False, False, rp=1, ip=1, cp=11),
    Structure("Antigrav Citadel", 0, 1, False, False, "v2", rp=2, ip=1, ips=111, cp=22),
    Structure("Antigrav Citadel", 0, 1, False, False, "v3", rp=4, ip=2, ips=111, cp=22),
    Structure("Antigrav Citadel", 0, 1, False, False, "v4", rp=4, ip=2, ips=222, cp=33),
    Structure("Hall of Delegates", 1, 1, False, False, ap=1, rp=1),
    Structure("Hall of Delegates", 1, 1, False, False, "(Upgraded)", ap=1, rp=1, ip=2),
    Structure("Gallery of Records", 1, 1, False, False, ap=2, aps=1800, ip=1, ips=180),
    Structure("Forum of Realms", 1, 1, False, False, mp=2, mpp=2, ap=2, app=2, rp=2, rpp=2, ip=1, ipp=2),
    Structure("Court of Eternity", 1, 1, False, False, mpp=5, app=5, rpp=5, ip=2, ipp=5),
    Structure("Civicordium Platform", 1, 1, False, False, ip=1, ipp=2),
    Structure("Civicordium Platform", 1, 1, False, False, "v2", ap=1, ip=1, ipp=3),
    Structure("Civicordium Platform", 1, 1, False, False, "v3", ap=2, ip=2, ipp=3),
    Structure("Civicordium Platform", 1, 1, False, False, "v4", ap=3, ip=2, ipp=4),
    Structure("Spire of Civicordium Dominion", 2, 1, True, False, mp=3, ap=3, rp=3, ip=4, ipp=4, ips=550),
    Structure("Tamed Undulok", 0, 1, False, False, mp=3, ap=1, pp=20),
    Structure("Bio-Symposium Lab", 1, 1, False, False, rp=6, ip=1, pp=22),
    Structure("Tree of Harmony", 1, 1, False, False, mp=1, ap=1, rp=1, pp=20),
    Structure("Tree of Harmony", 1, 1, False, False, "II", mp=1, ap=1, rp=1, ip=1, pp=30),
    Structure("Tree of Harmony", 1, 1, False, False, "III", mp=2, ap=2, rp=2, ip=1, pp=40),
    Structure("Bane Phage Sacrarium", 1, 1, False, False, ap=2, rp=3, rpp=3),
    Structure("Bane Phage Sacrarium", 1, 1, False, False, "v2", ap=3, rp=5, rpp=3),
    Structure("Bane Phage Sacrarium", 1, 1, False, False, "v3", ap=3, rp=6, rpp=5),
    Structure("Bane Phage Sacrarium", 1, 1, False, False, "v4", ap=5, rp=6, rpp=7),
    Structure("Chuhn Reclamation Drone", 0, 1, True, False, mp=4, mps=2200, mpp=5, ap=2, aps=2200),
    Structure("Covert BlackWatch", 1, 1, False, False, ap=1, rp=3, c=888),
    Structure("Cross-Signal Restrainer", 1, 1, True, True, cp=30),
    Structure("Dark Phage Entity", 0, 1, False, False, mpp=2, app=2, rpp=2, ipp=2, pp=-66, ic=3),
    Structure("Drannik Holo-Sanctum", 1, 1, False, False, ap=1, rp=2, rps=444, ip=1),
    Structure("Elios Soletta", 0, 1, False, False, mp=1, mpp=3, ap=1),
    Structure("Elios Soletta", 0, 1, False, False, "v2", mp=2, mpp=4, ap=1),
    Structure("Elios Soletta", 0, 1, False, False, "v3", mp=2, mpp=5, ap=2),
    Structure("Elios Soletta", 0, 1, False, False, "v4", mp=3, mpp=6, ap=3),
    Structure("Exotic Miners Guildhall", 1, 1, True, False, mpp=6, ip=1),
    Structure("Klorvis Shroud Generator", 1, 2, False, True, rp=1, c=200),
    Structure("Klorvis Troop Gateway", 1, 1, False, True, at=750, d=750),
    Structure("Portal of Legacies", 1, 1, False, False, mp=2, mpp=4, ap=1, app=4, rp=3, rpp=4, ip=1, ipp=4),
    ]

def addAbility(structureName, ability):
    for structure in structures:
        fullName = structure.name
        if structure.nameAdd != "":
            fullName += " " + structure.nameAdd
        if structureName == fullName:
            structure.addAbility(ability)

addAbility("Monolith of Miracles", {"name":"Upgrade", "planetEffects":[{"type":"Upgrade", "new":"Monolith of Miracles v2"}], "restrictions":[{"type":"Size","max":"Large"}]})
addAbility("Monolith of Miracles v2", {"name":"Upgrade", "planetEffects":[{"type":"Upgrade", "new":"Monolith of Miracles v3"}], "restrictions":[{"type":"Size","max":"Average"}]})
addAbility("Monolith of Miracles v3", {"name":"Upgrade", "planetEffects":[{"type":"Upgrade", "new":"Monolith of Miracles v4"}], "restrictions":[{"type":"Size","max":"Small"}]})
addAbility("Elios Corethune Shell", {"name":"Upgrade", "planetEffects":[{"type":"Upgrade", "new":"Elios Corethune Shell v2"}], "restrictions":[{"type":"Size","max":"Average"}]})
addAbility("Elios Corethune Shell v2", {"name":"Upgrade", "planetEffects":[{"type":"Upgrade", "new":"Elios Corethune Shell v3"}], "restrictions":[{"type":"Size","max":"Average"}]})
addAbility("Elios Corethune Shell v3", {"name":"Upgrade", "planetEffects":[{"type":"Upgrade", "new":"Elios Corethune Shell v4"}], "restrictions":[{"type":"Size","max":"Average"}]})
addAbility("Chuhn Star-Emporium", {"name":"Upgrade", "planetEffects":[{"type":"Upgrade", "new":"Chuhn Star-Emporium v2"}], "restrictions":[{"type":"Size","max":"Average"}]})
addAbility("Chuhn Star-Emporium v2", {"name":"Upgrade", "planetEffects":[{"type":"Upgrade", "new":"Chuhn Star-Emporium v3"}], "restrictions":[{"type":"Size","max":"Average"}]})
addAbility("Chuhn Star-Emporium v3", {"name":"Upgrade", "planetEffects":[{"type":"Upgrade", "new":"Chuhn Star-Emporium v4"}], "restrictions":[{"type":"Size","max":"Average"}]})
addAbility("Chuhn Star-Emporium v4", {"name":"Upgrade", "planetEffects":[{"type":"Upgrade", "new":"Chuhn Star-Emporium v5"}], "restrictions":[{"type":"Size","max":"Average"}]})
addAbility("Phylogenetic Core", {"name":"Decrease Genes Cooldown", "playerEffects":[{"type":"Decrease Grow Genes Cooldown", "value":"14%", "duration":"3 days"}]})

    
def generateNotesStr(notes: list[int] = []):
    if len(notes) < 1:
        return ""
    
    noteStr = "<sup>" + str(notes[0])
    for i in range(1, len(notes)):
        noteStr += "," + str(notes[i])
    return noteStr + "</sup>"

def generateNameStr(name: str, nameAdd: str = "", nameNotes: list[int] = [], alternatePageName: str = ""):
        fullName: str = name
        if len(nameAdd) > 0:
            fullName += " " + nameAdd
        nameStr: str = ""
        
        if len(alternatePageName) > 0:
            nameStr = "[[" +  alternatePageName + "|" + fullName + "]]"
        elif fullName != name:
            nameStr = "[[" +  name + "|" + fullName + "]]"
        else:
            nameStr = "[[" + name + "]]"

        return nameStr + generateNotesStr(nameNotes)

def generateLimitStr(limit: int, notes: list[int] = []):
    limitStr: str = ""
    if limit < 0:
        limitStr = "?"
    elif limit == 0:
        limitStr = "None"
    else:
        limitStr = str(limit)

    return limitStr + generateNotesStr(notes)

def generateValueStr(value: int, notes: list[int] = []):
    if value == 0 and len(notes) < 1:
        return ""
    
    valueStr = str(value)

    return valueStr + generateNotesStr(notes)


with open('structures.txt', 'w') as outFile:
    
    wikiString: str = ""
    for structure in structures:

        wikiString += (
            "|-\n"
            "| " + generateNameStr(structure.name, structure.nameAdd, structure.nameNotes, structure.alternatePageName) + "\n"
            "| align=\"center\" | " + str(structure.size) + "\n"
            "| align=\"center\" | " + generateLimitStr(structure.limit, structure.limitNotes) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.mp) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.mpp) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.mps) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.ap) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.app) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.aps) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.rp) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.rpp) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.rps) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.ip) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.ipp) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.ips) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.d, structure.defenseNotes) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.dp) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.at) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.atp) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.c, structure.cloakNotes) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.cp) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.p) + "\n"
            "| align=\"center\" | " + generateValueStr(structure.pp) + "\n"
            #"| align=\"center\" | " + generateValueStr(structure.id) + "\n"
            #"| align=\"center\" | " + generateValueStr(structure.esp) + "\n"
            #"| align=\"center\" | " + generateValueStr(structure.ic) + "\n"
            "| align=\"center\" | " + ("Yes" if structure.limited else "No") + "\n"
            "| align=\"center\" | " + ("Yes" if structure.extract else "No") + "\n"
            #"| align=\"center\" | " + structure.acq + "\n"
        )
    outFile.write(wikiString)

def generateArtifactPage(name: str):
    wikiStr: str = "== Structure ==\n"
    for structure in structures:
        if structure.name == name or structure.alternatePageName == name:
            if len(structure.formDescription) > 0:
                wikiStr += structure.formDescription + "<br>\n"
            wikiStr += "{{Structure\n"
            wikiStr += "|size=" + str(structure.size) + "\n"
            wikiStr += "|image=\n"
            
            if structure.mp != 0:
                wikiStr += "|mining=" + str(structure.mp) + "\n"

            if structure.ap != 0:
                wikiStr += "|artifact=" + str(structure.ap) + "\n"

            if structure.rp != 0:
                wikiStr += "|research=" + str(structure.rp) + "\n"

            wikiStr += "}}\n\n"

    print(wikiStr)

jsonDict = []

variantStructures = [
    "Bahreen Duodecix",
    "Bioship Gene Lab",
    "Strazi Link Anchor",
    "Meta-Tuned Jammer",
    "Rikthar's War Forge",
    "Adaptive Spire",
    "Litheor Core-Tunnel"
    ]

#name: str, size: int, limit: int, limited: bool, extract: bool, nameAdd: str = "", mp: int = 0, mpp: int = 0, mps: int = 0, ap: int = 0, app: int = 0, aps: int = 0, rp: int = 0, rpp: int = 0, rps: int = 0, ip: int = 0,
#                 ipp: int = 0, ips: int = 0, d: int = 0, dp: int = 0, at: int = 0, atp: int = 0, c: int = 0, cp: int = 0, p: int = 0, pp: int = 0, id: int = 0, esp: int = 0, ic: int = 0, acq: str = "",
#                 nameNotes: list[int] = [], cloakNotes: list[int] = [], limitNotes: list[int] = [], defenseNotes: list[int] = [], alternatePageName: str = "", formDescription: str = ""):

def setBase(structure):
    if structure['name'] in ["Galaxy Interrogators"]:
        structure['base'] = "Galaxy Overseers"
    elif structure['name'] in ["Spire of Civicordium Dominion", "Spire of Edenic Dominion", "Spire of High Dominion", "Spire of Scruuge Dominion", "Spire of Cybernetic Dominion", "Spire of Supel Dominion"]:
        structure['base'] = "Spire of Dominion"
    elif structure['name'] in ["Galaxy Inquisitors", "Galaxy Technocrats", "Galaxy Overseers", "Galaxy Interrogators", "Galaxy Pedants", "Galaxy Administrators", "Galaxy Aristocrats", "Galaxy Surrogates", "Galaxy Celestials"]:
        structure['base'] = "Galaxy Elitists"
    elif 'Sparkmatter' in structure['name']:
        structure['base'] = "Triangulum Sparkmatter"

for structure in structures:
    structureJson = {}
    if structure.nameAdd != "":
        structureJson['name'] = structure.name + " " + structure.nameAdd
        
        structureJson['base'] = structure.name
    else:
        structureJson['name'] = structure.name

    setBase(structureJson)
    structureJson['size'] = structure.size
    structureJson['limit'] = structure.limit
    structureJson['limited'] = structure.limited
    structureJson['extract'] = structure.extract
    if structure.mp != 0:
        structureJson['mp'] = structure.mp
    if structure.mpp != 0:
        structureJson['bmp'] = structure.mpp
    if structure.mps != 0:
        structureJson['mps'] = structure.mps
    if structure.ap != 0:
        structureJson['ap'] = structure.ap
    if structure.app != 0:
        structureJson['bap'] = structure.app
    if structure.aps != 0:
        structureJson['aps'] = structure.aps
    if structure.rp != 0:
        structureJson['rp'] = structure.rp
    if structure.rpp != 0:
        structureJson['brp'] = structure.rpp
    if structure.rps != 0:
        structureJson['rps'] = structure.rps
    if structure.ip != 0:
        structureJson['ip'] = structure.ip
    if structure.ipp != 0:
        structureJson['bip'] = structure.ipp
    if structure.ips != 0:
        structureJson['ips'] = structure.ips
    if structure.at != 0:
        structureJson['at'] = structure.at
    if structure.atp != 0:
        structureJson['bat'] = structure.atp
    if structure.d != 0:
        structureJson['d'] = structure.d
    if structure.dp != 0:
        structureJson['bd'] = structure.dp
    if structure.p != 0:
        structureJson['p'] = structure.p
    if structure.pp != 0:
        structureJson['bp'] = structure.pp
    if structure.c != 0:
        structureJson['c'] = structure.c
    if structure.cp != 0:
        structureJson['bc'] = structure.cp
    if structure.ic != 0:
        structureJson['ic'] = structure.ic
    if structure.esp != 0:
        structureJson['es'] = structure.esp
    if structure.id != 0:
        structureJson['id'] = structure.id
    if structure.ability != None:
        structureJson['ability'] = structure.ability

    jsonDict.append(structureJson)

with open("config/structures.json", "w") as jsonOut:
    json.dump(jsonDict, jsonOut, indent=4)



with open("./influenceStructure.txt", "w") as outFile:
    for structure in structures:
        if structure.ip > 0 or structure.ipp > 0:
            nameStr = structure.name
            if structure.nameAdd != "":
                nameStr += " " + structure.nameAdd
            outFile.write(f"{nameStr}\n")

sortedStructures: list[tuple[str, float]] = []
sortedRawCloakStructures: list[tuple[str, float]] = []
sortedCloakStructures: list[tuple[str, float]] = []

for structure in structures:
    if structure.size > 0 and (structure.ap > 0 or structure.app > 0 or structure.aps > 0):
        totalApS = (structure.ap + structure.app * 1.5 + structure.aps / 19 / 30) / structure.size
        index = 0
        for sortedStructure in sortedStructures:
            if sortedStructure[1] < totalApS:
                break
            else:
                index += 1
        nameStr = structure.name
        if structure.nameAdd != "":
            nameStr += " " + structure.nameAdd
        sortedStructures.insert(index, (nameStr, totalApS))
    elif structure.ap > 0 or structure.app > 0 or structure.aps > 0:
        
        nameStr = structure.name
        if structure.nameAdd != "":
            nameStr += " " + structure.nameAdd
        nameStr = structure.name
        if structure.nameAdd != "":
            nameStr += " " + structure.nameAdd
        sortedStructures.insert(0, (nameStr, 100000))

    if structure.size > 0 and (structure.c > 0 or structure.cp > 0):
        totalC = (structure.c + structure.cp * 200) / structure.size
        index = 0
        for sortedStructure in sortedCloakStructures:
            if sortedStructure[1] < totalC:
                break
            else:
                index += 1
        nameStr = structure.name
        if structure.nameAdd != "":
            nameStr += " " + structure.nameAdd
        sortedCloakStructures.insert(index, (nameStr, totalC))
    elif structure.c > 0 or structure.cp > 0:
        
        nameStr = structure.name
        if structure.nameAdd != "":
            nameStr += " " + structure.nameAdd
        nameStr = structure.name
        if structure.nameAdd != "":
            nameStr += " " + structure.nameAdd
        sortedCloakStructures.insert(0, (nameStr, 100000))

    if structure.size > 0 and (structure.c > 0):
        totalC = structure.c / structure.size
        index = 0
        for sortedStructure in sortedRawCloakStructures:
            if sortedStructure[1] < totalC:
                break
            else:
                index += 1
        nameStr = structure.name
        if structure.nameAdd != "":
            nameStr += " " + structure.nameAdd
        sortedRawCloakStructures.insert(index, (nameStr, totalC))
    elif structure.c > 0:
        
        nameStr = structure.name
        if structure.nameAdd != "":
            nameStr += " " + structure.nameAdd
        nameStr = structure.name
        if structure.nameAdd != "":
            nameStr += " " + structure.nameAdd
        sortedRawCloakStructures.insert(0, (nameStr, 100000))

    

with open("./orderedapstructures.txt", "w") as outFile:
    for structure in sortedStructures:
        outFile.write(f"{structure[0]}: {structure[1]}\n")

with open("./orderedcloakstructures.txt", "w") as outFile:
    for structure in sortedCloakStructures:
        outFile.write(f"{structure[0]}: {structure[1]}\n")

with open("./orderedrawcloakstructures.txt", "w") as outFile:
    for structure in sortedRawCloakStructures:
        outFile.write(f"{structure[0]}: {structure[1]}\n")
