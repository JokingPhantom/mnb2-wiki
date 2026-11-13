[Player reference](README.md) · [Recruitment](recruitment.md) · [Reading stats](reading-stats.md)

# Repair, replace crew or reload?

Repair, crew replacement and reload solve **different problems**. Restored vehicle health does not replace a missing gunner, and a new gunner does not repair the hull. Start with the missing function, then check the relevant role’s requirements.

Historical scope: selected **2.3.1g**.

| Missing function                       | Recruit/action cost                                                                     | Selected state change                                                   |
| -------------------------------------- | --------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| Heal an injured unarmored soldier      | [Medic](medic.md), 3 TP recruit                                                         | +1 health for eligible patients above 0 and below 100                   |
| Repair a supported vehicle/emplacement | [Mechanic](mechanic.md), 3 TP recruit                                                   | +1–6 health in each qualifying recipient branch                         |
| Fill a supported missing crew role     | [Crewman](crewman.md), 3 TP recruit                                                     | Writes a missing role to 1, with role-specific stat/animation transfers |
| Refill an empty rocket launcher        | [Launcher button](rocket-launcher.md#fire-and-refill-are-different-button-states), 1 TP | Restores loaded 16 without clearing its separate cooldown               |

The first three prices buy the recruit, not one healing point, one repair point
or a guaranteed completed transfer. The healer/Mechanic/Crewman must still be
usable and their actual recipient checks must pass. These are base costs and
selected actions, not completed transaction observations.

On this page: [Start with the missing function](#start-with-the-missing-function) · [Which vehicles have selected support branches?](#which-vehicles-have-selected-support-branches) · [A veteran replacement can replace recorded stats](#a-veteran-replacement-can-replace-recorded-stats) · [Full health and a crew flag do not settle readiness](#full-health-and-a-crew-flag-do-not-settle-readiness) · [A healthy gun can still have a counter that is not decreasing](#a-healthy-gun-can-still-have-a-counter-that-is-not-decreasing)

## Start with the missing function

- **Hull health is low.** A Mechanic needs a supported type, a passing health/distance test and its own usable state. Restoring health does not write a missing crew role. [Repair branches](mechanic.md).
- **A driver or gunner is missing.** Use the selected Crewman role table below; eligibility and gunner-first priority differ by recipient. Do not infer a Sherman selector from another vehicle. [Crew replacement](crewman.md).
- **The rocket launcher is empty.** Its selected 1-TP refill restores loaded 16, while its separate cooldown and other firing checks remain. [Fire versus refill](rocket-launcher.md#fire-and-refill-are-different-button-states).
- **Health looks repaired but the gun is still waiting.** A counter can sit behind crew, protection or settled-position admission. Repair alone need not reach that counter branch. [Waiting counters](#a-healthy-gun-can-still-have-a-counter-that-is-not-decreasing).
- **Vehicle XP changed after a gunner replacement.** The selected gunner branches copy incoming XP/rank rather than adding them or preserving the larger value. Driver alternatives differ. [Replacement fields](#a-veteran-replacement-can-replace-recorded-stats).

These are **selected 2.3.1g** routes into the existing evidence, not a promise
that one visible symptom identifies every hidden state or that the next click
restores the whole vehicle. Follow the individual recipient and later reader.

## Which vehicles have selected support branches?

| Recipient       | Mechanic health must be below                          | Selected Crewman roles                                   |
| --------------- | ------------------------------------------------------ | -------------------------------------------------------- |
| Jeep            | 500                                                    | Gunner first, otherwise driver                           |
| 20 mm AA        | 300                                                    | Gunner                                                   |
| M3 AT gun       | 500                                                    | Gunner first, otherwise driver                           |
| Static .50      | 200                                                    | Gunner                                                   |
| Halftrack       | 800                                                    | Gunner first, otherwise driver                           |
| Sherman         | 1000                                                   | No Sherman selector in this selected Crewman branch list |
| Rocket launcher | No matching type in this selected Mechanic branch list | Gunner first, otherwise driver                           |

The Mechanic list is six type/health alternatives, with armored recipients and
strict source distance below 150. Crew replacement instead requires its own armored
recipient and source distance strictly below 25. Those distances are source inputs,
not a calibrated screen ruler. A visually close vehicle can still fail other
actor or recipient gates.
[Mechanic scan](../player-mechanic-scan-evidence.md), [Crewman role table](../crewman.md)

The table's missing selectors are bounded findings about those selected bodies.
They do not certify every possible alternate repair, module, mode or lifecycle
path. Health values are repair **entry thresholds**, not assignments to a maximum.
Neither adding health nor a wrench animation replaces the named crew fields.
[Repair animation versus health addition](mechanic.md)

## A veteran replacement can replace recorded stats

At a selected gunner replacement, the Crewman's XP and rank replace the parent
vehicle's old values. For supplied old XP 80 and incoming XP 0, that write is 0,
not 80 or 80 plus a bonus. Rifle recipients differ between vehicles and can differ
from the field a later gun actually reads. Driver alternatives do not perform
those XP/rank/rifle copies.
[Exact replacement and reader boundaries](crewman.md#a-replacement-gunner-can-replace-the-vehicles-recorded-xp)

The gunner-first branches do not also fill the driver in that same alternative.
A single role write does not establish restoration of every role or an improved
attack comparison. The actor-removal requests, remaining indexed scans
and original-player callback order still need their separate qualification.

## Full health and a crew flag do not settle readiness

The M3's selected action entry accepts a positive driver-plus-gunner sum, while
Halftrack weapons require their gunner. The rocket fire button tests driver
exactly 1 or gunner exactly 1; its refill has different checks. Repairing and
recrewing therefore cannot share one universal ready-to-fire rule.
[AT option comparison](anti-tank-options.md), [Halftrack modules](halftrack-weapons.md)

An M3 can also be visibly stationary because a destination step was blocked,
while remaining outside its destination tolerance. Its selected firing-counter
branch belongs to the settled alternative. Changing health or a crew field
alone does not prove that branch was reached.
[M3 movement versus readiness](m3-at-gun.md#a-blocked-destination-is-different-from-being-ready-to-fire)

A valid still-present zero-health recipient passing a source repair threshold
is not a promise to restore a clip already removed by an earlier damage path.
Likewise, spending 1 TP on launcher ammunition does not repair health, replace
crew or clear the selected cooldown. Follow the individual state writer and
its later reader before buying a second support unit for the same symptom.

Sources: [Source identities](../player-notes/repair-crew-and-reload.md#citation-1).
Original synthesis of linked selected-source branches; no new repair-rate,
crew-transfer, reload-timing or battlefield outcome trial.

## A healthy gun can still have a counter that is not decreasing

Some waiting counters sit behind the same admission branch as the crew or
movement check. Repairing health does not by itself reach that branch.
These are named source readers at an otherwise eligible callback:

| Reader                          | Positive counter can decrement when                                 | A separate state can leave that counter unchanged here                                   |
| ------------------------------- | ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Static .50 parent               | Hull health>0 and gunner>0                                          | Missing gunner takes the operator-animation alternative                                  |
| Halftrack quad/AT/mortar turret | Positive hull gunner, hull not invincible and other entry guards    | Missing gunner or hull invincibility excludes that counter section                       |
| M3 AT controller                | Destination is within the selected tolerance and broad entry passes | An outstanding destination takes movement instead, even if an obstacle prevents the step |

For a supplied .50 with health 150/gunner 0/timer 20, its missing-gunner branch
does not decrement that timer. The selected replacement can write gunner 1
without changing timer 20; a later separately reached eligible parent visit
then decrements to 19. It is not a full recovery reset or a measured delay.
[Exact .50 branches and replacement](../player-fifty-evidence.md#the-selected-crewman-writes-one-role-and-replaces-combat-stats)

The [Halftrack continuation](../player-halftrack-continuation-evidence.md)
and [M3 destination comparison](../player-mounted-evidence.md#an-unmet-destination-can-keep-the-m3-out-of-its-timer-branch)
retain their own tests. A counter becoming zero still does not perform its
sibling expired work on that same visit. Already started action callbacks and
actual navigation/timing remain separate from these controller-admission facts.
Additional sources: [Source identities](../player-notes/repair-crew-and-reload.md#citation-2)

[Original opening and evidence context](../player-notes/repair-crew-and-reload.md#opening-before-player-language-correction).
