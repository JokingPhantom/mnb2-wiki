[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Role comparison](recruitment.md#choose-the-job-before-the-price)

# Sarge

A **12-TP recruit** with **125 starting health, 30 experience and rank 3** in the
selected load, plus conditional support effects. The menu also checks a prior-deployment flag; support effects have their own
recipient conditions. [Sarge source](../sarge.md)

Applies to **historical selected 2.3.1g**. Starting facts use the ordinary load;
career additions and other conditions are labeled separately.

| Key fact                 | Selected ordinary load                       |
| ------------------------ | -------------------------------------------- |
| TP cost and availability | 12 TP                                        |
| Health                   | 125                                          |
| Rifle skill              | Starts at 30 with random-stop 1–10 additions |
| Morale                   | 30–39 before career additions                |
| Experience / rank        | 30/3 before the separate XP addition         |
| Starting equipment       | Tommy gun / Thompson                         |

[Starting-stat evidence](../player-roster-evidence.md)

On this page: [Expect separate combat and support decisions](#expect-separate-combat-and-support-decisions), [Availability uses a deployment flag](#availability-uses-a-deployment-flag), [Three support effects have different recipient tests](#three-support-effects-have-different-recipient-tests), [Training chooses an eligible Officer by scan order](#training-chooses-an-eligible-officer-by-scan-order), [An unsuccessful support choice is not an immediate attack retry](#an-unsuccessful-support-choice-is-not-an-immediate-attack-retry).

## Expect separate combat and support decisions

Sarge's selected support choices can rally pinned troops, add XP to an eligible
Officer or add morale to an eligible low-morale recipient. They do not form a
constant all-purpose aura: each has its own gates, and a failed support choice
does not automatically fall through into a shot. Rally also does not reset every
recipient combat field. [Actual support and rally evidence](../player-sarge-support-evidence.md).

Before spending **12 TP**, check the deployment-flag restriction as well as the
unit's job. Losing a Sarge does not, by itself, establish that the offer reopens.
The flag and later aid conditions are selected **2.3.1g** source rules, not a
measured support rate or guaranteed replacement.
[Purchase and flag evidence](../player-recruitment-receipt-evidence.md#sarges-gate-reads-a-flag-not-current-survival).

Combat Ribbon and Medal of Honor each add 3 rifle, Defence Expert Award adds 10
morale, and Mud and Blood Cross adds 9 experience in this profile.
[Exact load evidence](../player-roster-evidence.md#resistance-and-sarge)

Sarge's starting rank 3 and health 125 also match the rank/health alternative in
the selected **Hold Fire offer**. That does not give him every Officer command:
Concentrate Fire, All Around Defense and withdrawal use their own Officer checks.
Compare [which commands need an Officer](orders.md#can-a-veteran-or-sarge-replace-an-officer-for-commands)
before treating rank, XP or Sarge's automatic support as interchangeable.
[Exact Hold Fire gate](../hold-fire.md)

## Availability uses a deployment flag

The menu requires the dedicated Sarge flag to equal zero, then sets it to one
before the spawn helper call. It checks that flag rather than looking for a
living Sarge. Death alone is not established as reopening the offer; selected
initialization has a separate reset write. Full affordability still precedes
the possible medal waiver.
[Exact flag writers and purchase guards](../player-recruitment-receipt-evidence.md#sarges-gate-reads-a-flag-not-current-survival)
Additional source: [Source identities](../player-notes/sarge.md#citation-1)

## Three support effects have different recipient tests

After the controller's actor-state and random entry tests, one branch clears
pinning on qualifying unarmored, pinned recipients within strict source distance 100. Another has an additional random gate and adds 1 experience to a qualifying
Officer **below 50 XP**. The third has its own random gate and adds 1 morale only to
a qualifying recipient **below 20 morale**. [Actual support branches](../sarge.md)

Those are not an uncapped morale aura or a promise every Officer is trained at
each visit. The Officer scan has its own termination behavior after a qualifying
recipient. Health, invincibility, distance, pinning and Sarge's own state still
matter; the numeric range is not a measured safe positioning circle.

A selected Sarge-death morale path subtracts rounded half of a recipient's current
morale under its own armor/other conditions. That is different from the ordinary
rank-related flat subtraction, and not a universal fixed loss. Keep survivability,
retreat claims and source-specific penalties separate. The playerDeath path
resets its scan and can apply a lower-rank loss after the half-loss, whereas
fear's Sarge call does not reset its index before the ordinary nearby-loss loop.
[Penalty ordering](../player-morale-branch-evidence.md#playerdeath-resets-the-index-before-its-rank-loss-loop), [Morale](morale.md)

Sources: [Source identities](../player-notes/sarge.md#citation-2). [Exact evidence](../player-roster-evidence.md)

The selected load also supplies specialization 11, read by the [Allied mortar](mortar.md#a-scout-or-sarge-can-satisfy-one-sight-alternative) sight alternative under health/protection guards. This does not bypass its other target or camouflage rules.
Additional source: [Source identities](../player-notes/sarge.md#citation-3)

## Training chooses an eligible Officer by scan order

The selected training scan takes its first eligible Officer, rather than
comparing who is closest or has the least XP. It adds 1 XP and calls the promotion
helper, then forces its scan index past an ordinary small squad. An Officer at
49 XP can reach 50 at that write; one already at 50 fails this branch's limit.
Current rank and the helper decide whether a promotion follows.
[Exact scan and supplied two-Officer example](../player-sarge-support-evidence.md#officer-training-selects-the-first-qualifying-index)

## An unsuccessful support choice is not an immediate attack retry

Support and ordinary target search are alternatives under the initial random
choice. A later failed training/morale test or an empty recipient scan does not
fall through into ordinary combat at these selected statements. Their personal
timer handling also differs, so one source counter is not the rate of all Sarge
actions. The combat branch's extra bunker chance is not repeated as a separate
gate around every support effect.
[Branch and timer scope](../player-sarge-support-evidence.md#one-admitted-ready-visit-chooses-support-or-ordinary-combat-search)
Additional source: [Source identities](../player-notes/sarge.md#citation-4)

## Rally clears pinning without resetting every combat field

The selected rally recipient branch clears pinning and requests the ready
frame; it does not itself raise morale, clear flee or reset that recipient's
action counter. For supplied morale 0/flee 1/timer 400 at a qualifying target,
those fields remain at the rally sites while pinned becomes 0. A sound or
unpinned animation is not a receipt that every combat requirement recovered.
[Exact target guards and retained fields](../player-sarge-support-evidence.md#sarge-rally-is-not-a-morale-boost-or-ordinary-pin-recovery)

For choosing between a paid boost and an unpin effect, use the
[morale-recovery comparison](morale.md#compare-morale-recovery-with-unpinning).
Cleared pinning, positive morale, flee state and an expired action counter are
separate questions when deciding why a soldier still is not acting.
Comparison source: [Source identities](../player-notes/sarge.md#citation-5)

Sarge's **own** recovery is different: after its morale-plus-flee pin comparison
clears him, it clears flee without the ordinary soldier's later positive-morale
test. His selected active controller also lacks the ordinary positive-morale
admission condition. Remaining health, pinning, withdrawal and other gates still
apply; these facts do not establish immunity to every fear or pinning mechanism.
[Own recovery and controller exception](../player-sarge-support-evidence.md#sarge-own-recovery-differs-even-when-the-threshold-matches-ordinary-infantry)
Additional source: [Source identities](../player-notes/sarge.md#citation-6)

## Fire conversion can reach two separate Sarge morale penalties

The selected enemy flame conversion sets its admitted player's health to-999,
then calls fear and the player-death helper before removal. If that stable
recipient is Sarge, each helper has its own half-of-current-morale loss for
unarmored squad entries; the fatal helper then has its separate lower-rank loss.

For declared Sarge rank 3 and a valid rank 0 follower at morale 20, unchanged
through those calls, the selected writes give 20→10→5→1. Equal-rank 3 instead ends
at 5 at these sites. These are supplied-state source comparisons, not a measured
squad penalty or a claim every Sarge death uses the same caller chain.
[Exact caller, rounding and remaining limits](../player-sarge-burn-evidence.md).
Additional source: [Source identities](../player-notes/sarge.md#citation-7)

The [random-stop rifle comparison](../player-random-stop-load-evidence.md) explains
why this initializer is not five fixed additions. Its conditional mean is
separate from the actual recruit, later bonuses and the role's attack reader.
Additional source: [Source identities](../player-notes/sarge.md#citation-8)

## What happens on a ready update, with or without enemies?

Modern comparison: the following observations and timing examples describe
the **November 7, 2026 simulation build**, not original Flash measurements.
See [dated study limits and later changes](combat-results.md).

Before enemy search, Sarge chooses support on 50% of eligible decisions.
Its three jobs are unpinning, Officer training (additional 10% roll), and
low-morale improvement (additional 20% roll). Eligible recipients are within
100 source units. Training adds one XP to the first eligible Officer below
50 XP; it does not pick the nearest or least experienced one.

If a support roll fails or no recipient qualifies, that update ends without
falling through into shooting. Successful support also leaves Sarge's action
timer unchanged. If it remains expired and other guards pass, Sarge can roll
support/combat again on the next modern 50-ms simulation step.
Under uninterrupted independent 50/50 choices, the average extra wait before
combat search is one update, not half the firing rate.
[Controller and timing explanation](unit-lifecycle.md#sarge-and-officer-support-does-not-require-an-enemy).

With no enemy, support still works. A combat-search decision finds no target,
may request chatter and resets the combat decision timer. With an enemy, the
same support priorities still compete with shooting.

Sarge's basic weapon handling resembles Soldier, including 1–3 Garand/Carbine
repeat counters. Extra support/voice decisions change timing and random draws.
Mixed small equal-stat test advantages do not prove hidden weapon bonuses;
the isolated test also excluded other allies who could benefit.
[Measured comparison](combat-results.md).
