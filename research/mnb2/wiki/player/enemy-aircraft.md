[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy aircraft

Enemy strafing and bombing threaten positions through different attack effects.
Strafing requests a sequence of small explosions; bombing creates a bomb with
a later explosion stage. The [unfair fast jet](unfair-attacks.md) uses another
path again. An aircraft-related statistic does not necessarily count planes or
casualties. [Attack and accounting evidence](../player-enemy-air-evidence.md)

Compare [Air Superiority, Radar and the AA cannon](air-defense.md) by what each
changes. None of their names proves every attack already underway is canceled.
The selected rules below do not establish a safe place to stand or a guaranteed
time to move out of danger.

The selected 2.3.1g German aircraft path can choose its vertical attack area
from your indexed force's positions. A helper counts entries with defined
health **at least 10** and source y **below 300**. **Five or more** makes its
upper-area flag true; four does not. It does not require those entries to be
infantry or visible at that helper. This is a selected source-stage choice,
not a continuously tracking enemy or a validated safe deployment tactic.
[Exact half-selection](../player-enemy-air-evidence.md#five-qualifying-upper-entries-change-the-selected-half)

Historical scope: selected **2.3.1g**.

| Attack           | Placement or accounting distinction                                            |
| ---------------- | ------------------------------------------------------------------------------ |
| Strafing         | 17 guarded small-explosion sites; not 17 guaranteed hits                       |
| Ordinary bombing | Emits a bomb before its later explosion                                        |
| Unfair fast jet  | Separate effect path and pending-bomb-state writes                             |
| Important limit  | No certified safe position, cancellation guarantee or universal aircraft count |

On this page: [Strafing and bombing use different placements](#strafing-and-bombing-use-different-placements) · [A plane statistic is not a plane count](#a-plane-statistic-is-not-a-plane-count) · [The unfair fast jet is a different source path](#the-unfair-fast-jet-is-a-different-source-path) · [Pending bombing is not a queue of every earlier request](#pending-bombing-is-not-a-queue-of-every-earlier-request)

## Strafing and bombing use different placements

Strafing has 17 guarded small-explosion sites, each with a separate horizontal
draw 20–380. The upper flag gives vertical literals 0 through 320 in steps 20;
the other branch gives 300 through 600, then repeats 600. The selected bomb
emission instead draws its initial y 0–299 or 300–599 from that flag and emits
a bomb object with another effect stage.

Those are source coordinates and conditional emission sites. They do not
certify the displayed blast outline, completed hit count, elapsed attack
duration or protection at a boundary. Moving one soldier is not enough to
infer a half-choice change without knowing the other qualifying entries and
when that helper is called.
[Positions and limits](../player-enemy-air-evidence.md#strafing-uses-separate-guarded-effect-positions)

## A plane statistic is not a plane count

The last guarded strafing action adds **17–21** to a statistic named
germanPlane, while clearing the strafing flag. It does not add exactly 1 there.
The bomb emission separately adds 1 to germanBomb. Neither write proves a
casualty or aircraft destruction.

Another aircraft action resets qualifying 20 mm guns' airburst and rewrites
their child readiness counter using that gun's XP. [20mm AA cannon](aa-cannon.md),
[exact reset guards](../player-enemy-air-evidence.md#bombing-and-gun-reset-are-separate-actions).
[Air superiority and radar](air-defense.md) have separate request/delay and
interception consumers; their names do not promise cancellation of everything
already emitted. [Enemy paratroopers](enemy-paratroopers.md) use another plane stage.

Sources: [Source identities](../player-notes/enemy-aircraft.md#citation-1).
[Version and exact bindings](../player-enemy-air-evidence.md)

## The unfair fast jet is a different source path

The selected fast-jet controller requests jetExplo and clears shared germbomb,
then increments the bomb statistic. Its random-point effect is separate from
the ordinary aircraft's upz half-selection and bombmc emission. The jet's named
blast inputs are 40/40/40/300 with tag tank, rather than the off-map 88's
25/50/50/100 or a universal aircraft damage value.

If that clear happens before an otherwise unchanged ordinary bomber's positive-
germbomb check, the latter guard fails; it does not remove a bomb already emitted.
Those are supplied callback-order consequences, not a reproduced cancellation
or proof that the jet always prevents another attack.
[Exact controller, field readers and effect boundaries](../player-unfair-jet-evidence.md).
Additional source: [Source identities](../player-notes/enemy-aircraft.md#citation-2)

The ordinary enemy bomb is the same named bombmc/bombexplomc pair used by friendly
bombing, with different initial coordinates and the enemy caller's rotation 180.
Its later transition copies the bomb's current x/y, without explicit rotation/
owner copies at that body. The shared effect's 100/100/200/100 helper arguments
are different from the fast jet's 40/40/40/300. They do not supply a universal
health-loss maximum or a complete damage/survival ranking.
[Exact shared-bomb caller/transition comparison](../player-shared-bomb-evidence.md).
Additional source: [Source identities](../player-notes/enemy-aircraft.md#citation-3)

## Pending bombing is not a queue of every earlier request

The finite supported literal germbomb writers replace the field with 0 or 1.
Two admitted bomb-request writes therefore leave 1, rather than accumulating 2.
Selected strafe/para choices and the fast jet can also clear that pending state.

The ordinary plane's frame 50 tail clears germbomb even when its positive-para
block was skipped, if execution reaches that tail. It does not remove a bomb
already emitted at that field assignment. Actual callback order and lifetime
remain unqualified. The Para Blitz also spells one sibling field germstrafe,
distinct from this plane's germstraff; those names are preserved separately.
[Exact 12-site map and supplied-field examples](../player-enemy-bomb-state-evidence.md).
Additional source: [Source identities](../player-notes/enemy-aircraft.md#citation-4)
