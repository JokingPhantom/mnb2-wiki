[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Wespe artillery vehicle

The Wespe is an artillery vehicle with **1000 starting health and armor code 2**. It **adds to shared German artillery state**, rather than
selecting one local player and directly placing a cannon blast around it.
[Exact firing and shared counter](../player-flak-wespe-evidence.md#wespe-requests-shared-artillery-rather-than-selecting-a-local-victim)

Historical scope: selected **2.3.1g**.

| Key fact              | Historical default or behavior                                                  |
| --------------------- | ------------------------------------------------------------------------------- |
| Starting hull health  | 1000                                                                            |
| Armor code            | 2                                                                               |
| Initial setup counter | 0–399 source units, not seconds                                                 |
| Attack                | Adds 1 to shared strike counter; later artillery consumer requests impacts      |
| Important limit       | A visible shell is not one certified hit; two source placements remain distinct |

On this page: [Setup and firing use different guards](#setup-and-firing-use-different-guards) · [A strike counter, shell representation and impact are separate](#a-strike-counter-shell-representation-and-impact-are-separate) · [Two retained placements stay distinct](#two-retained-placements-stay-distinct) · [A missing driver is not this hull's movement guard](#a-missing-driver-is-not-this-hulls-movement-guard)

## Setup and firing use different guards

The hull's setup counter starts at 0–399. While positive in the active movement
branch, it advances y by 0.3 and decreases the counter. The selected turret
controller does not repeat that setup-counter test before requesting fire.
A setup counter alone therefore does not prove a fixed delay or an absolute
only-when-stationary firing rule.

The ready turret instead checks a positive gunner, unpaused state, its own
expired timer, a 50-of-100 comparison and shared artillery delay **exactly zero**.
Its timer can reset even when those later tests do not request an attack.
[Exact counters and conditions](../player-flak-wespe-evidence.md#wespe-requests-shared-artillery-rather-than-selecting-a-local-victim)

## A strike counter, shell representation and impact are separate

A reached firing action increments the shared strike counter by 1. A later
action creates a shell representation at the vehicle's position; the inspected
shell callback handles movement and fading rather than calling a blast there.
The selected downstream consumer requests one big-explosion effect at a time
from positive strike state after its delay/random guards. It samples the squad's
current vertical-half test for each successful request; it does not target one
named local victim. Delay becoming zero does not emit in the same else-if branch.
[Shared consumer and exact inputs](../player-german-artillery-evidence.md).
It is not one certified healthy-target hit per visible shell.

The selected hull-death body does not clear that strike counter. That local
absence is not a complete guarantee about canceling every pending artillery
event. [Shared-state boundaries](../player-flak-wespe-evidence.md)

## Two retained placements stay distinct

The catalog retains two Wespe world placements. Their selected load and parent
callback bytes match, but their physical tag identities remain separate; this
does not prove every same-name caller resolves the same initialized instance.
[Exact placement identities](../player-flak-wespe-evidence.md#wespe-keeps-two-physical-placements-even-where-source-bodies-match)

Related: [enemy vehicles](enemy-vehicles.md), [support](support.md).

## A missing driver is not this hull's movement guard

The selected active hull movement does not require driver or gunner. Flakpanzer
uses its moving counter; Wespe uses its setup counter. The turret has a separate
gunner check. A supplied zero driver field therefore does not by itself prove
immobilization in these bodies, or certify a practical way to create that state.

At the selected health comparison, zero goes to hull death. Exit past y600 has
an earlier separate miss/removal request without a crew/health test. Complete
removal order and all helper accounting still matter.
[Exact movement, wreck and exit guards](../player-flak-wespe-evidence.md#hull-movement-and-destruction-do-not-use-one-generic-crew-rule)

Sources: [Source identities](../player-notes/wespe.md#citation-1)
