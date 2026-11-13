[Player reference](README.md) · [Waves](waves.md) · [Orders](orders.md)

# “Germans changed their tactic”: allocation replacement

When this message appears, the inspected helper removes indexed enemy entries
and requests a replacement group. A disappearance is not automatically a credited
kill, and the new group is not a verified reprieve. Use the [Grenadier guide](enemy-grenadier.md)
for the replacement role; keep checking the actual battlefield rather than
assuming every previous threat was cleared or difficulty reset.

The selected historical **2.3.1g** replacement helper is an **allocation cleanup followed by
new Grenadier requests**. It is not a count of 100 living enemies, a maximum
mission wave or an ordinary Blitz case. The historical community's estimated
10–15 replacements differs from the inspected helper's nominal loop.
[Exact helper and caller evidence](../enemy-allocation-replacement.md)

On this page: [The trigger can follow an allocation increment](#the-trigger-can-follow-an-allocation-increment) · [What the selected cleanup actually requests](#what-the-selected-cleanup-actually-requests) · [Replacement is nine nominal Grenadier requests](#replacement-is-nine-nominal-grenadier-requests)

## The trigger can follow an allocation increment

In the selected early Grenadier pass, a successful emission advances the enemy
allocation counter and then calls the replacement helper if that counter is
**above 100**. Other callers have their own guards. This does not mean the game
freshly counts 100 visible living enemies before every possible spawn.

The late generator has a separate health-positive enemy recount. An allocation
index, a live enemy, a vehicle's crew and a counted missed enemy are different
things. Neither this helper nor the late generator's eight-minus-live attempt
calculation is a universal cap on the battlefield.
[Waves](waves.md), [crew and misses](withdrawal-and-mission-end.md)

## What the selected cleanup actually requests

The helper sets its removal counter to 100, then visits named enemy slots from
**100 through 0 inclusive**. Under ordinary unchanged numeric inputs that is
**101 removal attempts**. It does not prove 101 actors existed or died, or that
slots 101 and above were examined by this loop.

It requests direct clip removal rather than explicitly invoking a per-enemy
death routine at that site. Do not count every disappearance as a credited kill,
a reward or a complete wipe: unload callbacks, other actors and earlier/later
accounting still require qualification.
[Exact indexed-removal scope](../enemy-allocation-replacement.md#removal-starts-from-a-fixed-index-not-the-old-counter)

## Replacement is nine nominal Grenadier requests

After resetting the enemy allocation counter to 0, the helper sets a replacement
counter to 10 and loops **while it is greater than 1**, subtracting 1 each time.
That gives **nine nominal requests**, not ten or an observed 10–15 living arrivals.
Each requests the enemy Grenadier template and position expressions with x 0–400,
y 0–9 and a rotation draw. Actual load, final placement and action callbacks remain
separate. [Grenadier role](enemy-grenadier.md), [source requests](../saturation-replacement.md)

The helper also uses the same shared quota field as surrounding generator
passes. In the cited caller, a supplied unchanged helper return value 1 becomes 0
at the caller's following quota decrement, ending that pass's next greater-than 1
test. The caller's old quota is not an independent local value automatically
restored on return. This is source state flow, not a measured full replacement
composition or a promise that later passes create no further actors.
[Shared quota boundary](../enemy-allocation-replacement.md)

The community describes this event as a possible reprieve from a dangerous
force. That remains historical advice, not a certified way to erase a tank or
reset difficulty. The new requests have their own stats and attacks, while
source timing, slot reuse and complete casualty accounting remain open.

Sources: [Source identities](../player-notes/changed-tactics.md#citation-1).
Selected publisher-associated 2.3.1g; original explanation, no new overflow,
cleanup, reward or live-arrival trial.
