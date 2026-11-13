[Player reference](README.md) · [Support](support.md) · [Purchase budgets](purchase-budgets.md)

# Naval and counter-artillery

These two requests have very different accounting. **Naval acceptance copies
the current TP balance into a shared quantity and sets TP to 0. Counter-artillery
has a guarded 2-TP menu debit and later checks whether enemy artillery is still
active.** Neither should inherit bombing's transaction rules.
[Exact radio and menu sites](../player-support-evidence.md#report-naval-and-counter)

Historical scope: selected **2.3.1g** source. Payment, radio acceptance and
effect delivery are separate stages.

| Call              | Menu/access stage                                                                | Acceptance and later effect                                                                               |
| ----------------- | -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| Naval             | At least 1 TP; pending radio request                                             | Copies current TP to shared quantity and sets TP to 0; later emissions separate                           |
| Counter-artillery | Eligible command actor and Signaller, active enemy artillery; guarded 2-TP debit | Rechecks active artillery; counter credit affects named future event selections, not all shells in flight |

On this page: [Naval artillery uses the acceptance-time balance](#naval-artillery-uses-the-acceptance-time-balance) · [Does Naval use the same quantity bonus as artillery?](#does-naval-use-the-same-quantity-bonus-as-artillery) · [Counter-artillery pays before the later state test](#counter-artillery-pays-before-the-later-state-test) · [A positive Naval request is not reserved TP](#a-positive-naval-request-is-not-reserved-tp)

## Naval artillery uses the acceptance-time balance

After its earlier radio/request-priority gates, the selected naval branch gains
1 experience, clears competing support states, copies the current tactical points
into shared naval quantity, then sets tactical points to 0. The value is not
necessarily the balance at the initial menu click. The later cadence can emit
naval effects from positive quantity and decrement it, with separate random
opportunities, placements and explosion processing.
[Quantity and delivery chain](../support-delivery.md)

The four numeric explosion arguments have different blast/damage roles. Naval
behavior also differs between same-labelled binary families, so an old universal
blast or invulnerability claim needs an exact version. No safe friendly-fire
layout or guaranteed total damage follows from spending the balance.
[Version differences](editions.md)

## Does Naval use the same quantity bonus as artillery?

**The selected acceptance writes use different quantity sources.** Artillery
copies the Signaller's local requested quantity; Naval instead copies the TP
balance at acceptance. Increasing a pending Naval number does not, by itself,
increase that balance-based accepted quantity.
[Exact menu and acceptance writes](../player-support-evidence.md#artillery-and-naval-copy-different-quantity-sources)

For separate supplied examples, each starting its reached acceptance branch
with **5 TP** and that call's local request value **3**:

| Call      | Shared quantity at the selected write | TP after the selected charge |
| --------- | ------------------------------------- | ---------------------------- |
| Artillery | 3, copied from the local request      | 2, after the 3-TP debit      |
| Naval     | 5, copied from the current TP balance | 0                            |

These are independent source-state comparisons, not two calls performed in
sequence or an observed payout. Artillery's [qualifying recon addition](artillery.md#does-a-scout-add-shells-and-can-spec-ops-do-the-same)
changes its local quantity before that copy. The selected Naval menu also has
local request-number writes, but its quoted acceptance does not copy that number
into shared quantity. Do not add it again on top of the balance-derived value.

Actual request admission, priority, overlap, emission opportunities and recipient
damage still matter. Neither table entry promises that many hits or ranks one
call as better value. Selected historical **2.3.1g**;
[quantity and delivery limits](../support-delivery.md).

## Counter-artillery pays before the later state test

The selected offer requires enough TP, an eligible command actor, an active enemy
artillery state and an eligible Signaller. It then deducts 2 TP and queues the
actor's counter request. At radio completion, enemy artillery is tested again.
The selected successful active-strike branch increments a shared counter; the
no-longer-active alternative has a different outcome. Initial active artillery
is not a guarantee that it remains active until that callback.

At this selected completion site, **both counter outcomes clear shared naval
and friendly artillery quantities**. The no-longer-active branch gains local
experience but does not grant a counter credit or a TP refund there. A paid
request can therefore reach a failure path that still changes friendly support.
This does not establish the outcome of an actual overlapping volley or remove
shells already emitted. [Exact comparison](../player-support-overlap-evidence.md#counter-failure-can-still-change-friendly-support)

The inspected shared-counter consumers are **future enemy event-selection
branches**: one starts an artillery request only when the counter equals 0;
otherwise it decrements the counter. Another later-wave event family has its
own corresponding consumption. Those sites are not a universal removal of shells
already in flight or proof the current strike instantly stops.
[Counter consumers](../player-support-evidence.md#report-naval-and-counter)

The selected later artillery-delivery consumer tests delay, positive strike
quantity and its random gate; it does not repeat a counter-credit test there.
It samples the current squad half for each successful effect request. A future
strike prevented at event selection and an already positive queue are different
states. [Exact shared consumer](../player-german-artillery-evidence.md).

The **Forward observer Ribbon**, with its stored flag equal to 1, can add **1 TP**
on the selected active counter-artillery completion, under its own mode/cap
conditions. Its source field is medal 43.
[Named award and consumer](../player-support-award-evidence.md#names-map-to-specific-fields-and-guards)
That is not a full refund of the 2-TP offer, nor proof that every
interrupted order receives any refund. Timing, stale actor indices, repeated
requests and other event sources still need qualification.

Sources: [Source identities](../player-notes/naval-and-counter-artillery.md#citation-1).
[Exact source notes](../player-support-evidence.md)

The [Scout request-field comparison](../support-delivery.md#the-same-scout-count-reaches-different-artillery-and-naval-readers)
shows another reason to distinguish menu state from acceptance quantity. The
Naval offer adds qualified recon entries to its local marker, but the quoted
acceptance quantity reads current TP instead of copying that marker. This does
not establish an extra round per Scout in the accepted Naval queue.

## A positive Naval request is not reserved TP

Spending TP after selecting Naval can change what the later acceptance provides.
A radio message alone does not prove a positive volley: this acceptance can
copy a zero balance while still changing competing support state.
[Exact zero-funds branch](../support-delivery.md#naval-has-no-repeated-positive-funds-guard-at-this-acceptance-site)

<details>
<summary>Detailed supplied zero-balance example and callback limits</summary>

The selected Naval offer requires at least 1 TP, but its later acceptance branch
has no repeated positive-funds check. With a separately supplied positive local
request and TP 0 at that callback, it can perform the quoted XP/shared-state
writes while copying 0 into the Naval queue. Its clear of friendly artillery is
still in that branch; the radio message alone is not proof of a positive volley.
Actual earlier clicks, valid request state, already emitted effects and later
callbacks remain unqualified.
[Exact no-repeat-gate branch and supplied zero-funds example](../support-delivery.md#naval-has-no-repeated-positive-funds-guard-at-this-acceptance-site).

</details>

Additional source: [Source identities](../player-notes/naval-and-counter-artillery.md#citation-2)
