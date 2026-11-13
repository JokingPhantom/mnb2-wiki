[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Goliath tracked explosive

The Goliath is a tracked explosive device with **500 starting health and armor code 1**. It can request an explosion through player proximity, nonpositive health
or both driver/gunner fields reaching zero. Triggering, effect placement and
the later blast's recipients remain separate tests.
[Exact source paths](../player-light-vehicle-evidence.md)

Historical scope: selected **2.3.1g**.

| Key fact              | Historical default or behavior                                           |
| --------------------- | ------------------------------------------------------------------------ |
| Starting hull health  | 500                                                                      |
| Armor code            | 1                                                                        |
| Important distinction | Strict below-30 player-proximity trigger; later AT radius 40 is separate |

On this page: [Proximity uses a strict point-distance test](#proximity-uses-a-strict-point-distance-test) · [Movement reads two fields with different weights](#movement-reads-two-fields-with-different-weights) · [The blast has its own inputs](#the-blast-has-its-own-inputs)

## Proximity uses a strict point-distance test

The selected trigger action scans positive-health player entries and checks
distance **strictly below 30**. It places the explosion at the Goliath's point,
rather than copying the player's point. Exactly 30 fails that predicate.
No armor, visibility or LOS condition appears at that local trigger test.
Full sampling cadence and transformed geometry remain unresolved.
[Trigger evidence](../player-light-vehicle-evidence.md#frame20-actor-proximity-and-the-separate-decoration-index-question)

The separate decoration scan has a source index mismatch: its loop counter and
the index used to read a decoration differ. It also lacks a local distance test.
This source finding is not a reproduced bug or a qualified “touching any wall”
rule. The exact names and mutable loop bound stay in the evidence note.

## Movement reads two fields with different weights

Its active movement expression adds driver plus half the gunner field to y.
With both fields 1, that is **1.5 source units per admitted visit**; with only
driver 1 it is 1, and with only gunner 1 it is 0.5. These field names do not
establish actual people aboard the device or a measured speed per second.
[Load, movement and removal](../player-light-vehicle-evidence.md#goliath-load-and-movement-expression)

## The blast has its own inputs

The selected effect supplies AT radius 40 and damage input 300 with tag `tank`.
Those are not the trigger's distance-30 condition or guaranteed health loss.
The effect-creation branches do not explicitly copy an owner, and recipient,
credit and complete destruction paths still need qualification.
[AT distinctions](anti-tank-and-vehicles.md), [exact effect](../player-light-vehicle-evidence.md#frame20-actor-proximity-and-the-separate-decoration-index-question)

Sources: [Source identities](../player-notes/goliath.md#citation-1)
