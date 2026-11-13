[Player reference](README.md) · [Support](support.md) · [Purchase budgets](purchase-budgets.md)

# Smoke request

The menu advertises **1 TP**, but the selected source has **two separate guarded
1-TP debit sites**: the coordinate click and the later Signaller acceptance.
This is a budgeting warning from the source flow, not an observed universal
2-TP price or a claim that every click reaches delivery.
[Smoke request evidence](../smoke-coordinate-request.md)

| Stage                  | Selected source behavior                                                       |
| ---------------------- | ------------------------------------------------------------------------------ |
| Offer                  | Finds an eligible Signaller, remembers its index and enables the smoke pointer |
| Coordinate mouse-up    | Requires sufficient TP, deducts 1 and stores root mouse coordinates            |
| Later radio acceptance | Requires its own successful radio/request/resource gates and deducts 1 again   |
| Delivery opportunity   | Reads shared smoke coordinates later and can emit the effect                   |

If a qualifying coordinate click starts at 2 TP, it can leave 1 TP; a later
qualifying acceptance can leave 0. With no intervening resource change, starting
at 1 instead leaves 0 after the click and fails the later at-least 1 check. Refund,
cancel, interruption and concurrent income outcomes still need their actual
paths. The two debits belong to different owners, not duplicate catalog views
of one subtraction. [Exact 2→1→0 conditional example](../smoke-coordinate-request.md)

The remembered index is not a frozen actor identity. The coordinate fields are
shared and read at the later emission, rather than stored in an immutable object
per order. Other writers, lost/replaced actors and overlapping orders therefore
need qualification before promising which click produces which effect.

The acceptance also clears several competing global support values. This does
not establish that all already emitted ordnance disappears. The later effect,
visual smokescreen, LOS and protection behavior remain separate consumers; no
universal smoke damage-reduction or invisibility percentage is claimed here.
[Support lifecycle distinction](support.md)

Sources: [Source identities](../player-notes/smoke.md#citation-1).
Selected 2.3.1g; [exact evidence](../player-support-evidence.md).

Historical scope: selected **2.3.1g** source. Payment, radio acceptance and
effect delivery are separate stages.

On this page: [Smoke supplies a sight obstacle, not a fixed protection percentage](#smoke-supplies-a-sight-obstacle-not-a-fixed-protection-percentage)

## Smoke supplies a sight obstacle, not a fixed protection percentage

A later selected effect action requests a separate smokescreen cloud. That
cloud has an obstacle child consumed by the sampled line-of-sight helpers.
This differs from a camouflage-net query or an ordinary bullet-cover save;
no universal damage-reduction percentage follows from the cloud drawing.
[Effect, cloud and sight source](../player-smokescreen-evidence.md#the-small-blast-and-later-cloud-are-distinct-actions)

Whether a particular cloud blocks a shot still depends on its indexing, geometry
and the attack's sight checks. A fading cloud is not by itself proof that its
sight obstacle has ended, and the source counter is not a duration in seconds.
[Line-of-sight guide](line-of-sight.md)

## Detailed cloud indexing, lifetime and sight alternatives

A visible cloud is not guaranteed to block a particular sight query, and fading does not itself disable an otherwise qualifying obstacle. Indexing, geometry and sampling still matter; the life counter is not a duration in seconds. Some weapons have their own sight alternatives, without universal smoke penetration.

[Full source comparison and limitations](../player-notes/smoke.md#technical-detail-1).
