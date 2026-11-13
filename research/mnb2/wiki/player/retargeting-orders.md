[Player reference](README.md) · [Orders](orders.md) · [Shooting stages](how-shooting-works.md)

# Concentrate Fire and All Around Defense

**Concentrate Fire supplies one chosen target; All Around Defense builds a
separate eligible-target pool for each recipient.** Both then separate a broad
target-field assignment from narrower animation requests. Neither source step
by itself proves a soldier fired immediately or bypassed a reload.
[Concentrate Fire evidence](../concentrate-fire.md),
[All Around Defense evidence](../all-around-defense.md)

Historical scope: selected **2.3.1g** source.

On this page: [Choose the target-selection behavior](#choose-the-target-selection-behavior) · [A target update can happen without the forced animation](#a-target-update-can-happen-without-the-forced-animation) · [Sight direction and later timing still matter](#sight-direction-and-later-timing-still-matter)

## Choose the target-selection behavior

| Order stage             | Concentrate Fire                                                                                               | All Around Defense                                                                 |
| ----------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Offer                   | Eligible Officer; concentrate counter at most 1; pending target choice                                         | Eligible Officer and at least 1 TP; debit precedes helper                          |
| Target input            | One chosen positive-health enemy through a matched target handler                                              | Each living recipient's newly built pool of living, visible, LOS-qualified enemies |
| Assignment              | Chosen reference assigned to recipients with health above 9                                                    | Random pool entry assigned only when that recipient's pool is nonempty             |
| Counter / payment limit | No direct TP debit in that inspected offer; later positive-target path writes 60, or 30 with medal29 exactly 1 | No shot-confirmation or empty-pool refund stage in the selected offer/helper sites |

The **Infantry Specialist Ribbon** is the selected medal 29 field. When that
stored flag equals 1, the positive-target Concentrate Fire helper overwrites
its counter 60 with **30**. This is a counter benefit at that source stage,
not a certified 30-second cooldown or proof that anyone fired.
[Award identity](../award-reference.md),
[Exact override and target condition](../concentrate-fire.md#cooldown-writes-depend-on-the-selected-target)

The Officer admission scans use specialization 2, health above 10 and invincible
not 1. These are source offer guards, not tested keyboard parity or permission
for every possible menu state. Concentrate's counter threshold includes 1; it
is not an only-at-zero check. Its later target helper does not repeat the offer's
Officer/counter check. That is not a demonstrated stale-order exploit.

All Around Defense rebuilds each recipient's pool. The selected predicates have
no explicit armor, invincibility, weapon-code or distance filter for candidates,
while positive health, visibility and LOS still apply. Separate recipients can
select the same enemy; the helper does not reserve a unique target for each.
[Exact pool construction](../all-around-defense.md#the-helper-rebuilds-a-pool-before-drawing)

## A target update can happen without the forced animation

For a reached broad assignment with valid target inputs, compare these supplied
recipient states. All Around Defense additionally needs that recipient's pool
nonempty:

| Recipient state               | Broad target assignment | Later forced-animation gate                               |
| ----------------------------- | ----------------------- | --------------------------------------------------------- |
| Health 9                      | Not admitted            | Not reached through this recipient branch                 |
| Health 100, armor 1           | Can be written          | Armor gate fails                                          |
| Health 100, armor 0, pinned 1 | Can be written          | Pinning gate fails                                        |
| Health 100, armor 0, unpinned | Can be written          | Other type/protection/sight/navigation guards still apply |

The later subset requires armor below 1, type different from the literal
`playerGruntFlamer`, invincible not 1 and pinned not 1. Preserve that exact type
selector rather than substituting a display name. Concentrate then has a
separate sight test. A qualifying non-mggrunt, or mggrunt with setup below 100,
is sent to frame 2; the other mggrunt branch goes to 59. These are navigation
requests into actor-specific behavior, not projectile creation.
[Assignment versus animation](../concentrate-fire.md#assignment-precedes-the-stricter-animation-gates)

## Sight direction and later timing still matter

All Around Defense's pool calls sight from recipient toward enemy. Concentrate's
later test supplies the chosen enemy first and recipient second. The selected
sight helper samples points; reverse directions cannot simply be declared
geometrically equivalent without qualification. Target selection and later
actor callbacks can also read different state.

These selected animation guards do not explicitly test current ammo, aiming or
actionTimer. Their absence does not prove every weapon fires, reloads disappear,
or damage occurs. Concentrate's counter writes do not require a confirmed shot,
and its counter 60/30 has not been calibrated as seconds here. A dead chosen
target takes another helper branch, clearing pending state without those same
counter writes. [Cooldown and cleanup](../concentrate-fire.md#cooldown-writes-depend-on-the-selected-target),
[ordinary shooting stages](how-shooting-works.md)

Sources: [Source identities](../player-notes/retargeting-orders.md#citation-1).
Selected publisher-associated 2.3.1g; original source-based comparison and supplied
recipient states, with no new order, reload, distribution or geometry trial.

Additional source: [Source identities](../player-notes/retargeting-orders.md#citation-2)
