[Player reference](README.md) · [Vehicles and emplacements](vehicles-and-emplacements.md) ·
[Repair, crew or reload?](repair-crew-and-reload.md)

# Static .50-caliber gun

A **6-TP placed gun with 200 starting health and a 100-round ammo pool** in the
selected 2.3.1g source. It needs its gunner to operate. Its controller, burst
animation and refill differ from the infantry Machine gunner and the M3 AT gun.
[Exact source and version](../player-fifty-evidence.md)

Applies to **historical selected 2.3.1g**. Starting health, crew and counters
are source load fields; they do not guarantee arrival or a complete attack.

| Key fact                     | Selected historical load                                                  |
| ---------------------------- | ------------------------------------------------------------------------- |
| TP cost and availability     | 6 TP; placement/completion, no Engineer requirement in the inspected path |
| Health / maxhealth           | 200 / 200                                                                 |
| Armor class                  | 1                                                                         |
| Gunner / driver / spare crew | 1 / 0 / 0                                                                 |
| Ammo                         | 100                                                                       |
| Experience / rank            | 0 / 0; Mud and Blood Cross adds 9 XP at its load branch                   |
| Initial action counter       | 20 source units                                                           |
| Morale                       | 0–99 before later changes                                                 |

[Starting-field evidence](../player-fifty-evidence.md).

On this page: [Placement, repair and a missing gunner are different questions](#placement-repair-and-a-missing-gunner-are-different-questions), [Placing it is separate from selecting the offer](#placing-it-is-separate-from-selecting-the-offer), [The gunner and protection classification matter](#the-gunner-and-protection-classification-matter), [Damage draws and accuracy](#damage-draws-and-accuracy).

## Placement, repair and a missing gunner are different questions

The inspected **6-TP offer/completion has no Engineer requirement**: it is a
placement path with its own later affordability and capacity conditions. A
pointer alone is not proof a gun arrived. [Placement evidence](../player-fifty-evidence.md#offer-placement-and-starting-fields).

If a living gun loses its gunner, its selected controller stops acquiring targets
and does not decrement the action counter in that branch. That is different from
a wreck caused by nonpositive hull health. Repairing the hull and supplying a
[Crewman](crewman.md) address different state; an idle gun need not simply be out
of ammunition. [Missing gunner versus wreck](../player-fifty-evidence.md#a-missing-gunner-is-different-from-a-destroyed-gun).

Selected historical **2.3.1g** source conditions; no new placement, recrewing or
reload-timing trial. The exact load and attack cycle follow.

Rifle uses a random stopping loop with additions of 1–10, then Combat Ribbon's
+3. Do not copy the infantry defaults or career bonuses onto every emplacement.

## Placing it is separate from selecting the offer

The menu sets a placement cue; the later completion retests affordability before
subtracting 6 TP and calling the spawn helper. The inspected offer/completion has
no Engineer requirement. Its player-cap checks are separate, so a pending pointer
is not proof a gun was created. [Placement bindings](../player-fifty-evidence.md#offer-placement-and-starting-fields)

A nonstock load clamps the position it sees to x=60..350 and y=60..560. That is a
source load operation, not a certified final placement rectangle: the order of
caller coordinate writes and load still needs qualification.

## The gunner and protection classification matter

The living, unpaused gun needs gunner>0 for its selected acquisition work. When
its counter expires, palisade classification and a random admission check precede
a nearest-eligible-target scan. Visibility, invincibility, armor/crew, line of
sight and other target state still matter. This is not the M3's armor-first index
rule. [M3 AT gun](m3-at-gun.md), [crew replacement](crewman.md)

The initial burst counter is **4–13**. That is a counter, not a certified
shots-per-burst range: later callbacks test ammo, decrement burst and request
another firing frame. [Acquisition and cycle evidence](../player-fifty-evidence.md#acquisition-bursts-and-refill-are-different-stages)

## Damage draws and accuracy

Its selected firearm path can subtract **0–199 health** from a living unarmored
target, including zero. Armor and crew paths differ; the number 200 is not an
unconditional hit amount.
[Vehicle/crew effects](anti-tank-and-vehicles.md)

The helper also adds twice a positive burst counter to its accuracy roll before
the inclusive rifle comparison. For a supplied rifle 20/burst 4 state, 13 of 100
integer rolls pass that stage; with burst 0, 21 pass. These are explicit source-stage
examples, not complete hit chances or measured firing performance.
[Shared helper and inputs](../player-fifty-evidence.md#shared-weapon-13-and-conditional-accuracy-stage)

## Refill has its own recovery counter

The inspected recovery frame refills empty ammo to 100 and sets 400 − XP source units.
With ammo remaining it instead sets 150 − XP. Acquisition can also write random 0–199
to an expired counter. These separate writes and animation/pause paths prevent
one timer from being an elapsed-time reload or firing-rate statistic.

Sources: [Source identities](../player-notes/fifty-caliber.md#citation-1). [Exact evidence](../player-fifty-evidence.md)

The [Sherman optional .50](sherman.md) uses a different direct firearm body,
including the opposite sign for its positive-burst roll modifier. A shared
weapon name does not make these formulas interchangeable.

## An empty crew position is different from a wreck

A living gun with no positive gunner takes a separate controller branch: it
changes the operator animation but does not acquire a target or decrement the
action counter there. Nonpositive **hull health** instead creates a wreck and
removes the gun at that controller path. A missing operator alone does not
produce that wreck.
[Exact parent branches](../player-fifty-evidence.md#a-missing-gunner-is-different-from-a-destroyed-gun)

The selected Crewman replacement requires gunner exactly 0 and writes it to 1.
It copies the recruit's rifle, XP and rank **over** the gun's values; it does
not repair health, refill ammo or reset the action counter in that branch.
For a supplied surviving health 150/ammo 12/timer 20/XP 80 gun and eligible XP 0
Crewman, those first three fields stay unchanged at the replacement sites while
XP becomes 0. Read the role/state that needs restoring before buying support.
[Replacement and input scope](../player-fifty-evidence.md#the-selected-crewman-writes-one-role-and-replaces-combat-stats)

Blocking controller acquisition is not a proven immediate stop for every
started animation: the local firing/repeat/refill actions do not all repeat
that gunner guard. Actual post-loss shots and timing remain unqualified.
[Callback limits](../player-fifty-evidence.md#controller-admission-does-not-prove-every-started-action-stops-immediately)
Additional source: [Source identities](../player-notes/fifty-caliber.md#citation-2)

The selected static .50 loads driver 0/gunner 1, but its short release handler
requires driver 1 before assigning new waypoint focus. Its inspected active
parent has firing/target work rather than a normal waypoint position step.
A restored gunner and a movable hull are different questions.
[Exact selection and stationary-gun readers](../player-vehicle-movement-evidence.md#a-stationary-guns-driver-field-is-not-its-firing-crew).
Additional source: [Source identities](../player-notes/fifty-caliber.md#citation-3)
