[Player reference](README.md) · [Anti-tank options](anti-tank-options.md) · [Vehicles and emplacements](vehicles-and-emplacements.md)

# Anti-tank hits, vehicle health and crew are different questions

A rocket nearing a vehicle, triggering an explosion and satisfying a later
anti-tank recipient test are **different stages**. Vehicle-outline hitboxes,
projectile sampling, AT radius, armor class, crew and parent health must not be
collapsed into one advertised accuracy or damage number.
[AT source evidence](../player-roster-evidence.md#anti-tank-and-vehicles)

Historical scope: selected **2.3.1g** source. Distances and coordinates below
are source inputs, not certified visible safe spacing.

For the classification itself, read [armor codes 0, 1 and 2](reading-stats.md#what-do-armor-codes-0-1-and-2-mean).
An armor code, hull health and occupied crew roles answer different questions
before the projectile and explosion stages below.

Jump to [why proximity is not an AT hit](#a-proximity-trigger-is-not-the-later-at-test),
[the Tiger/bazooka exception](#the-tigerbazooka-exception),
[hull health and crew](#initial-parent-health-is-not-the-whole-durability-model),
[what accuracy still needs](#compare-supplied-point-inputs-before-calling-it-accuracy),
[AT kill-counter credit](#an-at-kill-counter-write-is-not-always-a-removed-tank),
[Tiger damage stages](#the-tigers-500-subtraction-can-be-followed-by-another-health-draw), or
[stored front armor](#a-stored-front-armor-number-is-not-a-facing-based-reduction-rule).

## A proximity trigger is not the later AT test

The inspected bazooka projectile checks proximity only on selected events,
with a strict below 50 distance test in the cited enemy scan. Its identified blast
call supplies an AT argument 25 to a later helper. The selected allied enemy-trigger branch puts the blast at the sampled rocket
point before relocating the rocket. With declared unchanged shared coordinates,
rocket/blast (200,200) and enemy (240,200), distance 40 passes the trigger but fails
the later below-25 AT gate. This is a branch-local point example; actual callback
motion, coordinate transforms and total damage remain separate qualifications.
[Exact event-order binding](../player-bazooka-event-evidence.md)
[Bazooka sampling](bazooka.md), [helper chain](../anti-tank-helper.md)

The AT helper also has recipient exclusions and armor, distance, invincibility
and visibility guards. It is not an unconditional destruction circle around
every displayed explosion. The radius input is separate from the explosion's
ordinary damage argument, and friendly recipients have their own scan.

The [M3 AT gun](m3-at-gun.md) has a separate source chain: an offset explosion
near its selected target, then an AT-radius input of 50 with special tag **at**.
Its point-distance examples do not depend on a guessed vehicle-outline width.

The enemy [Pak38](pak-38.md) also creates an AT-radius-50 effect with tag at,
but its crew/setup and closer-before-armor target selection differ from the M3.
Its fixed axis-offset emitter does not read its loaded rifle or XP fields.
[Exact named enemy chain](../player-pak38-evidence.md#frame8-places-an-effect-around-the-current-indexed-target)

The [20 mm cannon](aa-cannon.md) instead supplies AT radius 2 and special tag
**air** in its selected ground effect. It does not inherit M3 AT radius 50 or
Bazooka radius 25 simply because its effect appears near an armored target.

The [rocket launcher](rocket-launcher.md) supplies AT radius 25 with tag **at**
in its selected random-coordinate impact effect. Equal radius inputs still do
not make its activation, targeting or Tiger handling the Bazooka path.

The [ordinary and AT mine effects](explosives.md#a-mine-trigger-does-not-center-the-blast-on-the-vehicle)
both supply AT radius 50 at their selected calls, despite different trigger
armor filters, fragment inputs and tags. Their triggers place the effect at
the mine point. The later AT predicate still uses its own point-distance test.

## This AT predicate uses coordinates rather than visible width

The selected helper passes the effect and indexed actor to a function that
reads their x/y fields for Euclidean point distance, then tests it strictly below
the AT input. The actor's visible width is not an extra term in this predicate.
Actual parent-coordinate transforms, effect placement and motion still need
qualification; a point test is not an observed whole-shot probability.
[Exact point-distance bindings](../player-tank-evidence.md#the-selected-at-gate-reads-points-not-an-outline)

The [Sherman cannon](sherman.md) supplies AT radius 40 with tag **tank** through
its selected explosion effect. Its stored blastrange field does not drive the
fixed axis-offset writes at that emitter. Tank, rocket, M3 and Bazooka paths
therefore need their own source context despite similar explosion artwork.

## The Tiger/bazooka exception

For the selected enemy armor 2 branch, subtype tiger with special tag zooka loses
**500 health** and is removed only after its relevant nonpositive-health check.
Other qualifying armor 2 recipients outside that exception take a different direct
removal branch. A generic “inside the AT radius means instant vehicle death”
statement therefore erases a real selected-source exception.
[Exact guarded branches](../anti-tank-helper.md)

The Tiger load's 3000 health would require six 500-point subtractions to reach 0
**only if those exact branches all qualify and no other health changes occur**.
That arithmetic is not “six fired rockets always kill”: missing/early triggers,
other damage, overrides and target state remain separate.

## An AT kill-counter write is not always a removed tank

In the selected AT helper, the common enemy kill-counter increment lies outside
the Tiger/Bazooka exception's death check. A qualifying Tiger starting at 3000
health becomes 2500 there without removal, yet still reaches that counter and
an effect-owner XP write. Owner-field validity and actual promotion remain
separate. Armor 1 vehicles also have driver/gunner/spare-crew count additions
before the common increment. A displayed kill tally should not be treated as
an exact count of destroyed chassis from this path.
[Exact branches and declared inputs](../player-at-accounting-evidence.md#the-common-enemy-counter-tail-is-outside-the-tiger-death-check)

The [hull-damage and crew guide](vehicle-damage-and-crew.md) follows a separate
fragment-blast path: hull subtraction precedes independent crew-loss checks.
Repairing health and filling a missing gunner are different follow-up actions.

## Initial parent health is not the whole durability model

| Vehicle load          | Initial hull health | Armor code |
| --------------------- | ------------------: | ---------: |
| US Jeep / German Jeep |                 500 |          1 |
| Halftrack             |                 800 |          1 |
| Sherman / Panther     |                1000 |          2 |
| Tiger                 |                3000 |          2 |
| SdKfz 222             |                 650 |          1 |
| Wespe placements      |                1000 |          2 |

The armor numbers are source classes, not percentages. Equal health/class does
not establish equal weapons, component states, crew, movement or survivability.
Distinct placements are preserved in the [vehicle source map](../vehicle-load-map.md).

In the selected SdKfz 222 controller, driver exactly 0 is reset to 1 and health loses 20
under its active guards. A shared rifle-helper crew hit is therefore not proof
of permanent immobilization for that actor. A bike also has a separate momentum
movement path, while a truck handles spare crew and unloading differently.
Do not use one “shoot the driver” rule for all vehicles.
[Source crew/movement comparisons](../vehicle-load-map.md), [vehicle accounting](../vehicle-crew-accounting.md)

Repairs, replacement crew and modules have their own receipts and caps/thresholds.
Full tank-gun aim dispersion versus transformed vehicle hitboxes remains a
shared reconstruction gap, not a guessed percentage from sprite width.
[Mechanic](mechanic.md), [Crewman](crewman.md)

Sources: [Source identities](../player-notes/anti-tank-and-vehicles.md#citation-1).
[Exact vehicle evidence](../player-roster-evidence.md),
[point-distance bindings](../player-tank-evidence.md),
[rocket/blast event order](../player-bazooka-event-evidence.md).

## An explosive vehicle has its own trigger and blast

The [Goliath](goliath.md) has a selected positive-health-player trigger at strict
distance below 30, while the emitted effect later supplies AT 40 and tag tank.
Its health/driver/gunner and decoration-scan paths are separate. This does not
make the trigger the same test as a later blast recipient, or resolve its
owner/credit and mutable decoration-index behavior.
[Exact trigger/effect boundaries](../player-light-vehicle-evidence.md#frame20-actor-proximity-and-the-separate-decoration-index-question)
Additional source: [Source identities](../player-notes/anti-tank-and-vehicles.md#citation-2)

Additional source: [Source identities](../player-notes/anti-tank-and-vehicles.md#citation-3)

## Small-arms crew hits are another path

The shared infantry helper can clear an armor-class 1 driver or gunner without
subtracting hull health at that site. Its type exceptions and crew-category
rolls differ from both AT destruction and fragment-blast crew checks.
[Small arms against vehicle crews](small-arms-against-vehicles.md).
Additional source: [Source identities](../player-notes/anti-tank-and-vehicles.md#citation-4)

## AT eligibility is not the blast's only removal mechanism

The named grenade effect supplies AT 5 and a separate core 10. A declared valid
armor 1 recipient at helper distance 7 can fail the former while entering the
later core/gib removal route. This is not a measured position or a whole-hit
probability; it shows why one AT-radius test is not the complete durability rule.
[Explosion-stage example](explosion-damage-stages.md#failing-the-at-radius-does-not-settle-every-removal-path).
Additional source: [Source identities](../player-notes/anti-tank-and-vehicles.md#citation-5)

For purchase and placement choices, compare [anti-tank options](anti-tank-options.md):
base TP, target selection, crew checks and the M3's spacing rule differ before
any later damage test. The comparison keeps rocket sampling separate from
scattered target-coordinate effects.

## Compare supplied point inputs before calling it accuracy

The M3 and Sherman cannon emitters both place their named effect using separate
axis offsets from −100 through 99; their later AT inputs are 50 and 40 respectively.
With a fixed target/effect in unchanged shared raw coordinates, 7,825 of the 40,000
ordered offset pairs pass the strict radius 50 point test, versus 5,013 for radius 40.
A point exactly 40 away fails the latter; exactly 50 away fails both.
[Exact assumptions, source bindings and two agreeing counts](../player-mounted-evidence.md#a-conditional-integer-grid-comparison-of-the-two-fixed-offset-emitters).

This compares one supplied geometric predicate, not measured hit or destruction
rates. Actual coordinates, movement and other recipient guards remain unresolved;
weapon cost, target acquisition, fire admission and later damage also differ.
The count cannot rank these purchases or certify a placement from the artwork.

## The Tiger's 500 subtraction can be followed by another health draw

The selected Bazooka effect sends separate core 5/AT 25/fragment 25/damage 50 inputs.
Its admitted TigerAT stage subtracts 500 before the later core/fragment scan.
If the same valid recipient survives and keeps its point/state, that later visit
can subtract again: core uses 0–99, while fragment uses 0–49 with its own LOS and
live-health guards. These are different stages, not competing damage labels.

With declared starting health 550 and all stated guards/owners valid, helper
distance 4 gives 550→50 then a core draw 0–99; distance 5 instead gives 550→50 then a
fragment draw 0–49. Those source distances are not measured safe placements.
At distance 25 the strict AT/fragment gates both fail; do not begin that row at 50.
[Exact boundaries, supplied fields and two different counter/XP tails](../player-zooka-tiger-stages-evidence.md).
Additional source: [Source identities](../player-notes/anti-tank-and-vehicles.md#citation-6)

## A stored front-armor number is not a facing-based reduction rule

The selected Panther/Tiger/Flakpanzer/Wespe loads store frontArmor 40/60/40/30.
A finite audit of 2114 hash-matched accepted source bodies finds 5 literal uses,
all load assignments including two separate Wespe placements. That does not
supply a 60% Tiger damage-reduction rule or an extra weak-point multiplier.

The inspected AT recipient gate reads armor class, subtype/tag, point distance,
visibility, protection and owner exclusion without a facing/frontArmor read.
With those declared inputs fixed, changing only facing or that stored field
does not alter its scalar branch. Earlier projectile/outline/transform results
can still differ; no native equal-damage-from-every-direction test is claimed.
[Exact literal inventory, selected readers and supplied Tiger example](../player-front-armor-evidence.md).
Additional source: [Source identities](../player-notes/anti-tank-and-vehicles.md#citation-7)

## A sticky bomb reaches a different Tiger tag branch

The [sticky bomb](sticky-bomb.md) creates the TNT effect, whose selected AT call
has radius 25 and tag tnt. The Tiger's special 500-health subtraction needs tag
zooka. For a separately reached, valid armor-2 Tiger AT visit with supplied
helper distance 24 and radius 25, tnt takes the other wreck/removal branch;
zooka takes the health-subtraction route. Exactly 25 fails the shared strict
distance test for both tags.

This is a guarded helper comparison. Actual placement, attachment, surviving
recipient, owner fields, callbacks and coordinate geometry remain necessary
before claiming a whole-bomb outcome. The ordinary damage input and later
health branches are separate from this AT decision.
[Exact actual TNT effect and all supplied guards](../player-sticky-tiger-evidence.md).
Additional sources: [Source identities](../player-notes/anti-tank-and-vehicles.md#citation-8)
