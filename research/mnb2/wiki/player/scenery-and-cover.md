[Player reference](README.md)

# Scenery, ordinary cover and obstacles

Certain craters, crate-shaped props and barrels **can qualify as ordinary cover**. The inspected tree, rock and haystack templates instead supply sight-obstacle inputs. Actual objects and overlap still matter: visible scenery does not supply one universal protection rule. Historical scope: selected **2.3.1g**. [Exact accepted bindings and source/version](../player-scenery-cover-evidence.md)

| Scenery or construction               | Ordinary-cover input                                | Separate limit                                           |
| ------------------------------------- | --------------------------------------------------- | -------------------------------------------------------- |
| Trench, Engineer sandbags, Mortar pit | Named ordinary-cover child                          | Actual point must pass the query                         |
| Airborne improvised wall              | Same child category                                 | Its transform differs from Engineer sandbags             |
| Selected craters                      | Named ordinary-cover child                          | Actual overlap and lifetime still matter                 |
| Selected crate-shaped prop            | Named ordinary-cover child                          | Not the same source identity as the arrival/reward crate |
| Selected barrels                      | Named ordinary-cover child                          | No tested safe position or survival guarantee            |
| Selected trees, rocks and haystacks   | No direct named ordinary-cover child in these lists | Obstacle input answers a separate sight question         |

[Exact original identifier table](../player-scenery-table-trace-099.md).

These are selected direct source bindings, not a census of live battlefield
objects or a guarantee every point inside a drawing passes a test. The full
[direct-placement inventory](../player-scenery-cover-evidence.md#the-full-named-cover-inventory-contains-eight-direct-placements)
retains exact characters, aliases and signed matrices.

On this page: [Ordinary cover is one successful query](#ordinary-cover-is-one-successful-query) · [The airborne wall does not copy the Engineer wall's footprint](#the-airborne-wall-does-not-copy-the-engineer-walls-footprint) · [Destruction needs its own state](#destruction-needs-its-own-state) · [Crater drawing, fading and removal are separate stages](#crater-drawing-fading-and-removal-are-separate-stages) · [The visible crater is a separate object from the blast](#the-visible-crater-is-a-separate-object-from-the-blast) · [A refresh pass is not a complete copy of the same cover](#a-refresh-pass-is-not-a-complete-copy-of-the-same-cover) · [A crate-shaped prop can use a tree destruction rule](#a-crate-shaped-prop-can-use-a-tree-destruction-rule) · [Can a barrel explode or survive a blast?](#can-a-barrel-explode-or-survive-a-blast) · [Rocket triggers use another type list](#rocket-triggers-use-another-type-list)

## Ordinary cover is one successful query

The cover helper scans named cover children and returns on its first successful
point test; it does not require the parent to be a trench or sandbag. A qualifying
crater or other listed cover child can therefore feed the same category.
The attacker still has its own shot, armor and save rules.

Several overlapping matches do not produce a new ordinary-cover roll per object.
A bunker save is another query in applicable firearm paths, while line of sight,
concealment and later blast protection are separate. A crate or barrel drawing
is not a certificate that those other tests succeed.
[Defense stacking](defenses.md), [line of sight](line-of-sight.md)

## The airborne wall does not copy the Engineer wall's footprint

The [3-TP airborne wall](improvised-wall.md) and [1-TP Engineer sandbag wall](sandbags.md)
share the underlying ordinary-cover child but use different signed scales and
translations. Their prices, eligible builder and actual protected footprint
should not be collapsed into one identical wall. This is source binding, not a
native placement stencil or a higher cover-save percentage for the dearer offer.
[Exact matrices and receipt distinction](../player-scenery-cover-evidence.md#airborne-and-engineer-walls-share-the-child-not-its-transform)

## Destruction needs its own state

A flammability flag, a named obstacle and a cover child answer different
questions. [TNT](tnt.md) has separate rock/bunker/palisade removal predicates;
[fire](fire-and-burning.md) and other blasts use other consumers. After a source
removal request, actual surviving objects and their later queries still need
qualification before promising a clear path or protected space.

[Crate rewards](crates.md) remain a separate arrival/collection question. The
cover record for 1579 does not resolve the existing same-name 836/1579 dispatch
boundary or make every supply crate proven cover.

Sources: [Source identities](../player-notes/scenery-and-cover.md#citation-1). Selected publisher-associated 2.3.1g; no new native geometry trial.

## Crater drawing, fading and removal are separate stages

Three selected crater placements share the same drawing, but their load counters
are 1000 for cratere, 500 for cratere2 and 1000 for cratere4. Their nonstock
callbacks decrement first, assign opacity only once the new life is below 100,
and request removal at exact zero. One universal crater duration would erase
those source differences and any later caller overrides.

With entry life 101, a reached callback writes 100 without that opacity write;
with entry 100 it writes life 99 and opacity 99. Entry 1 writes zero and requests
removal. Those are supplied source transitions, not time in seconds or a measured
last cover event. The callback bodies have no local pause test, but host delivery
and actual pause behavior still need qualification.

The ordinary-cover helper does not locally test the crater parent's life or
opacity. That does not establish protection after fading or removal: actual
object presence, shape query and callback order remain inputs.
[Exact aliases, boundaries and conditional visit counts](../player-crater-lifetime-evidence.md).
Additional source: [Source identities](../player-notes/scenery-and-cover.md#citation-2)

## The visible crater is a separate object from the blast

The selected Bazooka and mortar effects request cratere2, while TNT and ordinary
mine effects request cratere and the AT mine requests cratere4. Those requests
copy the effect's point and a random rotation before a later blast-helper call.
They do not locally set the crater's life or scale.

The later helper receives the original effect's source receiver and its own
AT/fragment/damage inputs. A crater's drawing or load counter is therefore not
a calibrated blast-radius or damage gauge. For example, the selected ordinary
and AT mine effects both pass AT 50 but request different crater aliases; the
500-counter cratere2 load is separate from the Bazooka's 500-health Tiger exception.
[Exact five-body caller, alias, counter and receiver map](../player-crater-lifetime-evidence.md#five-selected-effects-request-different-crater-aliases-before-their-blast-call)

## A refresh pass is not a complete copy of the same cover

The selected late-wave scenery pass has a removal branch for scanned entries
with defined life and a supplied non-frag type, without saving them for its
rebuild. A positive crater life counter therefore is not by itself a guarantee
against every other source removal path. This is a separately admitted branch,
not a promise about every crater's current type, cleanup cadence or actual lifetime.

Its other snapshot path copies seven selected keys rather than the whole object.
Only parent x-scale is saved as scalez and then restored to both axes. With
supplied old 80/120 parent scales, the selected new writes become 80/80. Those field
writes do not prove a particular change in physical cover area, and they do not
replace the exact signed child transforms bound earlier. Actual template,
load/order, availability and shape queries remain necessary.
[Exact index/flag gates and source field-transfer comparison](../player-scenery-refresh-evidence.md).
Additional source: [Source identities](../player-notes/scenery-and-cover.md#citation-3)

## A crate-shaped prop can use a tree destruction rule

The selected 1579 crate-shaped scenery load sets its type to tree, while its direct
cover child still feeds the ordinary-cover query. Those facts are compatible:
the cover reader uses the child, while a blast scenery helper chooses a branch
from the current type. This is separate from the same-name 836 arrival/reward path.

For that unchanged type and an admitted object intersection, treeKill requests
wood/dead-template replacements and contains a tree-counter increment and
original removal request. It does not use the Sandbag branch's local below 50
choice. Actual lookup and continuation remain unresolved: the constructed
replacement name deadcratemc has no exact row in the accepted template map.
This is a source boundary, not a verified failure or a guarantee of replacement
cover. [Exact load, type, field writes and name scope](../player-tree-tagged-crate-evidence.md).
Additional source: [Source identities](../player-notes/scenery-and-cover.md#citation-4)

The prop burn helper also uses a different query form from blast object overlap
and ordinary cover: it tests the effect shape at the prop's point. Its selected
tree/template gate does not read the flamable field locally. Those exact source
readers should stay separate when reasoning about a burning or removed prop.
[Burn/blast/cover receiver forms](../player-tree-tagged-crate-evidence.md#burn-blast-and-ordinary-cover-use-different-query-forms)

The selected burning-tree replacement has a direct obstacle child and no direct
named covermc in its five-record drawing inventory. Its frame 21 removes the
fire-child depth and changes obstacle transform fields. These records do not
measure ordinary cover or the callback's separate distance hazard.
[Replacement child inventory and transform limits](../player-tree-tagged-crate-evidence.md#direct-burning-tree-children-and-terminal-drawing-records)

## Can a barrel explode or survive a blast?

The inspected barrel drawings bind ordinary-cover children, but their retained
profiles do not supply a current destruction type or a complete spawn/load path.
The common scenery helper follows the object's current type, with a crate
explosion branch and a different tree replacement branch. It has no barrel-named
alternative. None of that proves explosive barrels, blast immunity or a safe
position beside one. An actual live object and a successful later cover query
are still needed before treating the drawing as protection.
[Exact barrel profiles, finite source search and supplied-type comparison](../player-scenery-cover-evidence.md#barrel-cover-does-not-supply-a-destruction-type).

Additional source: [Source identities](../player-notes/scenery-and-cover.md#citation-5)

## Rocket triggers use another type list

The [Bazooka terrain scan](bazooka.md#scenery-can-trigger-a-rocket-without-being-ordinary-cover)
uses a separate type/distance predicate. A loaded rock can satisfy its type test
without a direct ordinary-cover child; an Engineer sandbag's cover child does
not put its parent type in that list. Keep movement blockage, proximity trigger,
ordinary cover and later blast damage as separate questions.

[Original opening and evidence context](../player-notes/scenery-and-cover.md#opening-before-player-language-correction).
