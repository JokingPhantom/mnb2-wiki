[Player reference](README.md)

# Recruitment: availability, substitutions and free calls

An advertised price is one part of recruitment. The selected historical **2.3.1g** menu
can check allocation, a deployment flag, a Signaller and affordability before a
later payment or spawn choice. [Recruitment prices](recruitment.md),
[exact source joins](../player-recruitment-receipt-evidence.md)

On this page: [Find the reason an offer failed or changed](#find-the-reason-an-offer-failed-or-changed) · [A possible free recruit still needs the advertised balance](#a-possible-free-recruit-still-needs-the-advertised-balance) · [Resistance's offer can produce a different recruit](#resistances-offer-can-produce-a-different-recruit) · [Sarge is gated by prior deployment state](#sarge-is-gated-by-prior-deployment-state) · [Paratroopers have request and acceptance gates](#paratroopers-have-request-and-acceptance-gates) · [Airborne Challenge is a different command](#airborne-challenge-is-a-different-command) · [Halftrack's flag and Tank's payment are separate rules](#halftracks-flag-and-tanks-payment-are-separate-rules) · [The Special Operations Ribbon counter follows named offers](#the-special-operations-ribbon-counter-follows-named-offers)

## Find the reason an offer failed or changed

| What happened?                                                     | Check this distinction first                                                                                                                                                                              |
| ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| I expected a free Officer, Spec Ops, Resistance recruit or Sarge   | Their possible War Effort waiver comes after the full advertised-balance gate. [Balance before waiver](#a-possible-free-recruit-still-needs-the-advertised-balance)                                       |
| My old Sarge or Halftrack is gone, but I cannot buy another        | The cited offer reads a deployment flag, rather than simply counting living units. [Sarge](#sarge-is-gated-by-prior-deployment-state), [Halftrack](#halftracks-flag-and-tanks-payment-are-separate-rules) |
| Ordinary Paratroopers are unavailable or the call did not complete | Check the below-96 allocation gate, eligible Signaller, air-mission state and later acceptance conditions. [Request and acceptance](#paratroopers-have-request-and-acceptance-gates)                      |
| Airborne Challenge charges a different amount                      | Its selected root command checks 20 TP and uses another payment/quantity path. [Mode 99 command](#airborne-challenge-is-a-different-command)                                                              |
| A Resistance offer requested Spec Ops                              | That offer has a separate template-substitution roll; it is not two recruits or an upgrade to an existing soldier. [Substitution](#resistances-offer-can-produce-a-different-recruit)                     |

These are selected **2.3.1g** source routes. A message, payment or template request
still does not certify a healthy arrival, refund or completed replacement.

## A possible free recruit still needs the advertised balance

The inspected Officer, Spec Ops, Resistance and Sarge buttons check their full
3/5/1/12-TP balance before the War Effort Ribbon waiver branch. With its flag
equal to 1, exactly one integer draw out of 0–99 waives that payment: 1/100, or 1%, conditional on reaching this branch. You cannot
enter the Officer purchase at 2 TP by hoping for this waiver.
[Exact gates and waiver](../player-recruitment-receipt-evidence.md#direct-recruitment-gates-precede-the-ordinary-medal-waiver)

These direct buttons also require the player allocation counter below 100.
That counter is not simply the number of living soldiers on screen.

## Resistance's offer can produce a different recruit

After its payment choice, the **1-TP Resistance offer** has another roll against
Special Operations Ribbon's stored value. With the supplied value 1, draw 0
requests the Spec Ops template; the other 99 values request Resistance. Value 0
does not pass this comparison. This is a recruitment substitution, not an
upgrade to an existing Resistance soldier or a two-unit reward.
[Exact template mapping](../player-recruitment-receipt-evidence.md#resistance-can-request-the-spec-ops-template-instead)

The ordinary [Spec Ops](spec-ops.md) button remains 5 TP. The replacement branch
also differs from that button's persistent Special Ops recruitment counter
write; a template and a menu's accounting statements should not be conflated.

## Sarge is gated by prior deployment state

The Sarge button requires the dedicated deployment flag to be zero, then sets
it to one when entering its spawn path. It does not check whether a previous
Sarge is alive. A flag already at one therefore rejects another purchase even
if no Sarge is currently living. Initialization has a separate reset write;
death alone is not established as reopening this offer.
[Sarge](sarge.md), [exact flag writers](../player-recruitment-receipt-evidence.md#sarges-gate-reads-a-flag-not-current-survival)

## Paratroopers have request and acceptance gates

The ordinary radio offer requires the allocation counter **below 96**, at least
12 TP or the free-drop flag, no listed strafing/bombing mission, and an eligible
Signaller. Exactly 96 fails that first capacity check. This button requests
communication without directly charging TP; the later Signaller acceptance
rechecks capacity and affordability/free-drop state.

At acceptance, a medal waiver is tested **before** the free-drop consumption
alternative. If that medal branch succeeds, this local branch does not clear
the free-drop flag. Otherwise a free flag is consumed, or 12 TP is charged.
That is one source payment-order fact, not proof of unlimited free arrivals.
[Examples and guard boundaries](../player-recruitment-receipt-evidence.md#ordinary-paratrooper-request-and-later-acceptance)

The normal accepted quantity is nominally four, or six with the specific
Airborne profile flag. Landing health and delivery remain separate.
[Paratroopers](paratroopers.md)

## Airborne Challenge is a different command

Mode 99's root reinforcement action checks **20 TP and allocation below 100**,
then debits 20 and requests a nominal four. Its inspected body has no free-drop
or medal waiver test and does not use the ordinary four-versus-six quantity
choice. Those different capacity guards do not by themselves certify what
happens to every actual slot at the limit.
[Deployment modes](deployments.md), [exact root command](../player-recruitment-receipt-evidence.md#airborne-challenge-uses-another-root-command)

Sources: [Source identities](../player-notes/recruitment-limits.md#citation-1)

## Halftrack's flag and Tank's payment are separate rules

The **12-TP Halftrack** offer requires its deployment flag to be zero and
allocation below 100 before checking affordability. Its possible medal waiver
comes after the 12-TP balance check. The button then sets the flag before its
spawn request; absence of a living Halftrack does not itself pass that flag gate.

The **20-TP Tank** button has the same below 100 allocation check and directly
subtracts 20. This selected button has neither that uniqueness flag nor a medal
waiver. These are local purchase rules, not guaranteed arrivals or a complete
replacement/lifecycle test.
[Halftrack and Tank gates](../player-recruitment-receipt-evidence.md#halftrack-availability-and-tank-payment-differ)

The [actual carrier delivery](paratroopers.md#delivery-is-another-action-with-its-own-allocation-writes)
has a direct duplication loop and strict above-100 counter wrap. Earlier
below-96/below-100 offer gates are therefore not interchangeable with a living-
soldier cap or reserved free-slot ledger. Declared counter sequences still need
actual name/depth/lifetime evidence before claiming troops were replaced.
Additional source: [Source identities](../player-notes/recruitment-limits.md#citation-2)

## The Special Operations Ribbon counter follows named offers

Both supported direct **Spec Ops and Sniper** mouse offers add 1 to the career
highspeed counter after their spawn request. Their full-balance/capacity gates
still apply; a successful ordinary fee waiver does not remove that addition.
The Ribbon's source condition reads highspeed at least 100, not specialist kills.

Resistance's possible replacement with the same Spec Ops template does not add
to highspeed in that selected offer body, even though soldierdeployed still
increases. Counter accounting therefore cannot be inferred from the delivered
unit's name alone. Actual arrivals, award entry and durable saving remain
separate. [Exact offers, selector mapping and keyboard limit](../player-special-deployment-evidence.md).
Additional source: [Source identities](../player-notes/recruitment-limits.md#citation-3)
