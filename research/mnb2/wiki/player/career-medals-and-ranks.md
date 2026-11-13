[Player reference](README.md) · [Progression](progression.md) · [Medals and ranks](career-medals-and-ranks.md)

# Career medals and rank requirements

Career medals and ribbons use specific recorded counters and unlock conditions. Check the conditions below alongside your current profile and award entry: several old descriptions give different numbers. These historical **2.3.1g** tables do not prove that a counter, display or benefit has been saved. [Exact source, ordered checker and boundaries](../player-career-award-evidence.md)

On this page: [Why has a milestone not produced the expected reward?](#why-has-a-milestone-not-produced-the-expected-reward) · [Named field-action benefits](#named-field-action-benefits) · [Mission and wave milestones](#mission-and-wave-milestones) · [Career activity counters](#career-activity-counters) · [Career efficiency conditions](#career-efficiency-conditions) · [Calendar and separate event awards](#calendar-and-separate-event-awards) · [Why an eligible medal or rank can wait](#why-an-eligible-medal-or-rank-can-wait) · [Career rank reads points, not a soldier's XP](#career-rank-reads-points-not-a-soldiers-xp) · [Check the reward's actual reader](#check-the-rewards-actual-reader) · [Manoeuvre's TP bonus is not its award condition](#manoeuvres-tp-bonus-is-not-its-award-condition)

## Why has a milestone not produced the expected reward?

Check four separate stages before interpreting a threshold as a missing medal:

1. **Eligibility:** use the actual counter, comparison and other conditions in
   the tables below. The award's stored flag must still be unset.
2. **Award processing:** central awards share a display-frame gate and an ordered
   chain. Several eligible awards need not all be granted on one check.
3. **Benefit:** an earned flag affects particular later consumers. Its description
   alone does not apply a universal bonus or remove every payment/recipient gate.
4. **Persistence:** meeting a source test or seeing a result does not by itself
   qualify a durable saved profile.

These are **selected original 2.3.1g** boundaries from the
[ordered award evidence](../player-career-award-evidence.md).
For the practical benefit, follow [recruit stat bonuses](career-stat-bonuses.md),
[support and economy awards](support-and-economy-awards.md), or
[deployment gifts](deployment-gifts.md). For a new starting mode, use
[deployment entry ranks](deployments.md#compare-entry-rank-and-starting-resources).

Looking for a free upgrade or recruit after earning an award? Use
[fee waivers, free allowances and refunds](free-orders-and-refunds.md) to
separate the award's grant, the offer's admission and the later spending or
refund stage. Earning a flag does not by itself prove a delivered effect.

Counter names below identify the selected reader; they do not certify that many
distinct kills, aircraft or arrivals. Soldier XP and soldier rank are separate
from career points/rank. [Progression overview](progression.md).

## Named field-action benefits

An award's condition and the action that uses its earned flag are different
checks. Two selected benefits are useful to read alongside the requirements:

- **Gallantry Medal.** Flag exactly 1 enables a group-index +1 XP loop inside the Medic's exact-health rescue branch. It is not another point only to the current patient or proof every actual soldier gains XP/rank.
- **Infantry Specialist Ribbon.** Flag exactly 1 overwrites the positive-target Concentrate Fire counter from 60 to 30. It is not a measured 30-second interval or confirmation that a recipient fired.

Read the [Medic rescue/XP distinction](medic.md#rescues-and-experience-use-different-tests)
and [retargeting order benefit](retargeting-orders.md) before treating either
label as a universal upgrade. Exact identity and consumers:
[award catalog](../award-reference.md), [Medic bonus loop](../medic-healing.md#a-post-addition-value-11-triggers-the-rescue-branch),
[Concentrate Fire counter](../concentrate-fire.md#cooldown-writes-depend-on-the-selected-target).
Sources: [Source identities](../player-notes/career-medals-and-ranks.md#citation-1). No new award or action trial is implied.

## Mission and wave milestones

| Award                  | Selected condition, before its other entry/priority guards         |
| ---------------------- | ------------------------------------------------------------------ |
| Bronze Star            | Local wave ≥40                                                     |
| Silver Star            | Local wave ≥80                                                     |
| Gold Star              | Local wave ≥120                                                    |
| Combat Ribbon          | Mission stats.kills ≥100                                           |
| Medal of Honor         | Mission stats.kills ≥200                                           |
| Manoeuvre Ribbon       | Mission casualties exactly 0 and timer2 ≥600                       |
| Survival Ribbon        | Mission casualties exactly 0 and mission-total wave >100           |
| Guerilla warfare Award | buildingCalled+vehicleCalled exactly 0 and mission-total wave >100 |

## Career activity counters

| Award                        | Selected condition, before its other entry/priority guards |
| ---------------------------- | ---------------------------------------------------------- |
| War Effort Ribbon            | Deployment counter soldierdeployed ≥100                    |
| Gallantry Medal              | Saved-soldier counter soldiersaved ≥25                     |
| Distinguished Service Ribbon | Games counter ≥100                                         |
| Meritous Service Ribbon      | Games counter ≥500                                         |
| Legion of Merit              | Games counter ≥1,000                                       |
| Sapper commendation          | Construction counter ≥100                                  |
| Air Medal                    | airstrike counter ≥100                                     |
| Westpoint Commendation       | promoted counter ≥5                                        |
| Special Operations Ribbon    | highspeed counter ≥100                                     |
| Logistics Ribbon             | Career craterecovered ≥50                                  |
| Tank Killer Ribbon           | tankkilled counter ≥10                                     |
| BBQ Medal                    | bbq counter ≥50                                            |
| Air Command                  | airkill counter ≥50                                        |
| Ground Controller Ribbon     | artykill counter ≥50                                       |
| Urb's Anatomy Ribbon         | gib counter ≥100                                           |
| Kyoto Ribbon                 | treekilled counter ≥100                                    |
| Chain of Command Ribbon      | sitrep counter ≥100                                        |
| Shellshock Ribbon            | artyreceived counter ≥1,000                                |
| Legion d'Honneur             | frenchPromoted counter ≥1                                  |
| Search and Rescue Ribbon     | pilotrecovered counter ≥100                                |
| Air defence Ribbon           | planeKill counter ≥100                                     |
| Veterancy Ribbon             | bosswaved counter ≥100                                     |
| Son of London Ribbon         | v1 counter >2,419                                          |
| Close combat Ribbon          | hthKill counter >100                                       |
| Halloween Ribbon             | zombieKill counter >20                                     |
| Forward observer Ribbon      | antiArty counter >25                                       |
| Interdiction Ribbon          | boobyKill counter >25                                      |
| Field Commander Award        | bonusTP counter >1,000                                     |

## Career efficiency conditions

| Award                         | Selected condition, before its other entry/priority guards |
| ----------------------------- | ---------------------------------------------------------- |
| Assault Expert Award          | Games >10 and career killed/games >49                      |
| Defence Expert Award          | Games >10 and career wave/games >49                        |
| Meritorious Unit Commendation | Career wave ≥1,000 and games <26                           |
| Mud and Blood Cross           | Career wave ≥5,000 and games <51                           |
| Infantry Specialist Ribbon    | Career deployed <1,000 and games >50                       |
| Victoria Cross                | Career deployed <2,500, games <101 and career wave ≥10,000 |

## Calendar and separate event awards

| Award                   | Selected condition, before its other entry/priority guards                 |
| ----------------------- | -------------------------------------------------------------------------- |
| Xmas Ribbon             | xmasKillz exactly 1                                                        |
| MNB2 anniversary ribbon | Month 7/day ≥8 OR month 8/day ≤8; mission-total wave >100                  |
| D-DAY Ribbon            | Month 5/day 6; mission-total wave >100                                     |
| Ribbon of Unfairness    | Post-event-increment unfair counter >1,000, inside its separate event path |
| I love pie ribbon       | Separate qualifying crate collector/rare draw, pie not 1; see below        |
| Remembrance day ribbon  | Month 10/day 11; mission-total wave ≥100                                   |

The calendar rows retain zero-based month numbers: month 5 is June, 7 is August,
8 is September and 10 is November. Their tests read a date object, with unknown
refresh/caller timing here. Xmas's listed condition reads its special counter,
not a calendar test at that award site. This guide does not establish that an
award will appear after a wall-clock date changes.

**Ribbon of Unfairness and Pie use separate owner paths.** The former checks
its counter after an admitted unfair event increments it. Pie's crate path
needs a defined-health-at-least-10 collector strictly within 50, one specific
passing value from random(10000), pie not 1 and the unset medal flag. That rare
comparison is separate from the ordinary crate-content selector. It is not a
certified probability per crate or a promise of one outcome for every pickup.

The accepted view has only initialized flags for medal slots 49/50, without
named award sites. They are not added as two more earned medals here.

## Why an eligible medal or rank can wait

The central checker admits its chain only when the medal display is at frame 1.
It considers named medals 1–45, then Remembrance 48, then the Airborne badge,
then career promotions. Only the first matching alternative runs in that call.
For declared local wave 120 with Bronze/Silver/Gold all unset and earlier
alternatives excluded, Bronze is chosen first. Separately admitted later calls
can choose Silver then Gold. No delay in seconds or automatic next call is
qualified by that source ordering.

The Airborne badge alternative uses mode 99, mission-total wave at least 100 and
its own unset airborne flag. It is separate from a named medal and precedes the
career-rank ladder. [Airborne mode](deployments.md).

## Career rank reads points, not a soldier's XP

With earlier central alternatives excluded, these promotions use strict
**career points greater than** the listed number and current rank below the
new rank. Equality does not pass that comparison.

| New career rank       | Points must be greater than |
| --------------------- | --------------------------- |
| First Lieutenant      | 3,000                       |
| Captain               | 6,000                       |
| Major                 | 12,000                      |
| Lt. Colonel           | 24,000                      |
| Colonel               | 48,000                      |
| Brigadier General     | 100,000                     |
| Major General         | 200,000                     |
| Lieutenant General    | 400,000                     |
| General               | 800,000                     |
| Mud and Blood General | 2,000,000                   |

A supplied low rank with enough points for several promotions still takes the
first eligible rung at one admitted check, rather than jumping to the highest.
This is a different ladder from [soldier promotion](progression.md), which reads
actor XP and rank. Actual display timing, unlock entry and durable profile
storage remain separate.

## Check the reward's actual reader

[Career stat bonuses](career-stat-bonuses.md),
[support/economy awards](support-and-economy-awards.md),
[deployment gifts](deployment-gifts.md) and
[free-order allowances](ranger-training.md) explain selected consumers.
A medal description alone does not add a weapon modifier or override a payment,
mode, recipient or callback guard. The [progression overview](progression.md)
compares description/source mismatches and distinct counters.

Source: [Source identities](../player-notes/career-medals-and-ranks.md#citation-2). Later original coverage remains a
candidate; accepted pilot cards retain their acceptance.

## Manoeuvre's TP bonus is not its award condition

The Ribbon's source award test needs a casualty-free mission and timer2 at
least 600, plus its own unset flag and checker admission. A separate TP consumer
instead increments that counter, then needs the Ribbon flag already 1 and the
new value **exactly 600** with zero casualties to add 1 TP. Supplying 599 before
that admitted update can pass; supplying 600 produces 601 and does not.

The selected reward block does not reset the counter or award again at 1200.
With initialization 0 and only these admitted +1 updates supplied, it is a
single equality opportunity, not recurring income every 600 units. Whether the
first-ever award arrives before that particular consumer still needs actual
execution-order evidence. The source's five-minute message is not a measured
conversion of those counter units into seconds.
[Exact writers, caller, inputs and TP limits](../player-career-award-evidence.md#manoeuvre-eligibility-and-its-tp-reward-have-different-timer-tests).

For **Special Operations Ribbon**, the supported direct Sniper and Spec Ops
mouse offers both increment highspeed; Resistance's Spec Ops substitution omits
that increment in its own offer body. A requested specialist template is not
one universal counter receipt. [Exact named producers](../player-special-deployment-evidence.md).
Additional source: [Source identities](../player-notes/career-medals-and-ranks.md#citation-3)

For **Logistics Ribbon**, a supplied earned flag doubles the selected crate
request comparison from 1/300 to 2/300. Those are per-reached-action integer-input
counts; unresolved template lookup, falling/ground stages and later collection
prevent treating them as measured arrival or reward rates.
[Exact Logistics consumer and delivery boundaries](../player-crate-delivery-evidence.md).
Additional source: [Source identities](../player-notes/career-medals-and-ranks.md#citation-4)

For **Ribbon of Unfairness**, the admitted source body has two counter additions
with the award test between them. Its selected TP reward has two nested exact
1-of-100 tests plus a balance guard. Counter totals, distinct attacks survived,
award entry and reward frequency must therefore be read separately.
[Exact source order and declared counts](unfair-attacks.md).
Additional source: [Source identities](../player-notes/career-medals-and-ranks.md#citation-5)

[Original opening and evidence context](../player-notes/career-medals-and-ranks.md#opening-before-player-language-correction).
