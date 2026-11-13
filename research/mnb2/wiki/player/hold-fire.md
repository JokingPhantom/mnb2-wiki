[Player reference](README.md) · [Orders](orders.md) · [Shooting stages](how-shooting-works.md)

# Hold Fire

The selected order **replaces a qualifying recipient's action counter with 400**
and requests a stopped frame. It is a pending command followed by an actor-
specific receipt, not a permanently retained ceasefire flag or proof every
already-fired rocket disappears. [Exact source](../hold-fire.md)

Historical scope: selected **2.3.1g** source.

| Key fact         | Selected historical behavior                                             |
| ---------------- | ------------------------------------------------------------------------ |
| Offer cost       | No direct TP debit in the inspected offer                                |
| Offer access     | Qualifying Officer, or rank-at-least-3 soldier; exact alternatives below |
| Recipient effect | Actor-specific stopped-frame/counter writes, including 400               |
| Important limit  | Other writers and projectiles remain; no universal duration in seconds   |

On this page: [Using the order without assuming it recalls attacks](#using-the-order-without-assuming-it-recalls-attacks) · [A command actor enables the offer](#a-command-actor-enables-the-offer) · [Replacing a counter is different from adding a duration](#replacing-a-counter-is-different-from-adding-a-duration) · [Stopped actor and existing projectile are different objects](#stopped-actor-and-existing-projectile-are-different-objects) · [Officer aid has another counter writer](#officer-aid-has-another-counter-writer) · [The ordinary soldier has a different receipt and counter consumer](#the-ordinary-soldier-has-a-different-receipt-and-counter-consumer)

## Using the order without assuming it recalls attacks

1. Check that the offer has a qualifying Officer or sufficiently ranked soldier.
2. Select the order, then apply it to the intended eligible friendly recipient.
3. Check the recipient's action state. Earlier pending equipment or training
   choices can take precedence over that receipt. [Offer and recipient evidence](../hold-fire.md),
   [pending-choice behavior](training-and-equipment.md#several-pending-choices-do-not-form-a-queue).

Expect a change to that actor's action state, **not a permanent squad-wide
ceasefire**. Existing projectiles have their own callbacks, different actors
consume the counter differently, and another effect such as Officer aid can
replace it. The source value 400 is not a qualified universal duration in seconds.
The comparisons below explain those limits for selected historical **2.3.1g**.
[Actor-specific counter evidence](../player-ordinary-hold-fire-evidence.md),
[Bazooka receipt and later readers](../hold-fire.md).

## A command actor enables the offer

The selected menu scan accepts specialization 2 with health above 10 and
invincible not 1, **or rank at least 3 with health above 10**. The invincibility
condition belongs to the first alternative; do not silently apply it to both.
A successful scan sets the pending Hold Fire cue and pointer. The inspected
offer has no direct TP debit; full input/menu reachability remains separate.

The selected Bazooka receipt needs health above 9 and the pending cue after
earlier grenade, bayonet and training branches. Its unpinned alternative writes
400, requests stopped frame 1, clears the cue and resets the pointer. The pinned
alternative also clears the cue but does not perform that 400 write.

## Replacing a counter is different from adding a duration

| Supplied old counter, qualifying unpinned receipt | Counter at its assignment |
| ------------------------------------------------- | ------------------------- |
| 3                                                 | 400                       |
| 400                                               | 400                       |
| 500                                               | 400                       |

The last example can reduce an arbitrary old counter rather than extend it.
These are source-write examples, not tested repeated commands or measured
seconds. Historical five-second wording needs actual scheduling evidence.

For the separate Bazooka controller, each reached positive-counter branch
subtracts 1 under its live, unpaused, positive-morale, nonwithdrawing and
noninvincible guards. Pinning gates its expired action work, but is not repeated
on that positive-counter decrement. Starting 400 with no other writes takes 400
such qualifying decrements to reach 0. The visit that changes 1 to 0 does not also
enter the expired branch. Targeting and actual launch remain later questions.
[Exact receiver and admitted-visit arithmetic](../hold-fire.md#bazooka-receipt-and-the-later-positive-counter-consumer)

## Stopped actor and existing projectile are different objects

The reached Bazooka frame 1 body separately clears aiming. Its execution order
relative to the original click remains unqualified here. An existing rocket
still has its own movement/scan/blast callbacks; these selected receipt writes
do not remove it. Hold Fire is therefore not evidence of a guaranteed safe
explosive firing lane or a complete cancellation of support/projectiles.
[Bazooka stages](bazooka.md), [retargeting orders](retargeting-orders.md)

Other actor receipts and counter consumers need their own bindings. This guide
does not turn the selected Bazooka example into one universal hold duration
or a tested rule for every vehicle, support unit and already-started attack.

Sources: [Source identities](../player-notes/hold-fire.md#citation-1). Selected publisher-associated 2.3.1g;
source explanation and supplied states, without new input/timing trials.

## Officer aid has another counter writer

The selected reached Officer aid frame can replace a healthy unpinned
recipient's current counter with 1–50. For supplied old 400, that is replacement
with a smaller value at that write. Its pinned alternative clears pinning and
requests frame 1 instead, without also performing that same counter assignment.
An already held counter is therefore not a permanent state against all later
writers. This is a conditional source comparison, not a measured cancellation
or firing time. [Exact aid interaction](../hold-fire.md#officer-aid-can-replace-an-already-held-counter)
Additional source: [Source identities](../player-notes/hold-fire.md#citation-2)

## The ordinary soldier has a different receipt and counter consumer

The selected ordinary recipient handler has an **earlier Hold Fire branch**
that writes 400 before a later identical condition containing the pin check.
For supplied health 100, pending Hold Fire and no earlier competing cue, even
pinned 1 reaches that earlier write. This differs from the Bazooka receipt above;
it is a source-branch comparison, not an observed pinned-command trial.
[Exact order and conditions](../player-ordinary-hold-fire-evidence.md#an-earlier-identical-condition-precedes-the-pinned-check-branch)

If that ordinary soldier later reaches its active positive-counter section
with 400 unchanged, it writes 399 and then caps the result to 100. The selected
Bazooka section instead writes 399 at its simple decrement. Pinning belongs to
their separate expired-search checks, rather than automatically stopping these
positive-counter writes.

These are actor-specific source-counter examples. They do not establish which
callback runs immediately after a click, either hold's seconds, or immediate
firing when the counter expires. Keep later action guards and other writers
attached to any timing claim.
[Reader comparison](../player-ordinary-hold-fire-evidence.md#a-later-ordinary-counter-section-has-an-extra-cap)
Additional sources: [Source identities](../player-notes/hold-fire.md#citation-3)
