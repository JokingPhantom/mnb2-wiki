[Player reference](README.md) · [Explosives](explosives.md) · [Collateral damage](collateral-damage.md)

# Fire, burning soldiers and water

A burning figure can be a **separate spreading hazard**, rather than a wounded
soldier waiting for ordinary healing. The selected 2.3.1g source distinguishes
flame-component damage, conversion into a burning hazard, flamer explosions and
water contact. Bullet-save percentages do not describe all four mechanisms.
[Flamethrower](flamethrower.md), [enemy flame soldier](enemy-flamethrower.md)

Start with your question: [Is the burning figure still my soldier?](#the-original-victim-and-the-burning-hazard-are-different-objects),
[can the fire spread to either side?](#a-burning-hazard-can-spread-to-either-side),
[does steam mean the soldier was rescued?](#steam-is-not-a-receipt-that-a-soldier-was-rescued), or
[is a burning tree the same hazard?](#a-props-burn-reader-is-separate-from-ordinary-cover), or
[what do burn counters establish?](#burn-counter-death-navigation-and-removal-are-separate).

## The original victim and the burning hazard are different objects

Some selected flame branches replace the original victim with a **new burning
hazard** at its position; the source names that hazard `crameur`. The original
unit then follows its own health, accounting and removal path. Ordinary healing
or a movement order should not be assumed to control the new hazard.

Other flame hits subtract health without that same immediate replacement.
Distinguish an injured original actor from a separate burning hazard before
expecting the usual patient or unit controls. A burning image alone does not
settle which state remains. [Wounded and rescued soldiers](wounded-and-rescued.md).
[Exact flame conversion](../flamethrower.md), [enemy conversion and partial damage](../player-enemy-flame-evidence.md)

A flamer explosion is another effect, combining a generic blast with separate
burn-conversion scans. It is not simply a larger ordinary bullet or a guaranteed
explosion on every flamer death. An admitted nonfatal firearm hit has its own
possible enemy-flamer explosion trigger.
[Effect branches](../flamer-explosion.md), [nonfatal trigger](../player-shared-flamer-trigger-evidence.md)

## A burning hazard can spread to either side

The hazard is dangerous to qualifying troops on **both sides**, not just the
enemy. Ordinary incoming-bullet cover percentages do not describe this spread
scan, and water/steam does not establish that the original soldier was restored.
The guards below explain the difference; they are not a safe spacing or exposure
time. [Spread and water evidence](../burning-hazard.md).

In the named hazard's reached unpaused spread action, player and enemy scans
use different health gates:

| Candidate | Health requirement      | Armor | Later distance/random guards                                 |
| --------- | ----------------------- | ----- | ------------------------------------------------------------ |
| Player    | Defined and at least 10 | 0     | Helper distance below 25; uniform 0–99 draw below 5          |
| Enemy     | Above 0                 | 0     | Helper distance below 25; separate uniform 0–99 draw below 5 |

A positive-health player at 9 fails this spread health test, while an enemy at 9
can pass its own health part. That is not general immunity to flames or other
damage. The local below 5 comparison accepts five integer inputs for one admitted
candidate; it is not a five-percent-per-second or whole-attack risk. Actual
positions, action entry and every later effect still matter.
[Exact spread, receivers and limits](../burning-hazard.md#nearby-player-and-enemy-scans-have-different-health-guards)

The player conversion calls fear, creates another burning hazard, writes the
original player's health negative, calls the death helper and requests removal.
The enemy conversion has different career-counter processing. Do not equate the
two source paths with identical XP, casualty or score outcomes.

## Steam is not a receipt that a soldier was rescued

The selected water-contact test reads water-tagged decoration points and calls
the burning actor's shape test on them. Its direction is **not automatically the
same as a soldier's point lying anywhere inside a drawn pond**. A qualifying
contact writes the hazard's burn counter negative and requests a steam effect.
[Water query and counter write](../fire-and-water.md)

That write does not restore the previously removed soldier. The later spread
predicates also do not repeat a positive-burn-counter condition. Actual action
navigation, callback order and removal determine what executes; neither steam
nor the negative counter proves every possible later spread action was skipped.
This source does not certify a water rescue tactic or a safe pond boundary.
[Water and later spread scope](../burning-hazard.md#waters-counter-change-is-not-the-complete-control-flow)

## Burn counter, death navigation and removal are separate

The hazard's selected load starts a 60–459 burn counter. Its active controller
can request the death animation at one counter boundary, while terminal removal
has another life-state condition. These are source counters and requests, not a
measured lifetime in seconds or proof that a particular extinguishing image
already removed every hazard.
[Counter and lifetime sites](../burning-hazard.md#load-values-do-not-specify-a-measured-lifetime)

A Sarge conversion can also reach separate squad-morale helper calls; losing one
figure and changing other soldiers' morale are different effects.
[Exact Sarge caller comparison](sarge.md#fire-conversion-can-reach-two-separate-sarge-morale-penalties)

Selected publisher-associated 2.3.1g; original synthesis of the linked source
notes. No new burn, spread, water, geometry, casualty or timing trial.

[Source identities](../player-notes/fire-and-burning.md#citation-1)

## A prop's burn reader is separate from ordinary cover

The selected treeBurn helper tests its effect shape against a scanned prop's
point, then needs current type tree and a template other than burned. It does
not locally test the flamable field, health, ordinary cover or a bunker save.
This is one named helper, not a global rule for every fire path.

The crate-shaped 1579 scenery load uses tree/cratemc fields, despite having its own
ordinary-cover child. A separately admitted passing burn query can therefore
reach that helper's burningtree request and original-removal site. Actual
replacement, later cover and casualties still need their own source/host state;
this is separate from burning-soldier hazards and reward-crate collection.
[Exact three-query comparison and pending load/lifetime boundary](../player-tree-tagged-crate-evidence.md#burn-blast-and-ordinary-cover-use-different-query-forms)
Additional source: [Source identities](../player-notes/fire-and-burning.md#citation-2)

The burning-tree source has a separate local hazard visit: an unarmored friendly
needs at least 10 health, while the enemy branch accepts positive health. Both
also require the supplied distance below 25 and a random draw below 5 out of 100.
These are conditional checks on a visit; they do not establish seconds of safe
exposure or a cumulative chance. The clone's burned template excludes it from
this particular scenery-propagation gate after that load has completed.
[Exact load, gates, declared inputs and callback limits](../player-tree-tagged-crate-evidence.md#burning-tree-load-and-a-separately-admitted-casualty-visit)

A burning tree is not the burning-soldier hazard. Their loads use the same
burntime spelling, but the selected soldier's decrement and water writes belong
to the burning-soldier hazard's own callbacks. They are not a proven tree expiry or extinguishing rule.
[Finite field-owner audit](../player-tree-tagged-crate-evidence.md#a-shared-counter-spelling-does-not-share-its-callback-owner)
