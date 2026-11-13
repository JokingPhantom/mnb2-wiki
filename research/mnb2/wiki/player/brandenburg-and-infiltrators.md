[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Brandenburg troops and hidden infiltrators

Brandenburg troops and hidden infiltrators enter and reveal themselves in different ways. There are **side-entry, lower-field and hidden infiltrator variants**. The first two share a drawing but have different starting and movement rules; the hidden infiltrator is a separate enemy. A shared name
or sprite does not make their entry and detection rules identical.
[Exact identities](../player-brandenburg-evidence.md#shared-character-does-not-merge-two-placement-controllers)

Historical scope: selected **2.3.1g**.

| Selected placement     | Source entry / initial visibility                                           |
| ---------------------- | --------------------------------------------------------------------------- |
| Side-entry Brandenburg | x −10 or 420, y 0–449, horizontal objective 50–349                          |
| Lower-field variant    | x 1–400, y 600, vertical objective 400–599                                  |
| Hidden infiltrator     | Alpha 0 and visibility counter 0 at load; caller placement remains separate |

These are source assignments, not measured screen positions in every spawn.
All three selected loads have health 100, armor 0, XP 25–74 and morale 25–74
before the separate Assault Expert Award subtraction of 10. Rifle starts from
the ordinary local-wave roll divided by two.

On this page: [Proximity and experience can reveal an infiltrator](#proximity-and-experience-can-reveal-an-infiltrator) · [Firing, pinning and opacity are different reveal stages](#firing-pinning-and-opacity-are-different-reveal-stages) · [Their firearms also differ](#their-firearms-also-differ)

## Proximity and experience can reveal an infiltrator

In its inspected ready detection scan, a qualifying player detector needs health
above 9, armor other than 1 and a nonpillboxed result. Distance **below 50**
sets the infiltrator's visibility counter directly. From exactly 50 to strictly
below 200, another comparison uses half the detector's experience, with a
literal type-name shortcut. Exactly 200 fails these selected range branches.
These source-distance guards do not certify a visible detection circle.
[Exact scan and declared examples](../player-brandenburg-evidence.md#ready-detection-scan-and-the-scout-type-name-mismatch)

The shortcut checks type **`scout`**, but the recruited [Allied Scout](scout.md)
loads type **`recon`**. Its unchanged load therefore does not satisfy that literal
shortcut. The generic close-range and XP branches still apply; this is not proof
Scouts never detect an infiltrator or a reproduced runtime bug.

For a declared recon-type detector at XP 20, the longer-range comparison accepts
10 of 100 integer inputs on one eligible visit. At XP 0 it accepts none, while
the closer-than-50 branch still applies. Full squad frequency and later writers
remain separate.

## Firing, pinning and opacity are different reveal stages

Detection and a reached shot body write visibility 200. The pinned-down action
has a separate 20 write. The controller changes opacity and decrements positive
visibility through its own conditions; none of those counters is calibrated
seconds here. A visibility write is not the same as an immediate opacity change.
[Exact order and reveal writers](../player-brandenburg-evidence.md#hidden-infiltrator-load-and-visibility-processing)

## Their firearms also differ

The inspected unarmored damage draws are **0–149 for the Brandenburg character**
and **0–79 for the infiltrator**, after rifle and the selected 50/75 cover saves.
Zero damage remains possible. Their positive-burst repeat branches check the
counter before decrementing, and return to different firing stages. These facts
do not establish a whole-burst damage total or a universal combat ranking.
[Shot and repeat bindings](../player-brandenburg-evidence.md#shooting-reveal-and-repeat-boundaries)

Sources: [Source identities](../player-notes/brandenburg-and-infiltrators.md#citation-1)
