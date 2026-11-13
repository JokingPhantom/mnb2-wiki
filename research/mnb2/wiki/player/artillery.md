[Player reference](README.md) · [Support](support.md) · [Purchase budgets](purchase-budgets.md)

# Artillery support

Artillery requests shells over a sampled area, rather than aiming every round
at one enemy you select. An eligible Signaller starts the request, and later
radio acceptance determines the paid quantity available for delivery.
[Selected 2.3.1g request and effect chain](../support-delivery.md)

Advertised at **3 TP**, with a requested round quantity built from a random
**1–8 base**, a conditional career addition and qualifying recon recipients.
The selected quantity is not universally capped at 8, and a requested number
is not proof every round lands after interruptions or state changes.
[Quantity and delivery evidence](../player-support-evidence.md#artillery-and-bombing)

Historical scope: selected **2.3.1g** source. Payment, radio acceptance and
effect delivery are separate stages.

| Key fact                   | Selected historical behavior                                                              |
| -------------------------- | ----------------------------------------------------------------------------------------- |
| Advertised cost and access | 3 TP; eligible Signaller                                                                  |
| Payment                    | Later acceptance rechecks and deducts 3 TP                                                |
| Accepted quantity          | Local request: base 1–8 plus qualifying award/recon additions                             |
| Delivery limit             | Accepted quantity replaces shared artillery; emissions still need their own opportunities |

On this page: [Eligibility, payment and overlapping calls](#eligibility-payment-and-overlapping-calls) · [Does a Scout add shells, and can Spec Ops do the same?](#does-a-scout-add-shells-and-can-spec-ops-do-the-same) · [Where shells land](#where-shells-land)

## Eligibility, payment and overlapping calls

The selected menu path finds a Signaller with specialization 6, health above 10
and no invincibility flag. It sets that actor's quantity to 1–8, adds **4 requested
rounds for a positive Ground Controller Ribbon flag**, then adds its counted
qualifying recon value. The Ribbon is the selected medal 22 field; this adds
to a request, rather than guaranteeing four extra impacts.
[Named award and consumer](../player-support-award-evidence.md#names-map-to-specific-fields-and-guards)

At the later radio acceptance, affordability is checked again, 3 TP is deducted
and the actor's requested quantity is copied into shared artillery state.
This acceptance replaces any remaining shared artillery quantity; it does not
add the new request to an existing queue. Several other support acceptances
also clear that quantity. [Overlap comparison](../player-support-overlap-evidence.md#shared-state-written-by-each-selected-acceptance)
The source then emits an artillery effect only at a qualifying unpaused cadence
opportunity with a random 0–99 roll below 40 and positive shared quantity. Each
such emission decrements that quantity by 1.

## Does a Scout add shells, and can Spec Ops do the same?

**A qualifying recon entry adds 1 to the requested quantity.** The selected
Scout load identifies its type as recon; the selected Spec Ops load instead
uses sas. With those types unchanged, Spec Ops is not automatically a substitute
for this Scout quantity contribution. The scan also needs health **above 10**
and its particular `invincibility != 1` test.
[Exact named load and quantity join](../player-support-evidence.md#scout-type-and-the-artillery-recon-addition)

The base 1–8 request is formed before adding recon contributions. For supplied
counts of entries that actually pass the scan, the request arithmetic is:

| Qualifying recon entries counted | Ground Controller field not positive | Ground Controller field positive |
| -------------------------------- | ------------------------------------ | -------------------------------- |
| 0                                | 1–8 requested rounds                 | 5–12 requested rounds            |
| 1                                | 2–9 requested rounds                 | 6–13 requested rounds            |
| 2                                | 3–10 requested rounds                | 7–14 requested rounds            |

These are **selected 2.3.1g request quantities**, not measured impacts or a
recommendation to buy Scouts for artillery. The count is passing indexed entries,
not a guarantee that every recruited Scout is counted. The named award adds 4
when its field is positive; the quote does not impose an eight-round ceiling.
Later affordability, Signaller acceptance, replacement by another request and
actual shell emissions still matter. [Scout](scout.md), [Spec Ops](spec-ops.md),
[payment and delivery stages](../support-delivery.md)

The recon scan's `invincibility` field is spelled differently from the Signaller
guard's `invincible`. Do not replace one test with the other when interpreting
a particular supplied actor state. [Exact guard and source limits](../player-support-evidence.md#scout-type-and-the-artillery-recon-addition)

## Where shells land

Do not copy this request-quantity rule onto Naval support: its selected radio
acceptance takes quantity from the current TP balance instead. Compare
[artillery versus Naval quantity sources](naval-and-counter-artillery.md#does-naval-use-the-same-quantity-bonus-as-artillery)
before treating every recon-related local request number as delivered rounds.

The inspected effect placement uses x 0–399 and y 0–299 source coordinates. Those
are placement expressions, not a target-seeking accuracy percentage or a
promise of shells at the enemy you clicked. The later explosion helper has its
own armor, protection, distance and recipient branches; its damage argument 300
is not 300 guaranteed health loss to every nearby unit.
[Effect and blast chain](../support-delivery.md)

A per-opportunity 40-of-100 emission check is not a measured rounds-per-second
rate. Full effect activation, geometry, simultaneous request replacement and
uninterrupted-volley outcomes remain open. The useful distinction is **quantity
requested versus quantity accepted versus effects actually emitted**.

Sources: [Source identities](../player-notes/artillery.md#citation-1).
Selected 2.3.1g; [exact rows](../player-support-evidence.md).

Additional source: [Source identities](../player-notes/artillery.md#citation-2)
