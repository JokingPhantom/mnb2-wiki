[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Weapon comparison](weapon-comparison.md)

# Regular Soldier

A **3-TP general-purpose infantry recruit**, equipped with a Springfield unless
your career award supplies a Garand. Choose this unit when you want ordinary
infantry that can receive equipment and training; inspect each recruit's rifle
skill and morale before deciding where to invest. The legacy community guide
reports four free soldiers in regular deployment. [Recruitment and deployment](../player-pilot-evidence.md#recruitment-and-controls)

| Starting property | Selected 2.3.1g ordinary load profile                           |
| ----------------- | --------------------------------------------------------------- |
| Recruitment       | Reinforcements menu; base price 3 TP                            |
| Health            | 100 health points                                               |
| Rifle skill       | Random: starts at 10 and receives one or more additions of 1–10 |
| Morale            | 20–29 before career bonuses                                     |
| Experience        | 0 before career bonuses                                         |
| Weapon            | Springfield; M1 Garand with Meritorious Unit Commendation       |

These are load defaults, before scenario overrides and later changes. Rifle
skill has a random stopping rule: after each addition, another roll decides
whether to repeat. The initializer does not impose a fixed maximum. The old
community card's **15–45** is not a dependable starting range for this reference.
[Rifle rolls and stat evidence](../player-pilot-evidence.md#starting-stats)

## Using and equipping a soldier

Click the soldier and then its destination; hover to compare its stats. To issue
a [Garand](m1-garand.md), buy the 2-TP upgrade in equipment and select an eligible
recipient. Payment selects a pending weapon; the recipient click applies it.
Earlier pending grenade, training or order actions can take precedence. The
ordinary recipient must have more than 9 health for this equipment path.
[Controls and equipment evidence](../player-pilot-evidence.md#recruitment-and-controls)

Rifle skill participates in the shot's accuracy comparison, but distance, burst
state, target armor and health also affect the outcome. A skill of 40 should not
be read as a guaranteed 40% chance of damaging any target. The Springfield's
long-distance penalty starts above 400 source distance units; the Garand's
starts above 350. Neither threshold alone is a hard firing cutoff.
[Weapon behavior](m1-garand.md), [rifle distance](../rifle-distance.md)

## Training and progression

Career awards change the load defaults independently:

| Award                         | Effect in this load profile                |
| ----------------------------- | ------------------------------------------ |
| Combat Ribbon                 | +3 rifle skill                             |
| Medal of Honor                | Another +3 rifle skill                     |
| Defence Expert Award          | +10 morale                                 |
| Mud and Blood Cross           | +9 starting experience                     |
| Meritorious Unit Commendation | Start with a Garand instead of Springfield |

These are stat-point additions, not percentage multipliers. Ordinary soldier
rank progression and career medals are separate systems. [Award bindings](../player-pilot-evidence.md#career-bonuses),
[soldier promotions](../soldier-promotion.md)

The 5-TP Ranger Training offer can change equipment as well as stats; the
inspected infantry receipt supplies a Garand and grenade capability and adds
random rifle and morale bonuses. Read [Ranger Training](../ranger-training.md)
before replacing equipment you already bought. That article identifies its
recipient scope and the community/source morale discrepancy.

## Practical limits

This recruit costs half the Sniper's base price, while the Sniper starts its
rifle accumulator 30 points higher. That comparison alone does not determine
which purchase produces more kills. Keeping a soldier alive also preserves its
individual experience and later promotion opportunities; it does not promise
a fixed firing rate. First reaction, repeated fire and switching targets still
need separate timing models. [Sniper](sniper.md), [remaining mechanics questions](../player-pilot-evidence.md#open-mechanics-questions)

Sources: [Source identities](../player-notes/regular-soldier.md#citation-1).
Version and exact rows are in the linked [evidence notes](../player-pilot-evidence.md).

## Equal-stat modern combat comparison

Modern measurements: **November 7, 2026 simulation build**. The historical
2.3.1g facts above are separate; [study limits and later corrections](combat-results.md)
apply to the comparison below.

Soldier is the reference controller. At XP/rifle 100/100, Carbine cleared the
medium-distance group in 47.21 simulation seconds, versus Garand 69.50,
BAR 86.87 and Springfield 120.23. Thompson was stronger in the close formation.
Engineer, Signaller and Paratrooper exactly matched Soldier across six offered
weapons when their other jobs were inactive.
[Results and limits](combat-results.md), [ordinary lifecycle](unit-lifecycle.md).
