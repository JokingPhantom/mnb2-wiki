[Player reference](README.md) · [Defenses](defenses.md) · [Construction](construction.md)

# Sandbag wall

A **1-TP engineer construction** with an ordinary cover shape. A soldier that
passes its cover query can receive one **50% save against an otherwise accurate
shot** in the inspected cover-using enemy firearm paths. It is not a universal
50% reduction to damage from every attack. [Defense rules](defenses.md)

| Property                  | Selected 2.3.1g source finding                               |
| ------------------------- | ------------------------------------------------------------ |
| Base price                | 1 TP                                                         |
| Protection                | Ordinary cover; not the bunker category                      |
| Completion                | Pending wall cue, proximity state and affordability required |
| Normal completion fee     | 1 TP; a conditional career-medal branch can waive the debit  |
| Initial flammability flag | Off; not proof of indestructibility                          |

Historical scope: selected **2.3.1g** source; the stated saves and placement
checks are conditional, not a certified protected layout.

On this page: [Combining defenses](#combining-defenses) · [Durability and limitations](#durability-and-limitations) · [A selected blast path can remove the wall](#a-selected-blast-path-can-remove-the-wall) · [The airborne wall is a separate command](#the-airborne-wall-is-a-separate-command)

## Combining defenses

Sandbags and a trench both contribute to the same yes/no ordinary-cover query.
Overlapping them does not add a second ordinary-cover roll. A bunker uses a
separate query and can add a separate save for applicable shooters. That
combination is **conditional on both queries succeeding**, not a promise that
any placement of the two drawings protects a nearby soldier.
[Full stacking table and enemy Sniper exception](defenses.md)

The selected sandbag template has a named cover shape transformed differently
from the trench's, even though both reference the same underlying character.
Thus a wall's appearance and the trench's appearance should not be used to
assume identical coverage at an arbitrary point.
[Bound shape identities](../player-defense-evidence.md#structure-bindings)

## Durability and limitations

The community describes sandbags as destructible and recommends combining them
with other defenses. The source load turns off the flammability field; that
single flag does not establish immunity to explosives or every removal path.
Protection after damage or destruction still needs lifecycle qualification.
[Sandbag research](../trenches-and-sandbags.md)

For selecting between structures, the supported comparison is the 1-TP wall's
ordinary-cover category versus the 2-TP trench's same category and the 5-TP
bunker's separate category. Longevity, exact protected area and build convenience
remain relevant but are not certified equal by those prices.

Sources: [Source identities](../player-notes/sandbags.md#citation-1).
[Evidence and version identity](../player-defense-evidence.md)

See [explosions and fortifications](explosions-and-fortifications.md) for the
separate structure-removal and occupant-protection queries.

## A selected blast path can remove the wall

The common blast's first scenery helper tests the **effect object against the
wall object**, then admits Sandbag/improvised-wall removal on a random 0–99
comparison below 50. This branch does not require flammability or a prior wall
health subtraction. It runs before the separate bunker-removal dispatch, so
the latter's frag/air exclusion does not also exclude this Sandbag branch.

That is a source choice after a successful object test, not a measured 50%
destruction rate for every explosion on screen. After actual removal, ordinary
cover needs another surviving qualifying shape; an overlapping Trench can only
supply that match if its own current query still succeeds. It does not add an
extra ordinary-cover save.
[Exact first helper and post-removal inputs](../player-blast-dispatch-evidence.md#the-first-helper-also-handles-sandbags-and-support-structures)
Additional source: [Source identities](../player-notes/sandbags.md#citation-2)

## The airborne wall is a separate command

The [3-TP airborne improvised wall](improvised-wall.md) requires a nearby
Paratrooper at completion and creates another named template. Its command
message also says sandbag wall. That wording does not make this 1-TP Engineer
price or cover-shape binding apply to both constructions.
[Exact airborne object and payment](../player-airborne-wall-evidence.md).
Additional source: [Source identities](../player-notes/sandbags.md#citation-3)
