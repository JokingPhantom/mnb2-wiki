[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy paratroopers

Enemy paratroopers have a **landing and readiness sequence
before ordinary combat**. The plane assigns starting positions across x 0–400 and
y 0–499, rather than a single fixed top-edge row. Those source coordinates do
not certify the observed position or health of every actual drop.
[Exact plane and actor stages](../player-enemy-para-evidence.md#plane-caller-and-actor-load-are-different-stages)

Historical scope: selected **2.3.1g**.

| Load field      | Selected default                                   |
| --------------- | -------------------------------------------------- |
| Starting health | 100 before landing and later changes               |
| Armor code      | 0                                                  |
| Rifle skill     | Random 0 through local wave minus 1, divided by 2  |
| Experience      | 10–59                                              |
| Morale          | 0–99; Assault Expert Award separately subtracts 10 |

On this page: [Trees can cause more than one injury roll](#trees-can-cause-more-than-one-injury-roll) · [The initial timer is not its complete reaction time](#the-initial-timer-is-not-its-complete-reaction-time)

## Trees can cause more than one injury roll

The landing action scans decorations and can subtract 0–99 health for each
qualifying tree overlap. It does not stop after one tree. A declared one-tree
99-point injury leaves health 1; two 60-point injuries take 100 to −20. Those
examples are not measured landing odds or a safe tree-spacing rule.

The later enemy actor checks differ from the allied Paratrooper's usable-health
rule: these enemy frame/controller guards accept positive health, so 1–9 is not
rejected by those guards alone. Actual playback and subsequent damage still
matter. [Exact injury and health boundaries](../player-enemy-para-evidence.md#drop-tree-injury-and-readiness-writers)

## The initial timer is not its complete reaction time

The caller and load both write a timer of 999, but later drop/readiness actions
write 9999, then 999 and eventually a random 0–99 timer on another branch.
Separate animation loops and aiming writes intervene. Dividing the initial
counter by nominal movie FPS would miss those later writers and their timing.

Its ordinary ready-action branch uses a 70-of-100 comparison before target
selection. The firearm's experience navigation, rifle comparison, cover saves
and semi-repeat path remain separate stages. Ordinary cover and bunker use the
selected 50/75 save pattern after accuracy passes, with actual geometry still
unresolved. [Exact firearm stages](../player-enemy-para-evidence.md#target-acquisition-and-firearm-continuation)

The [allied Paratrooper](paratroopers.md) has different purchase, profile and
landing/control rules. A shared role name does not merge the two actors.

Sources: [Source identities](../player-notes/enemy-paratroopers.md#citation-1)

The [conditional one/two-injury comparison](../paratrooper-landing.md#one-or-two-reached-injury-writes-have-different-health-input-counts)
keeps that positive-health test separate from the Allied actor's later
health-at-least-ten requirement. With supplied initial health 100 and two reached
independent injury writes, 50.5% of the declared input pairs remain positive and
41.86% remain at least ten. Neither is an observed drop-survival rate; actual
tree overlaps, later actor state and callbacks are still unresolved.
