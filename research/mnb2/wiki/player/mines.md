[Player reference](README.md) · [Construction](construction.md) · [Explosives](explosives.md)

# Ordinary mines and AT mines

**An AT mine changes the trigger filter, not the selected AT-radius argument.**
Both mine effects pass AT radius 50; ordinary mines can be triggered without an
armor requirement, while the AT mine's selected trigger requires positive armor.
Both can consider friendly entries.
[Exact trigger and effect comparison](../player-mine-effect-evidence.md)

| Offer          | Base cost | Placements requested on admitted completion | Extra trigger armor requirement         |
| -------------- | --------- | ------------------------------------------- | --------------------------------------- |
| Ordinary mines | 1 TP      | Three ordinary mines                        | None in the selected trigger predicates |
| AT mine        | 1 TP      | One AT mine                                 | Candidate armor above 0                 |

The offers and later placement need an eligible Engineer; mouse completion also
checks strict pointer-to-Engineer distance below 100. Payment and the creation
requests happen later than selecting the offer. A conditional medal waiver has
its own test. These are source-bound transactions, not a guarantee that every
request produces a lasting mine in every mode.
[Offer, completion and counters](../player-mine-placement-evidence.md)

For a purchase decision, the useful distinction is **three ordinary placement
requests versus one armored-trigger mine**, with different trigger filters.
Both later effects still pass AT radius 50. Neither offer is a certified safe
barrier or a no-friendly-fire option. [Exact trigger/effect comparison](../player-mine-effect-evidence.md).

Historical scope: selected **2.3.1g** source.

On this page: [Friendly troops and vehicles can trigger them](#friendly-troops-and-vehicles-can-trigger-them) · [Same AT input, different fragment input and tag](#same-at-input-different-fragment-input-and-tag) · [A set of three and one construction event are different counts](#a-set-of-three-and-one-construction-event-are-different-counts)

## Friendly troops and vehicles can trigger them

At strict helper distance below 25, the ordinary mine's selected player trigger
needs health at least 10 and explicitly defined; the enemy trigger needs health
above 0. AT adds positive armor to both. Thus allied health 9 fails that player
health test, while enemy health 9 passes the enemy health part. A living friendly
armored vehicle is not automatically excluded from the AT trigger.

Triggering creates the effect at the mine's point, rather than copying the
triggering actor's current point into the explosion. Later damage has its own
recipient and protection tests; a passed trigger does not promise that actor
is killed or everyone else is safe. These source distances are not certified
visible safe spacing. [Exact points and guards](../player-mine-effect-evidence.md#the-effect-is-placed-at-the-mines-point)

## Same AT input, different fragment input and tag

| Selected effect input or tag | Ordinary mine | AT mine |
| ---------------------------- | ------------- | ------- |
| AT input                     | 50            | 50      |
| Fragment input               | 75            | 100     |
| Ordinary damage input        | 100           | 100     |
| Literal tag                  | mine          | naval   |

These values have different roles in the later helper. Damage input 100 is not
100 guaranteed health lost, and the AT mine's larger fragment input does not
make its AT input larger than the ordinary mine's. Both have separate scenery,
core, AT and fragment work. [Effect arguments and owner limits](../player-mine-effect-evidence.md#effect-arguments-retain-different-roles-and-tags),
[AT guards](anti-tank-and-vehicles.md), [blast stages](explosion-damage-stages.md)

## A set of three and one construction event are different counts

The ordinary completion requests three mine positions but increments the career
construction counter once. Its three source emissions also have separate
medal-dependent booby-trap writes. The AT completion has one emission, one such
conditional write and one construction increment. The selected branches do not
use the wall-building event-counter increment; that is separate from career
construction. [Exact site comparison](../player-mine-placement-evidence.md#the-ordinary-branch-has-three-creation-and-medal-sites)

[Pioneer/booby-trap interactions](../booby-trap.md) and actual mine removal have
other guards. The trigger bodies request removal inside their scans; complete
callback/removal behavior is still needed before promising one and only one
effect in every case.

Sources: [Source identities](../player-notes/mines.md#citation-1). Selected publisher-associated 2.3.1g; later additions remain candidates.

Ordinary and AT mine effects request different named crater aliases before their
blast calls. Those crater objects, load counters and visible drawings remain
separate from the effects' equal AT 50 inputs and different fragment arguments.
[Exact actual effect-to-crater comparison](../player-crater-lifetime-evidence.md#five-selected-effects-request-different-crater-aliases-before-their-blast-call)
Additional source: [Source identities](../player-notes/mines.md#citation-2)
