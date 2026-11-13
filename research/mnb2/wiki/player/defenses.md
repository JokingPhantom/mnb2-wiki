[Player reference](README.md) · [Defenses](defenses.md) · [Support](support.md)

# Defenses: what stacks and what does not

**Trenches and sandbags supply ordinary cover; bunkers use a separate protection
query.** For several enemy firearm paths, an accurate shot can then be stopped
by a 50% ordinary-cover roll and a separate 75% bunker roll. If both queries
really succeed at the soldier's position, those two saves stop **87.5% of
otherwise accurate shots** in those paths. This is a conditional source result,
not a measured survival bonus for every layout or attacker.
[Protection evidence](../player-defense-evidence.md#bullet-saves)

Historical scope: selected **2.3.1g** source.

Find a protection question:

- [How do the save percentages combine?](#before-spending-tp-on-a-position)
- [Which structures add a separate save?](#choosing-and-combining-structures)
- What changes against [enemy Snipers](#an-important-exception-enemy-snipers) or [SS](#ss-uses-a-different-ordinary-cover-save)?
- [Do vehicle crews use these infantry saves?](#vehicle-crews-do-not-automatically-get-the-infantry-save-table)
- [Can cover restrict a specialist's own action?](#protection-can-restrict-a-specialists-own-action)
- [Can a blast remove a defense before checking its occupants?](#a-blast-can-request-structural-removal-before-checking-occupants)
- [What differs for the German Officer?](#the-german-officer-uses-a-separate-sixtyeighty-save-pair)
- [Does scenery count as cover?](#craters-and-some-scenery-templates-also-have-ordinary-cover-children)
- [Do outgoing shots use the same saves?](#the-incoming-save-table-is-not-automatically-reciprocal)
- [Can two saves give two defense-counter credits?](#two-successful-saves-are-one-counter-credit-in-these-paths)

## Choose protection you can complete and still use

For **selected historical 2.3.1g**, these normal paid examples start without an
Engineer and assume qualifying placement with no waiver. They are budgets, not
safe layouts or measured survival rankings.

| Intended job                | Full base commitment                           | Drawback to check                                                                  |
| --------------------------- | ---------------------------------------------- | ---------------------------------------------------------------------------------- |
| Add one ordinary-cover wall | Engineer 4 + sandbags 1 = **5 TP**             | Exact protected point and incoming attacker still matter.                          |
| Use a trench instead        | Engineer 4 + trench 2 = **6 TP**               | Wall and trench use one cover category; their shapes are not certified equivalent. |
| Add a separate bunker save  | Engineer 4 + bunker 5 = **9 TP**               | Protection can restrict particular specialist abilities.                           |
| Combine wall and bunker     | Engineer 4 + sandbags 1 + bunker 5 = **10 TP** | Both queries must actually succeed; explosives and attacker exceptions remain.     |

With an existing eligible Engineer, subtract its 4-TP recruitment cost from
these sums. Inspect [construction completion](construction.md) and
[specialist restrictions](specialists-under-cover.md), then use the
[infantry-position plan](strategy-studies.md#hold-an-infantry-position-without-disabling-its-support)
for adaptation triggers. The [instructional diagrams](instructional-visuals.md)
explain categories without certifying their placement geometry.

## Before spending TP on a position

For **selected 2.3.1g**, ask three questions:

1. **What is hitting the position?** The table below concerns particular enemy
   bullets. Snipers have an exception; explosions and flames use other rules.
   [Shooter and threat comparison](../player-defense-evidence.md#bullet-saves),
   [explosions and fortifications](explosions-and-fortifications.md).
2. **Am I adding a new protection category?** A second ordinary-cover structure
   does not add another ordinary-cover save. Bunker protection is a separate
   category when the attacker checks it. [Cover-query evidence](../player-defense-evidence.md#structure-bindings).
3. **Can the occupant still do its job?** Some protection checks also prevent a
   specialist action. Inspect the Medic, Officer, Bazooka or other role before
   choosing its position. [Specialists under cover](specialists-under-cover.md).

The prices and combinations below help compare purchases. Exact protected
placement is still unqualified: visible overlap alone does not prove that both
protection queries succeed at the soldier's point.

| Protection queries at the target  | Saved out of otherwise accurate shots | Unsaved |
| --------------------------------- | ------------------------------------- | ------- |
| Neither ordinary cover nor bunker | 0% from these saves                   | 100%    |
| Ordinary cover only               | 50%                                   | 50%     |
| Bunker only                       | 75%                                   | 25%     |
| Ordinary cover and bunker         | 87.5%                                 | 12.5%   |

The last row follows because only half the shots fail the cover save, and only
one quarter of those also fail the bunker save: 0.5 × 0.25 = 0.125 unsaved.
It does **not** mean damage is reduced by 87.5% on every bullet that gets through.
A miss, saved shot, zero-damage roll and lethal hit are different outcomes.

## Choosing and combining structures

| Construction                | Base TP | What the selected source binds                                  |
| --------------------------- | ------- | --------------------------------------------------------------- |
| [Trench](trench.md)         | 2       | Named ordinary-cover shape                                      |
| [Sandbag wall](sandbags.md) | 1       | Named ordinary-cover shape, transformed differently from trench |
| [Bunker](bunker.md)         | 5       | Bunker/pillbox overlap query; separate from ordinary cover      |

Other constructions belong to different query or hazard families:

| Construction                     | Menu TP      | Supported distinction                                                                                    |
| -------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------- |
| [Mortar pit](mortar-pit.md)      | 4            | Another named ordinary-cover child; not an extra roll per pit                                            |
| [Pillbox](pillbox.md)            | 5            | Recognized by bunker, palisade and pillbox classification helpers; each caller applies its own rule      |
| [Palisade](palisade.md)          | 3 advertised | Palisade classification, not a new ordinary-cover percentage; selected normal completion instead costs 2 |
| [Barbed wire](barbed-wire.md)    | 1            | Separate both-side unarmored damage/wired-state hazard                                                   |
| [Camouflage net](concealment.md) | 5            | Reconnaissance-sensitive concealment query, distinct from bullet saves                                   |

A qualifying Mortar pit and trench still feed the one ordinary-cover success
test. A Pillbox's overlapping classifications do not create one independent
bullet save per helper. They can also restrict an ability: for supplied Pillbox
classifications true, an Officer's earlier palisade-false entry gate fails before
its bunker random alternative can help. The Medic has different direct gates.
[Exact pit/Pillbox queries](../player-construction-detail-evidence.md),
[specialists under cover](specialists-under-cover.md)

Palisade's price discrepancy is a selected menu-versus-completion distinction;
Engineer, pointer, affordability and possible waiver checks still belong to
those separate stages. Wire and nets should not be inserted as another additive
percentage in the bullet-save table. Exact shapes, actual intersections and
lifecycle remain necessary for every construction.
[Payment evidence](../palisade.md), [wire](../player-wire-evidence.md),
[net/reconnaissance source](../reconnaissance-squad-check.md)

The following is a **conditional placement guide**, assuming the target actually
passes every query listed. It excludes other scenery and actor changes.

| Construction around the target | Result if those queries apply          |
| ------------------------------ | -------------------------------------- |
| No listed defense              | No save from these constructions       |
| Trench                         | One ordinary-cover save                |
| Sandbags                       | One ordinary-cover save                |
| Trench + sandbags              | Still one ordinary-cover save, not two |
| Bunker                         | One bunker save                        |
| Bunker + trench                | Ordinary-cover and bunker saves        |
| Bunker + sandbags              | Ordinary-cover and bunker saves        |
| All three                      | Same two save categories, not three    |

Why no extra roll for the second ordinary-cover structure? The cover helper
returns true as soon as a qualifying cover shape hits the soldier's point.
The shooter receives a yes/no answer, not a count of trenches or walls. Both
structures refer to the same underlying cover-shape character, but with different
transforms. Their visible art is not an exact placement stencil.
[Shape bindings and query limits](../player-defense-evidence.md#structure-bindings)

## An important exception: enemy snipers

The inspected German Sniper firing path has the ordinary 50% cover save but
**does not perform the 75% bunker save**. Bunker status alone therefore supplies
no save in that specific path. Ordinary cover still matters if its own query
succeeds. This does not mean the Sniper always hits: attempt, accuracy and damage
checks remain separate. [Shooter exceptions](../player-defense-evidence.md#bullet-saves)

The confirmed two-save pattern covers the selected ordinary German infantry,
Volkssturm, grenadier, machine-gunner, Hitlerjugend, Brandenburg, infiltrator and
scout firearm paths. The separately inspected [enemy paratrooper](enemy-paratroopers.md)
frame also has the 50/75 pattern. [Exact body](../player-enemy-para-evidence.md#target-acquisition-and-firearm-continuation)
Additional source: [Source identities](../player-notes/defenses.md#citation-1). It is not a rule for every tank gun, allied weapon, shell or
special attack in the game.

## SS uses a different ordinary-cover save

The selected [SS infantry](ss-infantry.md) shot has a 60% ordinary-cover save
and a separate 75% bunker save for an otherwise accurate shot at an unarmored
target. With both queries true and independent uniform draws, 90% are saved
and 10% remain unsaved in that path. This changes the save threshold, not the
number of ordinary-cover rolls supplied by overlapping structures.
[Exact SS save comparison](../player-enemy-ss-evidence.md#ss-bullet-saves-differ-from-the-ordinary-50-percent-path)
Additional source: [Source identities](../player-notes/defenses.md#citation-2)

## Bullets, blasts and concealment differ

Match the incoming threat before using the bullet-save matrix. The following
selected paths have different victim and protection rules:

- **[Named grenade/shared blast](../player-blast-core-evidence.md):** Core removal, fragment damage and AT handling have different armor/owner/bunker/distance gates

- **[Enemy flame component](../player-enemy-flame-evidence.md):** Its later shape-victim scan does not repeat ordinary-cover or bunker saves

- **[Flamer explosion](../flamer-explosion.md):** A generic blast is followed by separate burn-conversion scans, with different bunker/armor/range conditions

- **[Bazooka backblast](../player-backblast-order-evidence.md):** Its own launcher region, health/armor tests, injury and later navigation/counter writes are a separate path

- **[Camouflage net](../reconnaissance-squad-check.md):** Reconnaissance can disable the query's positive result without physically removing the net; it is not another ordinary-cover roll

For example, the cited flamer-explosion conversion has an unbunkered branch
with distance below 50 and a different alternative below 100 using the negation
of that bunker-false comparison, without the same local armor test. Those source
predicates are not a certified visible danger circle or a safe bunker placement.
The current structure query, earlier removal and each live recipient still matter.
[Exact conversion branches](../flamer-explosion.md), [collateral stages](collateral-damage.md)

A bullet saved by a structure does not certify immunity to another mechanism;
an effect touching its artwork also does not establish that every guarded
recipient branch succeeded. Keep the specific attack and actual query result
in the comparison while transformed geometry remains unresolved.
Additional comparison sources: [Source identities](../player-notes/defenses.md#citation-3)

The [enemy flamethrower](enemy-flamethrower.md) component scans qualifying
player points against its own shape without repeating ordinary-cover or bunker
saves. Its controller's target acquisition and the component's later victims
are separate tests. A missing bullet save does not certify which protected
positions intersect the flame shape.
[Exact component and victim actions](../player-enemy-flame-evidence.md#exact-flame-component-scans-players-not-just-the-selected-target)
Additional source: [Source identities](../player-notes/defenses.md#citation-4)

Exact boundary placements, transformed hit tests and destruction transitions
still need the shared mechanics reconstruction. The useful answer already
supported is that protection depends on **which queries succeed and which
shooter consumes them**, rather than a universal sum of structure bonuses.

Sources: [Source identities](../player-notes/defenses.md#citation-5).
[Exact rows and version identity](../player-defense-evidence.md)

The [German Sniper role card](german-sniper.md) connects its missing extra bunker
save with the separate attempt, rifle, ordinary-cover and damage stages.

<details>
<summary>Source detail: cover query return and caller success test</summary>

## Read the success test separately from the helper return

Ordinary cover is a yes/no success test, not a count of structures. Its point
query differs from bunker and palisade object-overlap tests.
[Exact return values, caller expression and named child](../player-defense-query-trace-098.md).

</details>

## Structure removal and occupant protection are separate

The selected explo2 effect calls a bunker/palisade-removal helper before its
general blast helper. The former tests structure type and its own strict
distance threshold; the latter applies separate recipient/protection rules.
An earlier successful bunker classification is not a stored immunity promise.
[Explosions and fortifications](explosions-and-fortifications.md).
Additional source: [Source identities](../player-notes/defenses.md#citation-6)

## Vehicle crews do not automatically get the infantry save table

For the selected enemy Regular shot, ordinary-cover/bunker saves belong to its
unarmored recipient alternative. Its armor 1 crew branch uses different role
checks without repeating those saves. A true protection query alone does not
justify applying 87.5% to that crew attempt.
[Incoming crew-path comparison](small-arms-against-vehicles.md#incoming-regular-bullets-use-a-different-crew-table).
Additional source: [Source identities](../player-notes/defenses.md#citation-7)

## Protection can restrict a specialist's own action

Compare [specialist abilities under cover](specialists-under-cover.md) before
placing support roles: the Mechanic, Officer and Medic have different selected
entry checks. A Pillbox's combined classifications can fail an earlier ability
gate even where a separate bunker random branch exists. That action question
is distinct from how an incoming bullet is saved.

## A blast can request structural removal before checking occupants

The selected shared blast helper calls AT handling, then conditionally calls
bunker/palisade removal before its later enemy/player protection queries. Mine
and AT-mine tags admit that structural dispatch. The frag and air tags skip
that particular call; earlier AT handling is outside that condition.

A later bunker query uses the current indexed structures. It does not preserve
a building's pre-blast protection result after actual removal. This is a source
ordering fact, not a guaranteed occupant death or a measured safe blast radius.
[Exact dispatch, types and remaining state inputs](../player-blast-dispatch-evidence.md)
Additional sources: [Source identities](../player-notes/defenses.md#citation-8)

[Collateral-damage guide](collateral-damage.md) compares backblast, blast owner
exclusions and flame conversions that the infantry bullet-save table does not describe.

[Line of sight and smoke](line-of-sight.md) are distinct from the save table: a
sampled obstacle query, a protection query and a later damage path answer different questions.

Additional construction-family sources: [Source identities](../player-notes/defenses.md#citation-9)

## Some enemies exclude a protected infantry target during search

With a qualifying Pillbox query, the selected Regular enemy search rejects an
otherwise eligible **unarmored** candidate at its armor/Pillbox test. The German
Sniper search has no Pillbox query there. The enemy rocket soldier's ordinary
fallback has a Pillbox exclusion, but its earlier armored-first scan does not.
A light vehicle with positive driver+gunner also has a different Regular
candidate alternative from unarmored infantry.

These are fresh-search filters, separate from bullet saves and later damage.
They do not establish a safe vehicle position, universal invisibility, one-way
fire or cancellation of an attack already underway.
[Exact three-enemy candidate comparison](../player-pillbox-target-evidence.md).
Additional source: [Source identities](../player-notes/defenses.md#citation-10)

## A missed enemy shot uses another pin request

In the selected Regular-enemy shot, ordinary-cover and bunker saves belong to
the **accurate** unarmored branch. Its missed-shot alternative instead has a
current-target morale comparison and health-above 10 requirement, then requests
a pinned animation without an explicit pin-field assignment in that caller.
Those save percentages are not a reduction factor for this separate request.

The ordinary target's later recovery/action writers and actual label dispatch
remain separate. A supplied health 11/morale 20/comparison 21 reaches the local
request; health 10 does not. This is not a measured pin, duration, protection
failure or safe cover layout.
[Exact caller, label strings and later state boundaries](../player-incoming-pin-evidence.md).
Additional source: [Source identities](../player-notes/defenses.md#citation-11)

## The German Officer uses a separate sixty/eighty save pair

The inspected German Officer firearm branch uses **60% ordinary-cover and 80%
bunker saves** for an otherwise admitted accurate shot at an unarmored target.
If both actual protection queries succeed and the save draws are independent
uniform integers, 92% are saved and 8% remain unsaved in that branch. It differs
from the common 50/75 pair and the SS 60/75 pair without adding a save per overlapping
ordinary-cover shape.

The selected accuracy condition also requires source distance strictly below 200;
its unsaved health draw is 0–49. Those are source gates and a conditional save
comparison, not a 92% reduction in every health loss or a safe placement guide.
[Exact Officer body, strict range and declared query/draw counts](../player-enemy-firearm-damage-evidence.md#the-german-officer-has-sixtyeighty-saves-and-a-strict-range-gate).
Additional source: [Source identities](../player-notes/defenses.md#citation-12)

## Craters and some scenery templates also have ordinary-cover children

The finite direct drawing inventory contains named ordinary-cover children in
crater, crate-shaped and barrel definitions as well as the constructions. The
helper reads the named child and its point test rather than requiring the parent
to be a trench. A qualifying listed child can therefore feed the same ordinary-
cover category, without a new save roll for each overlapping prop.

The [airborne improvised wall](improvised-wall.md) has its own such binding. It
uses the same underlying child as Engineer sandbags with a different signed
matrix; its 3-TP cost does not establish a stronger save or identical coverage.
The source crate-shaped character 1579 binding also does not resolve the separate same-name
836 arrival/reward object. Read the [scenery comparison](scenery-and-cover.md)
for exact scope. Actual transformed overlap and surviving state remain inputs.
[Finite eight-placement inventory and reader](../player-scenery-cover-evidence.md).
Additional sources: [Source identities](../player-notes/defenses.md#citation-13)

The [crater lifetime comparison](../player-crater-lifetime-evidence.md) separates
three load counters from later fading/removal and the cover query. Shared crater
artwork does not certify one fixed cover duration or a safe final moment.
Additional source: [Source identities](../player-notes/defenses.md#citation-14)

A selected [scenery refresh](../player-scenery-refresh-evidence.md) can remove
life-defined non-frag entries through another admitted path, and its snapshot
copies only one parent scale into both restored axes. Neither an object's own
life counter nor a saved decoration entry certifies unchanged later cover.
The exact gates, source indices and actual transformed point query still matter.
Additional source: [Source identities](../player-notes/defenses.md#citation-15)

A common ordinary-cover child also does not imply a common destruction rule.
The selected crate-shaped character 1579 load uses type tree, so an admitted blast scenery
query selects the tree branch rather than the Sandbag's local removal choice.
That branch's requests, dynamic replacement name and actual post-removal cover
still need their own qualification.
[Exact type-versus-cover comparison](../player-tree-tagged-crate-evidence.md).
Additional source: [Source identities](../player-notes/defenses.md#citation-16)

## The incoming save table is not automatically reciprocal

The inspected outgoing shared infantry firing helper and direct Gunner shot
body do not ask for ordinary-cover or bunker saves. The named incoming Regular,
SS and German Sniper bodies use the different save paths described above.
Do not automatically give an enemy the same extra rolls because its drawing
looks protected, or assume all weapons on both sides use one cover routine.

That does not prove a one-way firing position: acquisition can still require
line of sight, actual structures/obstacles need their own transformed queries,
and other attack paths differ. A valid selected target and a later shot body
are separate stages. [Exact five-body comparison and supplied reader examples](../player-defense-evidence.md#incoming-and-outgoing-shot-bodies-do-not-mirror-the-same-cover-saves).
Additional sources: [Source identities](../player-notes/defenses.md#citation-17)

## Two successful saves are one counter credit in these paths

The inspected Regular and SS firing bodies keep one saved flag. Ordinary cover
and bunker can each set it, but a later common saved branch adds **one** to the
defense counter. Two successful saves on that selected shot do not add two there;
a bunker-only success can also add one.

Results copy that counter into their defended field. It is not a count of
trenches or proof that a displayed total represents distinct soldiers rescued.
Actual shot/target callbacks and result rendering remain separate from these
source writes. [Exact four supplied save pairs and result reader](../player-defense-evidence.md#two-successful-saves-do-not-add-two-defense-counter-credits-here).
Additional source: [Source identities](../player-notes/defenses.md#citation-18)
