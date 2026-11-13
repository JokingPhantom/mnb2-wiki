[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# German Jeep and enemy Halftrack

The German Jeep and enemy Halftrack have **different driver, spare-crew and targeting
rules**, even though their gunners share the same drawing. The enemy
Halftrack is not the Allied Halftrack's module system.
[Exact source comparison](../player-enemy-transport-evidence.md)

Historical scope: selected **2.3.1g**.

| Hull load            | German Jeep | Enemy Halftrack / SdKfz |
| -------------------- | ----------- | ----------------------- |
| Starting hull health | 500         | 1000                    |
| Armor code           | 1           | 1                       |
| Driver flag          | 1           | 1                       |
| Gunner flag          | 1           | 1                       |
| Spare crew           | 0           | 4                       |
| Initial moving field | 0–99        | 1000–2999               |

These fields are load state, not a complete count of healthy arrivals or a
movement duration in seconds. [Vehicle overview](enemy-vehicles.md)

On this page: [A driver loss can change later dismounts](#a-driver-loss-can-change-later-dismounts) · [Initial target choice differs from later retargeting](#initial-target-choice-differs-from-later-retargeting) · [Read the gunner's own fields](#read-the-gunners-own-fields)

## A driver loss can change later dismounts

The Jeep's inspected movement requires a positive driver. The enemy Halftrack
can instead spend one spare crew point to restore driver 1, before its later
movement/unloading decision. Its positive-moving branch has no additional
driver-positive test.

With a declared stopped Halftrack, driver 0 and crew 4, driver replacement
leaves crew 3. If that visit also passes the unloading branch, it requests
three infantry helper calls, assuming helper returns without parent removal
or another crew writer. A stopped, already-driven crew-4 state can instead
request four. Those are source requests, not guaranteed surviving passengers.
[Exact order and supplied inputs](../player-enemy-transport-evidence.md#enemy-halftrack-spends-a-passenger-before-possible-unloading)

The unloading branch can spend all remaining crew in one entered loop. That
differs from the [enemy truck](enemy-truck.md)'s selected one-at-a-time path.
Passenger display children are also separate from the crew counter and the
gunner's firing events.

## Initial target choice differs from later retargeting

The Jeep gunner starts with a closer eligible-target search. The enemy Halftrack
gunner starts by building a parent target pool and choosing from it. The pool's
health/LOS/visibility filters differ from the Jeep's initial guards; a pool is
not automatically a nearest-target selector.
[Exact controllers and receiver contexts](../player-enemy-transport-evidence.md#gunner-placements-and-different-initial-target-choice)

Their shared burst action can later attempt another pool-based target change.
At that retarget site, an empty new pool does **not** first clear the old child
target, unlike the APC's initial entry. Retaining an index does not prove the
old actor is still alive or eligible. The 33-of-100 attempt comparison is not
a measured retarget time or switch probability over an encounter.
[Exact repeat and empty-pool distinction](../player-enemy-transport-evidence.md#the-shared-burst-can-attempt-a-different-retarget-path)

## Read the gunner's own fields

Both selected gunner loads set rifle 1 and XP 1–10, separate from their hull's
rifle roll. The shot comparison reads the gunner's rifle, with later armor,
cover and damage handling. A nominal burst counter is not a count of guaranteed
hits. Full coordinates, playback, crew-damage and exit outcomes remain partial.

Related: [Allied Jeep](jeep.md), [Allied Halftrack](halftrack.md).

Sources: [Source identities](../player-notes/enemy-jeep-and-halftrack.md#citation-1)

[Enemies getting through the line](breakthroughs.md) compares ordinary, bike,
vehicle and advancement contributions, local loss checks and counter reductions.
