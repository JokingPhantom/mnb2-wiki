[Player reference](README.md) · [Explosives](explosives.md) · [Collateral damage](collateral-damage.md)

# Duds: waiting, approaching and defusing differ

An unexploded dud has its own autonomous hazard check as well as the Engineer's
click-to-defuse action. **The selected callback uses different health and distance
gates for those jobs.** These facts describe the selected 2.3.1g source; no timing
or safety trial is claimed. [Source and exact bindings](../player-defuse-evidence.md#untouched-dud-callback)

| Action/check                | Selected local condition                                                 |
| --------------------------- | ------------------------------------------------------------------------ |
| Engineer defuse candidate   | Engineer specialization, health > 10, pointer-to-Engineer distance < 100 |
| Dud's player proximity scan | Defined health>=10, distance from dud<5                                  |
| Dud's enemy proximity scan  | Health>0, distance from dud<25                                           |

A soldier at health 10 is therefore eligible for the dud's player proximity test
but cannot satisfy the Engineer defuse gate. The distance checks are strict:
exactly 5 fails the player proximity comparison, exactly 25 fails the enemy one.
These are source-point comparisons, not certified radii from visible artwork.

On this page: [The autonomous check is not the defuse roll](#the-autonomous-check-is-not-the-defuse-roll)

## The autonomous check is not the defuse roll

The dud starts with instability 0 and timer 30. Each delivered non-template
enter-frame callback subtracts one; **only when the result equals zero** does
this body perform its random and proximity checks. It has no timer reset or local
pause guard. Under an uninterrupted, otherwise unchanged timer sequence, that
means visit 30 reaches the checks; a surviving visit 31 reaches -1 and skips them.
Do not convert those visits to seconds or infer that pausing or waiting makes a
dud safe: callback delivery, removal and other state still need qualification.

The isolated autonomous random comparison accepts 2 of 100 integer values at
instability 0, or 12 at instability 10. Those are not full explosion rates: the
player and enemy proximity scans follow that roll. Each passing emission uses
the dud's position. Removing the object is not an explicit return, so this source
alone does not settle how many later scans/effects execute in that callback.

The Engineer's primary defuse success instead accepts **89 of 100** values at
instability 0, followed on failure by a separate XP-dependent outcome. Do not use
the autonomous 2% roll as a defuse-failure rate. A successful defuse adds one XP
and calls promotion. [Engineer outcomes](engineer.md#defusing-is-not-a-fixed-success-percentage)

Pioneer TNT has a different pickup, three-XP receipt and shared charge pool.
[Engineer pickup](engineer.md#pioneer-tnt-uses-a-different-receipt),
[TNT spending](explosives.md#tnt-has-several-kinds-of-state)

Sources: [Source identities](../player-notes/duds.md#citation-1).
[Evidence and conditional limits](../player-defuse-evidence.md)
