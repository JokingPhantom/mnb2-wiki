[Player reference](README.md) · [Anti-tank options](anti-tank-options.md) · [Vehicles and emplacements](vehicles-and-emplacements.md)

# Blast radius, scattered impacts and direct fire

When comparing mounted weapons, separate **where an effect appears** from
**which recipients it can damage afterward**. The selected original 2.3.1g
source uses several different paths; a field named blastrange does not combine
them into one accuracy or blast-size stat.

On this page: [Which attack path am I comparing?](#which-attack-path-am-i-comparing) · [A fixed-input placement example](#a-fixed-input-placement-example) · [Follow the later recipient test](#follow-the-later-recipient-test)

## Which attack path am I comparing?

| Selected weapon path                      | What actually places or resolves its attack                                                    |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Sherman, Panther and Tiger cannon effects | Current indexed target coordinates plus separate −100…99 offsets on each axis                  |
| Flakpanzer effects                        | The same fixed offset expressions, but two effect frames read different target-field receivers |
| SdKfz 222 turret                          | Rifle comparison and recipient armor/protection branches at its selected shot action           |

The tank cannon bodies reduce their stored blastrange field by 50 and floor it
to 1 before emission. Their coordinate formulas still use the fixed offsets.
A shorter stored range alone therefore does not tighten those formulas. The
222 also stores blastrange during selection, yet that field does not drive its
selected direct-fire shot.
[Exact receiver map and conditional examples](../player-blastrange-reader-evidence.md).

## A fixed-input placement example

For a valid target at (200,200), supplied offset draws 0 and 199 place the selected
tank effect at (100,299), whether the reduced field is 250 or 1. This is a source
calculation with declared inputs. Target movement, validity, effect ownership
and the later blast tests still matter; it is not an observed miss probability.

## Follow the later recipient test

Use the [AT guide](anti-tank-and-vehicles.md) for the later strict point-distance
and crew/core distinctions. A visible tank outline is not that point test, and
the 200 possible axis draws do not mean a 200-unit damage radius. Likewise,
ordinary bullet protection and fragment/AT protection need their own readers.
[Defense paths](defenses.md).

For buying and comparison, start with [mounted weapons](vehicles-and-emplacements.md),
[enemy tanks](enemy-tanks.md), [Flakpanzer](flakpanzer.md) or [222](sd-kfz-222.md).
Full firing rate, transformed geometry and initialized hit probabilities remain
unqualified. These later additions are candidates; the original pilots retain
their prior acceptance.

Source: [Source identities](../player-notes/blast-radius-and-scatter.md#citation-1)
