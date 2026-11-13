[Player reference](README.md) · [Support](support.md) · [Tactical points](tactical-points.md)

# Recovering a downed pilot

A qualifying friendly pickup grants the **collector 3 XP and 1 TP**, alongside a
career pilot-recovery addition. Enemy pickup instead subtracts 1 TP. Getting a
soldier or vehicle near a drawn pilot is not by itself a reward receipt: the
selected 2.3.1g source has separate arrival, proximity and removal stages.
[Exact source and limits](../player-pilot-recovery-evidence.md)

Historical scope: selected **2.3.1g** source.

| Key fact           | Selected historical behavior                                                                   |
| ------------------ | ---------------------------------------------------------------------------------------------- |
| Friendly collector | Defined health at least 10, strict helper distance below 50; no role/armor filter at this gate |
| Friendly reward    | Collector +3 XP and promotion check; player +1 TP and career recovery count                    |
| Enemy pickup       | Positive-health enemy, strict distance below 50; subtracts 1 TP                                |
| Main limit         | Approach, collection and final removal/accounting are separate                                 |

On this page: [Pilot collection uses its own eligibility and rewards](#pilot-collection-uses-its-own-eligibility-and-rewards) · [Move a usable collector close enough](#move-a-usable-collector-close-enough) · [The enemy can secure it too](#the-enemy-can-secure-it-too) · [Arrival and career credit are different stages](#arrival-and-career-credit-are-different-stages) · [The Ribbon's advertised extra-TP gift remains unqualified](#the-ribbons-advertised-extra-tp-gift-remains-unqualified) · [Blast cleanup has another path before collection](#blast-cleanup-has-another-path-before-collection)

## Pilot collection uses its own eligibility and rewards

The inspected friendly collection gate does not require a Medic, Engineer or
particular infantry role, and has no armor restriction there. It needs a valid
indexed collector with the health and proximity conditions below. This is not
ordinary healing or a roll from the crate reward table.
[Exact pilot receipt](../player-pilot-recovery-evidence.md), [crate comparison](crates.md).

Budget from the supported **direct +1-TP write** at a qualifying friendly pickup,
not the Ribbon description's unqualified possible 5-TP gift. The collector's XP,
career counter and later award/save state remain separate. Enemy pickup has its
own TP subtraction. No particular drawing or close approach proves a receipt.
[Description versus inspected receipts](../player-pilot-recovery-evidence.md#the-advertised-five-tp-ribbon-gift-is-not-established-by-these-receipts).

## Move a usable collector close enough

The selected player scan needs defined health **at least 10** and strict helper
distance **below 50**. It does not require an Engineer, Medic or particular infantry
role at that gate, nor does it add an armor restriction. Actual geometry and
movement still matter; these source distances are not a measured screen stencil.
A player at health 9 fails this collection-health test, while 10 passes it.

The +3 XP belongs to the eligible collector and is followed by a promotion check,
not an automatic squad-wide bonus or guaranteed new rank. The TP and career
counter additions are separate writes. [XP and rank](progression.md)

## The enemy can secure it too

The enemy scan uses health **above 0** and its own strict distance<50 test.
Its pickup branch displays a secured-pilot message and directly subtracts 1 TP.
Do not assume positive allied health alone meets the same threshold, or that
a pilot is harmless to leave simply because the enemy is wounded.

The player scan precedes the enemy scan in these actions, but removal/callback
semantics are still unqualified. No guaranteed tie winner, one-pilot/one-reward
count or safe paused pickup follows from that source ordering.

## Arrival and career credit are different stages

A later crash action can request a pilot at separately randomized coordinates;
its selected emission does not use the visible crash object's point. Another
arrival action creates the ground pilot. This is not a guaranteed pilot after
every aircraft destruction or proof of where a particular drawing will land.

The **Search and Rescue Ribbon** checks a career pilot counter at least 100 with
its award flag unset and the earlier display/ordering conditions. That is a
counter threshold, not a verified 100-unique-rescues or immediate-save promise.
[Career award source](../award-reference.md)

Source: [Source identities](../player-notes/pilot-recovery.md#citation-1). Original selected-version player explanation;
no new rescue, pause, reward, geometry or storage trial.

## The Ribbon's advertised extra-TP gift remains unqualified

Its description claims a 1% chance of a later pilot giving 5 TP, but the two inspected
pickup actions directly add 1 TP and contain no Ribbon-flag test or five-point
grant. The accepted dependency audit found no supported positive gameplay-effect
reference for that description. This is a bounded source finding, not proof
against every possible runtime/counter-driven effect.
[Description versus direct receipt](../player-pilot-recovery-evidence.md#the-advertised-five-tp-ribbon-gift-is-not-established-by-these-receipts).

## Blast cleanup has another path before collection

A shared blast's scenery scan can send a qualifying pilot-type decoration to
the gib helper and its removal request. That route is separate from friendly
recovery XP/TP and from the enemy-secured TP subtraction. It does not prove
which callback wins when collection and an effect are both pending.
[Exact pilot/crate cleanup comparison](../player-pickup-blast-evidence.md).
Additional source: [Source identities](../player-notes/pilot-recovery.md#citation-2)
