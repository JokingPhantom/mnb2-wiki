[Player reference](README.md) · [Vehicles and emplacements](vehicles-and-emplacements.md) ·
[Repair, crew or reload?](repair-crew-and-reload.md)

# Jeep

A **6-TP vehicle with 500 starting health and armor class 1** in the selected
2.3.1g source. Hull fields, gunner fields and their readers are separate; that
matters to its shooting, progression and crew behavior.
[Version and exact evidence](../player-jeep-evidence.md)

Applies to **historical selected 2.3.1g**; hull and gun-component fields
have separate readers. Starting values are not permanent health/crew guarantees.

| Key fact                     | Selected historical load                                   |
| ---------------------------- | ---------------------------------------------------------- |
| TP cost and availability     | 6 TP; vehicle offer                                        |
| Health / maxhealth           | 500 / 500                                                  |
| Armor class                  | 1                                                          |
| Driver / gunner / spare crew | 1 / 1 / 0                                                  |
| Experience / rank            | 2 / 0; Mud and Blood Cross adds 9 XP at its load branch    |
| Rifle                        | Random stopping additions of 1–10, then Combat Ribbon's +3 |

[Starting-field evidence](../player-jeep-evidence.md)

Start with your question: [Why will it not move or fire?](#what-to-check-when-using-the-jeep),
[which rifle stat matters?](#which-stat-does-each-stage-use), or
[what changes when the driver is missing?](#new-selection-and-an-existing-destination-use-different-driver-tests).

## What to check when using the Jeep

- **Moving and firing have different crew checks.** New movement selection needs
  the driver, while the gun's selected acquisition needs the gunner. An existing
  destination has a different later reader; this is not a tested promise of
  crewless driving. [Control and movement evidence](../player-vehicle-movement-evidence.md#losing-a-driver-and-losing-an-old-destination-are-different-events).
- **Repair and recrew solve different problems.** Restored hull health does not
  prove the gunner is present. Check the actual missing role before treating the
  gun as merely damaged. [Repair, crew or reload?](repair-crew-and-reload.md).
- **The panel does not summarize every weapon reader.** The selected hover
  copies gun-component rifle, while the firearm compares hull rifle. A displayed
  increase alone is not proof this shot comparison improved.
  [Hover and firearm fields](../player-hover-stat-evidence.md).

These are source distinctions for **selected 2.3.1g**, not a new movement,
crew-loss or combat-performance trial. Exact starting fields and attack stages
are below.

The load can therefore hold XP 11 with rank 0 under that medal branch. Starting
XP and a later promotion check are different stages. The gun component instead
loads its own rifle 1–10, XP 1–10 and action counter 20.
[Load and component scope](../player-jeep-evidence.md#purchase-hull-and-gun-placement)

## Which stat does each stage use?

| Source stage                           | Selected field             |
| -------------------------------------- | -------------------------- |
| Gun's aiming-loop comparison           | Gun component's experience |
| Firearm accuracy comparison            | Hull's rifle               |
| Ordinary Jeep promotion rifle addition | Gun component's rifle      |

A gun kill branch can add hull XP and call promotion, but the Jeep-specific
promotion bonus writes **a different rifle field from the one this firearm reads**.
It is not proof that this shot comparison automatically improves. That is a
selected source mismatch, not a claim XP has no other effect.
[Writer, reader and aiming gate](../player-jeep-evidence.md#the-promotion-writer-and-shot-reader-differ)

The inspected direct firearm body can draw **0–199 damage** against a qualifying
living unarmored target, with separate crew/armor branches. Its positive-burst
modifier also differs from the [static .50](fifty-caliber.md) helper. Do not copy
a standard infantry weapon's statistics from the gun component's numeric code.

## Gunner, driver and targeting checks differ

The selected acquisition controller needs a positive gunner flag and checks
protection, visibility, invincibility and line of sight. Its candidate distance
comparison uses the hull, while its stored-distance update uses the child gun.
That mix is not a proven nearest-target policy; the exact source and a declared
raw-coordinate example are linked below.
[Acquisition receivers](../player-jeep-evidence.md#acquisition-mixes-raw-coordinate-receivers)

The hull movement step does not contain the same local crew gate as gunner
acquisition. A driver display change and a gunner stop are not one universal
immobility rule. Actual crew-loss, obstacle, control and callback behavior still
needs qualification. [Crew replacement](crewman.md), [vehicle damage](anti-tank-and-vehicles.md)

Initial, aiming-loop, post-fire and retarget counters/navigation remain distinct.
No complete firing rate, burst length or first-shot time follows from one of them.

Sources: [Source identities](../player-notes/jeep.md#citation-1). [Exact evidence](../player-jeep-evidence.md)

At supplied hull health **0**, the selected parent still takes its health>=0
nonwreck alternative; negative health takes its carwreck/removal branch. The
movement subsection still has other guards, and earlier damage/removal can
prevent this reader from running. This is a source predicate distinction,
not a demonstrated usable zero-health Jeep or resurrection method.
[Parent health/wreck comparison](../player-vehicle-wreck-evidence.md).
Additional source: [Source identities](../player-notes/jeep.md#citation-2)

## New selection and an existing destination use different driver tests

The selected release handler assigns movement focus only when driver equals 1.
The later hull callback does not repeat that driver test before processing an
existing waypoint; its driver 0 appearance branch does not clear the stored
destination. A missing driver alone therefore does not reject those selected
movement statements. Actual crew-loss coasting, duration and interruption still
need a complete trial.
[Exact button, parent and declared-state limits](../player-vehicle-movement-evidence.md#losing-a-driver-and-losing-an-old-destination-are-different-events).
Additional source: [Source identities](../player-notes/jeep.md#citation-3)

## The hover rifle field follows the gun component

The selected Jeep hover copies gun-component rifle into the panel, but copies
hull XP and health and requests its rank icon from hull rank. Its inspected
firearm accuracy comparison still reads hull rifle. With declared hull 40/gun 10,
hover copies 10 while that comparison uses 40. A later child-only promotion bonus
can raise the hover input without changing this hull-reader value.

This is a source receiver distinction, not an observed display bug or proof
that every promotion is ineffective. Hover needs driver 1 or gunner 1; selected
movement focus instead needs driver 1. [Exact handler, field copies and supplied-state limits](../player-hover-stat-evidence.md).
Additional source: [Source identities](../player-notes/jeep.md#citation-4)
