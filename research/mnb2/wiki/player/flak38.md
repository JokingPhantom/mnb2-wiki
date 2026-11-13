[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy Flak38 emplacement

The Flak38 is an enemy emplacement with **500 health, armor class 1 and one driver plus
one gunner**. Its burst places small explosions around a selected player's later
point. It has its own controller and effect inputs; the source's shared nebel
type label does not make it a [Nebelwerfer](nebelwerfer.md).
[Exact source and identity](../player-flak38-evidence.md)

Historical scope: selected **2.3.1g**.

| Starting field         | Historical default   |
| ---------------------- | -------------------- |
| Health                 | 500                  |
| Armor code             | 1                    |
| Driver flag            | 1                    |
| Gunner flag            | 1                    |
| Spare crew             | 0                    |
| Rifle skill            | 1–10                 |
| Experience             | 20                   |
| Rank                   | 0                    |
| Morale                 | 0–99                 |
| Setup counter          | 100–399 source units |
| Initial action counter | 0–249 source units   |

These rifle and XP load expressions do not use wave. Neither field appears in
the inspected impact-offset expression. This distinguishes those readers from
an infantry hit-chance comparison; it does not exclude later stat changes.

On this page: [Setup and pinning do not use one universal rule](#setup-and-pinning-do-not-use-one-universal-rule) · [Its explosion is separate from the ejected casing](#its-explosion-is-separate-from-the-ejected-casing)

## Setup and pinning do not use one universal rule

Its setup counter decreases separately from movement's crew, wire, aiming and
random gates. Reaching zero does not also search on that same controller visit.
The later expired action counter resets to **200–449** before searching.
That inspected action branch has **no local pinning check**, unlike the
Nebelwerfer's selected acquisition branch. This is a useful controller distinction,
not measured burst timing or immunity to every pinning effect.
[Exact gates](../player-flak38-evidence.md#setup-and-selection-have-different-gates)

The scan requires a healthy, visible, non-invincible player candidate and line
of sight. It accepts a strictly closer candidate before checking positive armor
to end the scan. Eligible nearby infantry can therefore prevent a farther armor
entry from reaching that preference; candidate order matters.

## Its explosion is separate from the ejected casing

A reached firing action ejects a scaled shell graphic. A later action creates
the small explosion at the target's then-current point with separate
**−100..+99 offsets on each axis**, then decrements the burst counter. The later
repeat action returns to firing while that counter remains positive. These
source stages do not establish an elapsed burst duration or a traveling damage
projectile. [Casing, effect and repeat](../player-flak38-evidence.md#casing-and-damage-effect-are-separate-requests)

The small-explosion helper receives **core radius 7, AT radius 2, fragment radius
50 and damage input 100**, with tag air. These are distinct helper inputs;
recipient checks still determine damage. The air tag alone does not make this
an aircraft interception. Effect ownership remains unresolved at the selected
emission. [Effect arguments and limits](../player-flak38-evidence.md#small-explosion-uses-its-own-helper-arguments)

Losing both crew roles also enters a separate fade/removal path. The parent
health-death branch instead adds its current crew sum to a kill counter and
requests a wreck. Do not equate hull damage, crew damage and net counted kills.
[Crew source](../player-flak38-evidence.md#crew-loss-and-wrecks-are-different-paths),
[small arms against vehicles](small-arms-against-vehicles.md)

Sources: [Source identities](../player-notes/flak38.md#citation-1).
Selected publisher-associated 2.3.1g; no initialized encounter or geometry trial.
