[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy vehicles: hull, armor, crew and weapon

Check an enemy vehicle’s **hull health, armor, crew and weapon separately**. One starting-health
number does not describe every bullet, blast, disabled gun or escape outcome.
This overview uses the selected historical **2.3.1g** source.
[Exact vehicle-load map](../vehicle-load-map.md)

After a crew hit, [can the transport still unload infantry?](#can-a-damaged-transport-still-unload-infantry)

On this page: [Before choosing a response](#before-choosing-a-response) · [Can a damaged transport still unload infantry?](#can-a-damaged-transport-still-unload-infantry) · [Selected parent load values](#selected-parent-load-values) · [What an apparent hit can mean](#what-an-apparent-hit-can-mean) · [Read the weapon's own receiver](#read-the-weapons-own-receiver)

## Before choosing a response

Ask which part of the threat is still active, rather than reading the vehicle
as one health bar. These are **selected 2.3.1g** distinctions; the linked guides
give the exact source conditions.

| Player question                                         | What to inspect                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Should small arms and an AT blast have the same effect? | No. Crew-hit, ricochet, hull-damage and AT-removal paths differ. [Small arms against vehicles](small-arms-against-vehicles.md), [AT stages](anti-tank-and-vehicles.md)                                                                                                                         |
| Why did a nearby explosion leave the vehicle alive?     | The selected AT distance check uses points and other recipient guards; Tiger also has a Bazooka-tag exception. Visible size is not a complete hit probability. [Point and Tiger comparison](anti-tank-and-vehicles.md)                                                                         |
| Does losing the driver stop it permanently?             | Not universally. SdKfz 222 can reset its driver at a health cost; Flakpanzer and Wespe parent movement has no local driver/gunner gate. [SdKfz 222](sd-kfz-222.md), [Flakpanzer/Wespe guards](../player-flak-wespe-evidence.md#hull-movement-and-destruction-do-not-use-one-generic-crew-rule) |
| Which rifle or XP value controls its gun?               | Check the weapon's actual reader. A child turret and the hull can have different fields; one load number is not the entire attack. [SdKfz 222 turret](sd-kfz-222.md)                                                                                                                           |
| Does one escaping vehicle count as one missed enemy?    | Exit accounting differs. The selected motorcycle adds separately for positive driver and gunner fields. [Breakthrough consequences](breakthroughs.md)                                                                                                                                          |

For a purchase comparison, use [choosing AT support](anti-tank-options.md), then
check the relevant enemy card below. The load table is not a ranking of required
shots, kills per TP or measured danger; full effect geometry and lifecycles remain
partial.

Before reading the armor column, compare [what codes 0, 1 and 2 mean](reading-stats.md#what-do-armor-codes-0-1-and-2-mean).
The code selects particular recipient branches; it is not a percentage damage
reduction or a complete durability rating.

## Can a damaged transport still unload infantry?

**Crew loss alone does not rule out a later infantry request.** A cleared driver
or gunner field is different from removing the vehicle or exhausting its later
dismount paths. Check the particular transport before treating a crew hit as the
end of its threat.

| Transport                                      | What the selected source distinguishes                                                                                                                                                                       |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Enemy truck](enemy-truck.md)                  | Spare crew first replaces a gunner exactly at 0. A later qualifying unload check can spend one remaining crew point on one infantry request. Replacement can use the last point before unloading is checked. |
| [Enemy Halftrack](enemy-jeep-and-halftrack.md) | Spare crew can replace a driver exactly at 0 before the movement/unloading decision. A passing unload branch loops through the remaining crew, rather than requesting just one soldier.                      |
| [Enemy motorcycle](enemy-motorcycle.md)        | Driver loss can lead to coasting and then a separate machine-gunner dismount. A coast update reaching zero momentum does not also enter the sibling dismount branch on that visit.                           |

These are **selected historical 2.3.1g source paths**, not guaranteed healthy
arrivals or a measured time to unload. The newly requested infantry has its own
load and later state; its parent's hull health, rifle value and stored crew count
are not a complete infantry stat or arrival table.
[Truck replacement order](../player-truck-lifecycle-evidence.md#a-replacement-gunner-can-consume-the-last-possible-unload-slot),
[Halftrack replacement and unload loop](../player-enemy-transport-evidence.md#enemy-halftrack-spends-a-passenger-before-possible-unloading),
[motorcycle coasting and dismount](../player-bike-lifecycle-evidence.md#driver-loss-can-lead-to-a-new-machine-gunner-request-after-coasting).

Compare [small-arms crew hits](small-arms-against-vehicles.md) separately from
[AT and hull damage](anti-tank-and-vehicles.md). These distinctions do not give
an optimal target order, a permanent stopping tactic or a kill-counter reward.

## Selected parent load values

| Enemy family                                           | Starting hull health | Armor code | Deeper coverage                                                                                                      |
| ------------------------------------------------------ | -------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------- |
| [German Jeep](enemy-jeep-and-halftrack.md)             | 500                  | 1          | Driver guard, initial gunner search and shared retarget path                                                         |
| [Panther](enemy-tanks.md)                              | 1000                 | 2          | Ordered cannon targeting, fixed offsets and separate coax readers                                                    |
| [Motorcycle](enemy-motorcycle.md)                      | 300                  | 1          | [Crew and escape accounting](../vehicle-crew-accounting.md)                                                          |
| [Tiger](enemy-tanks.md)                                | 3000                 | 2          | [Tiger/Bazooka exception](anti-tank-and-vehicles.md#the-tigerbazooka-exception)                                      |
| [Enemy truck](enemy-truck.md)                          | 1000                 | 1          | [Spare crew and replacement](../vehicle-crew-accounting.md#the-trucks-spare-crew-is-separate-from-driver-and-gunner) |
| [Enemy Pak38 gun](pak-38.md)                           | 500                  | 1          | Crew-sum setup, closer-before-armor break and fixed-offset AT effect                                                 |
| [Flakpanzer](flakpanzer.md)                            | 1000                 | 2          | Mixed target-index effect frames and small-explosion inputs                                                          |
| [SdKfz 222](sd-kfz-222.md)                             | 650                  | 1          | Driver reset, gunner/crew latch and mission-total-wave turret                                                        |
| [Goliath](goliath.md)                                  | 500                  | 1          | Weighted movement, proximity trigger and separate blast inputs                                                       |
| [Wespe, two retained placements](wespe.md)             | 1000                 | 2          | Matching selected bodies retain distinct placement identities and shared-artillery path                              |
| [Enemy Halftrack / SdKfz](enemy-jeep-and-halftrack.md) | 1000                 | 1          | Spare-driver replacement, remaining-crew unload and distinct initial pool choice                                     |

The [Nebelwerfer launcher](nebelwerfer.md) has 500 starting health and armor class 1
in its selected load, with its own setup, target and effect stages.

These are **load assignments**, before later overrides, repair, damage or crew
changes. Several have nonstock-instance guards. Names follow the selected source
map; two Wespe placements are not silently merged into one spawn profile.
The table is not a census of every enemy event or static weapon.

Armor codes are classes used by particular recipient branches, not percentage
damage reduction. The enemy Halftrack's 1000-health load is also different from
the [Allied Halftrack](halftrack.md)'s 800-health load; the common word does not
merge their rules. [Exact loads and name guards](../vehicle-load-map.md)

## What an apparent hit can mean

A projectile trigger, an emitted effect, a later AT test and a crew hit are
different questions. The inspected AT predicate reads object coordinates for
point distance; visible width is not another term in that predicate. Full
transforms, sampling and recipient state still matter.
[AT and vehicle health](anti-tank-and-vehicles.md)

Tiger's selected armor-2/Bazooka branch subtracts health rather than following
the other qualifying armor-2 direct-removal route. That exception cannot be
predicted from health alone or copied onto every `at`, `tank` or `air` tag.
[Exact helper and special tag](../anti-tank-helper.md)

The [Goliath](goliath.md)'s strict-distance trigger and later effect radius are
also separate. Its decoration index issue stays explicit; the source has not
been rewritten into an assumed wall-contact collision rule.

The [Panther/Tiger comparison](enemy-tanks.md) now binds a closer-before-armor
selection rule, distinct hull/turret loads, fixed-offset cannon effects and
mixed coax target indices. The stored-range adjustment is not read by the
selected impact-coordinate expressions; a range field alone cannot supply
its accuracy-versus-outline model.
[Exact tank component readers](../player-enemy-tank-evidence.md)
Additional source: [Source identities](../player-notes/enemy-vehicles.md#citation-1)

## Read the weapon's own receiver

The [SdKfz 222 turret](sd-kfz-222.md) rolls its own rifle from mission-total wave.
Its hull's small rifle load is another field. The turret's damage/save path
therefore needs its own context rather than an infantry stat card or the
[Allied AA cannon](aa-cannon.md)'s scattered-effect formula.

Likewise, clearing that car's driver field is not a permanent movement stop in
its selected parent controller: it resets the field and costs parent health.
Its gunner state, spare-crew latch and death accounting have different consumers.
[Exact parent and turret comparison](../player-light-vehicle-evidence.md)

For the motorcycle and truck, the retained [crew/escape comparison](../vehicle-crew-accounting.md)
already separates their flags, spare crew, momentum and counter writes. Those
facts are not a universal crew model for every row above.

The [Flakpanzer](flakpanzer.md) and [Wespe](wespe.md) parent movement bodies
instead use their own counters without a local driver/gunner gate. Their
selected health 0 comparison enters hull death, while Allied AA has a different
zero-health split. A universal “kill driver, stop vehicle” or health 0 rule would
miss these differences. [Exact guards](../player-flak-wespe-evidence.md#hull-movement-and-destruction-do-not-use-one-generic-crew-rule)

Individual attack chains, later stat writers, full arrival/exit scheduling,
transformed geometry and battle results remain partial. The
[coverage plan](../PLAYER_COVERAGE.md) tracks these remaining questions.

Sources: [Source identities](../player-notes/enemy-vehicles.md#citation-2)

Flakpanzer/Wespe detail source: [Source identities](../player-notes/enemy-vehicles.md#citation-3). [Exact new bindings](../player-flak-wespe-evidence.md)

Transport detail source: [Source identities](../player-notes/enemy-vehicles.md#citation-4). [Exact parent/gunner bindings](../player-enemy-transport-evidence.md)

Additional source: [Source identities](../player-notes/enemy-vehicles.md#citation-5). [Exact gun evidence](../player-pak38-evidence.md).

Additional source: [Source identities](../player-notes/enemy-vehicles.md#citation-6)

The [Flak38 emplacement](flak38.md) adds its own crew/setup scan and small-explosion
inputs, including a different local pinning gate from Nebelwerfer.
Additional source: [Source identities](../player-notes/enemy-vehicles.md#citation-7)

[Compare enemy mounted guns](enemy-mounted-weapons.md) for crew gates, ordered
target scans and different AT/fragment inputs.
