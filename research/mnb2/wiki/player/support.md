[Player reference](README.md) · [Support](support.md) · [Tactical points](tactical-points.md) · [Purchase budgets](purchase-budgets.md)

# Radio support: selection, payment and delivery

Choose radio support by its **effect, required roles and actual charge timing**. The selected historical **2.3.1g** smoke request has two conditional charge sites, while Naval support takes the current TP balance when the Signaller accepts it. Check the individual call before treating its menu price as the whole cost or expecting shells to arrive. [Radio evidence](../player-support-evidence.md)

Find your question: [call effects](#what-the-calls-do),
[required roles](#do-i-need-an-officer-as-well-as-a-signaller),
[prices](#advertised-prices),
[pending TP](#does-selecting-a-call-reserve-its-tp), or
[missing requests](#why-a-request-may-disappear-without-the-expected-result).

## What the calls do

Choose by the effect you need, then check the individual call's requirements.
These are conditional source effects, not guaranteed arrivals or damage totals.
Each linked card gives its retained evidence and remaining limits.

| Call                                                | Effect to compare                                                | Main limitation                                                                                                  |
| --------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| [Artillery](artillery.md)                           | Scattered shell positions for area fire                          | Another accepted call can replace or clear rounds still waiting for delivery                                     |
| [Bombing](bombing.md)                               | An aircraft bomb with separate blast and structure effects       | Placement and blast checks decide who is affected; a blast value is not fixed health loss or a universal ceiling |
| [Close air support](close-air-support.md)           | Aircraft strikes at scattered positions                          | 17 possible strike sites are not 17 guaranteed hits                                                              |
| [Air superiority](air-defense.md)                   | Air protection for selected enemy support and V1 stages          | It does not establish cancellation of every pending attack or guaranteed interception                            |
| [Smoke](smoke.md)                                   | Smoke clouds used by line-of-sight checks                        | Geometry and sight-line sampling still matter; no fixed bullet-save percentage is established here               |
| [Situation report](situation-report.md)             | A possible TP reward after paying for the report                 | A net gain is not guaranteed                                                                                     |
| [Naval artillery](naval-and-counter-artillery.md)   | Naval barrage quantity based on TP at acceptance                 | Acceptance spends that balance; requested quantity is not guaranteed total damage                                |
| [Counter-artillery](naval-and-counter-artillery.md) | Counter credits against selected future enemy artillery requests | Existing queued or airborne shells are not proven to disappear                                                   |

## Do I need an Officer as well as a Signaller?

**Some selected offers add an Officer check; others' quoted request guards
identify a Signaller without that additional condition.** Use the named call,
rather than assuming every radio option has the same role requirement.
This compares selected historical **2.3.1g offer records**; other resource,
state, menu/input and later delivery conditions still apply.
[Exact role and request rows](../player-support-evidence.md#support-offer-role-comparison)

| Selected offer                                      | Role checks in the compared records                              | Another condition to watch                                                     |
| --------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| [Artillery](artillery.md)                           | Signaller request guard; no additional Officer condition there   | Initial 3 TP and later radio affordability are separate                        |
| [Smoke](smoke.md)                                   | Signaller selection guard; no additional Officer condition there | Coordinate selection and later acceptance have separate charges                |
| [Situation report](situation-report.md)             | Signaller request guard; no additional Officer condition there   | Cooldown and medal-dependent offer guards still apply                          |
| [Naval artillery](naval-and-counter-artillery.md)   | Signaller request guard; no additional Officer condition there   | Initial at-least-1-TP gate is separate from spending the balance at acceptance |
| [Bombing](bombing.md)                               | Officer check, then Signaller                                    | Shared bombing and strafing must both be below 1 at that offer                 |
| [Close air support](close-air-support.md)           | Officer check, then Signaller                                    | The same shared bombing/strafing exclusion applies                             |
| [Air Superiority](air-defense.md)                   | Officer check, then Signaller                                    | Its offer also checks those shared bombing/strafing states                     |
| [Counter-artillery](naval-and-counter-artillery.md) | Officer check, then Signaller                                    | Enemy artillery must be active at the offer; it is checked again later         |

The quoted role scans use **health above 10** and `invincible != 1`; exactly
10 health fails those role tests. Officer and Signaller mean their selected
specializations, not a high rank, a radio-looking sprite or a passing ordinary
movement test. Meeting a role guard does not prove the request was accepted or
its effect arrived. The table does not certify every keyboard or menu route.
[Officer](officer.md), [Signaller](signaller.md),
[health-10 differences](wounded-and-rescued.md#ten-health-does-not-mean-every-job-is-ready)

## Plan the request before calling

For **selected 2.3.1g**:

1. Check the Signaller's eligibility and any additional Officer requirement.
2. Select the named call and complete any required coordinate step.
3. Keep its needed TP available until acceptance; another purchase can change
   that later affordability check.
4. Check acceptance separately from shells or aircraft actually arriving.
   [Request and payment evidence](../player-support-evidence.md),
   [Signaller](signaller.md).

Before stacking calls, check the [replacement rules](../player-support-overlap-evidence.md#shared-state-written-by-each-selected-acceptance):
some accepted calls clear remaining artillery quantity, and another artillery
acceptance replaces it. This does not establish that already emitted effects
vanish. A cleared request or a successful radio roll alone is not proof of
the intended delivery.

## Budget one call, then check what actually arrived

With none of the listed roles already present, normal paid
**Signaller 3 + Artillery 3 = 6 TP**. For Bombing, the equivalent commitment is
**Officer 3 + Signaller 3 + Bombing 3 = 9 TP**. These assume eligible offers and
no waiver, free allowance or other balance change; they are arithmetic budgets,
not played completed calls. An existing eligible role reduces the additional
purchase needed. [Recruit-plus-call budgets](purchase-budgets.md#preparing-a-radio-request-from-scratch).

If the expected support does not arrive, check in this order:

1. Were the required roles eligible when the offer was chosen?
2. Was any coordinate/recipient step completed?
3. Was the required balance still available when the request was accepted?
4. Did a later accepted call replace or clear support still waiting for delivery?

Observe the actual shells, aircraft or effect separately from a radio sound or
cleared request. Do not assume a missing effect refunded the charge or that
selecting the call again is free. [Signaller cleanup](signaller.md),
[waivers versus refunds](free-orders-and-refunds.md).

For an immediate armor problem, compare [AT units and placed weapons](anti-tank-options.md)
with support before committing to a call whose delivery is still pending.

## Advertised prices

| Offer                                               | Advertised TP | Request/payment distinction                                      |
| --------------------------------------------------- | ------------- | ---------------------------------------------------------------- |
| [Artillery](artillery.md)                           | 3             | Requested quantity has base rolls and additions                  |
| [Bombing](bombing.md)                               | 3             | Officer/Signaller eligibility, then later affordability/payment  |
| [Aerial close support](close-air-support.md)        | 1             | Separate request/aircraft path; bombing rules are not universal  |
| [Air superiority](air-defense.md)                   | 1             | State countdown and particular event/rocket consumers            |
| [Smoke](smoke.md)                                   | 1             | Coordinate click and later radio acceptance have separate debits |
| [Situation report](situation-report.md)             | 1             | Charge precedes a conditional capped reward                      |
| [Naval artillery](naval-and-counter-artillery.md)   | Variable      | Uses TP at acceptance, then sets the balance to 0                |
| [Counter-artillery](naval-and-counter-artillery.md) | 2             | Menu debit, active-strike tests and future-event counter         |

## Does selecting a call reserve its TP?

The [Signaller](signaller.md) completion roll depends on experience, but passing
it does not bypass request-specific resource conditions. An initial affordability
check generally does not reserve the balance for a later callback. Stored
actor-local requests, shared future-delivery counters and already emitted effects
are different state.

The [named award guide](support-and-economy-awards.md) connects Air Medal/Air
Command waivers, Ground Controller quantity and Field Commander HQ effects to
their specific source guards. A medal does not apply one discount to every call.

## Why a request may disappear without the expected result

The selected completion frame handles requests in a fixed branch order. It then
clears several actor request fields under the successful outer radio roll even
if a branch-specific resource check failed. A cleared request is therefore not
a delivery receipt. Some support acceptances also clear competing shared states;
that does not prove every shell or aircraft already emitted disappears.
[Request cleanup](signaller.md)

At the selected acceptance frame, air superiority, smoke, naval and either
counter-artillery outcome clear shared artillery quantity. A new artillery
acceptance replaces its remaining quantity instead of adding to it. Bombing
and close-air acceptance do not explicitly clear artillery at that site.
Situation reports do not write the six compared delivery states there.
These distinctions matter when support overlaps; they do not guarantee that
already emitted effects disappear or that every pending request survives.
[Priority and replacement table](../player-support-overlap-evidence.md#shared-state-written-by-each-selected-acceptance)

An antenna changes a particular failed-call retry path; it does not add a new
term to that completion-success comparison. Radar and HQ detection scan different
receiver collections. More visible support buildings do not automatically produce
a count-based multiplier. [Air/antenna detection](air-defense.md), [Field HQ](field-hq.md)

Sources: [Source identities](../player-notes/support.md#citation-1).
All pages retain source/version and remaining execution limits;
[exact evidence](../player-support-evidence.md).

[Signaller interruption boundaries](signaller.md#an-interrupted-animation-is-not-a-refund-or-a-cleared-request)
now bind the own Hold Fire receipt and Concentrate Fire combat navigation.
Their selected sites do not explicitly erase local radio requests; that does
not certify resumption, cancellation, refund or recall of emitted support.
Additional source: [Source identities](../player-notes/support.md#citation-2)

[Original opening and evidence context](../player-notes/support.md#opening-before-player-language-correction).
