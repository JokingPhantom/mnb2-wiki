[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy rocket soldier

The enemy rocket soldier **looks for armored player units before searching other targets**. That first search chooses a qualifying entry rather than comparing all armored targets for the nearest one.
[Exact target order](../player-enemy-heavy-evidence.md#rocket-load-and-armor-first-target-search)

Historical scope: selected **2.3.1g**.

| Load field      | Selected default                                   |
| --------------- | -------------------------------------------------- |
| Starting health | 100                                                |
| Armor code      | 0                                                  |
| Rifle skill     | Local wave plus random 0–29                        |
| Experience      | 0                                                  |
| Morale          | 0–99; Assault Expert Award separately subtracts 10 |

The first armor pass exits by forcing the scan index to a high sentinel value. It needs positive health, line of sight and positive armor.
Its predicate does not repeat the fallback search's visibility, invincibility,
pillbox or distance filters. A selected target and permitted explosives are
still needed to request the firing animation. Target selection and the later
rocket's eligible blast recipients are separate stages.
[AT and vehicle health](anti-tank-and-vehicles.md)

On this page: [A high rifle load does not describe the launch comparison](#a-high-rifle-load-does-not-describe-the-launch-comparison) · [Low health and pause do not use one universal enemy rule](#low-health-and-pause-do-not-use-one-universal-enemy-rule)

## A high rifle load does not describe the launch comparison

The later navigation check loops on a draw greater than experience, or on pause.
With the selected XP-0 load and supplied unpaused state, only draw 0 out of
0–99 avoids this loop request on one visit. That is not a measured firing rate.
The selected launch copies position and facing into the shared rocket template;
it does not use the rifle field to calculate an accuracy percentage or scatter.
[Exact navigation and launch](../player-enemy-heavy-evidence.md#rocket-navigation-and-launch-do-not-read-loaded-rifle)

The launch also lacks the allied Bazooka action's explicit rocket-owner copy.
The shared flight code uses an owner field to choose its scan branch, so a full
initialized trace is needed to close enemy projectile ownership and recipients.
This is not evidence that the enemy rocket is harmless or a qualified copy of
every allied Bazooka behavior. [Rocket sampling and event order](../bazooka-detonation.md)

Sources: [Source identities](../player-notes/enemy-rocket-soldier.md#citation-1)

## Low health and pause do not use one universal enemy rule

At a separately supplied health of exactly 1, the inspected rocket soldier's
controller skips its movement/action chain, whose extra health test requires
more than 1. The enemy Mortar's corresponding chain accepts that supplied value.
That does not make a one-health rocket soldier harmless: its later reached firing
action has separate death-navigation and emission statements, with actual
navigation behavior still unresolved.

The two controllers also place their corpse-counter code under different pause
guards. A paused visual observation cannot establish a common corpse lifetime
or update schedule for both roles.
[Exact supplied-health and pause comparison](../player-enemy-heavy-evidence.md#rocket-and-mortar-controller-health-and-pause-gates-are-not-interchangeable)

Its inspected firing action also begins by increasing **shot**, the counter used
for the results screen's player accuracy denominator, rather than enemyShots.
With other supplied totals unchanged, that alone lowers a positive hit/shot
ratio without changing the selected base score. Actual firing/effect/counter
sequences are not certified by this field join.
[Counter and results-reader comparison](../shot-hit-statistics.md#an-enemy-rocket-action-writes-the-results-shot-denominator).
Additional source: [Source identities](../player-notes/enemy-rocket-soldier.md#citation-2)
