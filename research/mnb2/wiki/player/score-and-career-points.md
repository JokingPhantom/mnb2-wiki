[Player reference](README.md) · [Progression](progression.md) · [Medals and ranks](career-medals-and-ranks.md)

# Mission score, career points and carried TP

**Mission score, career rank, a soldier's XP and leftover TP are different
quantities.** The selected 2.3.1g results action copies some counters for display,
adds others to career fields and uses a guarded score expression for career
points. A results screen is not, by itself, a verified save receipt.
[Exact result-accounting source](../mission-result-accounting.md)

On this page: [Which number am I trying to improve?](#which-number-am-i-trying-to-improve) · [What enters the selected mission score?](#what-enters-the-selected-mission-score) · [Score does not always add the same career points](#score-does-not-always-add-the-same-career-points) · [Promotion checks happen separately and in order](#promotion-checks-happen-separately-and-in-order) · [Proper Planning carryover is not every TP you ended with](#proper-planning-carryover-is-not-every-tp-you-ended-with) · [A flush call is not the whole persistence result](#a-flush-call-is-not-the-whole-persistence-result) · [A death helper, kill write and fading are different stages](#a-death-helper-kill-write-and-fading-are-different-stages) · [The score bonus is applied before the point-addition limit](#the-score-bonus-is-applied-before-the-point-addition-limit) · [A lower displayed accuracy need not mean a lower score](#a-lower-displayed-accuracy-need-not-mean-a-lower-score)

## Which number am I trying to improve?

- **Mission score.** Combines hit, kill, local-wave and recovered-crate counters, with a separate conditional bonus; it is not total health damage.
- **Career points.** A guarded addition derived from the resulting score; career promotion has later rank/point and award-order checks.
- **One soldier's XP/rank.** That actor's separate progression, not the same value as the mission's career-point award. [Soldier progression](progression.md).
- **Leftover TP.** A separate stored balance for Proper Planning; the selected result copy has an upper clamp of 20, not a promise of the next start's final TP.

These distinctions and the formulas below come from the
[selected 2.3.1g result action](../mission-result-accounting.md). Before comparing
two scores or following an old progression guide, check which counters and
deployment it assumes. A high number alone does not prove promotion, persistent
saving or a more effective combat strategy.

## What enters the selected mission score?

Its base expression is:

**hits + 5×kills + 5×local wave + 10×recovered crates**

The kills value is copied from the mission kill counter earlier in that action.
Hits are counter values, not total health damage. Crew, AT, zero-damage and
recipient checks matter before treating the displayed numbers as a census of
distinct victims. [Shot/hit counters](../shot-hit-statistics.md),
[AT counting](anti-tank-and-vehicles.md#an-at-kill-counter-write-is-not-always-a-removed-tank)

A source domain comparison for mudandblood.net then adds one tenth of that
score. This is a conditional selected-source branch, not a claim about current
hosting, another binary or a live score submission.

For supplied hits 10, kills 2, local wave 3 and crates 1, the base expression gives 45.
If that domain branch applies, it becomes 49.5. These are declared arithmetic
inputs at the reader, not an observed mission or a tested scoring strategy.

## Score does not always add the same career points

The cited point addition requires the resulting score to be **strictly below
50,000**, then adds **score/3** to stored career points. Exactly 50,000 does not
pass that particular predicate. No explicit rounding appears at that addition.
In the supplied 49.5 example, it would add 16.5 if the remaining execution/context
assumptions hold. It does not change one soldier's XP to that number.
[Exact formula and limit](../mission-result-accounting.md#score-and-career-points-are-separate-expressions)

A separate career-wave addition uses the current **local wave**, rather than
mission-total wave at that site. Other career fields add kills, incoming V1s,
deployed units and gained ground from their own mission counters. They are not
all the same value as the score or a single campaign-progress meter.
[Wave-counter distinction](waves.md)

## Promotion checks happen separately and in order

Career promotion tests use strict point comparisons and the stored career rank.
First Lieutenant needs points above 3,000 in its cited branch; Captain above 6,000.
An outer award-display gate and earlier eligible medal/badge branches can take
precedence before those tests. Display target numbers do not replace the source
comparisons. [Career rank source](../career-ranks.md)

For a supplied rank 1/points 7,000/display-ready state with no earlier award branch
eligible, one entered promotion chain takes rank 2, not rank 3. A separately reached
later chain with those other conditions unchanged can then take rank 3. These
are branch-state examples, not a promise of immediate calls or promotions per
second. Reached promotion branches also add to an Airborne attempt allowance;
starting that challenge and earning its badge are separate paths.
[Deployment entry and allowances](deployments.md)

## Proper Planning carryover is not every TP you ended with

The result action copies current TP into the leftover field, then clamps values
**above 20 to 20** at that site:

| Supplied TP at this copy | Leftover after the selected upper clamp      |
| ------------------------ | -------------------------------------------- |
| 12                       | 12                                           |
| 25                       | 20                                           |
| -3                       | -3 at these writes; no local zero-floor test |

Those are source-write examples, not a promise of the next mission's final
balance. Proper Planning later adds the stored leftover to its current balance
and clears the stored field; deployment gifts and other initialization writes
remain separate. [Proper Planning source order](../player-deployment-entry-evidence.md#base-resource-writes-preserve-their-order-and-inputs),
[TP rules](tactical-points.md)

## A flush call is not the whole persistence result

The selected results action requests a profile flush **before** the compared
career/leftover additions. That order does not prove the later updates are lost,
already durable, automatically flushed or saved exactly once. Other writes,
flush calls, host storage and actual save/reload observations remain necessary.
No profile was modified or reset for this explanation.
[Flush order and limits](../mission-result-accounting.md#the-selected-flush-call-precedes-aggregation),
[withdrawal and mission end](withdrawal-and-mission-end.md)

Sources: [Source identities](../player-notes/score-and-career-points.md#citation-1).
Original synthesis of linked exact notes; no new score, rank, storage or game trial.

## A death helper, kill write and fading are different stages

For the selected Regular enemy, enemyDeathRoutine gates its dropped-weapon/dead
marker work on dead equal to 0 and sets that marker to 1. The mission kill increment instead
appears in the actor's separate death action; that action has no local dead-marker
test. The later placed-controller corpse branch decrements a life counter and
fades below 100. A dropped gun or fading sprite is therefore not one universal
kill, equipment-pickup or elapsed-lifetime receipt.

The corpse branch also sits outside that controller's living pause guard.
This is a source distinction, not a reproduced duplicate-kill or paused-fade
bug, nor a promise of what every enemy family does.
[Exact Regular caller, marker, counter and fade scope](../player-enemy-death-stages-evidence.md).
Additional source: [Source identities](../player-notes/score-and-career-points.md#citation-2)

## The score bonus is applied before the point-addition limit

The selected one-tenth domain bonus is added before the strict 50000 guard for
career-point addition. With a supplied integer base score 45454 and that branch
true, the guard sees 49999.4 and admits the addition. Base 45455 instead becomes
50000.5 and skips that particular addition; without the bonus, both bases pass.

This is a conditional source boundary, not a live-host comparison or an observed
loss of stored career points. Skipping this one addition does not itself reset
existing points, and actual result entry, other writes and storage still matter.
[Exact order, five supplied bases and boundary](../mission-result-accounting.md#the-domain-score-addition-precedes-the-career-point-threshold).

## A lower displayed accuracy need not mean a lower score

The inspected enemy rocket soldier's own firing action writes the same **shot**
counter used in the results accuracy denominator. That statement does not add a
hit or an enemy-shot counter in its own body. With all other supplied totals
fixed at 5 hits/10 shots, one such reached counter update makes the later ratio
5/11, or 45.45%, instead of 50%.

The selected base-score expression has no shot-count term, so changing only that
denominator does not change its hit/kill/wave/crate score. Actual rocket effects,
callback entry and later counters remain separate. This is a source-reader
example, not a newly observed mission or a claim every enemy rocket causes an
accuracy loss.
[Exact writer, result readers and supplied arithmetic](../shot-hit-statistics.md#an-enemy-rocket-action-writes-the-results-shot-denominator).
