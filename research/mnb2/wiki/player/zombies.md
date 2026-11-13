[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Zombies and the Halloween Ribbon

Zombies are durable enemy infantry with **400 starting health and armor code 0**. That is
high infantry health, not vehicle armor or immunity to ordinary damage. The
inspected generator includes a calendar-gated zombie branch, but its source
conditions do not certify what every host date or initialized game will do.
[Exact actor and calendar branch](../player-zombie-evidence.md)

Historical scope: selected **2.3.1g**.

| Load field      | Selected default                                                |
| --------------- | --------------------------------------------------------------- |
| Starting health | 400                                                             |
| Armor code      | 0                                                               |
| Rifle field     | Random 0 through local wave minus 1, divided by 2               |
| Experience      | 1–20                                                            |
| Morale          | 999; replaced by 2 when Assault Expert Award's flag is positive |

The own controller's ready action handles a timer and possible scream, rather
than the ordinary infantry target-and-fire search. Its loaded rifle field is
not proof of a rifle attack. Forward movement uses a random +0.5 increment with
wire and active-state conditions, without a local pin/aiming/melee guard in that
movement block. No movement speed in seconds is certified.
[Exact controller](../player-zombie-evidence.md#load-and-forward-movement)

On this page: [The calendar branch is conditional, not a complete wave recipe](#the-calendar-branch-is-conditional-not-a-complete-wave-recipe) · [The Ribbon checks a counter, not independently counted deaths](#the-ribbon-checks-a-counter-not-independently-counted-deaths) · [Lower morale does not add a pin check to this movement block](#lower-morale-does-not-add-a-pin-check-to-this-movement-block)

## The calendar branch is conditional, not a complete wave recipe

The inspected path tests a particular random value and stored month/day values,
then requests 2–6 zombie duplications. It precedes the ordinary budget assignment;
it does not by itself replace the rest of the wave. Host calendar, callback
ordering, initialization and actual arrivals still need qualification.
[Wave generation](waves.md), [calendar and budget evidence](../player-zombie-evidence.md#calendar-branch-and-ordinary-budget-are-separate)

## The Ribbon checks a counter, not independently counted deaths

The selected Halloween Ribbon condition is **zombie-kill counter above 20**,
with the award not already set and earlier medal-display/ordering guards met.
Counter 20 fails this comparison; 21 passes it under those conditions.

The zombie death frame, the enemy-death helper and the gib helper have separate
counter-increment sites. Their full interaction has not been qualified here,
so “21 distinct zombies killed always awards immediately” is a stronger claim
than these source facts support. This is also not a reproduced double-count
report. [Exact writers and award threshold](../player-zombie-evidence.md#different-sites-write-the-persistent-zombie-counter)

Related: [enemy stats](enemy-stats.md), [progression](progression.md),
[enemy roles](enemy-guide.md).

Sources: [Source identities](../player-notes/zombies.md#citation-1)

## Lower morale does not add a pin check to this movement block

At the selected shared-firearm **miss** pin comparison, a valid living target
with current morale 999 admits no integer 0–99 draw; morale 2 admits 97 draws.
That is one conditional pin-field/navigation site, not a chance per fired shot
or proof the Zombie stops moving after an admitted pin request.

Its separately reached forward movement block has no local pin or morale check.
With declared valid nonstock health 400, y 300, pause 0, no wire delay and movement
draw 0, that source step writes y 300.5 with either pinned 0 or pinned 1. Actual
navigation and callback order after a hit remain unqualified. The Assault Expert
load replacement changes one pinning input without installing a movement guard.
[Exact load, pin comparison and separately supplied movement inputs](../player-enemy-morale-loads-evidence.md#the-zombies-pin-field-and-its-forward-movement-are-different-readers).
Additional source: [Source identities](../player-notes/zombies.md#citation-2)
