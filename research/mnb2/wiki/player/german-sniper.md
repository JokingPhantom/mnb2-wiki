[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# German Sniper

The German Sniper starts with **rifle skill equal to the local wave**. Firing still depends on a separate attempt roll, concealment state and ordinary-cover save. Its attack is one reason a
bunker or an ally's hidden counter is not universal protection.
Historical scope: selected **2.3.1g**.
[Exact Sniper evidence](../player-german-sniper-evidence.md)

| Starting field      | Selected enemy load                               |
| ------------------- | ------------------------------------------------- |
| Starting health     | 100                                               |
| Armor code          | 0                                                 |
| Rifle               | Local wave W at load                              |
| Starting experience | 1–70                                              |
| Starting rank       | 0                                                 |
| Morale              | 5–104; subtract 10 if Assault Expert Award flag>0 |
| Visibility counter  | 0                                                 |

These are load sites, before later mutations. Rifle 100 at W=100 is not a guaranteed
shot or kill. [Wave-dependent stats](enemy-stats.md)

On this page: [Ordinary cover still matters; the inspected bunker save is absent](#ordinary-cover-still-matters-the-inspected-bunker-save-is-absent) · [A hidden ally is not automatically excluded from its scan](#a-hidden-ally-is-not-automatically-excluded-from-its-scan) · [Its reveal write happens before the hit comparison](#its-reveal-write-happens-before-the-hit-comparison)

## Ordinary cover still matters; the inspected bunker save is absent

Its firearm first rolls against **10+experience**, then against rifle. The
unarmored path can apply a **50-of-100 ordinary-cover save**, but lacks the extra
bunker save used by several other enemy firearm bodies. Its selected damage draw
is **0–199**, including zero; resulting health below 10 requests death in that branch.
[Protection differences](defenses.md)

For one declared W=100 / XP 20 firearm-frame visit with a valid unarmored target,
independent uniform integer 0–99 rolls and no other supplied modifiers:

| Ordinary-cover success test | Chance to reach health-subtraction branch |
| --------------------------- | ----------------------------------------- |
| False                       | 30%                                       |
| True                        | 15%                                       |

At W=100 and XP 20, (10+20)/100 attempt × 100/100 rifle comparison = 30%; a successful ordinary-cover query halves it to 15%. Those are source-branch counts, not a kill chance, firing rate or measured battle
result. An actual layout is not assumed to satisfy the ordinary-cover success test.
[Inputs and exact body](../player-german-sniper-evidence.md#the-firearm-has-attempt-accuracy-and-ordinary-cover-stages)

## A hidden ally is not automatically excluded from its scan

The selected target scan checks health, invincibility, line of sight, melee state
and armor other than class 2, but does not require the target's visibility counter
to be positive. Other guards can still fail. Its rank-sensitive stored-range rule
also depends on scan order; it is not a promise always to choose the nearest or
highest-ranked soldier. [Acquisition rules](../player-german-sniper-evidence.md#acquisition-does-not-require-positive-target-visibility)

## Its reveal write happens before the hit comparison

A passed firing-attempt branch sets its visibility counter to **100−XP**, before
the rifle comparison. With the unchanged base XP range this is 30–99 counter units.
The active controller decrements a positive counter and switches opacity by its
own guards. These values are not calibrated seconds or the allied Sniper's cloak
cycle. The initial action counter is not a complete reaction-time statistic.
[Visibility and timing boundary](../player-german-sniper-evidence.md#reveal-counter-and-opacity-are-different-stages)

Sources: [Source identities](../player-notes/german-sniper.md#citation-1). [Exact evidence](../player-german-sniper-evidence.md)

Even a supplied 200-health recipient can be left with **9 health by a draw of
191**, which reaches this body's below-ten death-state request. A draw of 190
leaves 10 and fails that comparison. These are admitted-branch inputs, not a
measured kill probability or permanent casualty. [Heroism and this threshold](heroism.md#the-german-snipers-below-ten-test-still-matters),
[exact evidence](../player-german-sniper-evidence.md#a-supplied-200-health-target-can-meet-the-below-ten-request-with-health-positive).
Additional source: [Source identities](../player-notes/german-sniper.md#citation-2)

## A reveal-counter average needs the right inputs

Higher experience both admits more attempt inputs and writes a smaller reveal counter. A source-input average needs the correct weighting; neither the ordinary nor conditional mean measures cloak duration or reveal rate.

[Full source comparison and limitations](../player-notes/german-sniper.md#a-reveal-counter-average-needs-the-right-inputs).
