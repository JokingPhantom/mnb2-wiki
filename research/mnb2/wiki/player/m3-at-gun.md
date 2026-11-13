[Player reference](README.md) · [Vehicles and emplacements](vehicles-and-emplacements.md) ·
[Repair, crew or reload?](repair-crew-and-reload.md)

# M3 AT gun

An **8-TP, crewed anti-tank gun** with 500 starting health and armor class 1 in the
selected 2.3.1g load. Nearby M3 guns can prevent a firing request, and its shot's
explosion can land away from the selected target. Its targeting and attack work
differently from the Bazooka soldier's rocket.
[Version and exact evidence](../player-mounted-evidence.md)

Applies to **historical selected 2.3.1g**. Starting health, crew and counters
are source load fields; they do not guarantee arrival or a complete attack.

| Key fact                 | Selected historical load                                |
| ------------------------ | ------------------------------------------------------- |
| TP cost and availability | 8 TP; crewed gun offer                                  |
| Health / maxhealth       | 500 / 500                                               |
| Armor class              | 1                                                       |
| Driver / gunner          | 1 / 1; spare crew 0                                     |
| Experience / rank        | 0 / 0; Mud and Blood Cross adds 9 XP at its load branch |
| Initial action counter   | 200 source units                                        |

[Starting-field evidence](../player-mounted-evidence.md).

On this page: [Check readiness and spacing before reading a pause as a reload](#check-readiness-and-spacing-before-reading-a-pause-as-a-reload), [Why it may not fire](#why-it-may-not-fire), [Armor first; distant infantry is a fallback](#armor-first-distant-infantry-is-a-fallback), [Scatter and anti-tank damage are different stages](#scatter-and-anti-tank-damage-are-different-stages).

## Put the 8-TP commitment to work

The **8 TP buys the base gun offer**, not a repair service or replacement crew.
Compare a [4-TP Bazooka](bazooka.md) for a smaller initial anti-armor commitment,
or a [20-TP Sherman](sherman.md) for a tank with separate weapon systems. Choose
by the job and requirements, not an assumed damage-per-TP ranking.
[AT comparison](anti-tank-options.md).

After arrival, inspect health and crew, then use the
[vehicle selection and movement checks](controls.md#vehicle-clicks-use-different-crew-and-health-gates)
if positioning it. Watch for arrival at the destination: an obstacle can leave
it looking stationary while its movement branch still prevents the firing
counter from progressing. A destination marker alone is not a ready gun.

If it does not fire, check the settled position, crew, nearby M3 entries and
eligible targets before buying another gun. Another damaged or poorly crewed M3
can still count in the spacing check. If it fires without the expected vehicle
loss, inspect scatter and later damage checks; a visible blast is not guaranteed
hull damage. For damage or lost crew, choose
[repair versus crew replacement](repair-crew-and-reload.md) before spending on
the wrong service.

## Check readiness and spacing before reading a pause as a reload

- **Crew and destination matter.** Its selected controller accepts a positive
  driver-plus-gunner sum, but firing work belongs to the settled-position branch.
  A blocked movement step can leave the gun visibly still without reaching that
  branch. [Movement versus firing](#a-blocked-destination-is-different-from-being-ready-to-fire).
- **Another M3 can inhibit the request.** The nearby same-name scan does not
  ignore an entry just because its crew or health is poor. Its strict source
  distance is explained below, not a tested artwork-spacing stencil.
- **The fallback range is not the armor range.** The above-400 condition belongs
  to its fallback search; the earlier armor-priority pass has different rules.

[Exact crew, spacing and target evidence](../player-mounted-evidence.md#target-selection-and-spacing).
These are selected **2.3.1g** conditions, not a measured reload time or guaranteed
positioning fix.

The rifle initializer is a random stopping loop, followed by Combat Ribbon's
+3. It is not five fixed additions. **The inspected effect-placement spread does
not read rifle or XP**; a higher rifle number cannot be translated directly into
a tighter spread from those writes. [Source chain](../player-mounted-evidence.md#offset-effect-and-later-at-point-test)

## Why it may not fire

It needs a living active gun, unpaused state, a crew-sum above zero, the relevant
random/action gate and a sufficiently settled position. Either driver or gunner
can satisfy that sum condition; loss of one is not automatically the loss of all
operation. The targeting scan also excludes the gun being bunkered or invincible.
[Crew replacement](crewman.md), [repair](mechanic.md)

A different nearby entry **named M3 AT gun**, at source distance strictly below
100, increments a no-fire count. That scan does not test the other entry's health
or crew. Clustering two such guns can therefore inhibit this firing request;
100 exactly fails that closeness comparison. Artwork dimensions and practical
placement still require geometry qualification.

## Armor first; distant infantry is a fallback

The first target pass takes the **first indexed living armored enemy with line
of sight**. It does not sort that pass by nearest distance. If no such target is
found, the fallback looks for a nearer eligible visible target, with its own
hand-to-hand/LOS tests and distance strictly above 400. That fallback restriction
is not a universal minimum range against armor.

The expired action counter resets to 200 − XP after its branch, even through some
no-shot outcomes. Movement, random admission, target availability and timeline
callbacks keep this from being a universal reload time in seconds.
[Target and spacing guards](../player-mounted-evidence.md#target-selection-and-spacing)

## Scatter and anti-tank damage are different stages

The inspected firing frame creates an explosion effect around the selected
target's then-current coordinates. Each axis receives a separate integer
offset **−100 through +99** in that write. It does not test a shell against the
vehicle's visible outline there.

The later effect supplies **AT radius 50** and a separate damage input 300 to the
shared blast helper. Actual recipients still need armor, distance, visibility,
invincibility and other guards. A point 50 away fails a strict below 50 test;
points offset (35,35) and (36,36) fall on opposite sides because distance combines
both axes.
These examples assume unchanged shared coordinates, not observed hits or a
complete geometry model. [AT guards and Tiger exception](anti-tank-and-vehicles.md)

Its special tag is **at**, rather than the Bazooka effect's **zooka**. Do not copy
the Tiger's 500-health zooka exception onto this effect simply because both are
anti-tank weapons. Blast/friendly-fire outcomes and effect timing remain separate.

Sources: [Source identities](../player-notes/m3-at-gun.md#citation-1).
[Exact source evidence](../player-mounted-evidence.md)

## A blocked destination is different from being ready to fire

The selected controller chooses its movement branch when either destination
axis remains more than three source units away. If an obstacle blocks the step,
the gun can stay visibly still while that branch still writes moving=1.
Its firing-counter decrement and search instead belong to the already-settled
alternative. An unmoved picture alone does not prove this timer is counting down.

For supplied otherwise-admitted state and counter 150, an outstanding offset
(4,0) with a blocked step leaves that counter 150 at this site; settled offsets
(3,3) reach the decrement to 149. A counter of one decrements to zero without
also taking the expired search in that same visit. These are source inputs,
not a measured positioning fix or a reload time.
[Exact movement/rest and counter boundaries](../player-mounted-evidence.md#an-unmet-destination-can-keep-the-m3-out-of-its-timer-branch)

The outer live test is health above zero; zero instead enters the selected
wreck/removal branch. That differs from ordinary infantry's usable-health
threshold and the AA parent's zero-health predicate. Full damage accounting
and original-player removal order remain separate.
[Wreck and advancement scope](../player-mounted-evidence.md#live-movement-and-wreck-use-vehicle-health-rather-than-infantry-ten)

## One surviving crew role can satisfy its movement gate

The selected M3 parent movement needs aiming 0 and driver+gunner above 0, along
with unpaused/health/random/destination guards. For ordinary 0/1 role inputs,
both roles give step scalar 1, one role gives 0.5, and neither fails the crew gate.
It does not specifically require the driver rather than the gunner. Those are
per-reached-step source scalars, not measured travel speed or proof of firing.
The health-gated click selection alone does not test that crew sum.
[Exact selection and movement distinction](../player-vehicle-movement-evidence.md#the-m3-needs-some-crew-rather-than-specifically-its-driver).
Additional source: [Source identities](../player-notes/m3-at-gun.md#citation-2)
