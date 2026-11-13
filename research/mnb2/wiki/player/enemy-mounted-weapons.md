[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy mounted guns: what actually differs?

A Pak38, Flak38, Nebelwerfer and Flakpanzer are different threats even when their
shots look like nearby explosions. Compare **which crew can select a target, where the later explosion is placed, and what damage checks it uses**. Starting rifle alone does not describe those stages.

Historical scope: selected **2.3.1g**.

| Enemy                         | Starting hull health | Armor code | Crew/action requirement                                   |
| ----------------------------- | -------------------- | ---------- | --------------------------------------------------------- |
| [Pak38](pak-38.md)            | 500                  | 1          | Positive driver + gunner sum                              |
| [Flak38](flak38.md)           | 500                  | 1          | Positive driver + gunner sum                              |
| [Nebelwerfer](nebelwerfer.md) | 500                  | 1          | Positive crew sum; selected action branch unpinned        |
| [Flakpanzer](flakpanzer.md)   | 1000                 | 2          | Turret needs hull gunner and passing random action choice |

The first three accept a closer eligible candidate before their armor preference can end the search. Flakpanzer uses its own turret scan. [Exact original comparison table](../player-mounted-table-trace-099.md).

These are selected loads, guards and helper inputs. They are not final health,
guaranteed damage, blast-versus-outline probabilities or measured fire rates.
Each linked actor page binds its exact retained source.

On this page: [A gunner loss is not a universal stop switch](#a-gunner-loss-is-not-a-universal-stop-switch) · [Armor preference is not a promise to shoot the nearest tank](#armor-preference-is-not-a-promise-to-shoot-the-nearest-tank) · [Similar effects can have very different AT inputs](#similar-effects-can-have-very-different-at-inputs)

## A gunner loss is not a universal stop switch

Pak38, Flak38 and Nebelwerfer use the **sum of driver and gunner** at their
inspected target-admission gate. With supplied driver 1/gunner 0, that predicate
still passes. This does not prove the queued animation or the whole encounter
will behave as though two crew remain; other state and callbacks still matter.

Flakpanzer's inspected turret instead explicitly needs its parent gunner. Its
hull movement has a separate counter path without that local crew requirement.
A disabled weapon and an immobilized hull are therefore different questions.
[Pak38 crew gate](../player-pak38-evidence.md#crew-sum-and-setup-have-different-roles),
[Flakpanzer hull and turret](../player-flak-wespe-evidence.md#flakpanzer-hull-final-load-and-turret-admission)

Pinning also needs the correct actor and stage. Nebelwerfer resets its expired
action counter before checking pinning around acquisition. Flak38's corresponding
inspected scan lacks that local pin comparison. Copying a universal pin-to-stop
rule between these guns would miss that distinction. This does not establish
immunity to every other pinning or animation effect.
[Flak38 comparison](../player-flak38-evidence.md#setup-and-selection-have-different-gates)

## Armor preference is not a promise to shoot the nearest tank

For Pak38, Flak38 and Nebelwerfer, a candidate must first beat the current stored
distance and pass eligibility checks. Only then does positive armor end the
scan. An earlier nearby infantry candidate can keep farther armor out; an early
accepted armored candidate can stop the scan before a later closer candidate.
These are ordered supplied-state consequences, not a tested tank-bait placement.
[Exact Pak38 examples](../player-pak38-evidence.md#the-scan-is-neither-two-pass-armor-first-nor-always-nearest)

Selection also happens before the inspected damage-effect position writes.
The emissions use the indexed target's later coordinates plus independent
**−100..+99 axis offsets**. Those coordinate expressions do not read these
actors' rifle or XP fields. A higher rifle card therefore does not by itself
tighten this particular scatter expression; later writers and other weapon
readers remain separate. [Enemy stats](enemy-stats.md)

Flakpanzer adds a different issue: one inspected emitter reads the turret's
target, another the hull's. The turret's earlier target assignment does not
prove both are centered on that same actor. Full second-emitter behavior and
actual target lifetime remain unresolved.
[Separate target receivers](../player-flak-wespe-evidence.md#flak-emission-frames-have-different-target-receivers)

## Similar effects can have very different AT inputs

The explo3 path passes core 25/AT 50/fragment 50/damage 300 with tag at. The
smallExplo path passes core 7/AT 2/fragment 50/damage 100 with tag air. The shared
AT helper tests its own eligible recipients and point distances. A fragment
radius 50 is not another AT 50 radius, and neither equals a vehicle outline.
[AT and vehicle rules](anti-tank-and-vehicles.md)

Pak38 explicitly copies father at its selected emission. The inspected
Nebelwerfer, Flak38 and Flakpanzer emissions do not make that explicit copy;
inherited effect fields and lifetime remain unresolved. This affects what can
be said about owner credit, rather than proving those effects have no owner.

A burst counter and repeated animation request also do not establish shots per
second or total hits. For choosing defenses, use the specific **blast stages**
and **crew/armor rules** rather than importing an infantry bullet-save percentage.
[Explosion stages](explosion-damage-stages.md), [vehicle crews](small-arms-against-vehicles.md)

Sources: [Source identities](../player-notes/enemy-mounted-weapons.md#citation-1).
Exact notes: [Pak38](../player-pak38-evidence.md), [Flak38](../player-flak38-evidence.md),
[Nebelwerfer](../player-nebelwerfer-evidence.md), [Flakpanzer](../player-flak-wespe-evidence.md).
No new encounter, callback, hitbox or timing trial; candidate player synthesis.

The [off-map88 support attack](off-map-88.md) is another path altogether:
root-controller requests, a random-point effect load and tank-tagged 25/50/50/100
helper inputs. It should not be treated as another field Pak38 crew/health card
or a measured barrage simply because its name contains 88.
Additional source: [Source identities](../player-notes/enemy-mounted-weapons.md#citation-2)
