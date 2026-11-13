[Player reference](README.md) · [Weapon comparison](weapon-comparison.md) · [Equipment](training-and-equipment.md)

# M1 Garand

A **2-TP rifle upgrade** for eligible infantry. Its ordinary-soldier path refills
to eight rounds when empty. It is also the Regular Soldier's starting weapon
with Meritorious Unit Commendation, and the inspected infantry Ranger Training
receipt supplies it. [Equipment evidence](../player-pilot-evidence.md#garand-purchase-and-fire)

| Property                                 | Selected 2.3.1g behavior                                                        |
| ---------------------------------------- | ------------------------------------------------------------------------------- |
| Upgrade price                            | 2 TP; equipment menu                                                            |
| Ordinary-soldier refill                  | 8 rounds                                                                        |
| Damage                                   | Shared unarmored hit path draws 0–119 health damage; hit and target gates apply |
| Long-distance accuracy modifier          | Above 350 source distance units: doubles the roll compared with rifle skill     |
| Close-distance accuracy modifier         | Below 100 source distance units: divides that roll by 1.1                       |
| Full reaction, reload and retarget times | Not yet reconstructed in seconds                                                |

The damage range describes a conditional random subtraction from a living,
unarmored target. An attempted shot may miss, hit another kind of target or do
zero damage. It is not 120 guaranteed damage per shot. Exactly 350 does not
trigger the long-distance modifier; exactly 100 does not trigger the close one.
These distances are game-source units, not meters. [Damage and distance evidence](../player-pilot-evidence.md#garand-purchase-and-fire)

## Buying and issuing it

Have at least 2 TP, select the Garand offer, then click an eligible infantry
recipient. The offer deducts the price and selects a pending weapon; it does not
immediately equip the entire squad. In the inspected regular/recon receipt,
health must be above 9 and earlier pending actions can take precedence. Applying
a different weapon replaces the current weapon field. The already-same-weapon
branch refunds the stored weapon cost; interleaved purchases and other
recipients need their own checks. [Purchase and recipient trace](../player-pilot-evidence.md#garand-purchase-and-fire)

## What changes from the Springfield?

The community describes repeated fire at one target and calls the Garand a
semi-automatic alternative to the Springfield. That is useful historical advice,
but the complete same-target and next-target timing model remains open.
[Archived comparison](../rifle-distance.md)

The selected shared firing helper gives the Garand a damage draw bound of 120
versus the Springfield's 125. The Garand's long-distance penalty starts above
350, versus above 400 for the Springfield. Both have the same inspected
below-100 roll divisor. An upgrade name alone therefore does not mean every
individual damage or range property increases. Fire cadence, target selection
and magazine handling must be assessed together. [Distance comparison](../rifle-distance.md),
[damage explanation](../damage.md)

## Reload and experience

In one ordinary-soldier post-fire branch, while unpaused and with its movement
state equal to 1, empty Garand ammo triggers an eight-round refill and assigns
a recovery timer of **250 minus experience**. With ammo remaining, that branch
assigns **50 plus a random 0–99 minus experience** instead. These are conditional
source counter assignments; they do not establish elapsed reload seconds, a
minimum timer, every actor's behavior or initial reaction speed.
[Exact timing bindings](../player-pilot-evidence.md#garand-purchase-and-fire)

This matters when reading the archived card's reload value of 200: it cannot be
used as a universal replacement for the selected regular-soldier branch. Keep
experience, actor, ammo and state context attached to timing claims.
[Open timing questions](../player-pilot-evidence.md#open-mechanics-questions)

Sources: [Source identities](../player-notes/m1-garand.md#citation-1).
Precise paths, conditions and version identity: [pilot evidence](../player-pilot-evidence.md).

## Modern group-clearance measurements

Modern experiment dated **2026-11-07**; the historical card above remains separate.

Soldier/Garand cleared the veteran medium group faster than BAR despite lower
dummy DPS. Spec Ops' larger repeat counter could instead waste time on dead targets;
Resistance's shorter recovery improved its Garand result.
[Measured outcomes and source limits](combat-results.md), [role lifecycles](unit-lifecycle.md).
