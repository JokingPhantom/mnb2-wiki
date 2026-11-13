[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy Regular and Jugend infantry

Regular and Jugend are enemy rifle infantry. Their starting rifle skill grows with the local wave,
but **their targeting and firing stages differ**. Jugend can pass its inspected
health filter for a 1–9-health player target; the Regular's >9 filter rejects
that same supplied health. Both still need their other target guards.
[Exact controller comparison](../player-regular-jugend-evidence.md#load-and-target-health-differences)

Historical scope: selected **2.3.1g**.

| Load field                        | Enemy Regular                                     | Jugend                               |
| --------------------------------- | ------------------------------------------------- | ------------------------------------ |
| Starting health                   | 100                                               | 100                                  |
| Armor code                        | 0                                                 | 0                                    |
| Rifle skill                       | Random 0 through local wave minus 1, divided by 2 | Same initializer                     |
| Experience                        | 1–50                                              | 1–30                                 |
| Morale                            | Random 0–99                                       | 70                                   |
| Assault Expert Award morale write | Subtract 10                                       | Subtract 10, giving 60 from the base |

The rifle field alone cannot rank their actual firing. Actor-specific navigation,
attempt, repeat and protection checks still matter. [Enemy stats](enemy-stats.md)

On this page: [Regular has an extra local firing-attempt test](#regular-has-an-extra-local-firing-attempt-test) · [Repeats and morale need their own context](#repeats-and-morale-need-their-own-context)

## Regular has an extra local firing-attempt test

Both have an earlier experience-based navigation comparison. In the later shot
frame, Regular additionally tests a draw below 10 plus experience before its
rifle comparison. Jugend's inspected shot frame has no such extra attempt test.

For a declared **XP 20, rifle 20, one reached shot-frame visit and a valid
unarmored target**, independent uniform draws give:

| Supplied protection results       | Regular reaches health-subtraction branch | Jugend reaches it |
| --------------------------------- | ----------------------------------------- | ----------------- |
| Neither ordinary cover nor bunker | 6%                                        | 20%               |
| Both queries true                 | 0.75%                                     | 2.5%              |

For Regular without saves, (10+20)/100 attempt × 20/100 accuracy = 6%. Jugend has only the 20/100 accuracy term at this stage. With both saves true, multiply each by 1/2 × 1/4. Those counts include the later attempt/accuracy/save branches only. They are
not a first-shot rate, kill probability or comparison across a whole encounter.
The damage draw can be zero, and a particular layout must actually satisfy
the protection queries. [Inputs and exact stages](../player-regular-jugend-evidence.md#frame8-navigation-is-not-the-only-xp-gate-for-regular)

## Repeats and morale need their own context

Jugend initializes a 1–4 semi counter for its selected nonmelee route. Its
continuation can request playback from before the experience comparison;
Regular's inspected return frame simply stops at its ordinary state and clears
aiming. Full scheduling and target changes remain unresolved.

The shared-shaped recovery comparison uses each actor's current morale.
For Jugend's unchanged base 70, 29 of 100 inputs take its pin/loop branch on
one reached recovery visit; morale 60 admits 39. That is not a universal
suppression or retreat probability. [Recovery bindings](../player-regular-jugend-evidence.md#continuation-and-recovery-also-differ)

Sources: [Source identities](../player-notes/enemy-regular-and-jugend.md#citation-1)

## Their ready timers do not reset on identical visits

Regular and Jugend do not reset their action timers under identical pin/search conditions. Death requests, kill accounting and fading are separate stages. The linked comparisons do not establish a first-shot race, duplicate-kill bug or paused-fade outcome; half-point rifle inputs also need their actual shot comparison.

[Full source comparison and limitations](../player-notes/enemy-regular-and-jugend.md#their-ready-timers-do-not-reset-on-identical-visits).

## A death helper, kill write and fading are different stages

[Full source comparison and limitations](../player-notes/enemy-regular-and-jugend.md#a-death-helper-kill-write-and-fading-are-different-stages).
