[Player reference](README.md)

# Reaction, repeat fire and reload are different delays

For an ordinary soldier, **finding a target, aiming, firing, repeating and
recovering are separate steps**. A refill timer
such as 250 minus experience does not tell you the time from an enemy appearing
to the first shot—or the time needed to switch to another enemy.
[Exact ordinary-soldier path](../player-weapon-evidence.md#ordinary-soldier-cycle)

Applies to **historical selected 2.3.1g ordinary infantry**. Modern timing
observations are labeled in the final section.

| Stage           | What the soldier does                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------ |
| Ready to look   | Checks health, pinning, protection and whether its action counter has expired                    |
| Find a target   | Searches eligible living visible enemies, considering distance and line of sight                 |
| Aim             | Starts aiming and sets the equipped weapon's repeat counters                                     |
| Prepare to fire | Passes an experience-dependent random check; failure can restart preparation                     |
| Fire            | Resolves the equipped weapon's attack                                                            |
| Repeat          | Checks ammunition and repeat counters before requesting another shot or continuing the animation |
| Recover/refill  | Uses the weapon's own recovery and ammunition rules in the qualifying movement state             |

[Exact frame requests and source trace](../player-shooting-stage-trace.md).

These are source navigation/callback facts. The complete host/timeline scheduling
and ordinary runtime transition model are still needed before publishing exact
first-shot or next-target seconds.

Choose the stage you are asking about:

- [Accuracy, rifle skill and effective caps in the modern game](rifle-skill.md)
- [Readiness and the first fire request](#ready-state-and-the-first-fire-request)
- [Repeats, ammunition and recovery](#repeats-ammunition-and-recovery)
- [Choosing and changing targets](#choosing-and-changing-targets)
- [Role-specific continuation](#a-different-role-uses-different-continuation)

## What should I check while the soldier waits?

**First decide whether you are seeing no attack, a delay between attacks, or an
attack that caused no damage.** Those problems need different responses:

- **No attack:** inspect health, morale, pinning, current orders and the target.
  Use the [nonfiring checklist](why-soldiers-stop-shooting.md) before paying for
  another weapon or training; higher rifle skill does not clear those blockers.
- **A pause after firing:** check the actual role and weapon. A pause can be
  recovery, preparation or a repeat decision, rather than an empty magazine.
  Rebuying the weapon is not a general refill command.
- **A new enemy is ignored:** target choice and changing targets are separate
  from repeating a shot. Check target eligibility and line of sight instead of
  treating every repeat as a fresh search.
- **Shots occur but health does not fall:** compare armor, crew, protection and
  the weapon's damage rules. A visible attack is not proof of a useful hit.
  [Small arms against vehicles](small-arms-against-vehicles.md).

Watch for the relevant next event: a shot, projectile, changed target or actual
health loss. No single waiting time proves the cause. For a purchase decision,
compare [weapon tradeoffs](weapon-comparison.md) with the
[complete recruit-plus-equipment cost](purchase-budgets.md).

## Ready state and the first fire request

### What can delay acquiring a target?

The inspected ordinary controller requires the actor to be healthy enough,
unpaused, with positive morale, not withdrawing, not invincible, timer below 1
and not pinned for the target-selection path. It also has palisade/bunker gates.
A bunkered actor's selected acquisition branch requires an additional below 15
random comparison where its unbunkered alternative does not.
[Acquisition guards](../player-weapon-evidence.md#ordinary-soldier-cycle)

The target scan checks living enemies, armor/crew eligibility, a closer distance
than the current selected range, positive visibility, melee-state compatibility
and line of sight. It does not automatically attack the weakest or highest-value
enemy. A Sniper's hidden-target path must be investigated separately.
[Sniper](sniper.md), [source targeting](../player-weapon-evidence.md#ordinary-soldier-cycle)

After the relevant action-choice block, the controller assigns **random 0–99
plus 20 minus experience**, then raises results below 20 to 20. Another active
positive-counter path decrements it and caps a still-above 100 value to 100.
Those operations are distinct from the later post-fire weapon recovery writes.
They also show why a timer read from an earlier nested branch may be overwritten
later in the same callback.

The ordinary controller can choose [close combat](close-combat-and-bayonets.md)
for its selected unarmored target strictly below 25 source distance, before the
firearm/grenade alternative. A first-shot scenario must therefore specify target
armor, distance and melee state rather than assuming every ready decision fires.
[Exact admission](../player-close-combat-evidence.md#ordinary-admission-is-separate-from-the-later-helper)

### A bounded experience comparison

Experience affects both the target-search counter and a later preparation check. The Sniper uses a different preparation draw; none of these input counts is an elapsed first-shot or retarget time.

[Full source comparison and limitations](../player-notes/how-shooting-works.md#a-bounded-experience-comparison).

### Experience also changes a preparation check before the fire request

[Full source comparison and limitations](../player-notes/how-shooting-works.md#experience-also-changes-a-preparation-check-before-the-fire-request).

## Repeats, ammunition and recovery

### Repeating a shot is not simply another target search

When ordinary infantry starts aiming, it sets Garand/Carbine semi counters to 1–3,
Thompson burst to 1–6 and BAR burst to 1–20. Those are initialized counters, not
promises of that many hits or a universal shot count for every state.

When checking whether to repeat, positive ammo and burst request another shot and a
burst decrement. With semi remaining instead, the selected repeat check uses a
random 0–19 roll below **1 plus experience divided by 10**. A failed semi check
requests another animation stage rather than guaranteeing an immediate new
shot. Pause and empty ammo have their own alternatives.
[Repeat and navigation bindings](../player-weapon-evidence.md#ordinary-soldier-cycle)

### A refill table needs an actor and state

These are **ordinary character 623, frame 15, unpaused, movement-state 1** writes,
when the listed weapon's ammo is below 1. The timer column is a source counter;
it is not elapsed seconds or the whole attack cycle.

| Weapon     | Refill to | Recovery-counter assignment |
| ---------- | --------- | --------------------------- |
| Garand     | 8         | 250−experience              |
| Thompson   | 30        | 150−experience              |
| Shotgun    | 8         | 200−experience              |
| BAR        | 20        | 200−experience              |
| Grease Gun | 30        | 150−experience              |
| M1 Carbine | 15        | 200−experience              |

With ammo remaining, those branches can assign different counters. Weapon
replacement also does not by itself prove the ammo field was immediately reset
to the eventual refill value. Do not copy this actor's table onto a Sniper,
vehicle component, or every visually stationary/moving state.

Full first-shot, same-target and next-target reconstruction remains a high-priority
shared recipe task. These source-backed stages already explain why a single
infobox “fire rate” hides several different questions.

Sources: [Source identities](../player-notes/how-shooting-works.md#citation-2).
[Exact evidence](../player-weapon-evidence.md)

### A refill assignment can be shortened by a later controller

A later controller can shorten an inherited refill counter. Springfield’s recovery floor, ordinary acquisition floor and other weapon recovery assignments belong to different stages. Counter arithmetic is not a measured reload duration; all active-state conditions still apply.

[Full source comparison and limitations](../player-notes/how-shooting-works.md#a-refill-assignment-can-be-shortened-by-a-later-controller).

### Replacing a weapon is not a complete attack-state reset

The selected ordinary recipient handler changes the weapon field without an
ammo, burst or semi write. Preparation then initializes the selected weapon's
repeat field without generally clearing the other one. The repeat action checks
positive burst **before** semi and does not recheck the weapon code around those
alternatives. A timing example must therefore state all these fields, plus when
the receipt actually ran.

For a supplied completed Garand receipt with ammo 5, burst 2 and semi 7, a later
reached preparation draw 0 sets semi 1 but leaves burst 2 at that body. A separately
reached unpaused repeat then takes its burst branch, writing burst 1 before a
later supplied firing-helper visit. This is a conditional source-state example,
not an observed Garand burst or a certified way to interrupt an attack.
[Exact receipt, preparation and reader scope](../player-weapon-state-evidence.md#repeat-gives-positive-burst-priority-without-retesting-the-weapon-code)

If burst is nonpositive and the positive-ammo/positive-semi branch is actually
reached, its repeat comparison accepts **1, 3, 6 or 11 of 20 inputs** at supplied
XP 0, 20, 50 or 100. Those are per-visit conditional counts, not a full-volley chance
or shots per second. Even XP 100 does not make that one test automatic.
[Declared inputs](../player-weapon-state-evidence.md#the-semi-comparison-is-per-visit-and-experience-dependent)
Additional source: [Source identities](../player-notes/how-shooting-works.md#citation-4)

[Ordinary pin recovery](morale.md#clearing-pinning-can-still-leave-the-ordinary-soldier-fleeing)
adds another ready-state distinction: clearing pinning replaces its action
counter, then nonpositive morale can still request fleeing. It is not an automatic
resume-fire event or a measured delay. [Exact recovery writer](../player-pin-recovery-evidence.md).
Additional source: [Source identities](../player-notes/how-shooting-works.md#citation-5)

### A magazine number is not a universal firing-entry guard

The ordinary repeat action needs positive ammo, but its separate shared firing
helper has no positive-ammo entry comparison before its shot work and later
ammo decrement. Springfield recovery has no empty/nonempty split or refill
write; Garand recovery does. A ping is another presentation branch after the
helper's decrement, rather than a completed refill receipt.

These are named source-stage differences. They do not establish a native extra
shot, reload bypass or whole-magazine timing; the actual call and intervening
state sequence still need qualification.
[Exact local ammo comparison](../player-ammo-stage-evidence.md).
Additional source: [Source identities](../player-notes/how-shooting-works.md#citation-6)

## Choosing and changing targets

### Which enemy does the ordinary scan choose?

It keeps a closer **eligible** candidate: living, visible, matching the selected
melee-state condition and passing line of sight. A rejected closer enemy does
not reserve its distance. Exact equal-distance ties keep the earlier qualifying
index in that scan; this does not establish a player-controlled ordering trick.

Armor-class 1 candidates also need a positive driver+gunner sum. The alternative
armor!=1 condition still admits class 2 tanks when the other filters pass.
A nearer tank can therefore be selected over farther infantry even though the
shared firearm's selected tank branch does not apply infantry health damage.
Selection and damage capability are different stages.
[Exact filters and supplied examples](../player-ordinary-target-evidence.md#the-scan-chooses-an-eligible-closer-target-not-a-damage-promise)

The target reset occurs inside the admitted search. Positive-timer callbacks
instead use their counter path; blocked search does not automatically mean a
fresh target was selected. The movement section's aiming check also must not be
copied onto the search section as a universal guard. Actual first/next-target
scheduling still needs the shared recipe.
[Retained versus reacquired state](../player-ordinary-target-evidence.md#a-retained-target-is-not-always-reacquired-on-every-callback)
Additional source: [Source identities](../player-notes/how-shooting-works.md#citation-7)

The [Mechanic's repair and combat entry](mechanic.md#repairing-competes-with-a-fresh-enemy-search)
also shows why matching weapon actions are insufficient: repair suppresses its
fresh enemy search, and its later nonempty Pistol recovery uses a different
expression from the Officer's. [Exact comparison](../player-mechanic-combat-evidence.md).
Additional source: [Source identities](../player-notes/how-shooting-works.md#citation-8)

### A repeat request does not freeze the target's earlier state

The ordinary repeat action requests another firing visit without a fresh
search in that body. The shared Garand shot then reads the **current target
field and current helper distance**, not the earlier stored acquisition range.
If a completed intervening order has changed that target field before the
reached shot, the later reader uses the changed value under the stated valid
recipient conditions. A menu click alone does not prove that assignment ran.
[Exact repeat and target readers](../player-repeat-state-evidence.md#a-garand-visit-reads-current-actiontarget-and-distance)

For supplied rifle 40, burst 0 and accuracy draw 21, a current helper distance
350 passes the Garand comparison; 351 doubles the roll to 42 and fails. An
old stored acquisition range of 350 does not change that later read. These
are source inputs, not a measured moving-target result or target-switch time.

The shared hit statistic also precedes the unarmored positive-health damage
guard. A valid still-present health-zero target can therefore pass the selected
accuracy count while receiving no subtraction at that guard. Ammo spending is
another operation. [Accounting and guard scope](../player-repeat-state-evidence.md#shared-shot-accounting-does-not-repeat-all-acquisition-filters)
Additional source: [Source identities](../player-notes/how-shooting-works.md#citation-9)

### A mounted retarget path has different state

The [enemy Jeep/APC gunner](enemy-jeep-and-halftrack.md) illustrates why retarget
is a separate question. Its burst can rebuild a parent pool, and an empty pool
at that repeat site retains the child's old index; APC's initial entry instead
resets its target before constructing the pool. These are bounded source facts,
not the ordinary soldier's completed retarget time or a universal switch rate.
[Exact caller, pool and repeat](../player-enemy-transport-evidence.md#the-shared-burst-can-attempt-a-different-retarget-path)
Additional source: [Source identities](../player-notes/how-shooting-works.md#citation-10)

The [Machine gunner](machine-gunner.md) also has a shared-helper retarget branch
that stores distance before potentially changing target and aim. Its later range
modifier reads that stored distance. This concrete ordering does not replace the
ordinary soldier's pending ready/repeat/reacquisition timing trace.
[Selected shared retarget readers](../player-gunner-retarget-evidence.md)

[Retargeting orders](retargeting-orders.md) have their own target assignments
and narrower animation gates. They do not qualify the ordinary first-shot or
reload cycle simply by navigating an actor to a firing frame.

## A different role uses different continuation

### An Officer uses a different continuation

The [Pistol](pistol.md) shares the damage helper but uses Officer character 671
preparation, frame 12 semi checks and frame 15 recovery. Empty/nonempty counters
are 200−XP/100−XP at those selected writes. The ordinary 623 table above must
not replace those actor-specific actions or their actual callback order.
[Exact source](../player-pistol-evidence.md).

## Controller decisions can interrupt preparation

An expired action timer admits a controller decision; it does not guarantee a
completed shot. Controller navigation can restart an aiming animation before
its firing gate. Recon's missing minimum decision reset demonstrates why more
decisions can produce slower gun clearance but faster grenade launches.

The modern simulation uses 50-ms fixed steps; the original movie declares
20 FPS, but callback order and timer overwrites still matter.
[Complete lifecycle, timing and role deviations](unit-lifecycle.md).
[Measured first-kill and group-clearance differences](combat-results.md).
