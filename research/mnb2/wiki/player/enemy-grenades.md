[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# How the Grenadier's grenade moves

The Grenadier’s grenade moves until its movement counter expires, then requests an explosion.
**An obstacle test that skips one movement update does not stop its counter
from running down.** Its later expiry branch still requests an explosion at
the grenade's then-current position.
[Exact movement and expiry](../player-grenadier-evidence.md#german-grenade-local-movement-and-expiry)

Historical scope: selected **2.3.1g**.

| Selected load field  | Value / meaning in the inspected callback                           |
| -------------------- | ------------------------------------------------------------------- |
| Movement counter     | 20–29; decremented on each eligible positive-counter visit          |
| Speed (source units) | 10–14, used to calculate each displacement                          |
| Heading              | Rotation 90 at load                                                 |
| Midpoint             | Half the initial movement counter, used for growing/shrinking scale |

These are source values, not seconds, measured throw range or screen-pixel
collision guarantees. The callback excludes the stock template and does not run
its movement/expiry body when pausez equals 1. Full runtime scheduling is still open.

On this page: [The late flight does not halve its speed field](#the-late-flight-does-not-halve-its-speed-field) · [Collision test and written position differ](#collision-test-and-written-position-differ) · [The last decrement is not the explosion request](#the-last-decrement-is-not-the-explosion-request)

## The late flight does not halve its speed field

The below-10 counter branch contains a division by 2 with no assignment. That
expression does not store a slower speed. The counter and changing scale can
make the source look like a decelerating flight, but the inspected position
formula continues to read the speed field.
[Exact source distinction](../player-grenadier-evidence.md#german-grenade-local-movement-and-expiry)

## Collision test and written position differ

The obstacle query uses position plus a computed displacement; a clear query
makes the position update subtract that displacement. For declared raw inputs
position (100, 100), heading 90 and speed 12, it queries (100, 88) but writes (100, 112)
when clear. If blocked, that visit leaves position unchanged while reducing the
counter. This example explains the source signs; actual hit-test coordinates,
terrain boundaries and callback ordering still need reconstruction.

At expiry it creates the fragmentation effect at its current position and
removes itself. A visible grenade, an explosion request and an actual injury
are different stages. The ordinary bullet-save percentages do not establish
grenade protection. [Defenses](defenses.md), [Grenadier role](enemy-grenadier.md)

Sources: [Source identities](../player-notes/enemy-grenades.md#citation-1)

## The last decrement is not the explosion request

For declared initial movement counter 20 or 29 with every eligible flight visit
completed and no other counter/removal writer, the counter reaches 0 after 20 or 29
positive-branch visits. The sibling expiry alternative needs a separately
reached 21st or 30th eligible visit. This is source callback counting, not a native
fuse in seconds. Its stored life 500 is not decremented or tested for expiry in
that complete flight body.

The German expiry copies its current point into the fragmentation effect but
has no explicit effect-dad assignment there, unlike the two selected Allied
grenade expiry bodies. Missing that copy does not prove an undefined owner,
no credit or any particular immunity result; defaults, other writers and the
later helper remain inputs. [Exact three-body expiry and field comparison](../grenade-flight-comparison.md#the-german-expiry-lacks-the-two-allied-explicit-dad-copies).
Additional source: [Source identities](../player-notes/enemy-grenades.md#citation-2)
