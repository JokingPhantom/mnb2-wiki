[Player reference](README.md) · [Defenses](defenses.md) · [Construction](construction.md)

# Off-field protection flag

An off-field actor can carry a **protection flag separate from health, armor
and visibility**. The selected source calls it invincible. One helper can set
or clear it from the actor's raw coordinates and flee field.
That does not make every boundary position safe against every attack.
[Exact helper and caller evidence](../player-protection-flag-evidence.md)

Historical source scope: selected **2.3.1g**. Attributed observations retain
their own version limits below.

On this page: [Exact edges do not pass the outside test](#exact-edges-do-not-pass-the-outside-test) · [Check when the actor calls the helper](#check-when-the-actor-calls-the-helper) · [A protected-looking state still needs the actual attack test](#a-protected-looking-state-still-needs-the-actual-attack-test)

## Exact edges do not pass the outside test

The helper considers raw x below 0 or above 400, or raw y below 0 or above 600,
outside. Exact 0/400 and 0/600 edges do not pass those strict comparisons.
For a valid reached helper with no other writer, 1 means the flag is set
and 0 means it is clear:

| Supplied point / flee state | Local flag behavior                             |
| --------------------------- | ----------------------------------------------- |
| x 400 / y 600, any flee     | Writes invincible 0                             |
| x 401 / y 100, flee 0       | Writes invincible 1                             |
| x 401 / y 100, flee 1       | Leaves the previous flag unchanged at this site |

The outside branch needs flee exactly 0 to grant the flag. The inside branch
clears it without that flee test. A no-write outside alternative is therefore
not a hidden clear or grant. The helper has no local health test.

These are raw receiver fields, not certified world-space sprite edges. The
visible portion of a soldier or vehicle is not another term in this predicate.
[Exact inputs and limits](../player-protection-flag-evidence.md#outside-and-inside-alternatives-are-asymmetric)

## Check when the actor calls the helper

The selected Bazooka callback calls it before the callback's own pause guard;
Sherman and Halftrack put it inside an unpaused branch. If a callback is reached
while pausez 1, those call sites have different guard behavior. This is not an
observed pause exploit or proof all actors update their flags on the same tick.
[Caller placement](../player-protection-flag-evidence.md#caller-pause-placement-is-part-of-the-input)

## A protected-looking state still needs the actual attack test

Heroism assigns current health 200 and does not set this flag at its selected
receipt. This helper changes the flag without raising health. The AT helper
then has its own flag, armor, visibility, owner and distance guards; its recipient
stage differs from a rocket's earlier proximity trigger.
[Heroism](heroism.md), [AT handling](anti-tank-and-vehicles.md), [Bazooka](bazooka.md)

Use the named actor and damage path before interpreting the flag. No universal
immunity, safe crossing distance, transformed hitbox or completed exit outcome
is qualified by this source table.

Sources: [Source identities](../player-notes/protection-flag.md#citation-1).
Selected publisher-associated 2.3.1g; supplied fields and source guards, with no
new immunity, pause or geometry trial.
