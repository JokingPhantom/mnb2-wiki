[Player reference](README.md) · [Support](support.md) · [Tactical points](tactical-points.md)

# Situation report

A **1-TP request** with a separate conditional 5-TP reward. A report can be
charged and counted without awarding TP, and 5 is the reward addition before
its cap—not an unconditional net gain.
[Report source comparison](../situation-report.md)

Historical scope: selected **2.3.1g** source.

| Key fact               | Selected historical behavior                                    |
| ---------------------- | --------------------------------------------------------------- |
| Advertised cost/access | 1 TP; Signaller request with its own offer/acceptance guards    |
| Accepted branch        | Charges 1 TP, adds Signaller XP and report count                |
| Cash reward            | Separate 9-of-100 comparison can add 5 TP before the reward cap |
| Budgeting limit        | Reward is not guaranteed net income                             |

On this page: [Charge, reward and cap happen in order](#charge-reward-and-cap-happen-in-order) · [The advertised reward is not expected TP income](#the-advertised-reward-is-not-expected-tp-income)

## Charge, reward and cap happen in order

After the Signaller's outer completion roll and preceding-request checks, the
affordable report branch adds 1 experience, subtracts 1 TP and increments the career
report counter. Only a further random 0–99 roll **below 9** awards 5 TP.
The nested source gate is 9 of 100 draws, differing from an older guide's one-in-ten
claim. This is not a measured reward frequency per menu click or per second.
[Exact charge/reward order](../player-support-evidence.md#report-naval-and-counter)

The reward path uses a base TP limit of **20**, with these award terms:

| Award                  | Added to this limit for a stored flag of 1 |
| ---------------------- | ------------------------------------------ |
| Survival Ribbon        | +1                                         |
| Veterancy Ribbon       | +1                                         |
| Guerilla warfare Award | +3                                         |

With all three stored flags supplied as 1, this report limit is 25. The source
expression is 20 plus medal 36 plus medal 34 plus 3 times medal 39; the mapping
and actual stored values matter. This clamp belongs to the rewarded/excess
branch, rather than an always-on TP ceiling for every source of income.
[Named awards and exact expression](../player-support-award-evidence.md#names-map-to-specific-fields-and-guards)

For example, with cap 20 and no intervening writes, a completed rewarded report
starting at 19 goes 18 after the fee, 23 after the reward, then 20 after the cap: net +1,
not +4. Starting at 10 and taking the same branch ends 14: net +4. These are
conditional arithmetic illustrations, not observed transactions or permission
to ignore the request's other gates.

The legacy guide's post-2.3 cooldown warning remains version-qualified.
Interruption, menu cooldown, retry scheduling and persistence still need their
own paths; source XP and report counts are not proof of delivered cash.
[Signaller completion and cleanup](signaller.md)

Sources: [Source identities](../player-notes/situation-report.md#citation-1). Selected 2.3.1g;
[exact evidence and assumptions](../player-support-evidence.md).

## The advertised reward is not expected TP income

The conditional 5-TP reward should not be budgeted as reliable income. The
accepted report also has its separate Signaller XP and career-count writes;
those benefits do not guarantee a cash return or establish the best use of a call.
[Source calculation and limits](../situation-report.md#conditional-tp-expectation-after-an-affordable-report-was-accepted)

<details>
<summary>Detailed expected-TP calculation after affordable acceptance</summary>

With the affordable completion branch already reached, cap 20 and a uniform
integer reward input, the fee/reward writes average a local change of −0.55 TP
when the starting balance is 1 through 16. In that supplied uncapped range,
−1 TP fee + (9/100 × 5 TP reward) = −0.55 TP, averaged across the reward draw. Near that cap, the conditional mean
falls further: starting 19 gives −0.82, while 20 gives −0.91. The nine reward inputs
out of 100 are averaged with the 91 nonreward inputs; this is not a measured payout
per menu click or a full radio-call model.

The affordable branch separately adds 1 Signaller XP and one report count before
the reward test. Those benefits, progression and later state are not captured
by the TP average, so it does not establish the best use of a call.
[Exact supplied balances, cap behavior and expectation](../situation-report.md#conditional-tp-expectation-after-an-affordable-report-was-accepted).

</details>

Additional source: [Source identities](../player-notes/situation-report.md#citation-2)
