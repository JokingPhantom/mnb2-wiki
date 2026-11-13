[Player reference](README.md) · [Explosives](explosives.md) · [Collateral damage](collateral-damage.md)

# Resistance sabotage

Sabotage is a **2-TP order on an eligible Resistance soldier**, followed by
departure and a separate shared-state evaluation. Paying the order does not
mean the mission succeeded. The recruit's 1-TP base price is a separate cost.
[Selected request and payment source](../player-sabotage-evidence.md#the-selected2tp-debit-is-at-the-actor-receipt)

Historical scope: selected **2.3.1g** source.

| Key fact           | Selected historical behavior                                                 |
| ------------------ | ---------------------------------------------------------------------------- |
| Cost and recipient | 2-TP order on eligible Resistance; the recruit's 1-TP base price is separate |
| Payment            | Later valid actor receipt, before departure                                  |
| Evaluation         | Shared bonus minus a fresh 0–99 draw; not just the latest actor's XP         |
| Important limit    | Paid order not guaranteed departure, success or suppression duration         |

On this page: [Selection pays before departure](#selection-pays-before-departure) · [The reward reads a shared bonus](#the-reward-reads-a-shared-bonus) · [Suppression is consumed at particular gates](#suppression-is-consumed-at-particular-gates) · [Sending the soldier is not a proved immediate firing cancel](#sending-the-soldier-is-not-a-proved-immediate-firing-cancel)

## Selection pays before departure

The menu checks affordability and enables recipient choice. The selected actor
receipt checks again, requires usable health and no fleeing, then subtracts 2 TP
and marks the actor for sabotage. Its later experience-related sound test is
not the success test. Pending equipment/orders can have earlier priority.

The selected active controller moves a nonwired, unpinned sabotaging actor
upward. At the upper boundary, it contributes its experience to a shared bonus,
requests the evaluation and removes the soldier. Health, morale, withdrawal,
pause and other state still matter; this is not a guaranteed safe journey.
[Departure and contribution](../player-sabotage-evidence.md#the-selected2tp-debit-is-at-the-actor-receipt)

## The reward reads a shared bonus

The evaluation compares the current shared bonus minus a fresh random 0–99 draw.
With an integer positive difference, its selected reward bands are:

| Difference | Selected reward write             |
| ---------- | --------------------------------- |
| 1–24       | +5 vehicle-suppression counter    |
| 25–49      | +10 aircraft-suppression counter  |
| 50–74      | +10 explosive-suppression counter |
| 75 or more | +8 TP                             |

Zero or a negative difference takes the selected failure branch. An earlier
comparison can request another animation pass instead of this evaluation;
these bands are not complete mission probabilities.
[Exact result branches](../player-sabotage-evidence.md#shared-bonus-is-read-the-terminal-expression-does-not-clear-it)

The terminal source statement does not clear the shared bonus. Do not model
every evaluation as automatically consuming it, or replace the shared pool
with only the latest soldier's XP. Other writers, repeated missions and actual
callback order remain necessary before predicting a campaign result.

## Suppression is consumed at particular gates

The selected counters gate particular vehicle generation, aircraft requests
and enemy rocket launch admission. Another unpaused timer site decrements
positive values. An addition of 10 is therefore not yet a certified 10 waves or
10 seconds, and does not itself erase already launched effects or every living
enemy of that kind.
[Named readers and timer](../player-sabotage-evidence.md#suppression-values-have-actual-readers-and-a-separate-decrement-site)

Read [Resistance](french-resistance.md) for the recruit and career modifiers,
and [waves](waves.md) for separate local/mission/career counters. No measured
profit strategy or universal suppression duration is established here.

Sources: [Source identities](../player-notes/sabotage.md#citation-1).
Selected publisher-associated 2.3.1g; [exact identities](../player-sabotage-evidence.md).

## Sending the soldier is not a proved immediate firing cancel

The selected successful receipt marks sabotage and charges 2 TP, without a
local stop-animation, aiming-clear, target-clear or magazine reset. The parent
controller then excludes fresh enemy acquisition while sabotage is 1. Later
own firing/repeat actions do not all repeat that test, so these source sites
alone establish neither guaranteed cancellation nor continued firing.
[Receipt and action boundaries](../player-sabotage-evidence.md#the-sabotage-receipt-is-not-a-local-stop-current-attack-action)

The counter alternative also is not limited to positive timers. With supplied
sabotage 1/timer 0 and its broad entry guards passing, it decrements to −1 while
still skipping fresh search. A negative value is not an immediate-fire signal.
These are conditional field writes, not an observed uninterrupted mission.
[Compound guard and table](../player-sabotage-evidence.md#the-sabotage-receipt-is-not-a-local-stop-current-attack-action)

Its direct north step has wire/pin gates but does not repeat the normal
movement branch's aiming, melee, destination and obstacle tests. That finding
does not certify a safe path through all terrain. At supplied y 15 the earlier
strict departure test fails before a later eligible step writes 14; actual
later departure still needs the actor and broad conditions to remain valid.
[Movement versus earlier departure](../player-sabotage-evidence.md#the-north-step-is-separate-from-normal-destination-movement)
Additional source: [Source identities](../player-notes/sabotage.md#citation-2)
