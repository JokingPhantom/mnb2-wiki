[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# V1 rocket attack

The V1 is a rocket attack with distinct **launch, interception opportunity,
impact and counter stages**. Air Superiority participates in particular source
paths; neither a warning nor an active protection field proves every rocket
has been canceled. [Exact event and source bindings](../v1-rocket.md)

Historical scope: selected **2.3.1g**.

| Key fact        | Historical behavior                                                      |
| --------------- | ------------------------------------------------------------------------ |
| Interception    | Air Superiority has event gates and a separate later removal opportunity |
| Impact          | Several effect requests at different relative positions                  |
| Counter         | Mission V1 increment is separate from launch, interception and impact    |
| Career reward   | Son of London Ribbon tests career V1 counter strictly above 2419         |
| Important limit | Neither a warning nor active protection proves cancellation or immunity  |

On this page: [Air Superiority acts at more than one stage](#air-superiority-acts-at-more-than-one-stage) · [Impact requests use several different effects](#impact-requests-use-several-different-effects) · [The V1 counter is not an emission or interception count](#the-v1-counter-is-not-an-emission-or-interception-count) · [Son of London Ribbon uses a strict threshold](#son-of-london-ribbon-uses-a-strict-threshold)

## Air Superiority acts at more than one stage

One inspected new-event selector requires Air Superiority state below 1, plus
its wave, squad-size and selector guards, before requesting a V1. Other quoted
rocket launch sites have different recorded guards. That one selector gate
must not be copied into a universal rule that no rocket can exist while
protection is active.
[Emitter comparison](../v1-rocket.md#three-actual-source-emitters-have-different-gates)

A reached rocket frame-39 action first requests an earlier animation frame
when its 0–99 draw is below 90. In the alternative, positive Air Superiority
state admits removal of the rocket. Thus **90–99** are the ten source draw
values that reach this removal opportunity under that supplied state. They
are not a measured overall interception chance: actual visits, state changes,
prior navigation and callback order still matter.
[Rocket loop and removal](../v1-rocket.md#a-frame-39-loop-has-its-own-removal-opportunity)

The support request's selected counter assignment is 60, with a separate later
decrement. That does not establish sixty seconds of protection. Radar's delay
and the 20 mm gun's anti-air attempts are other mechanisms.
[Air defense choices](air-defense.md), [Air Superiority consumer](../air-superiority.md)

For warning expectations, compare [Radar's V1 warning limits](radar.md#does-radar-guarantee-an-earlier-v1-warning).
The quoted Radar delay branches and these direct rocket request sites should
not be treated as one universal countdown or interception mechanism.

## Impact requests use several different effects

The selected later timeline actions request these attack effects around the
rocket's own coordinates at those actions:

| Source action | Requested effect | Relative source y offset |
| ------------- | ---------------- | ------------------------ |
| Frame 90      | Flame explosion  | 0                        |
| Frame 91      | Rocket blast     | +100                     |
| Frame 92      | Rocket blast     | +150                     |
| Frame 93      | Rocket blast     | +200                     |
| Frame 94      | Small explosion  | +250                     |

Frame 90 also requests a crater. A visual crater is a separate emission from the
attack effect. These are relative coordinate writes, not a verified screen
placement stencil, five successful hits or one shared damage radius. The
individual effects have their own blast arguments, ownership and recipients.
[Exact impact emissions](../v1-rocket.md#the-impact-region-has-six-emission-sites-with-different-roles),
[explosion stages](explosion-damage-stages.md), [fortification effects](explosions-and-fortifications.md)

## The V1 counter is not an emission or interception count

The selected rocket action at frame 40 increments the mission V1 counter,
after frame 39's earlier potential removal. A launch request, that increment,
and the later impact requests are separate sites. Reaching one is not proof
all the others completed.

The selected results-screen aggregation adds the mission V1 counter to the
recorded career V1 field. Display, aggregation, flush calls and verified
save/reload remain separate; this source join does not certify durable credit.
[Mission result transfer](../mission-result-accounting.md#display-copies-and-profile-additions-use-different-targets)

## Son of London Ribbon uses a strict threshold

The selected award tests the recorded career V1 counter **above 2419**, with
the Ribbon flag unset and its medal-check/display context. At supplied integer
2419 that comparison fails; at 2420 it passes the counter part. This is not an
observed count of intercepted rockets, immediate award or saved unlock.

The reward description advertises stopping later attacks, but the qualified
direct dependency evidence does not establish a supported positive gameplay
effect for that description. Keep that boundary when planning air defense;
the description alone does not certify immunity.
[Exact award and dependency limits](../v1-rocket.md#the-award-threshold-is-not-proof-of-the-advertised-benefit)

The [enemy rocket soldier](enemy-rocket-soldier.md), [Bazooka soldier](bazooka.md)
and [player rocket launcher](rocket-launcher.md) have their own source paths.

Sources: [Source identities](../player-notes/v1-rocket.md#citation-1). Original synthesis of linked selected-source facts;
no new warning, interception, impact, casualty or persistence trial.
