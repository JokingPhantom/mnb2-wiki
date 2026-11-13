[Player reference](README.md) · [Defenses](defenses.md) · [Construction](construction.md)

# Keeping specialist abilities usable under cover

**A protected position can still prevent a specialist from doing its job.** In
selected **2.3.1g**, the Mechanic's repair entry excludes bunker and palisade
classifications; the Medic's selected healing entry has neither direct check.
The Officer and Sarge have different rules again. Read the role's ability
conditions alongside the [bullet protection](defenses.md) you want to obtain.
[Medic conditions](../player-medic-controller-evidence.md#movement-and-healing-have-different-guards),
[Mechanic conditions](../mechanic.md).

The role's other actor-state, counter and recipient conditions still matter. A
Medic lacking those two cover checks does not make every visible protected
position a tested healing spot, and changing cover does not prove an action
immediately restarts. The comparisons below keep those boundaries explicit.

On this page: [The same supplied classification affects roles differently](#the-same-supplied-classification-affects-roles-differently) · [A Pillbox is not just the Officer's bunker coin flip](#a-pillbox-is-not-just-the-officers-bunker-coin-flip) · [Spotting does not override a mortar's protection gate](#spotting-does-not-override-a-mortars-protection-gate) · [Admission is not a promise to interrupt or resume an action](#admission-is-not-a-promise-to-interrupt-or-resume-an-action)

## The same supplied classification affects roles differently

The following compares **selected controller entry**, with every other actor,
timer and recipient condition assumed satisfied. It does not certify that a
particular visible position produces either classification.

| Action                         | If bunker query is true                                    | If palisade query is true                           |
| ------------------------------ | ---------------------------------------------------------- | --------------------------------------------------- |
| [Mechanic repair](mechanic.md) | Its required bunker-false gate fails                       | Its earlier palisade-false gate fails               |
| [Officer aid](officer.md)      | Its alternative needs an extra random-below-15 result      | Its earlier palisade-false gate fails               |
| [Medic healing](medic.md)      | No direct bunker query in the selected controller          | No direct palisade query in the selected controller |
| [Sarge support](sarge.md)      | No separate bunker gate around the selected support choice | Its earlier palisade-false gate fails               |

The Medic row does not mean healing ignores its own state. It still needs a
usable active Medic, not pinned or flagged invincible, an expired counter and eligible
patients. Its movement checks are another block. Mechanic repair has its own
vehicle-type, health and distance requirements. Officer aid also needs its
separate XP/random, melee and shared-counter conditions.
[Medic entry](../player-medic-controller-evidence.md#movement-and-healing-have-different-guards),
[Mechanic entry](../player-mechanic-combat-evidence.md#a-successful-repair-scan-takes-priority-over-new-acquisition),
[Officer entry](../officer-aid.md#entry-depends-on-several-actor-and-shared-states)

## A Pillbox is not just the Officer's bunker coin flip

The classification helpers recognize [Pillbox](pillbox.md) overlap in both the
bunker and palisade families. If both supplied classifications are true, the
Officer fails the earlier palisade-false gate; a passing bunker random result
does not override it. The Mechanic also fails its repair entry. The Medic's
selected direct healing gates do not acquire those checks from the other roles.

This is a conditional rule comparison, not a recommendation for an exact tile,
edge or overlap. The bunker helper's object test differs from ordinary cover's
point test. Actual transforms, surviving structures and caller state still need
to be checked before assigning the table to an on-screen layout.
[Classification/query forms](../player-construction-detail-evidence.md#ordinary-cover-and-classification-use-different-call-forms)

## Spotting does not override a mortar's protection gate

A qualifying [Scout or Sarge](mortar.md#a-scout-or-sarge-can-satisfy-one-sight-alternative)
can satisfy the Mortar soldier's selected sight alternative. That does not
remove its not-bunkered search gate, its strict target-distance-above-400
condition or the later firing request's camouflage check. A spotter, a mortar
pit, a bunker and a net serve different mechanisms.
[Exact mortar guards](../player-mortar-acquisition-evidence.md).

Likewise, ordinary-cover plus bunker bullet saves do not establish permission
to perform an ability. Those rolls belong to particular enemy shots, and their
exceptions still matter. [Defense stacking](defenses.md), [concealment](concealment.md)

## Admission is not a promise to interrupt or resume an action

These comparisons concern the selected ready/search/heal branches. They do
not prove that adding or removing a structure cancels an animation already
underway, refunds an order or instantly restarts an action. Recipient lifetime,
callback order and the later effect body remain separate. Use the individual
role pages for those supported stages and remaining gaps.

Sources: [Source identities](../player-notes/specialists-under-cover.md#citation-1).
Original synthesis of linked selected-source facts; no new cover layout or timing trial.

Sarge's selected support admission tests withdrawal but has no own morale/flee
read in that controller. His group rally still needs its own target health,
armor, pinning, invincibility and distance conditions; it does not reset every
recipient combat field. This actor exception does not supply a safe protected
placement or immunity to other fear/pinning paths.
[Exact Sarge admission and rally scope](../player-sarge-support-evidence.md#sarge-rally-is-not-a-morale-boost-or-ordinary-pin-recovery)
Additional sources: [Source identities](../player-notes/specialists-under-cover.md#citation-2)
