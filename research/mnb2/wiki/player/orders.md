[Player reference](README.md) · [Orders](orders.md) · [Shooting stages](how-shooting-works.md)

# Orders: selecting a command is not the whole action

Orders have **offer eligibility, pending selection, recipient/target handling
and later actor behavior**. These stages differ by command. An Officer check
from one offer must not be copied onto every command, and a target-field write
does not prove every recipient immediately fires.
[Order evidence](../player-interaction-evidence.md#orders)

Historical scope: selected **2.3.1g** source.

Find your question: [which command to choose](#choose-by-the-action-you-want),
[whether a veteran or Sarge can enable it](#can-a-veteran-or-sarge-replace-an-officer-for-commands),
[how target choices differ](#concentrate-fire-and-all-around-defense-choose-differently), or
[what Hold Fire and Morale Boost change](#hold-fire-and-morale-boost-change-specific-fields).

## Choose by the action you want

| Order                                                | Purpose and recipient distinction                                                                                | Selected cost or condition                                                      |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [Hold Fire](hold-fire.md)                            | Apply to an eligible ally to change its action state; it is not a permanent ceasefire or projectile recall       | Qualifying command actor; no direct TP debit in the inspected offer             |
| [Concentrate Fire](retargeting-orders.md)            | Choose an enemy for the selected target-assignment helper; assignment does not guarantee every soldier fires     | Eligible Officer and cooldown gate; no direct TP debit in that offer            |
| [All Around Defense](retargeting-orders.md)          | Rebuild a target pool for each qualifying recipient and draw from it; several soldiers can choose the same enemy | Advertised 1 TP, charged before target-pool processing                          |
| [Combat Leadership](combat-leadership.md)            | The selected friendly receipt adds 1 XP and checks promotion, rather than granting a guaranteed rank             | Advertised 1 TP or admitted free flag                                           |
| [Morale Boost](morale-boost.md)                      | Apply the pending morale bonus through its eligible recipient path; it is not a universal reset to full morale   | Advertised 1 TP; amount comes from the largest realized qualifying Officer roll |
| [Tactical withdrawal](withdrawal-and-mission-end.md) | Order a unit through its guarded movement/exit path; this differs from ending the whole mission                  | Officer-enabled pending order; not instant removal                              |

These are **selected historical 2.3.1g** source distinctions. Follow the linked
order's gates and recipient steps; an earlier pending purchase can take a click
before the action you intended. [Order and input evidence](../player-interaction-evidence.md#orders),
[pending-choice priority](training-and-equipment.md#several-pending-choices-do-not-form-a-queue).

“No direct debit” describes the inspected offer, not a universal transaction
certification across every input path. [Training/equipment](training-and-equipment.md),
[withdrawal and mission end](withdrawal-and-mission-end.md)

## Can a veteran or Sarge replace an Officer for commands?

**For the inspected Hold Fire offer, a soldier with rank at least 3 can meet
the command-actor requirement. That is not permission to use every Officer
order.** These selected historical **2.3.1g** offers have different checks:

- **[Hold Fire](hold-fire.md#a-command-actor-enables-the-offer).** Officer specialization with health above 10 and invincible not 1, **or soldier rank at least 3 with health above 10**
- **[Concentrate Fire and All Around Defense](retargeting-orders.md#choose-the-target-selection-behavior).** Officer specialization, health above 10 and invincible not 1; their cooldown/payment conditions also differ
- **[Morale Boost](morale-boost.md#the-highest-xp-officer-does-not-automatically-supply-the-bonus).** Eligible Officer scan; a veteran's rank alone does not supply that Officer's bonus roll
- **[Tactical withdrawal](../tactical-withdrawal.md#the-offer-enables-a-pending-recipient-action).** Officer specialization, health above 10 and invincible not 1
- **[Combat Leadership](combat-leadership.md#purchase-and-application-are-separate).** This release script checks its TP/free-allowance path without an explicit Officer scan; complete menu visibility and input reachability remain unqualified

Sarge's ordinary starting **rank 3 and health 125** meet the rank/health part of
Hold Fire's alternative. His support abilities and rank do not turn him into an
Officer for the other specialization checks. Likewise, **30 XP with rank 0**
does not pass a rank-at-least-3 test merely because the XP number is larger.
The player's career rank is a third, separate value.
[Sarge's load](sarge.md), [XP and rank](progression.md),
[exact Hold Fire alternatives](../hold-fire.md)

These comparisons concern the actor that **enables the offer**, not the soldier
that later receives the order. Health exactly 10 fails the cited above-10
command-actor tests even though some recipient tests accept it. Hold Fire's
invincibility condition belongs to its Officer alternative; it is not repeated
in its rank alternative. None of these offer checks alone proves an order was
applied, a unit moved, or an attack stopped.
[Recipient and input distinctions](../player-interaction-evidence.md#orders),
[health-10 comparison](wounded-and-rescued.md#ten-health-does-not-mean-every-job-is-ready)

## Concentrate Fire and All Around Defense choose differently

[Concentrate Fire and All Around Defense](retargeting-orders.md) separate broad
target assignments from narrower animation requests.

Concentrate Fire takes a chosen target through its target handler. Its offer
admits cooldown at most 1, rather than only 0. The helper's selected positive-
target-health path writes a cooldown 60, or 30 under its medal condition; those
counter values are not measured seconds or proof anyone shot.
[Chosen-target trace](../concentrate-fire.md)

The relevant award is **Infantry Specialist Ribbon** (medal 29): its stored
flag must equal 1 for the selected 60-to-30 override. Its career award test is
separate from this command consumer, and neither counter write confirms a shot.
[Award label and test](../award-reference.md),
[Named order benefit](retargeting-orders.md)

All Around Defense instead rebuilds a visible/LOS-eligible target pool for each
qualifying recipient and draws from that array. Different soldiers can pick the
same enemy. The debit precedes the helper; no shot-confirmation payment stage
is shown in those sites. Empty pools, recipient states and actual firing still
matter. [Per-recipient pools](../all-around-defense.md)

## Hold Fire and Morale Boost change specific fields

The inspected unpinned Hold Fire receipt replaces the action timer with 400; it
does not add 400. Pinned recipients and different families have their own paths.
A timer alone does not cancel every already-fired projectile or prove the old
guide's five-second duration. [Hold Fire](hold-fire.md)

Morale Boost compares realized Officer rolls and keeps the largest, rather than
simply choosing the highest-XP Officer. The selected regular/recon receipt adds
the pending amount before a strict **post-addition morale above 0** test for
clearing flee. Exactly 0 fails that recovery comparison. [Boost details](morale-boost.md)

Sources: [Source identities](../player-notes/orders.md#citation-1).
[Exact version and bindings](../player-interaction-evidence.md)

Additional source: [Source identities](../player-notes/orders.md#citation-2)
