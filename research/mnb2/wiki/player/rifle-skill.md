[Player reference](README.md) · [Reading stats](reading-stats.md)

# Rifle skill: accuracy and effective caps

**There is no universal effective cap at 100.** Rifle skill helps only where an
attack reads it. Weapon range modifiers, remaining burst and special unit rules
determine when more skill stops improving that attack.

This guide describes **current modern simulation rules, inspected November 7,
2026**, including the remaster's retained quirks and the named community-rule
exceptions. Its thresholds are arithmetic from the implementation, not measured
original Flash hit rates or a new historical-runtime qualification.

On this page: [player firearms](#player-firearms),
[special weapons and crew](#player-units-with-special-handling),
[enemy accuracy](#enemy-accuracy-and-caps) and
[why perfect accuracy is not guaranteed damage](#perfect-accuracy-is-not-guaranteed-damage).

## Player firearms

In the formulas, `random(n)` means a uniformly selected integer from 0 through
`n − 1`; **B** is the remaining burst counter at that attack. A distance
multiplier changes the comparison roll, not the damage draw.

Most player firearms roll an integer from 0 through 99, add **twice the remaining
burst counter**, apply the weapon's distance multiplier, then pass the accuracy comparison if the result
is **less than or equal to rifle skill**. A zero roll can therefore pass at zero
skill. The burst penalty generally shrinks as the burst progresses.

Skill changes accuracy, not the damage draw or firing speed. Experience affects
separate preparation, repeat and recovery stages; see [how shooting works](how-shooting-works.md).
[Shared firearm implementation](../player-modern-accuracy-evidence.md#weapons),
[Springfield implementation](../player-modern-accuracy-evidence.md#rules).

The following thresholds guarantee the **accuracy comparison** at **burst 0**.
They are rounded up to whole skill points. Distance is in battlefield pixels;
each threshold corresponds to the range band in the same position.

| Weapon                               | Distance bands and accuracy-roll multipliers                        | Skill thresholds at burst 0 |
| ------------------------------------ | ------------------------------------------------------------------- | --------------------------- |
| Springfield                          | Below 100: ÷1.1; 100–400: ×1; above 400: ×2                         | 90 / 99 / 198               |
| Garand                               | Below 100: ÷1.1; 100–350: ×1; above 350: ×2                         | 90 / 99 / 198               |
| Thompson                             | Below 100: ÷2; 100–200: ×1; above 200: ×3                           | 50 / 99 / 297               |
| Shotgun                              | Below 100: ÷3; 100 to below 200: ×1; 200 to below 400: ×3; 400+: ×5 | 33 / 99 / 297 / 495         |
| BAR                                  | Below 100: ÷1.3; 100–300: ×1; above 300: ×2                         | 77 / 99 / 198               |
| Carbine                              | Below 100: ÷2; 100–300: ×1; above 300: ×2                           | 50 / 99 / 198               |
| Grease Gun, the SAS/Spec Ops default | Below 100: ÷3; 100–150: ×1; above 150: ×2                           | 33 / 99 / 198               |
| Pistol                               | Below 100: ÷2; exactly 100: ×1; above 100: ×2                       | 50 / 99 / 198               |
| Sniper rifle and stationary .50      | No distance multiplier                                              | 99                          |

The ordinary shared weapons, sniper rifle and stationary .50 are in the shared
firearm implementation above. The [Grease Gun](../player-modern-accuracy-evidence.md#allied-sas)
and [pistol](../player-modern-accuracy-evidence.md#allied-officer) have separate readers.
The weapon equipped, rather than simply the recruit's role, selects these rules.
Inspected November 8: new modern Officers start with a Carbine and can use
ordinary weapons; the pistol row applies when a pistol is equipped. The added
Officer weapon timelines and rifle-grenade handling do not change the pistol
accuracy calculation. Community's post-scan correction changes when Spec Ops
can start a Shotgun attack, not its accuracy thresholds. Vehicle observation
fields do not change the fixed turret-skill readers below.
[Exact revision comparison](../player-evidence-reconciliation-101.md).

### Why skill above 100 still helps

For remaining burst counter **B**, the maximum possible modified roll is:

`(99 + 2B) × distance multiplier`

Skill at least this value passes every accuracy draw in that supplied situation.
For whole-number skill, round the result upward. For example:

- A long-range Thompson at B = 6 needs `(99 + 2×6) × 3 =` **333** skill.
- A long-range BAR at B = 20 needs **278** skill.
- A burst-0 sniper rifle needs **99** skill at any eligible firing distance.

These examples use counters that can be initialized by the respective weapons;
they do not promise a particular number of shots or hits per attack cycle.
An ordinary Springfield's burst-0 accuracy stops improving at 99 in its middle
range, but skill can still help up to 198 beyond 400 pixels.

The shotgun also loses damage with distance: its damage draw is 0–199 below 100,
0–99 from 100 to below 200, 0–9 from 200 to below 400, and 0–4 at 400+.
Perfect accuracy cannot restore its close-range damage.

## Player units with special handling

| Unit or weapon                                                 | What rifle skill actually changes                                                                                                                                                             |
| -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Handheld Machine Gunner                                        | Compares skill with `random(200) × machine-gunner count + 2B`, with no distance modifier. The maximum is **199 × count + 2B**. More counted machine gunners make handheld fire less accurate. |
| Deployed Machine Gunner                                        | Uses `random(100) + 2B`, divided by 3 below 100 pixels, unchanged at 100–300, doubled above 300. Its maximum authored B of 32 gives a long-range threshold of **326**.                        |
| Jeep MG and half-track hull MG                                 | Subtract `2B` from the 0–99 roll: a larger positive burst counter helps accuracy. No distance multiplier; threshold **99 − 2B**.                                                              |
| Sherman coax MG                                                | Uses an unmodified 0–99 roll and saturates at **99**.                                                                                                                                         |
| Half-track quad .50                                            | Uses fixed skill 5 rather than the vehicle's rifle stat. The inclusive comparison admits 6 of 100 raw rolls; raising the vehicle stat does not improve it.                                    |
| 20mm AA versus aircraft                                        | Rolls 0–399 and succeeds strictly below skill. Whole-number skill saturates at **400**; skill 100 passes 25% of individual interception rolls. Ground-shell scatter is separate.              |
| Mortar, bazooka, flamethrower, grenades, artillery and rockets | Their normal explosive/flame attacks do not use rifle skill to improve accuracy or scatter. A displayed rifle number does not imply such a bonus.                                             |

The deployed Machine Gunner also preserves a targeting quirk: it measures
distance before possibly choosing a different target for the shot.
[Machine Gunner calculation](../player-modern-accuracy-evidence.md#machine-gunner-fire),
[count and vehicle gun consumers](../player-modern-accuracy-evidence.md#registered-infantry),
[Jeep/hull MG](../player-modern-accuracy-evidence.md#allied-jeep),
[Sherman coax](../player-modern-accuracy-evidence.md#allied-sherman),
[AA interception](../player-modern-accuracy-evidence.md#allied-aa).
For attacks with separate projectile rules, see [blast and scatter](blast-radius-and-scatter.md),
[Mortar](mortar.md), [Bazooka](bazooka.md) and [Flamethrower](flamethrower.md).

### Replacement crew do not always supply the effective stat

In remaster rules, a replacement Jeep gunner writes skill to its turret, but the
Jeep's shots still read the parent vehicle's rifle skill. Even the Jeep's
promotion skill increase goes to that unused turret field. Replacement AA crew
write to a missing gunner component, leaving the cannon's effective skill intact.
The community rules correct both crew-skill transfers; the Jeep then reads its
turret skill. A replacement stationary .50 gunner does transfer skill to the
effective field. Do not assume every vehicle inherits its new crewman's skill.
[Crew transfer and Jeep promotion](../player-modern-accuracy-evidence.md#allied-jeep),
[AA ruleset difference](../player-modern-accuracy-evidence.md#allied-aa).

## Enemy accuracy and caps

Enemy small arms generally do **not** use the player's weapon-distance
multipliers. Most compare a 0–99 integer roll **strictly below** skill, rather
than the player's inclusive comparison. These are whole-number thresholds for
passing every accuracy draw, conditional on reaching the shot and having an
eligible target:

| Enemy                                                                                                           | Accuracy comparison                       | Whole-number skill threshold                                         |
| --------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | -------------------------------------------------------------------- |
| Ordinary rifle infantry, Volkssturm, grenadiers, Jugend, Brandenburgers, infiltrators, paratroopers and snipers | `roll < skill`                            | 100                                                                  |
| Machine Gunner                                                                                                  | `roll < skill − 3B`                       | 100 + 3B                                                             |
| Scout and Pioneer                                                                                               | `roll + 2B < skill`                       | 100 + 2B                                                             |
| SS                                                                                                              | `roll < skill − 2B`                       | 100 + 2B                                                             |
| Officer                                                                                                         | `roll < skill` **and distance below 200** | 100 within range; no amount of skill overcomes the range restriction |

Some enemies have half-point skill values. The exact saturation condition is
**skill greater than 99 plus the burst penalty**, so 99.5 already saturates an
unpenalized enemy roll. Unlike a player firearm, skill 0 cannot pass that roll.
[Enemy accuracy, firing gates and cover saves](../player-modern-accuracy-evidence.md#enemy-cover-fire).

At B = 32, an enemy Machine Gunner needs whole-number skill **196** to erase its
accuracy penalty. An SS burst initialized to B = 6 needs **112**. Higher skill
can therefore remain useful beyond 100 for these enemies too.

Enemy Snipers start with rifle skill equal to the local wave, reaching the
unpenalized whole-number accuracy threshold at **wave 100**. Many ordinary enemy
loads instead draw skill from `random(wave) / 2`; SS draws from `random(wave)`.
These are individual load rules, not one wave-wide hit percentage.
[Sniper load](../player-modern-accuracy-evidence.md#enemy-sniper),
[ordinary load](../player-modern-accuracy-evidence.md#rules),
[SS load](../player-modern-accuracy-evidence.md#enemy-ss), [enemy stats](enemy-stats.md).

Enemy Jeep, SdKfz half-track and Tiger MGs use **fixed turret skill 1**, rather
than the parent's displayed rifle stat. The SdKfz 222 reads its separate turret
skill, whose unpenalized roll saturates at whole-number skill 100. Enemy mortar,
flamethrower and Panzerschreck attacks likewise do not gain accuracy from their
rifle field. [Vehicle gun consumers](../player-modern-accuracy-evidence.md#registered-infantry),
[fixed Jeep turret skill](../player-modern-accuracy-evidence.md#enemy-jeep).

## Perfect accuracy is not guaranteed damage

Several enemies first pass an independent `random(100) < 10 + experience`
firing gate. Rifle skill cannot remove that gate. Protection and damage are
also separate: ordinary cover and bunker saves can reject an accurate shot,
armor can prevent damage, and a damage roll can be zero. Enemy snipers skip
the bunker-save check, but still face ordinary cover.

Once the relevant accuracy comparison saturates, extra skill does not defeat
those other checks. See [defenses](defenses.md), [reading stats](reading-stats.md)
and [shooting stages](how-shooting-works.md) before treating an accuracy threshold
as a guaranteed kill or a measured rate of fire.
