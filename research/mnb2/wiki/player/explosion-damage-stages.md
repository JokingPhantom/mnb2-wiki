[Player reference](README.md) · [Anti-tank options](anti-tank-options.md) · [Vehicles and emplacements](vehicles-and-emplacements.md)

# Explosion damage has several stages

**An explosion's damage number is not a universal health-loss cap.** The selected
helper has separate anti-tank, close-core, fragmentation and crew paths. A close
core can request direct removal; a later fragment path instead draws random
health damage. These are different rules.
[Exact selected source](../player-blast-core-evidence.md)

Historical scope: selected **2.3.1g** source. Distances and coordinates below
are source inputs, not certified visible safe spacing.

On this page: [A core hit is different from a fragment subtraction](#a-core-hit-is-different-from-a-fragment-subtraction) · [Keep armor, owner and protection in the example](#keep-armor-owner-and-protection-in-the-example) · [Already emitted effects still need their own recipients](#already-emitted-effects-still-need-their-own-recipients) · [Failing the AT radius does not settle every removal path](#failing-the-at-radius-does-not-settle-every-removal-path)

## A core hit is different from a fragment subtraction

For the named grenade-fragment effect, the helper receives separate inputs:

| Input    | Value | Role at the selected helper                            |
| -------- | ----: | ------------------------------------------------------ |
| Core     |    10 | Close-core distance test                               |
| AT       |     5 | Separate anti-tank distance test                       |
| Fragment |   100 | Later fragment-distance test                           |
| Damage   |   100 | Health-draw input; not a universal health-loss ceiling |

These values are source inputs, not a measured blast footprint. A qualifying close-core
player recipient with armor below 2 goes to the gib helper, whose terminal action
requests removal. That path does not first require a random 100 subtraction to
exhaust the recipient's health.

A supplied eligible 200-health, armor 0 recipient at helper distance 9 therefore
reaches that direct-removal route. At distance 10, the strict core test fails;
the separate fragment path needs its own range, line-of-sight and health gates.
With those supplied and a 99 damage draw, that latter write leaves 101 health.
[Declared inputs and boundary](../player-blast-core-evidence.md#exact-core-boundary-changes-the-selected-alternative)

These are source helper-result examples, not measured positions, a safe throwing
distance or an observed Heroism death. They explain why **200 health alone does
not protect against every removal mechanism**. [Heroism](heroism.md)

## Keep armor, owner and protection in the example

The cited player path excludes its supplied owner reference and has its own
bunker/armor condition before the core test. Armor-class 2 has a different core
alternative that draws below twice the damage argument. The earlier AT helper
also has different recipient and owner/protection checks.
[AT and vehicle stages](anti-tank-and-vehicles.md), [ownership source](../explosion-attribution.md)

A bunker save against bullets does not supply a universal explosive-save
percentage. Conversely, these core examples do not prove every bunkered soldier
is hit. Structure removal, actual overlap and the exact incoming effect still
matter. [Fortifications](explosions-and-fortifications.md), [defenses](defenses.md)

## Already emitted effects still need their own recipients

The selected helper calls scenery/AT work before its enemy and player loops.
Some effects also call structural removal before entering it. A projectile
trigger, effect creation, helper entry and later valid victim are separate
stages; do not count every emission as a kill or add all listed radii together.
[Grenades](grenades.md), [Bazooka](bazooka.md), [blast crew damage](vehicle-damage-and-crew.md)

Sources: [Source identities](../player-notes/explosion-damage-stages.md#citation-1).
Selected publisher-associated 2.3.1g; [source identities and limits](../player-blast-core-evidence.md).

## Failing the AT radius does not settle every removal path

The named grenade effect supplies AT 5 but core 10. With a supplied valid armor 1
recipient at unchanged helper distance 7 and all stated receiver conditions,
the AT distance check fails while the later core/gib route is admitted. That
is a branch example, not a qualified vehicle position or a grenade kill rate.
Use all named effect stages before concluding that a failed AT test means safety.
[Exact inputs](../player-blast-core-evidence.md#a-failed-at-distance-test-is-not-every-possible-vehicle-removal-test)
Additional source: [Source identities](../player-notes/explosion-damage-stages.md#citation-2)
