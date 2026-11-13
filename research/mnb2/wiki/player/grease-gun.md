[Player reference](README.md) · [Weapon comparison](weapon-comparison.md) · [Equipment](training-and-equipment.md)

# Grease Gun

The selected starting weapon for Engineer and Spec Ops, using the shared allied
Grease Gun branch. Its close-distance modifier and far-distance penalty differ
from Thompson even though both use 30 in the specified ordinary refill branch.
[Weapon comparison](weapon-comparison.md)

Historical scope: selected **2.3.1g** source. Modern findings, where listed,
are separate observations.

| Shared-helper property               | Selected behavior                                                                                               |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| Conditional unarmored damage draw    | 0–74 health                                                                                                     |
| Above 150 distance                   | Accuracy roll ×2                                                                                                |
| Below 100 distance                   | Accuracy roll ÷3                                                                                                |
| Specified ordinary empty-ammo refill | 30                                                                                                              |
| Cost and access                      | Starting weapon for Engineer (4 TP) and Spec Ops (5 TP); no standalone purchase in this selected equipment menu |

On this page: [Does the same weapon make Engineer and Spec Ops shoot alike?](#does-the-same-weapon-make-engineer-and-spec-ops-shoot-alike) · [Accuracy and damage can trade places in a supplied comparison](#accuracy-and-damage-can-trade-places-in-a-supplied-comparison) · [Artificial loadout coverage in the modern experiment](#artificial-loadout-coverage-in-the-modern-experiment)

## Does the same weapon make Engineer and Spec Ops shoot alike?

Their Grease Gun shots share the selected **2.3.1g** weapon's distance and damage
rules, but the recruits have their own combat controllers and specialist jobs.
Use the [Engineer](engineer.md) and [Spec Ops](spec-ops.md) cards to understand
their behavior; an ordinary soldier's refill table is not a complete firing
schedule for either specialist.
[Weapon and actor scope](../player-weapon-evidence.md)

Compared with [Thompson](thompson.md), Grease Gun has a smaller damage draw and
a stronger close-distance roll benefit, but its far-distance penalty starts
sooner. Neither the damage number nor the close-distance benefit alone tells
you which weapon produces more damage in a battle. The worked comparison below
keeps rifle skill and current burst explicit instead of ranking whole recruits.
[Declared comparison inputs](../player-weapon-evidence.md#close-range-grease-and-thompson-comparison-separates-accuracy-from-damage)

Exactly 150 does not trigger its above 150 penalty; exactly 100 does not trigger its
below 100 benefit. These are accuracy-roll modifications, not hard firing limits.
The smaller damage bound should be compared with actual actor state and firing
behavior, not converted directly into a universal DPS ranking.

The specified ordinary post-fire empty-ammo counter is 150 minus experience;
with ammo remaining it uses 10 plus random 0–149 minus experience. Engineer and
Spec Ops have distinct actor/controller paths, so this ordinary-soldier table
is not automatically their full firing schedule. [Cycle/state limits](how-shooting-works.md),
[Engineer](engineer.md), [Spec Ops](spec-ops.md)

Sources: [Source identities](../player-notes/grease-gun.md#citation-1). Selected 2.3.1g;
[evidence notes](../player-weapon-evidence.md).

The [Spec Ops actor's own preparation](spec-ops.md#its-own-firing-preparation-differs-from-the-ordinary-soldier)
now binds a separate Grease burst initializer 1–10 and matching selected fire/repeat
bodies. The ordinary preparation's absence of that initializer must not be copied
onto every Grease user. This still does not qualify the Engineer's or Spec Ops'
whole ready/first/repeat/next-target schedule.
Additional source: [Source identities](../player-notes/grease-gun.md#citation-2)

The [Engineer combat comparison](engineer.md#its-combat-actions-have-their-own-bindings)
also binds its Grease burst initializer 1–10 and selected own refill/recovery
expressions. Its preparation differs from Spec Ops for Garand/Carbine semi
counters, even where the firing/repeat action bytes match. No one shared weapon
name establishes their whole schedules.
Additional source: [Source identities](../player-notes/grease-gun.md#citation-3)

## Accuracy and damage can trade places in a supplied comparison

Against a separately supplied valid unarmored target at distance 99, rifle 20
and current burst 0, the Grease comparison passes 61 of 100 initial draws while
Thompson passes 41. Their eligible damage draws average 37 and 49.5, respectively.
Under declared independent inputs, the mean at that one direct subtraction site,
including zero when it is not reached, is 22.57 versus 20.295.

At supplied rifle 40 instead, the same calculation gives 37 versus 40.095.
This is why neither damage bound nor passing count alone ranks the whole weapon.
Burst 0 is an input here; actual specialist preparation, repeat, ammunition and
timing remain separate. [Exact ensemble, target state and limits](../player-weapon-evidence.md#close-range-grease-and-thompson-comparison-separates-accuracy-from-damage).

## Artificial loadout coverage in the modern experiment

Modern experiment dated **2026-11-07**; this is not a historical firing-rate measurement.

Engineer and Spec Ops supported Grease assignments; their veteran group
clearance averaged 52.81 seconds close and 85.78 medium/far. Other artificial
Grease assignments were rejected by the current model, not proved impossible
in the original Flash runtime. Grease is not a listed standalone purchase.
It supports eligible hand throws, not rifle grenades.
[Coverage and comparisons](combat-results.md), [grenade assay](grenades.md).
