[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Flakpanzer

The Flakpanzer is an armored vehicle with **1000 starting health and armor code 2**. Its turret fires scattered small-explosion effects. Its load first
writes a positive moving counter, then replaces it with zero; quoting only
the earlier assignment would miss the final local state.
[Exact hull and turret](../player-flak-wespe-evidence.md#flakpanzer-hull-final-load-and-turret-admission)

Historical scope: selected **2.3.1g**.

| Key fact              | Historical default or behavior                         |
| --------------------- | ------------------------------------------------------ |
| Starting hull health  | 1000                                                   |
| Armor code            | 2                                                      |
| Important distinction | Separate turret with scattered small-explosion effects |

On this page: [Target choice and effect placement are different stages](#target-choice-and-effect-placement-are-different-stages) · [A flak effect is not guaranteed damage](#a-flak-effect-is-not-guaranteed-damage) · [A missing driver is not this hull's movement guard](#a-missing-driver-is-not-this-hulls-movement-guard)

## Target choice and effect placement are different stages

Its ready turret needs a gunner and eligible unpaused state before a random
action test and search for a living, visible, noninvincible, line-of-sight target.
The selected effects use independent **−100…99 axis offsets**, rather than
rifle or experience in their position formulas.

The two inspected effect frames do not use the same target receiver: one reads
the turret's target index, the other the hull's. The controller's target write
does not resolve that difference by itself. Actual second-effect coordinates,
ownership and complete burst behavior remain unqualified.
[Exact emitters and repeat boundaries](../player-flak-wespe-evidence.md#flak-emission-frames-have-different-target-receivers)

## A flak effect is not guaranteed damage

The later effect supplies AT 2, fragment 50 and damage input 100 with tag `air`.
Those are distinct from a vehicle outline, a guaranteed health subtraction or
the M3 AT gun's effect inputs. Its 1–10 burst field is also not a count of
guaranteed hits or full two-effect animation cycles.
[AT/recipient distinctions](anti-tank-and-vehicles.md)

The [Allied AA cannon](aa-cannon.md) has its own ground-fire and anti-air
controllers. A shared effect or visual resemblance does not merge those actors.
No aircraft-interception result or firing rate is claimed by this ground path.

## A missing driver is not this hull's movement guard

The selected active hull movement does not require driver or gunner. Flakpanzer
uses its moving counter; Wespe uses its setup counter. The turret has a separate
gunner check. A supplied zero driver field therefore does not by itself prove
immobilization in these bodies, or certify a practical way to create that state.

At the selected health comparison, zero goes to hull death. Exit past y600 has
an earlier separate miss/removal request without a crew/health test. Complete
removal order and all helper accounting still matter.
[Exact movement, wreck and exit guards](../player-flak-wespe-evidence.md#hull-movement-and-destruction-do-not-use-one-generic-crew-rule)

Sources: [Source identities](../player-notes/flakpanzer.md#citation-1)
