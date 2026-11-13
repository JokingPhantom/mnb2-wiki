[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Volkssturm

Volkssturm is enemy rifle infantry with **100 starting health, no armor and low starting
morale** in historical **2.3.1g**. Its rifle skill still grows with the local
wave at load. Weak starting morale does not make it harmless or give every
encounter a fixed retreat percentage. [Wave-dependent enemy stats](enemy-stats.md)

| Starting field  | Selected load                                               |
| --------------- | ----------------------------------------------------------- |
| Starting health | 100                                                         |
| Armor code      | 0                                                           |
| Rifle skill     | Random integer 0..W−1 divided by 2; W is local wave at load |
| Experience      | 1–20                                                        |
| Morale          | 1–10; replaced by 2 if Assault Expert Award flag > 0        |
| Rank            | 0                                                           |

At W=50, the rifle values range 0..24.5 in half-point steps. A fresh wave value is
an input to load; changing the wave counter does not by itself reroll an already
living soldier. The inspected early spawn loop changes placement coordinates
and rotation, then advances wave counters. A retained observed example below
resolves ordering for one start; other starts still need qualification. [Load and caller evidence](../player-enemy-evidence.md#load-caller-and-later-state-are-different)

On this page: [One retained observed birth example](#one-retained-observed-birth-example) · [Rifle skill is only one of its shooting gates](#rifle-skill-is-only-one-of-its-shooting-gates) · [Pinning and flight are state changes](#pinning-and-flight-are-state-changes)

## One retained observed birth example

An independently reviewed original-runtime recording supplies a concrete case:
the early generator advances local wave from 1 to 2 **before** two new Volkssturm
loads. Both load at wave 2 with health 100 and rifle 0; their XP/morale pairs are
19/3 and 5/4. This confirms the ordering for that fixed start, not every spawn path.

The two matching repeats use one fixed input/profile/seed recipe. They stop the
qualified new behavior at birth/frame-one stop, before later Volks combat. Rifle 0
in those two units is not proof the W=2 formula cannot produce 0.5, or that an old
enemy was rerolled. [Observed context, identities and limits](../shared-results.md)

## Rifle skill is only one of its shooting gates

Its inspected firearm frame first rolls against **10+experience**, then against
rifle skill. An unarmored target can then receive an ordinary-cover save and a
separate bunker save; either can prevent the health subtraction. The damage
draw is 0–99, including zero. Enemy weapon code 1 does not mean it inherits the
allied Springfield's statistics. [Protection rules](defenses.md)

For one illustrative frame visit, fix XP 10 and rifle 20 (both possible at W=50),
a valid armor 0 target and independent integer 0–99 rolls:

| Supplied protection success tests | Chance to reach health-subtraction branch |
| --------------------------------- | ----------------------------------------- |
| Neither                           | 4%                                        |
| Ordinary cover only               | 2%                                        |
| Bunker only                       | 1%                                        |
| Both                              | 0.5%                                      |

Those are conditional source-branch results, not shots per second, kill chances
or measured encounter outcomes. The actual cover geometry, target selection and
number of visits remain separate. [Inputs and exact shot binding](../player-enemy-evidence.md#volks-firearm-and-conditional-example)

## Pinning and flight are state changes

The inspected recovery frame compares a roll with current morale. A passing
comparison pins the actor, then another roll can instead clear pinning and make
it flee. Otherwise it enters a pinned-down animation. An actor already fleeing
can return to that state through another branch. Low morale matters to these
comparisons; it is not a guarantee an approaching unit immediately runs away.
[Recovery branch](../player-enemy-evidence.md#recovery-is-a-visited-branch-not-a-retreat-percentage)

Sources: [Source identities](../player-notes/volkssturm.md#citation-1). [Version and exact evidence](../player-enemy-evidence.md)

A half-point rifle input is preserved by the [strict shot comparison](enemy-stats.md#half-point-rifle-is-not-rounded-down-for-a-shot-test): rifle 0.5 admits the zero roll, while 0 admits none at that one test. The observed rifle 0 births remain pre-combat evidence, not a permanent harmlessness guarantee.
