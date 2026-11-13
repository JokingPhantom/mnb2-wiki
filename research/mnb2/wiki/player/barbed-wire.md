[Player reference](README.md) · [Defenses](defenses.md) · [Construction](construction.md)

# Barbed wire

A **1-TP Engineer construction** that can hurt unarmored actors on **both sides**.
Its selected damage checks do not exempt your soldiers.
[Selected 2.3.1g evidence](../player-wire-evidence.md)

Historical scope: selected **2.3.1g** source; the stated saves and placement
checks are conditional, not a certified protected layout.

| Key fact                  | Selected historical behavior                                    |
| ------------------------- | --------------------------------------------------------------- |
| TP cost and availability  | 1 TP; Engineer construction                                     |
| Placement                 | Eligible Engineer, pointer proximity and current affordability  |
| Damage eligibility        | Both sides; qualifying intersection, health at least 1, armor 0 |
| Damage per admitted visit | 1 health; fresh wired counter may be zero                       |

On this page: [Placing it](#placing-it) · [Who can be hurt](#who-can-be-hurt) · [Slowing movement is different from pinning](#slowing-movement-is-different-from-pinning)

## Placing it

The offer needs an Engineer with health above 10 and at least 1 TP. Completion
also checks pointer proximity and affordability, normally spends 1 TP and places
the wire at the mouse coordinates with a random rotation -20..+19. The selected
commendation waiver can avoid the debit after affordability passed.
[Construction](construction.md), [purchase details](../player-wire-evidence.md#purchase-and-placement)

## Who can be hurt

The inspected branch checks each indexed allied and enemy actor for a qualifying
point/shape intersection, health at least 1 and armor exactly 0. A successful
experience-dependent random comparison removes **1 health** and writes a new
wired value. An armored actor fails this particular eligibility test; that is not
a guarantee against every possible hazard.

Experience makes this one comparison harder to pass. The two sides use different
divisors: with supplied experience 30 and all other eligibility checks satisfied,
84 of 100 integer comparison inputs pass for an allied actor, versus 89 for an
enemy. These are conditional counts, not measured damage rates.
[Both-side checks](../player-wire-evidence.md#both-sides-are-checked),
[calculation and timing limits](../player-wire-evidence.md#declared-comparison-counts)

An [enemy Pioneer](enemy-pioneer.md) has a separate proximity branch that disables
active wire; its sabotage guard does not require an unwired state.

Plan friendly routes around wire as well as enemy approaches. A wired assignment
alone does not establish one universal slow duration for all units. Exact footprint,
activation, repeated damage timing and actor-specific movement remain unqualified.

Source: [Source identities](../player-notes/barbed-wire.md#citation-1). [Version and exact bindings](../player-wire-evidence.md)

## Slowing movement is different from pinning

A successful damage visit **replaces** the wired counter with a fresh 0–99 draw;
it does not add to the old value. A supplied old 80 and new draw 3 produces 3,
not 83; a draw of zero is also possible. Those are local writes, not tested
repeat-wire outcomes. [Counter assignment](../player-wire-evidence.md#a-fresh-wired-assignment-replaces-the-old-counter)

For the ordinary Allied soldier, a positive wired value skips its normal
destination step and decrements. The separate target-search block does not
repeat that wired check: slowing its movement is not a universal attack stop.
Pinning, health, morale, cover and the attack timer still have their own gates.
A value of one becomes zero in the skipped-step branch; it does not execute
the skipped step again on that same visit.
[Exact ordinary consumer](../player-wire-evidence.md#ordinary623-movement-consumes-wired-before-its-separate-action-block)
Additional source: [Source identities](../player-notes/barbed-wire.md#citation-2)
