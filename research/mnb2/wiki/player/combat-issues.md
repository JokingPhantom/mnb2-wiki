[Player reference](README.md)

# Combat issues found during the modern tests

The November 7 combat experiments exposed the following issues. The operator
selected #1–4 and #7–8 as historical bugs to fix **only in the modern gameplay
candidate**, preserving historical 2.3.1g behavior. Original-runtime scope still
needs confirmation where only the modern fixture was measured.

This page preserves findings from the November 7 experiment build. Later
Community corrections and modern rechecks are described below; the original
measurements are not current-build performance guarantees. Check the linked
task for each correction. Original-game behavior still needs its own evidence.
[Evidence and full results](../../experiments/unit-combat-expanded.md).

| Issue                                 | Player-visible concern and current evidence                                                                                                                                                                                                       | Work                                                                  |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 1. Shotgun XP gate                    | The reached fallback requires random integer 0–99 > XP. XP 99–100 cannot pass; high-XP group fixtures never fired. This is a decision failure, not poor pellet damage.                                                                            | [Shotgun fix](../../../../tasks/MNB2-COMBAT-BUGS-001A.md)             |
| 2. Flamethrower XP gate               | Within its acquisition range, the reached fallback requires random integer 0–99 > 2×XP. XP 50+ cannot pass.                                                                                                                                       | [Flamer fix](../../../../tasks/MNB2-COMBAT-BUGS-001B.md)              |
| 3. Post-scan target receiver          | A lookup after the target scan can reach an absent receiver and the XP fallback. Community now uses the selected-target distance; Remaster retains the old lookup. The archived study predates that correction.                                   | [Receiver investigation](../../../../tasks/MNB2-COMBAT-BUGS-001C.md)  |
| 4. Recon aiming interruption          | Its short decision reset can request preparation again before a shot. More frequent decisions can slow gun clearance.                                                                                                                             | [Recon fix](../../../../tasks/MNB2-COMBAT-BUGS-001D.md)               |
| 5. Lost burning source context        | 36/160 secondary flame attempts raised an isolated burning-man source-context error. Later burning-source integration is verified; the original 160-cell means remain unqualified.                                                                | [Context investigation](../../../../tasks/MNB2-COMBAT-BUGS-001E.md)   |
| 6. Unexplained healthy-target removal | Four secondary attempts removed a 100-HP enemy without a qualifying target event; accompanying burn events identified the shooter. Later tracing identifies last-ally game-over cleanup, not four enemy kills; bounded rechecks are linked below. | [Removal investigation](../../../../tasks/MNB2-COMBAT-BUGS-001F.md)   |
| 7. Ineffective Mortar firearm offers  | Six firearm offers were accepted in the model but did not change mortar attacks. Normal purchase/debit behavior needs qualification before calling it a demonstrated wasted TP purchase.                                                          | [Equipment fix](../../../../tasks/MNB2-COMBAT-BUGS-001G.md)           |
| 8. Unused specialist grenades         | MG, Sniper and Mortar accepted a hand-grenade flag but never threw; normal purchase/debit handling needs qualification.                                                                                                                           | [Grenade eligibility fix](../../../../tasks/MNB2-COMBAT-BUGS-001H.md) |

Issues 5–6 are modern simulation or test-fixture investigations, not established
historical bugs. The isolated fixture omits tactic changes, waves and ordinary
board cleanup. A living enemy intentionally retreating or leaving through an
expected tactic-change rule is not itself a bug.

On this page: [What can be said about Flamethrower performance?](#what-can-be-said-about-flamethrower-performance) · [A test observer was corrected](#a-test-observer-was-corrected)

## What can be said about Flamethrower performance?

The ordinary medium/far test distances were outside its below-180 acquisition
range. Close XP-100 units also failed the XP gate in that archived build.
Community now corrects the post-scan receiver for Shotgun and Flamethrower;
Remaster retains the source lookup. The rates below remain November 7
measurements, not a rerun after that correction.
[Community correction](../../../../tasks/MNB2-COMBAT-BUGS-001C.md).
A separate single-target follow-up at distances 75/120 found:

- XP 0: all eight targets killed per distance, mean about 29–30 simulation seconds.
- XP 25: all eight killed, mean about 10–13 seconds.
- XP 49: only 7/8 and 6/8 cleared within 600 seconds.
- XP 50/100: no shots and no clears.

Lower-XP group tests encountered issues 5–6. Affected cells have **no qualified
mean**; failures were not counted as kills or converted into 600-second timeouts.
These tests therefore do not establish a useful flame crowd-clearance ranking.

## A test observer was corrected

The observer initially assumed burn victims always appeared in event.target.
Some native burn events put the victim in event.actor. That instrumentation
error was corrected and the secondary study recollected. That early observer correction did not eliminate
the source-context errors or four healthy removals. Subsequent tracing identified
the removals as last-ally game-over cleanup. The corrected observer excludes
healthy terminal survivors from kills. After the separate burning-source fix,
the four retained specialist cases clear with 20 genuine kills each; the other
160-cell outcomes and means have not been requalified.
[Original diagnosis and integrated rechecks](../../experiments/flame-terminal-observer-recheck.md).
[Failure history and archived inputs](../../../../tasks/MNB2-COMBAT-EXPERIMENT-004.md).

Spec Ops repeat behavior, Resistance recovery and Sarge support are explicit
role differences, not additional filed bugs simply because outcomes differ.
[Lifecycle explanation](unit-lifecycle.md).
