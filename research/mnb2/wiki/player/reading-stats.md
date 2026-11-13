[Player reference](README.md)

# Reading stats without confusing different quantities

**Read health, rifle skill, experience and morale separately.** Hover over a
soldier to inspect them, then ask which number matters to the problem: surviving,
hitting, waiting between actions or staying ready. A high number or expensive
recruit is not an all-purpose effectiveness score. [Inspecting a soldier](controls.md).

Applies to **historical selected 2.3.1g**, except explicitly labeled modern
links and comparisons. Source arithmetic is not a measured battle rate.

Find the question behind the number:

- [When does more rifle skill stop helping in the modern game?](rifle-skill.md)
- [Is an armor code a damage-reduction percentage?](#what-do-armor-codes-0-1-and-2-mean)
- [Which stat does this gun actually use?](#check-whose-stat-the-weapon-actually-reads)
- [What does a random starting stat mean?](#a-random-stopping-loop-is-not-a-fixed-starting-range)
- [Can a recorded hit deal no damage?](#a-recorded-hit-can-deal-zero-damage)
- [What does the hover panel copy?](#a-hover-number-is-a-copied-field-and-the-jeep-has-an-important-exception)
- [Do equal starting stats make roles equivalent?](#equal-starting-rifle-means-do-not-make-roles-equivalent)

- **TP:** Tactical points: a shared spending resource. Menu price, payment receipt and later radio acceptance can be separate stages. [Economy](tactical-points.md)

- **Health:** How much health the unit currently has. Being alive is not the same as being ready for every job: the ordinary active controller needs at least 10, while the compared radio-role checks need above 10. Healing infantry and repairing a vehicle are different jobs. [Wounds and readiness](wounded-and-rescued.md), [Medic](medic.md), [Mechanic](mechanic.md)

- **Rifle skill:** An input used by particular attack paths, not automatically a percentage of kills or even of all fired shots hitting. [Weapon comparison](weapon-comparison.md)

- **Experience / XP:** Experience can change particular waits, repeat decisions and radio checks. It does not guarantee an immediate shot or make all roles act alike; each action uses its own rules. [Shooting](how-shooting-works.md), [Signaller](signaller.md)

- **Rank:** A soldier's battlefield rank is separate from your career rank. Extra XP does not always run a promotion check, and a promoted soldier does not become an Officer. Use career rank for deployment unlocks. [Progression](progression.md)

- **Morale:** Helps determine whether the unit can act and how it responds to pinning or withdrawal. Clearing pinning need not stop fleeing when morale is nonpositive. Starting morale and later changes are separate. [Morale](morale.md)

- **Armor code:** A category used to decide how a weapon treats a target, not a percentage of damage stopped. Infantry health, vehicle hull and crew can follow different rules. [AT and vehicles](anti-tank-and-vehicles.md)

- **Ammo / burst / semi:** Distinct attack-cycle counters; a weapon assignment is not by itself proof of a refill or a guaranteed hit count. [Shooting stages](how-shooting-works.md)

- **Action or request timer:** A counter used by a particular action, not automatically a number of seconds. One counter does not tell you the whole wait from selecting support to its arrival, or from seeing an enemy to firing. [Support](support.md), [shooting](how-shooting-works.md)

- **Local wave:** A mission-state input used by selected generators and enemy loads; mission-total and career counts are separate. [Waves](waves.md)

- **Cover / bunker:** Different protection checks. Two ordinary-cover structures do not give two ordinary-cover saves; a bunker is a separate category for the attackers that check it. Visible overlap still needs to match the actual protected point. [Defenses](defenses.md)

- **Concealment:** Reconnaissance-sensitive visibility behavior, separate from stopping an already accurate shot. [Concealment](concealment.md)

- **Damage bound:** A limit used by a damage roll, not the guaranteed health loss from every shot. Check accuracy, target type and protection before comparing the number. [Weapons](weapon-comparison.md)

- **Nominal group:** A requested or counted quantity, not a measured count of healthy arrivals. [Paratroopers](paratroopers.md)

## Read the boundary next to a table

A **load default** describes initialization, before later writers. A **conditional
source result** gives what follows from stated branches and inputs. An **observed
result** requires an actual recorded run; an attributed community report is its
own kind of evidence. These descriptions should not be silently exchanged.

For example, the ordinary-cover plus bunker result is 87.5% saved **among otherwise
accurate shots in the inspected paths, when both queries succeed**. It is not
87.5% less health lost from every attack or a guarantee that a particular drawing
places the soldier inside both regions. [Worked defense comparison](defenses.md)

Likewise, an enemy Sniper load of rifle 100 at local wave 100 does not eliminate
its attempt, accuracy, protection and damage stages. [Enemy load examples](enemy-stats.md)
A useful comparison states the actor, version, starting state and question first.
[Mechanics questions](mechanics-at-a-glance.md), [strategy/version context](strategy-and-versions.md)

## What do armor codes 0, 1 and 2 mean?

Armor is a **classification used by a particular reader**, not a percentage
damage reduction. These named **selected 2.3.1g enemy-load examples** show why
health, crew and armor should be read separately:

| Example code and enemy | Reached shared Allied firearm alternative after its accuracy comparison                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------------------- |
| 0 — Volkssturm         | Falls in the armor-below-1 route, whose positive-health recipient can receive the weapon's health subtraction |
| 1 — German Jeep        | Enters separate crew-role alternatives, rather than the infantry health-subtraction route                     |
| 2 — Tiger              | The selected armor-2 alternative requests a ricochet sound; it does not copy infantry damage into that branch |

[Enemy load/class bindings](../vehicle-load-map.md),
[Volkssturm load](../player-enemy-evidence.md),
[exact shared armor/crew alternatives](../player-small-arms-crew-evidence.md#accuracy-is-followed-by-another-armor-specific-selection)

This describes **one shared firing helper**, not every firearm, mounted weapon,
explosion or anti-tank attack. A code-1 crew clear is not itself hull destruction
or permanent immobilization; a code-2 ricochet alternative does not make the
target immune to every other attack. Follow [small arms and crew](small-arms-against-vehicles.md)
or [AT/blast stages](anti-tank-and-vehicles.md) for the actual path you need.
Sources: [Source identities](../player-notes/reading-stats.md#citation-1)

## Check whose stat the weapon actually reads

A vehicle's hull and its mounted gun can own different fields. Even on one
actor, a number can affect one stage while another stage ignores it.

| Selected path                               | What the inspected reader does                                                                                     | What that does not establish                                                                               |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| [M3 AT gun](m3-at-gun.md)                   | Expired controller counter resets to 200−XP; target-offset writes do not read rifle or XP                          | Higher rifle does not tighten those offsets; the counter is not a measured reload                          |
| [Sherman](sherman.md)                       | Turret has its own rifle 1/XP 2; coax and optional .50 read hull rifle through different comparisons               | The hull's rifle is not every component's accuracy percentage                                              |
| [20mm AA cannon](aa-cannon.md)              | Anti-air comparison reads parent rifle; ground burst initialization reads child gun XP                             | Parent XP is not interchangeable with gun XP; a longer burst counter is not a certified interception count |
| [Halftrack quad](halftrack-weapons.md)      | Four selected shot bodies compare their draw <= 5, giving six qualifying integer values                            | Hull rifle does not change that threshold; four bodies do not prove four simultaneous hits                 |
| [Halftrack hospital](halftrack-hospital.md) | A later fresh random timer write overwrites the earlier XP-based expression                                        | Reading only the first timer write would invent an XP benefit at that reset                                |
| [SS infantry](ss-infantry.md)               | Shot comparison subtracts twice current burst from rifle; controller and firing entry write different burst values | The loaded rifle value alone does not determine its current shot comparison                                |
| [SdKfz 222](sd-kfz-222.md)                  | Child turret rifle load uses mission-total wave separately from hull fields                                        | A hull stat or local-wave label cannot replace that child's actual input                                   |

These are selected **2.3.1g** readers, not a global rule that rifle or XP never
helps those units. Follow the named component, its current writer and the stage
being compared. Whole-cycle timing, recipients and actual battlefield outcomes
remain separate from any one table cell.
[M3 bindings](../player-mounted-evidence.md), [Sherman bindings](../player-tank-evidence.md),
[20mm bindings](../player-aaa-evidence.md), [Halftrack weapon bindings](../player-halftrack-weapons-evidence.md),
[hospital overwrite](../player-halftrack-hospital-evidence.md), [SS writers](../player-enemy-ss-evidence.md),
[222 component](../player-light-vehicle-evidence.md).

Sources: [Source identities](../player-notes/reading-stats.md#citation-2).
[Retained evidence and qualified explanations](../player-reference-evidence.md)

## Follow the current value before comparing the next attack

A useful stat comparison identifies **whose field changed, how it changed and
which later action reads it**. These source examples show why a starting value,
a promotion message and a weapon result can differ:

- **Was the value added or replaced?** A Crewman can copy supplied XP 0 over a vehicle's XP 80. The operation replaces XP; it does not preserve the veteran value and add zero

- **Did XP invoke promotion?** Selected Medic, airborne rescue, hospital and radio XP bodies do not locally call rankup. XP can change without that same body running the promotion ladder or its cap

- **Was the living actor changed?** Best-soldier result fields copy rifle and XP into a stored snapshot. A recorded career/result value is not a combat upgrade to the source soldier

- **Did the wave change an earlier load?** Detailed Orders subtracts local wave; the selected rifle load needs its own execution. An existing supplied rifle 50 does not become 35 merely because wave changes 50 to 35

- **Did a smaller random range guarantee a weaker next soldier?** An earlier divided-family W=50/draw=0 gives rifle 0; a separate W=35/draw=34 gives 17. Lower possible maximum and lower realized next draw are different claims

- **Is a high priority guaranteed to be selected first?** The Sniper compares distance/priority but stores raw distance after selection. Eligibility and scan order still matter; priority is not a universal threat ranking

[XP additions, copies, caps and snapshots](../player-experience-writer-evidence.md),
[rifle writer boundaries](../player-rifle-writer-evidence.md),
[changed-wave inputs](../player-campaign-evidence.md#a-lower-local-wave-is-not-a-guaranteed-lower-realized-rifle-value),
[exact priority reader](../player-enemy-priority-evidence.md).

The numeric pairs above are declared source inputs, not newly observed births,
recrewing outcomes or a reproducible whole-battle forecast. For an actual enemy
stat at a specified wave, the remaining shared work must identify its load wave,
reached later writers and attack reader in order. The already qualified Volks
birth example and rifle sequence each retain their own narrower boundary.
[Enemy stats](enemy-stats.md), [qualified birth](../shared-results.md),
[qualified rifle sequence](observed-rifle-sequence.md).

Additional sources: [Source identities](../player-notes/reading-stats.md#citation-3)

## A random stopping loop is not a fixed starting range

The selected Machine gunner and M3 loads add 1–10 rifle points, then draw whether
to continue. Their first addition is mandatory; “random-stop additions” does not
mean five additions or a total bonus confined to 1–10. With declared independent
uniform inputs, the loop averages two additions, for a mean bonus 11 before career
or later writers. That is conditional arithmetic, not a measured recruit average
or a universal starting stat. [Exact two loads, stop counts and assumptions](../player-random-stop-load-evidence.md).
Additional source: [Source identities](../player-notes/reading-stats.md#citation-4)

## A recorded hit can deal zero damage

Zero at a health-subtraction draw does not identify every other effect or
counter at that attack stage. These **selected 2.3.1g** cases differ:

| Reached source case                                               | What zero health subtraction means here                                                                                                        |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Halftrack quad against an eligible unarmored target               | Its hit counter can already be recorded even when the later draw subtracts zero.                                                               |
| Passed shared infantry accuracy with damage 0                     | It does not fall through to the separate failed-accuracy pinning block.                                                                        |
| Shared firearm against a stable, valid enemy with the flammen tag | A separate below-10 comparison can still request the flamer explosion before the later fatality check, even if the draw left health unchanged. |

These are reached-branch examples, not observed whole-shot rates or a promise
that the later effect completes. Identify the actor, target and reader before
interpreting a hit counter, unchanged health or an explosion image.
[Quad outcome/accounting](../player-shot-outcome-evidence.md),
[miss-only pinning branch](../player-miss-pinning-evidence.md),
[enemy-flamer trigger inputs](../player-shared-flamer-trigger-evidence.md)
Additional sources: [Source identities](../player-notes/reading-stats.md#citation-5)

The selected Halftrack quad action admits 6 of 100 initial draw values, records
a hit, then can subtract zero from a living unarmored target. Under supplied
independent uniform draws, 6% reach the hit counter but 5.94% subtract a positive
amount at that action. These are source counts with declared state, not a measured
battle accuracy or four-shot burst result.

The 222 turret records its enemy-hit counter after its infantry saves, so the
two counters do not even use the same stage. At supplied rifle 40 and successful
ordinary-cover plus bunker queries, 5% of reached shot actions record a hit and
about 4.967% subtract positive health. Starting health and different death
thresholds still determine which local death request can follow.
[Exact denominators, mean subtractions and health examples](../player-shot-outcome-evidence.md).
Additional source: [Source identities](../player-notes/reading-stats.md#citation-6)

A vehicle field called **moving** can encode sound-state transitions. In the
selected Halftrack/Sherman parent route, a distant target can set moving to 1 and
later to 2 even if the obstacle query prevented that step's position writes.
Those values do not certify movement speed or actual displacement.
[Exact blocked-step inputs and later sound-state writes](../player-vehicle-movement-evidence.md#halftrack-focus-uses-health-and-moving-is-also-a-sound-state-field).
Additional source: [Source identities](../player-notes/reading-stats.md#citation-7)

## A hover number is a copied field, and the Jeep has an important exception

Selected hover handlers copy actor fields to the info panel when that event runs.
A separate health/rifle change does not itself execute another copy in those
handlers. The ordinary rollover also requests rank and specialization icons
from their separate fields; it does not derive either from experience. Actual
refresh timing and rendered text remain unqualified.

For the Jeep, the selected panel rifle copy reads **the gun component's rifle**,
while the inspected firearm compares against **hull rifle**. Supply hull 40 and
gun 10: that hover copies 10, but the firearm's cited accuracy comparison uses 40.
A qualifying Jeep promotion can add to the child field without a hull-rifle write;
a later hover can therefore copy a higher value without proving that comparison
improved. Other writers and full combat outcomes still matter.
[Exact finite stat-copy map and declared promotion/hover example](../player-hover-stat-evidence.md#jeeps-panel-rifle-is-not-the-inspected-firearms-hull-rifle).

Hover eligibility also differs from movement selection: the AA's gunner 1/driver 0
state can pass its hover crew gate while its selected release-focus gate requires
driver 1. A panel copy is not proof a unit can move or fire. Parent health, child
gun stats and actual current combat readers remain separate.
[Exact selected handlers and copy limits](../player-hover-stat-evidence.md).
Additional source: [Source identities](../player-notes/reading-stats.md#citation-8)

## Compare readiness and spread at their actual readers

The enemy Mortar loads a wave-dependent rifle value, but its inspected emission
uses fixed independent axis offsets rather than that field. Its setup counter
and action timer also occupy different arms of one branch: pinning can prevent
a ready search without freezing positive setup or a positive action timer.
[Mortar selection, setup and placement](enemy-mortar.md).

Health has the same need for a named reader. At supplied health 1, a ready timer
can decrease in the Mortar controller, while the rocket soldier's extra health
gate skips its action chain. Neither fact qualifies a complete low-health firing
cycle or a safe enemy state. [Exact controller comparison](../player-enemy-heavy-evidence.md#rocket-and-mortar-controller-health-and-pause-gates-are-not-interchangeable).
Additional source: [Source identities](../player-notes/reading-stats.md#citation-9)

## Equal starting rifle means do not make roles equivalent

The named-load explanation now binds all 21 retained placed callbacks with its
exact stopping-loop pattern. Under the same declared independent inputs, it gives
an Officer, Medic and Signaller each a post-loop rifle mean of 11 before career
additions. That equality does not make three interchangeable pistol soldiers:

| Role      | What still needs its actual reader                                                                              |
| --------- | --------------------------------------------------------------------------------------------------------------- |
| Officer   | Its command eligibility, Pistol preparation and Officer-specific promotion ladder                               |
| Medic     | Its healing controller and patients; the inspected own scope has no ordinary enemy acquisition/shared-fire call |
| Signaller | Its radio completion reads experience, with request-specific payment/delivery gates                             |

The wider table also keeps vehicle parent fields and specialist load fields
separate from component stats and final writers. These are conditional field
means rather than observed recruit averages or accuracy percentages.
[Twenty-one exact bindings, scalar bases and unchanged shared method](../player-random-stop-load-evidence.md#thirteen-remaining-named-bindings-complete-this-finite-placed-load-pattern),
[Medic scope](../player-medic-controller-evidence.md), [Signaller](signaller.md),
[Officer](officer.md).
Additional source: [Source identities](../player-notes/reading-stats.md#citation-10)
