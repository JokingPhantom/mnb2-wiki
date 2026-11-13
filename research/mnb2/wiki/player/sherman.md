[Player reference](README.md) · [Vehicles and emplacements](vehicles-and-emplacements.md) ·
[Repair, crew or reload?](repair-crew-and-reload.md)

# Sherman tank

The selected **20-TP Tank offer** creates a Sherman, with **1000 starting health
and armor class 2** in its nonstock load. Its main cannon, coaxial gun and optional
paid .50 mount use different attack paths. A single rifle or damage row does not
describe all three. [Exact 2.3.1g source](../player-tank-evidence.md)

Applies to **historical selected 2.3.1g**. The tank body and individual guns do
not all use one shared set of stats. Starting health and crew can change later.

| Key fact                     | Selected historical load                                |
| ---------------------------- | ------------------------------------------------------- |
| TP cost and availability     | 20 TP; Tank offer, optional .50 costs another 4 TP      |
| Health / maxhealth           | 1000 / 1000                                             |
| Armor class                  | 2                                                       |
| Driver / gunner / spare crew | 1 / 1 / 0                                               |
| Rifle                        | 1; Combat Ribbon adds 3 at its load branch              |
| Experience / rank            | 0 / 0; Mud and Blood Cross adds 9 XP at its load branch |
| Optional .50 flag            | Off                                                     |

[Starting-field evidence](../player-tank-evidence.md)

Start with your question: [What does the base tank include?](#what-the-base-tank-and-optional-gun-provide),
[what does the extra .50 change?](#the-4-tp-50-upgrade-has-its-own-formula),
[can its guns choose different targets?](#its-guns-can-acquire-different-targets), or
[what stops movement?](#movement-has-its-own-health-and-destination-tests).

## Plan the base tank and the optional upgrade separately

For normal paid purchases, **20 TP buys the Tank offer** and the separate
**4-TP .50 offer makes 24 TP total** if its intended recipient step completes.
That total excludes repairs, replacement crew, defenses and other support. It
is an arithmetic commitment, not a recorded arrival or combat result.

- **Before buying:** compare what answers armor while saving the 20 TP. A prior
  4-TP Bazooka plus the later base tank is also 24 TP, but it buys two different
  units, not the tank's .50 upgrade. [Armor-transition study](strategy-studies.md#answer-armor-before-committing-to-a-tank-transition).
- **After buying:** distinguish the offer's charge from the Sherman actually
  arriving. The optional .50 then needs its own recipient handling; paying for
  that offer does not by itself prove the gun was enabled or fired.
- **During combat:** watch each weapon's actual attacks and the target's resulting
  state. The cannon/coax and optional .50 can aim at different enemies, so one
  gun's action is not evidence that all systems chose that target.
- **When movement or fire stops:** check the component and current state before
  treating the pause as a reload or assuming a crew rule from a different vehicle.
  Use the movement and targeting sections below, then compare
  [repair, crew replacement and reload](repair-crew-and-reload.md).

If the cannon misses, a higher displayed rifle number does not tighten its
inspected impact-offset expression. If the tank is harmed, armor class 2 is not
immunity from every eligible anti-tank effect. [AT damage stages](anti-tank-and-vehicles.md),
[alternative AT commitments](anti-tank-options.md).

## What the base tank and optional gun provide

| System       | Cost relationship                                 | Important distinction                                                                     |
| ------------ | ------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Main cannon  | Part of the base tank's selected attack paths     | Armor-first targeting; its inspected impact offsets do not read rifle or XP               |
| Coaxial gun  | Another base-tank attack alternative              | A firearm path with its own burst and hull-rifle comparison                               |
| Optional .50 | Separate 4-TP offer, then tank recipient handling | Its own target/counter and firearm rules; it does not simply reuse the static .50 formula |

Budget the optional gun separately from the **20-TP base offer**, then check
that its recipient step actually enabled it. A selected target, a paid upgrade
and a completed shot are different events. The guns can also hold different
targets; one accuracy number does not describe the entire tank.
[Exact cannon, coax and optional-gun evidence](../player-tank-evidence.md),
[separate gun targets](#its-guns-can-acquire-different-targets).

The rows describe selected historical **2.3.1g** source paths, not a measured
damage ranking or a guarantee every system fires in a given encounter.

The turret initializes its own rifle 1 / XP 2 fields. Those are separate from the
hull fields read by the inspected coax and .50 firearm comparisons. Do not copy
the infantry's random-stop rifle initializer onto this tank. Armor 2 is a class,
not a percentage reduction or a guarantee against an eligible AT blast.
[Vehicle handling](anti-tank-and-vehicles.md)

## Movement has its own health and destination tests

The selected active hull can enter movement with health above 0; its local
movement body has no driver/gunner gate. Offsets must exceed 3 on at least one
axis, and an obstacle-shape test still controls the position write. Supplied
health 1 or driver 0 is therefore not the ordinary infantry's incapacitation rule
at this site. This is a source comparison, not a proven battlefield tactic or
speed in seconds.

At y below 15 with positive health, the hull writes invincible and a new lower
position/destination before calling advance. The turret separately excludes an
invincible parent. At nonpositive hull health, the parent requests a wreck and
removal. Those stages need their own callback and accounting context; they do
not establish that every loss invokes the infantry death helper.
[Exact movement, advance and wreck](../player-tank-evidence.md#hull-movement-advance-and-wreck-have-their-own-guards)

## Targeting and first readiness differ from later resets

The main turret first selects the **first indexed living armored target with
line of sight**. It only uses the nearer-target fallback when that pass finds
none. The fallback has its own visibility, invincibility and distance-above 300
checks; 300 is not a universal minimum range against armor.

The child initially loads a random 0–199 counter. Later expiry resets draw again,
then raise values below 60 to 60, including some no-shot outcomes. That is not a
uniform 60–199 draw or a reload time in seconds. Its parent-health/protection,
random-selection and animation gates still matter.
[Acquisition and counter order](../player-tank-evidence.md#turret-acquisition-and-cannon-selection)

## Cannon and coaxial fire are different choices

After a target is found, one branch requests the cannon; the alternative starts
a coaxial burst counter 3–12. The selected cannon creates an effect around the
then-current target coordinates, with separate integer offsets **−100..+99** on
each axis. Those writes do not read rifle, XP or the stored blastrange field.
[The range field and emission](../player-tank-evidence.md#cannon-placement-is-not-its-blastrange-field)

The cannon effect supplies **AT radius 40, fragment radius 40 and damage input 300**
with tag **tank**. These are separate inputs, not unconditional 300 damage. The
coaxial firearm instead uses an inclusive roll against hull rifle and a selected
unarmored damage draw **0–124**. Parent health and crew, actual target state,
blast geometry and later recipients remain separate questions.

## The 4-TP .50 upgrade has its own formula

The selected logistics offer charges 4 TP before a recipient click. Its tank-button
receipt can enable the .50 flag; another selected branch refunds 4 when that receiver's
flag is not zero. A cue is not a completed upgrade or a universal refund promise.
[Menu versus receipt](../player-tank-evidence.md#coaxial-and-optional-fifty-firearm-paths)

The optional gun's inspected body **subtracts twice positive burst** from its
accuracy roll, while the [static .50](fifty-caliber.md) shared helper adds it.
At supplied hull rifle 20 / burst 4, 29 of 100 integer values pass the optional gun's
comparison versus 13 for the static helper. This illustrates different formulas;
it is not comparative battlefield accuracy or a firing-rate ranking. Its selected
unarmored damage draw is 0–199, with separate armor/crew and target/cycle guards.

The selected AT helper uses point-coordinate distance, rather than visible
vehicle width, at its AT eligibility predicate. Effect placement and actual
coordinate transforms still need qualification before estimating whole-shot
success. [AT geometry boundary](../player-tank-evidence.md#the-selected-at-gate-reads-points-not-an-outline)

Sources: [Source identities](../player-notes/sherman.md#citation-1). [Version and exact evidence](../player-tank-evidence.md)

## The Tank button directly charges20TP

This selected offer requires allocation below 100 and at least 20 TP, then subtracts
20 before requesting the Sherman template. Unlike the inspected Halftrack offer,
this button has no uniqueness-flag check and no medal waiver. That source
difference does not certify unlimited deployments or completed arrivals.
[Exact vehicle-offer comparison](../player-recruitment-receipt-evidence.md#halftrack-availability-and-tank-payment-differ)
Additional source: [Source identities](../player-notes/sherman.md#citation-2)

## Its guns can acquire different targets

The main turret and optional .50 keep separate target and timer fields. Both
search armored candidates first, but their nearer-target fallbacks differ:
the turret requires helper distance above 300 there; the optional gun does not.
The coax reads the turret's target, while the optional gun reads its own.
[Exact component receivers](../player-sherman-repeat-evidence.md#turret-and-optional-gun-do-not-read-one-shared-target-field)

The coax repeat decrements the turret's burst before deciding to repeat. The
optional gun instead repeats while its own burst is above one, with a separate
terminal counter write of 1–200. An initial burst field is not a verified count
of completed shots: later targeting, counters, pause and animation requests
remain part of each component's cycle.
[Reached repeat and recovery actions](../player-sherman-repeat-evidence.md#the-coax-repeat-decrements-its-parents-burst)

Neither selected acquisition controller adds a parent driver/gunner gate.
Their later shot actions also do not repeat every acquisition guard. These
source boundaries do not prove firing after crew loss or parent removal;
actual component survival and callback order remain necessary.
[Guard scope](../player-sherman-repeat-evidence.md#the-optional-guns-repeat-has-a-different-terminal-counter)

At supplied hull health **0**, this parent's health>0 test fails and selects its
tankwreck/removal branch. Jeep and AA parents have different equality predicates.
The local wreck is separate from earlier damage/accounting and from actual gun-
component lifetime; it does not certify a whole destruction or casualty outcome.
[Exact parent comparison and operations](../player-vehicle-wreck-evidence.md).
Additional source: [Source identities](../player-notes/sherman.md#citation-3)
