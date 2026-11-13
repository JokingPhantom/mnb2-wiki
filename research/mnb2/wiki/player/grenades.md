[Player reference](README.md) · [Weapon comparison](weapon-comparison.md) · [Combat results](combat-results.md)

# Hand grenades and rifle grenades

**Historical rules first; modern measurements are a separate [dated section](#measured-grenade-output-in-the-modern-simulation).**

**Hand grenades and rifle grenades are separate equipment states.** The selected
2.3.1g hand-grenade offer debits **1 TP** before recipient selection; the rifle-
grenade offer debits **2 TP**. Equipping either does not guarantee the next
attack will be a grenade. [Purchase and choice evidence](../player-grenade-choice-evidence.md)

On this page: [What do I get from each equipment choice?](#what-do-i-get-from-each-equipment-choice) · [Equipping, duplicating and removing](#equipping-duplicating-and-removing) · [What changes at an ordinary soldier's attack decision?](#what-changes-at-an-ordinary-soldiers-attack-decision) · [Their flight differs; their selected blast template is shared](#their-flight-differs-their-selected-blast-template-is-shared) · [Zero movement counter is followed by a separate expiry visit](#zero-movement-counter-is-followed-by-a-separate-expiry-visit) · [Measured grenade output in the modern simulation](#measured-grenade-output-in-the-modern-simulation)

## What do I get from each equipment choice?

| Equipment      | Base TP | Main difference to check                                                                                         |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------- |
| Hand grenades  | 1       | A separate capability applied through an eligible recipient; the actor still has to choose a hand-grenade attack |
| Rifle grenades | 2       | A different capability, with compatible-weapon and actor-specific launch requirements                            |

The selected rifle-launch branches admit weapon states **Springfield, M1 Garand
or M1 Carbine**: codes 1, 2 and 12 in the Allied infantry upgrade map. This does
not certify that every role accepts every combination or that the next shot
launches a grenade. [Exact launcher conditions](../rifle-grenade-launch.md),
[retained weapon-selector map](../../content/upgrade_weapons.csv).

Both inspected projectile expiry paths request the same fragmentation template;
their movement/expiry fields differ. The extra TP does not, by itself, establish
a larger blast, guaranteed longer effective range or more casualties. Those
flight and recipient distinctions are explained below.
[Flight and shared-effect evidence](../grenade-flight-comparison.md).

## Equipping, duplicating and removing

The selected ordinary/recon recipient handler requires health above 9. Buying
hand grenades sets the hand-grenade flag if absent; its duplicate alternative
returns 1 TP. Rifle grenades have their own assignment and 2-TP duplicate-return
path. Invalid recipients and overlapping pending actions need their own guards;
a menu debit is not proof equipment was received.
[Rifle recipient distinctions](../rifle-grenade-upgrade.md)

The removal offer selects hand-grenade removal. Its selected ordinary recipient
branch clears the hand flag without a TP refund there. It does not remove the
separate rifle-grenade flag. These are local source rules, not a guarantee of
every invalid click or cancellation outcome.

## What changes at an ordinary soldier's attack decision?

For one admitted **ordinary soldier using the Garand weapon state**, with a valid
nonmelee target, no bunker classification and all earlier guards passing:

| Equipment flags | Firearm animation | Rifle request | Hand request | No request here |
| --------------- | ----------------: | ------------: | -----------: | --------------: |
| Neither         |              100% |            0% |           0% |              0% |
| Hand only       |               90% |            0% |          10% |              0% |
| Rifle only      |               90% |            5% |           0% |              5% |
| Both            |               90% |            5% |           5% |              0% |

This conditional comparison assumes independent uniform random draws. It is not
an observed firing rate or hit chance. The rifle branch follows a failed first
choice and has its own second test. A failed rifle-only choice has no hand-grenade
fallback; both-equipped state can use that fallback.
[Exact inputs and ordered branches](../player-grenade-choice-evidence.md#conditional-ordinary-attack-choice)

The rifle launcher also checks the current weapon state. Its cited branches
use codes 1, 2 or 12 (the mapped rifles above); simply owning the upgrade does
not make every equipped weapon a launcher. The nearby-target exclusion specifically combines distance
below 25 **and armor zero**. It is not a universal minimum range for every target,
weapon or troop. Specialists also have different actor/priority conditions.
[Launch gates and mapped troop paths](../rifle-grenade-launch.md)

## Their flight differs; their selected blast template is shared

The hand projectile loads a 20–29 movement counter and speed 10–14. The rifle
projectile loads a 30–49 counter and speed 10. Those are source fields, not
seconds or measured throw ranges. Obstacle-blocked movement does not necessarily
stop the counter from running down. The inspected slowdown expression does not
assign a halved speed field. [Flight comparison](../grenade-flight-comparison.md)

Both inspected expiry paths request the same fragmentation effect. That does
not guarantee equal casualties: landing position, armor, protection, line of
sight, owner fields and recipient state remain separate. Friendly troops can
qualify for damage, and friendly vehicles have distinct hull/crew handling.
The ordinary bullet-save table is not a grenade survival percentage.
[Fragmentation evidence](../fragmentation-blast.md), [vehicle damage](vehicle-damage-and-crew.md),
[defenses](defenses.md)

No safe throwing distance, complete first-throw time or grenade damage per second
is established here. [Enemy grenades](enemy-grenades.md) have their own bound
movement/expiry source; those callbacks are not this equipment receipt.

Sources: [Source identities](../player-notes/grenades.md#citation-1).
Selected publisher-associated 2.3.1g; [exact evidence](../player-grenade-choice-evidence.md).

The [explosion-stage guide](explosion-damage-stages.md) distinguishes its close
core removal route from the later random fragment health subtraction. Damage 100
is not a universal maximum casualty rule for every recipient branch.
Additional source: [Source identities](../player-notes/grenades.md#citation-2)

## Zero movement counter is followed by a separate expiry visit

In the selected hand and rifle grenade callbacks, the positive-counter visit
moves if admitted and decrements the counter. Its explosion request is the
sibling alternative on a later eligible visit. With declared uninterrupted
counter 20, it takes 20 positive visits to reach 0 and a 21st eligible visit to request
the blast; rifle counter 30 similarly needs 30 then 31. These are callback counts,
not seconds or full throw-to-damage timing. The stored life 500 is not the expiry
counter read by those complete flight bodies.

An obstacle can block position writes while those decrements continue. If a
declared grenade stays at one raw point through every positive visit, its later
expiry requests the effect at that current point. These expiry sites do not
require a nearby enemy match. Actual transformed obstacles, callbacks and later
blast recipients remain separate. [Exact counts, point and owner-copy comparison](../grenade-flight-comparison.md#reaching-zero-and-requesting-the-blast-happen-on-different-eligible-visits).
Additional source: [Source identities](../player-notes/grenades.md#citation-3)

## Measured grenade output in the modern simulation

**Modern section: archived simulation results, not historical Flash. Check [editions](editions.md) and [later corrections](combat-issues.md) before applying them to a current build.**

Modern assay dated **2026-11-07**, separate from the historical source rules above.

High-XP Recon/Carbine was a strong grenade specialist. At XP/rifle 100/100,
eight seeds per configuration produced these mean launches per simulation minute:

| Equipment | Hand grenades | Rifle grenades |
| --------- | ------------: | -------------: |
| G only    |         16.90 |              0 |
| RG only   |             0 |           8.97 |
| G + RG    |          9.12 |           9.42 |

These categories are not interchangeable. G only selects hand grenades on 10%
of eligible decisions; RG only selects rifle grenades on 5% and no attack on
5%; both select 5% rifle and 5% hand. Both does not gain a higher total grenade
selection probability than G alone. Its slightly higher measured combined
launch count is not an established cadence bonus; timing and random sequences
differ. Likewise, 9.42 versus 8.97 does not prove that adding G improves RG cadence.

**Value RG output separately:** its flight has a farther travel band than G's.
The useful target distance and landing/blast geometry determine which launch
is valuable; do not add the two rates into an interchangeable damage score.
The source travel counters above do not establish universal effective minimum
and maximum ranges. This assay removed projectiles after birth, so it did not
measure effective landing ranges, damage, casualties or friendly fire.

Recon's unclamped decision reset enables frequent high-XP launches. Rookie Recon
did not show that same advantage. At XP 100, Soldier/Carbine averaged G-only
3.35 per minute; both gave G 1.45 and RG 1.60. Weapon cadence and role therefore
matter even with identical selection fractions.

Rifle grenades require Springfield, Garand or Carbine in these branches.
Thompson, Shotgun, BAR and Grease still throw eligible hand grenades but produced
zero RG. MG, Sniper and Mortar accepted hand flags but never threw.
Recon/Shotgun reached about 41 hand launches per minute, but its veteran firearm
path did not shoot: this is a problematic candidate, not a certified optimal build.
[Full weapon/role tables and assay controls](../../experiments/unit-combat-expanded-grenades.md),
[lifecycle](unit-lifecycle.md), [pending fixes](combat-issues.md).
