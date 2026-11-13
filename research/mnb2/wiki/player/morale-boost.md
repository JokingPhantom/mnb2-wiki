[Player reference](README.md) · [Training and equipment](training-and-equipment.md) · [Purchase budgets](purchase-budgets.md)

# Morale Boost

A selected **1-TP order** that stores a bonus before choosing its recipient.
The offer keeps the **largest realized Officer roll**. The later selected
Regular/Scout receipt adds that amount, then checks whether morale is positive
before clearing flee. Payment, morale gain and recovery are separate stages.
[Exact selected 2.3.1g source](../morale-boost.md)

Historical scope: selected **2.3.1g** source; offer, recipient and later
combat effects are separate stages.

| Key fact                   | Selected historical behavior                                                       |
| -------------------------- | ---------------------------------------------------------------------------------- |
| Advertised cost and access | 1 TP; eligible Officer scan, then recipient choice                                 |
| Bonus                      | Largest realized qualifying Officer roll, not the sum or always highest-XP Officer |
| Ordinary/Scout receipt     | Adds pending bonus with live-health and old-morale guards                          |
| Recovery                   | Positive result can clear flee; pinning and withdrawal are separate                |

On this page: [The highest-XP Officer does not automatically supply the bonus](#the-highest-xp-officer-does-not-automatically-supply-the-bonus) · [More rolls can change the mean without changing the recovery threshold](#more-rolls-can-change-the-mean-without-changing-the-recovery-threshold) · [Recovery checks the result after addition](#recovery-checks-the-result-after-addition) · [The full-morale refund is a guarded alternative](#the-full-morale-refund-is-a-guarded-alternative)

## The highest-XP Officer does not automatically supply the bonus

The menu resets its pending bonus fields, then scans eligible specialization-2
actors with health above 10 and invincible not 1. Each produces a random value
from 1 through its supplied positive integer XP. Only a value larger than the
current pending bonus replaces it.

For supplied eligible Officers at XP 5 and XP 20, valid realized rolls of 5 and 1
leave a pending bonus of 5. The higher-XP Officer has the larger possible range,
but does not win that comparison. These are declared inputs, not measured
frequencies or a recommendation to field a particular number of Officers.
[Offer scan](../morale-boost.md#the-offer-keeps-the-largest-realized-roll)

With an Officer detected and at least 1 TP, the selected offer deducts 1 TP and
changes the pointer. It has not raised a soldier's morale yet. Earlier pending
equipment/orders and the later recipient's health still affect application.

## More rolls can change the mean without changing the recovery threshold

For a separately supplied recipient at morale −10, the selected positive-result
receipt needs a pending bonus above 10. With declared independent uniform offer
rolls, one eligible XP-20 Officer gives that in half the inputs. Adding an
eligible XP-5 Officer slightly raises the mean pending bonus, from 10.5 to 10.7,
but leaves this above-10 fraction at one half: its own roll never exceeds 5.

Two eligible XP-20 Officers instead give a mean maximum 13.825 and an above-10
fraction of three quarters. The offer keeps the best realized roll; it does not
add the rolls or double a recovery percentage. These are conditional examples
with a paid accepted offer and a later valid receipt, not measured command
outcomes or advice about the best number of Officers.
[Exact declared domains and receipt boundary](../morale-boost.md#declared-officer-inputs-separate-the-bonus-mean-from-recovery-admission).

## Recovery checks the result after addition

For the selected Regular/Scout family, health must be above 9, the pending boost
positive and old morale below 100, after earlier command priorities. Assuming
that receipt is reached with valid fixed state:

| Old morale / pending boost | Morale at the addition | Selected flee-clear test     |
| -------------------------- | ---------------------- | ---------------------------- |
| -10 / 10                   | 0                      | Fails: result is not above 0 |
| -10 / 11                   | 1                      | Passes                       |
| 95 / 20                    | 115                    | Passes                       |

The branch clears the pending boost before the later recovery test. That does
not erase the addition or make the result test unreachable. The old-below-100
guard is also not an immediate 100 cap: the supplied 95-plus-20 example reaches 115
at that write. Later morale writers remain separate.
[Receipt order](../morale-boost.md#a-selected-regularrecon-receipt-adds-before-checking-recovery)

The passing recovery branch clears flee and requests frame 1. It does not assign
pinned or withdraw at those sites, so this is not a universal cancel-retreat or
unpin command. Subsequent actor logic still matters. [Morale and pinning](morale.md)

## The full-morale refund is a guarded alternative

For an otherwise reached selected receipt with ordinary finite old morale 100
or higher, the not-below-100 alternative returns 1 TP, clears the pending boost
and resets the pointer. It is not a refund guarantee for every dead or invalid
recipient, cancellation or specialist.

A later facing scan also chooses an eligible Officer by its own indexed search;
it does not recover the identity of whichever Officer supplied the winning
bonus roll. Do not infer a nearest-Officer or highest-XP facing rule from it.
[Facing and refund predicates](../morale-boost.md#facing-and-refunds-have-separate-predicates)

Sources: [Source identities](../player-notes/morale-boost.md#citation-1). Selected publisher-associated 2.3.1g,
regular/recon receipt scope; original source-derived guide and supplied inputs,
with no new purchase, recovery or refund trial.

If the soldier remains pinned or does not resume firing after a boost, compare
[morale recovery and unpinning](morale.md#compare-morale-recovery-with-unpinning).
The selected positive-morale recovery writes and Sarge's unpin writes address
different fields; neither is a guaranteed complete readiness reset.
Comparison source: [Source identities](../player-notes/morale-boost.md#citation-2)
