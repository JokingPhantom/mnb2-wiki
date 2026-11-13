[Player reference](README.md)

# Line of sight, cover and smoke answer different questions

A soldier can be hidden, protected or unable to see a target for different
reasons. In selected historical **2.3.1g**, the line-of-sight helpers sample obstacle shapes;
ordinary cover, bunker classification and camouflage use other queries. A
visible cloud or wall is not one universal accuracy penalty.
[Exact sight helper](../line-of-sight-sampling.md), [query comparison](../cover-and-sight.md)

- **Can this soldier see a candidate target?:** Sampled obstacle checks answer a particular sight query; the actor's other target filters still matter

- **Does a wall or cloud automatically give a bullet save?:** No. Ordinary-cover and bunker saves are separate from a sight obstacle, and apply only in the relevant shooter paths

- **Does a camouflage net conceal this position?:** Its own net-intersection query, gated by shared reconnaissance state; not the same rule as a smoke obstacle

- **Will new smoke immediately cancel an attack already underway?:** Acquisition and later firing are separate visits; the inspected shared shot does not repeat every sight filter, so immediate cancellation is not established

- **Can the later blast hurt the actor anyway?:** Its AT/core/fragment/protection/recipient checks are separate from the earlier sight result

Passing one row does not settle the others. [Defenses](defenses.md),
[concealment](concealment.md), [explosion stages](explosion-damage-stages.md)

For a shot that seems to cross an obstacle, first separate **new target selection**
from an attack that already had a target. Then check the named actor/weapon and
the particular obstacle query. The source distinctions below explain possible
causes; they do not diagnose a screenshot or certify a way to shoot through smoke.
[Acquisition and later-reader evidence](../player-repeat-state-evidence.md#shared-shot-accounting-does-not-repeat-all-acquisition-filters).

On this page: [Sight uses discrete samples](#sight-uses-discrete-samples) · [Caller direction can matter](#caller-direction-can-matter) · [Smoke must reach the right query with the right object](#smoke-must-reach-the-right-query-with-the-right-object) · [A target search and a later shot are separate visits](#a-target-search-and-a-later-shot-are-separate-visits)

## Sight uses discrete samples

The selected helpers divide distance by 30 and visit positive integer sample
indices up to that value. For the supplied positive finite distances below, the maximum visit count is the whole-number part of distance ÷ 30, before any early blocked return. Their source uses 30-unit steps, not a continuous
intersection test through every point of the segment. With supplied exact
finite distances and no early blocked return:

| Supplied distance | Maximum sampled visits |
| ----------------- | ---------------------- |
| 29                | 0                      |
| 30                | 1                      |
| 89                | 2                      |
| 90 or 91          | 3                      |

These are source-arithmetic examples, not calibrated on-screen placements or
proof a nearby obstacle can be ignored in play. Actual transforms, numeric
boundaries, object state and caller admission still need qualification.
The helper returns false when a sampled point hits an indexed obstacle shape;
after its loops it returns true. That result alone does not acquire a target,
fire a projectile or guarantee damage.
[Loop bounds and tested-point order](../line-of-sight-sampling.md#the-tested-coordinate-advances-before-the-shape-query)

## Caller direction can matter

Some orders and actor scans supply the endpoints in different directions. For
an **ideal exact one-dimensional 89-unit segment**, 30-unit steps from one end
sample positions 30 and 60; starting at the other end samples 59 and 29 in the same
coordinate system. Those are different sample grids because the endpoint
remainder is not a full step.

This illustration does not qualify an actual asymmetric shot or a tactic to
shoot through a particular wall. It explains why reversing arguments should
not be silently treated as an identical query. The actual geometry and source
numeric behavior remain open. [Exact caller and inputs](../line-of-sight-sampling.md#caller-direction-can-change-an-ideal-sample-grid),
[retargeting orders](retargeting-orders.md)

## Smoke must reach the right query with the right object

The selected smokescreen has a physical obstacle child, so it can participate
in sampled sight **when its indexed object and transformed sample intersection
qualify**. It does not add an ordinary-cover save merely because smoke art is
visible. The cloud's own fade/opacity and sight eligibility are different reads.
[Exact smoke component](../player-smokescreen-evidence.md#the-small-blast-and-later-cloud-are-distinct-actions)

Its emission name and sight-scan bound also differ. The cloud uses a decoration
name based on decoration count plus garbage count; the sight helper scans names
only through current decoration count. For supplied stable decoration count 10,
a cloud named deco10 is in that query's 0..10 index names, while deco15 is not.
That is conditional index membership, not a reproduced smoke-failure bug or a
claim the first cloud definitely blocks a target. Same-name objects, later
counter changes and actual intersections remain inputs.
[Exact name/bound example](../player-smokescreen-evidence.md#emission-name-and-sight-scan-bound-must-be-joined)

The sight helpers do not read cloud life or opacity as their skip condition.
A fading cloud therefore does not, by itself, prove its obstacle is already
absent from the query. Actual removal and callback order still matter.
[Smoke lifetime and opacity](../player-smokescreen-evidence.md#lifetime-and-opacity-are-not-a-sight-disable-flag),
[Smoke request and payment](smoke.md)

## A target search and a later shot are separate visits

The ordinary soldier's admitted target scan checks sight alongside health,
visibility, distance and other eligibility. Its later shared firing helper does
not repeat every acquisition filter: the inspected complete body has no fresh
sight query. It reads the current target and helper distance for that visit.

This does not prove an actual soldier fires through newly placed smoke or a
new wall. The target must remain valid, the firing action must be reached and
all intervening callbacks still matter. It does show why a new obstacle cannot
be described as a guaranteed immediate cancellation from these source sites
alone. [Repeat versus later readers](../player-repeat-state-evidence.md#shared-shot-accounting-does-not-repeat-all-acquisition-filters),
[shooting stages](how-shooting-works.md)

Sources: [Source identities](../player-notes/line-of-sight.md#citation-1). Original synthesis of exact existing notes; no new geometry,
visibility, smoke-failure, shot or timing trial.

The [scenery comparison](scenery-and-cover.md) binds selected tree/rock/haystack
obstacle children separately from named ordinary-cover children in other props.
That distinction follows actual source child names and reader forms; it does
not infer a visible protected region or movement clearance from the artwork.
[Exact direct-child and helper scope](../player-scenery-cover-evidence.md).
Additional source: [Source identities](../player-notes/line-of-sight.md#citation-2)
