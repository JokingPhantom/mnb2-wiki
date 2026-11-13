[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Role comparison](recruitment.md#choose-the-job-before-the-price)

# Bazooka soldier

A **4-TP anti-tank recruit** whose rocket checks for nearby targets at intervals.
Passing close to a vehicle between those checks need not trigger the rocket.
Firing also creates a separate backblast that can hurt unarmored troops on either
side. A bigger rifle number is not a complete rocket-hit percentage.
[Flight research](../bazooka-detonation.md), [backblast](../bazooka-backblast.md)

Rifle, morale and experience have separate career additions in this load profile.
The actor-specific weapon field must not be interpreted through the shared
infantry-rifle weapon table. This soldier's rocket, backblast and explosion
paths are distinct mechanisms. [Actor/load evidence](../player-defense-evidence.md#bazooka-and-engineer-defaults)

Applies to **historical selected 2.3.1g**. Starting facts use the ordinary load;
career additions and other conditions are labeled separately.

| Key fact          | Selected ordinary load                                                        |
| ----------------- | ----------------------------------------------------------------------------- |
| Recruitment       | Reinforcements; base 4 TP                                                     |
| Health            | 100 health points                                                             |
| Morale            | 10–19 before career bonuses                                                   |
| Experience        | 0 before career bonuses                                                       |
| Rifle skill field | Starts at 10 with random-stop additions; not a complete rocket-hit percentage |

[Starting-stat evidence](../player-roster-evidence.md)

On this page: [A shot counter and the rocket are separate stages](#a-shot-counter-and-the-rocket-are-separate-stages), [Why rockets can pass a target](#why-rockets-can-pass-a-target), [The blast starts at the sampled rocket point](#the-blast-starts-at-the-sampled-rocket-point), [Keep the backblast region clear](#keep-the-backblast-region-clear), [The armored search is first by index, not nearest](#the-armored-search-is-first-by-index-not-nearest).

## Use the launcher without confusing a launch with a hit

For **selected historical 2.3.1g**, budget the 4-TP recruit separately from any
later defenses or support. Compare the [8-TP M3](m3-at-gun.md) when choosing a
crewed gun instead; neither price measures vehicle kills per TP.
[AT decision guide](anti-tank-options.md).

1. **Check that the recruit arrived and can act.** A completed purchase is not a
   completed attack. Check readiness, orders and the target rather than treating
   the weapon name as proof that a rocket is about to fire.
2. **Check the position for friendly hazards.** Keep unarmored allies out of its
   backblast region and account for the later explosion separately. This page
   supplies no certified safe spacing or guarantee from a bunker or net.
3. **Watch the sequence:** launch sound, actual rocket, explosion, then the
   vehicle's resulting state. Those observations do not prove the same event.
4. **If it stays idle under a net, check the camouflage restriction below.**
   Do not assume Concentrate Fire is a proven workaround; an accepted order can
   still fail to produce an immediate rocket.

If rockets repeatedly pass a target, separate a missed trigger from a blast
that triggered but did not qualify to damage that vehicle. Moving or retargeting
the soldier does not steer a rocket already launched. Historical advice to
reposition is not a tested hit-chance recipe for this selected binary.
[Flight and blast stages](#the-blast-starts-at-the-sampled-rocket-point),
[friendly explosive hazards](collateral-damage.md).

## A shot counter and the rocket are separate stages

The selected preparation action sets a large counter before an XP-based
navigation test. A later frame records a shot and plays the launch sound,
while a separate frame creates the actual rocket. Those selected sites do
not certify a completed launch from the sound or statistic alone.

The shot/sound frame also adds 50 to each qualifying nearby living unarmored
player entry's action counter. That is a counter addition under source-distance
and scan guards, not a universal measured suppression duration or a safe layout.
Preparation, nearby actors, backblast and the emitted rocket have different
writers and recipients. [Exact stages and supplied XP inputs](../player-bazooka-event-evidence.md#preparation-and-shot-accounting-precede-a-separate-rocket-birth)

## Why rockets can pass a target

With the selected load defaults, the first scan occurs after **31 qualifying
active events**, then every **16**. If rotation stays fixed, every movement is
allowed, no override occurs and nothing removes or detonates the rocket early,
the speed ramp gives **195.5 source units** of travel before that first scan and
**128** between later scans. These are conditional source derivations, not
universal measured flight distances or seconds.
[Counter and movement trace](../bazooka-detonation.md)

The inspected enemy scan checks distance **strictly below 50** and positive
enemy health. Terrain and friendly-target branches have their own conditions.
A proximity check is not a vehicle-outline hit test, and triggering the later
blast is not automatically the same as damaging the vehicle.
[Projectile conditions](../bazooka-detonation.md)

## The blast starts at the sampled rocket point

The selected enemy-trigger predicate checks positive health and distance below 50. It does not require armor, visibility, invincibility or line of sight there.
An infantry entry can therefore meet this local trigger; it is not a vehicle-only
contact filter. Later damage eligibility still has its own tests.

On the allied enemy-scan match, the new blast receives **the rocket's current
post-movement coordinates**, before the rocket is relocated. It is not centered
on the enemy. For a declared unchanged shared-coordinate example, rocket/blast
at (200,200) and enemy at (240,200) are distance 40 apart: the trigger passes below
50, but the later AT-radius-25 distance gate fails. This is a source-point example,
not a measured miss rate or a guarantee of every later damage outcome.
[Exact order, owner copies and remaining limits](../player-bazooka-event-evidence.md)

A historical player analysis reported detonation bands around 200, 325, 450 and
575 pixels and recommended moving the launcher when rockets repeatedly pass a
stationary vehicle. That is attributed historical advice, not a guaranteed
placement fix or a measured hit chance for this exact binary.
[Original report and assumptions](../bazooka-detonation.md)

## Keep the backblast region clear

The selected firing-frame path tests a separate region against unarmored,
living recipients, with loops for both allied and enemy troops. Its damage draw
is **1–3 health**, differing from the legacy guide's 1–4 claim. It also writes
an action timer of 80; that is not yet a calibrated pin duration in seconds.
Do not assume a bunker protection rule from a different blast helper prevents
this damage. [Backblast source](../bazooka-backblast.md)

The community reports camouflage-net firing restrictions and order exceptions.
Those require their own actor-state checks; neither a transparent drawing nor a
successful purchase proves the launcher is ready to fire.
[Community account](../bazooka-backblast.md)

Sources: [Source identities](../player-notes/bazooka.md#citation-1), Selected 2.3.1g with attributed community
observations; [exact evidence](../player-defense-evidence.md).

[Hold Fire](hold-fire.md) now binds this actor's selected counter replacement
and later positive-counter consumer. It does not certify cancellation of a
rocket which already has its own callback. Additional source: [Source identities](../player-notes/bazooka.md#citation-2)

## The armored search is first by index, not nearest

The selected ready path first looks for a living, line-of-sight-qualified armored
enemy. It takes the first qualifying index, without a closest-distance comparison
or positive-visibility test at that acceptance. Only the fallback uses a closer-
distance search with additional visibility/melee conditions. The later blast's
AT-recipient visibility and other guards are still separate.
[Exact two-pass selection](../player-bazooka-acquisition-evidence.md#the-armored-pass-and-fallback-have-different-filters)

## Camouflage and order entry have their own gates

The inspected nonshotgun attack request checks that camouflage is false. A
qualifying net overlap can block that request, but shared reconnaissance state
can disable the net query without removing the net itself. Other weapon/grenade
alternatives and actor conditions remain separate.

Concentrate Fire has its own target/recipient/line-of-sight guards and can request
an actor animation without that same camouflage query at its navigation site.
This source difference does not certify an actual net/reload bypass or immediate
rocket; later pause, bunker, preparation and birth actions still matter.
[Exact camouflage, reconnaissance and order comparison](../player-bazooka-acquisition-evidence.md#camouflage-gates-one-nonshotgun-request-not-every-order-entry)
Additional sources: [Source identities](../player-notes/bazooka.md#citation-3)

## Backblast's damage, pin request and timer are separate

After its damage write, the selected backblast action can request a death state
and then still request **PinnedDown** and write the counter 80. The player-side
death test is below 10 health; the enemy-side test is below 1. There is no explicit
pin-flag assignment in that body, and the exact requested label spelling differs
in case from the mapped ordinary/Regular labels.

This is source request order, not a reproduced revival, a proven label failure
or a calibrated pin duration. Actual navigation, actor-specific recovery and
callbacks still matter. The timer write also replaces the previous value:
a supplied 400 becomes 80 at that assignment, rather than receiving another 80.
[Exact requests, label strings and counter inputs](../player-backblast-order-evidence.md#no-explicit-pinned-field-assignment-accompanies-that-timer-here)

Blood placement uses different indexed readers for its two axes in this action;
its position should not be treated as an exact recipient or damage receipt.
The actual health write still has its own loop recipient.
[Exact coordinate-reader scope](../player-backblast-order-evidence.md#the-blood-position-does-not-use-one-recipient-index-for-both-axes)
Additional source: [Source identities](../player-notes/bazooka.md#citation-4)

## A launched rocket is a separate object from the new aim order

The Allied launch copies the soldier's point and facing onto a rocket. Its
selected flight direction reads the rocket's own rotation, rather than the
launcher's later position, facing or chosen target index. Moving or retargeting
the launcher is therefore not a steering instruction in those flight expressions.
A future launch can copy a different facing; these are different stages.

The flight still reads a live owner field to choose its trigger scan, so this
is not a guarantee that owner lifetime never matters or that an already-created
rocket survives every interruption. Full callback order and coordinates remain
unqualified. [Exact heading and owner readers](../player-bazooka-event-evidence.md#launch-copies-heading-but-flight-still-reads-a-live-owner-field).
Additional source: [Source identities](../player-notes/bazooka.md#citation-5)

## A surviving Tiger can reach a later core or fragment subtraction

The selected effect's AT stage can subtract 500 from an eligible Tiger, then its
later scan can subtract a separate draw if the same valid recipient survives
and still qualifies. The effect supplies core 5, AT 25, fragment 25 and damage 50;
the later core draw is 0–99 and fragment draw 0–49. The numeric 50 does not replace
the earlier special 500, and 500 is not necessarily the whole health change.

A declared Tiger at 550 health and stable helper distance 4 first falls to 50,
then a supplied core draw 50 gives 0. The earlier AT removal check had failed;
the later armor 2 core fatal counter is not an immediate removal or tankkilled
write at that site. Actual owner validity, parent wreck behavior, callbacks and
transformed geometry remain unresolved. [Exact ordered stages and declared distance 4/5/25 comparison](../player-zooka-tiger-stages-evidence.md).
Additional source: [Source identities](../player-notes/bazooka.md#citation-6)

The selected Bazooka blast also requests a separate cratere2 object before its
helper call. Its selected crater load counter 500 is a different receiver from
the Tiger exception's health subtraction 500. Crater appearance/lifetime does
not provide a calibrated rocket blast footprint or damage measurement.
[Exact alias, point writes and later blast receiver](../player-crater-lifetime-evidence.md#five-selected-effects-request-different-crater-aliases-before-their-blast-call)
Additional source: [Source identities](../player-notes/bazooka.md#citation-7)

## Scenery can trigger a rocket without being ordinary cover

The selected terrain scan accepts tree, rock, deco or crate types within its
separate point-distance threshold. It does not choose from a prop's flammability
or named cover child. The crate-shaped prop (character 1579) loads a tree type and therefore
can satisfy that type test; the inspected sandbag, airborne wall, Bunker,
Pillbox and camouflage-net load types do not belong to this particular list.
That is a local trigger distinction, not immunity or proof rockets pass through
those defenses. The earlier movement query and later blast tests still matter.

A blocked displacement also does not by itself create a blast or skip the
separate zero-counter scan. Actual point, current types, actor matches and
callback order are needed before predicting a detonation beside scenery.
[Exact nine-load comparison and separate move/scan guards](../player-bazooka-event-evidence.md#scenery-trigger-membership-is-separate-from-cover-and-flammability).
Additional sources: [Source identities](../player-notes/bazooka.md#citation-8)

## Why this infantry test does not rank anti-tank value

The following comparison uses the **November 7, 2026 modern simulation build**.
It is separate from the historical source facts above and from later corrections.
[Study conditions and build limits](combat-results.md).

The native rocket package did not clear the modern infantry fixture, and
self-incapacitation can stop a specialist early. That result does not establish
its vehicle effectiveness. A stored training weapon code 2 still invokes rockets;
it is not a Garand loadout. Rocket birth, flight, backblast and blast are distinct
from shot accounting. [Lifecycle](unit-lifecycle.md), [study limits](combat-results.md).
