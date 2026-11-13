[Player reference](README.md) · [Defenses](defenses.md) · [Support](support.md)

# Air superiority, radar and antenna

Air Superiority, Radar and an antenna serve **different support jobs**. Air Superiority affects particular enemy-request and V1-removal rules; Radar can delay selected enemy requests; an antenna changes a failed radio call’s retry route. They do not provide one universal protective aura or a single percentage speed upgrade. [Detection and consumers](../player-support-evidence.md#air-and-support-buildings)

Historical scope: selected **2.3.1g** source.

On this page: [Which purchase addresses which problem?](#which-purchase-addresses-which-problem) · [Air superiority](#air-superiority) · [The 20 mm gun is a separate purchase](#the-20-mm-gun-is-a-separate-purchase) · [Radar](#radar) · [Antenna](#antenna)

## Which purchase addresses which problem?

| Need                                            | Start with                                          | Keep in mind                                                                   |
| ----------------------------------------------- | --------------------------------------------------- | ------------------------------------------------------------------------------ |
| Change selected enemy air/support opportunities | [1-TP Air Superiority request](#air-superiority)    | Its positive state is neither a certified duration nor guaranteed interception |
| Add delay to selected enemy support requests    | [3-TP Radar construction](radar.md)                 | Delay counters are not calibrated warning seconds                              |
| Change the Signaller's failed-call retry route  | [1-TP Radio Antenna construction](radio-antenna.md) | It does not add to the completion-success roll                                 |
| Place a weapon with an anti-air path            | [20-TP AA cannon](aa-cannon.md)                     | Its crew, rifle and gun state matter separately from the radio request         |

These are selected **2.3.1g** distinctions. The sections below link the source
consumers and remaining limits; prices alone do not rank protection or value.

## Air superiority

If you are choosing Radar for V1 warnings, read the [qualified warning answer](radar.md#does-radar-guarantee-an-earlier-v1-warning).
A delay assignment, a warning and an interception opportunity need their own
source/caller context; this comparison does not promise one defense covers all.

The base advertised request is 1 TP. Its qualified radio branch sets air-superiority
state to 60 and an enemy-plane delay to −1. A separate unpaused controller decrements
the state. The literal 60 does not by itself establish 60 seconds of protection.

### Does Air Superiority stop an attack already underway?

**It is not a guaranteed recall of pending attacks or effects already emitted.**
New enemy requests and later attack delivery use different checks.

One new enemy-support selector is gated by air superiority being below 1,
wave above 10 and a squad-size helper. That does not show all pending attacks are
cancelled: a separately guarded enemy artillery emission lacks that air-superiority
test. An identified V1 rocket frame also has a conditional removal branch while
air superiority is positive, with a separate random test. That is not guaranteed
interception of every rocket. [Exact air-superiority paths](../air-superiority.md)

[Enemy aircraft](enemy-aircraft.md) has source-bound half-selection, strafing/
bomb positions and later gun-reset comparisons. These stages are distinct from
air-superiority request state.

## The 20 mm gun is a separate purchase

The [20 mm AA cannon](aa-cannon.md) is a 20-TP placed weapon with selected
300-health parent load and a separate gun component. Its anti-air roll reads
the parent's rifle; its ground burst counter reads the gun's own XP. A successful
anti-air branch can reset other qualifying guns, and its counter is spent before
the bunker/roll result. This is not radar, a guaranteed interception rate or the
1-TP air-superiority request. [Exact cannon evidence](../player-aaa-evidence.md)

## Radar

The construction menu advertises 3 TP. A selected Boolean helper scans indexed
decorations for its radar flag. In three inspected enemy request branches,
detected radar adds a random 0–29 to the selected delay counter. That is a source
counter addition, not calibrated warning seconds or proof of stronger armor.
[Receiver and delay distinctions](../support-detection.md)

## Antenna

The construction menu advertises 1 TP. The selected presence helper returns a
Boolean from indexed decorations, not a count-based multiplier. After a failed
radio completion roll, its result selects a different retry destination and
associated state. It does not add a term to the experience-based completion
comparison itself. [Signaller](signaller.md), [antenna query](../support-detection.md)

Mobile HQ's component can set related flags, but these radar/antenna helpers do
not automatically gain the separate halftrack scan that the HQ helper has.
Do not turn a parent flag into proof that every caller sees every mobile module.
Full runtime detection and lifecycle/geometry questions remain open.

Sources: [Source identities](../player-notes/air-defense.md#citation-1).
[Exact evidence](../player-support-evidence.md)

Additional mounted-gun source: [Source identities](../player-notes/air-defense.md#citation-2)

The [V1 rocket guide](v1-rocket.md) separates its new-event gates, later
Air Superiority removal opportunity, multi-effect impact and career counter.
Its selected frame-39 removal branch is not a guarantee of interception for
every launched rocket or a universal protection duration.

Read the separate [Radar](radar.md) and [Radio Antenna](radio-antenna.md) cards for
placement, active-state loss and the limits of their different support consumers.

[Original opening and evidence context](../player-notes/air-defense.md#opening-before-player-language-correction).
