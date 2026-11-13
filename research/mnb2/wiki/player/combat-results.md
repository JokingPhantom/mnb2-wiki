[Player reference](README.md) · [Weapon comparison](weapon-comparison.md) · [Combat results](combat-results.md)

# Combat choices measured in the modern simulation

For stationary, unopposed veteran infantry in the November 7 test, the fastest
tested crowd-clearing packages were a deployed
Machine Gunner, Carbine-equipped ordinary infantry, and a close-range
Resistance/Thompson. A high-XP Recon was the standout grenade launcher.

These are **modern simulation measurements from November 7, 2026**, not measured
original Flash 2.3.1g rates or a whole-campaign strategy ranking.
The expanded study covers 17 infantry roles, 65 supported loadouts, 4,160
finite-target trials and 3,664 separate grenade-launch trials.
The archived build predates later Community receiver, burning-source and
Officer-equipment changes. Use these results for the tested packages; do not
assume unchanged rates for new loadouts or corrected branches.
[Corrections and preserved study scope](combat-issues.md).
Each expanded configuration has eight paired seeds. Units were stationary,
unopposed and without cover; MG/Mortar started deployed. Veteran comparisons
use XP/rifle 100/100. Natural kill progression remains active.
[Published study method](evidence-and-method.md#combat-study-method-and-limits). Raw study archives remain local research.

On this page: [Choose for the engagement](#choose-for-the-engagement) · [Why dummy DPS and first-kill speed can mislead](#why-dummy-dps-and-first-kill-speed-can-mislead) · [Springfield has a finishing niche](#springfield-has-a-finishing-niche) · [Equal stats do not give equal behavior](#equal-stats-do-not-give-equal-behavior) · [Native specialists and equipment limits](#native-specialists-and-equipment-limits) · [What these tests cannot settle](#what-these-tests-cannot-settle)

## Choose for the engagement

Mean simulation seconds to clear twenty fresh 100-HP infantry; lower is better.
Distances are formation centerlines in source units, not a weapon's exact range limit.

| Package               | Close: 75 | Medium: 250 | Far: 450 |
| --------------------- | --------: | ----------: | -------: |
| Deployed MG           |     19.19 |       20.07 |    52.82 |
| Soldier / Carbine     |     47.21 |       47.21 |    86.94 |
| Soldier / Thompson    |     44.41 |      106.84 |   106.84 |
| Resistance / Thompson |     35.93 |       85.28 |    85.28 |
| Resistance / Garand   |     65.42 |       65.42 |   102.54 |
| Soldier / Garand      |     69.50 |       69.50 |   121.73 |
| Soldier / BAR         |     80.81 |       86.87 |   109.34 |
| Soldier / Springfield |    120.23 |      120.23 |   237.55 |

The Carbine was a strong general veteran choice. Thompson favored the close
formation; Resistance's different recovery made it particularly effective.
Do not treat small differences, such as Resistance/Thompson versus Carbine at
far distance, as a certified ranking from eight seeds.
All roles, weapons, intervals and censoring (local research).

The deployed MG remained fastest at every tested distance, but deployment,
movement, return fire and squad cost were not measured here. It can change
targets during firing. An earlier diagnostic that prevented those target
changes increased group clearance from 20.32 to 84.75 seconds while preserving
the rest of that MG package.
Retargeting experiment (local research).

## Why dummy DPS and first-kill speed can mislead

A burst can continue into an already-dead target. In the earlier 32-seed group
test, Soldier/BAR spent 68.6% of shots on dead targets, versus Garand's 31.8%
and Springfield's 0%. Garand therefore cleared groups faster than BAR despite
BAR's higher sustained dummy damage. Spec Ops' longer semiautomatic sequences
can likewise increase waste.

Against one enemy, an MG did not necessarily score the fastest first kill.
At XP/rifle 50/50 in the earlier progression screen, BAR killed within five
seconds in 16/16 samples, Garand in 12/16, and MG in 15/16. These are controlled
stat samples, not guaranteed natural progression thresholds.
Single-target and crowd results (local research).

## Springfield has a finishing niche

Against groups starting at 20 HP, veteran Springfield averaged 58.48 seconds,
versus Soldier/Garand 57.81, Spec Ops/Garand 68.67 and BAR 74.99.
Springfield and Soldier/Garand had no clear difference in that sample.
At 50 HP, Soldier/Garand remained stronger; Springfield's apparent advantage
over BAR was uncertain. Native MG remained fastest throughout.

This supports a wounded-target finishing niche, not a universal veteran
Springfield upgrade. Carbine and Thompson were not included in that HP sweep.
Held-out wounded-target follow-up (local research).

## Equal stats do not give equal behavior

- Engineer, Signaller and Paratrooper matched Soldier exactly in all 384 paired
  trials per role across the six offered weapons, with their other jobs inactive.
- Spec Ops matched Soldier with Springfield, Thompson and BAR in these conditions,
  but its larger Garand/Carbine repeat counter could slow group clearance.
- Recon's frequent decisions did not improve firearm clearance; it can restart
  aiming. Its major measured advantage was high-XP grenade frequency.
- Sarge's support and chatter decisions change timing and the subsequent random
  sequence. Mixed small advantages do not establish hidden weapon bonuses.
- Resistance has distinct Garand/Thompson recovery, beyond displayed stats.

[Unit lifecycle and role differences](unit-lifecycle.md).

## Native specialists and equipment limits

In the archived pistol loadout, at medium distance, veteran Officer averaged 188.46 seconds to clear the group,
Crewman and Mechanic 250.66, and Sniper 182.89. Their jobs and survival value are
not represented by those clearance times.

Grease Gun was tested on Engineer and Spec Ops: group clearance was 52.81 seconds
close and 85.78 medium/far. It was useful but did not establish superiority over
Carbine. Other artificial Grease assignments were rejected by the current model;
this is not proof of original Flash behavior.

Mortar accepts stored firearm replacements in the experiment but still uses its
mortar attack. Bazooka's training code likewise does not turn it into a Garand.
Medic remains nonfiring. Bazooka/Mortar did not clear the fixture and some
specialists could incapacitate themselves; these results do not rank their
anti-vehicle or indirect-fire value.

High-XP Shotgun and Flamethrower firing gates, ignored equipment and flame
qualification failures require the cautions in [combat issues](combat-issues.md).
[Grenade strategy](grenades.md#measured-grenade-output-in-the-modern-simulation)
is separate from gun clearance.

## What these tests cannot settle

No survival, enemy return fire, movement, natural recruit value, cover, mixed-squad
crossfire or whole-campaign cost efficiency was measured. Grenade assays counted
launches before flight, not damage or kills. Flame group results with execution
or removal failures have no qualified clearance mean. Do not turn a timeout,
an unsupported loadout, or a failed execution into a measured kill rate.

## Supporting local research

The practical explanations above are self-contained. The following exact research
references are intentionally excluded from this published edition; their labels
identify retained evidence, not additional pages you need to play. Read the
[published evidence and study scope](evidence-and-method.md) or [edition guide](editions.md).

- [Full study and archives](../../experiments/unit-combat-expanded.md)
- [All roles, weapons, intervals and censoring](../../experiments/unit-combat-expanded.md)
- [Retargeting experiment](../../experiments/unit-combat-ttk.md)
- [Single-target and crowd results](../../experiments/unit-combat-ttk.md)
- [Held-out wounded-target follow-up](../../experiments/unit-combat-ttk.md#wounded-target-follow-up-declared-before-sampling)
