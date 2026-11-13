[Player reference](README.md) · [Weapon comparison](weapon-comparison.md) · [Combat results](combat-results.md)

# How an infantry unit moves, decides and acts

A soldier’s **health, morale, ammunition, timers and current action** determine what it can do next. An expired timer permits a decision rather than an automatic shot. Movement, support work, orders and damage can interrupt the cycle. Historical source stages and dated modern observations are labeled separately below.

The sequence below explains source-derived behavior implemented in the modern
simulation. Named historical rules come from selected 2.3.1g evidence; modern
measured timings are labeled separately.
[Ordinary source stages](../player-weapon-evidence.md#ordinary-soldier-cycle).
Modern measurements on this page retain their November 7 build scope. New
modern Officers start with a Carbine and can use ordinary weapons; the old
pistol package is still a historical/existing-loadout case, not their only
current attack. [Revision comparison](../player-evidence-reconciliation-101.md).

On this page: [The ordinary Soldier cycle](#the-ordinary-soldier-cycle) · [Why a shorter timer can make shooting slower](#why-a-shorter-timer-can-make-shooting-slower) · [Sarge and Officer support does not require an enemy](#sarge-and-officer-support-does-not-require-an-enemy) · [What does one update mean?](#what-does-one-update-mean) · [Role-specific deviations](#role-specific-deviations) · [Wounding, pinning, withdrawal and removal](#wounding-pinning-withdrawal-and-removal)

## The ordinary Soldier cycle

1. **Recruit.** Assign starting stats, weapon, ammunition, rank and timers; apply the relevant career/scenario additions. XP and rank are separate fields.
2. **Enter and move.** Follow the destination if movement guards permit it. Aiming, melee, wire, obstacles, withdrawal and off-board state can matter.
3. **Check readiness.** Check usable health, morale, pinning, protection and the action timer. A positive timer normally counts down instead of admitting a fresh decision.
4. **Choose work.** Run the role's support, healing, repair or enemy-search logic.
5. **Acquire.** Ordinary infantry scans living eligible enemies, checking visibility, LOS and melee compatibility, generally retaining the closest eligible candidate.
6. **Choose attack.** Close combat, firearm, hand grenade or rifle grenade according to the target, equipment and role.
7. **Prepare.** Enter aiming and initialize weapon counters. A later XP-dependent gate passes toward firing or restarts preparation.
8. **Attack and repeat.** Resolve the shot or emit a projectile; ammunition and burst/semi state decide continuation.
9. **Recover.** Refill where appropriate, write the weapon recovery timer, clear aiming and return toward readiness.

A failed preparation check returns to aiming; it is not an accuracy miss. Rifle
skill influences the later hit comparison, while XP also influences decisions,
preparation and recovery. [Shooting stages](how-shooting-works.md);
[exact frame landmarks](../player-shooting-stage-trace.md#lifecycle-landmarks-and-clock-implementation).

## Why a shorter timer can make shooting slower

The controller and animation both write timers and request frames.
Recon resets its decision timer to random(100)+20−XP without Soldier's minimum 20. At high XP, it can decide to fire again before reaching the firing gate,
sending itself back to preparation frame 2. Here random(100) is a uniform
integer draw from 0 to 99, and XP means experience: at XP 100, this reset
can write −80 through 19. Those are source counters, not elapsed seconds.

In retained Carbine seed 5001 at medium distance, Soldier's first shot occurred
at step 6, Recon's at 13; frame-2 observations were 24 versus 129 and group
clearance 44.40 versus 52.95 seconds. This illustrates preparation interruption,
not a universal delay ratio. Once the firing gate is reached, its large timer
helps protect the firing sequence.

Grenade emission is requested directly in the decision branch, so frequent
decisions benefit grenade output without waiting through the same firearm
preparation. [Recon](scout.md), [study](../../experiments/unit-combat-expanded.md).

## Sarge and Officer support does not require an enemy

Both choose support before enemy search. With no eligible enemy, support can
still occur; combat search simply finds no attack target. Neither is a constant
passive firing-speed aura.

Sarge chooses support on 50% of eligible ready decisions. Its random job can
unpin nearby allies, train the first eligible nearby Officer below 50 XP, or
increase low morale. A failed job does not fall through into shooting.
**Successful and unsuccessful support branches both leave Sarge's timer unchanged.**

If it stays expired and all other guards still pass, Sarge can reconsider on
the next update. With independent 50/50 choices and uninterrupted readiness,
combat search happens on the first opportunity with probability 50%, one update
later with 25%, two later with 12.5%. The expected additional wait is one update.
This is not a 50% firing-rate loss; attacks and later recovery have their own duration.
[Sarge's recipient limits and combat](sarge.md).

Officer aid entry instead passes a 25% roll and an XP-based roll, requires
nonmelee state, and checks a shared aid cooldown. Aid can rally troops, raise
morale, generate TP below the relevant bank threshold or reduce flanking-enemy
accounting. Its animations and selected outcomes have their own timing.
[Officer aid](officer.md).

## What does one update mean?

The modern page uses a fixed **50 ms simulation step: 20 steps per simulation
second**. Rendering can run at another rate; wall-clock catch-up can execute
several simulation steps during one browser wake. Pause or speed settings affect
wall time, not the logical duration of a simulation step.
[Clock implementation and landmarks](../player-shooting-stage-trace.md#lifecycle-landmarks-and-clock-implementation).

The original Flash movie also declares **20 FPS**, a nominal 50 ms per movie
frame. It uses enter-frame handlers and movie-clip frame actions. A frame can
contain several action callbacks; a navigation request can execute another frame's
action within that update. A stopped animation does not imply its controller
stops receiving enter-frame events.

Matching nominal rate does not prove callback-order or elapsed-time parity for
every role. Sarge's next eligible enter-frame visit is nominally about 50 ms
later; the complete original-runtime Sarge sequence has not been qualified.
Some oracle experiments drive browser RAF in 40-ms increments. Those are
emulator-driver increments, not a 25-FPS game declaration.
[Original clock evidence](../../CLOCK_REVIEW.md).

A raw timer assignment is not automatically timer × 50 ms: decrements,
overwrites, caps, animation transitions and guards decide when work actually resumes.

## Role-specific deviations

| Role         | Changes to the cycle                                                                                                                                                  |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Soldier      | Ordinary reference cycle.                                                                                                                                             |
| Spec Ops     | Garand/Carbine repeat counter 1–5 instead of 1–3; Grease burst preparation; different movement and pin recovery; low morale alone does not select withdrawal.         |
| Resistance   | Different Garand/Thompson recovery; different natural recruit stats.                                                                                                  |
| Recon        | No ordinary minimum decision reset; movement can proceed while aiming; special spotting/support readers.                                                              |
| Sarge        | Local support before combat search; ordinary-style weapon handling and distinct support/voice decisions.                                                              |
| Officer      | Aid before combat search, shared cooldown, distinct historical pistol repeat/recovery and officer promotion ladder; current modern Officers can use ordinary weapons. |
| Engineer     | Ordinary-style gun combat plus separate construction, defusing and explosive interactions; native Grease preparation.                                                 |
| Signaller    | Gun combat plus call/retry/completion actions. Accepting a request is separate from delivering support.                                                               |
| Paratrooper  | Landing and possible injuries before combat; an equipped healing-kit attempt can replace fresh enemy search; distinct pin recovery.                                   |
| MG           | Stationary setup required; moving resets setup; firing can change live targets within a sequence.                                                                     |
| Mortar       | Setup, minimum distance and sight/spotter gates; emits an independently moving shell.                                                                                 |
| Sniper       | Hidden-target eligibility and priority-dependent selection; harder preparation roll and separate one-round recovery.                                                  |
| Bazooka      | Separate preparation, shot accounting, rocket birth, flight and backblast stages.                                                                                     |
| Flamethrower | Short-range acquisition, flame contact/propagation and burning actors; see pending combat issues.                                                                     |
| Medic        | Healing sweeps replace normal enemy attacks and can visit multiple patients.                                                                                          |
| Mechanic     | Repair work with recipient-specific conditions alongside pistol combat; repair does not restore crew.                                                                 |
| Crewman      | Pistol on foot; boarding transfers its role to the vehicle/emplacement crew system.                                                                                   |

The [role articles](README.md#recruits-vehicles-and-placed-weapons) explain each
job. Equal displayed stats do not equalize these controllers.

## Wounding, pinning, withdrawal and removal

Pinning interrupts ordinary work and has a separate recovery process. Clearing
pinning need not restore morale, clear a withdrawal order or erase another timer.
Low morale can initiate ordinary fleeing; explicit withdrawal has its own route.

Ordinary active work generally requires at least 10 health. A unit at 1–9 can
be incapacitated yet still healable; jobs and rescue credit use distinct thresholds.
Death animation, health loss, casualty credit, corpse creation and removal are
separate stages. Burning, gibbing and legitimate retreats or tactic-change cleanup
can follow different paths. A projectile/effect may continue after its owner dies.
[Wounded and rescued](wounded-and-rescued.md).

The isolated flame test's four healthy removals were later traced to last-ally
game-over cleanup. Healthy terminal survivors are excluded from kills. This
does not make legitimate living-enemy cleanup a bug. [Investigation limits](combat-issues.md).

[Original opening and evidence context](../player-notes/unit-lifecycle.md#opening-before-player-language-correction).
