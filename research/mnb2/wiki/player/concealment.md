[Player reference](README.md) · [Waves](waves.md) · [Orders](orders.md)

# Camouflage, reconnaissance and the “six-unit rule”

A **5-TP camouflage net** has a concealment query, distinct from bullet cover,
bunker protection and each actor's visibility counter. In selected historical **2.3.1g**, the camouflage
helper tests net intersections only while shared reconnaissance state is below 1.
A net can therefore still exist while that particular query cannot return its
usual positive result. [Concealment evidence](../player-interaction-evidence.md#concealment)

The net's selected load flammability flag is on. The community describes fragile
nets and hostile interference; exact destruction, coverage boundaries and elapsed
interference duration remain separate from that initializer.
[Net research](../camouflage.md), [bullet defenses](defenses.md)

| Key fact             | Historical scope                                                      |
| -------------------- | --------------------------------------------------------------------- |
| Advertised net cost  | 5 TP; construction offer                                              |
| Mechanism            | Concealment query, separate from ordinary cover and bunker saves      |
| Enemy reconnaissance | Can prevent that net query's positive result without removing the net |
| Squad-size rule      | Randomized qualifying count, not a seventh-unit attack guarantee      |

Start with your question: [does a seventh unit guarantee an attack?](#the-squad-size-helper-is-randomized),
[does bombardment prove I broke the rule?](#does-bombardment-mean-i-broke-the-six-unit-rule),
[can an enemy Scout interfere without removing the net?](#reconnaissance-changes-a-shared-query-condition),
or [is a visibility counter the same as opacity?](#a-visibility-counter-is-not-the-same-as-opacity-or-net-coverage).

## The squad-size helper is randomized

**A seventh qualifying unit does not automatically trigger enemy support.**
The selected squad-size helper makes a random comparison, and only some event
paths use it. Nor is its count simply the number of portraits or visible figures.
[Exact count and event context](../reconnaissance-squad-check.md).

It counts indexed actors with defined health **at least 10** and a negative
camouflage result. A count **above 12** is multiplied by 10 for the weight. The helper then
returns true only when the weight is above 6 and a random 0–2999 draw is below
it. At a supplied qualifying count of 7, seven inputs pass one reached comparison;
that is not a guarantee of an attack, or an attack frequency in seconds.

| Qualifying count | Weight | Passing values at this comparison |
| ---------------- | ------ | --------------------------------- |
| 6                | 6      | None: above 6 condition fails     |
| 7                | 7      | 7 of 3000                         |
| 12               | 12     | 12 of 3000                        |
| 13               | 130    | 130 of 3000                       |
| 16               | 160    | 160 of 3000                       |

These are conditional helper-domain counts, not measured attacks per second.
Other event gates and generators still matter. The count is not automatically
the number of visible infantry portraits or every living sprite on screen.
[Exact count/predicate chain](../reconnaissance-squad-check.md)

## Does bombardment mean I broke the six-unit rule?

**An enemy attack alone does not identify the rule that requested it.** Six
qualifying actors make this particular squad helper return false, but separate
[Blitz events](blitz-events.md) and [unfair attacks](unfair-attacks.md) have their
own conditions. Their selected guards do not use this squad-size helper.
A small squad is therefore not a guarantee against every hostile support event.
[Squad-helper scope](../reconnaissance-squad-check.md),
[Blitz selector](../blitz-reference.md#the-selected-event-selector-has-17-cases),
[unfair-event guard](../player-unfair-event-evidence.md#admission-can-pass-after-wave-80-even-with-no-missed-enemies).

Conversely, a seventh qualifying actor only opens the randomized comparison
above; it does not order an immediate attack. The count uses health and the
camouflage query, not just the figures you can see. Reconnaissance can change
that query without tearing down the net. Check the event and current conditions
before blaming a particular recruit or treating a visible net as proof of safety.
[Count and reconnaissance evidence](../reconnaissance-squad-check.md).

These are selected **2.3.1g** source distinctions. Actual check cadence, net
coverage and complete attack delivery remain unqualified; no attack-per-second
rate, safe roster size or guaranteed way to prevent bombardment follows.

## Reconnaissance changes a shared query condition

**An enemy Scout can interfere with concealment without destroying the net.**
The shared reconnaissance condition and physical net removal are different paths;
neither is a universal change to every soldier's visibility or rendered opacity.
[Scout and net-query evidence](../reconnaissance-squad-check.md).

One selected enemy Scout action adds 10 to shared reconnaissance state; another
active site decrements a positive value. Repeated additions can accumulate,
but 10 is not established as ten seconds simply from that literal. While the
state is at least 1, the helper's net-success path is gated out. This does not
physically remove all nets or set every actor's own visibility field.

The Allied Scout's abilities, the enemy Scout action and the Allied Sniper's
hidden-target selector are separate paths. Do not turn a “spotter” label into
one universal reveal mechanic. [Scout](scout.md), [Sniper](sniper.md),
[reconnaissance chain](../reconnaissance-squad-check.md)

Sources: [Source identities](../player-notes/concealment.md#citation-1).
[Exact source notes](../player-interaction-evidence.md)

The [enemy Scout role](enemy-scout.md) connects its scouting action to shared
reconnaissance additions and the net-query gate, without treating the counter
as physical net removal or a known duration.

## Enemy infiltrator opacity has its own reader

The [hidden infiltrator](brandenburg-and-infiltrators.md) separately processes
its visibility counter and rendering opacity. Detection/shot/pin actions write
different counter values, while the controller handles opacity and decrement
through its own conditions. The counter is not a universal duration in seconds
or the same mechanism as a camouflage-net query.
[Exact order and detector types](../player-brandenburg-evidence.md)
Additional source: [Source identities](../player-notes/concealment.md#citation-2)

## A blast can physically remove a net through another helper

The common blast's first scenery helper has a selected camnet branch that
requests a wreck and net removal after an effect/object hit test. This requests
physical removal, separate from reconnaissance merely preventing the camouflage
query's positive result. No Sandbag-style below-50 choice appears in that net
branch. The later frag/air bunker-removal exclusion does not skip this earlier
helper. Actual intersection and removal visibility still need qualification.
[Exact net branch and source spelling](../player-blast-dispatch-evidence.md#the-first-helper-also-handles-sandbags-and-support-structures)
Additional source: [Source identities](../player-notes/concealment.md#citation-3)

## A visibility counter is not the same as opacity or net coverage

The Allied Sniper and German Sniper have selected 100−XP visibility writes, but
at different actions and under different guards. Their later controllers also
use different zero-counter opacity values: with supplied old alpha 100, the
Allied branch assigns 30 while the German branch assigns 0. A positive 1 counter
can decrement to 0 while alpha remains 100 until a later admitted zero-counter
visit; this is not a measured fade or concealment duration.

The Allied Sniper's separate hand-to-hand entry action writes visibility 100,
rather than using 100−XP. Infiltrators have their own detection/firing/pinning
writes and an hth-dependent decrement. A camouflage net instead answers its
separate reconnaissance-sensitive overlap query.
[Exact named writers, label and supplied state table](../player-visibility-stage-evidence.md).
Additional source: [Source identities](../player-notes/concealment.md#citation-4)
