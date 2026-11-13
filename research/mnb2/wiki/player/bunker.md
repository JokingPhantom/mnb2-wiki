[Player reference](README.md) · [Defenses](defenses.md) · [Construction](construction.md)

# Bunker

A **5-TP engineer construction** with a separate bunker-protection query.
For several enemy firearm paths, a target classified as bunkered has a **75%
chance to save an otherwise accurate shot**. Adding qualifying ordinary cover
can supply a separate save, but the German Sniper path is an important exception.
[Bullet protection and stacking](defenses.md)

| Property                    | Supported fact                                                                    |
| --------------------------- | --------------------------------------------------------------------------------- |
| Base menu price             | 5 TP                                                                              |
| Construction                | Select the bunker order and its placement pointer; completion is a separate stage |
| Protection query            | Object overlap with a decoration typed bunker or pillbox                          |
| Ordinary enemy firearm save | 75%, conditional on this query and the selected shooter path                      |
| German Sniper exception     | Inspected Sniper path does not perform the bunker save                            |

The overlap helper is not a test that the soldier's center sits inside a drawn
floor plan. Nor is it a fixed damage multiplier or immunity switch. Its own
scan has no structure-health condition; structure removal and lifecycle still
matter before concluding what a destroyed object does.
[Overlap source explanation](../bunker-overlap.md)

Historical scope: selected **2.3.1g** source; the stated saves and placement
checks are conditional, not a certified protected layout.

On this page: [Can the occupant still do its job?](#can-the-occupant-still-do-its-job) · [What to watch when placing it](#what-to-watch-when-placing-it) · [Limits against other attacks](#limits-against-other-attacks) · [A too-close Bunker message is a separate placement test](#a-too-close-bunker-message-is-a-separate-placement-test)

## Can the occupant still do its job?

**Bullet protection and permission to act are separate checks.** These selected
**2.3.1g** comparisons assume the bunker query succeeds and all other relevant
conditions are supplied; they do not identify a tested spot within the artwork.

- **[Medic healing](medic.md).** No direct bunker exclusion in the selected healing entry; the Medic and patients still need to qualify
- **[Mechanic repair](mechanic.md).** The required not-bunkered condition fails, so this repair entry is unavailable
- **[Officer aid](officer.md).** The bunker alternative needs an extra random-below-15 result; this is not guaranteed periodic aid
- **[Mortar target search](mortar.md).** Requires not bunkered; a qualifying Scout or Sarge does not bypass that condition
- **[Machine gunner target search](machine-gunner.md).** Does not repeat ordinary infantry's extra bunker-dependent random check; other readiness and target conditions remain

[Medic, Mechanic and Officer comparison](specialists-under-cover.md),
[Mortar sight and protection gates](specialists-under-cover.md#spotting-does-not-override-a-mortars-protection-gate),
[Gunner acquisition evidence](../player-gunner-path-evidence.md#this-ready-search-has-no-ordinary-extra-bunker-chance).

A [Pillbox](pillbox.md) also belongs to the palisade classification. That earlier
gate can block Officer aid even if the separate bunker random result would pass.
Do not treat every bunker-shaped structure as the same ability check.
[Pillbox comparison](specialists-under-cover.md#a-pillbox-is-not-just-the-officers-bunker-coin-flip).
These entry conditions do not establish what happens to an action already
underway, an instant restart after relocation or a universal firing-rate bonus.

## What to watch when placing it

The selected built-bunker load clamps its center coordinates to x **50–350**
and y **50–550** in source coordinates. A placement near the edge can therefore
be adjusted by that initializer. These numbers are not measured interior-safe
zones or a guarantee that every occupant fits the protection test.
[Placement bindings](../player-defense-evidence.md#structure-bindings)

The community describes slower firing for several occupants and a gunner-specific
benefit, plus restrictions on mortars, bazookas and hand grenades. Those effects
need the particular soldier and weapon path; the bullet-save percentage alone
does not settle their net effectiveness. [Archived Bunker comparison](../bunker.md)

## Limits against other attacks

A selected fragmentation branch can exclude an ordinary unarmored bunkered
recipient, while retaining an armored alternative and other distance/LOS/health
gates. Bazooka backblast uses a separate region test without the bunker condition
in its cited health-damage rows. Neither is covered by one universal protection
percentage. [Fragmentation](../fragmentation-blast.md), [backblast](../bazooka-backblast.md)

The legacy guide's close-packed “invincible bunker” exploit is described as
pre-2.3. Do not use that older strategy as proof of immunity in selected 2.3.1g.
The community also warns about flames and direct large-explosive hits; exact
outcomes and protected layouts remain open. [Version-qualified archive](../bunker.md)

Sources: [Source identities](../player-notes/bunker.md#citation-1). Selected 2.3.1g; [evidence notes](../player-defense-evidence.md).

See [explosions and fortifications](explosions-and-fortifications.md) for the
separate structure-removal and occupant-protection queries.

The [Gunner admission comparison](machine-gunner.md#bunkered-acquisition-differs-from-ordinary-infantry) now binds one offensive distinction: its selected ready search omits the ordinary extra bunker chance, while other gates remain. This is not a complete bunker damage or fire-rate multiplier.
Additional source: [Source identities](../player-notes/bunker.md#citation-2)

## A too-close Bunker message is a separate placement test

The selected completion scans existing **bunker-type** decorations and tests
pointer-clip distance strictly below 120 before its fee/clone branch. At supplied
helper distance 119 that candidate blocks;120 alone does not. This is a source
predicate, not a measured final-building spacing stencil. The test has no local
structure-health or opacity filter.

The new clone later receives root mouse coordinates, while its separate load
clamps whichever own coordinates it sees. Pointer tracking, load/caller order
and final transforms still need qualification; the 50–350/50–550 load bounds are
not automatically a final mouse-placement or occupant-safe rectangle.
[Exact three-stage comparison](../player-construction-placement-evidence.md).
Additional source: [Source identities](../player-notes/bunker.md#citation-3)
