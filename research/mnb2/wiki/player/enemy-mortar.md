[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy mortar soldier

The enemy mortar soldier attacks targets **strictly farther than 300 source-distance units** when choosing a target. Firing later places
an explosion effect around the target's then-current coordinates with independent
horizontal and vertical offsets. Selection distance, impact placement and blast
damage are different tests.
[Exact source stages](../player-enemy-heavy-evidence.md#mortar-load-setup-and-minimum-selection-distance)

Historical scope: selected **2.3.1g**.

| Load field      | Selected default                                   |
| --------------- | -------------------------------------------------- |
| Starting health | 100                                                |
| Armor code      | 0                                                  |
| Rifle skill     | Local wave plus random 0–19                        |
| Experience      | 1–50                                               |
| Setup counter   | 0–399; source units, not seconds                   |
| Action timer    | 0–199; source units, not seconds                   |
| Morale          | 0–99; Assault Expert Award separately subtracts 10 |

On this page: [Selecting beyond 300 is not a continuous safety boundary](#selecting-beyond-300-is-not-a-continuous-safety-boundary) · [Spread uses fixed offsets rather than the loaded rifle value](#spread-uses-fixed-offsets-rather-than-the-loaded-rifle-value) · [Pinning, setup and movement have different gates](#pinning-setup-and-movement-have-different-gates) · [Loaded stats are not automatically the last writers](#loaded-stats-are-not-automatically-the-last-writers)

## Selecting beyond 300 is not a continuous safety boundary

The search also checks living health, visibility, invincibility, compatible
melee state, line of sight and a closer eligible distance. Exactly 300 fails
the distance test. This selected scan has no armor or pillbox filter.
The firing-action body does not repeat the >300 condition, so it does not by
itself prove a reached shot is canceled when a target moves closer.
[Selection and later-reader limits](../player-enemy-heavy-evidence.md)

## Spread uses fixed offsets rather than the loaded rifle value

Each firing-action axis adds a random integer **−150 through 149** to the target
coordinate read at that later action. These are independent axis offsets, not
a circular radius, and the placement expressions do not read rifle or experience.
A higher wave-dependent rifle load therefore does not by itself tighten them.

The action creates the mortar effect at those coordinates. That site does not
create a separate traveling shell. The later effect calls the explosion helper
with its own protection and recipient rules; its damage input of 50 does not
guarantee 50 health lost or exclude friendly fire.
[Exact placement and effect](../player-enemy-heavy-evidence.md#mortar-emission-uses-later-target-coordinates-and-fixed-axis-offsets)

## Pinning, setup and movement have different gates

Pinning does not freeze the inspected setup countdown. Even with movement
blocked, a positive setup counter decreases; counting down from one writes −99
and requests the setup frame. That branch does not also search or decrease the
action timer through its alternative in the same source chain.

With setup already zero or negative, an action timer of one decreases to zero
even while pinned. A timer already zero instead reaches the ready branch, where
pinning blocks search and leaves that timer unchanged. Without pinning, a
separately supplied passing search draw admits the scan and its later timer
reset, including when no eligible target is found.

This explains why preventing movement, preventing search and stopping setup are
different claims. It does not establish a first-shot delay, stun duration or
actual sequence of callbacks. Starting at zero does not request the same setup
transition as counting down from one.
[Combined setup/timer/pin inputs](../player-enemy-heavy-evidence.md#mortar-setup-timer-and-pin-gates-in-the-same-source-branch)

The [allied Mortar](mortar.md) and [Mortar pit](mortar-pit.md) are separate actors
and construction. Their names do not make all selection or firing rules identical.

Sources: [Source identities](../player-notes/enemy-mortar.md#citation-1)

## Loaded stats are not automatically the last writers

The mortar explicitly copies itself into its emitted effect's owner field.
A later admitted blast branch for **another enemy recipient** can add XP to
that valid surviving owner and call the generic promotion helper. That helper's
ordinary ladder has no Allied-only gate and can add rifle/morale to this mortar.

With declared load wave 20, rifle draw 0, XP 9 and rank 0, one qualifying source
receipt takes XP to 10 and rank to 1. A supplied promotion rifle draw 9 writes
rifle 29. This is a conditional writer example, not an observed enemy promotion
or a claim every shell grants XP. It also does not tighten the fixed impact
offsets above, which do not read rifle.
[Exact enemy owner, recipient branch and promotion inputs](../player-enemy-mortar-credit-evidence.md)
Additional sources: [Source identities](../player-notes/enemy-mortar.md#citation-2)

A shared positive-health label is not a common readiness threshold for every
enemy. At separately supplied health 1 and the other stated gates, this Mortar's
controller can still decrease its ready timer while the rocket soldier's extra
health gate skips that chain. This is a field-reader comparison, not a live
wounded-enemy or first-shot result.
[Health and pause guard differences](../player-enemy-heavy-evidence.md#rocket-and-mortar-controller-health-and-pause-gates-are-not-interchangeable)
