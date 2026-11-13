[Player reference](README.md) · [Construction](construction.md) · [Explosives](explosives.md)

# Construction offers and placement

Choose a construction offer, then complete its placement requirements. Check the builder, proximity, pending action, available TP and intended object; selecting the offer does not finish the building. Engineer construction and airborne abilities have different actor requirements. [Construction evidence](../player-interaction-evidence.md#construction-and-explosives)

Historical scope: selected **2.3.1g** source.

On this page: [Choose a job, then complete the placement](#choose-a-job-then-complete-the-placement) · [Protection depends on the receiving helper](#protection-depends-on-the-receiving-helper) · [Construction counting is another receipt](#construction-counting-is-another-receipt)

## Choose a job, then complete the placement

For **selected historical 2.3.1g**, treat building as several steps:

1. Choose the offer for the job below and check its advertised cost.
2. Meet that offer's placement requirements, including the appropriate builder
   and proximity where required. A pending pointer is not a finished object.
3. Meet the completion-time payment or charge rules. Initial affordability need
   not reserve the TP; a possible waiver need not bypass the balance check.
4. Distinguish the created object from its later protection or active-state
   result. A visible defense alone does not certify the occupant's cover query.

The [construction evidence](../player-interaction-evidence.md#construction-and-explosives)
and individual cards separate these stages; do not apply one builder, radius or
fee rule to all offers.

| Offer                                             | Advertised TP | Job and important distinction                                                    |
| ------------------------------------------------- | ------------- | -------------------------------------------------------------------------------- |
| [Trench](trench.md)                               | 2             | Ordinary bullet-cover category                                                   |
| [Barbed wire](barbed-wire.md)                     | 1             | Separate slowing/damage hazard; qualifying troops on either side can be affected |
| [Three anti-personnel mines](mines.md)            | 1             | Grouped mine offer; triggers and later explosion recipients are separate         |
| [Antenna](radio-antenna.md)                       | 1             | Changes a failed radio-call retry path                                           |
| [Radar](radar.md)                                 | 3             | Can add delay to selected enemy support requests; not an AA gun                  |
| [Bunker](bunker.md)                               | 5             | Separate bunker protection where the attacker checks it                          |
| [Sandbag wall](sandbags.md)                       | 1             | Ordinary cover, sharing the category used by trenches                            |
| [Camouflage net](concealment.md)                  | 5             | Reconnaissance-sensitive concealment, separate from bullet saves                 |
| [TNT](tnt.md)                                     | 2             | Explosive with its own damage and scenery-removal paths                          |
| [Palisade](palisade.md)                           | 3             | Palisade classification; the selected normal completion instead charges 2 TP     |
| [Field HQ](field-hq.md)                           | 5             | Conditional income with a separate recorded-bonus repayment path                 |
| [Booby-trap explosive](booby-trap.md)             | 1             | Its own placement and detonation chain                                           |
| [Mortar pit](mortar-pit.md)                       | 4             | Named ordinary-cover shape; not an extra save per pit                            |
| [Pillbox](pillbox.md)                             | 5             | Bunker and palisade classifications, which can also restrict specialist actions  |
| [AT mine](mines.md)                               | 1             | Armored trigger includes friendly vehicles; later damage checks differ           |
| [Airborne improvised defence](improvised-wall.md) | 3             | Paratrooper placement, separate from Engineer sandbags                           |
| [Airborne sticky bomb](sticky-bomb.md)            | 2             | Paratrooper placement and later armored-follow path                              |

These are base menu prices, not measured completed builds or a promise all
scenarios expose every offer. Some paths can use a conditional fee waiver or
stored charge; a pointer is not proof a structure was built.

## Work one small build through to its result

A normal paid **Engineer 4 + sandbag wall 1 = 5 TP** gives a useful budget to
check. With an eligible Engineer already present, the wall is the separate
1-TP purchase. Assume no waiver or free allowance and verify the offer's builder,
proximity and completion-time affordability; do not count an uncompleted offer
as protection. [Complete building budgets](purchase-budgets.md#building-one-position-from-scratch).

After placement, check both outcomes: **was the intended structure created, and
does the intended soldier actually receive its protection?** These are different
questions. If placement does not finish, recheck the builder, pending choice,
proximity and TP against that structure's card. If a completed position does not
solve the problem, check the attacker and protected point before buying another
wall. A trench and wall still use one ordinary-cover category.

Before sheltering a specialist, check whether that protection blocks its job.
Use [defense comparisons](defenses.md) to choose the category and
[specialists under cover](specialists-under-cover.md) to keep the ability usable.
The [infantry-position study](strategy-studies.md#hold-an-infantry-position-without-disabling-its-support)
shows how those decisions fit together without claiming a safe layout.

## Protection depends on the receiving helper

Bunker classification recognizes bunker and pillbox intersections. Palisade
classification recognizes palisade and pillbox. Thus a pillbox can participate
in both helper families; it does not follow that every actor action allowed in
one protection context is allowed in the other.
[Officer aid](officer.md), [defense rules](defenses.md)

Trench and sandbags feed ordinary cover rather than a stack of one save per
construction. Camouflage queries instead depend on net overlap and shared
reconnaissance state. Drawings, flags, actual transformed hit tests and destruction
lifecycles are different pieces of the answer. [Concealment](concealment.md)

TNT scenery removal also has its own type/distance helpers, independent of the
explosion's ordinary damage/fragment arguments. A removed decoration, debris and
actual obstacle-clearance state still need their own qualification.
[Demolition](explosives.md), [scenery source](../scenery-demolition.md)

Sources: [Source identities](../player-notes/construction.md#citation-1). [Exact source notes](../player-interaction-evidence.md)

The [Pillbox](pillbox.md) offer has an indexed-type existence gate, while the
[Mortar pit](mortar-pit.md) exposes a named ordinary-cover child. Their exact
query forms, fee/waiver gates and placement limits have
[new source bindings](../player-construction-detail-evidence.md).

## Construction counting is another receipt

The Guerilla award's source counter changes at specific qualifying completion
branches, including improvised airborne defence. Its addition precedes the fee
waiver, so a waived build can still change that counter. Selected mine/TNT/sticky
completion paths differ from the twelve counted branches; do not infer the
award state solely from a menu category or an empty battlefield.
[Exact construction and vehicle-counter comparison](../player-guerilla-counter-evidence.md)
Additional source: [Source identities](../player-notes/construction.md#citation-2)

The [Bunker spacing/placement comparison](bunker.md#a-too-close-bunker-message-is-a-separate-placement-test)
distinguishes Engineer proximity, pointer-to-existing-Bunker spacing and the
clone's own load corrections. Passing one does not qualify every later
placement or protection query.

The [airborne improvised wall](improvised-wall.md) has a separate 3-TP offer and
completion, requiring a Paratrooper above 10 health and strict pointer-distance
below 100 at placement. Its object is improvisedwall; the Engineer's 1-TP
sandbagsmc price and protected shape should not be substituted for that path.
[Exact airborne receipt](../player-airborne-wall-evidence.md).
Additional source: [Source identities](../player-notes/construction.md#citation-3)

Read the separate [Radar](radar.md) and [Radio Antenna](radio-antenna.md) cards for
placement, active-state loss and the limits of their different support consumers.

[Original opening and evidence context](../player-notes/construction.md#opening-before-player-language-correction).
