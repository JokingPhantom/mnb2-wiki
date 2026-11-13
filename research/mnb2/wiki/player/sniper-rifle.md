[Player reference](README.md) · [Weapon comparison](weapon-comparison.md) · [Equipment](training-and-equipment.md)

# Sniper rifle

The Sniper's starting weapon has a **0–199 health damage draw after an eligible
unarmored hit** and a one-round ammunition/refill path. The selected source
calls it Sniper rifle; the legacy guide calls the equipment Scoped Springfield.
Its weapon branch has no added distance modifier, but target acquisition,
accuracy and armor handling still apply.
[Exact weapon and actor evidence](../player-sniper-rifle-evidence.md)

Historical scope: selected **2.3.1g** source. Modern findings, where listed,
are separate observations.

| Key fact                          | Selected historical behavior                                |
| --------------------------------- | ----------------------------------------------------------- |
| Cost and access                   | Sniper starting weapon; base recruit 6 TP                   |
| Initial/refilled ammunition       | 1 round; refill depends on actor state                      |
| Eligible unarmored damage draw    | 0–199 health; may draw zero                                 |
| Weapon-specific distance modifier | None in this branch; accuracy and target checks still apply |

[Recruitment and starting load](sniper.md); [weapon evidence](../player-sniper-rifle-evidence.md).

On this page: [Does no distance penalty mean every shot hits?](#does-no-distance-penalty-mean-every-shot-hits) · [Experience affects different stages](#experience-affects-different-stages) · [Target priority is not simply closest or lowest score](#target-priority-is-not-simply-closest-or-lowest-score)

## Does no distance penalty mean every shot hits?

No. In selected **2.3.1g**, the absence of a weapon-specific distance modifier
leaves the other accuracy, target, sight and actor checks in place. The 0–199
damage draw describes an eligible unarmored hit, and can itself draw zero; it
does not promise that a fired shot hits or kills. The Sniper's preparation and
one-round refill are separate stages of its own attack cycle.
[Shared weapon and Sniper actor](../player-sniper-rifle-evidence.md#shared-weapon7-and-actual-actor828-have-separate-responsibilities)

The Sniper can search without the enemy's positive visibility counter, but still
has line-of-sight and other eligibility rules. Use the [Sniper role card](sniper.md)
for concealment and recruitment; the rifle's damage range alone does not explain
which enemy it selects or how quickly it attacks.
[Target-selection evidence](../player-sniper-rifle-evidence.md#sniper-priority-is-compared-with-a-raw-stored-distance)

## Experience affects different stages

The Sniper has an experience-dependent preparation check before a later firing
frame. With supplied XP 0/20/100, that reached comparison passes 10/30/110 of 200
integer draws. Success requests a later firing stage; it does not itself create
a hit or establish elapsed aiming time.

Its selected unpaused, movement-state 1 recovery writes a counter of 200 minus
experience and ammunition 1 for this weapon. At XP 20 that counter is 180; at
XP 100 it is 100. This is not a measured reload in seconds, and its separate
movement/pause branches must remain part of a full cycle.
[Preparation and refill bindings](../player-sniper-rifle-evidence.md#shared-weapon7-and-actual-actor828-have-separate-responsibilities)

## Target priority is not simply closest or lowest score

The selected Sniper search compares a candidate's distance divided by its
priority, but stores raw distance after accepting one. A later candidate can
therefore replace an earlier one without having the best weighted score of
all candidates. Scan order matters under the declared source inputs.
[Worked two-candidate comparison](../player-sniper-rifle-evidence.md#sniper-priority-is-compared-with-a-raw-stored-distance)

Its selected search also does not require the enemy's positive visibility
counter, while line of sight and other eligibility gates remain. That does
not globally reveal every enemy to the squad or make a concealed Sniper immune.
Read the [Sniper pilot](sniper.md) for recruitment, starting stats and concealment.

For damage to crews and tanks, follow [small-arms recipient branches](small-arms-against-vehicles.md).
A larger unarmored damage draw does not itself grant vehicle-hull penetration.

Sources: [Source identities](../player-notes/sniper-rifle.md#citation-1).
Selected publisher-associated 2.3.1g; [exact source identities](../player-sniper-rifle-evidence.md).

[The preparation comparison](../player-pre-fire-gate-evidence.md#fixed-experience-changes-the-passing-input-count)
uses twice the ordinary soldier's draw bound at these named sites. At supplied
XP 90, the ordinary gate accepts all 100 inputs while the Sniper gate accepts
100 of 200. This is a comparison of reached gates, not a measured first-shot
race, overall effectiveness ranking or a change to the accepted Sniper pilot.
Additional source: [Source identities](../player-notes/sniper-rifle.md#citation-2)

The [named enemy priority table](enemy-stats.md#priority-is-a-separate-load-field-used-by-a-sniper-selector)
shows actual load inputs behind this selector. The Officer/Grenadier example
explains why current scan order still matters despite different priority values.
