[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy Pioneer

The enemy Pioneer sabotages prepared defenses and explosives. It can
plant TNT near certain structures, remove mines/TNT and disable active barbed wire.
These are separate actions with different eligibility tests.
Historical scope: selected **2.3.1g**.
[Exact sabotage evidence](../player-pioneer-evidence.md)

On this page: [What it can do](#what-it-can-do) · [Timing and interruption](#timing-and-interruption) · [Starting combat stats](#starting-combat-stats) · [Its gun has a separate burst counter](#its-gun-has-a-separate-burst-counter)

## What it can do

| Selected object                           | Sabotage branch                                                                                     |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------- |
| Bunker, Palisade, camouflage net, Pillbox | A successful object-overlap test creates a TNT object near the Pioneer                              |
| Mine or TNT                               | Strict distance below 100 removes it; a booby-trapped one first creates an explosion at the Pioneer |
| Active Barbed wire                        | Strict distance below 100 sets its active flag to 0 and stops it at frame 21                        |

The TNT placement branch does not itself certify structure destruction. The mine
branch increments the booby-kill counter when it creates the explosion, before a
kill outcome is established. Avoid reading that counter as proof that every
booby-trapped mine necessarily kills a Pioneer.
[Exact branches and limits](../player-pioneer-evidence.md#three-different-decoration-actions)

## Timing and interruption

Sabotage requires a living, unpaused deployed instance and its separate timer to
be negative. The load timer starts 0; with unchanged guards and no other writer,
the first admitted visit decrements it and the second scans. Afterward a random
0..299 reset changes the number of admitted visits until the next scan. This is
not a verified period in seconds.

The sabotage guard does not test wired, pinned or aiming. Wire's movement penalty
therefore does not, by these guards alone, guarantee that sabotage stops. More
than one decoration may be visited in a scan.
[Timer derivation](../player-pioneer-evidence.md#load-values-and-sabotage-admission),
[movement-reader distinction](../player-pioneer-evidence.md#wired-movement-and-independent-sabotage)

## Starting combat stats

| Starting field | Historical default                                        |
| -------------- | --------------------------------------------------------- |
| Health         | 100                                                       |
| Armor code     | 0                                                         |
| Experience     | 1–100                                                     |
| Rifle skill    | Random integer 0 through local wave minus 1, divided by 2 |

The rifle value is not a final hit percentage. Later combat,
spawn overrides and actual encounters remain separate from this load receipt.
[Wave-stat interpretation](enemy-stats.md)

Related: [Barbed wire](barbed-wire.md), [construction](construction.md),
[explosives](explosives.md). Source: [Source identities](../player-notes/enemy-pioneer.md#citation-1)

## Its gun has a separate burst counter

The firearm path is separate from sabotage. Its selected target scan requires
living visible eligible allies and line of sight; a nonmelee selection starts
a burst counter 1–10. The shot's accuracy test subtracts twice the current burst
counter from rifle skill. Its repeat action decrements a positive counter
before requesting another shot.

With supplied rifle 40, a reached shot visit with burst 10 admits 20 of 100
accuracy inputs; with burst 1 it admits 38, and with burst 0 it admits 40. These
are conditional source comparisons, not whole-burst hit rates. Cover saves
and damage still follow. The selected ordinary-cover and bunker saves are
50% and 75%, with their query results supplied rather than inferred from a layout.
[Exact firearm fields and examples](../player-pioneer-evidence.md#burst-changes-the-firearm-accuracy-reader)

The ordinary firing exit clears aiming without writing a new timer. The
controller separately resets an expired action timer, including visits that
do not select a target. Its independent sabotage timer cannot be used as the
gun's reload time. [Controller and timer distinction](../player-pioneer-evidence.md#its-firearm-search-and-timer-differ-from-sabotage)
