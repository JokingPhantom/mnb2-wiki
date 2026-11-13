[Player reference](README.md) · [Vehicles and emplacements](vehicles-and-emplacements.md) ·
[Repair, crew or reload?](repair-crew-and-reload.md)

# 20 mm AA cannon

A **20-TP placed cannon** with a selected parent load of **300 health, armor
class 1 and one gunner**. It has both ground-fire and anti-air source paths.
Buying the gun is different from buying radar or making the 1-TP air-superiority
request. [Air-defense choices](air-defense.md), [exact source](../player-aaa-evidence.md)

Applies to **historical selected 2.3.1g**. Starting health, crew and counters
are source load fields; they do not guarantee arrival or a complete attack.

| Key fact                     | Selected historical load                                |
| ---------------------------- | ------------------------------------------------------- |
| TP cost and availability     | 20 TP; placement/completion retests affordability       |
| Health / maxhealth           | 300 / 300                                               |
| Armor class                  | 1                                                       |
| Gunner / driver / spare crew | 1 / 0 / 0                                               |
| Experience / rank            | 2 / 0; Mud and Blood Cross adds 9 XP at its load branch |
| Initial action counter       | 20 source units                                         |

[Starting-field evidence](../player-aaa-evidence.md).

On this page: [What to check before expecting air protection](#what-to-check-before-expecting-air-protection), [The unit and gun component have different stats](#the-unit-and-gun-component-have-different-stats), [Replacing the gunner does not replace every stat](#replacing-the-gunner-does-not-replace-every-stat), [Ground fire is a scattered explosion effect](#ground-fire-is-a-scattered-explosion-effect).

## What to check before expecting air protection

The cannon, Radar and Air Superiority are different purchases or requests.
This **20-TP cannon** has guarded anti-air attempts and a separate ground-fire
path; it is not a guaranteed shield against every aircraft or support event.
[Air-defense systems](air-defense.md), [anti-air request/attempt evidence](../player-aaa-evidence.md#anti-air-arming-and-consumption).

For a silent or damaged cannon, separate hull health, a missing gunner and the
current ground/air action. Those paths use different crew and stat readers.
Gunner replacement also does not explicitly replace every parent/gun field, so
a veteran replacement is not proof both attack modes improved.
[Crew and receiver limits](../player-aaa-lifecycle-evidence.md#crew-replacement-does-not-bind-every-gun-stat-to-the-new-soldier).

These are selected **2.3.1g** source distinctions, not a measured interception
rate, completed replacement or guaranteed firing fix.

The offer enables placement, then a separate completion retests affordability
and charges 20 TP before the spawn helper's own capacity guard. A pending pointer
is not proof a cannon was delivered. [Purchase/load boundaries](../player-aaa-evidence.md#parent-and-child-are-separate-stat-receivers)

## The unit and gun component have different stats

The parent rifle initializer uses a random stopping loop, then Combat Ribbon's
+3. The separately loaded gun component instead starts at **1–10 XP and rifle 5–14**.
That distinction matters: the selected **ground burst counter uses the gun's XP**,
while the **anti-air comparison uses the parent's rifle**. Combining the two
objects into one stat row would misdescribe both paths.

## Replacing the gunner does not replace every stat

A qualifying [Crewman](crewman.md) can fill this cannon's missing gunner. That
branch copies XP/rank to the parent, but its rifle write names gunnermc rather
than the gunz component used by the weapon notes. It does not explicitly replace
parent rifle or gunz XP. Do not assume a veteran replacement automatically
improves every anti-air and ground-fire comparison. The exact receiver and
callback effects still need qualification.
[Recrew and zero-health predicates](../player-aaa-lifecycle-evidence.md#crew-replacement-does-not-bind-every-gun-stat-to-the-new-soldier)

## Ground fire is a scattered explosion effect

Ground acquisition needs a usable gunner, unpaused state and no active anti-air
burst, plus target and protection gates. Its scan compares a parent's distance
but stores a child's distance after selection, so it cannot yet be described
as uniformly choosing the nearest target. It differs from the M3's first-armored
slot priority. [Distance receivers](../player-aaa-lifecycle-evidence.md#ground-selection-mixes-parent-and-child-distance-receivers) Bunker classification tests the
parent, while a palisade query tests the child, so precise placements still need
transformed geometry. [Ground-source chain](../player-aaa-evidence.md#ground-selection-and-effect)

Selected firing frames place a small explosion around the target's coordinates,
with integer offsets −100 through +99 on each axis. Its later blast call supplies
**AT radius 2, fragment radius 50 and separate damage input 100**. These are not
unconditional health loss or the M3 AT gun's AT 50 / damage 300 inputs.
[Anti-tank recipients](anti-tank-and-vehicles.md), [M3 AT gun](m3-at-gun.md)

Two effect-creation frames write different owner fields; final credit and
friendly/self-recipient outcomes remain separate. The ground burst counter and
frame requests are not a measured number of shells or a firing-rate statistic.

## Anti-air attempts spend their counter before the result

Selected enemy requests set a qualifying cannon's anti-air counter to 20 and
request its gun component play. Health>0 and gunner exactly 1 gate those request
recipients. A later attempt subtracts one counter unit **before** its bunker check
and rifle comparison, so a counter decrement does not prove a successful shot.
[Request and attempt bindings](../player-aaa-evidence.md#anti-air-arming-and-consumption)

For a supplied parent rifle 20, the isolated random 0–399 comparison accepts 20
values: 5%. That is per stated comparison, not overall interception probability
or twenty independent attempts before a plane arrives. Successful handling also
resets other qualifying guns. Plane stopping and the separate crash animation
roll are different outcomes. [Detailed anti-air behavior](../anti-aircraft-burst.md)

## The aircraft's later reset checks a different crew field

The selected enemy-aircraft action 20 resets a20mm entries only with positive
health and **driver exactly 1**. The request-arming path above uses **gunner
exactly 1** instead. The cannon's selected load starts driver 0/gunner 1: with those
fields unchanged it passes that crew part of arming, but fails that crew part
of the later aircraft reset. Other guards and callback order still apply.

For a passing reset recipient, the aircraft clears airburst, writes the child
gun's counter to 100+random(100)−child XP and navigates that gun to 1. This is a
separate source writer, not a guarantee that every armed cannon receives a
reset or an observed stuck-gun report.
[Exact aircraft reset](../player-enemy-air-evidence.md#bombing-and-gun-reset-are-separate-actions)

Sources: [Source identities](../player-notes/aa-cannon.md#citation-1). [Version and exact evidence](../player-aaa-evidence.md)

## The Air defence Ribbon counter is not only a plane-loss count

The selected ground effect carries the tag **air**. In an admitted enemy core
or lethal-unarmored blast branch, the shared medal helper uses that tag to
increment the same career counter used by the Air defence Ribbon. It does not
check for an aircraft type there. The gun's anti-air success has another writer.

The Ribbon's source threshold is counter **at least 100**, with a separate
medal-check/display path. This source join does not establish a ground-kill
farming rate or an awarded/saved Ribbon, but it does mean the field cannot be
read as a verified count of aircraft destroyed.
[Exact ground effect, counter helper and award gate](../player-air-defence-counter-evidence.md)
Additional sources: [Source identities](../player-notes/aa-cannon.md#citation-2)

The selected AA release handler uses driver 1 for new waypoint focus, while its
named load sets driver 0/gunner 1. Its inspected parent route rotates toward a
stored target without a normal waypoint position step. A working gunner does
not therefore establish that the emplacement can be moved like the M3.
[Selection versus parent movement](../player-vehicle-movement-evidence.md#a-stationary-guns-driver-field-is-not-its-firing-crew).
Additional source: [Source identities](../player-notes/aa-cannon.md#citation-3)
