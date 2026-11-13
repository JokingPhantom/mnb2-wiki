[Player reference](README.md) · [Waves](waves.md) · [Enemy guide](enemy-guide.md)

# Waves, reinforcements and local difficulty

A wave number is **not a fixed enemy count**. Different reinforcement rules
can use an internal budget, the number of enemies still alive, or a special
request count. Enemy composition and [enemy starting stats](enemy-stats.md)
are separate ways a battle can change.
[Generator evidence](../player-campaign-evidence.md#wave-generation)

Historical scope: selected **2.3.1g** source; these are conditional rules,
not a forecast of a particular battle.

Find your question: [what changes during battle](#what-should-i-watch-as-the-battle-develops),
[how enemy groups are requested](#how-ordinary-generators-differ),
[Detailed Orders and wave progress](#did-detailed-orders-set-back-my-wave-progress), or
[Taunt's separate rules](#taunting-is-another-caller).

## What should I watch as the battle develops?

These answers describe **selected historical 2.3.1g**, rather than a guaranteed
schedule of enemy arrivals.

- **Is the wave number the number of enemies?.** No. A request or internal budget does not guarantee the same number of living arrivals. See the wave-rule comparison below. [Source scope](../player-campaign-evidence.md#wave-generation)
- **Does a new wave make every survivor stronger?.** Those wave-based values are starting stats. Changing the wave count alone does not update every surviving enemy's stats. [Enemy stat explanation](enemy-stats.md#a-new-wave-does-not-itself-rerun-an-old-load-assignment)
- **Can I use Taunt just to collect TP?.** Taunt can request reinforcements; its TP, cooldown and wave-counter conditions differ. Check those conditions before using it. [Taunt](taunt.md)
- **Why did an unusual group or attack appear?.** Blitz and unfair attacks have separate event paths. Identify the event before treating it as the ordinary next wave. [Blitz](blitz-events.md), [unfair attacks](unfair-attacks.md)
- **Which wave count matters for a medal?.** Local wave, mission-total waves and career waves are separate. Use the named award's actual condition. [Counter distinctions](../wave-counters.md), [medals](career-medals-and-ranks.md)

For recognizing an enemy's job and threats, use the [enemy guide](enemy-guide.md).
If bombardment seems related to squad size, compare the [six-unit rule and other
event paths](concealment.md#does-bombardment-mean-i-broke-the-six-unit-rule).
An attack alone does not identify its caller, and a small squad does not exclude
every hostile support event.
The source details below explain composition; they do not supply a tested build
order or an exact surviving-enemy forecast.

## How ordinary generators differ

| Generator  | What it uses                                             | Interpretation limit                             |
| ---------- | -------------------------------------------------------- | ------------------------------------------------ |
| Early      | Ordered passes spending a changing internal budget.      | Budget units are not guaranteed enemies or TP.   |
| Late       | Attempts based on positive-health enemy count.           | Not a hard cap of 8 living enemies.              |
| Special    | Argument-count attempts with a different selector bound. | Not exactly that many successful arrivals.       |
| Saturation | Allocation cleanup/replacement.                          | Not the same as counting visible living enemies. |

The early budget starts at 1–3 below local wave 15, 4–6 from 15 to below 30, 7–9 from 30
to below 100 in several source branches, and 10 in the remaining branch. Successful
earlier passes change what later passes see. Some pass quotas are snapshots;
their loop condition is not a fresh affordability check against the budget after
every emission. A declared budget is therefore not an exact threat-point total.
[Early source ordering](../early-wave-generation.md)

For ordinary integer live-count examples, the late helper's attempt count is
8 minus counted live entries, raised to at least 1: 0 live gives 8 attempts, 3 gives 5,
and 8 or more still gives 1. A failed extra gate or unmatched selector value need
not create an arrival. This does not cap the battlefield at 8 living enemies.
[Late source model](../late-wave-generation.md)

The special helper draws 0–255, while the late helper draws 0–265. In the selected
special table, one final Goliath branch has no reachable selector value; that
is not evidence Goliaths are absent from other generators or the game.
[Special/late comparison](../special-wave-generation.md)

## “Wave” names refer to different counters

The source distinguishes local mission/terrain wave, mission-total waves and
career-accumulated waves. Detailed Orders crates can reduce the local value by 15
without writing mission total at that site. Another callback applies a lower
bound later. Awards and enemy initializers do not all read the same counter.
[Counter explanation](../wave-counters.md)

The selected mission-end career write adds local wave, not mission total. That
is a source distinction, not a played save-loss result or proof of a constant
offset between the HUD and every internal field.

## Did Detailed Orders set back my wave progress?

**It lowers the local wave by 15 at collection; it does not lower mission-total
waves at that source site.** Which kind of progress you mean changes the answer.
The following comparisons concern selected historical **2.3.1g**.
[Counter and crate evidence](../wave-counters.md)

- **An unearned Bronze, Silver or Gold Star.** These tests read local wave: at least 40, 80 or 120 respectively. A reduced local value can fall below the relevant threshold. Other award guards still apply.
- **Survival or Guerrilla's wave requirement.** These read mission-total waves greater than 100. That field is not reduced by this crate branch; casualties or building/vehicle calls still have their own tests.
- **Career wave accumulation at mission end.** The inspected result action adds the then-current local wave. It does not substitute mission total for that addition. This is separate from career points or an already-earned medal.

For supplied local wave **50** and mission total **110**, an admitted Detailed
Orders subtraction writes local **35**, leaving mission total **110** at that
site. At those unchanged values, an unearned Bronze Star's wave test fails,
while Survival's wave test passes; Survival still needs zero casualties and the
remaining award conditions. If the selected result action later runs with local
wave still 35, its career-wave addition is 35. These are supplied-state source
comparisons, not an observed run or a recommended crate-avoidance strategy.
[Award conditions](career-medals-and-ranks.md#mission-and-wave-milestones),
[result accounting](score-and-career-points.md)

This does **not** establish that an earned medal is removed, that the HUD must
drop by 15, or that saved career progress was lost. Negative local values have a
separate later lower-bound writer; actual HUD binding, callback order and durable
saving remain unqualified. Do not assume one constant gap between the counters.
[Exact writers and limits](../wave-counters.md)

## Taunting is another caller

The selected button chooses the early helper below local wave 50 and the late
helper otherwise, with cooldown/enemy-allocation gates. Calling the late helper
does not guarantee its wave-counter increment: those writes require its timer
to be at least 30. The button's own TP addition has separate conditions, and
cooldown can be reset even when no reinforcement call occurs.
[Taunt](../taunt.md), [TP accounting](tactical-points.md)

Sources: [Source identities](../player-notes/waves.md#citation-1).
Selected 2.3.1g; [exact evidence](../player-campaign-evidence.md).

Composition also changes behavior, not just rifle fields. The [enemy Scout](enemy-scout.md)
has a later request selector and reconnaissance path; a selected request still
needs its own delivery and recipient conditions.

The [German Officer](german-officer.md) special contains an enemyWave helper
call. Its local random comparison, full special playback and the generator's
actual emissions are distinct; this is not a fixed one-enemy arrival rule.

The [Blitz event guide](blitz-events.md) connects the 17 selected cases to their
actor cards while keeping nominal requests, allocation alternatives and later
support delivery separate from observed living arrivals.
Additional source: [Source identities](../player-notes/waves.md#citation-2)

[Taunt](taunt.md) separates direct TP, cooldown and counter increments.
[Changed tactics](changed-tactics.md) explains allocation cleanup and nine nominal
Grenadier requests without turning them into a living-enemy cap or free kills.

[Unfair attacks](unfair-attacks.md) have their own state-dependent admission and
four-case selector. The selected late-wave term can pass even with a supplied
zero missed count. Its precision scan also does not maintain a highest-rank
accumulator; reference selection and actual scattered impact are separate.
Additional source: [Source identities](../player-notes/waves.md#citation-3)

## Scout progress is a shared-timer display, not an arrival census

The selected Scout indicator has a child requesting round(timer*100/30), while
early cadence separately chooses whether its parent is in enabled frame 2.
Supplied timer 15 requests child frame 50; that is not proof half the enemies are
dead, fifteen seconds remain or a particular next unit will appear. The child
has no enemy-count or Scout-health read in its complete body.

The early cadence's recon scan follows its generator request within the entered
totalwave-below 100 block. The separate late-generator alternative has no matching
indicator-frame write there. These source stages do not certify a continuously
refreshed late-wave countdown. The selected ordinary truck warning also reads
that parent frame, rather than independently checking living Scouts at the
message site. [Exact indicator/cadence/warning comparison](../player-recon-display-evidence.md).
Additional source: [Source identities](../player-notes/waves.md#citation-4)

[Enemies getting through the line](breakthroughs.md) compares ordinary, bike,
vehicle and advancement contributions, local loss checks and counter reductions.
