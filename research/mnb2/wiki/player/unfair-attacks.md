[Player reference](README.md) · [Waves](waves.md) · [Orders](orders.md)

# Unfair attacks: flankers, target selection and rewards

Unfair events use a separate source selector from ordinary reinforcements and
[Blitz events](blitz-events.md). The selected 2.3.1g checks state, then chooses one
of four cases. Starting an attack representation is not the same event as
projectiles arriving or damage occurring.
[Exact source and declared inputs](../player-unfair-event-evidence.md).

| Selected case       | What the source requests                                | Separate unresolved outcome                                     |
| ------------------- | ------------------------------------------------------- | --------------------------------------------------------------- |
| Fast jet            | Start germanJet at frame 2                              | Aircraft callbacks, impact and damage                           |
| Brandenburg raid    | Repeated brand duplication requests                     | Bare-miss namespace, allocation replacement and living arrivals |
| Precision artillery | Choose a reference point, then a scattered bigexplosion | Current objects, effect ownership, blast recipients and damage  |
| Off-map 88          | Start german88 at frame 2                               | Battery delivery and later targets                              |

On this page: [No missed enemies does not exclude every late-wave event](#no-missed-enemies-does-not-exclude-every-late-wave-event) · [Precision does not mean highest rank or nearest bunker](#precision-does-not-mean-highest-rank-or-nearest-bunker) · [The Ribbon counter is not a distinct-event total](#the-ribbon-counter-is-not-a-distinct-event-total)

## No missed enemies does not exclude every late-wave event

The selected guard has one term above local wave 20 involving the missed count,
and another above local wave 80 involving missed count plus local wave/25.
At supplied wave 81 and miss 0, independent uniform integer draws give 4 passing
inputs out of 100 at the latter term. This is one reached guard opportunity,
not a 4%-per-wave or per-second measured attack rate. The lower-wave flankers
message alone does not establish that an enemy must have crossed your line.

At supplied wave 100/miss 9, the two short-circuited terms give 16.48% under those
same independent inputs, not 4%+13%=17%. Actual timer, pause, callback and profile
state still determine whether this guard is reached.
[Exact comparisons and integer boundaries](../player-unfair-event-evidence.md#admission-can-pass-after-wave-80-even-with-no-missed-enemies).

## Precision does not mean highest rank or nearest bunker

The selected precision case takes coordinates from the **last matching bunker
index** in its decoration scan. If none is found, it scans eligible living,
noninvincible player entries against a rank reference initialized 0. It never
updates that reference when accepting a candidate, so a later eligible rank 0
entry can overwrite an earlier rank 9 entry's coordinates.

These are selected scan rules, not a reproduced way to control an attack.
The later effect adds independent −100…99 offsets to both axes. A reference point
is not an exact impact, a confirmed hit or a reason to infer a safe layout.
[Complete scan and fixed-rank-reference examples](../player-unfair-event-evidence.md#the-player-fallback-never-updates-its-rank-reference).

## The Ribbon counter is not a distinct-event total

This admitted event body has two career unfair-counter increments, with the
Ribbon test between them. With declared execution through both writes and no
other changes, 998 becomes 999 at the test then 1000 at the end. The next such
visit can reach 1001 at the test and 1002 afterward. Actual interruption and
other writers still matter; the stored number is not a verified count of
that many different attacks survived.

The Ribbon's selected TP consumer also needs **two nested 1-of-100 tests**, then
its old-balance guard. Under supplied independent uniform inputs those two tests
give 1/10,000 before the balance check, not a universal 1% reward per event.
[Counter and reward source order](../player-unfair-event-evidence.md#ribbon46s-selected-tp-reward-needs-two-exact-value-tests),
[career entry](career-medals-and-ranks.md).

For defensive responses, use [enemy roles](enemy-guide.md),
[air defense choices](air-defense.md), [counter-artillery](naval-and-counter-artillery.md)
and [blast/fortification stages](explosions-and-fortifications.md). These source
comparisons do not certify an optimal formation or survival rate.

Source: [Source identities](../player-notes/unfair-attacks.md#citation-1). Original later coverage remains a candidate.

The [off-map 88 path](off-map-88.md) has a separate root controller and a
random-point effect load. It does not share the precision reference scan or
the field Pak38's health/crew targeting model.
Additional source: [Source identities](../player-notes/unfair-attacks.md#citation-2)

The fast jet's named action also clears shared pending germbomb and records
a bomb statistic. Its effect chooses a random whole-field source point, rather
than the normal aircraft's selected half, and uses 40/40/40/300 blast inputs.
Clearing a pending field and recalling an emitted bomb remain different events.
[Exact fast-jet and ordinary-bomber comparison](../player-unfair-jet-evidence.md).
Additional source: [Source identities](../player-notes/unfair-attacks.md#citation-3)
