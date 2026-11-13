[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Repair, crew and reload comparison](repair-crew-and-reload.md)

# Mechanic

A **3-TP repair specialist**. The inspected repair path has different health
entry thresholds for particular recipient types, rather than one universal
“repair any armored object” rule. [Repair evidence](../mechanic.md)

Applies to **historical selected 2.3.1g**. Starting values below describe the
ordinary load; career, scenario and later changes remain separate.

| Key fact                 | Selected ordinary load                      |
| ------------------------ | ------------------------------------------- |
| TP cost and availability | 3 TP; Reinforcements                        |
| Health                   | 100                                         |
| Rifle skill              | Starts at 5 with random-stop 1–10 additions |
| Morale                   | 10–19 before career bonuses                 |
| Experience               | 0 before career bonuses                     |
| Starting equipment       | Pistol                                      |

[Starting-stat evidence](../player-roster-evidence.md)

On this page: [Repairing health is a separate job from restoring crew](#repairing-health-is-a-separate-job-from-restoring-crew), [Repairing competes with a fresh enemy search](#repairing-competes-with-a-fresh-enemy-search), [Repair and personal combat are separate](#repair-and-personal-combat-are-separate).

## Repairing health is a separate job from restoring crew

Use the Mechanic for the supported damaged vehicles and gun positions listed
below. A qualifying scan can add health to several recipients; it does not fill
a missing driver or gunner, or reload an empty rocket launcher. Compare those
jobs before buying another support recruit. [Repair, crew or reload?](repair-crew-and-reload.md),
[repair scan](../player-mechanic-scan-evidence.md).

If it is not repairing, check the recipient's type, health and distance, then
the Mechanic's own readiness and protection: its selected repair entry excludes
both bunker and palisade classification. A wrench animation alone is not proof
that every nearby recipient gained health. [Entry gates](../mechanic.md),
[animation versus health writes](../player-mechanic-scan-evidence.md#the-repair-flag-survives-later-nonrepairing-candidates).

Selected historical **2.3.1g**. Thresholds below are entry tests, not one universal
maximum health or a measured repair speed.

For a vehicle that is still silent after repair, start with the
[missing-function checks](repair-crew-and-reload.md#start-with-the-missing-function)
before treating hull health, crew, ammunition and the firing counter as one state.

The selected controller needs usable live actor state, an expired timer, no
pinning and **no palisade or bunker classification**. Its recipients need armor
above 0 and source distance strictly below 150. A visually nearby vehicle is not
a guarantee the whole repair path is eligible.
[Exact actor/recipient guards](../mechanic.md)

| Recipient type       | Health must be below this value to enter the addition |
| -------------------- | ----------------------------------------------------- |
| Jeep                 | 500                                                   |
| 20 mm AA position    | 300                                                   |
| AT gun               | 500                                                   |
| .50-caliber position | 200                                                   |
| Sherman              | 1000                                                  |
| Halftrack            | 800                                                   |

Each cited branch adds a random **1–6 health**. These thresholds are not assignments
to a maximum: for a Jeep at 499, adding 6 would produce 505 at that write, before any
other clamp/writer. That is a conditional arithmetic example, not certification
that 505 is a persistent final health ceiling or that every vehicle can overshoot.

The timer gate is checked before the recipient loop, so one admitted scan can
repair more than one qualifying indexed vehicle. Repairing the first does not
break the scan or retest the timer before the next. A later full-health armored
candidate can also receive the wrench-animation request after an earlier repair
has set the shared local repair flag; that animation alone does not prove its
health increased. [Scan and animation distinction](../player-mechanic-scan-evidence.md#the-repair-flag-survives-later-nonrepairing-candidates)

Each repair writes a random timer, but a later assignment in the same controller
overwrites those values and applies a floor of 20. With supplied XP 10, that final
comparison maps 21 of 200 integer draws to 20, not a uniform 20..199 range. The
positive-timer path has its own decrement and upper 100 adjustment. None of these
counters alone gives repairs per second.
[Timer order and inputs](../player-mechanic-scan-evidence.md#per-recipient-timer-writes-are-not-the-callbacks-last-timer-write) Crew replacement
and weapon-component state are separate. [Crewman](crewman.md),
[vehicles](anti-tank-and-vehicles.md)

Sources: [Source identities](../player-notes/mechanic.md#citation-1).
Selected 2.3.1g; [exact evidence](../player-roster-evidence.md).

## Repairing competes with a fresh enemy search

A successful repair in the admitted scan suppresses that scan's new enemy
search. If no repair occurs, the Mechanic searches for a closer eligible living,
visible enemy with line of sight; a closer ineligible enemy does not reserve
the distance. A selected unarmored enemy strictly below helper distance 25
can request melee instead of the Pistol preparation path. This does not prove
that repairing cancels a firing animation already underway.
[Exact arbitration and selection](../player-mechanic-combat-evidence.md#a-successful-repair-scan-takes-priority-over-new-acquisition)

The Mechanic's selected early Pistol actions match the Officer's, but its
nonempty recovery matches the Crewman's: **10 plus a 0–499 draw minus XP**.
At supplied XP 20, draws 0/499 write −10/489; the Officer's corresponding
nonempty expression writes 80. Empty-ammo recovery writes 200 minus XP and
refills eight. These counters are not firing intervals or proof of immediate
shots from a negative value.
[Actual role-specific bodies](../player-mechanic-combat-evidence.md#matching-early-pistol-bodies-do-not-identify-the-entire-role-cycle)
Additional source: [Source identities](../player-notes/mechanic.md#citation-2)

For a damaged or silent vehicle, compare [repair, crew replacement and reload](repair-crew-and-reload.md) before treating those jobs as one action.

## Repair and personal combat are separate

Mechanic's pistol matched Crewman's equal-stat modern group clearance
(250.66 seconds at medium distance). That says nothing about repair value.
Repair health does not restore missing crew, and repair decisions have their
own recipient and protection guards.
[Lifecycle](unit-lifecycle.md), [combat results](combat-results.md).
