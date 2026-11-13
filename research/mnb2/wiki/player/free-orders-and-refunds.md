[Player reference](README.md) · [Support](support.md) · [Tactical points](tactical-points.md) · [Purchase budgets](purchase-budgets.md)

# Fee waivers, free allowances and refunds

“Free” can describe **different stages of a purchase**. In selected historical
**2.3.1g**, distinguish a conditional fee waiver, a stored allowance and a later
refund branch before planning to spend less than the advertised price.
[Ordinary paid budgets](purchase-budgets.md), [recruitment payment evidence](../player-recruitment-receipt-evidence.md)

On this page: [Three different mechanisms](#three-different-mechanisms) · [Which named awards supply the retained allowances?](#which-named-awards-supply-the-retained-allowances) · [A failed or competing choice does not imply one refund rule](#a-failed-or-competing-choice-does-not-imply-one-refund-rule) · [A duplicate weapon has its own guarded credit](#a-duplicate-weapon-has-its-own-guarded-credit)

## Three different mechanisms

- **Fee waiver.** A direct Officer offer with the War Effort Ribbon flag at 1 has one qualifying draw out of 100 that waives its debit. The full 3-TP affordability gate comes first; hoping for the waiver does not admit that offer at 2 TP.
- **Stored free allowance.** Ranger Training admits a supplied freeTrain value exactly 1 instead of requiring 5 TP. The offer consumes that allowance before its later eligible recipient receives training.
- **Later refund credit.** A reached ordinary/recon Morale Boost receipt has a full-morale alternative that returns 1 TP. Its outer health, pending-choice and recipient conditions still matter; this is not a refund for every invalid click.

[Officer gate and waiver](../player-recruitment-receipt-evidence.md#direct-recruitment-gates-precede-the-ordinary-medal-waiver),
[Ranger admission and spending](../ranger-training.md),
[Morale Boost refund](../morale-boost.md#facing-and-refunds-have-separate-predicates)

These are named source examples, not one universal transaction rule. An allowance
can supply an alternative admission path where the particular offer supports it;
a possible random waiver alone does not erase the offer's earlier tests.

## Which named awards supply the retained allowances?

The selected initialization first resets these fields, then has the following
grant writes when each named award flag equals 1:

| Award            | Allowance                       | Selected spending stage                          |
| ---------------- | ------------------------------- | ------------------------------------------------ |
| Xmas Ribbon      | Ranger Training: freeTrain = 1  | Ranger menu admission, before recipient training |
| Halloween Ribbon | Heroism: freeHero = 1           | Valid ordinary/recon Heroism receipt             |
| Victoria Cross   | Ordinary paradrop: freeDrop = 1 | Its radio-acceptance allowance alternative       |

[Exact producers and consumers](../player-allowance-evidence.md),
[Ranger](ranger-training.md), [Heroism](heroism.md),
[ordinary Paratroopers](recruitment-limits.md#paratroopers-have-request-and-acceptance-gates)

The ordinary paradrop tests its medal-based waiver **before** the freeDrop
consumption alternative. If that earlier waiver succeeds, that local branch
does not clear freeDrop. Otherwise an admitted allowance can be spent, or the
paid branch charges 12 TP. Capacity, Signaller, request and delivery tests remain
separate; this ordering does not promise unlimited free arrivals.
[Exact acceptance order](../player-recruitment-receipt-evidence.md#ordinary-paratrooper-request-and-later-acceptance)

Those initialization writes do not establish a fresh allowance after every
menu visit, cancellation or failed recipient. A stored entitlement is different
from a guaranteed delivered recruit, completed upgrade or persistent save.

## A failed or competing choice does not imply one refund rule

Ranger consumes freeTrain before training; an earlier pending recipient branch
can clear its cue without restoring that allowance at the cited sites. Heroism
uses a different later valid-receipt spending stage. Its selected paid refund
for failed rank qualification still sits inside outer live-health and pending-
priority gates. A dead or otherwise invalid click does not inherit that refund
just because another failure path returns TP.
[Pending-choice comparison](../player-pending-choice-evidence.md),
[Heroism receipt/refund](../heroism.md#failed-rank-and-health-alternatives-need-their-full-outer-context)

**Combat Leadership's positive allowance grant remains unqualified.** Its
selected offer can admit freeLeadership exactly 1, but the retained literal map
finds reset writes without qualifying a positive grant mechanism. Do not assign
it to a named medal from description text alone or budget an entitlement that
has not been established for the current start.
[Known consumer and missing grant](combat-leadership.md#do-not-plan-around-an-unqualified-free-allowance)

## A duplicate weapon has its own guarded credit

For the selected ordinary/Scout weapon recipient, a current weapon equal to the
nonzero pending weapon takes a branch that adds the **stored pending weapon
cost** to TP and sets that cost to 0. This is different from replacing a weapon,
refilling ammunition or returning all previous upgrade spending. Health and
earlier pending-choice conditions still decide whether that branch is reached.
[Exact purchase and credit](../bar.md#buying-selects-a-pending-weapon-code),
[worked BAR example](weapon-comparison.md#does-buying-or-rebuying-a-weapon-refill-ammunition)

The complete selected recipient body has no ammo, burst or semi-field write.
Do not turn the duplicate credit into a refill strategy or a universal invalid-
recipient refund. Other actors, input paths and later callbacks remain separate.
[Complete handler and firing-state boundary](../player-weapon-state-evidence.md#the-selected-receipt-changes-weapon-without-writing-ammo-or-repeat-fields)

Before using an exception, identify the current balance, actual role/recipient,
admitted flag or waiver branch, and the stage that spends or returns TP. Then
check what the recipient or request actually received.
[Equipment steps](training-and-equipment.md), [support stages](support.md)

Sources: [Source identities](../player-notes/free-orders-and-refunds.md#citation-1).
Original synthesis of retained selected-source branches; no new purchase,
refund, free-order, initialization or save trial.
