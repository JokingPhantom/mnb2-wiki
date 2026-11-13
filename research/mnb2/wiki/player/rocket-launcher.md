[Player reference](README.md) · [Vehicles and emplacements](vehicles-and-emplacements.md) ·
[Repair, crew or reload?](repair-crew-and-reload.md)

# Rocket launcher

A **20-TP placed launcher**, operated through its own selected fire/reload button.
It starts with a **loaded counter of 16**, uses a separate cooldown, and creates
impact effects at random coordinates. Its firing/effect chain differs from the Bazooka
soldier's moving rocket. [Exact selected 2.3.1g source](../player-rocket-evidence.md)

The health/maxhealth mismatch is retained. A field called maxhealth is not proof
that actual health never exceeds it. The rifle initializer also uses random
stopping, followed by Combat Ribbon's +3; it is not five fixed additions.
[Reading stats](reading-stats.md)

Applies to **historical selected 2.3.1g**. Starting health, crew and counters
are source load fields; they do not guarantee arrival or a complete attack.

| Key fact                     | Selected historical load                                      |
| ---------------------------- | ------------------------------------------------------------- |
| TP cost and availability     | 20 TP; placed launcher; an empty refill costs a separate 1 TP |
| Health                       | 300                                                           |
| Source maxhealth field       | 200; a different field from initial health                    |
| Armor class                  | 1                                                             |
| Driver / gunner / spare crew | 1 / 1 / 0                                                     |
| Experience / rank            | 0 / 0; Mud and Blood Cross adds 9 XP at its load branch       |
| Loaded counter / cooldown    | 16 / 0                                                        |

[Starting-field evidence](../player-rocket-evidence.md).

On this page: [Fire and refill are different button states](#fire-and-refill-are-different-button-states), [The selected impact pattern does not follow a designated enemy](#the-selected-impact-pattern-does-not-follow-a-designated-enemy).

## Fire and refill are different button states

Use the current loaded state, rather than treating every positive value as ready
or every button press as a refill:

| Loaded counter | Button result                               | Conditions and limits                                                                |
| -------------- | ------------------------------------------- | ------------------------------------------------------------------------------------ |
| Exactly 16     | Requests firing; writes cooldown 900 − 2×XP | Cooldown below 1, no bunker, gunner exactly 1 or driver exactly 1                    |
| Exactly 0      | Restores loaded 16; charges 1 TP            | Positive TP; does not repeat the firing crew/bunker/cooldown gates or clear cooldown |
| 1–15           | Busy branch                                 | No partial top-up                                                                    |

Refilling therefore does not, by itself, make the launcher ready to fire again.
These are conditions of the selected handler; counters are not measured seconds
and a firing request is not proof of all later impacts.
[Button and timer order](../player-rocket-evidence.md#the-launcher-button-chooses-fire-reload-or-busy)

Positive cooldown decreases in the selected unpaused callback. The popup's
numeric-seconds condition is unusual, so its momentarily text should not be
read as a precise countdown. Actual input/animation/pause delivery still matters.

## The selected impact pattern does not follow a designated enemy

The inspected impact writes choose **x=0–399 and y=0–299** with separate draws in the
effect parent's coordinates. They do not use a selected enemy or cursor point
for those positions. The source emits explosion effects through timeline actions;
it does not borrow the Bazooka rocket's proximity-sampling path.
[Impact evidence and limits](../player-rocket-evidence.md#impacts-are-sampled-coordinates-not-a-chosen-target)

The later effect supplies **AT radius 25, fragment radius 50 and damage input 200**,
with special tag **at**. Those are separate helper inputs, not guaranteed health
loss or 16 reliable kills. Scenery removal, friendly recipients, owner credit and
all later damage/geometry gates remain separate. [AT rules](anti-tank-and-vehicles.md)

A purchase pointer, firing request and decrementing loaded counter are different
stages. This source explanation does not certify exactly 16 completed impacts,
a full elapsed-time salvo or observed pause safety.

Sources: [Source identities](../player-notes/rocket-launcher.md#citation-1).
[Version and exact evidence](../player-rocket-evidence.md)
