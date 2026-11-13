[Player reference](README.md) · [Deployments](deployments.md) · [Progression](progression.md)

# Unit withdrawal, advancement and ending the mission

Choose the action by its purpose: advancing moves the battle onward, unit
withdrawal attempts to remove a particular troop, and Retreat to Main Menu ends
the mission through the inspected historical **2.3.1g** menu path.

| Action               | Practical consequence and limit                                                                                                             |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Withdraw a unit      | The order must reach the recipient, then its movement and exit guards must succeed. A refund is conditional.                                |
| Advance              | Wounded cleanup, missed-enemy accounting and survivor rewards have separate steps; see [advancement](advancing.md).                         |
| Retreat to Main Menu | Treat this as a mission-ending action. The inspected script has no confirmation predicate; its flush request does not prove a durable save. |

[Selected 2.3.1g interaction evidence](../player-interaction-evidence.md#withdrawal-and-ending).

**Withdrawing one soldier is different from retreating to the main menu.**
The selected unit order sets pending state, applies a recipient flag and uses
later movement/exit guards. The menu-retreat button has a direct flush/gameover
path without a confirmation predicate in that script.
[Mission/withdrawal evidence](../player-interaction-evidence.md#withdrawal-and-ending)

On this page: [Withdrawal value is not a personal purchase receipt](#withdrawal-value-is-not-a-personal-purchase-receipt) · [Missed enemies are a shared counter, not one per visible chassis](#missed-enemies-are-a-shared-counter-not-one-per-visible-chassis) · [A flush request is not a universal save guarantee](#a-flush-request-is-not-a-universal-save-guarantee) · [Ordinary withdrawal has a different movement guard](#ordinary-withdrawal-has-a-different-movement-guard)

## Withdrawal value is not a personal purchase receipt

The selected literal load-value map has 17 unit profiles. Examples from that map:

| Named profile examples                     | Stored refund value (TP) |
| ------------------------------------------ | -----------------------: |
| Regular, Medic, Officer, Crewman, Mechanic |                        3 |
| Engineer, Gunner, Bazooka                  |                        4 |
| Spec Ops                                   |                        5 |
| Scout, Sniper                              |                        6 |
| Mortar                                     |                        8 |
| Sarge                                      |                       12 |
| Paratrooper                                |                        3 |
| Resistance                                 |                        1 |

These values are not dynamically recomputed from whatever TP you personally
paid or spent on later upgrades.
A skipped debit or a starter spawn can still have a positive load field; that
is not an observed free-money exploit. [Exact value/exit joins](../withdrawal-values.md)

The selected additions require a qualifying exit, positive withdrawal state, a
random 0–99 draw below 25 and an old-TP threshold, along with actor-specific guards.
They add the load value when that branch qualifies, rather than simply returning
one quarter of every purchase price. Successful receipt and escape are separate
from selecting the offer.

With no relevant cap bonuses, the cited old-balance guard is **below 19**. At 18,
adding 3 would yield 21 or adding 12 would yield 30 at that write; at 19 the guard fails.
That is not an immediate final-total clamp or a played refund outcome.
[Source-specific gates](../withdrawal-values.md), [TP rules](tactical-points.md)

## Missed enemies are a shared counter, not one per visible chassis

The selected ordinary enemy exit adds 1 and tests post-increment miss above 9:
10 satisfies that source gameover test. A bike can have separate driver/gunner
contributions; advancement also uses different qualifying actor/crew predicates.
Do not replace all of them with “one point for every vehicle” or the current
number of sprites on the battlefield. [Vehicle accounting](../vehicle-crew-accounting.md),
[mission source](../mission-end.md)

The death helper's selected survivor count requires defined health at least 10,
not merely positive health. Advancement has another count with an invincibility
condition. A1–9-health actor or the reuse of a counter name does not make the
two qualifying sets identical.

## A flush request is not a universal save guarantee

The selected menu-retreat script requests profile flush, then gameover, without
a confirmation predicate there. This supports treating it as a mission-ending
action; durable storage, keyboard mapping and every exit/reload outcome have
not been played back by this wiki work.
[Actual exit path](../mission-end.md)

Sources: [Source identities](../player-notes/withdrawal-and-mission-end.md#citation-1).
[Exact source notes](../player-interaction-evidence.md)

[Advancing the squad](advancing.md) now separates admission, wounded-loop morale,
XP/TP rewards and indexed cleanup. Those later writes do not imply a promotion
or a whole-field casualty/save result.

For the later result calculations, see [score, career points and carried TP](score-and-career-points.md).
Field additions, result display and actual durable storage remain separate.

## Ordinary withdrawal has a different movement guard

The selected ordinary soldier's withdrawal flag 1 sends its health-at-least 10,
unpaused callback toward the retreat alternative when it is not pinned. That
route adds 1 to y without repeating normal movement's aiming, wire, facing or
obstacle-test gates. It tests y above 620 after the step; the later refund and
casualty/removal requests are separate from the order receipt.

At this selected route, pinning prevents that retreat y step, and health 1–9 does
not enter the health-at-least 10 normal/retreat block. These are named source
guards, not a guaranteed escape time or a rule for every role. A waypoint click
is also separate from the withdrawal flag.
[Exact ordinary route, thresholds and declared inputs](../player-movement-input-evidence.md#ordinary-withdrawal-chooses-a-different-movement-route).
Additional source: [Source identities](../player-notes/withdrawal-and-mission-end.md#citation-2)

For a normal destination click that did not lead to movement, start with the
[movement diagnostic](controls.md#why-is-a-selected-soldier-not-moving).
A withdrawal flag and a waypoint are different inputs; this retreat route is
not a general workaround for every stalled soldier or vehicle.

[Enemies getting through the line](breakthroughs.md) compares ordinary, bike,
vehicle and advancement contributions, local loss checks and counter reductions.
