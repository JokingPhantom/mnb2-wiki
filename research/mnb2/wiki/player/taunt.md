[Player reference](README.md) · [Waves](waves.md) · [Orders](orders.md)

# Taunt: more enemies, TP and wave counting are different effects

**Taunt can call more enemies and conditionally add TP.** A refreshed cooldown
does not prove either happened, and reinforcements need not increment the wave
counter. The selected historical **2.3.1g** button chooses its generator using
local wave; automatic cadence uses a different counter and threshold.
[Exact button and caller evidence](../taunt.md)

Find your question: [eligibility and cooldown](#acceptance-uses-a-cooldown-and-an-allocation-counter),
[when TP is added](#the-direct-tp-addition-depends-on-wave-and-mode), or
[why the wave count may not advance](#taunt-and-automatic-waves-choose-different-generators).

## Acceptance uses a cooldown and an allocation counter

The inspected release handler needs **taunt counter below 1** and **enemy
allocation counter below 80** before its reinforcement call. That enemy counter
is not the late generator's positive-health recount or a visible-enemy total.
The admitted branch sets the taunt counter to 20. A separate failed-allocation
branch also sets it to 20, so a new cooldown does not prove enemies were requested.

A selected cadence site decrements the positive taunt counter while unpaused.
Those writes do not establish 20 seconds or keyboard parity. The menu advertises
hotkey 4; this source binding is for the mouse-release handler, not an independently
qualified equivalent keyboard path. [Controls](controls.md)

## The direct TP addition depends on wave and mode

Within the admitted cooldown/allocation branch, direct TP additions require
mode not 5 and old TP below 20:

| Local wave at this selected button test | Direct addition if other gates pass |
| --------------------------------------- | ----------------------------------- |
| Below 5                                 | +2 TP                               |
| 5 or above                              | +1 TP                               |

That is a pre-write guard. For supplied old TP 19/local wave 4/mode 0 with accepted
button state, the direct +2 write yields 21; it is not a final clamp to 20. Called
generators can have their own resource writes, and intervening state still
matters. This is a declared source-state example, not a measured net taunt payout.
[TP rules](tactical-points.md), [exact resource sites](../taunt.md#the-buttons-tp-addition-is-conditional)

## Taunt and automatic waves choose different generators

| Caller            | Selected generator choice                                                              |
| ----------------- | -------------------------------------------------------------------------------------- |
| Taunt button      | Early below local wave 50; late otherwise                                              |
| Automatic cadence | Early below mission-total wave 100, with an earlier total-wave 5 split; late otherwise |

Automatic calls also need their own unpaused/timer conditions. The two callers
cannot be described by one universal wave 50 or wave 100 threshold. Detailed
Orders crates can change local wave without changing mission-total wave at that
site, so those fields are not always interchangeable. [Wave counters](waves.md)

The late helper only increments local and mission-total wave when its shared
timer is at least 30. A button call can therefore enter that generator without
executing those particular counter writes. Reinforcement attempts, actual living
arrivals and the final HUD display remain distinct. This is why a taunt need
not be summarized as “exactly one wave and one TP.”
[Generator/counter guards](../taunt.md#calling-a-helper-does-not-guarantee-its-counter-increment)

The early generator uses changing budget passes; the late generator uses a
live-enemy deficit with at least one attempt. Taunting does not convert either
into a promised fixed enemy count. A safe timing or optimal TP-farming routine
would need complete initialized state, call ordering and observed outcomes.
[Wave generation](waves.md)

Sources: [Source identities](../player-notes/taunt.md#citation-1).
Selected publisher-associated 2.3.1g; original synthesis of linked exact source
facts, without a new input, timing, reinforcement or payout trial.
