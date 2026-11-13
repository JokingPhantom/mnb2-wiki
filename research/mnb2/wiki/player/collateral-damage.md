[Player reference](README.md) · [Explosives](explosives.md) · [Collateral damage](collateral-damage.md)

# Collateral damage and friendly fire

Your own squad can be hurt by mechanisms that are separate from enemy bullets.
In selected **2.3.1g**, check **which attack path runs and which recipients it
admits**. An explosion's owner, a bunker save and a healthy vehicle hull do not
provide one universal friendly-fire exemption.

On this page: [Which friendly-damage risk am I dealing with?](#which-friendly-damage-risk-am-i-dealing-with) · [Leave room for backblast, but do not read its drawing as a safe boundary](#leave-room-for-backblast-but-do-not-read-its-drawing-as-a-safe-boundary) · [Owner credit and owner immunity are different questions](#owner-credit-and-owner-immunity-are-different-questions) · [A vehicle can lose hull health and crew through separate draws](#a-vehicle-can-lose-hull-health-and-crew-through-separate-draws) · [A flamer explosion has more than one damage region](#a-flamer-explosion-has-more-than-one-damage-region) · [A burning clip is a new hazard, not a rescued soldier](#a-burning-clip-is-a-new-hazard-not-a-rescued-soldier)

## Which friendly-damage risk am I dealing with?

- **[Bazooka backblast](bazooka.md#keep-the-backblast-region-clear).** Both sides are scanned. Qualifying living unarmored recipients lose 1–3 health and receive an action-counter change; bullet cover is not a universal exemption.
- **[Blast and AT stages](explosion-damage-stages.md).** An Allied request does not make the whole explosion friendly-safe. Different stages check recipients and owner information separately.
- **[Vehicle fragments](vehicle-damage-and-crew.md).** A blast can change hull health and crew through separate checks. Repairing health does not replace a missing gunner.
- **[Flamer explosion](../flamer-explosion.md).** The ordinary blast is followed by additional burn-conversion scans. One blast radius or bullet-save percentage does not describe the whole effect.
- **[Burning hazard](fire-and-burning.md).** A new hazard can spread to qualifying nearby troops on either side. Water or steam does not promise restoration of the removed soldier.

These are source paths with conditional eligibility, not measured safe circles,
whole-attack risks or proof every nearby actor takes damage.

Check the mechanism before relying on a bunker, visible gap or ownership credit.
The exact tests below explain why the same protective assumption can fail for a
different path. [Defense distinctions](defenses.md), [owner-field evidence](../explosion-attribution.md).

## Leave room for backblast, but do not read its drawing as a safe boundary

Bazooka backblast uses the actor's backblast region against recipient points.
Its selected branch requires positive health and armor below 1, then subtracts
**1–3 health** and writes an action counter of **80**. Separate loops visit both
player and enemy entries. That counter is not yet an elapsed pin duration.

The backblast action does not apply the ordinary-cover and bunker bullet-save
table. A bunker save from an enemy rifle is therefore not evidence that this
region cannot hurt a soldier. Exact transformed placement remains unqualified;
the legacy guide's 1–4 damage description also differs from this selected source.
[Exact guards and source](../bazooka-backblast.md), [defenses](defenses.md)

## Owner credit and owner immunity are different questions

The common blast helper excludes its supplied **father argument** from its
later enemy/player damage scans. Before those scans it calls a separate AT
helper, whose recipient exclusion instead reads the **effect's dad field**.
Its selected enemy XP tail reads the effect's **father field**. These names are
not automatic synonyms.

A valid owner argument for the later blast scan therefore does not, by itself,
prove the earlier AT scan excludes that same actor or credits that actor. The
caller must actually populate the fields used by each stage. The inspected
AA ground emitters even write father at one site and dad at another; their
later small-explosion call reads father. Inheritance, other writers and actor
lifetime remain open, so the difference is not proof of guaranteed self-damage
or lost credit. [Exact owner readers](../explosion-attribution.md)

The common blast scans both sides; it is not made Allied-safe merely because
an Allied actor requested the effect. AT eligibility, bunker state, distance,
line of sight, armor and the actual recipient path still decide what happens.
[Blast order](explosion-damage-stages.md), [AT versus vehicles](anti-tank-and-vehicles.md)

## A vehicle can lose hull health and crew through separate draws

For a valid player vehicle surviving earlier dispatch and reaching the fragment
branch, health subtraction occurs **before** the armor-class-1 crew tests.
Driver and gunner loss use separate fresh random comparisons. Spare crew are
a different alternative when the initial gunner branch was not selected.
A failed crew roll does not undo hull damage; a successful crew roll does not
require the health-damage draw to have been large.

Repair and recrew address different state. A repaired hull is not proof that
its gunner is present, and one generic infantry bunker-save percentage cannot
be copied onto every vehicle damage branch.
[Exact fragment/crew order](../player-vehicle-blast-evidence.md),
[repair, crew or reload?](repair-crew-and-reload.md)

## A flamer explosion has more than one damage region

Certain attack branches can emit a flamer explosion; this is not a universal
10% chance on every flamer death. That effect calls the generic blast helper
and then runs additional conversion scans. One selected player branch requires
noninvincibility, bunker classification equal to false, unarmored state and
distance below 50. The alternative uses the **negation of that bunker-false
comparison** and distance below 100, without the same local armor test.

Those are different tests from the generic fragment radius. Do not interpret
this as a measured 100-pixel danger circle or a certified bunker exploit: actual
classification, transforms, live recipients and callback order still matter.
It does show why a single bullet-save percentage misses part of this effect.
[Exact conversions and accounting](../flamer-explosion.md)

## A burning clip is a new hazard, not a rescued soldier

The burning hazard has its own spread scan. Qualifying player recipients need
health **at least 10**; qualifying enemy recipients need health **above 0**.
Both selected paths use armor 0, strict source distance below 25 and a separate
random-below-5 test. These are per-visit guards, not 5% per second or a guaranteed
chain reaction. Player conversion has its own removal/accounting calls.
[Spread and lifetime](../burning-hazard.md)

Water contact can write a negative burn counter and request steam/animation
changes. That write does not restore the removed controllable soldier or prove
all intervening spread scans are skipped. Moving a hazard toward a pond is
therefore not a source-qualified rescue promise.
[Water source and limits](../fire-and-water.md), [Flamethrower](flamethrower.md)

Sources: [Source identities](../player-notes/collateral-damage.md#citation-1). Original synthesis of the linked exact notes; no new
friendly-fire, geometry, survival or timing trial.
