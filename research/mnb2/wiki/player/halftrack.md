[Player reference](README.md) · [Vehicles and emplacements](vehicles-and-emplacements.md) ·
[Module weapon comparison](halftrack-weapons.md)

# Halftrack: buying a new module replaces its role

The selected base halftrack offer is **12 TP**. Five module offers then select a
new role on a matched halftrack; they are not five permanent bonuses accumulated
on every vehicle. Changing to Mobile HQ enables support flags, while the other
four module handlers clear them. [Exact module comparison](../halftrack-modules.md)

Applies to **historical selected 2.3.1g**.

| Key fact                 | Selected offer/module conditions                                              |
| ------------------------ | ----------------------------------------------------------------------------- |
| TP cost and availability | 12 TP base vehicle; deployment flag and allocation gates apply                |
| Starting role            | Base module state one; conversions cost extra                                 |
| Conversions              | Quad guns, mortar, AT, hospital or Mobile HQ; a new role replaces the old one |
| Support limitation       | Non-HQ conversions clear the compared mobile HQ/radar/antenna flags           |

[Offer evidence](../player-recruitment-receipt-evidence.md#halftrack-availability-and-tank-payment-differ),
[module evidence](../halftrack-modules.md).

Start with your question: [What does each conversion cost?](#choose-a-replacement-role-and-budget-it-separately),
[will Mobile HQ benefits survive another conversion?](#mobile-support-does-not-remain-after-every-conversion),
[can I replace a lost Halftrack?](#the-base-offer-uses-a-deployment-flag), or
[can I select movement without a driver?](#new-move-selection-does-not-require-its-driver-field).

## Choose a replacement role and budget it separately

The **12-TP base vehicle** and a later module are separate purchases. A conversion
replaces the selected role; the four non-HQ module handlers clear the compared
mobile support flags. Include the role you are giving up when choosing again.
[Module transaction evidence](../halftrack-modules.md).

| Module offer and additional TP                  | Role and next reference                                                                                                                                           |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Quad machine guns — 15 TP                       | Automatic-gun module with its own shot paths. [Weapon modules](halftrack-weapons.md)                                                                              |
| 81 mm mortar — 10 TP                            | Mortar weapon profile with separate targeting and scattered effects. [Weapon modules](halftrack-weapons.md)                                                       |
| 75 mm anti-tank — 12 TP                         | AT weapon profile; its selected scan has a strict above-400 source-distance gate. [Weapon modules](halftrack-weapons.md)                                          |
| [Field hospital](halftrack-hospital.md) — 10 TP | Adds 2 health per qualifying patient, under its own patient/module/timer conditions                                                                               |
| Mobile HQ — 12 TP                               | Sets the compared radar, antenna and HQ flags; each support/income consumer still has its own rules. [Support buildings](air-defense.md), [Field HQ](field-hq.md) |

Each additional price belongs to its qualifying module handler, after the base
vehicle purchase; it is not a bundled vehicle price or a completed conversion.

Distances and counter values are source conditions, not a calibrated placement
radius, treatment rate or firing performance ranking.

## Retained source module selectors

Module selector numbers are internal identifiers, not infantry weapon codes, gun counts or power ratings. Use the purchase and module comparisons above to choose equipment.

[Full source comparison and limitations](../player-notes/halftrack.md#technical-detail-1).

Each listed handler has affordability and matching-halftrack guards before its
debit and assignment. The cited guards do not require an empty module, and these
handlers have no previous-module refund write. That is a scoped source result,
not a whole-program refund audit or an observed repeat purchase.

## Mobile support does not remain after every conversion

Mobile HQ sets the radar, antenna and HQ flags to one. The quad, mortar, anti-tank
and hospital handlers set those flags to zero. A conversion can therefore replace
support state rather than retaining the benefits of every earlier purchase.
Flags alone do not specify every consumer's range or scheduling.
[Field HQ](field-hq.md), [antenna and radar](air-defense.md)

The handlers scan player entries for the halftrack type and force the scan index
to a large stopping value after a successful match. They do not establish that a
clicked vehicle is the recipient when several halftracks exist. Multi-vehicle,
damaged-vehicle, crew and replacement-timing behavior still needs a complete
transaction or observation; do not buy from an assumed target model.

The community's suppression, rate-of-fire, hospital and explosive-risk comparisons
remain historical advice. Four guns in a name/image are not evidence of four
independent attack events. Compare the actual firing/effect consumer before
claiming damage per second or one universally best module.
[Community and source distinctions](../halftrack-modules.md)

Sources: [Source identities](../player-notes/halftrack.md#citation-1).
[Exact evidence](../player-vehicle-structure-evidence.md)

## Hospital healing has its own rules

The hospital module adds 2 health per passing patient within strict distance 75,
with health above 0 and below 100 and armor 0. It can visit multiple player indices.
Its rescue branch tests exactly 11 after that addition, and a later fresh timer
write replaces the earlier XP-based expression. These are source-stage facts,
not a healing-per-second or safe-radius trial.
[Hospital card](halftrack-hospital.md), [exact patient/timer bindings](../player-halftrack-hospital-evidence.md)
Additional source: [Source identities](../player-notes/halftrack.md#citation-2)

## Weapon modules have different target and firing readers

The [weapon-module comparison](halftrack-weapons.md) now binds the quad's four
distinct shot-action frames, the AT module's strict >400 selection gate, and
the mortar's strict >300 gate. The quad's inspected initial comparison uses six
integer draw values rather than hull rifle; AT/mortar emissions use fixed axis
offsets around later target coordinates. Their weapon fields do not make them
one shared infantry gun. Full timing and effect ownership remain separate.
[Exact component and source bindings](../player-halftrack-weapons-evidence.md)
Additional source: [Source identities](../player-notes/halftrack.md#citation-3)

## The base offer uses a deployment flag

The 12-TP offer also requires allocation below 100 and the Halftrack deployment
flag zero. It sets that flag before requesting the vehicle. The retained literal
writer set has initialization 0 and two deployment writes 1, with no death reset
in that set; this does not certify every possible dynamic write. A lost vehicle
therefore cannot be assumed to reopen the offer. The medal waiver is reached
only after checking the full 12-TP balance.
[Exact purchase and flag writers](../player-recruitment-receipt-evidence.md#halftrack-availability-and-tank-payment-differ)
Additional source: [Source identities](../player-notes/halftrack.md#citation-4)

## Driver presentation does not by itself stop hull movement

The selected parent requests a missing-driver animation at driver 0. Its later
positive-health destination movement does not repeat a driver/gunner gate.
An existing destination can therefore still reach those movement comparisons
under supplied valid state; a new driverless order and actual path still need
input and geometry qualification.

The parent's gunner-animation test reads `module`, while purchase and component
selection use `moduleType`. Those names cannot be merged into one field when
explaining crew visuals. Health 0 selects a parent wreck/removal branch, without
a local refund or passenger loop. Each module's weapon, healing or support
consumer retains its own admission rules.
[Exact parent guards and receiver names](../halftrack-modules.md#parent-crew-presentation-and-movement-use-different-fields)

## New move selection does not require its driver field

The Halftrack's selected release handler needs positive health, then assigns
movement focus without a driver/gunner or module test. Combined with its
separate parent destination reader, this closes the source distinction between
an existing destination and permission to assign a new one. It is not a
reproduced driverless-order or full movement outcome.

Its moving field is also used for sound transitions: a blocked positional step
can still change that field from 0 to 1 to 2. The number alone is not evidence of
actual displacement or speed. [Exact input and blocked-step sequence](../player-vehicle-movement-evidence.md#halftrack-focus-uses-health-and-moving-is-also-a-sound-state-field).
Additional source: [Source identities](../player-notes/halftrack.md#citation-5)
