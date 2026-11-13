[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# SdKfz 222 armored car

The SdKfz 222 is an armored car with **650 starting health, armor code 1 and 3 spare crew**. Hull, crew roles and turret have separate rules. In particular,
the turret's rifle roll uses **mission-total wave**, rather than the hull's
1–10 load or the common infantry local-wave/2 formula.
[Exact parent and turret](../player-light-vehicle-evidence.md)

Historical scope: selected **2.3.1g**.

| Key fact              | Historical default or behavior                                      |
| --------------------- | ------------------------------------------------------------------- |
| Starting hull health  | 650                                                                 |
| Armor code            | 1                                                                   |
| Spare crew            | 3 spare crew                                                        |
| Important distinction | Turret rifle uses mission-total wave, separate from hull rifle 1–10 |

On this page: [A cleared driver field is not permanent immobilization](#a-cleared-driver-field-is-not-permanent-immobilization) · [Its turret has its own accuracy and burst path](#its-turret-has-its-own-accuracy-and-burst-path) · [Its infantry death request uses a below-10 threshold](#its-infantry-death-request-uses-a-below-10-threshold)

## A cleared driver field is not permanent immobilization

In its active positive-health controller, driver 0 is reset to 1 and costs the
parent 20 health. Its selected lateral movement branches do not add another
driver check. With supplied starting health 650 and driver 0, those statements
leave health 630 and driver 1; this is not an observed attack outcome.

A zero gunner instead has a latched crew-loss/appearance branch, while the
turret's own admission requires a positive gunner. Spare crew, a replaced driver,
disabled weapon and destroyed hull are different states.
[Crew, movement and destruction](../player-light-vehicle-evidence.md#sdkfz-222-parent-and-changing-crew-fields)

The selected destruction loop increments the kill counter for remaining crew
as it counts down. Three such increments are not three destroyed armored cars.
Likewise, its lateral exit path is separate from a complete destruction result.

## Its turret has its own accuracy and burst path

At supplied mission-total wave 50, the turret's load can roll rifle 0–49.
The shot uses that child rifle field, then separate armor/protection branches.
For a declared rifle 40 and valid unarmored target, independent uniform draws
admit 40% at accuracy and 5% (0.40 × 1/2 × 1/4) to the health-subtraction branch when both ordinary
cover and bunker queries succeed. These are one reached shot-action counts,
not firing rate, kill chance or an actual layout's survival result.

The unarmored damage draw is 0–149. The selected shot does not create a scattered
ground-explosion effect like the allied AA cannon's path. Its burst counter,
an additional flakburst field and the later timer writes are also distinct.
[Exact turret readers](../player-light-vehicle-evidence.md#the-222-turret-reads-mission-total-wave-not-hull-rifle)

Related: [enemy wave stats](enemy-stats.md), [AT and vehicle health](anti-tank-and-vehicles.md),
[allied 20 mm AA](aa-cannon.md).

Sources: [Source identities](../player-notes/sd-kfz-222.md#citation-1)

## Its infantry death request uses a below-10 threshold

The selected turret shot checks the unarmored recipient's health below 10 after
subtracting its 0–149 draw. With supplied starting health 100 and no intervening
writes, damage 90 leaves 10 and fails that test; damage 91 leaves 9 and requests
death. A positive arithmetic health value therefore does not prove this actor
escaped that local death request. The later navigation/casualty result remains
separate from the source comparison.
[Exact counts, zero damage and other mounted threshold](../player-shot-outcome-evidence.md).
Additional source: [Source identities](../player-notes/sd-kfz-222.md#citation-2)
