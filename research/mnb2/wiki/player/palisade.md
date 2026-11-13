[Player reference](README.md) · [Defenses](defenses.md) · [Construction](construction.md)

# Palisade: a 3-TP offer with a separate 2-TP completion

For movement, see [can soldiers walk through it?](#can-soldiers-walk-through-it).

The selected menu advertises **3 TP** and requires at least three to select the
order. Its later mouse completion path instead requires at least **2 TP** and
normally subtracts two. This is a concrete selected-source price discrepancy,
not a reason to assume every construction pays its advertised amount.
[Payment source](../palisade.md)

The menu scans for an Engineer-specialization actor with health above ten before
setting the pending construction cue. Completion then requires that cue, a
successful proximity test and sufficient current TP. A conditional medal/random
branch can waive the subtraction; it does not remove that affordability gate.
Pointer selection and completed construction are separate events.

Historical source scope: selected **2.3.1g**. Attributed observations retain
their own version limits below.

| Key fact                  | Selected historical behavior                                         |
| ------------------------- | -------------------------------------------------------------------- |
| TP cost and availability  | Engineer; menu advertises/requires 3 TP                              |
| Normal completion payment | Requires and subtracts 2 TP; conditional waiver after affordability  |
| Classification            | Palisade query; no independent ordinary-cover save established       |
| Movement                  | Operator-observed pass-through; exact original binary not identified |

On this page: [Can soldiers walk through it?](#can-soldiers-walk-through-it) · [A barrier is not another ordinary-cover save](#a-barrier-is-not-another-ordinary-cover-save)

## Can soldiers walk through it?

**The retained operator observation says they can:** historical Palisades block
line of sight, not movement. [October 30 confirmation](../../../../tasks/MNB2-MOD-HR015.md#october-30-operator-correction).

That statement does not identify the exact original binary. It is an attributed
historical-behavior observation, not a new playback test of the selected 2.3.1g
original. The overlap checks below still matter to particular attacks and
abilities: crossing a Palisade does not itself permit a Mechanic to repair or
an Officer to perform aid. [Observation and source boundaries](../palisade.md#retained-operator-observation-movement-and-sight).

## A barrier is not another ordinary-cover save

The selected palisade-overlap helper recognizes **palisade and pillbox** decoration
types. Individual callers decide what this classification prevents. For example,
the Mechanic's selected repair path excludes palisaded actors.
[Mechanic](mechanic.md), [construction helpers](construction.md)

That helper is not itself a complete ray-based sight or bullet-blocking model.
The community describes blocking, tactical enclosure uses and destructibility;
those reports do not certify every firing direction, attack type or transformed
edge position in the selected reference. [Historical report](../palisade.md)

The emitted object's source coordinates use the mouse position, with a random
rotation from −10 through 9. Exact collision geometry, cancellation/reset ordering,
keyboard parity and destruction outcomes still need qualification. Use the
[defense comparison](defenses.md) for ordinary cover versus bunker saves rather
than adding a guessed palisade percentage.

Sources: [Source identities](../player-notes/palisade.md#citation-1).
[Exact source and retained comparison](../player-vehicle-structure-evidence.md)

Movement observation: [Source identities](../player-notes/palisade.md#citation-2)

See [explosions and fortifications](explosions-and-fortifications.md) for the
separate structure-removal and occupant-protection queries.
