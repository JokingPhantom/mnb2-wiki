[Player reference](README.md) · [Defenses](defenses.md) · [Support](support.md)

# Explosions, fortifications and their occupants

**Protecting a soldier and surviving an explosion are different questions.**
A bunker can supply a bullet save or pass a blast-protection query, while a
separate structure-removal helper can select the bunker itself. The selected
2.3.1g source does not give every fortification one shared health/durability rule.
[Exact source and limits](../player-fortification-blast-evidence.md)

On this page: [Which structure is tested?](#which-structure-is-tested) · [Do not freeze the protection result before the blast](#do-not-freeze-the-protection-result-before-the-blast) · [Use the protection rule for the incoming attack](#use-the-protection-rule-for-the-incoming-attack)

## Which structure is tested?

| Selected mechanism           | What it tests                                                                     |
| ---------------------------- | --------------------------------------------------------------------------------- |
| Ordinary bullet cover        | Soldier point against a named cover shape; trench and sandbag share this category |
| Bunker classification        | Object overlap against a bunker or pillbox                                        |
| Selected bunker demolition   | Bunker type, with effect-to-structure helper distance strictly below 25           |
| Selected palisade demolition | Palisade type, with that distance strictly below 45                               |

For example, a supplied bunker helper distance of 24 passes its distance
comparison; exactly 25 does not. Structure type and every other guard still
have to pass, and this alone says nothing about an occupant dying.

The last two distances are source helper inputs, not artwork-edge clearances
or a placement guide. The demolition body does not require a prior structure-
health subtraction reaching zero. Pillboxes, trenches and sandbags are absent
from its selected type branches; that does not make them indestructible against
every other effect.
[Different type and distance rules](../player-fortification-blast-evidence.md#explo2-calls-structural-removal-before-its-general-blast-helper)

## Do not freeze the protection result before the blast

The selected explo2 effect calls the fortification-removal helper before its
general explosion helper. TNT also has a source route through scenery removal
before its blast helper. The later occupant-protection query examines current
structures; it is not a stored promise from when the soldier first entered.
[Selected source order](../player-fortification-blast-evidence.md), [TNT](../scenery-demolition.md)

If the only matching bunker has actually been removed before that query, and
nothing else qualifies, the query has no matching bunker to return. This does
not certify the occupant's death: other objects, recipient eligibility, range,
line of sight, damage and actual callback order still matter. Adding ordinary
cover does not itself grant a bunker-only blast exemption.

## Use the protection rule for the incoming attack

[Bullet stacking](defenses.md) covers specific firearm saves. [Backblast](bazooka.md)
and [enemy flame](enemy-flamethrower.md) have different victim tests. Visible walls,
a faded pillbox, or one successful bunker query are not universal immunity.
Exact transformed placements and complete destruction/casualty outcomes remain
shared reconstruction work.

Sources: [Source identities](../player-notes/explosions-and-fortifications.md#citation-1). Selected 2.3.1g;
[source identities](../player-fortification-blast-evidence.md).

The common blast first runs a different scenery helper with effect/object tests.
Its Sandbag/improvised-wall removal has a below-50 random comparison; its net
branch requests a wreck/removal without that choice gate. Active HQs have a
separate frame-2 request. These precede the later conditional bunker dispatch,
including for frag/air tags that skip that later call.
[Exact first-helper branches and current-state limits](../player-blast-dispatch-evidence.md#the-first-helper-also-handles-sandbags-and-support-structures)
Additional source: [Source identities](../player-notes/explosions-and-fortifications.md#citation-2)
