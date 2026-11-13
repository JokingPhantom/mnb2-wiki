[Player reference](README.md)

# Controls and reading a soldier

**Click a soldier, then click its destination to order a move.** Hover over
the soldier to inspect health, rifle skill, experience and morale. Watch for
actual movement after the destination marker appears.

Applies to **historical selected 2.3.1g**. Two recorded runs show selection
feedback and movement; they do not verify every destination or device. Keyboard
shortcuts have separate limits below. Control evidence (local research)

Find your question: [how to inspect, move or equip](#how-to-perform-the-common-actions),
[selected but not moving](#why-is-a-selected-soldier-not-moving),
[vehicle controls](#vehicle-clicks-use-different-crew-and-health-gates), or
[keyboard shortcuts](#keyboard-instructions-are-legacy-guidance).

For the labels printed beside the main menus, use the
[menu-category label map](#which-shortcut-labels-are-printed-for-the-main-menus).

## How to perform the common actions

These instructions concern historical **selected 2.3.1g**. The mouse route has
limited retained playback evidence; the shortcut list below is legacy guidance.

1. **Inspect a soldier.** Hover over it to read health, rifle, experience and morale. A visible panel does not mean the soldier can act. Stat-panel evidence (local research)

2. **Move ordinary infantry.** Click the soldier, then a destination. Check actual movement after the marker appears; pinning, aiming, morale or an earlier pending choice can interfere. Movement evidence (local research)

3. **Equip or train a soldier.** Select the offer, then click an eligible recipient where required. Check the resulting equipment; a pending choice may take priority over movement. [Equipment](training-and-equipment.md)

4. **Give a command.** Follow that command's recipient or enemy-target step. Hold Fire and Concentrate Fire have different recipients and eligibility. [Orders](orders.md)

5. **Place a defense.** Select construction, then complete its placement requirements. The menu choice alone does not finish the structure. [Construction](construction.md)

6. **Leave the battle.** Distinguish withdrawing a soldier from menu retreat. The inspected menu-retreat script requests mission end without a confirmation check. [Withdrawal and mission end](withdrawal-and-mission-end.md)

If a soldier will not fire, use the [nonfiring checklist](why-soldiers-stop-shooting.md).
If it will not move, use the [movement checks](#why-is-a-selected-soldier-not-moving)
before treating the marker as proof of travel.

| Displayed stat | Keep this distinction in mind                                                          |
| -------------- | -------------------------------------------------------------------------------------- |
| Health         | Positive, at least 10 and full health are different thresholds in several source paths |
| Rifle          | A state used by weapon-specific comparisons, not a universal hit percentage            |
| Experience     | Can affect particular gates/counters; does not always invoke promotion                 |
| Morale         | Used by separate pin, fear, retreat, combat and aid paths                              |

## Menus select different kinds of actions

Reinforcement offers, pending equipment/orders, target commands, construction
placement and radio calls are not one interaction type. A successful menu scan
can be followed by another recipient, click, affordability or state check.
[Recruitment](recruitment.md), [orders](orders.md), [equipment](training-and-equipment.md),
[construction](construction.md), [radio](support.md)

These pages describe selected historical 2.3.1g; pending selection and the later
recipient/target/placement step remain distinct where required.

## Which shortcut labels are printed for the main menus?

The selected **2.3.1g menu tooltips** show these six labels. They identify the
source-advertised categories; this is not a claim that pressing each key works
in the selected host. Use the [menu map](menu-reference.md) to find each category and its offer guide;
printed shortcuts can be reused in different menus.

| Printed main-menu label | Menu or action named by the tooltip                                              |
| ----------------------- | -------------------------------------------------------------------------------- |
| 1                       | [Reinforcements](recruitment.md), with a separate airborne-reinforcement context |
| 2                       | [Commands](orders.md)                                                            |
| 3                       | [Logistics and equipment](training-and-equipment.md)                             |
| 4                       | [Radio support](support.md)                                                      |
| 5                       | [Construction](construction.md)                                                  |
| 6                       | Toggle sound                                                                     |

The Reinforcements entry's **20-TP advertised amount applies to airborne mode
99**, rather than a general charge for opening the ordinary reinforcement menu.
Availability, payment and any later recipient step remain separate.
[Exact main-menu labels and price context](menu-reference.md#main-menu).

The retained keyboard qualification is still **unsupported for gameplay-fact
extraction**. Tooltip labels do not resolve that gap or qualify a working
category-then-item sequence, focus behavior or parity with mouse input.
[Keyboard evidence and limits](evidence-and-method.md#controls-and-specialist-evidence),
retained qualification (local research).

## Keyboard instructions are legacy guidance

The archived community guide lists these shortcuts. **They have not all been
qualified in the selected binary and current host**; focus and player behavior
can matter. [What the retained controls evidence supports](evidence-and-method.md#controls-and-specialist-evidence)

| Legacy input                | Reported action                                                   |
| --------------------------- | ----------------------------------------------------------------- |
| Space                       | Pause                                                             |
| Ctrl                        | Return from a submenu                                             |
| Category key, then item key | Choose a menu command; individual bindings are not qualified here |
| Shift                       | Hide menus                                                        |
| Tab, then Enter             | Reach and activate an obscured object                             |

Pausing, a numeric timer and an animation/callback visit are also different
mechanisms. Do not convert every source counter into seconds from one nominal
frame rate or assume every unrelated callback has the same pause guard.
[Shot/recovery stages](how-shooting-works.md), [explosive timing](explosives.md)

Treat menu retreat as a different action from withdrawing one unit: the selected
menu script has a direct flush/gameover path without a confirmation predicate.
[Withdrawal and mission end](withdrawal-and-mission-end.md)

Sources: Source identities (local research).
Version and exact evidence (local research)

[Off-field protection state](protection-flag.md) is based on selected raw actor
fields and caller guards. The source boundary tests are not a certified visible
movement rectangle or safe zone.

Protection detail source: Source identities (local research)

## A destination marker is an order, not arrival

The selected ordinary soldier's button processes pending equipment/orders before
ordinary movement selection. Its normal selection needs health above 9. The later
world mouse-release handler writes destination fields and places a marker; it
does not teleport the soldier, clear aiming or guarantee the firing animation
ended. Exact event order still needs playback qualification.

The ordinary soldier's later normal movement route needs unpaused living state,
positive morale, no withdrawal, no active wire delay, aiming 0 and hth 0. A marker
can therefore coexist with a destination the actor has not yet acted on. Other
roles and retreat/withdrawal paths have different readers.

That route considers the destination close enough when **both axis differences
are at most 3**, rather than testing a circular three-unit radius. Its step uses
current facing before a possible later rotation update, so a new destination
does not promise an immediate straight line. The obstacle-test operands and
written-position operands also have opposite signs in this selected body;
actual collision/route behavior remains unqualified.
Exact press/selection/destination/movement stages (local research).
Additional source: Source identities (local research)

## Why is a selected soldier not moving?

For **selected 2.3.1g ordinary infantry**, check the stages in this order.
These source checks explain possible reasons, rather than certify a newly
tested click sequence or a guaranteed way to restart movement.

1. **Did the click apply an earlier choice?** Pending equipment or orders can take the recipient click before ordinary movement selection. Inspect what changed on the soldier.

2. **Was there only a hover panel?** Hover and selection use different tests. A stat panel alone does not prove movement focus was set.

3. **Can the ordinary actor enter normal movement?** The cited route needs unpaused living state, health at least 10, positive morale and no withdrawal flag. Wounded and retreat routes differ.

4. **Is wire, aiming or melee still involved?** A numeric wire counter of at least 1 takes its decrement alternative; normal movement also needs aiming and hand-to-hand state zero. A destination marker does not clear them.

5. **Is the target already close enough for this test?** Both axis differences at most 3 fail the normal further-step condition. This is not a circular three-unit radius or calibrated screen distance.

6. **Is this a vehicle or placed weapon?** Use the separate crew/health/input readers below. Ordinary infantry rules do not promise a waypoint step from an AA or static .50 parent.

Selection and movement evidence (local research),
hover versus focus (local research),
vehicle input/readers (local research)

The cited normal movement subsection has no direct extra pinning predicate.
That does not prove a pinned soldier always moves: aiming, animation and callback
state still matter. The selected **withdrawal** alternative does test pinning
before its retreat step, and does not repeat several normal-movement tests.
Keep those routes separate. [Withdrawal comparison](withdrawal-and-mission-end.md#ordinary-withdrawal-has-a-different-movement-guard)

Facing and obstacle tests also remain separate from assigning the destination.
The retained operand differences do not certify a path around an obstacle or
an immediate straight line to the marker. Use the detailed stages above when
the simple checks do not explain the observed behavior.

## Vehicle clicks use different crew and health gates

The Jeep's selected new selection needs driver 1, but its later parent movement
route does not repeat that driver check for an existing destination. Sherman
uses a health-gated selection after its pending .50-upgrade alternative, and its
selected parent movement also has no local crew-role gate. Those source
differences do not certify a live crewless-driving outcome.

M3 AT selection uses positive health; actual movement needs aiming 0 and at least
one of driver/gunner, plus its other guards. AA and static .50 instead load
driver 0 with gunner 1 and use a driver 1 selection test, while their inspected
parent routes have no normal waypoint position step. Their gunner-gated firing
is a different mechanism.
Exact five-handler and later-reader comparison (local research).
Additional source: Source identities (local research)

The Halftrack's positive-health selection also has no local crew-role check.
Its later moving field can change for sound state even when the obstacle query
blocked that step, so a destination marker or moving value is not an arrival/
displacement receipt. Halftrack source distinction (local research).
Additional source: Source identities (local research)

## Hovering for stats is separate from selecting a unit

The selected hover handlers copy current stat fields into the shared info panel
under their own guards. AA with gunner 1/driver 0 can pass its hover test while its
selected movement-focus click needs driver 1. The ordinary hover has no local
health gate even though normal selection requires health above 9; actual frame
and input availability still matter. Seeing a stat panel therefore does not
certify readiness, movement or a successful equipment receipt.

The ordinary handler copies values at that event rather than installing a live
actor-stat observer in its body. Actual refresh and displayed text need playback
qualification. The Jeep also copies its gun component's rifle, which differs
from the hull rifle read by its inspected firearm. Exact hover and receiver comparison (local research).
Additional source: Source identities (local research)

## Supporting local research

The practical explanations above are self-contained. The following exact research
references are intentionally excluded from this published edition; their labels
identify retained evidence, not additional pages you need to play. Read the
[published evidence and study scope](evidence-and-method.md) or [edition guide](editions.md).

- [Control evidence](../player-interaction-evidence.md#crates-and-controls)
- [Stat-panel evidence](../player-hover-stat-evidence.md)
- [Movement evidence](../player-movement-input-evidence.md)
- [retained qualification](../../content/keyboard_qualification.json)
- [Source identities](../player-notes/controls.md#citation-1)
- [Version and exact evidence](../player-interaction-evidence.md)
- [Source identities](../player-notes/controls.md#citation-2)
- [Exact press/selection/destination/movement stages](../player-movement-input-evidence.md)
- [Source identities](../player-notes/controls.md#citation-3)
- [Selection and movement evidence](../player-movement-input-evidence.md)
- [hover versus focus](../player-hover-stat-evidence.md)
- [vehicle input/readers](../player-vehicle-movement-evidence.md)
- [Exact five-handler and later-reader comparison](../player-vehicle-movement-evidence.md)
- [Source identities](../player-notes/controls.md#citation-4)
- [Halftrack source distinction](../player-vehicle-movement-evidence.md#halftrack-focus-uses-health-and-moving-is-also-a-sound-state-field)
- [Source identities](../player-notes/controls.md#citation-5)
- [Exact hover and receiver comparison](../player-hover-stat-evidence.md)
- [Source identities](../player-notes/controls.md#citation-6)
