[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Repair, crew or reload?](repair-crew-and-reload.md)

# Buying vehicles and placed weapons

The reinforcement menu offers vehicles and placed weapons as well as infantry.
Applies to **historical selected 2.3.1g**. Prices below are **base offers**;
upgrades, crew and refill can cost extra. Check the role and its requirements
before buying. A selected offer does not guarantee arrival or combat readiness. [Menu map and offer guides](menu-reference.md)

Use the price/role list below, then compare [weapon stats](#which-stat-does-the-weapon-actually-read),
[health and crew](#keep-purchase-parent-and-component-state-separate) or
[range and scatter](#range-fields-and-actual-impacts).

| Offer                                      | Base TP | Role and extra commitment to check                                                         |
| ------------------------------------------ | ------- | ------------------------------------------------------------------------------------------ |
| [Jeep](jeep.md)                            | 6       | Mobile gun platform; driver, gunner and hull/weapon readers have different jobs            |
| [Sherman tank](sherman.md)                 | 20      | Cannon and coaxial attack paths; the optional .50 is a separate 4-TP upgrade               |
| [Halftrack](halftrack.md)                  | 12      | Base vehicle for separately priced replacement weapon/support modules                      |
| [M3 AT gun](m3-at-gun.md)                  | 8       | AT gun with an armor-first pass, crew gates and a nearby-gun crowding check                |
| [Static .50-caliber gun](fifty-caliber.md) | 6       | Placed automatic gun with its own gunner, burst and refill controller                      |
| [20 mm AA cannon](aa-cannon.md)            | 20      | Anti-air attempts and separate ground effects; parent and gun stats have different readers |
| [Rocket launcher](rocket-launcher.md)      | 20      | Manual fire/refill states and area impacts; an empty refill has its own 1-TP cost          |

Use **selected historical 2.3.1g** role and cost evidence in the linked cards.
For an existing vehicle that is damaged or silent, distinguish
[repair, replacement crew and reload](repair-crew-and-reload.md) before choosing
another purchase. The base price does not include every later upgrade, module
or refill, and it does not establish kills per TP.

These are distinct menu handlers. A common price or a familiar weapon name does
not prove common crew rules, aiming, reload, damage, or placement requirements.
The [weapon comparison](weapon-comparison.md) describes a named shared infantry
helper; it is not a table of all mounted and emplacement weapons.

## Which stat does the weapon actually read?

A vehicle's displayed fields do not automatically belong to every child weapon.
Use the exact stage when deciding what an experience or rifle increase means:

| Selected path                  | Stat or placement reader                                              | Practical interpretation                                                                                   |
| ------------------------------ | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [Jeep gun](jeep.md)            | Child XP in the aiming loop; hull rifle in the shot comparison        | The Jeep promotion's child-rifle write is not the hull-rifle shot reader                                   |
| [Static .50](fifty-caliber.md) | Own rifle in the shared helper; adds twice positive burst to its roll | A burst counter is not automatically the number of hits; the roll modifier differs from tank .50           |
| [Sherman cannon](sherman.md)   | Fixed independent axis-offset writes at emission                      | Those writes do not read rifle, XP or stored blastrange; do not infer tighter spread from that field alone |
| [M3 AT gun](m3-at-gun.md)      | Fixed independent axis-offset writes at emission                      | The separate 200-XP recovery write does not make XP a spread term                                          |
| [20 mm AA](aa-cannon.md)       | Child XP for its ground burst; parent rifle for anti-air comparison   | Ground-cycle and anti-air behavior cannot share one undifferentiated accuracy statistic                    |

The [Halftrack weapon modules](halftrack-weapons.md) add another distinction:
quad shot actions test a fixed six-of-100 draw comparison, while AT/mortar effect
placement uses fixed axis offsets. The AT module's >400 minimum belongs to its
inspected search, unlike the standalone M3's separate armor-first/fallback split.
[Exact Halftrack readers](../player-halftrack-weapons-evidence.md)
Additional source: [Source identities](../player-notes/vehicles-and-emplacements.md#citation-1)

This compares identified readers, not total combat effectiveness. Admission,
crew, target selection, projectile/effect placement, save/damage and later
recovery still need their own conditions. The [AT guide](anti-tank-and-vehicles.md)
separates sampled trigger points, emitted effects and later recipient radii.
[Jeep bindings](../player-jeep-evidence.md),
[static .50 bindings](../player-fifty-evidence.md),
[Sherman bindings](../player-tank-evidence.md),
[M3 bindings](../player-mounted-evidence.md),
[AA bindings](../player-aaa-evidence.md).

## Keep purchase, parent and component state separate

The selected US Jeep load initializes parent health 500 and armor code one.
Sherman initializes 1000 and armor code two in its qualifying nonstock branch;
halftrack initializes 800 and armor code one in its own branch. These are load
writes, before every later override, repair, crew change and destruction path.
[Exact vehicle placements and name guards](../vehicle-load-map.md)

Armor codes are classes rather than percentages. Equal parent health/class does
not prove equal durability against each attack. A crew hit, a disabled weapon
component and removal of the parent vehicle are also different outcomes.
[AT recipients](anti-tank-and-vehicles.md), [Crewman](crewman.md)

The Mechanic's selected repair path has type-specific below-threshold checks,
distance, usable-actor and protection exclusions. Do not assume a displayed
vehicle under a repair threshold will be repaired regardless of its placement
or the Mechanic's state. [Repair behavior](mechanic.md)

Buying a halftrack module can also clear its mobile support flags. Purchase
price is therefore only part of an upgrade comparison: include the replaced
role and the surrounding squad's needs. Full firing performance, gun recipient
geometry and multi-vehicle transaction behavior remain open, rather than filled
with a guessed damage-per-second ranking. [Module decisions](halftrack.md)

Sources: [Source identities](../player-notes/vehicles-and-emplacements.md#citation-2).
[Retained menu and load evidence](../player-vehicle-structure-evidence.md)

Reader comparison sources: [Source identities](../player-notes/vehicles-and-emplacements.md#citation-3)

The Guerilla award's selected vehicle counter increments on Sherman, AA, M3 AT,
static .50 and rocket-launcher spawn paths. The compared Jeep/Halftrack paths
omit that increment. This is a source-event distinction, not an award guarantee
or a scan of which vehicles are still living. [Exact paths](../player-guerilla-counter-evidence.md#five-spawn-selectors-increment-vehiclecalled)
Additional source: [Source identities](../player-notes/vehicles-and-emplacements.md#citation-4)

## Range fields and actual impacts

A stored blastrange field is not a common accuracy or damage-radius stat. The
selected tank emitters use fixed axis offsets after reducing that field; the
222 stores it but uses a direct-fire reader.
[Compare blast radius, scatter and actual readers](blast-radius-and-scatter.md).
Additional source: [Source identities](../player-notes/vehicles-and-emplacements.md#citation-5)
