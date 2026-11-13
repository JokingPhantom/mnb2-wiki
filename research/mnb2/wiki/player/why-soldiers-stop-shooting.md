[Player reference](README.md) · [Orders](orders.md) · [Shooting stages](how-shooting-works.md)

# Why is a soldier not shooting?

Start with the soldier's **current health, action and target**, then check orders
and cover. Rifle skill alone cannot tell you whether an attack was requested.
This guide uses selected 2.3.1g ordinary-soldier source paths; specialists have
additional choices. It is a checklist of possible causes, not a guaranteed live
status detector. [Shooting stages](how-shooting-works.md)

On this page: [Work through the question in this order](#work-through-the-question-in-this-order) · [Check readiness before buying more skill](#check-readiness-before-buying-more-skill) · [An enemy on screen is not necessarily the chosen target](#an-enemy-on-screen-is-not-necessarily-the-chosen-target) · [A pause between shots is not always a refill](#a-pause-between-shots-is-not-always-a-refill) · [Specialists can spend a decision on another job](#specialists-can-spend-a-decision-on-another-job) · [Keep the observation specific](#keep-the-observation-specific)

## What can I do next?

Use this recovery shortlist for **selected historical 2.3.1g**. It does not
promise an immediate shot after an action; the unit still needs its own readiness
and target checks.

| What you notice                       | Practical next check                                                                                              | What would count as progress                                                                                |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Wounded, pinned or fleeing soldier    | Inspect health/morale and the [wound and rescue rules](wounded-and-rescued.md); do not buy rifle skill as a cure. | The unit can act again, then makes an eligible attack; an unpinned animation alone is insufficient.         |
| Soldier protected but idle            | Check [cover restrictions](specialists-under-cover.md) for that role and current orders.                          | Its ability or target search resumes under qualifying conditions; moving the drawing alone proves neither.  |
| Soldier attacks a tank without effect | Compare [anti-tank choices](anti-tank-options.md).                                                                | A suitable attack reaches its damage checks; an ordinary rifle sound is not hull damage.                    |
| Pause after a weapon change           | Check [replacement versus refill](weapon-comparison.md#does-buying-or-rebuying-a-weapon-refill-ammunition).       | A later shot/refill follows the actual actor rules, rather than another purchase being assumed to reset it. |
| Support specialist seems idle         | Check [what that role does](recruitment.md#are-support-recruits-also-extra-riflemen).                             | A job or attack that the role actually supports occurs; a Medic is not a spare rifleman.                    |

If the situation remains unclear, record the current role, weapon, order and
what actually happened before changing several things at once. The detailed
checks below explain why these observations matter.

## Work through the question in this order

1. **Identify the role and actual weapon.** A Medic's initialized weapon field
   does not make it an ordinary rifleman. A specialist may spend its decision on
   aid, healing or repair. [Recruit roles](recruitment.md), [Medic action scope](../player-medic-controller-evidence.md).
2. **Check readiness and orders.** Health, morale, pinning, withdrawal, pause and
   current action state can block a fresh search. Check the table below before
   buying rifle skill. [Ordinary controller](../player-weapon-evidence.md#ordinary-soldier-cycle).
3. **Check the target and protection.** An enemy drawing on screen does not
   establish that it passed this actor's target, sight or cover-related guards.
   [Exact target filters](../player-ordinary-target-evidence.md).
4. **Separate no shot from no damage.** A sound, fire visit, projectile, hit-counter
   change and health loss are different events. A rifle aimed at tank-class
   armor need not damage the hull. [Observed rifle example](observed-rifle-sequence.md),
   [small arms against vehicles](small-arms-against-vehicles.md).

This route explains possible causes in **selected historical 2.3.1g**. It does
not diagnose a new encounter from a screenshot or provide a measured reload fix.

## Check readiness before buying more skill

- **Health below 10.** The ordinary active controller requires health at least 10; positive health alone is insufficient. [Wounded and rescued](wounded-and-rescued.md).
- **Pinning or fleeing.** Ordinary fresh acquisition needs positive morale and an unpinned, nonwithdrawn actor; clearing pinning can still lead to fleeing. [Morale and recovery](morale.md).
- **Hold Fire or another positive action counter.** The ready controller can take its decrement/cap alternative instead of a fresh search. [Hold Fire](hold-fire.md).
- **Off-field protection.** The ordinary target-search entry also excludes its invincible state. [Protection flag](protection-flag.md).
- **Palisade or bunker classification.** The ordinary admitted search needs palisaded false; a bunkered search has an additional below 15 random gate. [Protection and ability differences](specialists-under-cover.md).

A bunker can protect against particular incoming bullets while also making one
ordinary acquisition gate harder to pass. The below 15 comparison belongs to
that ready-search branch; it is not a universal 85% fire-rate reduction. Pillbox
classification, current overlap and actor-specific guards must be checked
separately. Moving a drawing is not proof of a changed protection-query result.
[Exact ordinary entry and counter scope](../player-weapon-evidence.md#ordinary-soldier-cycle)

Likewise, a rally sound or unpinned animation is not proof all readiness fields
were cleared. The ordinary recovery branch can replace its counter and still
choose fleeing at nonpositive morale. [Recovery writes](../player-pin-recovery-evidence.md)

## An enemy on screen is not necessarily the chosen target

The ordinary search checks living health, visibility, line of sight, melee
compatibility and armor/crew state before accepting a closer target. It is not
simply a click on the nearest visible drawing. For a light vehicle, its selected
crew-sum filter reads driver+gunner; spare crew does not replace those two fields.
[Exact filters and strict ties](../player-ordinary-target-evidence.md)

A tank-class 2 enemy can pass that acquisition filter even though the later
ordinary shared firearm takes a ricochet path rather than damaging its hull.
A soldier aiming at a tank therefore need not have a useful anti-tank weapon.
[Small arms and crews](small-arms-against-vehicles.md), [AT choices](anti-tank-options.md)

The later shared shot reads the current target index and current distance.
An earlier search range is not frozen accuracy for a moving target, and a repeat
request is not another complete target search. [Later readers](../player-repeat-state-evidence.md)

## A pause between shots is not always a refill

Aim preparation, burst/semi repeats and recovery have separate counters and
navigation requests. Ordinary Garand/Carbine repeats need the admitted semi
branch's XP-dependent comparison; even XP 100 accepts only 11 of its 20 supplied
integer inputs. That is a conditional comparison count, not shots per second.
[Repeat states](../player-weapon-state-evidence.md#the-semi-comparison-is-per-visit-and-experience-dependent)

Equipment receipt changes selected fields, rather than guaranteeing a fresh
magazine and normalized burst/semi counters. An order can also change a target
field without proving that the attack animation or projectile reached its
firing action. [Retargeting orders](retargeting-orders.md), [weapon replacement](../player-weapon-state-evidence.md)

## Specialists can spend a decision on another job

A Paratrooper with a positive healing-kit pool can choose the healing alternative
before fresh combat search. It writes a counter even if no patient later passes
the scan. Sarge can choose support instead of the sibling combat search; a
support attempt without a qualifying recipient does not automatically fall
through to an ordinary shot at that site.
[Paratrooper decision](../player-paratrooper-combat-evidence.md),
[Sarge decision](../player-sarge-support-evidence.md)

Medic healing, Officer aid, Mechanic repair and other specialist actions need
their own actor rules. A shared weapon name does not turn every role into an
ordinary soldier. [Roles](recruitment.md), [specialists under cover](specialists-under-cover.md)

## Keep the observation specific

For a reproducible question, record the role, weapon, health, morale/pinning,
order, target type, protection and whether a shot sound, projectile, health loss
or statistic actually occurred. These are different observations. Exact first-
shot and retarget times still need qualified callback scheduling; this checklist
does not give a universal reload fix, safe cover placement or measured delay.
[One qualified rifle observation](observed-rifle-sequence.md)

Sources are the linked original source notes for selected 2.3.1g; no new gameplay
trial, reconstruction recipe or acceptance of later candidates is claimed here.

[Source identities](../player-notes/why-soldiers-stop-shooting.md#citation-1)

The [ordinary Shotgun decision](shotgun.md#one-ordinary-decision-has-an-xp-dependent-fallback)
has another source-specific request gate. Its distance expression reads the
search index and its false-distance fallback uses a roll above XP. Preserve
that exact reader before diagnosing an apparent range cutoff or slower veteran;
this local condition is not a universal firing rate or an initialized bug report.

Melee state is another [fresh-search compatibility filter](close-combat-and-bayonets.md#melee-can-affect-teammates-fresh-target-searches).
The fighting helper can set that state before doing injury, while a later shared
shot has no repeated melee-state read. Do not diagnose the two stages from a
single animation or assume the state gives universal protection from bullets.
