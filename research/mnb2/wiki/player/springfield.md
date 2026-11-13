[Player reference](README.md) · [Weapon comparison](weapon-comparison.md) ·
[Equipment](training-and-equipment.md)

# Springfield

The Regular Soldier's usual starting rifle, unless Meritorious Unit Commendation
replaces it with a Garand. The selected equipment menu also offers a **1-TP
Springfield downgrade**; returning to it is not advertised as a free universal
reset. [Purchase and source bindings](../player-weapon-evidence.md#weapon-offers)

Applies to **historical selected 2.3.1g**. Damage rows are conditional draws,
not guaranteed health loss; refill rows apply only to the stated ordinary-soldier
recovery branch. A weapon purchase is not itself a completed recipient/refill.

| Key fact                          | Selected behavior                                                   |
| --------------------------------- | ------------------------------------------------------------------- |
| TP cost and availability          | Starting rifle on the ordinary Regular Soldier; menu downgrade 1 TP |
| Conditional unarmored damage draw | 0–124 health                                                        |
| Above 400 source distance         | Accuracy roll multiplied by 2                                       |
| Below 100 source distance         | Accuracy roll divided by 1.1                                        |
| At 100 or 400                     | The corresponding strict distance modification does not apply       |

[Weapon offer and behavior evidence](../player-weapon-evidence.md).

On this page: [Should I replace the starting rifle?](#should-i-replace-the-starting-rifle), [Its ammo field does not select a Garand-style refill here](#its-ammo-field-does-not-select-a-garand-style-refill-here), [Measured finishing niche](#measured-finishing-niche).

## Should I replace the starting rifle?

Compare the firing cycle and engagement distance before spending TP. In selected
**2.3.1g**, the [2-TP Garand](m1-garand.md) changes the ordinary soldier's
repeat/refill behavior, while Springfield keeps a slightly larger damage draw
and takes its far-distance accuracy penalty later. That supports a tradeoff,
without establishing which rifle delivers more damage over a whole fight.
[Weapon and cycle evidence](../player-weapon-evidence.md)

Keeping a starting Springfield costs no equipment purchase. Choosing the menu's
1-TP downgrade later is a separate paid selection; it does not promise to refund
the previous weapon. Check the recipient's weapon after applying an upgrade.
[Purchase and recipient rules](../bar.md#buying-selects-a-pending-weapon-code)

Damage is drawn only after the appropriate accuracy and target checks. The
long-distance change is a roll penalty, not itself a hard 400-unit refusal to
fire. Garand uses a slightly smaller damage bound and an earlier far-distance
penalty, so “upgrade” does not mean every individual property increases.
[Comparison table](weapon-comparison.md), [Garand](m1-garand.md)

In the inspected ordinary-soldier post-fire branch, Springfield recovery is
10 plus random 0–99 minus experience, raised to 40 if below 40. That branch is different
from Garand's empty/nonempty ammo split and does not certify elapsed firing
rate. [Actor cycle](how-shooting-works.md)

A weapon selection can be pending until applied to an eligible recipient, and
an existing grenade/training/order action can take precedence. Inspect the actual
weapon after the receipt rather than assuming a menu click already equipped it.
[Recruitment and equipment](recruitment.md)

Sources: [Source identities](../player-notes/springfield.md#citation-1).
Selected 2.3.1g; [exact evidence](../player-weapon-evidence.md).

## Its ammo field does not select a Garand-style refill here

The ordinary load writes ammo 8 for the actor, but the selected Springfield
recovery branch has no ammo test or refill write. Garand recovery instead has
a distinct empty-magazine alternative. The later ordinary repeat action tests
positive ammo, while the shared firing helper has no positive-ammo admission
test of its own. These are different stages, not one universal magazine rule.

This does not certify an extra or infinite shot in actual play. The actual
call/refill/navigation sequence and inherited state remain necessary.
[Exact ammo readers and supplied states](../player-ammo-stage-evidence.md).
Additional source: [Source identities](../player-notes/springfield.md#citation-2)

## Measured finishing niche

Modern evidence: **November 7, 2026 studies and their linked earlier trials**.
These are tested-build outcomes, separate from historical source arithmetic
and later corrections. [Study limits](combat-results.md).

Veteran Springfield was slow against fresh groups but avoided dead-target firing
in the earlier study. Against 20-HP groups it beat BAR and Spec Ops/Garand and
approximately tied Soldier/Garand. This does not establish it as the best general
veteran weapon; Carbine was absent from that wounded-target sweep.
[Measured comparison](combat-results.md#springfield-has-a-finishing-niche).
