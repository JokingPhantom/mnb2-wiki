[Player reference](README.md) · [Training and equipment](training-and-equipment.md) · [Purchase budgets](purchase-budgets.md)

# Heroism

**Heroism sets a qualifying recipient's current health to 200.** The selected
2.3.1g offer advertises **4 TP**, with a separate free-Heroism allowance path.
Payment or allowance admission happens before the later recipient choice.
[Offer and health assignment](../heroism.md#the-selected-valid-receipt-writes-200-rather-than-adding-200)

Historical scope: selected **2.3.1g** source; offer, recipient and later
combat effects are separate stages.

| Key fact                   | Selected historical behavior                                           |
| -------------------------- | ---------------------------------------------------------------------- |
| Advertised cost            | 4 TP; separate free allowance path                                     |
| Ordinary/Scout eligibility | Live-health/pending priorities and stored rank above 1                 |
| Health write               | Sets current health to 200; does not add 200                           |
| Important limit            | Not an invincibility flag or a raised Medic/hospital healing threshold |

On this page: [Stored soldier rank matters more than an XP label](#stored-soldier-rank-matters-more-than-an-xp-label) · [Applying it again does not add another 200 health](#applying-it-again-does-not-add-another-200-health) · [Ordinary medical healing still checks below 100](#ordinary-medical-healing-still-checks-below-100) · [The refund branch has its own conditions](#the-refund-branch-has-its-own-conditions) · [The German Sniper's below-ten test still matters](#the-german-snipers-below-ten-test-still-matters) · [Another pending choice can take the earlier recipient branch](#another-pending-choice-can-take-the-earlier-recipient-branch)

## Stored soldier rank matters more than an XP label

The inspected ordinary/recon receipt requires health above 9, the pending
Heroism selection, stored rank above 1 and a later positive-health test. Earlier
pending grenade, training and order branches have priority. The broader static
recipient map retains that rank/health guard across its selected success sites;
it is not proof every template can be recruited or clicked in every mode.
[Exact recipient coverage](../heroism.md#broader-static-receipt-coverage-still-needs-runtime-reachability)

A Medic can load at 25 XP but rank 0, while an Officer can load at 5 XP and rank 9.
With those fields unchanged, the Medic fails **this rank gate** and the Officer
passes it. Other receipt conditions still apply. Buying Heroism should not be
planned from XP alone. [XP and soldier rank](progression.md)

## Applying it again does not add another 200 health

| Supplied current health, qualifying receipt | Health at this assignment |
| ------------------------------------------- | ------------------------- |
| 150                                         | 200                       |
| 200                                         | 200                       |
| 250                                         | 200                       |

The selected write assigns the value; it does not add to current health or
change a maximum-health field. No health-below-200 condition appears at that
success site. These are conditional write results, not a tested repeat-purchase
transaction, guarantee of no later damage or complete survival model.
[Exact assignment and examples](../heroism.md#the-selected-valid-receipt-writes-200-rather-than-adding-200)

The supplied 250-health row makes the spending risk clear: this assignment does
not preserve a value above 200. It does not establish that an ordinary recruit
can reach that state or that a real repeated purchase follows every receipt gate.
Heroism's price and name should not be read as a guaranteed extra 200 health.

## Ordinary medical healing still checks below 100

The cited [Medic](medic.md) sweep admits patients below 100 health and adds 1.
The [Halftrack hospital](halftrack-hospital.md) also checks below 100 but adds 2.
A supplied qualifying patient at 150 therefore fails each of those health tests,
even if an earlier Heroism receipt set its health to 200. At 99, the Medic's
addition gives 100; the hospital's gives 101 at its write. Neither path obtains
a 200-health healing threshold from the Heroism assignment.
[Medic patient guard](../medic-healing.md), [hospital guard and local overshoot](../player-halftrack-hospital-evidence.md#healing-entry-and-patient-scan)

Heroism's inspected receipt does not assign the invincible flag or a protection
expiry counter. The separately named invincibility helper has its own predicates.
Health 200 is not evidence that attack, backblast, AT or friendly-fire guards
are bypassed. [Health and protection state](../heroism.md#increased-health-and-the-invincible-flag-are-different-state)

## The refund branch has its own conditions

For the cited ordinary recipient, a failed rank qualification can return 4 TP
only on its paid path. It still sits below the outer live-health and pending-
priority gates. That does not establish refunds for every dead or invalid click.
The selected Halloween Ribbon initialization supplies the free allowance; its
actual initialization frequency, cancellation and repeated-input outcomes remain
separate. The selected menu does not clear it; the valid ordinary/recon receipt
does. [Producer and spending stage](../player-allowance-evidence.md). [Receipt and refund guards](../heroism.md#failed-rank-and-health-alternatives-need-their-full-outer-context)

Sources: [Source identities](../player-notes/heroism.md#citation-1). Selected publisher-associated 2.3.1g;
[original evidence](../heroism.md). No new gameplay or healing trial.

Allowance producer sources: [Source identities](../player-notes/heroism.md#citation-2)

The [off-field protection flag](protection-flag.md) has an asymmetric outside/
flee grant and inside clear, plus actor-specific caller guards. That is another
reason health 200 does not describe every protection state.

Protection detail source: [Source identities](../player-notes/heroism.md#citation-3)

The [blast core example](explosion-damage-stages.md#a-core-hit-is-different-from-a-fragment-subtraction) follows a separate direct-removal request that does not first exhaust a 200-health pool. Its declared helper distance is not a measured lethal placement.
Additional source: [Source identities](../player-notes/heroism.md#citation-4)

## The German Sniper's below-ten test still matters

The selected German Sniper damage branch can draw 0–199, then requests the
recipient's death state when resulting health is **below 10**. With supplied
current health 200 and every earlier shot/save guard admitting the subtraction:

| Damage draw | Remaining health | That below-ten request |
| ----------- | ---------------- | ---------------------- |
| 190         | 10               | No                     |
| 191         | 9                | Yes                    |
| 199         | 1                | Yes                    |

A damage maximum below 200 therefore does not by itself promise continued
operation after one admitted hit. These are source writes and navigation
requests, not measured one-shot kills or proof a positive-health wounded actor
can never recover. The earlier ordinary-cover save still has its own test;
this enemy Sniper body does not add the common extra bunker save.
[Exact input boundary and remaining actor-state limits](../player-german-sniper-evidence.md#a-supplied-200-health-target-can-meet-the-below-ten-request-with-health-positive)
Additional source: [Source identities](../player-notes/heroism.md#citation-5)

## Another pending choice can take the earlier recipient branch

On the selected ordinary recipient, pending grenades or Ranger training are
earlier than Heroism and can clear its pending cue. A supplied rank 3/health 100
soldier with frag 0 and both grenade/Heroism cues receives the earlier grenade
effect, without a health 200 assignment or 4 TP refund at that selected branch.
Bayonet/Hold Fire earlier branches have different cleanup and can leave the
Heroism cue unchanged there. This is declared source priority, not a native
multi-click or cancellation guarantee. [Exact competing-choice examples and free-allowance distinction](../player-pending-choice-evidence.md).
Additional source: [Source identities](../player-notes/heroism.md#citation-6)
