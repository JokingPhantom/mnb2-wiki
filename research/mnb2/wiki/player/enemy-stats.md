[Player reference](README.md) · [Waves](waves.md) · [Enemy guide](enemy-guide.md)

# Enemy starting stats change by wave and by unit

Enemy difficulty is not one universal multiplier. **Different load profiles
initialize rifle skill differently from local wave**, while wave generators
also change which units and how many attempts occur. The tables below are
**load-default formulas and examples**, not final stats after every spawn or
later write, and not hit probabilities. [Wave composition](waves.md)

Let **W mean the positive integer local wave value when that load handler runs**.
It is not assumed to be the displayed mission-total or career wave count.

Historical scope: selected **2.3.1g** source; these are conditional rules,
not a forecast of a particular battle.

Find your question: [do existing enemies change with a new wave?](#a-new-wave-does-not-itself-rerun-an-old-load-assignment),
[what does Detailed Orders change?](#detailed-orders-changes-an-input-not-every-enemy-already-on-the-field), or
[is rifle skill a hit percentage?](#half-point-rifle-does-not-mean-that-exact-percentage),
[priority](#priority-is-a-separate-load-field-used-by-a-sniper-selector),
[enemy morale](#assault-expert-changes-enemy-load-morale-in-different-ways), or
[fixed health draws](#wave-dependent-rifle-does-not-scale-every-bullets-health-draw).

| Load family                           | Rifle field formula                        | W=10  | W=50   | W=100   |
| ------------------------------------- | ------------------------------------------ | ----- | ------ | ------- |
| Many ordinary enemy infantry profiles | Random integer 0 through W−1, divided by 2 | 0–4.5 | 0–24.5 | 0–49    |
| SS                                    | Random integer 0 through W−1               | 0–9   | 0–49   | 0–99    |
| German Sniper                         | W                                          | 10    | 50     | 100     |
| Enemy flame troop                     | W plus random 0–59                         | 10–69 | 50–109 | 100–159 |
| Enemy rocket troop                    | W plus random 0–29                         | 10–39 | 50–79  | 100–129 |
| Enemy mortar troop                    | W plus random 0–19                         | 10–29 | 50–69  | 100–119 |

The divided ranges include **half-point steps**; they are not rounded into an
invented integer skill range. The ordinary expression appears in Regular,
Grenadier, Officer, Volkssturm, MG, parachute infantry, Jugend, Scout, Pioneer
and Brandenburg/infiltrator load profiles. Exact placements and aliases remain
separate in the source notes. A similarly initialized field does not prove all
actors use the same weapon or even use that field in the same way.
[Exact formulas and example inputs](../player-campaign-evidence.md#enemy-load-formulas)

## Health, experience and morale are different fields

The 18 catalogued enemy-unit placements have cited health defaults of 100, except
the zombie placement at 400. Those are not every enemy vehicle or actor in the
game, and high health is not an armor class. The zombie's selected armor load
is 0. [Enemy template map](../enemy-infantry-map.md)

Selected Regular, Volkssturm and German Sniper loads have different experience
rolls: 1–50, 1–20 and 1–70 respectively. Their morale rules also differ. Regular morale
starts at 0–99 with a separate 10-point Assault Expert Award penalty; Volkssturm
starts at 1–10 but that award's branch **replaces it with 2**. Subtraction and
replacement are not the same operation. [Volkssturm comparison](../volkssturm.md),
[morale](morale.md)

The [Volkssturm role card](volkssturm.md) follows one actor from these load
fields into its shooting and recovery branches, with an explicit XP/rifle/cover
example. The early caller writes placement coordinates before advancing the wave;
the [retained observed birth example](../shared-results.md) resolves that order
for one fixed start: wave 2 is already visible to the two new loads. Other spawn
paths, starting states and subsequent stat writers remain open.

The [German Sniper](german-sniper.md) card adds its selected visibility/target
guards, rank-sensitive range update and ordinary-cover exception, with an
explicit per-frame example rather than a universal rifle percentage.

## Follow the field into the actual attack

The [SS infantry](ss-infantry.md) shot subtracts twice its current burst from
rifle skill and uses a 60% ordinary-cover save. The [enemy MG](enemy-machine-gunner.md)
subtracts three times its burst; those are different readers even when a load
range looks similar.

For the [enemy rocket soldier](enemy-rocket-soldier.md), the selected launch and
navigation do not use rifle to calculate a hit percentage. For the
[enemy mortar](enemy-mortar.md), the inspected impact placement uses fixed
−150…149 axis offsets without reading rifle or experience. A rising wave-loaded
field alone does not prove either placement becomes more accurate.
[Exact rocket/mortar reader boundaries](../player-enemy-heavy-evidence.md),
[SS writers and shot](../player-enemy-ss-evidence.md),
[MG stages](../player-enemy-mg-evidence.md).

The [enemy flamethrower](enemy-flamethrower.md) also separates a wave-loaded
rifle field from its selected experience-based navigation and shape-based
victim component. [Exact stages](../player-enemy-flame-evidence.md)

Additional sources: [Source identities](../player-notes/enemy-stats.md#citation-1)

[Regular and Jugend](enemy-regular-and-jugend.md) share the half-wave rifle
initializer but differ in the later shot-body attempt gate, target-health filter
and continuation. A declared shared rifle/XP pair still does not make their
per-visit source branches identical. [Exact comparison](../player-regular-jugend-evidence.md)
Additional source: [Source identities](../player-notes/enemy-stats.md#citation-2)

## A rifle value is not a guaranteed shot or kill

The inspected German Sniper firearm still has an attempt roll involving
experience before its accuracy comparison, then separate cover/damage handling.
At W=100 the load sets rifle 100; that is not a promise it fires continuously or
kills every target. Its ordinary-cover save and lack of the inspected bunker
save are also actor-specific. [Defense exceptions](defenses.md)

Changing local wave does not, from these **load assignments alone**, retroactively
reroll every existing enemy. Exact spawn/caller overrides, caps/later writers,
geometry and runtime results remain part of the shared reconstruction. These
examples already answer why a single community stat range can be misleading
without a wave and actor context.

Sources: [Source identities](../player-notes/enemy-stats.md#citation-3). [Exact evidence and limits](../player-campaign-evidence.md)

## A vehicle turret can use another wave counter

The [SdKfz 222](sd-kfz-222.md) turret load reads mission-total wave in
random(totalwave), while its hull loads rifle 1–10 and many infantry use local
wave divided by 2. At supplied totalwave 50, the turret roll is 0–49. Its shot
reads that child rifle, not the hull field. This is another reason to name
both receiver and wave context; the actual turret-load ordering remains open.
[Exact parent/child readers](../player-light-vehicle-evidence.md#the-222-turret-reads-mission-total-wave-not-hull-rifle)
Additional source: [Source identities](../player-notes/enemy-stats.md#citation-4)

## A later action helper can read wave again

The common enemy timer helper's body writes a random value minus **current
local wave**, with a floor of 20 in that written field. Regular and Jugend call
it under different reset guards. This is a later wave read, separate from the
wave supplied to an earlier rifle load. The source return uses a different
spelling from its written field, so return/receiver binding and callback order
remain explicit reconstruction needs before treating it as a final action timer
or elapsed fire rate. [Helper, declared field values and caller comparison](../player-enemy-timer-evidence.md)
Additional source: [Source identities](../player-notes/enemy-stats.md#citation-5)

A truck's [unload helper](enemy-truck.md) requests a new Regular, Volkssturm or
Grenadier and sets placement fields without directly copying truck combat stats.
Its infantry load-wave and later writers need their own birth trace; the parent
truck's earlier wave or remaining crew is not a ready-made child stat table.
[Source caller, fields and lifecycle limits](../player-truck-lifecycle-evidence.md#the-unload-helper-chooses-a-new-actor-rather-than-transferring-truck-stats)
Additional source: [Source identities](../player-notes/enemy-stats.md#citation-6)

## A new wave does not itself rerun an old load assignment

The wave formulas above read their input when a load body executes. They are
not continuously linked to the displayed wave counter. A later stat change
needs an actual writer; the accepted finite rifle-assignment map separates
load bodies, training/crew/crate writes, aliased promotion and profile snapshots.
It does not certify that every already-living enemy keeps its initial value.
[Writer map and runtime limits](../player-rifle-writer-evidence.md).
Additional source: [Source identities](../player-notes/enemy-stats.md#citation-7)

## Half-point rifle is not rounded down for a shot test

The selected Volks accuracy comparison is a strict integer 0–99 roll below its
current rifle field. Fixed rifle 0/0.5/1/1.5 therefore admit 0/1/1/2 integer values;
rifle 20/20.5 admit 20/21. These are conditional comparison counts, not hit chances
for every enemy or an entire wave. Earlier attempt checks, saves and damage remain.
[Named source and exact inputs](../player-enemy-rifle-threshold-evidence.md#fixed-rifle-inputs-meet-a-strict-integer-roll-test)

The retained observed wave 2 birth supplies two actual rifle 0 loads, while the
source formula can also produce 0.5 there. Applying the shot predicate later
still requires unchanged fields and an actually reached combat action; that
recording qualified birth rather than a whole battle.
[Observed boundary and conditional reader](../player-enemy-rifle-threshold-evidence.md#reuse-the-qualified-birth-without-claiming-qualified-combat)
Additional sources: [Source identities](../player-notes/enemy-stats.md#citation-8)

## A named enemy effect can reach an aliased later writer

The [enemy mortar owner-credit chain](enemy-mortar.md#loaded-stats-are-not-automatically-the-last-writers)
provides a concrete conditional path beyond its load: another enemy recipient's
blast branch can credit the mortar owner, then generic promotion can write its
rifle. That source path is separate from the wave at load and does not establish
observed enemy friendly-fire rates or every final writer. The fixed mortar
impact expressions still do not read that rifle value.
[Exact caller/receiver and declared promotion example](../player-enemy-mortar-credit-evidence.md).
Additional sources: [Source identities](../player-notes/enemy-stats.md#citation-9)

The [Nebelwerfer](nebelwerfer.md) instead loads rifle 1–10 and XP 20 without a
wave term in those expressions. Its selected impact offsets do not read either
field. Keep that launcher separate from the local-wave infantry table and from
claims about every possible later writer.
Additional source: [Source identities](../player-notes/enemy-stats.md#citation-10)

## Detailed Orders changes an input, not every enemy already on the field

The crate's selected outcome subtracts 15 from **local wave**, without writing
mission-total wave at that site. That subtraction alone does not rerun existing
rifle loads. If a living German Sniper still has rifle 50 and the local input
changes 50→35, a separately reached new Sniper load at 35 writes 35; the crate does
not itself turn the earlier rifle 50 into 35.

Random-load families need another distinction. Their possible range can shrink
while the next individual still rolls higher than an earlier enemy. For declared
separate inputs, an old divided-family load at W50/draw 0 gives rifle 0, while a
new one at W35/draw 34 gives 17. Both fit their own ranges. This does not predict
the next enemy, qualify an actual spawn sequence or guarantee a lower hit rate.
[Exact supplied-input comparison](../player-campaign-evidence.md#a-lower-local-wave-is-not-a-guaranteed-lower-realized-rifle-value)

A later enemy timer helper can read the **current** local wave, whereas the
SdKfz222 turret uses mission-total wave for its separate load. These consumers
must be named before describing the crate as a squad-wide difficulty reduction.
[Later timer boundary](../player-enemy-timer-evidence.md), [vehicle receiver](sd-kfz-222.md)
Additional source: [Source identities](../player-notes/enemy-stats.md#citation-11)

## “Priority” is a separate load field used by a Sniper selector

These selected infantry loads initialize another field independently of their
wave-rifle expressions:

| Named load family                                                    | Priority field |
| -------------------------------------------------------------------- | -------------- |
| German Officer                                                       | 10             |
| Enemy MG / Mortar                                                    | 9              |
| German Sniper                                                        | 8              |
| SS                                                                   | 7              |
| Jugend                                                               | 6              |
| Enemy parachute infantry                                             | 5              |
| Rocket soldier                                                       | 4              |
| Grenadier / Flamethrower                                             | 3              |
| Regular, Scout, Pioneer, Brandenburg placements / hidden infiltrator | 2              |
| Volkssturm / Zombie                                                  | 1              |

This is not a measured threat ranking or a promise that higher priority always
gets shot first. The Allied Sniper's selected search compares distance/priority
but stores raw distance afterward, so scan order can change its choice. With
declared Officer priority 10 at distance 100 and Grenadier priority 3 at 200, the
later Grenadier can replace that Officer; reversing their scan order can leave
the Officer selected instead. Other eligibility and callback state still apply.
[Exact 18 placements, source reader and supplied comparison](../player-enemy-priority-evidence.md).
Additional source: [Source identities](../player-notes/enemy-stats.md#citation-12)

## Half-point rifle does not mean that exact percentage

The selected Regular and Jugend loads can store rifle 20.5. Their strict
below-rifle shot comparison against integer 0–99 draws admits 21 values, so
that isolated comparison passes 21%, under supplied uniform inputs. Rifle 20
admits 20 values. This counts possible draws; it does not round the stored stat
or supply the earlier attempt, frame navigation and later saves.

With declared unchanged uniform load inputs at local wave 50, mean stored rifle
is 12.25 while the mean isolated comparison count is 12.5 out of 100. This is a
conditional calculation, not a measured spawn distribution or enemy battle hit
rate. Actual births, later writers and which actors reach the shot still matter.
[Exact integer boundaries, wave inputs and limits](../player-half-rifle-evidence.md).
Additional source: [Source identities](../player-notes/enemy-stats.md#citation-13)

## Assault Expert changes enemy load morale in different ways

Across the 18 selected enemy-unit placements, the two morale writes form six
patterns. Most start at 0–99 and subtract 10 under a positive Assault Expert
flag; German Sniper starts at 5–104, Jugend at 70 and the Brandenburg families
at 25–74 before that subtraction. Volkssturm and Zombie instead **replace**
their base morale with 2. These selected morale expressions do not use local wave.

For a supplied Volks base value 1, that replacement raises it to 2; Zombie's
999 becomes 2. A Regular's admitted subtract-10 load can be negative, which
matters to its separately reached morale-based pin recovery. Those are field
comparisons, not final spawned stats or battle pin/retreat rates. Changing the
wave does not itself execute these load writes again on an existing actor.
[Exact 18-placement map, ranges and named later readers](../player-enemy-morale-loads-evidence.md).
Additional source: [Source identities](../player-notes/enemy-stats.md#citation-14)

## Wave-dependent rifle does not scale every bullet's health draw

The selected direct firearm view has 13 health-subtraction sites with fixed
bounds. These are already-admitted unarmored damage draws, after each actor's
own attempt, accuracy, range and save guards:

| Selected shooter                                                        | Health subtraction draw | Inputs leaving health below 10, starting at 100 |
| ----------------------------------------------------------------------- | ----------------------- | ----------------------------------------------- |
| German Officer                                                          | 0–49                    | 0 of 50                                         |
| Hidden infiltrator                                                      | 0–79                    | 0 of 80                                         |
| Regular / Volks / SS / Grenadier / MG / Para / Jugend / Scout / Pioneer | 0–99                    | 9 of 100                                        |
| Brandenburg shared 1391 body                                            | 0–149                   | 59 of 150                                       |
| German Sniper                                                           | 0–199                   | 109 of 200                                      |

At the 0–99 draw, damage 91–99 leaves health 9–1 and still passes the selected
below 10 death-state request; damage 90 leaves 10 and fails it. A request is not
proof of nonpositive health, removal or credited death. The listed health draws
do not read wave, rifle or XP, while those fields can still change other stages.
These counts are not kill probabilities per shot or encounter.
[Exact finite view, declared inputs and health/navigation boundaries](../player-enemy-firearm-damage-evidence.md).
Additional source: [Source identities](../player-notes/enemy-stats.md#citation-15)

## Matching rifle loads still have different shot gates

The [Pioneer](enemy-pioneer.md#its-gun-has-a-separate-burst-counter) and
[Scout](enemy-scout.md#its-firearm-is-separate-from-its-support-call) both load
rifle from half the local-wave roll. Their selected firearm accuracy tests
subtract twice the current burst counter. The Scout additionally needs a
local attempt roll against 10+experience; the Pioneer's selected shot does not.

With supplied XP 20, rifle 40 and burst 10, a reached Pioneer shot admits 20% of
accuracy inputs, while the Scout's extra attempt gate reduces admission to 6%.
These are conditional source comparisons before damage and supplied defenses,
not rankings or whole-burst results. Repeat navigation also has a different
order around the burst decrement, so the same starting fields do not certify
identical later shots. [Pioneer source](../player-pioneer-evidence.md#burst-changes-the-firearm-accuracy-reader),
[Scout source](../enemy-scout-requests.md#the-ordinary-firearm-has-its-own-experience-and-burst-readers).
Additional sources: [Source identities](../player-notes/enemy-stats.md#citation-16)

The [SS current-burst comparison](ss-infantry.md#a-wave-loaded-rifle-number-still-meets-the-current-burst)
also keeps the load wave separate from a later accuracy reader. Its declared
unchanged-load ensembles differ with the supplied current burst; a load-range
maximum is not one realized per-shot percentage or an initialized birth recipe.

The enemy MG combines a **half-wave load** with a later penalty of **three times current burst**, unlike the SS's full-wave load and two-times penalty. At supplied
unchanged load wave 20/current burst 3, its strict accuracy reader admits only one
of the 2,000 declared load/shot input pairs; lowering the separately supplied
current burst to 1 changes that to 49. Neither fraction is a qualified spawn or
battle rate. [Exact MG inputs and reader boundaries](../player-enemy-mg-evidence.md#an-unchanged-half-wave-rifle-load-and-current-burst-are-separate-inputs).
Additional source: [Source identities](../player-notes/enemy-stats.md#citation-17)

## A mean rifle field can hide the comparison's ceiling

For a declared unchanged Regular/Jugend load wave of 400, uniform independent
load/shot inputs give a mean rifle field of 99.75, but only **75% of that input
domain** passes their isolated strict rifle comparison. Half the supplied loads
have lower fields; the higher half already admit every one of the 100 possible
shot integers. The extra high values cannot contribute more than all 100.

Putting the mean field into the comparison is therefore different from averaging
its bounded outcome across those loads. At declared load wave 1000 the stored
mean is 249.75 while the corresponding marginal passing fraction is 90%, not an
unbounded percentage. Neither row is an actual wave's hit rate or difficulty.
[Exact high-wave sum, four domains and source limits](../player-half-rifle-evidence.md#higher-declared-load-waves-saturate-the-reader-without-capping-rifle).
Additional source: [Source identities](../player-notes/enemy-stats.md#citation-18)
