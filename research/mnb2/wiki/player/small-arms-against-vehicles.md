[Player reference](README.md)

# Small arms against vehicle crews

Rifle fire can **clear a driver or gunner role without damaging the vehicle’s hull** in the selected historical **2.3.1g** shared infantry firing path. Its armor-class 1 crew checks differ from infantry health damage and anti-tank destruction. A recorded hit, a crew kill and a destroyed vehicle are different outcomes. [Exact path](../player-small-arms-crew-evidence.md)

Use the [armor-code examples](reading-stats.md#what-do-armor-codes-0-1-and-2-mean)
to distinguish this class-1 crew route from the same helper's infantry and
armor-2 alternatives. They are branch distinctions, not one universal damage scale.

On this page: [Driver and gunner are separate chances](#driver-and-gunner-are-separate-chances) · [The Goliath and SdKfz222 have exceptions](#the-goliath-and-sdkfz222-have-exceptions) · [A hit counter does not prove penetration](#a-hit-counter-does-not-prove-penetration) · [Incoming Regular bullets use a different crew table](#incoming-regular-bullets-use-a-different-crew-table)

## Driver and gunner are separate chances

After accuracy succeeds, another random test must pass before the helper draws
an impact category. Four of its ten categories attempt neither role, three
select driver and three select gunner. The chosen role must still be nonzero.
It does not switch to the other seat when the selected one is already empty.
The ordinary role path then needs another successful test to clear that field.

Given an otherwise valid armor-class 1 target with both roles present and a
passed accuracy comparison, the ordinary branches each have a **7.5% conditional
role-clear chance**. The ordinary calculation is 1/2 crew entry × 3/10 role selection × 1/2 final test = 3/40, or 7.5%, for each role. Those are not chances per fired round: acquisition,
accuracy and later vehicle behavior remain separate.
[Declared inputs and boundaries](../player-small-arms-crew-evidence.md#type-exceptions-and-conditional-counts)

## The Goliath and SdKfz222 have exceptions

The Goliath bypasses the final ordinary role test for both driver and gunner;
the SdKfz222 does so for driver only. With the same declared inputs, the
bypassed role's conditional chance is 15% rather than 7.5%. These are source
fields, not a claim that human crew sit inside a Goliath.

Clearing the SdKfz222 driver also does not establish permanent immobilization:
its controller can restore that field and subtract 20 hull health. A bike can
coast without its driver, and trucks handle replacement crew separately.
[SdKfz222](sd-kfz-222.md), [motorcycle](enemy-motorcycle.md), [truck](enemy-truck.md)

Crew loss also need not end a transport's infantry requests. Compare
[truck, Halftrack and motorcycle dismount paths](enemy-vehicles.md#can-a-damaged-transport-still-unload-infantry)
before reading a cleared role as proof that no more infantry can appear.

## A hit counter does not prove penetration

This helper increments the hit statistic before its armor branch. Its selected
armor-class 2 alternative requests a ricochet sound; it does not copy the
infantry's random health subtraction into the tank. Crew-success kill counters
also do not automatically count wrecks. This does not classify every weapon or
mounted component: follow the actual firing path.
[Accounting and recipient branches](../player-small-arms-crew-evidence.md#accuracy-is-followed-by-another-armor-specific-selection)

For blasts, read [hull damage and crew loss](vehicle-damage-and-crew.md).
For vehicle destruction, read [AT stages](anti-tank-and-vehicles.md).

Source: [Source identities](../player-notes/small-arms-against-vehicles.md#citation-1). selected publisher-associated 2.3.1g.
No whole-cycle accuracy, vehicle-outline hitbox or native encounter is claimed.

## Incoming Regular bullets use a different crew table

The selected **enemy Regular** shot has a 35% crew-entry comparison, then
three impact categories: one attempts neither role, one selects driver, and
one selects gunner. The chosen field must equal 1, followed by a separate
below 50 test before it is cleared. It does not reuse the outgoing Allied
table or its Goliath/SdKfz222 exceptions.

Given a valid stable armor 1 target with both roles 1, already passed Regular
attempt/accuracy and independent uniform draws, each role's conditional clear
chance is **7/120, about 5.83%**. The calculation is 35/100 crew entry × 1/3 role selection × 1/2 final test = 7/120. This is not a chance per fired round or a
whole-battle survival rate.
[Exact branches and strict boundaries](../player-regular-crew-evidence.md#do-not-mirror-the-outgoing-shared-helper-crew-table)

The ordinary-cover/bunker save calls are in the preceding unarmored alternative;
they are not repeated inside this armor 1 crew branch. Do not apply the infantry
87.5% combined-save figure to these selected vehicle-crew attempts. This remains
one named shooter path, with acquisition and other damage mechanisms separate.
[Save scope and hull distinction](../player-regular-crew-evidence.md#infantry-saves-are-not-repeated-inside-this-armor1-branch)
Additional source: [Source identities](../player-notes/small-arms-against-vehicles.md#citation-2)

[Original opening and evidence context](../player-notes/small-arms-against-vehicles.md#opening-before-player-language-correction).
