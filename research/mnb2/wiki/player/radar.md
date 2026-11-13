[Player reference](README.md) · [Defenses](defenses.md) · [Support](support.md)

# Radar

A **3-TP Engineer construction** that can add delay to three selected enemy
support-request paths. It is a different system from the 1-TP Air Superiority
request and the 20-TP anti-aircraft cannon. The source does not establish one
fixed number of warning seconds or a guaranteed interception.
[Exact source/version and construction/disable comparison](../player-support-structure-evidence.md)

Historical scope: selected **2.3.1g** source.

| Key fact                 | Selected historical behavior                                       |
| ------------------------ | ------------------------------------------------------------------ |
| TP cost and availability | 3 TP; Engineer construction                                        |
| Payment                  | Rechecked at completion; conditional waiver after affordability    |
| Selected effect          | Presence can add a 0–29 delay draw to three enemy-request branches |
| Important limit          | No guaranteed V1 warning or interception                           |

On this page: [Building it](#building-it) · [What it changes](#what-it-changes) · [Does Radar guarantee an earlier V1 warning?](#does-radar-guarantee-an-earlier-v1-warning) · [Losing its active state](#losing-its-active-state)

## Building it

The offer needs an Engineer above 10 health and at least 3 TP. Actual placement
checks for a qualifying Engineer strictly closer than 100 in the pointer-distance
helper, then repeats affordability. It normally spends 3 TP and requests Radar at
the mouse point with a random rotation. The selected medal waiver happens only
after affordability passed; with 2 TP, that waiver does not admit this build.
These are source gates, not a native placement stencil or a safe-location guide.
[Construction](construction.md)

## What it changes

Three inspected enemy-request branches assign a base delay 10..24 and add 0..29
when the Radar helper returns true. At those assignments possible stored delay
is 10..53: the extra draw can be zero. These are counters, not measured warning
seconds. The helper returns presence, so two detected Radars do not add two
extra rolls at that one caller. A possible Mobile HQ component is not proof of
membership in this decoration-only scan.
[Exact detection and callers](../support-detection.md), [Air defense](air-defense.md)

## Does Radar guarantee an earlier V1 warning?

**That guarantee is not established for selected 2.3.1g.** The archived Radar
guide advertises earlier aircraft/rocket warnings, but the retained source
qualifies three particular enemy-request delay branches. The direct V1 request
quoted from the same frame-168 action belongs to a different selector case.
Its emission guard is not the same thing as a Radar-added delay assignment.
[Attributed warning claim and delay branches](../support-detection.md#three-enemy-request-branches-add-a-radar-dependent-delay-term),
[direct V1 request scopes](../v1-rocket.md#three-actual-source-emitters-have-different-gates)

Do not turn a possible Radar delay counter into promised V1 warning seconds,
or assume a warning means the rocket will be intercepted. Actual warning
coverage and elapsed timing still need qualification. This does not prove
Radar has no effect through any other caller or in another version.

[Air Superiority](air-defense.md) is a separate request: a positive state can
participate in a conditional rocket-removal opportunity. Radar's delay draw
does not itself perform that removal. Follow the [V1 stages](v1-rocket.md) when
distinguishing a request, warning, removal opportunity and eventual impact.

## Losing its active state

A qualifying scenery-blast intersection has a selected route to the Radar's
disabled frame when its current Radar type and active flag match. That own frame
clears the active flag. The small body has no local TP refund or HQ-style shared
bonus repayment. Actual callback order and other structures still determine the
next detection result. This flag clear alone does not subtract a previously
assigned enemy delay or recall an already emitted attack.
[Exact lifecycle limits](../player-support-structure-evidence.md#active-load-and-disabled-frame-are-separate-source-stages)

Sources: [Source identities](../player-notes/radar.md#citation-1).
Selected publisher-associated 2.3.1g; later candidate coverage, no new native trial.
