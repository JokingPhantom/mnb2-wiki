[Player reference](README.md) · [Recruitment](recruitment.md) · [Reading stats](reading-stats.md)

# Wounded, rescued or dead?

**Positive health, an active soldier and a credited rescue are different states.**
In selected 2.3.1g, ordinary soldier action gates and one mission-survivor count
need at least 10 health. Named healing paths can admit lower positive health,
while rescue credit tests another exact threshold.
[Exact source and reader scope](../player-wounded-state-evidence.md)

For triage, a soldier at **1–9 health** is neither automatically a functioning
rifleman nor proven dead. It can fail ordinary action and usable-survivor tests
while still passing a healer's patient-health test. If no indexed soldier meets
the cited survivor threshold, that mission-ending path can still request loss;
positive health does not guarantee time for a rescue. [Health and mission-end evidence](../player-wounded-state-evidence.md).

| Player question                                              | Selected threshold / distinction                                                |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| Can an ordinary soldier do its main active work?             | Health at least 10, plus its other conditions                                   |
| Can it count as a usable survivor in the cited mission scan? | Defined health at least 10                                                      |
| Can it receive Medic or kit healing?                         | Above 0 and below 100, plus patient armor/range and the healer's own conditions |
| When does the selected healing path credit a rescue?         | Exactly 11 health after its addition                                            |
| When does the cited fatal-only health test pass?             | Health below 1 at that later test                                               |

A death-animation request alone does not prove health 0 or a casualty-counter
increase. Actual animation dispatch, still-present actors and later callbacks
remain separate. [Health and statistics](reading-stats.md)

On this page: [Ten health does not mean every job is ready](#ten-health-does-not-mean-every-job-is-ready) · [What can heal a wounded soldier?](#what-can-heal-a-wounded-soldier) · [Healing enough to count and receiving rescue credit are separate](#healing-enough-to-count-and-receiving-rescue-credit-are-separate) · [The mission can count no usable survivors while health remains positive](#the-mission-can-count-no-usable-survivors-while-health-remains-positive)

## Ten health does not mean every job is ready

At a **supplied health value of 10**, these selected **2.3.1g** tests differ:

| Named test                                              | Health requirement | Does 10 pass this health test? |
| ------------------------------------------------------- | ------------------ | ------------------------------ |
| Ordinary soldier's cited main active work               | At least 10        | Yes                            |
| Medic's own cited healing entry                         | At least 10        | Yes                            |
| Engineer scanned by the Mortar-pit menu offer           | Above 10           | No                             |
| Officer and Signaller scanned by the Bombing menu offer | Each above 10      | No                             |

The “yes” rows do not promise movement or healing: the other actor, timer,
patient and state conditions still apply. The “no” rows explain why passing an
ordinary active-health threshold need not make a particular build or radio
offer available. Sufficient TP alone does not remove those role-health checks.
[Active/healing thresholds](../player-wounded-state-evidence.md),
[Mortar-pit offer](../player-construction-detail-evidence.md#two-construction-paths-and-one-menu-side-existence-test),
[Bombing role chain](../bombing-request.md)

Do not copy one row onto every construction, support call or specialist. A
patient's healing admission and exact rescue-credit threshold are different
tests again, as described below. Sources: [Source identities](../player-notes/wounded-and-rescued.md#citation-1)

## What can heal a wounded soldier?

| Support                                     | Health per admitted visit | Strict source distance | Other conditions                                          |
| ------------------------------------------- | ------------------------- | ---------------------- | --------------------------------------------------------- |
| [Medic](medic.md)                           | +1 health                 | Below 50               | Active healer state and its sweep counter/guards          |
| [Airborne healing kit](healing-kit.md)      | +1 health                 | Below 50               | Positive kit pool at entry; spends per qualifying patient |
| [Halftrack hospital](halftrack-hospital.md) | +2 health                 | Below 75 from hull     | Its module/hull/timer conditions; different rescue step   |

The named patient scans also need health above 0/below 100 and armor 0. They are
not resurrection for health 0, repair for an armored hull or measured healing
per second. Multiple eligible patients can be visited; actual positions and
callbacks still matter. [Repair versus crew versus healing](repair-crew-and-reload.md)

## Healing enough to count and receiving rescue credit are separate

For a supplied eligible patient, **Medic 9→10** crosses that survivor-count health
threshold but does not take the exact 11 rescue branch. A later eligible **10→11**
visit does. That intermediate count result is not proof the patient's animation
or weapon already resumed; healing receipt and action navigation still matter.

The hospital's **9→11** can take its rescue branch in one admitted +2 visit,
while **8→10** does not. With only repeated +2 changes, an even-health sequence
skips 11; other damage or healing can change the sequence. This explains a counter
boundary, not which healer is universally fastest or best.
[Exact comparisons](../player-wounded-state-evidence.md#healing-and-counted-rescue-use-another-threshold)

## The mission can count no usable survivors while health remains positive

The cited death helper counts slots with defined health at least 10. If all
supplied indexed health values are 9, that count is 0; if unchanged at its final
test, it requests gameover. Positive health alone is therefore not a guarantee
that a rescue opportunity remains after every mission-ending path.
[Mission source](../player-wounded-state-evidence.md#playerdeath-counts-usable-survivors-before-its-fatal-only-block),
[withdrawal and mission end](withdrawal-and-mission-end.md)

That helper also has lifetime/best-soldier bookkeeping outside its fatal-only
block. A statistics update or a death label should not be read as a complete
permanent-casualty receipt. Full end-of-mission saving and actual rescue outcomes
remain unqualified by this source comparison.

Sources: [Source identities](../player-notes/wounded-and-rescued.md#citation-2).
Original explanation; no new wound, rescue, mission-loss or timing trial.
