[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy Grenadier

The enemy Grenadier combines ordinary shooting with a separate grenade action. **Its grenade choice does not require the ordinary target search
to find one of your soldiers.** The throw branch is gated by its battlefield
position and the global explosive restriction.
[Exact action choice](../player-grenadier-evidence.md#grenadier-load-and-action-choice)

Historical scope: selected **2.3.1g**.

| Load field      | Selected starting value                                |
| --------------- | ------------------------------------------------------ |
| Starting health | 100                                                    |
| Armor code      | 0                                                      |
| Rifle skill     | Random 0 through local wave minus 1, then divided by 2 |
| Experience      | 1–50                                                   |
| Morale          | 0–99; Assault Expert Award separately subtracts 10     |

These are load defaults. Wave at load, later changes and the firing path matter;
the rifle value is not a final hit probability. [Enemy stats](enemy-stats.md)

On this page: [When it can request a grenade](#when-it-can-request-a-grenade) · [Ordinary targeting has its own restrictions](#ordinary-targeting-has-its-own-restrictions)

## When it can request a grenade

On a ready action visit, an unpinned Grenadier first has a 50-of-100 action test.
Inside that, 95 values choose target search; the other 5 can request a grenade if
its source y coordinate is strictly below 300 and explosives are allowed.
With all those stated guards supplied and independent uniform draws, **2.5% of
these ready visits request the grenade animation**: 50/100 × 5/100 = 0.025. That is not a throw rate:
the action timer, animation and later callbacks still intervene. Exactly y = 300
fails this branch. [Bindings and boundaries](../player-grenadier-evidence.md#grenadier-load-and-action-choice)

The grenade is created at the Grenadier's position. The creation action does not
copy the selected target or its facing into the grenade, whose own load sets
rotation 90. Do not read this as a proven aimed throw at the nearest soldier.
[How the enemy grenade moves](enemy-grenades.md)

## Ordinary targeting has its own restrictions

The search checks living, visible, noninvincible targets with compatible melee
state and line of sight. Its eligibility expression distinguishes pillboxed
targets from armor 1 units with crew. An armor 2 selection can double the stored
comparison range after an experience roll, affecting which later candidate wins.
This is not guaranteed nearest-target selection or proof every selected armor
class takes health damage from its firearm.
[Exact target guards](../player-grenadier-evidence.md#grenadier-load-and-action-choice)

Sources: [Source identities](../player-notes/enemy-grenadier.md#citation-1)

## Its two attack routes recover differently

Ordinary fire and grenade attacks have different exit behavior. The grenade animation ending does not itself establish a fresh fixed throw cooldown. Preparation comparisons are separate from accuracy, and timer replacements are not measured recovery seconds.

[Full source comparison and limitations](../player-notes/enemy-grenadier.md#its-two-attack-routes-recover-differently).
