[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Repair, crew and reload comparison](repair-crew-and-reload.md)

# Crewman

A **3-TP recruit** that can fill particular missing crew roles. It does not
simply transfer a universal health pool into every vehicle, and its receipt is
separate from the Mechanic's health-repair action.
[Crew source](../crewman.md)

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

On this page: [Check the missing role before recruiting](#check-the-missing-role-before-recruiting), [A replacement gunner can replace the vehicle's recorded XP](#a-replacement-gunner-can-replace-the-vehicles-recorded-xp), [On-foot and mounted combat are different lifecycles](#on-foot-and-mounted-combat-are-different-lifecycles).

## Check the missing role before recruiting

The Crewman fills a supported missing crew role; the selected successful entry
branch removes the deployed Crewman. It does **not heal the hull**. Check the
recipient list below: Sherman is not one of these selected entry branches.
For low vehicle health, compare the [Mechanic](mechanic.md) instead.
[Crew transfer and recipient evidence](../crewman.md), [job comparison](repair-crew-and-reload.md).

When both gunner and driver are missing on a supported two-role vehicle, these
branches fill gunner first; one entry does not fill both at that site. Gunner
replacement can also replace the vehicle's recorded XP/rank with the Crewman's,
rather than keeping the higher values. Check the role and recipient instead of
assuming every transfer is a stat upgrade. [Exact receiver comparison](../crewman.md#gunner-replacement-copies-values-rather-than-adding-them).

Selected historical **2.3.1g**. Full live entry/unloading and click geometry remain
unqualified; the source scan's distance is not a calibrated screen radius.

In the inspected controller, the Crewman needs usable live/unpaused state, an
expired action timer, no pinning or palisade and other actor guards. A recipient
needs armor above 0 and source distance below 25. The cited role-write conditions
do not add a universal recipient-health test or establish a measured 25-pixel
entry boundary. [Actual scan conditions](../crewman.md)

| Recipient selector       | Roles in the cited branches |
| ------------------------ | --------------------------- |
| Jeep                     | Gunner, otherwise driver    |
| 20 mm AA                 | Gunner                      |
| Halftrack                | Gunner, otherwise driver    |
| AT gun                   | Gunner, otherwise driver    |
| .50-caliber position     | Gunner                      |
| Rocket-launcher selector | Gunner, otherwise driver    |

For the Jeep, missing gunner is handled before the driver alternative. Its gunner
branch copies the Crewman's rifle into the gunner component and experience/rank
into the vehicle, then removes the Crewman clip. That ordering is not proof of
atomic entry, safe unloading, which candidate wins every scan or transfer of
the soldier's health to the chassis. [Jeep-specific writes](../crewman.md)

The AA replacement has a different receiver detail: it restores gunner and
its gunz.drivermc animation, copies XP/rank to the parent, but writes rifle to
gunnermc rather than explicitly to parent rifle or gunz XP. Those latter fields
feed different AA comparisons; a new gunner is not proof of a uniform weapon-stat
upgrade. [AA-specific writes](../player-aaa-lifecycle-evidence.md#crew-replacement-does-not-bind-every-gun-stat-to-the-new-soldier)

## A replacement gunner can replace the vehicle's recorded XP

All six selected gunner branches assign the Crewman's XP and rank to the parent
vehicle. They replace the old fields rather than adding experience or keeping
the higher value. A supplied XP 80 vehicle receiving an XP 0 Crewman therefore
gets an XP 0 write at that branch; this can matter to a later XP-based counter
formula, without proving its timing or complete firing behavior.

The selected driver alternatives copy neither XP/rank nor rifle. If both roles
are 0, the gunner branch takes precedence and does not also fill the driver there.
The.50 writes rifle directly to the parent, while most others write gunnermc;
Halftrack's role-animation receiver is nested elsewhere again. A copied stat
needs its actual later reader before claiming an accuracy upgrade. These entry
writes do not heal the hull.
[Exact receiver table and supplied examples](../crewman.md#gunner-replacement-copies-values-rather-than-adding-them)

The community suggests moving the Crewman into the vehicle and describes
selection workarounds. Treat those as historical instructions requiring the
actual control/vehicle context, rather than proof every displayed crew deficit
can be repaired by the same gesture. [Mechanic](mechanic.md),
[vehicle parent/crew differences](anti-tank-and-vehicles.md)

Sources: [Source identities](../player-notes/crewman.md#citation-1). [Exact evidence](../player-roster-evidence.md)

If it remains deployed, the selected Crewman has an actual shared-helper Pistol
firing call. Its nonempty recovery uses a fresh 0–499 draw rather than the
Officer's fixed expression; matching equipment does not give identical firing
cycles. [Pistol comparison](pistol.md#the-crewman-has-a-different-recovery-expression).
Additional source: [Source identities](../player-notes/crewman.md#citation-2)

For a damaged or silent vehicle, compare [repair, crew replacement and reload](repair-crew-and-reload.md) before treating those jobs as one action.

Use the [symptom route](repair-crew-and-reload.md#start-with-the-missing-function)
to separate a missing crew role from low hull health, launcher ammunition or a
waiting counter before interpreting one transfer as a complete restoration.

## On-foot and mounted combat are different lifecycles

On-foot pistol group clearance matched Mechanic in the equal-stat modern test
(250.66 seconds at medium distance). Boarding changes the relevant driver,
gunner and mounted-weapon state; the on-foot result does not rank that vehicle.
[Lifecycle](unit-lifecycle.md), [combat results](combat-results.md).
