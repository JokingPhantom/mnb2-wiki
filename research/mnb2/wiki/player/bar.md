[Player reference](README.md) · [Weapon comparison](weapon-comparison.md) ·
[Equipment](training-and-equipment.md)

# BAR

The BAR is a **6-TP automatic weapon upgrade**. It uses a burst counter, and recovery differs depending on whether ammunition remains. In the compared unarmored-hit path, it shares Garand’s **0–119 conditional health-damage draw**; the higher price does not itself mean more damage per hit. [Source comparison](../bar.md)

Applies to **historical selected 2.3.1g**. Damage rows are conditional draws,
not guaranteed health loss; refill rows apply only to the stated ordinary-soldier
recovery branch. A weapon purchase is not itself a completed recipient/refill.

| Key fact                          | Historical rule                                      |
| --------------------------------- | ---------------------------------------------------- |
| TP cost and availability          | 6 TP equipment offer; apply to an eligible recipient |
| Conditional unarmored damage draw | 0–119 health                                         |
| Above 300 distance                | Accuracy roll ×2                                     |
| Below 100 distance                | Accuracy roll ÷1.3                                   |
| Ordinary aiming burst initializer | 1–20 counter                                         |
| Specified empty-ammo refill       | 20 rounds                                            |

[Weapon offer and behavior evidence](../player-weapon-evidence.md).

On this page: [What does the extra TP buy?](#what-does-the-extra-tp-buy), [Sustained damage versus completed kills](#sustained-damage-versus-completed-kills).

## What does the extra TP buy?

In selected **2.3.1g**, BAR introduces an automatic burst route and a specified
20-round refill for the ordinary soldier. Its 6-TP price does not buy a larger
unarmored damage draw than the [2-TP Garand](m1-garand.md). Compare its burst
behavior with the job you need, rather than treating price as damage per bullet.
[Purchase, burst and refill evidence](../bar.md)

Rebuying BAR is not a refill shortcut in the inspected ordinary/Scout recipient
handler. A different pending weapon changes the weapon field without an ammo
write; a matching BAR instead has a guarded stored-cost credit. Compare the
[purchase versus refill example](weapon-comparison.md#does-buying-or-rebuying-a-weapon-refill-ammunition)
before treating the listed 20-round refill as something the menu purchase gives.

A longer current burst counter also makes the accuracy comparison harder.
High rifle skill helps that comparison but does not make every long burst
accurate. The retained source does not establish a minimum rifle skill for
equipping BAR, a best upgrade order or a kills-per-TP advantage. Buy the selection,
apply it to an eligible soldier, then inspect the resulting weapon.
[Burst and receipt limits](../bar.md), [equipment steps](training-and-equipment.md)

Long bursts are not uniformly accurate: this helper adds twice the current
positive burst counter to the accuracy roll before the weapon's distance
modifier. That changes a value compared with rifle skill, not the rifle stat
itself. The initializer has no experience/skill term at that particular write.
[Bound burst/distance evidence](../bar.md)

The inspected ordinary post-fire path assigns 200 minus experience when empty,
but 10 plus random 0–99 minus experience with ammo remaining. Neither counter is the
whole first-shot or retarget delay; callback order and animation entry still
matter. [Shooting cycle](how-shooting-works.md)

The retained community guide debates burst length, experienced shooters and
ammo efficiency. Those recommendations are attributed advice, not a tested
minimum skill 30 requirement or proof that BAR is the best upgrade. Buy and
apply are separate actions, and the selected receipt can overwrite equipment.
[Purchase/receipt and historical comparison](../bar.md)

Sources: [Source identities](../player-notes/bar.md#citation-1).
[Exact evidence](../player-weapon-evidence.md)

## Rifle 100 does not erase a long-burst penalty

High rifle skill does not erase the BAR’s burst and distance penalties. Exactly 100 loses its close-distance benefit; exactly 300 does not yet take the far penalty. The linked counts describe supplied individual comparisons, not an observed burst or final damage chance.

[Full source comparison and limitations](../player-notes/bar.md#rifle-100-does-not-erase-a-long-burst-penalty).

## Sustained damage versus completed kills

Modern evidence: **November 7, 2026 studies and their linked earlier trials**.
These are tested-build outcomes, separate from historical source arithmetic
and later corrections. [Study limits](combat-results.md).

BAR's bursts can spend shots on dead targets. In the earlier veteran group test,
68.6% of Soldier/BAR shots targeted already-dead enemies, and Garand cleared faster.
At intermediate stats BAR was nevertheless a strong single-target option.
[First-kill, crowd and wounded-target comparisons](combat-results.md).
BAR supports eligible hand grenades but produced no rifle grenades.
[Grenade output](grenades.md).

[Original opening and evidence context](../player-notes/bar.md#opening-before-player-language-correction).
