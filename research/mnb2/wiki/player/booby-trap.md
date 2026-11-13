[Player reference](README.md) · [Explosives](explosives.md) · [Collateral damage](collateral-damage.md)

# Booby trap

Booby Trap costs **1 TP to apply to an existing eligible mine or TNT object**. Selecting the offer starts a pending action; the object’s release action checks the Engineer and proximity conditions, then sets the trap flag and handles payment. [Exact offer and receipt](../player-booby-mode-evidence.md#offer-and-recipient-receipt-remain-separate)

Historical scope: selected **2.3.1g** source.

| Key fact        | Selected historical behavior                                               |
| --------------- | -------------------------------------------------------------------------- |
| Cost and host   | 1 TP application to an existing eligible mine/TNT                          |
| Application     | Eligible Engineer, pointer proximity and current affordability             |
| Payment         | At the selected object's eligible receipt; no Sapper waiver in that branch |
| Important limit | Rigging, Pioneer interaction, explosion and casualty credit differ         |

On this page: [Rigging can succeed, cancel or leave the cue selected](#rigging-can-succeed-cancel-or-leave-the-cue-selected) · [The Pioneer interaction is not the same as an ordinary mine trigger](#the-pioneer-interaction-is-not-the-same-as-an-ordinary-mine-trigger) · [Interdiction uses a counter above 25](#interdiction-uses-a-counter-above-25)

## Rigging can succeed, cancel or leave the cue selected

With the rigging cue active, an unrigged target, sufficient balance and an
eligible Engineer above 10 health at strict pointer-distance below 100, the
selected receipt sets the target's trap flag, charges 1 TP and clears the cue.
There is no Sapper medal fee-waiver test in that recipient branch.

A failed Engineer-proximity check clears the cue without that debit. Insufficient
TP also clears it. An already-rigged object with enough TP instead receives a
stacking message without another debit or a cue-clear write at that branch.
These are source outcomes for a reached handler, not full-click or focus guarantees.
[Inputs and exact mode table](../player-booby-mode-evidence.md#offer-and-recipient-receipt-remain-separate)

Placed [TNT](tnt.md) is especially worth distinguishing: outside the rigging cue,
its selected release handler requests an explosion and removal. With the cue
active it takes the rigging alternative. An already-rigged rejection there does
not automatically fall through to the TNT explosion branch. Actual event order
and effect activation still need the original player.
[Exact TNT-versus-mine dispatch](../player-booby-mode-evidence.md#tnt-has-a-different-earlier-branch-when-rigging-is-not-selected)

## The Pioneer interaction is not the same as an ordinary mine trigger

The selected Pioneer branch scans a trapped mine/TNT, creates its mine effect
at the Pioneer's own point and removes the scanned object. It does not simply
reuse the ordinary mine's trigger-center step. Both ordinary and AT mine loads
use the recognized mines type, while their ordinary triggers remain different.
A triggered trap is not proof the Pioneer died or nearby allies are safe.
[Existing exact Pioneer/counter comparison](../booby-trap.md)

## Interdiction uses a counter above 25

The award's selected test requires boobyKill above 25 and an unearned ribbon,
under its other display and ordering gates. Counter 25 fails that comparison;
26 passes. The cited counter increment belongs to the Pioneer interaction and
emission path, not a verified unique-death census. Do not turn it into a promise
that the 26th distinct Pioneer kill immediately awards the ribbon.

Once the ribbon flag is supplied as 1, certain construction sites have their
own below-10 random comparison for an automatic trap-flag write. The ordinary
three-mine completion has three such sites; AT mine and TNT have their own.
Those are conditional writes, not a guaranteed rigging benefit or a measured
whole-kit probability. [Mine placement sites](../player-mine-placement-evidence.md),
[award source](../booby-trap.md#the-award-counter-is-not-a-verified-kill-count)

Sources: [Source identities](../player-notes/booby-trap.md#citation-1).
Selected publisher-associated 2.3.1g; no new native detonation, casualty or award trial.

The selected scenery snapshot explicitly handles an exact-one trap flag when
rebuilding eligible saved objects, but it is not a complete copy of every field
or proof of the same later trigger/damage. It also has a separate unsaved-removal
branch. [Refresh, scale and trap-state limits](../player-scenery-refresh-evidence.md).
Additional source: [Source identities](../player-notes/booby-trap.md#citation-2)

[Original opening and evidence context](../player-notes/booby-trap.md#opening-before-player-language-correction).
