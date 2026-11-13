[Player reference](README.md) · [Waves](waves.md) · [Enemy guide](enemy-guide.md)

# Enemies getting through your line

**The missed-enemy counter is not one point per visible vehicle.** Many selected
exit paths request mission loss when their post-exit count exceeds 9, but their
contributions and checks differ. Read that separately from losing all usable
soldiers or choosing Retreat to Main Menu.
[Exact source/version and counter/readers](../player-breakthrough-evidence.md)

Historical scope: selected **2.3.1g** source; these are conditional rules,
not a forecast of a particular battle.

On this page: [How should I read the missed-enemy warning?](#how-should-i-read-the-missed-enemy-warning) · [What an exit can count](#what-an-exit-can-count) · [A counter write is not always the same loss check](#a-counter-write-is-not-always-the-same-loss-check) · [Advancing can add to the counter too](#advancing-can-add-to-the-counter-too) · [Reducing the number is not undoing a loss](#reducing-the-number-is-not-undoing-a-loss)

## How should I read the missed-enemy warning?

- **Can I count visible escapes and allow nine through?.** Do not treat nine visible actors as a safe allowance. Different exits add different amounts, and most selected local loss tests use the resulting counter above 9.
- **Does one motorcycle count once?.** It can add twice when both driver and gunner fields are positive. With an old count of 8, those writes reach 10 before its local loss check.
- **Can advancing raise the counter without an ordinary escape?.** Yes. The selected advancement scan counts certain remaining enemy slots before their lower-edge exit callbacks. [Advancement](advancing.md)
- **Can an Officer or crate undo a loss already requested?.** Their selected counter reductions do not prove that an executed mission-loss action can be reversed. [Officer aid](officer.md), [crates](crates.md)

These are source-backed **selected historical 2.3.1g** answers, with the exact
[counter writers and loss checks](../player-breakthrough-evidence.md) kept behind
the explanation. The German Jeep's different local check, callback order and
later readers prevent turning the warning into a universal grace period.
The sections below explain each distinction; no new exit-timing or recovery
trial is claimed.

## What an exit can count

A selected ordinary enemy exit adds 1 when a living nonstock actor's unpaused
callback sees y above 600. A motorcycle instead adds 1 for a positive driver and
another 1 for a positive gunner, then checks the total. With 8 already recorded and
both bike seats positive, its two additions produce 10 before that check. Those
are role fields, not a count of drawn passengers.
[Motorcycle](enemy-motorcycle.md), [vehicle accounting](../vehicle-crew-accounting.md)

The inspected tank and German Jeep exits have their own earlier exit branches,
without a repeated living-health requirement there. That does not prove a
wreck can move through the line: it still needs to be a valid object reaching
that callback and boundary. Damage, removal and movement have separate guards.

## A counter write is not always the same loss check

Most selected exit writers also update the indicator and test the loss threshold
locally. The German Jeep's complete selected body instead increments and requests
removal without that local display/threshold operation. Other callbacks can
still read the changed total. This source distinction is not a safe-tenth-enemy
strategy or a measured delay before gameover.
[Exact Jeep-versus-tank/infantry comparison](../player-breakthrough-evidence.md#the-counter-increment-and-the-loss-request-are-distinct-operations)

## Advancing can add to the counter too

The admitted advancement helper counts certain remaining enemy slots without
waiting for their ordinary lower-edge exits. It uses living armor 0 or armor 1 with
positive driver-plus-gunner, and its selected scan is limited to indices 100 down
to 0. It is neither one per spare passenger nor the same type/health rule for all
visible tanks. The helper can then request mission loss from the total.
[Advancing](advancing.md), [mission ending](withdrawal-and-mission-end.md)

## Reducing the number is not undoing a loss

An Officer's selected support alternative can reduce the stored counter with a
lower correction to 0. An Airborne-mode crate alternative can also reduce a
positive count; another advertised Vital Intel alternative is unreachable in
its selected branch chain. None of those source writes establishes that an
already executed mission-loss action can be reversed.
[Officer](officer.md), [crates](crates.md), [unfair attack counter consumers](unfair-attacks.md)

Sources: [Source identities](../player-notes/breakthroughs.md#citation-1). Selected publisher-associated 2.3.1g;
no new native exit, loss-timing or save trial.
