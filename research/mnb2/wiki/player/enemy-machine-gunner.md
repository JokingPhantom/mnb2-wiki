[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy machine gunner

The enemy machine gunner sets up before firing and uses a **burst counter that also changes its accuracy comparison**. Its loaded rifle skill alone cannot describe
every shot, and the allied Machine gunner's weapon statistics do not substitute
for this enemy's attacks.
[Exact source stages](../player-enemy-mg-evidence.md#frame26-admission-frame27-shot-and-frame30-continuation)

Historical scope: selected **2.3.1g**.

| Load field      | Selected default                                   |
| --------------- | -------------------------------------------------- |
| Starting health | 100                                                |
| Armor code      | 0                                                  |
| Rifle skill     | Random 0 through local wave minus 1, divided by 2  |
| Experience      | 1–50                                               |
| Morale          | 0–99; Assault Expert Award separately subtracts 10 |
| Setup counter   | 0–399; source units, not seconds                   |
| Action timer    | 0–199; source units, not seconds                   |

On this page: [Movement ends at a setup transition](#movement-ends-at-a-setup-transition) · [Later burst visits can have a less severe accuracy penalty](#later-burst-visits-can-have-a-less-severe-accuracy-penalty) · [Cover, crew and pinning still matter](#cover-crew-and-pinning-still-matter)

## Movement ends at a setup transition

Its ordinary forward movement needs a positive setup counter as well as the
movement, pin and aiming guards. The controller counts a positive setup counter
down without its own pin/aiming check. Reaching 0 writes a sentinel value and
requests setup. An initial 0 follows a different branch and does not make that
same setup request. Pinning therefore does not, from these statements alone,
freeze the setup counter. [Exact boundaries](../player-enemy-mg-evidence.md#load-movement-and-setup-boundaries)

## Later burst visits can have a less severe accuracy penalty

A selected nonmelee target starts burst at 3–32. The shot frame compares a fresh
integer 0–99 draw against rifle skill minus three times the current burst.
For a declared rifle 40, the threshold is 40−3×current burst. At burst 10, this is 10, admitting draws 0–9:

| Current burst | Passing draws out of 100 at this comparison |
| ------------- | ------------------------------------------- |
| 20            | 0                                           |
| 10            | 10                                          |
| 3             | 31                                          |
| 1             | 37                                          |

The continuation frame reduces the counter and can return to the shot frame;
that makes this penalty smaller if the path continues. The earlier experience
navigation test is another stage. These values are **conditional comparison
counts**, not the probability a battle, complete burst or second of firing hits.
[Exact repeat path and inputs](../player-enemy-mg-evidence.md#frame26-admission-frame27-shot-and-frame30-continuation)

## Cover, crew and pinning still matter

For an unarmored target after accuracy passes, ordinary cover and bunker have
separate saves; if both queries are true, their conditional unsaved fraction is
12.5%: 1/2 ordinary-cover failure × 1/4 bunker failure = 1/8. That does not certify any particular layout. Armor 1 uses crew handling,
while armor 2 goes to a ricochet branch. An accuracy failure can request pinning
without incrementing the inspected enemy-hit counter.
[Defenses](defenses.md), [vehicle health and crew](anti-tank-and-vehicles.md)

Recovery also distinguishes whether setupCounter is still positive, requesting
different stopped frames. Full animation scheduling and first-shot/retarget time
remain unresolved. [Recovery binding](../player-enemy-mg-evidence.md#recovery-destination)

Sources: [Source identities](../player-notes/enemy-machine-gunner.md#citation-1)

## A wave label alone does not determine a later shot comparison

Starting rifle skill and the current burst counter are separate inputs to a later shot. The linked wave examples are not observed hit rates. An animation request for pinning is also separate from a direct pin-field assignment or completed suppression outcome.

[Full source comparison and limitations](../player-notes/enemy-machine-gunner.md#a-wave-label-alone-does-not-determine-a-later-shot-comparison).
