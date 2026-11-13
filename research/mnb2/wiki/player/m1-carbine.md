[Player reference](README.md) · [Weapon comparison](weapon-comparison.md) ·
[Equipment](training-and-equipment.md)

# M1 Carbine

A **2-TP weapon upgrade** and the Scout's base starting rifle, before the career
award that can substitute a Garand. It has a different close-distance modifier,
damage bound and refill state from the equally priced Garand.
[Scout](scout.md), [weapon comparison](weapon-comparison.md)

Applies to **historical selected 2.3.1g**. Damage rows are conditional draws,
not guaranteed health loss; refill rows apply only to the stated ordinary-soldier
recovery branch. A weapon purchase is not itself a completed recipient/refill.

| Key fact                             | Selected behavior                                                 |
| ------------------------------------ | ----------------------------------------------------------------- |
| TP cost and availability             | 2 TP equipment offer; base Scout rifle before career substitution |
| Conditional unarmored damage draw    | 0–99 health                                                       |
| Above 300 distance                   | Accuracy roll ×2                                                  |
| Below 100 distance                   | Accuracy roll ÷2                                                  |
| Specified ordinary empty-ammo refill | 15                                                                |

[Weapon offer and behavior evidence](../player-weapon-evidence.md).

On this page: [How does it differ from the equally priced Garand?](#how-does-it-differ-from-the-equally-priced-garand), [Compare current burst and the exact distance edge](#compare-current-burst-and-the-exact-distance-edge), [A strong measured general-purpose choice](#a-strong-measured-general-purpose-choice).

## How does it differ from the equally priced Garand?

Both menu upgrades cost 2 TP in selected **2.3.1g**. Carbine makes the
below-100 accuracy comparison easier than Garand does, but has a smaller
unarmored damage draw and takes its far-distance penalty sooner: above 300,
rather than above 350 source units. Equal price does not make the weapons
interchangeable or establish a best choice for every engagement.
[Weapon branches and offers](../player-weapon-evidence.md)

Both initialize a semi counter in the ordinary aiming path. That counter is
part of later repeat checks, rather than a promise of three immediate shots.
For the Scout's starting weapon, keep the role's own state and career
substitutions attached to the comparison. After buying an upgrade, apply it
and inspect the recipient. [Scout](scout.md),
[equipment steps](training-and-equipment.md)

The ordinary aiming path initializes a 1–3 semi counter, as for Garand. The
selected repeat gate depends on experience and a separate random comparison.
This is not proof of an immediate three-shot volley, a universal target-switch
advantage or complete elapsed-time firing statistics.
[Repeat and target-cycle explanation](how-shooting-works.md)

The specified ordinary empty-ammo recovery counter is 200 minus experience;
with ammo remaining it uses 10 plus random 0–99 minus experience. Keep that actor
and state attached to the numbers rather than applying them to every Scout or
specialist callback. Purchasing also does not prove immediate ammo reset.

The source's distance changes are roll modifiers. Exactly 300 avoids its
above 300 penalty and exactly 100 does not get its below 100 benefit; neither row
alone specifies the maximum distance at which an actor can select a target.

Sources: [Source identities](../player-notes/m1-carbine.md#citation-1).
[Version and exact evidence](../player-weapon-evidence.md)

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

## A strong measured general-purpose choice

Modern evidence: **November 7, 2026 studies and their linked earlier trials**.
These are tested-build outcomes, separate from historical source arithmetic
and later corrections. [Study limits](combat-results.md).

Soldier/Carbine cleared the veteran group in 47.21 seconds close/medium and
86.94 far in the modern simulation. It also supports rifle grenades.
Recon/Carbine was the strongest tested mixed grenade-output package, but G and
RG rates should be compared separately and are not measured damage.
[Combat comparison](combat-results.md),
[grenade categories](grenades.md#measured-grenade-output-in-the-modern-simulation).
