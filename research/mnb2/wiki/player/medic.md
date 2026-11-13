[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Role comparison](recruitment.md#choose-the-job-before-the-price)

# Medic

A **3-TP healing specialist** that starts with **25 experience** but the ordinary
initial rank value. Its active healing sweep can visit **multiple eligible
soldiers**, rather than choosing only one nearest or most injured patient.
[Healing and rank evidence](../player-specialist-evidence.md#medic)

Applies to **historical selected 2.3.1g**. Starting values below describe the
ordinary load; career, scenario and later changes remain separate.

| Key fact                 | Selected ordinary load                                                                          |
| ------------------------ | ----------------------------------------------------------------------------------------------- |
| TP cost and availability | 3 TP; Reinforcements                                                                            |
| Health                   | 100 health points                                                                               |
| Morale                   | 10–19 before career bonuses                                                                     |
| Experience               | 25; Mud and Blood Cross adds 9                                                                  |
| Initial rank             | 0; experience does not automatically determine rank at load                                     |
| Starting equipment       | Legacy guide describes a noncombatant; a numeric weapon field alone does not prove a usable gun |

[Starting-stat evidence](../player-specialist-evidence.md)

On this page: [What to expect from the Medic](#what-to-expect-from-the-medic), [Who gets healed?](#who-gets-healed), [Rescues and experience use different tests](#rescues-and-experience-use-different-tests), [Cover and movement do not use the Mechanic's repair gates](#cover-and-movement-do-not-use-the-mechanics-repair-gates), [A healing lifecycle rather than a gun ranking](#a-healing-lifecycle-rather-than-a-gun-ranking).

## What to expect from the Medic

The Medic restores health to qualifying living unarmored soldiers. One healing
sweep can help several patients. It does not resurrect a soldier at zero health,
repair a vehicle or supply an extra ordinary rifleman. [Healing conditions](../medic-healing.md),
[Medic action scope](../player-medic-controller-evidence.md).

If healing seems to stop, check both the **patient and the Medic**: the patient
needs the right health, armor and distance; the Medic needs usable health,
positive morale, no pinning and a ready action counter. Its healing controller
does not use the Mechanic's bunker/palisade exclusion. This distinction is not a
certified safe placement or healing rate. The exact thresholds and separate
rescue-count rule are below. [Controller and movement guards](../player-medic-controller-evidence.md#movement-and-healing-have-different-guards).

Selected historical **2.3.1g**; source conditions, with no new live healing trial.

The legacy guide calls the sidearm an unusable Colt. Keep that description
separate from active firing capability: this page does not promise a combat
weapon just because the source initializes a weapon field. [Medic research](../medic.md)

## Who gets healed?

In the inspected sweep, a patient must have health **above 0 and below 100**,
armor **exactly 0**, and source distance **strictly below 50**. A passing patient
gains **1 health**. The loop can continue to other qualifying indices.
A soldier exactly at distance 50 fails that strict range check, and zero health
does not qualify as resurrection. These are source-distance tests, not a measured
visible circle at every display scale. [Sweep conditions](../medic-healing.md)

The Medic also has its own requirements: live non-template instance, unpaused,
at least 10 health, positive morale, no withdrawal/invincibility, an expired
action counter and not pinned for this healing branch. Being near a Medic does
not override the healer's condition. Its recovery-counter reset depends on a
random roll and experience; no universal healing-per-second value is certified.
[Medic entry conditions](../medic-healing.md)

## Rescues and experience use different tests

After adding the health point, this path tests whether the patient now has
**exactly 11 health**. For an ordinary integer patient, **10 → 11** triggers that
rescue branch; **9 → 10** does not yet trigger it. The branch increments a career
rescue counter and requests the patient's ordinary frame.
[Rescue source](../medic-healing.md)

The Medic's own experience gain is a separate **random 0–99 roll below 5** for
a qualifying healed patient. That is a 5-of-100 source comparison, not a fixed
“one point every 25 stitches” counter. The legacy guide's fixed-stitch statement
therefore should not replace this selected source path. Healing XP and the
promotion-helper call are also separate; gaining XP here does not certify an
immediate rank change. [XP and promotion evidence](../medic-healing.md)

The **Gallantry Medal**, with its stored medal 2 flag exactly 1, enables a
separate loop inside that rescue branch. It adds **1 XP to indexed player
entries**, rather than merely another point to the current patient. The selected
bonus loop has no extra recipient-health check and no local promotion-helper
call. This does not prove every named slot is a valid deployed actor or that
all actual soldiers receive a point or rank immediately.
[Award identity](../award-reference.md),
[Exact rescue branch and bonus loop](../medic-healing.md#a-post-addition-value-11-triggers-the-rescue-branch)

Full rescue, award and promotion outcomes remain separately unqualified.

Sources: [Source identities](../player-notes/medic.md#citation-1). Selected 2.3.1g; [exact evidence](../player-specialist-evidence.md).

The [Halftrack field hospital](halftrack-hospital.md) is a distinct healing path:
its inspected sweep adds 2 at strict distance below 75 and tests the resulting
health for exactly 11. That differs from this Medic's +1 transition 10→11; neither
comparison alone establishes healing throughput or a universal survivor count.
[Hospital source](../player-halftrack-hospital-evidence.md)
Additional source: [Source identities](../player-notes/medic.md#citation-2)

## Cover and movement do not use the Mechanic's repair gates

The selected Medic healing controller does not query bunker or palisade status;
the [Mechanic](mechanic.md) repair entry checks both. Movement has its own
obstacle and aiming conditions, but healing does not repeat a requirement to
have reached the destination or successfully moved. These are source admission
differences, not a certified protected placement or a measured moving heal rate.
[Exact controller scope](../player-medic-controller-evidence.md#movement-and-healing-have-different-guards)

Its recovery counter is assigned **before** the sweep's later XP gains. Those
points do not recalculate the already written value. A positive timer simply
decrements here, without the Mechanic's above-100 adjustment; pinned state can
block a fresh sweep while that separate decrement remains eligible.
[Counter order and supplied inputs](../player-medic-controller-evidence.md#the-reset-precedes-this-sweeps-experience-gains)

The Medic's own controller and six retained own action bodies contain no
ordinary enemy acquisition or shared firing call. A weapon field should not
turn this source-backed healing role into an assumed spare rifleman.
[Finite source boundary](../player-medic-controller-evidence.md).
Additional source: [Source identities](../player-notes/medic.md#citation-3)

[Wounded, rescued or dead?](wounded-and-rescued.md) compares action/count thresholds,
healing eligibility and the separate exact-health rescue branch.

Additional source: [Source identities](../player-notes/medic.md#citation-4)

## A healing lifecycle rather than a gun ranking

Medic remained nonfiring in the expanded modern experiment. Its job is a guarded
healing sweep, potentially visiting multiple patients. The firearm clearance
table cannot value rescues or squad survival.
[Lifecycle and wounded states](unit-lifecycle.md), [test limits](combat-results.md).
