[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Role comparison](recruitment.md#choose-the-job-before-the-price)

# Scout

A **6-TP observer recruit**, distinct from the cheaper combat-focused Spec Ops.
The selected source has distinct movement, acquisition-counter and observer
paths. The legacy guide also describes a next-wave progress display; that UI
feature remains separate from the source-bound findings below.
[Scout research](../scout-and-specops.md)

Applies to **historical selected 2.3.1g**. Starting facts use the ordinary load;
career additions and other conditions are labeled separately.

| Key fact                 | Selected ordinary load                                            |
| ------------------------ | ----------------------------------------------------------------- |
| TP cost and availability | 6 TP; Reinforcements                                              |
| Health                   | 100 health points                                                 |
| Rifle skill              | Starts at 10 with random-stop 1–10 additions                      |
| Morale                   | 10–19 before career bonuses                                       |
| Experience               | 0 before career bonuses                                           |
| Starting equipment       | M1 Carbine; replaced with Garand by Meritorious Unit Commendation |

[Starting-stat evidence](../player-specialist-evidence.md)

On this page: [What the observer role does and does not promise](#what-the-observer-role-does-and-does-not-promise), [Do not assume every “spotter” claim is detection](#do-not-assume-every-spotter-claim-is-detection), [One infiltrator shortcut uses a different type name](#one-infiltrator-shortcut-uses-a-different-type-name), [Scout versus Spec Ops](#scout-versus-spec-ops), [Movement does not repeat the ordinary aiming restriction](#movement-does-not-repeat-the-ordinary-aiming-restriction).

## What the observer role does and does not promise

The Scout can satisfy one Allied mortar sight alternative under its health and
protection conditions; the mortar still has other target and camouflage checks.
The next-wave indicator is a separate shared-timer display, rather than a count
of arriving enemies. [Mortar sight condition](mortar.md#a-scout-or-sarge-can-satisfy-one-sight-alternative),
[indicator evidence](../player-recon-display-evidence.md).

The Scout's selected load type can match the artillery request's recon scan:
each passing entry adds 1 requested round, with separate health and flag tests. This is not an extra
guaranteed impact or a universal benefit from every Scout you hire.
[Artillery quantity and Spec Ops distinction](artillery.md#does-a-scout-add-shells-and-can-spec-ops-do-the-same),
[exact type/quantity join](../player-support-evidence.md#scout-type-and-the-artillery-recon-addition).
Source: [Source identities](../player-notes/scout.md#citation-1)

Do not buy it expecting automatic global detection of hidden enemies. Its own
target search still checks visibility, and the selected infiltrator detector's
literal Scout shortcut uses a type name different from this recruit's load.
Ordinary proximity/XP detection is separate, so that mismatch also does not mean
it can never reveal an infiltrator. [Target selection](../player-specialist-evidence.md#scout-and-spec-ops),
[exact detector/load comparison](../player-brandenburg-evidence.md#ready-detection-scan-and-the-scout-type-name-mismatch).

Selected historical **2.3.1g**. No universal detection radius, measured artillery
bonus or guaranteed next-arrival forecast is qualified here.

Combat Ribbon and Medal of Honor each add 3 rifle; Defence Expert Award adds 10
morale; Mud and Blood Cross adds 9 initial experience. A career equipment change
can therefore replace the base Carbine before combat. Judge the actual recruit
and loadout, not just the community equipment illustration.
[Load evidence](../player-specialist-evidence.md#scout-and-spec-ops)

## Do not assume every “spotter” claim is detection

The retained community Scout page specifically says planned infiltrator/sniper
detection was not implemented in its then-current patch. It also describes
mortar spotting and possible artillery assistance. Those are distinct claims,
and a specialty icon or a wave display does not prove global reveal of hidden
enemies in the selected binary. [Attributed ability limits](../scout-and-specops.md)

The player Scout's inspected target-selection condition still includes a
positive target-visibility test. That is another reason not to copy the Allied
Sniper's separate hidden-target selector onto this recruit.
[Selection binding](../player-specialist-evidence.md#scout-and-spec-ops),
[Sniper](sniper.md)

## One infiltrator shortcut uses a different type name

The selected hidden infiltrator's detection scan accepts qualifying nearby
player entries, with a closer-than-50 direct reveal and a farther-than-that,
strictly-below-200 XP comparison. Its literal automatic shortcut checks type
`scout`; this Allied Scout's load writes type `recon`. The unchanged load alone
therefore does not satisfy that shortcut. Generic proximity/XP detection still
exists, so this is not a promise that Scouts never detect an infiltrator.

With supplied type recon and XP 0, the longer-range XP roll admits no integer
0–99 input; the closer-than-50 branch remains separate. Later XP, actor state,
pillbox exclusion and geometry matter. This is a source mismatch, not a
reproduced runtime bug or measured universal spotting radius.
[Exact detector guards and load identity](../player-brandenburg-evidence.md#ready-detection-scan-and-the-scout-type-name-mismatch)
Additional source: [Source identities](../player-notes/scout.md#citation-2)

## Scout versus Spec Ops

The Scout's 6 TP versus Spec Ops 5 TP is not a strict stat-upgrade ladder. Scout
starts its rifle accumulator at 10 with morale 10–19; Spec Ops starts the
accumulator with a random 15–34 value and morale 30–59 before career additions.
Both then have their own subsequent load rules. Observation and combat roles
must be compared along with price. [Spec Ops](spec-ops.md)

No measured movement speed, infiltrator-detection radius or artillery bonus
rate is claimed here. These are concrete remaining mechanics questions, rather
than permission to treat an old table's pixel-per-second value as calibrated.

Sources: [Source identities](../player-notes/scout.md#citation-3). Selected 2.3.1g with separately attributed community abilities;
[exact evidence](../player-specialist-evidence.md).

The selected load also supplies specialization 11, read by the [Allied mortar](mortar.md#a-scout-or-sarge-can-satisfy-one-sight-alternative) sight alternative under health/protection guards. This does not bypass its other target or camouflage rules.
Additional source: [Source identities](../player-notes/scout.md#citation-4)

## Movement does not repeat the ordinary aiming restriction

The selected Scout controller can enter its movement section without an
`aiming == 0` check. The ordinary soldier's corresponding movement requires
that field to be 0. Wire, melee, destination, health, morale, pause and obstacle
conditions still apply; this does not prove a shot and translation occurred
together in a qualified original-game trial.

Its per-section movement coefficient is 0.8 versus the ordinary controller's
0.5. Those source numbers are not measured pixels per second. For declared raw
position (200,300), destination (200,400), rotation 90 and the exact clear-path
inputs, an aiming Scout can reach (200,300.8) at its write while the ordinary
aiming guard blocks that movement section.
[Exact supplied inputs and movement scope](../player-scout-controller-evidence.md#sharing-character-623-does-not-merge-the-two-placed-controllers)

The Scout also lacks the ordinary acquisition reset's immediate minimum-20
clamp. At supplied XP 20/draw 0, its reached reset writes 0 where the ordinary
reset writes 20 after clamping. That is a stage-specific counter difference,
not instant firing, an elapsed reaction result or a shared-timeline guarantee.
[Reset and later cap](../player-scout-controller-evidence.md#the-scout-acquisition-reset-has-no-ordinary-minimum-20-clamp)

## Its artillery contribution is extra requested quantity

The artillery menu adds **one requested round per qualifying recon entry**,
with health strictly above 10 and the source's separately spelled invincibility
flag condition. It does not add a range condition to that selected counting
scan. For a base draw of 1 round, no career quantity addition and two qualifying
recon entries, the local request becomes 3. Acceptance, payment and actual
shell emissions remain separate.
[Exact type/flag guards and quantity example](../player-scout-controller-evidence.md#artillery-counts-recon-entries-rather-than-a-generic-observer-ability)

This quantity write is not a precision bonus. Mortar spotting, infiltrator
detection and the community's next-wave display use different questions and
selectors; do not apply one observer label to every feature.
Additional sources: [Source identities](../player-notes/scout.md#citation-5)

| Observer question              | Selected source selector                   | What it supports                                                                   |
| ------------------------------ | ------------------------------------------ | ---------------------------------------------------------------------------------- |
| Mortar sight alternative       | Specialization 11, plus its actor guards   | Scout or Sarge can satisfy that alternative; other mortar conditions remain        |
| Artillery request quantity     | Type recon and its exact health/flag guard | One extra requested round per qualifying entry                                     |
| Infiltrator automatic shortcut | Literal type scout                         | Unchanged Scout load type recon does not match; generic close/XP detection remains |

Those are different mechanisms. A mortar spotter does not automatically qualify
for every artillery/detection rule, and none of these selected source paths
establishes the next-wave display's actual UI behavior.

## The wave indicator reads a shared timer after a separate enable decision

The selected indicator's child requests its frame from the shared wave timer
multiplied by 100/30 and rounded. Supplied timer 3/15/30 requests frames 10/50/100;
these are source inputs, not seconds remaining, enemies killed or a forecast
of the next composition. The child itself does not count living Scouts.

Early cadence separately scans qualifying recon entries, then requests the
enabled parent frame 2 or frame 1. Health must be above 10, and that scan uses the
separately spelled invincibility flag. Multiple qualifying Scouts select the
same enabled frame; they do not multiply this timer. The late-generator sibling
has no corresponding display-frame assignment at that site. Actual refresh,
rendering and paused callback behavior remain unqualified.
[Exact child, cadence boundary and retained inputs](../player-recon-display-evidence.md).

The ordinary truck-request branch reads that parent's current frame to choose
whether to request a warning; it does not repeat the Scout-health scan there.
A warning is neither proof the Scout is still healthy nor a truck-arrival receipt.
The separate enemy-Scout request has an empty corresponding message body in the
selected source, so its warning cannot simply be copied from the ordinary event.
[Exact warning-reader difference](../player-recon-display-evidence.md#the-ordinary-truck-warning-reads-the-selected-display-frame).
Additional source: [Source identities](../player-notes/scout.md#citation-6)

## Artillery quantity and Naval acceptance use the count differently

The selected Artillery offer adds 1 to its local requested quantity for each
indexed recon-type actor passing health>10 and the separately spelled
invincibility test. With base 3, no Ground Controller addition and two supplied
qualifying Scouts, the local quantity is 5; its accepted Artillery branch later
copies that quantity. This is requested quantity, not an extra guaranteed impact.

The Naval offer also adds those qualifying recon entries to a positive local
request marker. Its acceptance instead uses the current TP balance, rather than
that marker's number, for shared Naval quantity. Holding acceptance TP 10 fixed,
local markers 1 and 3 both lead to shared quantity 10 at that source write.
[Exact two-offer/acceptance comparison and supplied fields](../support-delivery.md#the-same-scout-count-reaches-different-artillery-and-naval-readers).

These scans are different from the Mortar's specialization 11 spotter match and
the wave indicator's enabled/disabled state. One useful Scout-related ability
does not establish every older spotting or support claim.
Additional sources: [Source identities](../player-notes/scout.md#citation-7)

## The starting initializer is not a final rifle range

Starting fields can receive loop additions and career effects before later
combat readers use them. The initializer alone is not a final range or accuracy
percentage. [Exact load scope](../player-random-stop-load-evidence.md#scout-and-spec-ops-add-two-bindings-to-the-existing-method)

## Detailed Scout/Spec Ops input means (not measured recruit averages)

Starting rifle skill includes the random-stop additions before career bonuses. The supplied-input averages in the note are mathematical means, not measured recruit averages or a universal accuracy comparison.

[Full source comparison and limitations](../player-notes/scout.md#technical-detail-1).

## Frequent grenade decisions can coexist with slower shooting

Modern comparison: the following observations and timing examples describe
the **November 7, 2026 simulation build**, not original Flash measurements.
See [dated study limits and later changes](combat-results.md).

Recon uses the ordinary firearm timeline but resets its decision counter without
Soldier's minimum 20. At high XP, another firearm decision can restart aiming
before the firing gate. It therefore cleared groups more slowly with several
guns despite its shorter decision reset.

Grenades are requested directly in the controller. Veteran Recon/Carbine
averaged G-only 16.90 launches per simulation minute; RG-only 8.97; both
G 9.12 plus RG 9.42. Keep G and RG separate because their flight distance bands
differ; these are launches, not measured kills. The small observed RG difference
between both and RG-only does not establish a bonus.
[Grenade methods and rates](grenades.md#measured-grenade-output-in-the-modern-simulation).

Recon can move during aiming states and uses a higher movement coefficient than
Soldier; this is not a measured moving-fire advantage.
[Lifecycle and interrupted preparation](unit-lifecycle.md),
[pending modern correction](combat-issues.md).
