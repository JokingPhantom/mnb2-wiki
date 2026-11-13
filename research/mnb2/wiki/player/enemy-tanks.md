[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Panther and Tiger tanks

Panther and Tiger tanks have **separate hull and weapon stats**. Their cannons use similar impact-placement rules, but hull health, hull experience, action timers and extra machine-gun components differ.
[Exact hull/component identities](../player-enemy-tank-evidence.md)

Historical scope: selected **2.3.1g**.

| Selected load            | Panther | Tiger |
| ------------------------ | ------- | ----- |
| Starting hull health     | 1000    | 3000  |
| Armor code               | 2       | 2     |
| Hull experience          | 0       | 20    |
| Cannon-turret rifle      | 1       | 1     |
| Cannon-turret experience | 2       | 2     |
| Initial moving counter   | 100     | 100   |

These are load values, not final durability or firing intervals. Armor 2 is a
class, not percentage reduction, and the Tiger's hull XP is not its turret XP.
[Enemy vehicle overview](enemy-vehicles.md)

On this page: [Target order can matter before the cannon choice](#target-order-can-matter-before-the-cannon-choice) · [The range write is not the cannon's scatter formula](#the-range-write-is-not-the-cannons-scatter-formula) · [Machine-gun components need their own readers](#machine-gun-components-need-their-own-readers) · [Incoming AT damage is another path](#incoming-at-damage-is-another-path) · [Bazooka AT damage is not necessarily the last health write](#bazooka-at-damage-is-not-necessarily-the-last-health-write) · [Front-armor values do not establish a percentage or weak-point rule](#front-armor-values-do-not-establish-a-percentage-or-weak-point-rule) · [The Tiger's extra gunner has its own shot and retarget rules](#the-tigers-extra-gunner-has-its-own-shot-and-retarget-rules)

## Target order can matter before the cannon choice

The turret scan first requires a closer eligible target, then stops its indexed
scan early after accepting positive armor. An armored entry farther than an
already accepted infantry target can fail the closer test; an armored entry
accepted earlier can end the scan before a later closer infantry entry.
It is not a universal nearest-armored preference.
[Declared order examples](../player-enemy-tank-evidence.md#cannon-target-order-and-the-closer-before-armor-condition)

After a target is selected, another random branch requests either the cannon
animation or a coax path. That branch count is not a measured weapon-use ratio,
and an action timer can reset even when no target was found.

## The range write is not the cannon's scatter formula

Both selected cannon actions modify a stored range field, but their impact
coordinates use **fixed independent −100…99 axis offsets** around the target's
coordinates read at firing. The placement expressions do not use the modified
range, rifle or experience. A higher displayed XP does not by itself prove
tighter impacts at these sites.

The later explosion has its own AT, fragment, damage and recipient guards.
Its damage input of 300 does not guarantee that health loss, and visible vehicle
width does not become an accuracy term in these coordinate expressions.
[Exact emission and effect](../player-enemy-tank-evidence.md#cannon-effect-placement-ignores-the-modified-range-field)

## Machine-gun components need their own readers

The coax reads its turret parent's rifle field, but some later target references
use its own target index while others use its parent's. That source distinction
still needs closure before claiming an actual victim or hit rate. Tiger has an
additional gunner component with another controller. The hull's stats do not
stand in for all those paths.
[Exact coax and gunner contexts](../player-enemy-tank-evidence.md#coax-and-extra-tiger-gunner-retain-their-own-contexts)

## Incoming AT damage is another path

The selected Tiger/Bazooka exception subtracts 500 health when its guards qualify.
Six such unchanged-health subtractions would exhaust the 3000 load, but six
fired rockets are not guaranteed six qualifying hits. Other attack tags and
recipient states have different rules. [AT and Tiger exception](anti-tank-and-vehicles.md#the-tigerbazooka-exception)

The AT helper's common kill/XP sites can be reached even when that Tiger
subtraction leaves positive health. Its separate tankkilled increment remains
inside the exception's death branch. These counters answer different questions.
[Accounting comparison](../player-at-accounting-evidence.md#the-common-enemy-counter-tail-is-outside-the-tiger-death-check)

Movement counters, escape misses and destruction accounting likewise have their
own parent branches; full timing and outcomes remain partial.

Sources: [Source identities](../player-notes/enemy-tanks.md#citation-1)

The Panther/Tiger turrets reduce their stored blastrange before emitting, but
the actual impact expressions use separate fixed −100…99 axis offsets. Reducing
that field alone does not narrow these coordinate formulas.
[Range bookkeeping versus scatter and later damage](blast-radius-and-scatter.md).
Additional source: [Source identities](../player-notes/enemy-tanks.md#citation-2)

## Bazooka AT damage is not necessarily the last health write

For a Tiger surviving the selected 500-point AT subtraction, a later qualifying visit
from that same Bazooka effect can reach its core or fragment health draw.
With declared starting 550 and unchanged helper distance 4, AT leaves 50 and the
later core draws 0–99; at distance 5, the fragment instead draws 0–49 under its
other guards. This is source-stage arithmetic, not a measured lethal radius,
safe spacing or promised shots-to-kill result.

The AT common kill-counter tail and later core fatal tail can both be reached
for the declared 550→50→0 case, while the later core site has no immediate
removal/tankkilled increment. Parent wreck/counter consumers remain separate.
Distinct effect.father versus effect.dad credit fields must also be supplied.
[Exact actual effect and remaining source/runtime boundaries](../player-zooka-tiger-stages-evidence.md).
Additional source: [Source identities](../player-notes/enemy-tanks.md#citation-3)

For supplied starting 549 and draw 49, the admitted AT then core and AT then fragment
examples can each end at health 0 but reach different kills-counter sites. A
separately reached valid nonstock Tiger parent death callback then increments
the persistent tank counter, without another kills increment in that parent
body. Health, wreck, kills tally and persistent tank counter are different
observations. [Exact later parent and declared equal-health comparison](../player-zooka-tiger-stages-evidence.md#a-separately-reached-tiger-parent-wreck-has-its-own-counter).

## Front-armor values do not establish a percentage or weak-point rule

The selected Panther and Tiger loads store frontArmor 40 and 60, separately from
armor class 2. The finite accepted-source text audit finds that literal field
only in 5 load assignments, including Flakpanzer and two Wespe placements. The
inspected AT damage/removal predicate does not read facing or frontArmor; its
Tiger exception instead depends on subtype and the zooka tag.

That is a bounded source dependency result, not proof every shot direction has
the same actual geometry or outcome. Hold point-distance/query results and
other fields fixed before applying the scalar comparison. [Exact audit and declared field/facing example](../player-front-armor-evidence.md).
Additional source: [Source identities](../player-notes/enemy-tanks.md#citation-4)

## The Tiger's extra gunner has its own shot and retarget rules

The extra gunner is separate from the coax. Its selected shot reads its own
rifle, which loads as 1, and its own target index. The shot does not replace
that rifle with the hull's experience or the cannon turret's stats. With that
unchanged rifle and uniform integer inputs, only draw 0 of 0–99 passes the
local accuracy test. Cover, armor, damage and actual shot scheduling still
follow; this is not a whole-vehicle hit rate.
[Exact shot reader and conditional saves](../player-enemy-tank-evidence.md#the-extra-tiger-gunner-reads-its-own-rifle-and-target)

During a positive repeat counter, 33 of 100 comparison inputs can request a
new player-target pool on the turret. A nonempty pool can replace the gunner's
index; an empty pool retains its old index at that site. This does not prove
that every repeat aims at a different soldier, or that an old index remains a
valid target. Its initial and repeat scans also use different health filters
and source-coordinate origins.
[Exact repeat, timer and receiver limits](../player-enemy-tank-evidence.md#extra-gunner-repeat-can-use-a-different-target-pool-and-origin)

Additional sources: [Source identities](../player-notes/enemy-tanks.md#citation-5)
