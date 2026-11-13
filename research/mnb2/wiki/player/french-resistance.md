[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Role comparison](recruitment.md#choose-the-job-before-the-price)

# French resistance soldier

A **1-TP recruit** with a distinct low-stat base profile and a staged sabotage
path. Its selected rifle initializer is a single 1–5 roll before career bonuses,
not the repeated random-stop loop used by many other recruits.
[Resistance evidence](../player-roster-evidence.md#resistance-and-sarge)

Applies to **historical selected 2.3.1g**. Starting facts use the ordinary load;
career additions and other conditions are labeled separately.

| Key fact                 | Selected ordinary load                                 |
| ------------------------ | ------------------------------------------------------ |
| TP cost and availability | 1 TP                                                   |
| Health                   | 75; 100 with Legion d'Honneur's load condition         |
| Rifle skill              | 1–5 before career additions                            |
| Morale                   | 2–11 before Defence Expert Award's +10                 |
| Experience               | 0 before Mud and Blood Cross's +9                      |
| Starting equipment       | Springfield; Garand with Meritorious Unit Commendation |

[Starting-stat evidence](../player-roster-evidence.md)

On this page: [Recruiting a cheap soldier and sending a saboteur are separate choices](#recruiting-a-cheap-soldier-and-sending-a-saboteur-are-separate-choices), [The 1-TP offer can substitute a Spec Ops recruit](#the-1-tp-offer-can-substitute-a-spec-ops-recruit), [Sabotage is a request and a later evaluation](#sabotage-is-a-request-and-a-later-evaluation), [Weapon-specific recovery advantage](#weapon-specific-recovery-advantage).

## Recruiting a cheap soldier and sending a saboteur are separate choices

The **1-TP recruit** is not a low-price copy of the Regular Soldier: health,
rifle and morale start differently. Sabotage has a separate **2-TP recipient
debit** under its own conditions. When the qualifying saboteur reaches the
departure path, the actor is removed before the later result evaluation.
Do not budget a guaranteed reward or assume the soldier remains on the line.
[Recruit and sabotage evidence](../french-resistance.md), [sabotage stages](sabotage.md).

The Ribbon-dependent Spec Ops substitution belongs to the purchase path, not a
promotion or second recruit. Check the actual arrival/profile before equipping
it. These are selected **2.3.1g** source conditions, not a measured profit strategy.

Combat Ribbon adds 5 rifle points in this profile, differing from the 3-point
addition seen in many other loads; Medal of Honor adds 3 separately. The retained
community rifle 1–20 card should not overwrite these ordered source assignments.
[Exact career/profile comparison](../french-resistance.md)

## The 1-TP offer can substitute a Spec Ops recruit

The selected purchase body separately tests a random 0–99 draw against Special
Operations Ribbon's stored value. With that value supplied as 1, only draw 0
requests the Spec Ops template instead of Resistance; with 0, none pass.
This happens after the payment/waiver choice. It is a replacement recruit,
not a second soldier or a promotion of an already placed Resistance actor.
Legion d'Honneur's health bonus is a different medal and load path.
[Exact offer, medal and spawn mapping](../player-recruitment-receipt-evidence.md#resistance-can-request-the-spec-ops-template-instead)
Additional source: [Source identities](../player-notes/french-resistance.md#citation-1)

## Sabotage is a request and a later evaluation

The inspected recipient request needs health above 9, no fleeing and at least 2 TP,
after earlier pending actions. It sets the actor's sabotage state. That alone is
not a successful mission. The selected valid receipt subtracts 2 TP at that stage;
the menu selection has a separate affordability check.

At the selected top-boundary/controller path, a usable sabotaging actor adds its
experience to a **shared sabotage bonus**, starts a separate evaluation clip and
is removed. The bonus is accumulated shared state, not simply an independent
success percentage belonging to that one recruit. [Request and departure](../french-resistance.md)

The later positive-result branches can add vehicle, air or explosive suppression
state, or TP, depending on another comparison. Numeric additions to those states
are not automatically that many seconds or waves of suppression. Multiple
contributors, resets, retries and downstream consumers remain relevant; no
universal reward frequency or guaranteed cheap-recruit profit is certified.

Sources: [Source identities](../player-notes/french-resistance.md#citation-2).
Selected 2.3.1g; [exact bindings](../player-roster-evidence.md).

The [Sabotage guide](sabotage.md) follows the actual debit, departure, shared
bonus, result bands and named suppression-counter consumers. Its selected
terminal expression does not clear the shared bonus.
Additional source: [Source identities](../player-notes/french-resistance.md#citation-3)

The [sabotage movement/counter comparison](sabotage.md#sending-the-soldier-is-not-a-proved-immediate-firing-cancel)
separates blocking fresh target search from a proved cancellation of every
started attack. Wire, pinning and the earlier departure check also have
different source scopes; the north-step expression is not a safe-route guarantee.
Additional source: [Source identities](../player-notes/french-resistance.md#citation-4)

## Weapon-specific recovery advantage

Modern comparison: the following observations and timing examples describe
the **November 7, 2026 simulation build**, not original Flash measurements.
See [dated study limits and later changes](combat-results.md).

Resistance's nonempty Garand recovery writes 10+random(100)−XP instead of the
ordinary 50+random(100)−XP. Its empty Thompson writes 100−XP instead of 150−XP.
These internal assignments feed later controller processing; they are not seconds.

In the modern equal-stat veteran group test, Resistance/Thompson cleared the
medium formation in 85.28 seconds versus Soldier's 106.84. Resistance/Garand
also improved, but these rules do not give every Resistance weapon a damage bonus.
Natural low recruit stats remain a separate concern.
[Results](combat-results.md), [modern recovery evidence](../player-notes/french-resistance.md#modern-recovery-implementation).
