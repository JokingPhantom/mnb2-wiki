[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy Scout

The enemy Scout has separate **calling, scouting and ordinary targeting** paths.
Its reconnaissance action changes a shared camouflage-query gate; its calling
path leads to a later support selector. Neither is an immediate guaranteed attack.
Historical scope: selected **2.3.1g**.
[Version identity](editions.md). Sources: [request evidence](../enemy-scout-requests.md),
[reconnaissance state](../reconnaissance-squad-check.md).

| Key fact        | Behavior                                                                      |
| --------------- | ----------------------------------------------------------------------------- |
| Role            | Rifle infantry with separate support-call and reconnaissance actions          |
| Reconnaissance  | Adds to shared state that can block camouflage-net queries                    |
| Support         | Six reachable request families in the inspected selector                      |
| Important limit | Request is not delivery; no calibrated call duration or completed attack rate |

On this page: [Calling and scouting start through guarded animation requests](#calling-and-scouting-start-through-guarded-animation-requests) · [Reconnaissance can block a net query without removing the net](#reconnaissance-can-block-a-net-query-without-removing-the-net) · [The support selector has six reachable families](#the-support-selector-has-six-reachable-families) · [Its firearm is separate from its support call](#its-firearm-is-separate-from-its-support-call)

## Calling and scouting start through guarded animation requests

The selected active callback needs a living nonstock Scout, unpaused state, an
expired action counter and no pinning, before its nested random branches. One
branch requests the calling label; the alternative within that route requests
scouting. Another route handles ordinary target selection. A label request is
not completed support or an uninterruptible call duration.

Its ordinary target helper builds a pool of living, visible, line-of-sight player
indices before the caller chooses from it. It does not establish one universal
nearest-target preference. [Target pool and caller](../target-pools.md#the-scouts-self-receiver-and-gates-differ)
[Starting fields by wave](enemy-stats.md) are a separate part of this enemy's role.

## Reconnaissance can block a net query without removing the net

The selected scouting action **adds 10** to shared reconnaissance state. It does
not replace the field with 10: starting at 0, two executions with no intervening
write give 10 then 20. A separate unpaused positive-counter path subtracts 1 at its
own source visits. These are counter operations, not a calibrated ten-second aura.

The camouflage helper only enters its net-success scan while that shared counter
is below 1. With an ordinary numeric value of 1 or more, that helper reaches its
false result rather than the same net-overlap success path. This write does not
remove a net object or assign every soldier's visibility field. Counter decay,
other writers and actual interruption/death ordering remain separate.
[Exact additions, decrement and query](../reconnaissance-squad-check.md)

## The support selector has six reachable families

The later selected action draws an integer 1–7 and applies ordered branches:

| Selector value | Selected request family         |
| -------------- | ------------------------------- |
| 1              | Artillery request/counter state |
| 2              | Bombing flags and delay         |
| 3              | Smoke strike and delay          |
| 4              | Strafing flags and delay        |
| 5              | V1 projectile emission          |
| 6 or 7         | Paradrop flags/count/delay      |

The later-listed truck alternative has no reachable value left after the earlier
6-or-more branch. This is a local source result, not proof trucks never arrive
through another owner, event or version. Failure of an air branch's extra gate
does not turn its draw into an automatic fallback truck or a fresh random roll.
[Ordered selector and exact gates](../enemy-scout-requests.md#seven-draw-values-do-not-mean-seven-equally-reachable-effect-types)

An artillery branch with its shared counter at zero writes strikes/delay state;
its counter-not-zero alternative instead subtracts one from that counter. Other
requests have their own air/radar and gun-arming conditions. Pending flags, an
emitted V1, actual shells/aircraft and completed damage are different stages.
[Delivery and detection](../support-detection.md), [AA cannon](aa-cannon.md)

No call rate per second, complete-wave probability, guaranteed interruption or
measured support outcome is supplied by these source branches.

Sources: [Source identities](../player-notes/enemy-scout.md#citation-1).
[Version identity](editions.md), [request source](../enemy-scout-requests.md),
[reconnaissance source](../reconnaissance-squad-check.md).

## Its firearm is separate from its support call

The Scout's gun has a burst penalty: its accuracy comparison subtracts twice
the current burst counter from rifle skill. It also has a separate shot-attempt
roll against 10+experience. Shared starting rifle values therefore do not make
its firearm equivalent to the Pioneer's.

With supplied XP 20, rifle 40 and burst 10, the attempt term is (10+20)/100 = 0.30 and accuracy term is (40−2×10)/100 = 0.20; their product is 6%. Thus 6% of reached firearm visits pass those
two gates. With both ordinary-cover and bunker query results supplied true,
the selected saves reduce admission to the health-subtraction branch to 0.75%.
These are declared local source comparisons, including possible zero damage,
not complete hit or kill rates or a placement guarantee.
[Exact inputs, guards and repeat-order limit](../enemy-scout-requests.md#the-ordinary-firearm-has-its-own-experience-and-burst-readers)

Its repeat action requests another shot before decrementing the positive burst
counter. Exact dispatch timing remains unresolved; it does not prove an extra
shot, a whole burst length or how quickly the Scout switches targets.
