[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# SS infantry

SS infantry can start with a higher rifle skill than ordinary enemy infantry: its starting random roll uses the full local-wave range,
while many ordinary enemy loads divide that roll by two. Its firearm still has
separate navigation, burst, accuracy, cover and damage stages. **Ordinary cover
uses a 60% conditional save in this SS firing path**, rather than the 50% used
by several other enemy shooters.
[Exact load and save bindings](../player-enemy-ss-evidence.md)

Historical scope: selected **2.3.1g**.

| Load field      | Selected default                                   |
| --------------- | -------------------------------------------------- |
| Starting health | 100                                                |
| Armor code      | 0                                                  |
| Rifle skill     | Random 0 through local wave minus 1                |
| Experience      | 0                                                  |
| Ammo            | 30                                                 |
| Morale          | 0–99; Assault Expert Award separately subtracts 10 |

At local wave 100 this rifle load can be 0–99. That is not a final 0–99% encounter
accuracy range. Later writes, the current burst and the reached firing stage
still matter. [Wave-stat explanation](enemy-stats.md)

On this page: [Burst setup has a later writer](#burst-setup-has-a-later-writer) · [Cover and pinning have actor-specific effects](#cover-and-pinning-have-actor-specific-effects)

## Burst setup has a later writer

The target-selection controller initially writes burst 1–5, then requests frame 2.
The frame-2 action writes burst 1–6. Quoting only the first assignment misses
that later source writer when the action is reached.

The shot compares an integer 0–99 draw against rifle skill minus twice the
current burst. At declared rifle 40, burst 6/3/1 admits 28/34/38 values at this
comparison. Burst and ammo then decrease in another frame; continuing fire
requests the shot frame directly. The earlier experience navigation test is
another stage, so these counts are not sustained hit rates.
[Exact writers and repeats](../player-enemy-ss-evidence.md#burst-writers-and-navigation)

## Cover and pinning have actor-specific effects

If the target is unarmored, accuracy has passed and both ordinary-cover and
bunker queries are true, independent saves leave **10% unsaved** in this path:
40% fail ordinary cover, then 25% fail the bunker save: 0.40 × 0.25 = 0.10. Trench plus sandbags
still does not supply two ordinary-cover rolls. Geometry remains unresolved.
[Defense stacking](defenses.md)

The inspected forward-movement block checks wire and melee state, but has no
local pin or aiming check. Pinning does prevent its ready action-choice branch.
Those are different restrictions; a pin request alone is not source proof that
all SS movement stops. [Exact movement guards](../player-enemy-ss-evidence.md#load-and-controller-differences)

Sources: [Source identities](../player-notes/ss-infantry.md#citation-1)

## A wave-loaded rifle number still meets the current burst

Wave-dependent starting rifle skill and the current burst counter jointly affect the shot comparison. The linked unchanged-load averages hold burst separately; they are not observed SS hit rates, complete burst sequences or an encounter ranking.

[Full source comparison and limitations](../player-notes/ss-infantry.md#a-wave-loaded-rifle-number-still-meets-the-current-burst).
