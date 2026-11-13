[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Role comparison](recruitment.md#choose-the-job-before-the-price)

# Mortar soldier

An **8-TP soldier for attacking distant enemies with explosions**. It needs to
finish setting up and find a qualifying target; a nearby enemy or a spotter alone
does not make it fire. This recruit is separate from the [Mortar pit](mortar-pit.md)
construction. [Target and setup evidence](../player-mortar-acquisition-evidence.md)

Its attack places an explosion around the selected enemy's position, with a
random offset on each axis. The selected action does not simulate a separate
shell flying to that point. The scatter and later explosion checks mean an
attack is not a guaranteed hit on that enemy. [Mortar chain](../mortar-soldier.md)

Applies to **historical selected 2.3.1g**. Starting facts use the ordinary load;
career additions and other conditions are labeled separately.

| Key fact                 | Selected ordinary load                                                            |
| ------------------------ | --------------------------------------------------------------------------------- |
| TP cost and availability | 8 TP; Reinforcements                                                              |
| Health                   | 100                                                                               |
| Rifle skill field        | Starts at 1 with random-stop 1–10 additions; not a complete mortar-hit percentage |
| Morale                   | 10–19 before career bonuses                                                       |
| Experience               | 0 before career bonuses                                                           |

[Starting-stat evidence](../player-roster-evidence.md)

On this page: [What to check if the mortar is silent](#what-to-check-if-the-mortar-is-silent), [Setup, minimum target distance and camouflage matter](#setup-minimum-target-distance-and-camouflage-matter), [A Scout or Sarge can satisfy one sight alternative](#a-scout-or-sarge-can-satisfy-one-sight-alternative), [The large reset counter is not a measured firing interval](#the-large-reset-counter-is-not-a-measured-firing-interval), [The enemy mortar does not use your setup sequence](#the-enemy-mortar-does-not-use-your-setup-sequence).

## What to check if the mortar is silent

- **Setup and movement:** its selected search needs setup above 100. A movement
  attempt can reset that state even if an obstacle prevents translation; a still
  image does not prove setup is complete.
- **Target and protection:** the selected target must be strictly farther than
  400 source units, with the other target guards passing; bunker classification
  also blocks this search.
- **Spotter limits:** a qualifying Scout or Sarge can satisfy one sight
  alternative, but not remove the distance, visibility or later camouflage rules.

[Exact setup, target and sight evidence](../player-mortar-acquisition-evidence.md).
This **8-TP soldier** is separate from a [Mortar pit](mortar-pit.md) construction.
The distances and setup state are selected **2.3.1g** conditions, not a safe
impact radius, calibrated placement or measured time to fire.

The selected attack action places its effect at target x plus a random integer
**−150 through 149**, and target y plus another such offset. Those independent
axis expressions describe a square coordinate-offset space, not a guarantee of
a circular accuracy radius or a measured impact distribution.
[Placement bindings](../player-roster-evidence.md#mortar-and-flame)

The later effect calls the explosion helper with separate gib, AT, fragment and
damage arguments 25, 5, 75 and 50. The final 50 is a damage argument, not 50 guaranteed
health loss to every nearby actor. Protection, armor, proximity and helper
special branches remain necessary. [Explosion/AT distinctions](anti-tank-and-vehicles.md)

The mortar soldier, enemy mortar actor and mortar-pit construction are different
source entities. A structure name or community firing restriction should not be
applied to all three without checking the actual actor/recipient path.
Complete target/callback timing, friendly-fire handling, effect activation and firing
cadence remain open; no universal rounds-per-second or kill radius is certified.

Sources: [Source identities](../player-notes/mortar.md#citation-1).
Selected 2.3.1g; [exact evidence](../player-roster-evidence.md).

## Setup, minimum target distance and camouflage matter

The selected target-search path needs setup above 100, expired action counter,
usable live/unpaused actor state, no pinning and no bunker classification.
A movement-attempt block resets setup to−100 even when its obstacle test blocks
translation. Stationary setup and successful physical movement are different
questions; no fixed setup time in seconds follows from the counter.
[Setup source](../player-mortar-acquisition-evidence.md#setup-is-its-own-state-before-target-acquisition)

Candidates still need to be **strictly farther than 400 source distance units**,
plus health, visibility, armor/crew and other target checks. Exactly 400 fails
this acquisition test. This is not a safe blast radius or a prohibition on an
effect later landing closer to another actor.

## A Scout or Sarge can satisfy one sight alternative

The mortar checks for a player actor with specialization 11, health above 10
and no invincibility flag. Both the selected Scout and Sarge loads supply that
specialization. The local match condition has no distance test, and two matches
do not add a bonus multiplier at this scan.

A qualifying match can satisfy the search's line-of-sight alternative. It does
**not** remove the strict greater-than 400 rule, enemy visibility or other filters.
The later firing request also has a separate camouflage check. Putting the
mortar under a net is not established as compatible with firing just because
a spotter passed the sight condition.
[Exact spotter and camouflage gates](../player-mortar-acquisition-evidence.md#a-specialization11-ally-can-satisfy-one-sight-alternative)

## The large reset counter is not a measured firing interval

The search reset writes 400 plus a 0–199 draw minus experience, with a floor 20.
A later positive-counter visit subtracts 1 and caps a value above 100 to 100.
Reading only the first expression would miss that later cap. These different
stages need actual callback/frame order before they become a first-shot or
repeat-fire time.
[Declared two-visit counter example](../player-mortar-acquisition-evidence.md#expired-counter-reset-and-later-positive-counter-cap-are-different-writes)

## The enemy mortar does not use your setup sequence

The Allied mortar counts setup upward while stationary; the enemy's positive
setup counter counts downward. Their search branches are arranged differently:
the Allied setup block precedes a separate later search gate, while the enemy
positive-setup branch excludes its sibling timer/search alternatives for that
selected chain.

They also use different minimum target distances, spotter/sight conditions and
own firing-action health tests. Their matching offset expressions do not make
them interchangeable weapons or establish equal first-shot time.
[Exact supplied-state and emission comparison](../player-mortar-acquisition-evidence.md#allied-and-enemy-setup-do-not-share-the-same-source-chain-boundary),
[enemy mortar](enemy-mortar.md).
Additional source: [Source identities](../player-notes/mortar.md#citation-2)

## What the modern experiment can and cannot rank

The following comparison uses the **November 7, 2026 modern simulation build**.
It is separate from the historical source facts above and from later corrections.
[Study conditions and build limits](combat-results.md).

The study used a deployed Mortar and a farther grenade-assay target to satisfy
its acquisition conditions. It did not establish competitive group clearance.
All six firearm offers left mortar attack behavior unchanged, and an accepted
hand-grenade flag produced no throws. Normal purchase/debit paths remain part
of the selected eligibility investigations.
[Results](combat-results.md), [equipment issues](combat-issues.md), [lifecycle](unit-lifecycle.md).
