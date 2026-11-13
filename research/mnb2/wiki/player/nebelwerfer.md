[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy Nebelwerfer launcher

The Nebelwerfer is an enemy launcher with **500 starting health, armor class 1 and
one driver/one gunner**. Its firing action creates an explosion near a selected
player's later coordinates. The source load's rifle and XP are not inputs to
that inspected spread expression. [Exact source](../player-nebelwerfer-evidence.md)

Historical scope: selected **2.3.1g**.

| Starting field         | Historical default   |
| ---------------------- | -------------------- |
| Health                 | 500                  |
| Armor code             | 1                    |
| Driver flag            | 1                    |
| Gunner flag            | 1                    |
| Spare crew             | 0                    |
| Rifle skill            | 1–10                 |
| Experience             | 20                   |
| Rank                   | 0                    |
| Morale                 | 0–99                 |
| Setup counter          | 100–399 source units |
| Initial action counter | 0–249 source units   |

This rifle load does not use local wave. That is not a promise the field has no
later writer. A catalogued Mobile artillery event requests three launchers
alongside Pak38 requests; nominal requests are not certified living arrivals.
[Wave/event distinction](waves.md), [event source](../blitz-reference.md)

On this page: [Setup, movement and pinning affect different stages](#setup-movement-and-pinning-affect-different-stages) · [It does not always choose armor ahead of closer infantry](#it-does-not-always-choose-armor-ahead-of-closer-infantry) · [Its selected shot is a scattered effect request](#its-selected-shot-is-a-scattered-effect-request)

## Setup, movement and pinning affect different stages

A positive setup counter decreases separately from the movement checks.
Movement's selected branch needs an unwired, unaiming actor with positive crew
sum and a passing random comparison. Setup reaching zero does not also enter
the next action branch on that same source visit.

The later expired action branch writes a fresh **200–449 counter before its
pinning test**. A supplied pinned launcher can therefore get that reset without
acquiring a target at that site. These counters are not a measured setup or
reload time.
[Exact guards and counter order](../player-nebelwerfer-evidence.md#movement-and-setup-do-not-have-identical-admission)

## It does not always choose armor ahead of closer infantry

Candidates need health above 9, positive visibility, no invincibility flag
and line of sight. The scan accepts a closer candidate before checking whether
its positive armor should end the scan. Earlier eligible nearby infantry can
therefore prevent a farther armored entry from reaching that armor preference.
Scan order still matters; this is not a certified bait placement.
[Two-candidate source example](../player-nebelwerfer-evidence.md#armor-can-end-the-scan-only-after-the-closer-test-passes)

## Its selected shot is a scattered effect request

The firing action places an effect around the target's later point using
separate **−100..+99 axis offsets**. It does not read rifle or XP there. The
later effect supplies **AT radius 50, fragment radius 50 and damage input 300**
with tag at; those are separate helper inputs, not unconditional damage or
an outline hitbox. Effect-owner copying remains unresolved at this emission.
[Effect, repeat and owner boundary](../player-nebelwerfer-evidence.md#a-reached-shot-creates-an-effect-near-later-target-coordinates)

Crew loss also has its own consequences. The scan needs a positive driver-plus-
gunner sum, while losing both starts a separate fade/removal counter path.
The nonpositive-health wreck branch instead adds the current crew sum to a kill
statistic before removal. A crew hit, a wreck and a counted kill are different
source operations. [Crew/accounting source](../player-nebelwerfer-evidence.md#wreck-accounting-and-crewless-fading-are-separate),
[small-arms crew effects](small-arms-against-vehicles.md)

Sources: [Source identities](../player-notes/nebelwerfer.md#citation-1).
Selected publisher-associated 2.3.1g; no new salvo, geometry or encounter trial.
