[Player reference](README.md)

# Mechanics questions at a glance

These answers cover historical **selected 2.3.1g**. Start with the five main
questions below, or use the other question lists to find a particular interaction.
The linked guides put deeper source details and remaining limits beside each fact.
For measured modern outcomes, use [modern combat choices](combat-results.md);
for modern Remaster/Community accuracy rules, use [rifle skill](rifle-skill.md).

Start with [shooting delays](#why-is-a-soldier-slow-to-shoot-or-change-targets),
[defense stacking](#which-defenses-stack),
[anti-tank damage](#why-did-an-anti-tank-attack-leave-a-vehicle-alive),
[rockets and backblast](#why-can-a-bazooka-rocket-pass-a-target-or-hurt-my-squad)
or [enemy stats](#how-do-enemy-stats-change-by-wave).
[More questions](#more-questions-at-a-glance) groups equipment, support and progression.

## Why is a soldier slow to shoot or change targets?

**Finding a target, aiming, firing, repeating and recovering take separate
steps.** Health, pinning, morale, orders and target eligibility can prevent the
soldier from reaching the next step at all. Check the [nonfiring checklist](why-soldiers-stop-shooting.md)
before treating every pause as a slow weapon. Rifle skill is not a universal
reaction-speed stat. [Shooting stages and ordinary-soldier evidence](how-shooting-works.md).

Experience changes some counters, but one refill expression does not give
first-shot or next-target seconds. In the retained fixed encounter, one soldier
fires at different targets 89 world ticks apart; that gap does not locate the
target-change moment or measure retarget time. **Exact general reaction and
retarget timings remain unqualified.** [Observed sequence and limits](observed-rifle-sequence.md),
[retained observation](../shared-rifle-sequence.md).

## Which defenses stack?

**Trench plus Sandbags still provides one ordinary-cover save.** A bunker can
add a separate save when the attacker checks bunker protection. In the inspected
common enemy firearm paths, ordinary cover saves 50% of otherwise accurate shots
and bunker protection saves 75%; when both queries succeed and their draws are
independent and uniform, the combined saved fraction is 87.5%. This is not a
damage reduction applied to every attack. [Defense comparison and evidence](defenses.md),
[exact protection queries](../player-defense-evidence.md#bullet-saves).

The enemy Sniper omits that bunker save, SS uses a different ordinary-cover
threshold, and blasts/flames have their own rules. Some defenses also restrict
specialist actions. **Visible overlap does not establish a tested safe layout.**
[Shooter exceptions](defenses.md#an-important-exception-enemy-snipers),
[specialists under cover](specialists-under-cover.md).

## Why did an anti-tank attack leave a vehicle alive?

**Target selection, effect placement and damage eligibility are different
tests.** The selected AT distance check uses the effect's and actor's x/y points;
the visible vehicle width is not added to that particular predicate. A nearby
explosion can still fail its strict distance, armor or other recipient guards.
[Point-distance evidence](../player-tank-evidence.md#the-selected-at-gate-reads-points-not-an-outline),
[AT and vehicle guide](anti-tank-and-vehicles.md).

The Tiger has a further Bazooka-tag exception: its selected AT branch subtracts
500 health and checks whether it survives, rather than always removing it.
Other later blast stages can matter too. A kill-counter write alone does not
prove destruction. **Actual outline-hit probabilities and full damage outcomes
remain unqualified.** [Tiger stages](anti-tank-and-vehicles.md#the-tigers-500-subtraction-can-be-followed-by-another-health-draw).
For a purchase decision, compare [AT options](anti-tank-options.md) by their job
and targeting requirements rather than treating one radius as their accuracy.

## Why can a Bazooka rocket pass a target or hurt my squad?

**The rocket samples proximity intermittently, and its blast starts at the
sampled rocket point.** In the selected enemy scan, distance strictly below 50
can trigger it; the later AT call uses a strict below-25 distance gate. At
unchanged shared-coordinate distance 40, that trigger passes while the later AT
distance check fails. This example does not settle other damage paths.
[Exact trigger, event order and point example](../player-bazooka-event-evidence.md),
[Bazooka guide](bazooka.md).

Backblast separately scans living unarmored troops on both sides. Do not use a
vehicle's visible outline, one explosion size or a bunker rule from another
helper as a guaranteed safe spacing rule. **Full flight/terrain geometry, a
measured hit chance and a certified safe backblast layout remain open.**
[Backblast conditions](bazooka.md#keep-the-backblast-region-clear),
[friendly-fire comparison](collateral-damage.md).

## How do enemy stats change by wave?

**Different enemy types use different starting formulas.** For a positive local
wave of 50 when the selected load runs, many ordinary infantry profiles draw
rifle values from 0 to 24.5 in half-point steps, SS draws 0–49, and the German
Sniper starts at 50. Those are starting rifle fields, not final hit chances.
Enemy composition and the later weapon reader are separate. [Enemy stat table](enemy-stats.md),
[exact load formulas](../player-campaign-evidence.md#enemy-load-formulas).

Changing the wave does not itself rerun every survivor's load. Local wave,
mission-total waves and career waves are different counters, and later stat
writes can change an actor. **A universal final-stat table for every spawn,
mode and override is not yet qualified.** [Later-writer limits](enemy-stats.md#a-new-wave-does-not-itself-rerun-an-old-load-assignment),
[wave behavior](waves.md).

## More questions at a glance

| Player question                                            | Supported answer and next limit                                                                                                                                                          |
| ---------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Why do starting rifle cards disagree?                      | Many recruits use a random stopping loop, rather than five fixed rolls. [Regular Soldier](regular-soldier.md)                                                                            |
| Does rifle 40 mean 40% hit chance?                         | One shared-helper comparison is inclusive and applies weapon/distance/burst changes first; full shot outcomes need target/state context. [Weapon comparison](weapon-comparison.md)       |
| Is a bunker safe against every sniper and explosion?       | The inspected enemy Sniper lacks the bunker save, and blast/backblast/conversion paths have other guards. [Bunker](bunker.md)                                                            |
| Does a kill-counter increase prove the Tiger died?         | The AT common counter/XP tail can run while the Tiger exception leaves positive health. [AT accounting](anti-tank-and-vehicles.md#an-at-kill-counter-write-is-not-always-a-removed-tank) |
| Can a repaired vehicle still need a gunner?                | Hull-health subtraction and crew-loss tests are separate; Mechanic and Crewman address different state. [Hull damage and crew](vehicle-damage-and-crew.md)                               |
| Does buying grenades guarantee the next attack throws one? | Equipment flags, actor admission and nested choice tests differ; the ordinary example distinguishes hand-only, rifle-only and both. [Grenades](grenades.md)                              |
| Does XP automatically determine rank?                      | Medic/Officer defaults and helper-call timing show otherwise. [Progression](progression.md)                                                                                              |
| Does a 1-TP smoke menu mean one final charge?              | The coordinate and later radio paths have distinct guarded debit sites. [Smoke](smoke.md)                                                                                                |
| Does placing a net stop every support event?               | Concealment and one randomized squad helper are separate from other event sources. [Concealment](concealment.md)                                                                         |
| Can I use one health cap for healing and repair?           | Patient thresholds, base health and additive repair writes differ. [Medic](medic.md), [Mechanic](mechanic.md)                                                                            |
| Is withdrawal just returning purchase cost?                | A load value and guarded exit addition are separate from the personal payment history. [Withdrawal](withdrawal-and-mission-end.md)                                                       |
| Can a screenshot prove a strategy's success rate?          | Version, starting profile, trials and failures still need to be recorded. [Strategy context](strategy-and-versions.md)                                                                   |
| Can wire only hurt enemies?                                | No friendly exemption appears in the selected damage loops; both sides need armor 0 and a qualifying point intersection. [Wire](barbed-wire.md)                                          |
| Does wire stop all Pioneer sabotage?                       | Its selected sabotage guard does not require wired<1; movement and sabotage have different admission checks. [Pioneer](enemy-pioneer.md)                                                 |
| Does a German Officer call exactly one extra soldier?      | The later special calls a wave generator; its random comparison and the generator's actual emissions are different steps. [Officer](german-officer.md)                                   |
| Does every mounted gun use its own displayed rifle?        | Jeep shot and promotion readers differ, while M3/Sherman emission offsets do not read rifle there. [Stage-specific comparison](vehicles-and-emplacements.md)                             |

More crew, support and award questions:

- [Can a replacement gunner lower a vehicle's recorded XP?](crewman.md#a-replacement-gunner-can-replace-the-vehicles-recorded-xp) The selected gunner branches replace parent XP/rank; driver alternatives do not copy them.
- [Does shooting the driver stop every enemy vehicle?](flakpanzer.md#a-missing-driver-is-not-this-hulls-movement-guard) Flakpanzer and Wespe hull movement use counters without a local crew gate; their turrets have separate gunner checks.
- [Does counter-artillery erase an already queued strike here?](naval-and-counter-artillery.md) The selected later consumer has delay/quantity/random guards, without a repeated counter-credit test.
- [Does one Wespe shell pick one named soldier?](wespe.md#a-strike-counter-shell-representation-and-impact-are-separate) Shared artillery delivery samples the current squad half for each successful effect request.
- [Does the Close combat Ribbon description prove 10% extra melee damage?](close-combat-and-bayonets.md#the-ribbon-description-does-not-qualify-an-extra-damage-multiplier) The advertised reward and supported damage helper are separate evidence.
- [Does the next wave reroll every living enemy's rifle?](enemy-stats.md#a-new-wave-does-not-itself-rerun-an-old-load-assignment) A load expression is evaluated when its writer runs; the finite later-writer map still needs runtime receiver/order qualification.

More enemy questions:

- [Do all enemy firearms use the same cover saves?](defenses.md#ss-uses-a-different-ordinary-cover-save) SS differs from the common 50% ordinary-save path; the enemy Sniper has another exception.
- [Does a larger burst always mean greater per-shot accuracy?](enemy-machine-gunner.md) The inspected MG comparison subtracts a counter-dependent penalty.
- [Does a Grenadier need to find a target before choosing its grenade?](enemy-grenadier.md) Its grenade branch is separate from ordinary target search.
- [Does rising rifle skill tighten every mortar impact?](enemy-mortar.md) The inspected enemy placement uses fixed axis offsets without that field.

- [Does a small-arms hit destroy a vehicle?](small-arms-against-vehicles.md) Shared-helper crew checks and tank ricochets are separate from hull damage and AT destruction.
- [Does a second Officer guarantee twice the aid?](officer.md#several-officers-share-an-entry-counter) Entry reads shared state without reserving it at that site; full callback order remains open.

More acquisition, support and reward questions:

- [Does the Sniper always pick the lowest weighted target score?](sniper-rifle.md#target-priority-is-not-simply-closest-or-lowest-score) Its inspected scan compares a quotient but stores raw distance; the supplied two-target example changes with index order.
- [Can a Scout or Sarge help an Allied mortar see a target?](mortar.md#a-scout-or-sarge-can-satisfy-one-sight-alternative) A qualifying specialization 11 actor satisfies one sight alternative, while range, visibility and camouflage gates remain.
- [Does a faded smoke cloud prove the sight obstacle is gone?](smoke.md#smoke-supplies-a-sight-obstacle-not-a-fixed-protection-percentage) Opacity is not the sampled-sight skip condition; cloud indexing and actual geometry remain separate.
- [Does the nearest Officer always get Sarge's training?](sarge.md#training-chooses-an-eligible-officer-by-scan-order) That selected scan takes its first qualifying index, adds XP and calls the promotion helper.
- [Does only the crate collector receive the manuals?](crates.md#the-collector-and-the-group-can-receive-different-rewards) Collector+3 XP precedes separate group sweeps that do not repeat pickup proximity.
- [Does sabotage consume only the latest soldier's XP?](sabotage.md#the-reward-reads-a-shared-bonus) It reads a shared pool; the selected terminal statement does not clear it.

More state and progression questions:

- [Does Heroism set the off-field protection flag?](protection-flag.md) Its selected receipt sets health 200; the separate coordinate/flee helper has its own writes and caller guards.
- [Does Hold Fire always extend the current counter?](hold-fire.md#replacing-a-counter-is-different-from-adding-a-duration) The selected assignment replaces it with 400; a supplied old 500 becomes 400.
- [Does a Bazooka shot statistic prove the rocket exists?](bazooka.md#a-shot-counter-and-the-rocket-are-separate-stages) Preparation, shot/sound accounting and actual rocket birth are separate selected actions.
- [Does advancement automatically promote everyone?](advancing.md#the-later-xp-and-tp-writes-are-not-a-promotion-or-universal-cap) Its indexed reward loop adds XP without a local rankup call; the wounded penalty and later morale bonus are different stages.
- [Does a career TP gift set the whole starting balance?](deployment-gifts.md) The selected gift block adds to the current balance; base mode and full initialization remain separate.
- [Are all free-order allowances used at the menu?](support-and-economy-awards.md#starting-allowances-are-spent-at-different-stages) Ranger, Heroism and ordinary paradrop consumers spend their fields at different stages.

More observed firing and command questions:

- [Has an original rifle sequence actually been observed?](observed-rifle-sequence.md) One independently reviewed fixed start has eight fires without a hit-counter increase, then enemy health 100→98 on fire nine. It is not an average damage or retarget-time estimate.
- [Does replacing a weapon reset every attack field?](how-shooting-works.md#replacing-a-weapon-is-not-a-complete-attack-state-reset) The selected ordinary receipt leaves ammo, burst and semi unwritten; later preparation and repeat have their own readers.
- [Does Hold Fire give every actor the same counter path?](hold-fire.md#the-ordinary-soldier-has-a-different-receipt-and-counter-consumer) The ordinary soldier's earlier receipt and later cap differ from the inspected Bazooka path. Neither is a measured universal hold duration.

Browse the [enemy role guide](enemy-guide.md) for the covered actors and their exact boundaries.

The operator's five priority questions—reaction/retarget cycle, defense stacking,
AT versus vehicle geometry, bazooka triggers and wave-dependent enemy stats—now
have linked partial answers with explicit boundaries. More precise timings and
hitbox/placement results need the separately scoped shared reconstruction, not
a guessed universal number added to a stat card.

Sources: [Source identities](../player-notes/mechanics-at-a-glance.md#citation-1). [Exact evidence](../player-reference-evidence.md)

Additional source-bound answers: [Source identities](../player-notes/mechanics-at-a-glance.md#citation-2). See the linked exact-source notes for each stage.

New linked comparisons: [Source identities](../player-notes/mechanics-at-a-glance.md#citation-3)

Further source-bound states: [Source identities](../player-notes/mechanics-at-a-glance.md#citation-4)

Further linked sources: [Source identities](../player-notes/mechanics-at-a-glance.md#citation-5)

Additional bounded inputs: [Source identities](../player-notes/mechanics-at-a-glance.md#citation-6). See the linked exact notes for reviewed observation
versus supplied source-state boundaries.

For a soldier who appears inactive, use the [nonfiring checklist](why-soldiers-stop-shooting.md)
to distinguish readiness, target eligibility, orders, repeat state and specialist
jobs before interpreting one rifle or reload number.

More source-bound player questions:

- [Does rank 9 automatically supply Officer commands?](officer.md#a-rank-9-soldier-does-not-automatically-become-this-specialist) The helper does not install command specialization; particular offers still read that separate field.
- [Does the Jeep panel rifle match its firearm reader?](jeep.md#the-hover-rifle-field-follows-the-gun-component) The selected hover copies child rifle, while the inspected firearm reads hull rifle.
- [Does the Scout indicator count enemies or forecast arrivals?](scout.md#the-wave-indicator-reads-a-shared-timer-after-a-separate-enable-decision) Its child reads a shared timer after a separate parent-enable decision.
- [Is 500 the entire Tiger/Bazooka health change?](anti-tank-and-vehicles.md#the-tigers-500-subtraction-can-be-followed-by-another-health-draw) A surviving recipient can reach a later core or fragment draw under its own guards.
- [Does stored front armor define a facing reduction?](anti-tank-and-vehicles.md#a-stored-front-armor-number-is-not-a-facing-based-reduction-rule) The finite literal audit and selected AT readers do not supply that percentage or weak-point rule.
- [Do several pending purchases form a queue?](training-and-equipment.md#several-pending-choices-do-not-form-a-queue) Earlier recipient branches clear or retain other cues differently; application and refunds remain separate.
- [Does the last grenade decrement emit the blast immediately?](grenades.md#zero-movement-counter-is-followed-by-a-separate-expiry-visit) Expiry is a sibling alternative reached on a later eligible visit, without a seconds conversion.

These are conditional source and declared-input comparisons. They do not add
new native timing, safe placement, final counter or complete transaction claims.
Additional sources: [Source identities](../player-notes/mechanics-at-a-glance.md#citation-7). Each linked page retains its exact evidence.

## Questions about a high number or a changed roster

| Player question                                                          | Start with the relevant stage                                                                                                                 |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Does rifle 100 remove BAR's current-burst penalty?                       | [BAR comparison](bar.md): burst is added before the distance modifier; a high rifle field is not a promise every comparison passes.           |
| Does more XP always encourage the ordinary Shotgun decision?             | [Shotgun acquisition](shotgun.md): its distance-false alternative uses random100 greater than XP, separately from the later shot reader.      |
| Does a Gunner casualty immediately improve another Gunner's direct roll? | [Gunner count](machine-gunner.md): the direct shot reads stored mgCount; roster type, a new count and actual cleanup are separate.            |
| Does a Scout's extra Naval marker equal another queued shell?            | [Naval acceptance](naval-and-counter-artillery.md): local marker, current TP and copied shared artillery quantity have different readers.     |
| Does a low-TP Situation report promise a net gain?                       | [Situation report](situation-report.md): payment and the balance-sensitive reward branch are separate; a conditional mean is not a guarantee. |
| Does every enemy getting through immediately run the same loss check?    | [Breakthroughs](breakthroughs.md): contribution, local threshold check and display are distinct, including the Jeep exception.                |
| Can a result bonus change whether career points are added?               | [Score and career points](score-and-career-points.md): the conditional bonus precedes the strict guard on the resulting mission score.        |

These links bring existing supported comparisons together; they add no new
mechanics derivation, initialized battle or optimal purchase recommendation.
Additional sources: [Source identities](../player-notes/mechanics-at-a-glance.md#citation-8). Each linked reference preserves its exact source
and supplied-input boundaries.

## Can an enemy flamer explosion follow a zero-damage hit?

In the selected shared-firearm path, yes as a **conditional effect request**:
after an admitted hit on a stable valid flammen-tagged enemy, a separate roll
can request the explosion before the later fatality test. A supplied zero
health subtraction does not itself prevent that request. It is not a guaranteed
completed blast or a whole-shot explosion percentage.
[Enemy-flamer example](enemy-flamethrower.md#a-firearm-hit-can-request-an-explosion-before-the-target-dies),
[hit counters and zero-subtraction cases](reading-stats.md#a-recorded-hit-can-deal-zero-damage),
[exact supplied inputs](../player-shared-flamer-trigger-evidence.md).
Additional source: [Source identities](../player-notes/mechanics-at-a-glance.md#citation-9)
