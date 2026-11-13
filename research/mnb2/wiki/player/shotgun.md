[Player reference](README.md) · [Weapon comparison](weapon-comparison.md) ·
[Equipment](training-and-equipment.md)

# Shotgun

A **1-TP weapon upgrade** whose shared-helper damage and accuracy change sharply
with source distance. It cannot be described by one maximum-damage number or
by copying another actor's range restriction.
[Weapon and actor evidence](../player-weapon-evidence.md#shotgun-bands)

Applies to **historical selected 2.3.1g**. Damage rows are conditional draws,
not guaranteed health loss; refill rows apply only to the stated ordinary-soldier
recovery branch. A weapon purchase is not itself a completed recipient/refill.

| Key fact                 | Selected offer/behavior                                                               |
| ------------------------ | ------------------------------------------------------------------------------------- |
| TP cost and availability | 1 TP equipment offer; apply to an eligible recipient                                  |
| Close-distance behavior  | Below 100 source units: conditional damage draw 0–199 health, accuracy roll ÷3        |
| Main limitation          | Damage and accuracy worsen in farther bands; acquisition also has separate conditions |

[Weapon offer and behavior evidence](../player-weapon-evidence.md).

On this page: [What should I check before spending 1 TP?](#what-should-i-check-before-spending-1-tp), [One ordinary decision has an XP-dependent fallback](#one-ordinary-decision-has-an-xp-dependent-fallback), [High-XP firing failure in the modern experiment](#high-xp-firing-failure-in-the-modern-experiment).

## What should I check before spending 1 TP?

Distance changes both the damage draw and the accuracy comparison in selected
**2.3.1g**. Below 100 source units, Shotgun has its largest damage draw and an
easier accuracy roll. At 200, the draw drops to 0–9 and the roll becomes harder.
The low price and large close-distance number therefore do not describe a
general-purpose replacement for distant rifle fire.
[Exact distance bands](../player-weapon-evidence.md#shotgun-bands)

Check whether the soldier actually acquires and fires at the intended target,
too. Its earlier Shotgun decision has a separate target-index issue explained
below; this damage table alone cannot guarantee firing. Buying also leaves a
pending equipment choice to apply, rather than proving immediate replacement
or a fresh eight-round load. [Equipment steps](training-and-equipment.md),
[ordinary cycle](../player-weapon-evidence.md#ordinary-soldier-cycle)

| Source distance  | Conditional unarmored damage draw | Accuracy roll change       |
| ---------------- | --------------------------------- | -------------------------- |
| Below 100        | 0–199                             | ÷3                         |
| 100 to below 200 | 0–99                              | None in this weapon branch |
| 200 to below 400 | 0–9                               | ×3                         |
| 400 and above    | 0–4                               | ×5                         |

The band boundaries are strict: exactly 100 uses the second band, exactly 200 the
third, and exactly 400 the last. Damage is still conditional on the helper's
accuracy and target checks. A large close-distance bound is not guaranteed
health loss or a promise that an actor chooses to fire.

The ordinary soldier has an additional shotgun decision during target
acquisition. One distance expression there references the scan index rather
than the stored selected target, so a shorthand “250-unit maximum” should not
be asserted without binding that actual path. The shared-helper table itself
does not impose such a 250 cutoff. [Acquisition source distinction](../player-weapon-evidence.md#shotgun-bands)

A separate direct Gunner firing body has a weapon 4 distance-below 400 condition.
That is a different source body; it does not erase the shared helper's last
damage band or prove an ordinary player can equip a Gunner through every menu
path. Actor and reachable state remain necessary qualifications.
[Actor comparison](../player-weapon-evidence.md#shotgun-bands)

The specified ordinary-soldier recovery branch refills empty ammo to 8 and assigns
200 minus experience. It is one conditional state path, not a universal reload
duration in seconds or proof that purchasing immediately supplies 8 rounds.
[Recovery table](how-shooting-works.md)

Sources: [Source identities](../player-notes/shotgun.md#citation-1).
[Exact source bindings](../player-weapon-evidence.md)

## One ordinary decision has an XP-dependent fallback

In the selected ordinary controller's Shotgun choice, a passing below 250 distance
comparison requests firing preparation. Its false alternative instead needs a
random 0..99 draw strictly above the actor's experience: XP 20 admits 79 draws, XP 50
admits 49, and XP 99 admits none at that one request site. The distance expression
reads the search scan index, rather than the stored chosen target.

Those details do not establish that experienced shotgun users always stop
shooting or that a nearby selected enemy supplies the comparison's distance.
The actual read object and callback state remain essential. The later shared
shot reads the current selected target for its own damage/distance bands.
[Exact reader, supplied inputs and retained counter work](../player-weapon-evidence.md#ordinary-shotgun-choice-reads-the-scan-index-and-has-a-reverse-xp-comparison).
Additional source: [Source identities](../player-notes/shotgun.md#citation-2)

## High-XP firing failure in the modern experiment

Modern evidence: **November 7, 2026 studies and their linked earlier trials**.
These are tested-build outcomes, separate from historical source arithmetic
and later corrections. [Study limits](combat-results.md).

The reached controller fallback requires random integer 0–99 > XP.
At XP 99–100 that cannot pass; veteran group trials never fired the gun.
This is separate from its distance-dependent damage. The archived result alone does not settle original-game receiver and
callback behavior; the later Community correction is described below.

Recon/Shotgun's exceptional hand-grenade launch count therefore does not establish
a sound firearm build. Community now corrects the post-scan receiver, using the selected-target
distance before reaching the XP fallback. Remaster retains the old lookup.
The veteran results above describe the archived November 7 build; no updated
clearance ranking is implied. Historical 2.3.1g rules remain separate. [Issue and current task](combat-issues.md).
