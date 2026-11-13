[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Role comparison](recruitment.md#choose-the-job-before-the-price)

# Machine gunner

A **4-TP support recruit** with a machine gun and movement-related setup states.
Its firing paths differ: one has a count-dependent accuracy roll, while another
uses the shared infantry firing helper. One machine-gun number cannot describe
both. [Firing-path evidence](../player-specialist-evidence.md#machine-gunner)

Applies to **historical selected 2.3.1g**. Starting facts use the ordinary load;
career additions and other conditions are labeled separately.

| Key fact                 | Selected ordinary load                                       |
| ------------------------ | ------------------------------------------------------------ |
| TP cost and availability | 4 TP; Reinforcements                                         |
| Health                   | 100 health points                                            |
| Rifle skill              | Starts at 10 with random-stop 1–10 additions                 |
| Morale                   | 10–19 before career bonuses                                  |
| Experience               | 0 before career bonuses                                      |
| Initial ammunition field | 200; not proof of 200 delivered shots per every reload cycle |
| Starting equipment       | Machine gun; community identifies a Browning.30              |

[Starting-stat evidence](../player-roster-evidence.md)

On this page: [Positioning and firing expectations](#positioning-and-firing-expectations), [Moving affects setup state](#moving-affects-setup-state), [More Gunners can change one Gunner's roll](#more-gunners-can-change-one-gunners-roll), [Suppression and changing targets](#suppression-and-changing-targets), [Bunkered acquisition differs from ordinary infantry](#bunkered-acquisition-differs-from-ordinary-infantry).

## Positioning and firing expectations

Movement changes the Gunner's setup state; setup in turn selects different
firing paths. Let the distinction guide how you read a pause after relocation,
without assuming a fixed deployment time. The selected destination/setup guards
and the Gunner's actual state still matter. [Setup evidence](../machine-gunner.md),
[path selection](../player-gunner-path-evidence.md).

A missed shot can lead to a separate pinning attempt, so damage and suppression
are different outcomes. Neither every miss nor every burst pins a target.
Adding Gunners also changes one path's accuracy comparison through a stored
Gunner count; this is not evidence that another recruit always improves or
reduces total squad performance. [Firing and count comparison](../player-specialist-evidence.md#machine-gunner),
[pinning](../pinning.md).

Selected historical **2.3.1g**; no measured firing-rate, optimal Gunner count or
universal bunker damage bonus is established by these source distinctions.

Career rifle/morale/experience additions are separate from these defaults.
The old card's narrower rifle/morale ranges are community presentations, not
a substitute for the selected random-stop load pattern.
[Source and community comparison](../machine-gunner.md)

## Moving affects setup state

In the inspected guarded controller, being more than 3 source coordinate units
from the destination on either axis resets setup to 0. The stationary alternative
increments it and changes 100 to 101. Health, morale, pause, withdrawal, obstacles,
aiming and close-combat state still gate these updates. “Standing still” does
not by itself establish a universal deployment time in seconds.
[Setup transitions](../machine-gunner.md)

## More Gunners can change one Gunner's roll

One selected firing path multiplies a random 0–199 roll by a count obtained from
the machine-gunner counting helper. That helper counts player entries typed as
Gunners and has no health check inside its counted branch. Cleanup and count
refresh therefore matter. A positive burst also adds twice its current value
to the roll compared with rifle skill.

As a narrow illustration, with **rifle 40, burst 0, and no other changes**, this
path's raw comparison passes 41 of 200 rolls at count 1, 21 at count 2 and 14 at
count 3. This is a per-shot comparison-stage derivation, not evidence that buying
another Gunner lowers the squad's total kills or that every Gunner shot uses
this formula. [Count and path evidence](../player-specialist-evidence.md#machine-gunner)

The other cited path calls the shared helper, with a different initial roll.
The paths also have different damage-draw bounds:125 in the direct unarmored
branch, 100 for shared weapon 10. Do not average them into one guaranteed damage
stat. [Machine-gunner source comparison](../machine-gunner.md)

## Suppression and changing targets

A failed accuracy test can lead to a separate pinning check against the target's
morale. A miss is not automatically useless, but neither is every miss a pin.
The shared retarget branch uses a random test involving 10 plus experience and
chooses from a previously built candidate array. It can pick the same enemy;
it is not a guaranteed spread of suppression or a special threshold at 20 XP.
[Pinning](../pinning.md), [retargeting](../machine-gunner.md)

In that shared helper, distance is stored before the possible target change.
A successful retarget updates the target and aim, but the range modifier still
reads the earlier distance at that site. A newly selected nearby enemy can thus
inherit a distance modifier based on the old target. This is a source-order
comparison, not a measured target-switch delay or a rule for the separate direct
Gunner firing path. [Exact order and supplied example](../player-gunner-retarget-evidence.md#distance-is-stored-before-the-shared-weapon10-branch-changes-target)

The community recommends deployed and bunkered Gunners. Their full bonuses,
state transitions and comparative performance need separate qualification;
[bullet defenses](defenses.md) alone do not settle offensive benefits.

Sources: [Source identities](../player-notes/machine-gunner.md#citation-1).
[Exact evidence](../player-specialist-evidence.md)

## Bunkered acquisition differs from ordinary infantry

The inspected Gunner ready search does **not** repeat ordinary infantry's extra
bunker-dependent below 15 chance. Its own usable-state, pinning, palisade and
target gates still apply. This gives a concrete source distinction behind the
bunker comparison, without establishing a damage multiplier or a full firing-rate
bonus. A pillbox's separate palisade classification still matters.
[Exact admission scope](../player-gunner-path-evidence.md#this-ready-search-has-no-ordinary-extra-bunker-chance)

## Setup selects different source paths

The ready nonmelee branch below setup 100 requests the direct route. Its other
branch requests the setup route and builds a candidate array. The reached
direct frame 8 and shared-helper frame 60 therefore must keep their own accuracy,
damage and retarget readers; the array is not automatically rebuilt for each
later shot.
[Selected navigation and preparation](../player-gunner-path-evidence.md#preparation-requests-differ-by-selected-source-action)

Both inspected empty-ammo recovery actions refill 200 and write 400 minus XP.
But one returns to stopped 1, while the other requests the setup label again.
These destinations, pause guards and later counter changes prevent that number
from being a universal reload time in seconds or a guaranteed 200-shot burst.
[Repeat and recovery destinations](../player-gunner-path-evidence.md#repetition-and-recovery-preserve-their-different-destinations)
Additional source: [Source identities](../player-notes/machine-gunner.md#citation-2)

The load's stopping loop makes at least one rifle addition before testing whether
to stop. It is not five fixed rolls or a total 1–10 bonus. The conditional mean
under independent uniform inputs is 21 before medal additions; actual recruits,
later writes and both attack readers remain separate.
[Exact loop and supplied-input limits](../player-random-stop-load-evidence.md).
Additional source: [Source identities](../player-notes/machine-gunner.md#citation-3)

A count stored during acquisition is not a live roster query at the direct shot.
An entry still typed as Gunner can count even at zero health; a later change in
roster type does not by itself rewrite the stored multiplier. A new controller
count and the direct shot's later read must be kept separate. This does not
establish when actual casualty cleanup or refresh happens.
[Stored count versus fresh count](../player-gunner-path-evidence.md#a-fresh-roster-count-does-not-rewrite-the-stored-shot-multiplier)

## Measured crowd-clearing strength

The following comparison uses the **November 7, 2026 modern simulation build**.
It is separate from the historical source facts above and from later corrections.
[Study conditions and build limits](combat-results.md).

At equal veteran stats, an already-deployed MG cleared twenty fresh humans in
19.19/20.07/52.82 simulation seconds at close/medium/far centerlines. Its live
target switching is a major advantage: an earlier intervention preventing that
switching increased mean clearance from 20.32 to 84.75 seconds.

This does not measure deployment cost, survival, squad-size accuracy effects or
movement. MG need not get the fastest first kill against one enemy. Hand-grenade
flags produced no throws in the assay.
[Results and controls](combat-results.md), [equipment issue](combat-issues.md).
