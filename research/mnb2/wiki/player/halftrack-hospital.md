[Player reference](README.md) · [Vehicles and emplacements](vehicles-and-emplacements.md) ·
[Halftrack roles](halftrack.md)

# Halftrack field hospital

A **10-TP module conversion** on a Halftrack. Its inspected healing sweep can
add **2 health to multiple eligible soldiers** within strict source distance 75
of the hull. It replaces the vehicle's module role and clears the mobile
HQ/radar/antenna flags in its purchase handler.
[Module selection](halftrack.md), [exact purchase and component](../player-halftrack-hospital-evidence.md#purchase-and-physical-component)

Applies to **historical selected 2.3.1g**.

| Key fact                 | Selected module behavior                                                                         |
| ------------------------ | ------------------------------------------------------------------------------------------------ |
| TP cost and availability | 10 TP conversion on a Halftrack; base vehicle costs a separate 12 TP                             |
| Healing                  | Adds 2 health per eligible indexed patient; multiple patients can qualify                        |
| Range condition          | Strict source distance below 75 from hull, not a calibrated screen radius                        |
| Important limits         | Replaces the old module and clears mobile support flags; healing entry does not require a gunner |

[Module and healing evidence](../player-halftrack-hospital-evidence.md).

On this page: [What needs to be ready?](#what-needs-to-be-ready), [Healing and a counted rescue are different](#healing-and-a-counted-rescue-are-different), [A timer expression is overwritten later](#a-timer-expression-is-overwritten-later).

## What needs to be ready?

Unlike the [weapon modules](halftrack-weapons.md), the selected hospital healing
entry **does not require a gunner**. It still needs its active, unpaused,
noninvincible hull context, a ready timer and eligible patients. That source
difference does not certify every wreck, crew-loss or module-switch outcome.
[Exact healing entry](../player-halftrack-hospital-evidence.md#healing-entry-and-patient-scan).

Its +2 health per passing patient is not evidence of twice the Medic's healing
rate. Their movement, protection and timer rules differ; no universal throughput
winner is qualified. [Medic](medic.md), [timer writes](../player-halftrack-hospital-evidence.md#the-later-timer-overwrites-the-xp-expression).

| Patient condition     | Inspected requirement                    |
| --------------------- | ---------------------------------------- |
| Health before healing | Above 0 and below 100                    |
| Armor                 | Exactly 0                                |
| Distance from hull    | Strictly below 75                        |
| Change                | +2 health for each passing indexed entry |

It does not choose just the nearest or most injured soldier; one admitted sweep
can visit multiple eligible indices. The patient checks and healer-entry checks
remain separate.
[Exact scan](../player-halftrack-hospital-evidence.md#healing-entry-and-patient-scan)

## Healing and a counted rescue are different

The rescue branch checks for **exactly 11 health after healing**. A supplied
9-health patient becomes 11 and enters that branch; an 8-health patient becomes
10 and does not. With only repeated +2 changes, an even starting health skips 11. Other injury/healing can change that sequence.

The branch increments a career rescue counter and requests the patient's
ordinary frame. With the selected medal flag, it also runs a separate XP loop
over player indices. That reward is not restricted to the current patient.
[Rescue and XP bindings](../player-halftrack-hospital-evidence.md#rescue-accounting-and-squad-xp-loop)

The health gate is checked before adding 2: a supplied 99 can become 101 in this
body, while exactly 100 does not qualify. That is a local arithmetic result,
not a certified permanent health cap or guaranteed survival.

## A timer expression is overwritten later

The scan first writes a timer expression involving the child's experience,
then replaces the timer with a fresh 0–199 draw after the scan. Quoting only
the first write would misstate the final local assignment. Full callback timing
is still unresolved, so these counters are not a healing-per-second statistic.
[Exact writers](../player-halftrack-hospital-evidence.md#the-later-timer-overwrites-the-xp-expression)

The [Medic](medic.md) has a different selected sweep: +1 health, strict distance
below 50, its own usable-state guards and XP behavior. These source differences
do not establish a universal winner without movement, protection and timing.

Sources: [Source identities](../player-notes/halftrack-hospital.md#citation-1)
