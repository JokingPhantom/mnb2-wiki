[Player reference](README.md) · [Recruitment](recruitment.md) · [Reading stats](reading-stats.md)

# Airborne healing kit

A **2-TP offer** with a selected recipient write that **sets the kit pool to 25**.
It does not add 25 to an existing pool. Menu qualification, the later payment
and the paratrooper's healing sweep are separate stages in selected 2.3.1g.
[Exact evidence](../healing-kit.md)

| Key fact                   | Selected historical behavior                                            |
| -------------------------- | ----------------------------------------------------------------------- |
| Advertised cost and access | 2 TP; menu scans for a living, noninvincible Paratrooper                |
| Payment                    | Later eligible recipient receipt debits 2 TP                            |
| Pool write                 | Sets pool to 25; does not add 25                                        |
| Patient effect             | Each qualifying visit adds 1 health and spends 1 pool point             |
| Important limit            | Pool admission is outside the patient loop; no guaranteed total healing |

On this page: [The menu and recipient test differ](#the-menu-and-recipient-test-differ) · [Spending is per patient, not per sweep](#spending-is-per-patient-not-per-sweep) · [Rescue credit and squad XP have their own threshold](#rescue-credit-and-squad-xp-have-their-own-threshold)

## The menu and recipient test differ

The offer scans for a living, noninvincible paratrooper and requires at least 2 TP
to set a pending cue. The selected later soldier-button receipt needs health
above 9 and the cue after earlier pending-command priorities. It sets the pool,
debits 2 TP and clears the cue without repeating the menu's type/affordability
checks at those writes. A selected menu is therefore not proof of a completed
purchase or universal recipient eligibility. Cancellation and intervening state
remain separate.

## Spending is per patient, not per sweep

A qualifying healing sweep needs an active nonstock, unpaused paratrooper with
health at least 10, no withdrawal/invincibility/pinning, an expired timer, a
positive kit pool and its random admission test. Patients need health above 0
and below 100, armor 0 and source distance strictly below 50. Each passing visit
adds 1 health and spends 1 pool point. These are source comparisons, not a safe
measured healing radius or a healing rate.

The positive-pool check is outside the patient loop. For a supplied admitted
scan starting with pool 1 and these three qualifying patients, with no other
state changes:

| Patient health before visit | Health after its addition | Pool after its spend |
| --------------------------- | ------------------------- | -------------------- |
| 9                           | 10                        | 0                    |
| 10                          | 11                        | -1                   |
| 99                          | 100                       | -2                   |

The selected loop has no fresh positive-pool guard between those visits.
This conditional overrun is not an observed negative balance or a promise of
more than 25 healing in a real purchase. The guard also has no explicit self
exclusion; actual self-healing still needs the healer's scan membership/state.
[Patient and pool guards](../healing-kit.md#healing-spends-once-for-each-qualifying-scanned-recipient)

## Rescue credit and squad XP have their own threshold

The selected rescue test is health exactly 11 **after** the addition. In the
example, the old-health 10 patient passes it; old-health 9 does not. The branch
increments the career saved-soldier counter and requests the patient's frame 1.
It is not a general “every point is a rescue” rule.

With `medal2` exactly 1, that branch also increments XP across its indexed squad
loop. It is inside each qualifying patient's rescue branch and has no explicit
promotion call there. XP, rank and award display/persistence remain different
state. [Exact medal loop and limits](../healing-kit.md#rescue-branch-and-medal-xp-are-inside-the-patient-loop),
[progression](progression.md)

The selected purchase portrait expression and a later panel refresh spell the
pool field differently. A displayed cross is not yet a qualified exact pool
meter. [Portrait field names](../healing-kit.md#a-portrait-expression-is-not-the-pool)

Sources: [Source identities](../player-notes/healing-kit.md#citation-1). Selected publisher-associated 2.3.1g;
static guards and declared inputs, with no new purchase/healing trial.
