[Player reference](README.md) · [Weapon comparison](weapon-comparison.md) ·
[Equipment](training-and-equipment.md)

# Thompson / Tommy gun

A **3-TP weapon upgrade** in the selected menu; the shared allied helper calls
its weapon branch Tommy gun. It has a stronger close-distance accuracy-roll
modifier than Garand, but a larger far-distance penalty starting sooner.
[Weapon comparison](weapon-comparison.md)

Applies to **historical selected 2.3.1g**. Damage rows are conditional draws,
not guaranteed health loss; refill rows apply only to the stated ordinary-soldier
recovery branch. A weapon purchase is not itself a completed recipient/refill.

| Key fact                             | Selected behavior                                    |
| ------------------------------------ | ---------------------------------------------------- |
| TP cost and availability             | 3 TP equipment offer; apply to an eligible recipient |
| Conditional unarmored damage draw    | 0–99 health                                          |
| Above 200 distance                   | Accuracy roll ×3                                     |
| Below 100 distance                   | Accuracy roll ÷2                                     |
| Ordinary post-fire empty-ammo refill | 30 in the specified frame 15 branch                  |

[Weapon offer and behavior evidence](../player-weapon-evidence.md).

On this page: [Is it a close-distance upgrade?](#is-it-a-close-distance-upgrade), [Compare current burst and the exact distance edge](#compare-current-burst-and-the-exact-distance-edge), [Close-range strength and Resistance recovery](#close-range-strength-and-resistance-recovery).

## Is it a close-distance upgrade?

In selected **2.3.1g**, Thompson eases the shared accuracy comparison below 100
source units more than Garand does. Above 200 it instead triples the roll,
making the comparison harder; that penalty begins sooner than Garand's. This
explains a close-versus-distant tradeoff, without promising more hits in a whole
fight or a hard maximum firing range. Current burst, rifle skill and target
eligibility still matter. [Exact distance branches](../player-weapon-evidence.md#shared-helper)

The [2-TP Carbine](m1-carbine.md) has the same unarmored damage-draw bound but
different burst/repeat and distance behavior. Thompson's 3-TP price therefore
does not prove it is the stronger choice for every soldier or distance. Use the
comparison below, and apply the pending weapon to its recipient after buying.
[Weapon offers and cycles](../player-weapon-evidence.md),
[equipment steps](training-and-equipment.md)

Exactly 200 does not trigger its above 200 penalty; exactly 100 does not trigger its
below 100 benefit. Distance is in source units. The roll changes do not turn into
universal hit percentages without rifle skill, burst and target context.
[Exact branches](../player-weapon-evidence.md#shared-helper)

The ordinary aiming path initializes burst to a random 1–6 counter. A positive
burst also adds twice its current value to the shared helper's accuracy roll.
The repeat, ammo and later recovery states therefore matter along with the
weapon's damage draw. An initialized burst is not a guarantee of that many hits.
[Repeating and recovering](how-shooting-works.md)

Buying selects a pending weapon code; applying it is a separate recipient action.
The inspected regular/recon receipt requires health above 9 and can be preceded by
other pending actions. Weapon replacement overwrites the prior weapon field;
no optimal-upgrade or comparative kills-per-TP result is claimed.
[Equipment receipt](../bar.md)

Sources: [Source identities](../player-notes/thompson.md#citation-1). Selected 2.3.1g;
[evidence notes](../player-weapon-evidence.md).

## Compare current burst and the exact distance edge

At supplied rifle 40/current burst 0, the Carbine admits 41 of 100 integer draws
at distance 201 while the Thompson admits 14. At distance 99, both zero-burst
columns admit 81. A separately supplied Thompson burst 6 reduces those named
counts to 2 and 69 respectively, because its positive burst penalty is applied
before the distance modifier.

These are inputs to one reached shared comparison, not normal starting-state
claims or a whole-weapon ranking. The two weapons have the same inspected damage
bound but different current-state, repeat and ammo contexts.
[Full strict-edge table and assumptions](../player-weapon-evidence.md#carbine-and-thompson-distance-edges-with-separately-supplied-current-burst).

The [Grease/Thompson close-range example](../player-weapon-evidence.md#close-range-grease-and-thompson-comparison-separates-accuracy-from-damage)
also shows that the larger damage bound alone does not settle a supplied
subtraction average. At rifle 20/current burst 0/distance 99, Grease's larger
roll divisor can outweigh its smaller damage draw; at rifle 40 the scalar
ordering reverses. This retains declared inputs rather than ranking whole
recruits or establishing damage per second.

## Close-range strength and Resistance recovery

Modern evidence: **November 7, 2026 studies and their linked earlier trials**.
These are tested-build outcomes, separate from historical source arithmetic
and later corrections. [Study limits](combat-results.md).

The modern veteran close group took Soldier/Thompson 44.41 seconds and
Resistance/Thompson 35.93. At medium distance those became 106.84 and 85.28.
Resistance's shorter empty-magazine recovery is a real role difference.
Thompson supports eligible hand grenades but not rifle grenades.
[Combat comparison](combat-results.md), [grenade output](grenades.md).
