[Player reference](README.md) · [Orders](orders.md) · [Shooting stages](how-shooting-works.md)

# One observed rifle sequence: firing is not the same as hitting

In one fixed selected **2.3.1g original-game scenario**, the first eight observed
Allied rifle fires do not increase the hit counter. The ninth fire reduces its
target from **100 to 98 health** and increases hits from 0 to 1. Both retained
repeats agree. This is an actual bounded example, not an average hit rate or a
promise about a new deployment.
[Qualified observation and exact inputs](../shared-rifle-sequence.md)

| World tick | Firing slot | Target index | What this visit shows                                        |
| ---------- | ----------- | ------------ | ------------------------------------------------------------ |
| 611        | Soldier 3   | Enemy 0      | First global rifle fire; no hit increment; target stays 100  |
| 700        | Soldier 3   | Enemy 1      | Same soldier, different target index; no hit increment       |
| 1110       | Soldier 0   | Enemy 1      | Ninth global fire; first hit increment; target health 100→98 |

These are selected rows, with other fires between them. Soldier numbers are
slot identities in this one start. The qualified actors are ordinary character 623;
the table does not compare three different recruit classes.

## What it tells you about reaction and retargeting

The same soldier can fire at different indexed targets across visits. Here,
Soldier 3's selected fires are 89 world ticks apart, but that is **not its retarget
time**. The rows do not say when its target changed, when it first became ready,
or which intervening decisions consumed time. A universal fire-rate figure would
hide those separate stages. [How shooting works](how-shooting-works.md)

Nor does a shot or sound alone prove damage. The first hit here subtracts only 2
health at its observed boundary and leaves that target alive. That single draw
is not typical damage, maximum damage or expected DPS. The complete 1,508-tick
capture has 18 rifle fires and four hit-counter increases; those figures describe
this fixed encounter, rather than an estimate for arbitrary soldiers or waves.

The two repeats use the same seed, date and recorded inputs. They demonstrate
repeat agreement, not two independent random starts. No elapsed reload time,
first-shot delay, hitbox probability, generated-model acceptance or full encounter
resolution is inferred. [What remains open](../RECONSTRUCTION_REQUESTS.md)

Sources: [Source identities](../player-notes/observed-rifle-sequence.md#citation-1).
[Source identities, review and frozen receipts](../shared-rifle-sequence.md).
No new game run or reconstruction engine was created for this wiki explanation.
