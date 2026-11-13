[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy truck

The enemy truck starts with **1000 health, armor code 1, driver/gunner fields
of 1 and spare crew 1–8**. The spare-crew field is separate from its active
driver and gunner state. It can be spent replacing a gunner or on a later infantry
spawn; it is not an immediate guaranteed count of healthy enemy arrivals.
[Exact load and crew paths](../vehicle-crew-accounting.md#the-trucks-spare-crew-is-separate-from-driver-and-gunner)

Historical scope: selected **2.3.1g**.

| Key fact             | Historical default or behavior                                              |
| -------------------- | --------------------------------------------------------------------------- |
| Starting hull health | 1000                                                                        |
| Armor code           | 1                                                                           |
| Crew                 | 1–8 spare crew; driver and gunner flags 1                                   |
| Important limit      | Spare crew can replace a gunner before the later one-at-a-time unload check |

On this page: [Spare crew can replace a cleared gunner](#spare-crew-can-replace-a-cleared-gunner) · [Unloading creates a separately indexed soldier](#unloading-creates-a-separately-indexed-soldier) · [Replacing a gunner happens before the unload check](#replacing-a-gunner-happens-before-the-unload-check) · [An empty truck can start moving back](#an-empty-truck-can-start-moving-back) · [Abandonment and advancement use different tests](#abandonment-and-advancement-use-different-tests)

## Spare crew can replace a cleared gunner

In the selected active living truck branch, gunner **exactly 0** and positive
spare crew restore gunner to 1 and reduce crew by 1. The check does not replace
a driver and is not a rule for every negative gunner value.

Movement uses its own state: with positive moving counter and driver, it adds
0.5 to y. Without a positive driver, that selected alternative stops the moving
state, with another ordered decrement in the enclosing branch. Those writes
are source state changes, not a measured movement speed or a universal vehicle
immobilization rule. [Crew and movement](../vehicle-crew-accounting.md#the-trucks-spare-crew-is-separate-from-driver-and-gunner)

## Unloading creates a separately indexed soldier

With the truck active, positive health, nonpositive moving state and spare crew,
a random integer 0–99 comparison below 1 can call the infantry-spawn helper and
spend one crew point. That is one qualifying draw value on a reached callback,
not one soldier per second or a guaranteed unloading time.

The helper has selected Regular, Volkssturm and Grenadier template branches,
writes the new enemy y to the truck y minus 60 and advances the enemy index.
The resulting infantry has its own load and later state. A crew field, a spawn
request and a healthy deployed enemy are different quantities.
[Exact helper and recipient coordinates](../vehicle-crew-accounting.md#unloading-creates-a-separately-indexed-infantry-actor)

## Replacing a gunner happens before the unload check

A missing gunner can spend the last spare crew point before unloading is tested.
For an admitted nonmoving-state visit, a missing gunner and one spare crew
point leave no spare crew after replacement, so this visit cannot request an
infantry unload. With two spare crew points, replacement leaves one and a
passing unload comparison can spend that point on one new infantry request.
These are source-state examples, not two guaranteed arrivals or an unload rate.
[Exact order](../player-truck-lifecycle-evidence.md#a-replacement-gunner-can-consume-the-last-possible-unload-slot)

The helper places its selected Regular/Volks/Grenadier at truck y minus 60 and
truck x plus or minus 50. It does not copy the truck's combat stats at those
placement sites. Infantry load callbacks and the wave seen there remain separate.
[Template/position boundaries](../player-truck-lifecycle-evidence.md#the-unload-helper-chooses-a-new-actor-rather-than-transferring-truck-stats)

## An empty truck can start moving back

The selected nonmoving, no-positive-crew, positive-driver alternative subtracts
0.5 from y; it differs from the forward movement path. A driver loss in the
positive-moving branch instead writes moving to 0 and then decrements it to −1, without
entering the unload alternative in that same visit. The final y<0 removal is
another distinct source test. [Movement/return order](../player-truck-lifecycle-evidence.md#an-emptied-truck-has-a-distinct-return-and-boundary-removal)

## Abandonment and advancement use different tests

The selected truck life decrement requires driver below 1 and spare crew below 1,
alongside its active positive-health conditions. It tests spare crew rather than
the gunner field. The general advancement helper instead has a separate armored-
slot driver/gunner-sum test and does not include spare crew in that predicate.
Do not copy the motorcycle's two exit increments onto this truck or count every
stored crew point as one immediate miss.
[Abandonment](../vehicle-crew-accounting.md#abandonment-timers-have-different-guards),
[advance accounting](../vehicle-crew-accounting.md#advancement-uses-one-armored-slot-predicate)

A truck's local health-destruction loop counts remaining spare crew, while the
AT armor 1 path has additional driver/gunner/common counter sites. With supplied
crew 3/driver 1/gunner 1, those selected local increments are 3 versus 6. They are not
a certified net kill total for an actual explosion or a fixed reward per truck.
[Counter paths](../player-truck-lifecycle-evidence.md#health-destruction-and-at-removal-have-different-local-kill-writes)

Full firing, wreck/crew-damage ordering, arrival/exit and fade timing remain
partial. The retained community Opel description is separately versioned; it
does not turn every source truck field into a certified historical occupant count.
[Enemy vehicle overview](enemy-vehicles.md)

Sources: [Source identities](../player-notes/enemy-truck.md#citation-1)
