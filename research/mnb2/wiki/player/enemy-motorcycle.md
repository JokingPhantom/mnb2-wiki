[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy motorcycle

The enemy motorcycle starts with **300 health and armor code 1**, with
driver and gunner fields both set to 1. Its inspected exit path can add
**two missed-enemy points for one vehicle**, because those fields are counted
separately. [Exact load and exit writes](../vehicle-crew-accounting.md#a-bike-can-add-two-crew-contributions-at-its-exit)

Historical scope: selected **2.3.1g**.

| Key fact             | Historical default or behavior                                         |
| -------------------- | ---------------------------------------------------------------------- |
| Starting hull health | 300                                                                    |
| Armor code           | 1                                                                      |
| Crew                 | Driver and gunner flags 1                                              |
| Important limit      | Crew loss can leave coasting momentum and a later separate MG dismount |

On this page: [An exit is not one point for every chassis](#an-exit-is-not-one-point-for-every-chassis) · [Losing the driver does not immediately erase momentum](#losing-the-driver-does-not-immediately-erase-momentum) · [Coasting can be followed by a machine-gunner dismount](#coasting-can-be-followed-by-a-machine-gunner-dismount) · [Health and counter guards are not interchangeable](#health-and-counter-guards-are-not-interchangeable)

## An exit is not one point for every chassis

At the selected nonstock, unpaused y-above-600 exit branch, a positive driver
adds one missed point and a positive gunner adds another. Those two writes
contain no unconditional extra point for the chassis. With both fields positive,
they add two; with both nonpositive, they add none at those sites.

The later miss-threshold check and removal remain part of that source path.
This is not an observed empty-bike escape, a universal rule for every vehicle,
or a promise that every starting crew field survives until the boundary.
[Mission ending and counters](withdrawal-and-mission-end.md)

## Losing the driver does not immediately erase momentum

With unpaused state and health above 1, a positive driver adds 1 to y. Without
a positive driver, a separate positive-momentum path can move it by that
momentum. Clearing the driver field therefore does not alone prove an immediate
stop. Momentum changes, later damage and actual callbacks still matter.
[Exact movement readers](../vehicle-crew-accounting.md#a-bike-can-add-two-crew-contributions-at-its-exit)

Its abandonment life decrement uses both gunner and driver exactly zero.
That selected decrement has no own pause test; this is not a measured pause
exception or a fade time in seconds. Removal tests life exactly zero in the
later below-100 branch, rather than every possible negative/overridden value.
[Abandonment conditions](../vehicle-crew-accounting.md#abandonment-timers-have-different-guards)

## Coasting can be followed by a machine-gunner dismount

With the driver no longer positive, the living branch can coast while momentum
is positive, reducing it by 0.05 per qualifying visit. When that branch no longer
applies and the gunner flag is exactly 1, the next selected alternative clears
the gunner, changes its visual state and requests a separate enemy machine gunner
at bike x plus 25 and the bike's current y. It does not copy the bike's combat
stats at those placement sites. Actual new MG load-wave and survival need their
own callback evidence. [Dismount source order](../player-bike-lifecycle-evidence.md#driver-loss-can-lead-to-a-new-machine-gunner-request-after-coasting)

A momentum update reaching zero does not also enter the sibling dismount branch
in that same source execution. A gunner field and the named visual child also
do not by themselves prove a mounted weapon: the selected child bodies only stop
and jitter its rotation. [Exact component scope](../player-bike-lifecycle-evidence.md#the-gunner-field-and-child-name-do-not-prove-a-mounted-firing-path)

## Health and counter guards are not interchangeable

The exit-counter branch precedes the health split and has no own health condition.
The later health-wreck crew-count sites instead use driver/gunner **strictly above
1**, which unchanged load-like flags of 1 do not pass. AT removal has another
positive-crew/common-counter path. These are local source guards, not a fixed
kill reward or proof of a dead-bike overrun in native play.
[Exit and death counter sites](../player-bike-lifecycle-evidence.md#the-exit-check-precedes-the-health-split)

Mounted firing, full crew-damage transitions and actual exit outcomes remain
partial. Armor class and parent health do not by themselves describe them.
[Enemy vehicle overview](enemy-vehicles.md), [AT distinctions](anti-tank-and-vehicles.md)

Sources: [Source identities](../player-notes/enemy-motorcycle.md#citation-1)
