[Player reference](README.md) · [Construction](construction.md) · [Explosives](explosives.md)

# TNT: placed charges and recovered stock

A normal Engineer placement costs **2 TP**, or spends a positive **shared recovered
TNT charge** first. Dropped TNT, stored charges and the placed tntmc object are
different states with different controls.
[Placement spending order](../player-defuse-evidence.md#spending-recovered-tnt)

Historical scope: selected **2.3.1g** source.

| Key fact               | Selected historical behavior                                                   |
| ---------------------- | ------------------------------------------------------------------------------ |
| Normal cost and access | 2 TP; eligible Engineer and proximity                                          |
| Recovered stock        | Positive shared TNT stock spends one charge before TP                          |
| Placed-object release  | Detonation request outside the active rigging cue; rigging has another receipt |
| Main limitation        | Placement, fuse, scenery removal and blast recipients are separate             |

On this page: [A stored charge comes before the normal fee](#a-stored-charge-comes-before-the-normal-fee) · [Placed TNT release depends on the booby-trap cue](#placed-tnt-release-depends-on-the-booby-trap-cue) · [Blast and scenery have different consumers](#blast-and-scenery-have-different-consumers) · [Pioneer drops are picked up through another handler](#pioneer-drops-are-picked-up-through-another-handler)

## A stored charge comes before the normal fee

The offer and later completion need eligible Engineer/proximity state plus the
2-TP-or-positive-stock condition. With a positive recovered pool, the selected
completion spends one charge before TP even when you could afford the fee.
Its fee-waiver alternative requires the no-charge branch; a waiver roll does not
preserve an available recovered charge at these writes. The charge also does
not bypass the Engineer and strict pointer-distance-below-100 requirements.

For supplied valid completion, stock 1/TP 2 spends the charge and leaves TP 2 at
those payment sites. Stock 0/TP 1 fails the affordability/pool gate before the
waiver. These are declared source inputs, not a tested free-build or persistence
strategy. [Exact branches and examples](../player-defuse-evidence.md#spending-recovered-tnt)

## Placed TNT release depends on the booby-trap cue

The selected placed-TNT handler requests the TNT effect and its own removal
when the rigging cue is not 1. That branch does not first require another TP
payment or an Engineer-proximity test. When the cue is 1, it takes the separate
[booby-trap application](booby-trap.md), with its own payment, proximity,
already-rigged and cancellation outcomes.
[Exact release-mode comparison](../player-booby-mode-evidence.md#tnt-has-a-different-earlier-branch-when-rigging-is-not-selected)

Those are handler requests, not a measured click-to-explosion delay, verified
pause behavior or guaranteed detonation in every event order. Source positions,
button delivery and the effect's later callbacks remain separate.

## Blast and scenery have different consumers

The TNT effect calls rock and bunker/palisade helpers before its generic blast.
Their selected strict helper distances differ: rock below 30, bunker below 25,
palisade below 45. These are type/point predicates, not a certified cleared
corridor or protected escape distance. [Scenery source](../scenery-demolition.md)

Its later blast also supplies tag tnt, which takes a different guarded Tiger AT
route from tag zooka. Attachment, owner fields, friendly recipients and later
health work still need their own checks; damage input 100 is not 100 promised
health lost. [Actual TNT effect and AT branch](../player-sticky-tiger-evidence.md),
[blast stages](explosion-damage-stages.md)

## Pioneer drops are picked up through another handler

A qualifying nearby Engineer can collect a dropped Pioneer charge into the
shared freeTNT pool and receive 3 XP at the cited pickup sites, followed by a
promotion-helper call. It is shared stock, not a private charge field on that
Engineer. Later placement still needs its own eligible Engineer and checks.

The dropped object's own countdown can request its explosion and has no local
pause test in that body. Full scheduling is needed before treating pause as
indefinite storage. This pickup object is not the placed TNT release described
above. [Exact drop, pickup and expiry chain](../pioneer-and-tnt.md)

Sources: [Source identities](../player-notes/tnt.md#citation-1).
Selected publisher-associated 2.3.1g; no new native placement, collection or blast trial.

The TNT effect's crater request is another object, made before the later blast
helper call. Its selected template life counter is not the numeric damage 100 or
AT 25 argument, and its drawing does not certify a safe escape boundary.
[Exact crater request and effect receiver](../player-crater-lifetime-evidence.md#five-selected-effects-request-different-crater-aliases-before-their-blast-call)
Additional source: [Source identities](../player-notes/tnt.md#citation-2)
