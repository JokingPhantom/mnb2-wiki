[Player reference](README.md) · [Defenses](defenses.md) · [Construction](construction.md)

# Airborne improvised wall

A **3-TP airborne construction** with its own template and placement checks.
The command's message calls it a sandbag wall, but it creates **improvisedwall**;
the [Engineer's 1-TP sandbag wall](sandbags.md) is a separate object and command.
[Exact offer and output](../player-airborne-wall-evidence.md#the-selected-offer-and-normal-completion-both-require-3-tp)

1. **Select command.** An indexed Paratrooper with health above 10 and at least 3 TP
2. **Complete placement.** Rechecks a Paratrooper with health above 10, source distance strictly below 100 from the pointer, and current 3 TP
3. **Normal payment.** 3 TP; a later medal branch can waive the debit after affordability passes
4. **Created object.** improvisedwall at the mouse point, with a -5 through +4 rotation write

A Paratrooper at exactly 10 health fails these health checks. Exactly 100 fails
the selected pointer-distance check. The range is a source predicate, not a
measured on-screen build circle. The offer does not reserve payment or guarantee
the later Paratrooper/proximity check still succeeds.
[Placement and supplied boundary examples](../player-airborne-wall-evidence.md#placement-repeats-actor-and-affordability-checks)

Historical scope: selected **2.3.1g** source; the stated saves and placement
checks are conditional, not a certified protected layout.

On this page: [A free debit still counts as construction](#a-free-debit-still-counts-as-construction) · [Durability and protection still need the right query](#durability-and-protection-still-need-the-right-query)

## A free debit still counts as construction

The selected completion increments the building-event counter before testing
the medal waiver, and increments the career construction counter after its
creation request. An admitted waived wall therefore still has those counter
writes; removing it later does not turn that completion into an unbuilt event.
Keep this in mind when reading the [Guerilla award's counter condition](support-and-economy-awards.md).
This is not certification of a complete award run.

## Durability and protection still need the right query

Its load turns off the flammability flag. The selected blast-structure helper
nevertheless has a separate wall-removal branch for this exact type: after its
object intersection passes, 50 of 100 comparison inputs request removal.
That is a conditional branch, not a measured chance for every nearby blast.

The full drawing record now binds a named ordinary-cover child, character 582,
to this airborne wall. Engineer sandbags use the same child with a different
signed scale and translation. It feeds the ordinary-cover category when its
actual point test succeeds; it does not add an extra roll per overlapping wall.
Those distinct transforms do not establish identical protected geometry or a
higher save percentage for this wall. Use the [defense guide](defenses.md)
for the distinction between ordinary cover, bunker saves and actual overlap;
this card supplies no certified placement stencil for the airborne wall.
[Exact type and removal scope](../player-airborne-wall-evidence.md#exact-output-and-durability-boundary)

Sources: [Source identities](../player-notes/improvised-wall.md#citation-1)

[Exact ordinary-cover child and signed transform](../player-scenery-cover-evidence.md#airborne-and-engineer-walls-share-the-child-not-its-transform),
[scenery and other named-cover bindings](scenery-and-cover.md).
Additional source: [Source identities](../player-notes/improvised-wall.md#citation-2)
