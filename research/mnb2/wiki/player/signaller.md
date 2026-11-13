[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Role comparison](recruitment.md#choose-the-job-before-the-price)

# Signaller

A **3-TP radio specialist** that turns support requests into attempted calls.
The legacy guide equips it with a Springfield and radio pack and describes slow
movement. Its starting experience is 3, and experience changes a selected call
completion roll; it is not a universal radio-speed multiplier.
[Radio actor evidence](../player-specialist-evidence.md#signaller)

Applies to **historical selected 2.3.1g**. Starting facts use the ordinary load;
career additions and other conditions are labeled separately.

| Key fact                 | Selected ordinary load                      |
| ------------------------ | ------------------------------------------- |
| TP cost and availability | 3 TP; Reinforcements                        |
| Health                   | 100 health points                           |
| Rifle skill              | Starts at 0 with random-stop 1–10 additions |
| Morale                   | 10–19 before career bonuses                 |
| Experience               | 3; Mud and Blood Cross adds 9               |
| Starting equipment       | Community: Springfield and radio pack       |

[Starting-stat evidence](../player-specialist-evidence.md)

On this page: [Requesting support with a Signaller](#requesting-support-with-a-signaller), [Experience helps one completion roll](#experience-helps-one-completion-roll), [Antennas and interruptions](#antennas-and-interruptions), [An interrupted animation is not a refund or a cleared request](#an-interrupted-animation-is-not-a-refund-or-a-cleared-request), [Isolated shooting versus radio work](#isolated-shooting-versus-radio-work).

## Requesting support with a Signaller

Choose the needed [radio support](support.md), complete any required target or
coordinate step, and keep its payment conditions in mind until acceptance.
The Signaller attempts a call; even a passing completion roll still leaves that
request's own TP and delivery conditions. Higher XP helps the inspected roll,
but does not guarantee an immediate arrival. [Call and cleanup evidence](../signaller.md).

If the expected support does not arrive, distinguish a failed/retried call, a
request cleared after a later affordability failure, and an accepted request
still awaiting its effects. An antenna changes a retry path. Interrupting the
animation with an order does not itself prove cancellation, refund or recall.
[Retry rules](../signaller.md), [interruption limits](../player-signaller-interruption-evidence.md).

Selected historical **2.3.1g**; no guaranteed call duration or universal refund
rule is qualified. Individual support pages explain the different charges.

Combat Ribbon and Medal of Honor each add 3 rifle points; Defence Expert Award
adds 10 morale in this load profile. These bonuses do not collapse call timing,
shooting ability and survivability into one stat. [Load bindings](../player-specialist-evidence.md#signaller)

## Experience helps one completion roll

Before treating the Signaller alone as sufficient for every offer, compare
[which support requests also check for an Officer](support.md#do-i-need-an-officer-as-well-as-a-signaller).
The selected request guards differ, and their above-10 health tests are separate
from later communication, payment and delivery.

At the selected unpaused completion frame, the comparison is a random 0–99 roll
**below twice experience**. At base experience 3, 6 of 100 possible rolls pass;
at experience 25, 50 pass; at 50, all 100 pass. These are conditional values for one
frame's gate, not call success per second or guaranteed support delivery.
[Completion/retry trace](../signaller.md)

After the gate, requests are handled in this order: bombing, strafing, artillery,
air superiority, smoke, situation report, paradrop, naval, counter-artillery.
The ordered branches do not deliver every pending request simultaneously. Each
request still has its own resource and state checks.

Several actor request flags are then cleared under the successful completion
roll, even when a branch's affordability test fails. A cleared request therefore
does not prove shells or aircraft arrived. Paradrop and counter-artillery are
not in that particular reset list; do not extend the rule to them automatically.
[Request cleanup conditions](../signaller.md)

## Antennas and interruptions

A failed roll has different retry destinations depending on whether the antenna
helper returns true. That is a concrete retry-path difference, not evidence of
a fixed percentage speed bonus or a guaranteed completion duration.
[Radio retry evidence](../signaller.md)

The community reports that pinning, Concentrate Fire and Hold Fire can interrupt
calls and warns that repeated situation reports have a post-2.3 cooldown. Those
reports need their exact actor/caller paths before treating all interruptions as
cancellation with an identical payment/refund outcome. Read the individual
request's source explanation. [Bombing](../bombing-request.md),
[situation reports](../situation-report.md)

Sources: [Source identities](../player-notes/signaller.md#citation-1). Selected 2.3.1g; [exact evidence](../player-specialist-evidence.md).

## An interrupted animation is not a refund or a cleared request

The selected Signaller Hold Fire receipt assigns its action counter 400 and
requests the ready frame when unpinned. It does **not explicitly clear its local
radio requests** at that branch. A qualifying Concentrate Fire helper can instead
request combat preparation without an explicit radio-request cleanup. Those
navigation requests help explain the community's interruption warning, but do
not qualify complete cancellation, automatic resumption or support delivery.
[Exact order/actor paths](../player-signaller-interruption-evidence.md#hold-fire-receipt-does-not-explicitly-erase-a-radio-request)

The comms entry's counter 9999 is also a field assignment, not a reserved call
duration. If that unchanged value later reaches this actor's eligible positive-
counter section, it decrements then caps to 100. Actual frame/controller order
must be established before interpreting that conditional change as elapsed time
or a demonstrated way to make a call faster.
[Counter guard and supplied inputs](../player-signaller-interruption-evidence.md#the-radio-entry-counter-is-not-an-invulnerable-reservation)

Successful completion cleanup and each request's payment are separate sites.
Neither stopping an animation nor retaining a local request proves a TP refund,
recalls an emitted shell, or guarantees a retry. Keep the individual support
path and current request/delivery state in view.
Additional source: [Source identities](../player-notes/signaller.md#citation-2)

## Isolated shooting versus radio work

Modern comparison: the following observations and timing examples describe
the **November 7, 2026 simulation build**, not original Flash measurements.
See [dated study limits and later changes](combat-results.md).

Signaller exactly matched Soldier across six offered weapons in the equal-stat
stationary modern study, where radio work was absent. Calling, retries, completion
and actual support delivery are separate lifecycle stages and can interrupt that
ordinary shooting context. [Lifecycle](unit-lifecycle.md), [combat results](combat-results.md).
