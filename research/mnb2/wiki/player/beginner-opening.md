[Player reference](README.md) · [Starting checklist](starting-checklist.md) · [Purchase budgets](purchase-budgets.md)

# Practice one purchase before planning a full opening

**Edition: historical selected 2.3.1g.** This short opening was exercised on November 11, 2026 in the identified original binary: inspect, move, buy one Garand, then deliberately end the mission. It teaches a transaction and results reading, not a survival strategy or optimal formation.

## Observed worked opening

The recorded run used a new browser context with no saved cookies or origins,
ordinary default deployment, four starting soldiers and displayed **0 TP**.
The original selected binary had SHA-256
`1e066cc28219fc68ba7a52604c6740d5f21d98332dbbe2466c45cc39c67a250a`,
with the retained Ruffle runtime and Edge 157.0.4341.46. One run is evidence of
these interactions, not qualification of every browser or profile.

| Action in this run                               | Visible result and cost                                                                             | Why or when to change course                                                                                          |
| ------------------------------------------------ | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| Inspect/select R. Ryker near stage (15,550)      | Health 100, rifle 18, XP 0, morale 22; spend 0 TP                                                        | Inspect your actual squad; these are not guaranteed starting rolls                                                    |
| Order this soldier to (65,350)                   | Soldier travels there; spend 0 TP                                                                    | Move one unit to learn the order; this is an observed destination, not certified safe cover                           |
| Wait until wave 1 shows 2 TP                       | Garand can be afforded                                                                              | Use actual income; do not force this schedule with Taunt                                                              |
| Open Logistics, select the named M1 Garand offer | Tooltip says 2 TP; balance changes 2→0 within the same wave; rifle cursor and recipient prompt appear | Read the tooltip, not a guessed submenu row number                                                                    |
| Click the healthy moved soldier                  | Recipient prompt is consumed; spend no second purchase                                              | The panel does not independently expose the exact weapon field; use the equipment guide if the choice remains pending |
| Open Commands and choose Retreat to Main Menu    | Mission ends at the score/results screen                                                            | This intentionally ends the exercise, rather than trying to survive longer                                            |

For this 400×600 reference stage, Logistics and its Garand offer were at about
(15,113); Commands was at (15,88), and Retreat at **(15,306)**. Scaled windows
and other releases can differ: match the named tooltip instead of copying pixels.
Earlier attempts clicked the wrong menus or All-around Defence; they did not
end the mission. Printed shortcut 6 did not mean the sixth submenu row.

The final display showed **score 12**, shots fired 8, enemies killed 1, soldiers
lost 4/deployed 4 and ground gained 0. It printed “Germans overran your position”
even though the observed trigger was deliberate menu retreat. Some statistics
were NaN, so neither those fields nor its displayed mission time certify elapsed
time or combat performance. No durable save, natural-loss condition or surviving
formation was tested. Original screenshots remain local research; the admitted
pictures are [original conceptual diagrams](instructional-visuals.md).

## Set up the exercise

Use default deployment, with no assumed career gifts, free purchases or saved
TP. Inspect the actual squad: the selected base setup requests four Regular
Soldiers and starts from 0 base TP before later changes. If your profile supplies
different equipment or resources, record that difference rather than treating
it as this exercise's starting condition. [Modes and base squad](deployments.md).

The practice purchase is a **2-TP Garand for an existing eligible ordinary
soldier**. A fresh recruit is a separate **3-TP** purchase, so adding both would
need **5 TP** under normal paid conditions. Check who already has a Garand first.
[Regular Soldier](regular-soldier.md), [purchase arithmetic](purchase-budgets.md#equipping-an-ordinary-recruit).

## Work through the sequence

| Step | Action and cost                                                                     | Expected result                                  | If conditions change                                                                        |
| ---- | ----------------------------------------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------------- |
| 1    | Inspect each starting ordinary soldier; spend 0 TP                                  | Compare health, rifle, morale and current weapon | Do not assume all four starts are identical                                                 |
| 2    | Move one soldier a short distance on clear ground; spend 0 TP                       | Selection feedback, marker, then actual movement | If stuck, use [movement checks](controls.md#why-is-a-selected-soldier-not-moving)           |
| 3    | Keep observing until the displayed balance can cover 2 TP                           | The upgrade is affordable now                    | Do not force income with Taunt just to meet this exercise; it can request enemies           |
| 4    | Select the Garand offer, then click one eligible ordinary soldier; normal cost 2 TP | That soldier receives the weapon                 | Avoid an already-equipped recipient or an unfinished earlier equipment choice               |
| 5    | Observe the unit fighting; spend 0 TP                                               | Distinguish aiming, shots and actual damage      | If it stops firing, check [health, orders and targets](why-soldiers-stop-shooting.md) first |

For step 4, the ordinary equipment recipient needs more than 9 health.
Garand is a weapon replacement, not Ranger Training or a promise to refill every
magazine. [Garand limits](m1-garand.md), [purchase versus refill](weapon-comparison.md#does-buying-or-rebuying-a-weapon-refill-ammunition).

## Position and adapt deliberately

Use the [battlefield and failed-order diagrams](instructional-visuals.md) to
identify the line, movement order and threats. The teaching choice is to move
one unit first and keep the rest available while you learn; it is tactical
judgment, not a tested formation. No pixel coordinates or safe blast spacing are
recommended without a matching observed placement.

If infantry fire is the problem, compare [cover and specialist limits](defenses.md).
If armor appears, stop treating a rifle upgrade as a complete answer and compare
[anti-tank jobs and commitments](anti-tank-options.md). If the enemy is getting
through, inspect the [breakthrough warning](breakthroughs.md). Do not continue
this purchase merely because it is next in the table.

## End, read and repeat

At a natural mission end, or after deliberately using the mission-ending retreat
action, read [score and career points](score-and-career-points.md). Write down
your build/profile, starting squad and TP, the actual purchase, any failed order,
and how the mission ended. The results screen alone does not certify saving.

The worked run above validates this bounded interaction sequence. It does not measure hit rates, natural campaign survival or reliable saving. Repeat the [starting checklist](starting-checklist.md) for controls and [budgets](purchase-budgets.md) for arithmetic; change one decision at a time.
