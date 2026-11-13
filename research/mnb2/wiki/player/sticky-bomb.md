[Player reference](README.md) · [Construction](construction.md) · [Explosives](explosives.md)

# Sticky bomb

A **2-TP Paratrooper ability** with separate placement validation, following and
explosion stages. **The vehicle that permits placement is not stored as the
bomb's guaranteed following target.** Its later callback performs its own
closest eligible armored-enemy search.
[Existing exact placement and follow comparison](../sticky-bomb.md)

Historical scope: selected **2.3.1g** source.

| Key fact         | Selected historical behavior                                                           |
| ---------------- | -------------------------------------------------------------------------------------- |
| Cost and access  | 2 TP; eligible Paratrooper, then separate placement checks                             |
| Placement inputs | Paratrooper and armored-enemy pointer-distance checks, both strictly below 100         |
| Following        | Later closest eligible armored-enemy search; placement does not freeze target identity |
| Detonation       | TNT effect with its own guarded AT, fragment and scenery work                          |

On this page: [Getting a bomb onto the field](#getting-a-bomb-onto-the-field) · [Why Tiger handling differs from the Bazooka](#why-tiger-handling-differs-from-the-bazooka) · [Fuse and nearby troops](#fuse-and-nearby-troops)

## Getting a bomb onto the field

The offer needs an indexed Paratrooper above 10 health and at least 2 TP. The
later placement checks a Paratrooper above 10 health strictly within 100 of the
pointer, plus a positive-health, positive-armor enemy strictly within 100 of
the pointer. These are two pointer-based tests, not one measured
Paratrooper-to-vehicle throw distance. Payment and creation follow their own
flags; selecting the command is not a completed purchase.

After creation, the bomb's own search can choose the closest eligible armored
enemy and store its name. The later follow writes do not locally recheck that
stored target's health or existence. Detachment after target death still needs
a real target-loss trace; do not treat the community description as a certified
fallback behavior for every selected-build state.

## Why Tiger handling differs from the Bazooka

The selected detonation creates the TNT effect. Its later AT helper call passes
**AT radius 25 and tag tnt**; its separate numeric damage input is 100. The
Tiger's special 500-health subtraction is specifically the **zooka** tag route.
A separately admitted armor-2 Tiger on the tnt route instead takes the other
wreck/removal branch without that nonpositive-health gate.

For supplied helper distance 24 and AT input 25, a valid visible, noninvincible
3000-health Tiger passes that distance test. The zooka branch subtracts 500;
the tnt branch requests removal at the selected sites. Exactly distance 25
fails the gate for both. These are guarded source comparisons, not guaranteed
attachment, a safe blast radius, whole-bomb kill probability or a price ranking.
[Actual effect/tag, every supplied guard and remaining limits](../player-sticky-tiger-evidence.md#the-tiger-exception-requires-both-subtype-and-tag)

## Fuse and nearby troops

Pause-sensitive timeline jumps precede the later emission. The historical
rough fuse description is not a newly measured timer in seconds. The emitted
TNT effect has separate AT, fragment, ordinary damage and scenery consumers;
following one armored enemy does not make every nearby soldier safe.
[Counter/callback and source boundaries](../sticky-bomb.md#animation-and-effect-inputs-qualify-fuse-and-lethality-claims),
[collateral damage](collateral-damage.md)

Related: [airborne wall](improvised-wall.md), [Paratroopers](paratroopers.md),
[AT options](anti-tank-options.md), [explosive stages](explosives.md).

Sources: [Source identities](../player-notes/sticky-bomb.md#citation-1)
