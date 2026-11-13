[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Role comparison](recruitment.md#choose-the-job-before-the-price)

# Spec Ops

A **5-TP combat recruit** with a Grease Gun and grenade capability in its
selected load profile. Its starting rifle accumulator and morale differ from
ordinary recruits; that does not by itself certify an optimal purchase or
universal immunity to retreat. [Source and community comparison](../scout-and-specops.md)

Applies to **historical selected 2.3.1g**. Starting facts use the ordinary load;
career additions and other conditions are labeled separately.

| Key fact                 | Selected ordinary load                                            |
| ------------------------ | ----------------------------------------------------------------- |
| TP cost and availability | 5 TP; Reinforcements                                              |
| Health                   | 100 health points                                                 |
| Rifle skill              | Starts with a random 15–34 value, then random-stop 1–10 additions |
| Morale                   | 30–59 before career bonuses                                       |
| Experience               | 0 before career bonuses                                           |
| Starting equipment       | Grease Gun                                                        |
| Grenade capability       | Enabled in the inspected load profile                             |

[Starting-stat evidence](../player-specialist-evidence.md)

On this page: [A combat load, not a universal upgrade to every role](#a-combat-load-not-a-universal-upgrade-to-every-role), [Another offer can request this template](#another-offer-can-request-this-template), [What the higher base stats do and do not mean](#what-the-higher-base-stats-do-and-do-not-mean), [Its own firing preparation differs from the ordinary soldier](#its-own-firing-preparation-differs-from-the-ordinary-soldier), [Low morale alone does not select its ordinary withdrawal branch](#low-morale-alone-does-not-select-its-ordinary-withdrawal-branch).

## A combat load, not a universal upgrade to every role

Compare Spec Ops with a Scout by the **job you need**: the selected Spec Ops
load brings a Grease Gun and grenade capability, while the Scout's observer
paths are different. The higher starting expressions below are not final hit
percentages or proof of better kills per TP. [Load and role evidence](../player-specialist-evidence.md#scout-and-spec-ops),
[Scout](scout.md).

For artillery quantity, the selected Spec Ops load's sas type is different from
the Scout's recon type. With those fields unchanged, it does not automatically
supply the Scout's contribution to that request scan. Compare
[the artillery recon bonus](artillery.md#does-a-scout-add-shells-and-can-spec-ops-do-the-same)
before substituting the cheaper combat recruit for the observer role.
[Exact load and request guards](../player-support-evidence.md#scout-type-and-the-artillery-recon-addition).
Source: [Source identities](../player-notes/spec-ops.md#citation-1)

Grenade capability still needs the actor's attack choice and launch conditions.
Likewise, the old no-retreat description is not a qualified universal immunity
in selected **2.3.1g**. [Grenade rules](grenades.md),
[exact morale-branch limits](../player-morale-branch-evidence.md#the-or-guard-is-not-a-spec-ops-or-paratrooper-exclusion).

The rifle initializer is not simply a fixed 15–34 final stat: it subsequently
adds random values until a random stopping rule ends the loop. Combat Ribbon
and Medal of Honor each add 3 rifle points; Defence Expert Award adds 10 morale;
Mud and Blood Cross adds 9 initial experience. Keep those career additions
separate from the base rolls. [Exact load bindings](../player-specialist-evidence.md#scout-and-spec-ops)

## Another offer can request this template

The ordinary Spec Ops button costs 5 TP. Separately, the 1-TP Resistance offer
has a Special Operations Ribbon-dependent substitution branch that requests the
same Spec Ops template instead of Resistance. With supplied medal value 1 and
a uniform 0–99 draw, one value qualifies. The selected Resistance body does not
repeat the direct Spec Ops button's persistent recruitment-counter increment.
[Exact template and counter distinctions](../player-recruitment-receipt-evidence.md#resistance-can-request-the-spec-ops-template-instead)
Additional source: [Source identities](../player-notes/spec-ops.md#citation-2)

## What the higher base stats do and do not mean

The higher morale and rifle starting expressions are direct differences from
the Regular Soldier and Scout. Later accuracy still depends on the firing path,
distance, target state and current weapon. Grenade capability does not guarantee
a throw on a chosen frame or remove friendly-fire risk.
[Regular Soldier](regular-soldier.md), [Scout](scout.md),
[fragmentation research](../fragmentation-blast.md)

The community describes Spec Ops as unwilling to flee and recommends particular
upgrades. The inspected fear/death source conditions include compound type/armor
tests that must not be simplified into a clean universal no-retreat exception.
For a stable sas type, the separate “not para” OR term remains true, so that
particular guard does not exempt Spec Ops. Other entry/retreat conditions and
runtime outcomes still need qualification. [Exact source comparison](../player-morale-branch-evidence.md#the-or-guard-is-not-a-spec-ops-or-paratrooper-exclusion)
Treat the historical advice as attributed until the full paths and versions are
qualified. [Morale and retreat differences](../morale.md)

Choose between Scout and Spec Ops by the needed role, not solely by price or
one rifle roll. The Scout's claimed observer features and the Spec Ops recruit's
combat load are different capabilities. No comparative kills-per-TP experiment
or universal “best upgrade” is claimed by these starting profiles.

Sources: [Source identities](../player-notes/spec-ops.md#citation-3). [Version and exact evidence](../player-specialist-evidence.md)

## Its own firing preparation differs from the ordinary soldier

The selected Spec Ops preparation action initializes a **Grease Gun burst
counter 1–10**. Its Garand/Carbine preparation uses a **semi counter 1–5**, versus
ordinary soldier 1–3. These are initialized fields, not guaranteed bullets or hits.
The inspected ordinary preparation has no fresh Grease-code initializer there;
old repeat fields and weapon-replacement timing still matter.
[Exact preparation](../player-spec-ops-combat-evidence.md#preparation-has-a-grease-gun-initializer-and-larger-semi-bound)

Its retained firing and repeat action bodies match the ordinary soldier's
byte-for-byte. That does not make their entire cycles identical: current counters,
ammo, controller entry and recovery differ or need their own bindings. The
shared Grease helper also penalizes the roll by current positive burst before
its distance modifier; a long initialized counter is not uniformly accurate fire.
[Fire/repeat readers and declared example](../player-spec-ops-combat-evidence.md#fire-and-repeat-bodies-match-but-their-inputs-can-differ)

At the selected healthy/unpaused/moving 1 recovery branch, empty Grease ammo refills
to 30 with counter 150−XP; nonempty recovery uses 10+random 0–149−XP. Its own pin
recovery also omits the ordinary soldier's flee-field contribution and later
morale/flee choice. These source differences do not certify a retreat immunity,
recovery duration or damage-per-second advantage.
[Recovery comparison](../player-spec-ops-combat-evidence.md#pin-recovery-has-a-different-flee-branch)
Additional source: [Source identities](../player-notes/spec-ops.md#citation-4)

## Low morale alone does not select its ordinary withdrawal branch

The selected Spec Ops active controller tests withdrawal without the ordinary
soldier's **morale above 0** requirement. At supplied morale 0/withdraw 0, that
one condition can pass for Spec Ops while failing for the ordinary soldier.
The remaining health, pause, pinning, protection, counter and target conditions
still apply. This supports a specific part of the historical trait, rather than
making Spec Ops immune to every fear or retreat mechanism.
[Exact admission comparison](../player-spec-ops-combat-evidence.md#low-morale-alone-does-not-select-this-controllers-withdrawal-alternative)

Morale still enters its own pin-recovery comparison. A withdrawal value of 1
also fails that active condition and has its separate unpinned exit behavior.
Do not read the missing morale gate as an ignored withdrawal order or guaranteed
ability to fire while pinned.
[Withdrawal and field scope](../player-spec-ops-combat-evidence.md#a-withdrawal-order-is-still-a-different-input)

Its movement section retains `aiming == 0`, unlike the Scout's selected movement
path. Its 0.7 source step coefficient versus ordinary 0.5 is not a measured
speed in pixels per second. The later positive-counter cap is separately bound;
none of these facts collapses its whole combat cycle into the ordinary model.
[Movement and later counter readers](../player-spec-ops-combat-evidence.md#movement-still-waits-for-the-aiming-field)
Additional sources: [Source identities](../player-notes/spec-ops.md#citation-5)

The selected direct Spec Ops offer increments the career highspeed counter,
as does the separate direct Sniper offer. That counter's at-least 100 condition
feeds the Special Operations Ribbon. Resistance's possible Spec Ops substitution
has no such increment in its own offer body. These are source request/accounting
distinctions, not a count of specialist kills or verified healthy recruits.
[Exact producers, waiver and award boundaries](../player-special-deployment-evidence.md).
Additional source: [Source identities](../player-notes/spec-ops.md#citation-6)

## The starting initializer is not a final rifle range

Starting fields can receive loop additions and career effects before later
combat readers use them. The initializer alone is not a final range or accuracy
percentage. [Exact load scope](../player-random-stop-load-evidence.md#scout-and-spec-ops-add-two-bindings-to-the-existing-method)

## Detailed Scout/Spec Ops input means (not measured recruit averages)

The initial rifle roll is not the final range: mandatory and later random-stop additions still follow before career bonuses. The note’s means are mathematical input means, not measured recruits or actual hit rates.

[Full source comparison and limitations](../player-notes/spec-ops.md#technical-detail-1).

## Why equal stats do not mean a faster Soldier

Modern comparison: the following observations and timing examples describe
the **November 7, 2026 simulation build**, not original Flash measurements.
See [dated study limits and later changes](combat-results.md).

Spec Ops initializes Garand/Carbine repeat counters at 1–5, versus Soldier's
1–3. The subsequent firing/repeat bodies are shared, but their inputs differ.
Longer sequences can help sustained dummy damage and waste shots after a target
dies. In the modern veteran group test, Spec Ops/Garand averaged 83.64 seconds
at medium distance versus Soldier's 69.50; Springfield, Thompson and BAR matched.

Its native Grease has explicit burst preparation. Its controller does not
require positive morale for the active branch, but it can still be pinned and
obeys withdrawal. Movement uses a higher coefficient than Soldier while still
waiting for aiming to clear.
[Exact source distinctions](../player-spec-ops-combat-evidence.md),
[measured results](combat-results.md), [lifecycle](unit-lifecycle.md).
