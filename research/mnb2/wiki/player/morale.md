[Player reference](README.md) · [Recruitment](recruitment.md) · [Reading stats](reading-stats.md)

# Morale, pinning and retreat

When a soldier stops acting, check its state before assuming morale alone
explains it. Pinning, fleeing and returning to useful action are different steps.
Historical scope: selected **2.3.1g** source.

- **Pinned soldier.** Recovery has actor-specific checks; no fixed recovery duration is established here.
- **Pinning clears.** The recovery path can still leave the soldier fleeing and replace its action counter. Clearing pinning is not an immediate firing guarantee.
- **Morale is exactly zero.** Different retreat/recovery predicates treat zero differently. Do not round it into a universal safe or failed state.
- **Elite recruit or high morale.** Neither supplies a verified universal immunity to pinning or retreat.

Use the [nonfiring checklist](why-soldiers-stop-shooting.md) for orders, targets,
weapon state and other causes. These distinctions follow the selected 2.3.1g
[recovery evidence](../player-pin-recovery-evidence.md) and
[morale branches](../player-morale-branch-evidence.md).

Morale affects several **different source checks**, rather than one global
bravery percentage. Pinning, retreat, close combat, death penalties and recovery
have their own conditions. A morale value alone does not predict the exact
frame a soldier must flee or resume firing.
[Morale and pinning evidence](../player-campaign-evidence.md#morale-and-pinning)

On this page: [Compare morale recovery with unpinning](#compare-morale-recovery-with-unpinning) · [A miss can still matter](#a-miss-can-still-matter) · [Zero morale is a real boundary difference](#zero-morale-is-a-real-boundary-difference) · [Sarge penalties depend on which helper runs](#sarge-penalties-depend-on-which-helper-runs) · [Losing and promoting soldiers changes morale differently](#losing-and-promoting-soldiers-changes-morale-differently) · [Clearing pinning can still leave the ordinary soldier fleeing](#clearing-pinning-can-still-leave-the-ordinary-soldier-fleeing) · [Fire conversion can reach two separate Sarge morale penalties](#fire-conversion-can-reach-two-separate-sarge-morale-penalties) · [An accurate zero-damage hit is not the same as a suppressing miss](#an-accurate-zero-damage-hit-is-not-the-same-as-a-suppressing-miss) · [A missed enemy shot uses another pin request](#a-missed-enemy-shot-uses-another-pin-request) · [A reaction request is not always a direct pin-field write](#a-reaction-request-is-not-always-a-direct-pin-field-write)

## Compare morale recovery with unpinning

**Morale Boost and Sarge's unpin effect change different fields.** For these
selected **2.3.1g** branches, assume the relevant actor/recipient, pending choice,
timer and other admission conditions have already passed:

- **Morale Boost on its selected Regular/Scout receipt.** Adds the pending bonus, then clears flee and requests the ready frame only if resulting morale is above 0. Those recovery statements do not assign pinned or withdraw; exactly 0 fails the positive-morale test.
- **Sarge's selected unpin recipient branch.** Requests the ready/effect frames and sets pinned to 0 for its qualifying target. It does not locally assign recipient morale, flee, actionTimer or withdraw.

Thus paying for a morale boost does not certify unpinning. Likewise, a Sarge
rally can clear pinning while a supplied recipient's morale 0, flee 1 and counter
400 remain at those statements. Neither is a promise of an immediate shot or
a complete reset of retreat and readiness.
[Morale Boost receipt](../morale-boost.md#a-selected-regularrecon-receipt-adds-before-checking-recovery),
[Sarge recipient guards and retained fields](../player-sarge-support-evidence.md#sarge-rally-is-not-a-morale-boost-or-ordinary-pin-recovery)

Actual ready-frame execution and later writers are separate stages. Other
families and Sarge's **own** recovery have different conditions; do not turn
these two recipient examples into one universal panic-recovery rule.
[Morale Boost](morale-boost.md), [Sarge](sarge.md),
[nonfiring checks](why-soldiers-stop-shooting.md)
Additional sources: [Source identities](../player-notes/morale.md#citation-1)

## A miss can still matter

In the inspected shared allied firing path and direct Gunner path, a failed
accuracy comparison can reach a separate random 0–99 roll **greater than the
target's morale**, with its own living-target guard, to set pinning and request
a pinned animation. That does not mean every miss pins, or that a projectile
must pass through a measured suppression circle. [Gunner](machine-gunner.md),
[pinning research](../pinning.md)

One Regular enemy's movement and action-selection paths are blocked by pinning,
but that is not proof every actor, already-started attack or motion source stops
immediately. Its recovery path has another morale-dependent random check, so
pinning duration is not established by one flag or animation label.

## Zero morale is a real boundary difference

The selected fear helper's retreat test is **below 0**, plus an unpinned recipient with health above 9. A rank-qualified death-penalty path tests **below 1** after
its loss. A soldier at exactly 0 does not satisfy the same comparison in both
paths. Other actor/armor conditions remain part of those compound tests.
[Different retreat predicates](../morale.md)

The community describes Spec Ops, paratroopers and Sarge as unwilling to retreat.
The selected fear and rank-loss guards use OR between “not Spec Ops” and “not
paratrooper.” For either stable named type, one inequality remains true, so
those guards do not supply the claimed type exclusion. The remaining distance,
rank, health, pinning and actor/caller conditions still decide what happens;
a lack of exclusion at one guard is not a universal retreat rule.
[Exact type comparison](../player-morale-branch-evidence.md#the-or-guard-is-not-a-spec-ops-or-paratrooper-exclusion) “High morale” is also not a certified immunity to
every pinning or retreat mechanism.

## Sarge penalties depend on which helper runs

When fear is called with Sarge, its first half-morale loop exhausts the shared
index; the following ordinary nearby-loss loop does not reset it. The separate
playerDeath helper does reset its index and can apply its rank-loss loop after
the Sarge half-loss. With supplied dead rank 3 and a lower-ranked unarmored
recipient at morale 20, the latter source path gives 20 → 10 → 6. This is a
conditional source calculation, not proof that both helpers run at every death.
[Loop and penalty order](../player-morale-branch-evidence.md#playerdeath-resets-the-index-before-its-rank-loss-loop)

## Losing and promoting soldiers changes morale differently

A selected rank-related death penalty subtracts the dead actor's rank plus 1 from
qualifying lower-ranked recipients. Sarge has a separate subtraction based on
rounded half of the recipient's current morale. Promotion bonuses can draw 0;
these are not all flat, guaranteed changes of the same size.
[Officer](officer.md), [progression](progression.md), [source penalties](../morale.md)

Starting morale also varies by recruit and career awards. A Regular Soldier's
base 20–29 is different from Spec Ops 30–59 or the Officer's 10–99; even a role with
a higher-looking card can roll below another role on a particular source draw.
[Recruitment](recruitment.md)

Sources: [Source identities](../player-notes/morale.md#citation-2). Selected 2.3.1g; [exact evidence](../player-campaign-evidence.md).

## Clearing pinning can still leave the ordinary soldier fleeing

The ordinary soldier's reached recovery action compares a random 0–99 draw with
**morale plus 10 times its existing flee field**. Strictly greater stays pinned;
equality takes the clearing alternative. With supplied morale 20, flee 0 accepts
21 of 100 inputs for clearing, while flee 1 accepts 31. Those are conditional
per-visit counts, not a recovery duration or a universal immunity.

After clearing pinning, that action separately checks **morale above 0**. At
supplied morale 0/flee 0/draw 0, it clears pinned but sets flee 1 and requests the
flee state. At morale 20/flee 1/draw 30, it clears pinning and then flee. Unpinned
therefore is not automatically ready to fight.
[Exact alternatives and input table](../player-pin-recovery-evidence.md#the-comparison-uses-the-old-flee-field-then-later-morale-chooses-readiness)

The clearing branch also replaces the action counter with random 0–99, without
the acquisition minimum 20 or an XP term in that body. This is another possible
writer, separate from Hold Fire or weapon recovery; its actual reachability and
later callback order still matter. The named enemy Regular recovery instead
uses morale without this flee term and lacks the same local timer/flee choice.
[Actor-specific recovery](../player-pin-recovery-evidence.md#the-regular-enemy-uses-another-recovery-body)
Additional source: [Source identities](../player-notes/morale.md#citation-3)

[Paratrooper and Engineer recovery](../player-paratrooper-pin-evidence.md)
use morale without the ordinary recovery's flee bonus at their named actions.
Spec Ops' named recovery also uses morale alone but lacks that action's later
positive-morale/flee decision. These local differences do not establish immunity
to other fear helpers or an immediate return to firing.
Additional source: [Source identities](../player-notes/morale.md#citation-4)

[Sarge's own recovery](sarge.md#rally-clears-pinning-without-resetting-every-combat-field)
clears flee on its pin-clear alternative without the ordinary action's later
positive-morale test. His group rally is a different writer: it clears selected
recipients' pinning without itself resetting their morale, flee or action counter.
One universal infantry recovery rule would erase those distinctions.
Additional source: [Source identities](../player-notes/morale.md#citation-5)

Spec Ops' selected active controller also lacks the ordinary positive-morale
gate, while its own pin recovery still reads morale. An explicit withdrawal
flag and the other active-state conditions remain separate. [Exact Spec Ops
admission and withdrawal](spec-ops.md#low-morale-alone-does-not-select-its-ordinary-withdrawal-branch).
Additional source: [Source identities](../player-notes/morale.md#citation-6)

## Fire conversion can reach two separate Sarge morale penalties

The selected enemy flame conversion sets its admitted player's health to-999,
then calls fear and the player-death helper before removal. If that stable
recipient is Sarge, each helper has its own half-of-current-morale loss for
unarmored squad entries; the fatal helper then has its separate lower-rank loss.

For declared Sarge rank 3 and a valid rank 0 follower at morale 20, unchanged
through those calls, the selected writes give 20→10→5→1. Equal-rank 3 instead ends
at 5 at these sites. These are supplied-state source comparisons, not a measured
squad penalty or a claim every Sarge death uses the same caller chain.
[Exact caller, rounding and remaining limits](../player-sarge-burn-evidence.md).
Additional source: [Source identities](../player-notes/morale.md#citation-7)

## An accurate zero-damage hit is not the same as a suppressing miss

The shared firearm's direct pinning write belongs to its **failed-accuracy**
alternative. A passed accuracy comparison with damage 0 does not fall through to
that miss-only block. At supplied Springfield distance 200/burst 0, rifle 0 admits
99 initial miss values, rifle 40 admits 59 and rifle 100 admits none; a reached
pinning attempt still has its separate current-target morale test.

These local input counts do not rank weaker shooters above veterans: actual
damage, other pin sources, targets and full firing/recovery behavior also matter.
Ricochet graphics around a target are separate visual requests, not a measured
suppression circle or one additional pin roll per spark.
[Exact branch, strict morale boundaries and supplied comparison](../player-miss-pinning-evidence.md).
Additional source: [Source identities](../player-notes/morale.md#citation-8)

## A missed enemy shot uses another pin request

In the selected Regular-enemy shot, ordinary-cover and bunker saves belong to
the **accurate** unarmored branch. Its missed-shot alternative instead has a
current-target morale comparison and health-above 10 requirement, then requests
a pinned animation without an explicit pin-field assignment in that caller.
Those save percentages are not a reduction factor for this separate request.

The ordinary target's later recovery/action writers and actual label dispatch
remain separate. A supplied health 11/morale 20/comparison 21 reaches the local
request; health 10 does not. This is not a measured pin, duration, protection
failure or safe cover layout.
[Exact caller, label strings and later state boundaries](../player-incoming-pin-evidence.md).
Additional source: [Source identities](../player-notes/morale.md#citation-9)

## A reaction request is not always a direct pin-field write

The thirteen inspected enemy firearm action bodies each request a pin animation
label without a literal pinned-field assignment in that same body. Their exact
conditions differ. The shared Allied firearm helper has a direct field write
before its own label request, so it should not replace every incoming reaction
path in an explanation or model.

Actual label matching, target entry/recovery, interrupted actions and later
field writers still need qualification before a request becomes a pin outcome
or duration. [Finite thirteen-body scope](../player-incoming-pin-evidence.md#the-same-thirteen-shot-bodies-request-pin-labels-without-literal-pin-field-writes),
[MG/shared statement comparison](../player-incoming-pin-evidence.md#a-requested-label-is-not-an-immediate-field-write-receipt).
Additional sources: [Source identities](../player-notes/morale.md#citation-10)
