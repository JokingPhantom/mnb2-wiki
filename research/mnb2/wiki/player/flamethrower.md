[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Role comparison](recruitment.md#choose-the-job-before-the-price)

# Flamethrower soldier

A **3-TP soldier for attacking nearby enemies with flame**. It can damage an
unarmored enemy or turn one into a burning hazard. That hazard and a flamer
explosion can also threaten nearby troops, so check [fire and burning](fire-and-burning.md)
and [collateral damage](collateral-damage.md) before planning its position.
[Flame source paths](../flamethrower.md)

Start with your question: [How far can it target, and who can the flame hit?](#target-range-damage-and-spreading-fire-are-different-checks),
[does experience improve every attack check?](#experience-does-not-improve-every-selected-comparison), or
[what can endanger nearby troops?](#burning-soldiers-and-tank-explosions-are-separate-hazards).

Applies to **historical selected 2.3.1g**. Starting facts use the ordinary load;
career additions and other conditions are labeled separately.

| Key fact                 | Selected ordinary load                                         |
| ------------------------ | -------------------------------------------------------------- |
| TP cost and availability | 3 TP; Reinforcements                                           |
| Health                   | 100                                                            |
| Rifle skill field        | Starts at 10 with random-stop 1–10 additions                   |
| Morale                   | 10–19 before career additions                                  |
| Experience               | 0 before career additions                                      |
| Firing model             | Actor/component flame path, not one shared bullet damage value |

[Starting-stat evidence](../player-roster-evidence.md)

## Target range, damage and spreading fire are different checks

The selected target search needs distance **strictly below 180 source units**.
The later flame effect checks which eligible enemies its shape touches; its
victims are not limited to the enemy being aimed at. The targeting distance is
not a measured visible flame length or a guaranteed hit on the selected enemy.
[Target versus component evidence](../player-flamer-acquisition-evidence.md#selected-target-distance-and-flame-shape-victims-are-separate).

A flame hit can subtract health or create a separate burning hazard. The
hazard's later spread and a flamer explosion follow different rules from that
first hit; ordinary bullet cover does not establish safety from all three.
[Fire and burning](fire-and-burning.md), [collateral damage](collateral-damage.md).

Rifle skill and XP do not describe every part of this attack with one accuracy
or damage-rate statistic. Flame uses different rules from ordinary bullets;
a matching weapon-code field does not give it the Grease Gun's firing behavior.
This is selected **2.3.1g** source guidance, not a tested safe firing layout.

This selected load has the Combat Ribbon rifle addition; its rifle-load writes
do not show the Medal of Honor addition present in many other recruit profiles.
That is a bounded load-source difference, not proof the actor never gains any
other later benefit. [Exact load evidence](../player-roster-evidence.md#mortar-and-flame)

## A flame hit can take different paths

In one component scan, an eligible living unarmored enemy must pass a shape-hit
test. A random-below 40 branch creates a separate burning hazard and removes the
scanned enemy; the alternative subtracts random 0–49 health. These are guarded
component visits, not a universal 40% kill probability per whole attack.
The later death-call index in one alternative differs from the scan/subtraction
index, so accounting/removal needs its actual binding.
[Conversion and index distinction](../flamethrower.md)

The actor's burst counter depends on experience, but repeated timeline visits
are not a measured fire rate. The community's range/vehicle-immunity advice
remains attributed until geometry and all caller paths are qualified.

## Burning soldiers and tank explosions are separate hazards

A converted burning clip has its own lifetime, spread and removal paths; it is
not automatically the original controllable recruit. Nearby player/enemy spread
checks have different health thresholds. Changing its burn counter at water
contact does not alone restore the removed soldier or prove every intervening
spread scan is skipped. [Burning hazard](../burning-hazard.md), [water](../fire-and-water.md)

Certain attack branches can emit a flamer explosion. Its generic explosion call
and additional burn-conversion scans have different recipient/protection rules.
Do not assume one 50-unit fragment radius or a bunker makes every part safe.
[Separate flamer explosion paths](../flamer-explosion.md)

Sources: [Source identities](../player-notes/flamethrower.md#citation-1).
[Exact evidence](../player-roster-evidence.md)

## Acquiring a target is not the flame's damage footprint

The selected search requires an eligible target at **strictly below 180 source
distance**, with sight, visibility, armor/crew and other checks. That is not a
measured 200-pixel flame length. The later flame component has its own victim
shape scan, so the aim target and actual burn recipients are different questions.
[Search versus component victims](../player-flamer-acquisition-evidence.md#selected-target-distance-and-flame-shape-victims-are-separate)

## Experience does not improve every selected comparison

One later controller distance test reads the completed scan index rather than
the stored selected target. Its fallback requests an attack only when a random
0–99 draw is greater than twice XP. Conditional on reaching that fallback,
XP 0/20/49/50 give 99/59/1/0 passing draws out of 100.

These counts do not establish that experienced flamethrowers stop working in
play: the actual indexed receiver, earlier branches and callback/order entry
still need qualification. Other XP checks affect preparation and burst state;
the separate component burn-conversion comparison uses a fixed below 40 test.
Do not replace all of these with one accuracy or rate bonus.
[Exact indices and declared inputs](../player-flamer-acquisition-evidence.md#a-later-distance-check-reads-the-completed-scan-index)

For the separate risks to nearby troops, see [collateral damage and friendly fire](collateral-damage.md).

[Fire, burning soldiers and water](fire-and-burning.md) compares separate hazard
objects, both-side spread, steam and the remaining rescue/lifetime limits.

## Range, experience and unresolved test failures

The following comparison uses the **November 7, 2026 modern simulation build**.
It is separate from the historical source facts above and from later corrections.
[Study conditions and build limits](combat-results.md).

The reached modern acquisition path needs targets below 180 source units.
Medium/far test targets were outside it. Even close targets did not trigger
XP-100 fire: the reached fallback requires random(100) > 2×XP and cannot pass
at XP 50+. XP-25 single-target follow-ups did fire and averaged about 10–13 seconds.

The archived group tests exposed burning-source context errors and
positive-health removals later traced to last-ally game-over cleanup. Their
original means remain unqualified. After the burning-source and observer
corrections, four retained cases clear with 20 genuine kills each; this does
not requalify the full study or provide a new overall ranking. Community also
corrects the post-scan receiver; the XP fallback above remains an explanation
of the archived build and Remaster, not a current Community firing guarantee. [All flame findings and fix status](combat-issues.md).
