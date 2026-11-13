[Player reference](README.md) · [Vehicles and emplacements](vehicles-and-emplacements.md) ·
[Halftrack roles](halftrack.md)

# Halftrack weapon modules

The Halftrack's quad guns, AT gun and mortar have **different target and firing
paths** in selected publisher-associated 2.3.1g. Their own weapon fields do not
make them ordinary infantry guns, and a hull rifle increase does not automatically
tighten their inspected shot or impact formulas.
[Exact components and readers](../player-halftrack-weapons-evidence.md)

If a converted Halftrack does not fire, first check its **gunner, module and
eligible target**, rather than interpreting hull rifle as every weapon's accuracy.
The selected weapon controllers need a gunner even for their waiting-counter
decrements; the hospital's healing entry has different requirements.
[Weapon ready/counter evidence](../player-halftrack-continuation-evidence.md),
[hospital comparison](halftrack-hospital.md).

| Module       | Additional TP | Minimum selection distance (source units) | Attack check or axis offsets                         |
| ------------ | ------------: | ----------------------------------------- | ---------------------------------------------------- |
| Quad guns    |            15 | No extra minimum in this scan             | Four separate actions; each integer comparison is ≤5 |
| 75 mm AT     |            12 | Strictly above 400                        | Current target plus independent −100…99 offsets      |
| 81 mm mortar |            10 | Strictly above 300                        | Current target plus independent −150…149 offsets     |

Module prices are additional to the **12-TP base Halftrack**. Buying another
module replaces its role and support flags, rather than stacking all modules.
[Purchase/replacement rules](halftrack.md)

The selection distances are not safe blast boundaries or guarantees of an
emitted shot. Read each module's target, protection and later-effect conditions
alongside its cost.

Applies to **historical selected 2.3.1g**. Compare the module price and
its target requirements; these are not measured rates or safe blast boundaries.

On this page: [Selection can fail before any attack](#selection-can-fail-before-any-attack), [Four quad shot actions are not four guaranteed hits](#four-quad-shot-actions-are-not-four-guaranteed-hits), [AT and mortar impacts use later coordinates](#at-and-mortar-impacts-use-later-coordinates), [A missing gunner also stops these waiting-counter writes](#a-missing-gunner-also-stops-these-waiting-counter-writes).

## Selection can fail before any attack

These three weapon controllers require a gunner, unpaused noninvincible hull
state, an expired turret timer and a nonbunkered result. The mortar also checks
that the hull is not camouflaged. An additional 75-of-100 comparison precedes
their search for a living, visible, noninvincible, line-of-sight target.

The AT scan's strict >400 condition applies to this selected scan; exactly 400
fails. The [M3 AT gun](m3-at-gun.md) differs: its first armor-priority pass has
different rules, and >400 belongs to its fallback search. The Halftrack AT scan
has no armor-priority pass in this inspected controller.
[Exact guards and reset](../player-halftrack-weapons-evidence.md#ready-target-searches-and-timer-reset)

Expired timers can reset even if no attack is requested. Their 0–199 or 60–259
source values therefore do not establish firing intervals in seconds.

## Four quad shot actions are not four guaranteed hits

The quad has four distinct shot-action frames with separate shot-counter
increments and draws. Each inspected initial comparison accepts **six values
out of 100: 0 through 5**. The comparison does not read rifle, experience or
burst. That is a conditional source count for a reached action, not a universal
6% battle hit rate or proof every animation executes all four actions.

Armor and health then route the admitted result. Unarmored health damage uses
a 0–99 draw; armor-1 crew handling and named vehicle exceptions differ; armor 2
has a ricochet branch. The hit counter is incremented before those distinctions.
Hull XP can be awarded on the inspected unarmored kill route, which is a separate
effect from changing the shot threshold.
[Quad action and continuation evidence](../player-halftrack-weapons-evidence.md#quad-has-four-separate-shot-actions-not-one-shared-weapon-call)

## AT and mortar impacts use later coordinates

Their firing actions read the target's coordinates again, then add fixed random
axis offsets. Neither selected placement expression uses rifle, XP or visible
vehicle width. Selection range is not an impact circle, and an emitted effect
is not automatically a hit on the chosen vehicle.

The two effects also call the explosion helper with different AT, fragment,
damage and special-tag inputs. The AT emission's owner expression differs from
the mortar's; full credit/ownership is still unresolved. These facts do not
certify a vehicle hit probability or total combat ranking.
[Exact effect and owner expressions](../player-halftrack-weapons-evidence.md#at-and-mortar-emissions-read-later-target-coordinates),
[AT recipient rules](anti-tank-and-vehicles.md)

The [hospital module](halftrack-hospital.md) has another controller and does not
repeat the gunner requirement at its own selected healing entry.

Sources: [Source identities](../player-notes/halftrack-weapons.md#citation-1)

## A missing gunner also stops these waiting-counter writes

The selected quad, AT and mortar controllers require a positive hull gunner
before entering either their ready attempt or positive-timer decrement. For a
supplied valid turret timer 10, one otherwise-admitted callback with gunner 1
writes 9; gunner 0 leaves 10 at those sites. Hull invincibility and pause also gate
that counter section. Bunker classification instead belongs to the expired
attempt, so it is not an extra guard on every positive decrement.
[Exact counter scope](../player-halftrack-continuation-evidence.md#gunner-and-invincibility-gate-the-waiting-counter-too)

This does not prove gunner loss cancels an attack already underway. The quad's
later repeat action and AT/mortar's reached effect actions do not repeat every
controller gate locally. Their own stopped actions also do not create a new
universal refill/recovery timer. Full traversal, target lifetime and vehicle/
module removal remain separate. The quad's casing-copy order is irregular too;
visible casings are not a qualified bullet count.
[Later actions and casing scope](../player-halftrack-continuation-evidence.md#quad-repetition-is-a-separate-action)
Additional source: [Source identities](../player-notes/halftrack-weapons.md#citation-2)

## One hit need not finish a full-health infantry target

At a reached quad frame 3 with a valid living armor-0 enemy and pause 0, a
recorded hit can draw 0–99 health damage. From unchanged health 100, that local
subtraction leaves at least 1, so its below-1 death test cannot pass from this
one subtraction alone. From health 50, 50 of the 100 damage values do reach the
local death request. This is one selected action, not the whole four-action
animation or a guarantee of surviving a quad burst.
[Conditional counts and separate hit/death stages](../player-shot-outcome-evidence.md).
Additional source: [Source identities](../player-notes/halftrack-weapons.md#citation-3)
