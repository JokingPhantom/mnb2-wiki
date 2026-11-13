[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Weapon comparison](weapon-comparison.md)

# Sniper

A **6-TP infantry specialist** with a sniper rifle, called Scoped Springfield
by the legacy guide, and a higher starting rifle-skill value than the Regular
Soldier. Its targeting path can select hidden
enemies without requiring their visibility counter to be positive. Concealment
and that selection ability make it useful to consider against hidden infantry;
line of sight and other eligibility checks still apply. Targeting evidence (local research)

| Starting property        | Selected 2.3.1g ordinary load profile                           |
| ------------------------ | --------------------------------------------------------------- |
| Recruitment              | Reinforcements menu; base price 6 TP                            |
| Health                   | 100 health points                                               |
| Rifle skill              | Random: starts at 40 and receives one or more additions of 1–10 |
| Morale                   | 10–39 before career bonuses                                     |
| Experience               | 0 before career bonuses                                         |
| Weapon                   | Sniper rifle (legacy name: Scoped Springfield)                  |
| Initial ammunition state | 1 round                                                         |

The rifle loop has a random stopping rule, just like the Regular Soldier's.
The legacy community card's **45–80 rifle** and **20–50 morale** are separately
reported ranges, not the base distributions of this selected load profile.
Scenario overrides, career bonuses and later changes must be considered apart
from these defaults. Starting-stat evidence (local research)

## When to choose it and what to check

Consider the **6-TP Sniper** when hidden infantry is the problem. Ordinary
infantry costs **3 TP**, leaving more of the same budget for another job; the
Sniper's targeting eligibility does not establish twice the kills or protection
from explosions. Compare the [recruitment choices](recruitment.md) before spending.

Recruit it through Reinforcements, inspect the actual soldier, and use the
[ordinary click-and-destination controls](controls.md). Watch what it targets
and whether it fires; hiring one does not reveal every hidden enemy to the squad.
If it stops, check health, pinning, morale, orders and target eligibility in the
[nonfiring checklist](why-soldiers-stop-shooting.md). An apparently transparent
Sniper can still be harmed. Do not budget a replacement weapon assuming the
Regular Soldier's equipment rules apply.

## Concealment and target choice

The community guide describes the Sniper becoming transparent between shots and
warns that nearby explosions can still hit it. The selected source has separate
visibility-counter, drawing-opacity and targeting logic. A transparent soldier
should not be treated as immune to attack. Sniper research (local research)

One firing-frame path sets its visibility counter to **100 minus experience**;
another frame sets it to **100**. Its unpaused controller decreases a positive
counter. These paths do not establish a universal four-second reveal interval
or permanent invisibility at 100 experience. The old guide's 80-tick description
is not an exact match for every selected source path. Visibility evidence (local research)

The inspected targeting path ignores the candidate's positive-visibility
requirement, but still checks line of sight, health, armor/crew and melee state.
The Sniper's own morale, health, pinning and action state also matter. This
supports a specialist targeting role; it does not mean hiring one globally
reveals every concealed enemy to the entire squad. Targeting evidence (local research)

## Control, upgrades and progression

Use the ordinary soldier click-and-destination movement interface and hover to
inspect stats. [Controls](controls.md) identifies which instructions have
recorded playback evidence. The community guide says Snipers cannot receive
replacement weapons or rifle grenades; full recipient qualification remains
open, so do not assume the Regular Soldier's equipment menu applies identically.
Community report and source limits (local research)

The selected Sniper load adds **3 rifle skill** for Combat Ribbon and another
**3** for Medal of Honor, **10 morale** for Defence Expert Award, and **9 starting
experience** for Mud and Blood Cross. These are separate career bonuses.
Grenade capability starts off and has a career-dependent random grant; it is
not guaranteed for every Sniper. Career and equipment bindings (local research)

The selected Sniper Ranger Training receipt grants grenade capability and adds
**15 rifle and 15 morale**. That specific block has no ordinary weapon-replacement
write. It is a separate source-bound receipt from the Regular/Scout's random
stat additions; applying the pending upgrade still needs its actor/state guards.
[Training comparison](training-and-equipment.md), exact receipt (local research)

## Practical limits

Budget 6 TP against the Regular Soldier's 3 TP base price. The specialist's
higher rifle initialization and hidden-target selection are concrete differences;
comparative kills per TP, full concealment safety and shot-to-shot timing have
not been measured here. The community describes slow fire that improves with
experience. A precise reaction/reload/retarget cycle needs the separate mechanics
reconstruction rather than a conversion from one animation counter.
Open timing questions (local research)

Sources: Source identities (local research). See evidence notes (local research).

## First-kill power is separate from group clearance

**Modern section: archived November 7 simulation, not historical Flash.**

Modern measurements: **November 7, 2026 simulation build**. The historical
2.3.1g facts above are separate; [study limits and later corrections](combat-results.md)
apply to the comparison below.

Sniper uses a harder preparation draw than ordinary infantry: random(200)
compared with 10+XP, plus its separate one-round recovery/refill. Hidden-target
eligibility and priority selection do not guarantee fast crowd clearing.
In the modern veteran medium group test it averaged 182.89 seconds.
An accepted hand-grenade flag produced no throws.
[Results](combat-results.md), [lifecycle](unit-lifecycle.md), [equipment issue](combat-issues.md).

## Supporting local research

The practical explanations above are self-contained. The following exact research
references are intentionally excluded from this published edition; their labels
identify retained evidence, not additional pages you need to play. Read the
[published evidence and study scope](evidence-and-method.md) or [edition guide](editions.md).

- [Targeting evidence](../player-pilot-evidence.md#concealment-and-hidden-targets)
- [Starting-stat evidence](../player-pilot-evidence.md#starting-stats)
- [Sniper research](../sniper.md)
- [Visibility evidence](../player-pilot-evidence.md#concealment-and-hidden-targets)
- [Targeting evidence](../sniper.md)
- [Community report and source limits](../sniper.md)
- [Career and equipment bindings](../player-pilot-evidence.md#career-bonuses)
- [exact receipt](../ranger-training.md)
- [Open timing questions](../player-pilot-evidence.md#open-mechanics-questions)
- [Source identities](../player-notes/sniper.md#citation-1)
- [evidence notes](../player-pilot-evidence.md)
