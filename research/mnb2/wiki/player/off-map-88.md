[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Off-map 88 support attack

The **off-map 88 is an enemy support attack**, separate from the
field [Pak38](pak-38.md), [Flak38](flak38.md) or [Nebelwerfer](nebelwerfer.md).
An unfair event starts a sequence that requests separate explosion effects. A gun name alone does not supply hull health, crew,
accuracy or an ordinary battlefield targeting scan.
[Exact controller/effect source](../player-offmap-88-evidence.md).

Historical scope: selected **2.3.1g**.

| Key fact        | Historical behavior                                                         |
| --------------- | --------------------------------------------------------------------------- |
| Role            | Off-map support attack, not a field gun with a crew/health card             |
| Effect position | Random source x 0–399 and y 0–599                                           |
| Blast inputs    | Core 25; AT 50; fragment 50; damage 100                                     |
| Important limit | Inputs are not guaranteed health loss, hit count or measured barrage timing |

On this page: [The effect chooses a random source point](#the-effect-chooses-a-random-source-point) · [The blast inputs and protection path matter](#the-blast-inputs-and-protection-path-matter) · [A support field is not a local recall command](#a-support-field-is-not-a-local-recall-command)

## The effect chooses a random source point

The controller has effect-request actions at frames 20, 30 and 40. These are not
three verified hits, a whole-barrage count or calibrated seconds between shells.
The selected nonstock effect load supplies random x0..399 and y0..599, without
reading a chosen soldier, bunker, rifle or XP in those coordinate expressions.
It is not the unfair precision strike's reference-plus-offset selection.

The source load also contains a discarded comparison to typez "explo", rather
than assigning that value. Actual inherited type/owner, load timing and
transformed effect/recipient geometry remain separate. A successful request
or visual crater does not certify any particular damage.

## The blast inputs and protection path matter

Its named effect passes **core 25, AT 50, fragment 50 and damage 100** with tag tank
to the shared explosion helper. AT 50 is a point-distance eligibility input,
not a vehicle-outline hit probability or a promise of 100 health damage.
It also requests bunker removal directly before the shared helper's own
structural dispatch. Two selected calls do not prove two successful removals
or two occupant hits.
[Blast stages](explosion-damage-stages.md),
[fortification removal](explosions-and-fortifications.md).

## A support field is not a local recall command

The selected unfair case and these short emitter bodies do not test airsup or
counter at those sites. That differs from particular other enemy-event gates;
neither active protection nor a counter credit alone proves this attack was
canceled or a created effect recalled. Full timing and state still need a
qualified trace. [Unfair attacks](unfair-attacks.md),
[Air Superiority](air-defense.md), [counter-artillery](naval-and-counter-artillery.md).

Source: [Source identities](../player-notes/off-map-88.md#citation-1). Original later coverage remains a candidate; no new
barrage, hit, crew, timing or survival trial is claimed.
