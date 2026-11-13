[Player reference](README.md) · [Support](support.md) · [Tactical points](tactical-points.md)

# Radio Antenna

A **1-TP Engineer construction** that changes a selected failed radio call's
retry route. It does not add a success term to the Signaller's experience roll
or establish a fixed percentage call-speed bonus.
[Exact source/version and construction/disable comparison](../player-support-structure-evidence.md)

Historical scope: selected **2.3.1g** source.

| Key fact        | Selected historical behavior                                         |
| --------------- | -------------------------------------------------------------------- |
| Cost/access     | 1 TP; Engineer construction                                          |
| Payment         | Completion rechecks affordability; conditional waiver after the gate |
| Effect          | Presence changes a failed-call retry route                           |
| Important limit | No added completion-success term or count multiplier                 |

On this page: [Building it](#building-it) · [What it changes](#what-it-changes) · [Losing its active state](#losing-its-active-state)

## Building it

The offer needs an Engineer above 10 health and at least 1 TP. Later placement also
requires a qualifying Engineer strictly closer than 100 in the pointer-distance
helper and repeats affordability. It normally spends 1 TP, requests the antenna
at the mouse point and chooses a random rotation. The selected medal waiver
comes after the TP gate, so 0 TP does not admit it even with a favorable waiver draw.
A pointer or construction counter is not proof of a completed active live object.
[Construction](construction.md)

## What it changes

After a failed Signaller completion roll, the presence query selects a retry
navigation to 55 instead of 38, with associated aiming/counter writes. Those frame
labels do not measure the time saved. The quoted completion comparison remains
a random 0..99 roll below twice experience. Further request-specific payment and
delivery checks remain separate.
[Signaller](signaller.md), [exact retry reader](../support-detection.md)

The query returns Boolean presence from indexed decorations. Extra qualifying
antennae do not become a count multiplier in that caller. A Mobile HQ flag does
not automatically add the separate halftrack scan used by the HQ detector.
[Support overlap and cancellation](support.md)

## Losing its active state

The selected scenery-blast route checks the object's current antenna type and
active flag before requesting its disabled frame. The own disabled body clears
that flag, with no local TP refund, removal request or HQ-bonus repayment. A later
presence query needs the current indexed flags and any other qualifying antenna.
Neither this flag clear nor interrupting a Signaller animation proves every
pending request cancelled or refunded.
[Exact lifecycle and reader limits](../player-support-structure-evidence.md#active-load-and-disabled-frame-are-separate-source-stages)

Sources: [Source identities](../player-notes/radio-antenna.md#citation-1).
Selected publisher-associated 2.3.1g; later candidate coverage, no new native trial.
