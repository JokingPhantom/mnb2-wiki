[Player reference](README.md) · [Progression](progression.md) · [Medals and ranks](career-medals-and-ranks.md)

# Career awards that change starting soldier stats

Career bonuses can change a recruit's **starting rifle, morale, experience or
weapon**. They do not all mean higher damage, and the same award does not make
every role start with identical stats. This guide follows selected 2.3.1g source
loads and award tests. [Exact source](../player-career-stat-evidence.md)

On this page: [When to expect the stat change](#when-to-expect-the-stat-change) · [A Regular Soldier's load has five distinct bonuses](#a-regular-soldiers-load-has-five-distinct-bonuses) · [Do not replace every role's base with the bonus](#do-not-replace-every-roles-base-with-the-bonus) · [Earning the award is another source path](#earning-the-award-is-another-source-path) · [Assault Expert changes enemy morale at selected loads](#assault-expert-changes-enemy-morale-at-selected-loads)

## When to expect the stat change

The listed stat bonuses are **load-time consumers**. A newly earned flag alone
does not re-execute an already living soldier's load; other later writers must
be traced separately. These source blocks do not certify an immediate squad
buff, a fully initialized start or persistent storage after every exit.
[Exact load and award evidence](../player-career-stat-evidence.md).

Use the table for the named role's starting fields, then check exceptions below.
A starting XP addition and a promotion check are separate steps.

## A Regular Soldier's load has five distinct bonuses

| Award                         | Change when its stored flag is positive at this selected load |
| ----------------------------- | ------------------------------------------------------------- |
| Combat Ribbon                 | +3 rifle skill                                                |
| Medal of Honor                | Another +3 rifle skill                                        |
| Defence Expert Award          | +10 morale                                                    |
| Meritorious Unit Commendation | Starting weapon becomes Garand                                |
| Mud and Blood Cross           | +9 experience                                                 |

The rifle additions stack at these two writes. They change rifle skill, not the
weapon's damage bound or a universal hit percentage. For a supplied base rifle 31
and morale 24, the relevant awards produce rifle 37 and morale 34. Ordinary XP 0
becomes 9; its initial rank is still a separate 0 write.
[How to read stats](reading-stats.md), [Regular Soldier](regular-soldier.md)

## Do not replace every role's base with the bonus

Mud and Blood Cross **adds 9 XP** in these selected loads: Medic 25→34, Officer 5→14
and Regular 0→9. The Medic still initializes rank 0; the Officer initializes rank 9.
Starting experience and starting rank are different fields.

The Medic's complete inspected load has the morale/XP bonuses but lacks the
Combat Ribbon/Medal of Honor rifle additions. The Allied Flamethrower load has
the Combat Ribbon rifle addition but lacks the Medal of Honor addition there.
These are named-load exceptions, not claims that later effects can never change
their stats. Their actual combat/ability controllers also remain different.
[Medic](medic.md), [Officer](officer.md), [Flamethrower](flamethrower.md)

## Earning the award is another source path

| Award                         | Selected numeric award test, with unset flag and display/ordering gates |
| ----------------------------- | ----------------------------------------------------------------------- |
| Combat Ribbon                 | Mission kill counter at least 100                                       |
| Medal of Honor                | Mission kill counter at least 200                                       |
| Defence Expert Award          | Career game counter above 10; career wave/game ratio above 49           |
| Meritorious Unit Commendation | Career wave counter at least 1000; career game counter below 26         |
| Mud and Blood Cross           | Career wave counter at least 5,000; career game counter below 51        |

Career waves, mission-total waves and local wave are separate. The mission kill
counter also has crew/AT writers, so the table does not promise an award after
exactly 100 unique visible enemies. These tests run in an ordered award chain;
an earlier qualifying award can take precedence. Full display/save timing remains
unqualified here. [Progression](progression.md), [wave counters](waves.md)

TP gifts, extra recruit requests and free-order allowances are other award
mechanisms. Their guards can even require a flag exactly 1 instead of merely
positive. [Career deployment gifts](deployment-gifts.md)

Sources: [Source identities](../player-notes/career-stat-bonuses.md#citation-1).
Original player explanation; no new award, recruit, profile or saving trial.

## Assault Expert changes enemy morale at selected loads

Its positive flag subtracts 10 in many enemy infantry loads, but sets Volkssturm
and Zombie morale to 2 instead. A fixed replacement is not a universal ten-point
penalty or a multiplier by wave. Those load fields then meet different pinning,
recovery and movement readers; the Zombie's selected forward step has no local
pin-field guard. [Exact load families and supplied reader comparisons](../player-enemy-morale-loads-evidence.md).
Additional source: [Source identities](../player-notes/career-stat-bonuses.md#citation-2)
