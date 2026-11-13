[Player reference](README.md) · [Construction](construction.md) · [Explosives](explosives.md)

# Mines, booby traps, TNT and sticky bombs

Placement eligibility, trigger detection, a later explosion and damage recipients
are separate stages. A nearby trigger is not automatically a lethal hit, and
these paths include friendly-fire risks with their own armor/health conditions.
[Explosive evidence](../player-interaction-evidence.md#construction-and-explosives)

Historical scope: selected **2.3.1g** source.

On this page: [Which offer matches the job?](#which-offer-matches-the-job) · [Ordinary and AT mines](#ordinary-and-at-mines) · [A mine trigger does not center the blast on the vehicle](#a-mine-trigger-does-not-center-the-blast-on-the-vehicle) · [Booby trapping is another application](#booby-trapping-is-another-application) · [TNT has several kinds of state](#tnt-has-several-kinds-of-state) · [Sticky-bomb placement does not freeze a vehicle identity](#sticky-bomb-placement-does-not-freeze-a-vehicle-identity)

## Which offer matches the job?

These are **selected historical 2.3.1g** base offers. Recruiting the required
specialist and supplying a host mine/TNT for rigging are separate commitments.
The linked cards give the retained placement, payment and later-effect evidence.

| Choice                        | Base offer cost                                  | What to arrange before expecting an effect                                                                                 |
| ----------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| [Ordinary mines](mines.md)    | 1 TP for three placement requests                | Eligible Engineer and later placement; ordinary triggers can consider friendly troops as well as enemies                   |
| [AT mine](mines.md)           | 1 TP for one placement request                   | Eligible Engineer and later placement; its armored trigger includes qualifying friendly vehicles                           |
| [Placed TNT](tnt.md)          | Normally 2 TP, or a recovered charge spent first | Eligible Engineer/proximity for placement; the placed object's release has separate explosion-versus-rigging behavior      |
| [Booby trap](booby-trap.md)   | 1 TP application                                 | An existing eligible mine/TNT and later Engineer/proximity receipt; it does not buy another standalone mine                |
| [Sticky bomb](sticky-bomb.md) | 2 TP placement ability                           | Eligible Paratrooper and placement checks; the later armored-follow scan need not retain the originally considered vehicle |

[Carried hand and rifle grenades](grenades.md) are separate equipment choices,
with their own recipient and attack-decision rules. More expensive equipment or
an armored trigger does not establish a stronger blast or a better vehicle-kill
rate. Placement, triggering and actual damage remain separate below.

## Ordinary and AT mines

The ordinary 1-TP offer has three explicit placement emissions: at the stored
mouse coordinates, plus (50, 50), and plus (−50, 50) in source coordinates. That is
not a measured gap-free barrier. AT mines have a separate 1-TP offer and object.
[Placement sources](../mines.md)

Both variants scan player and enemy slots with strict distance-below 25 tests.
The AT variant additionally requires positive armor at the cited trigger sites;
the ordinary variant does not. Player/enemy health gates also differ. Triggering
and the explosion's eventual recipients are different tests, so do not assume
an AT mine is a universal no-friendly-fire device.

## A mine trigger does not center the blast on the vehicle

Both selected mine trigger bodies place the new effect at the **mine's own
point**, rather than copying the triggering actor's center. The player health
threshold is at least 10; the enemy threshold is above zero. With all other
trigger guards passing, a wounded ally at health 9 fails that player threshold,
while an enemy at health 9 passes its health part. Neither comparison is the
later blast's recipient test.
[Exact point/health readers](../player-mine-effect-evidence.md#the-effect-is-placed-at-the-mines-point)

The later ordinary and AT mine effects both supply **AT radius 50** and damage
input 100. Their fragment inputs differ, 75 versus 100, and their literal tags
are mine versus naval. An AT mine's armored trigger filter is therefore not
proof of a larger AT-radius input or a no-friendly-fire rule. Blast recipients,
owner credit and full geometry still need their separate guards.
[Effect argument table](../player-mine-effect-evidence.md#effect-arguments-retain-different-roles-and-tags)

## Booby trapping is another application

The 1-TP booby-trap offer enables a cue. Eligible mine/TNT object handlers then
set a flag and debit under their own closeness/affordability/not-already-trapped
conditions. One selected Pioneer interaction emits a blast **at the Pioneer**,
while removing the scanned trapped object. Its career-counter increment is not
itself proof the Pioneer died or every ally is safe. [Booby-trap chain](../booby-trap.md)

## TNT has several kinds of state

A positive shared recovered-charge pool is spent **before TP**, even when you
could afford the normal 2-TP fee. With no stored charge, the selected Sapper
commendation branch can waive that fee, but the ordinary 2-TP affordability gate
still comes first. One TP and no charge cannot enter placement just by rolling
a waiver. A charge also does not bypass the eligible Engineer/proximity checks.
[Exact spending order and examples](../player-defuse-evidence.md#spending-recovered-tnt)

Successful selected placement creates TNT at the mouse coordinates and increments
the construction counter even when it spends a recovered charge. Interdiction
Ribbon has a separate 10-of-100 conditional roll to booby-trap the placed object.
That flag does not establish a casualty or complete blast outcome.

Pioneer drops, collection, stored charges and placed TNT are distinct stages.
The dropped-TNT countdown has no pause test in its own body; full event scheduling
is needed before claiming pause safety. [Pickup and timer](../pioneer-and-tnt.md)
[Duds](duds.md) use another autonomous check and a different defuse failure path.

The TNT effect calls rock and bunker/palisade scenery helpers before its generic
explosion helper. Their strict distance/type conditions differ: cited rock
removal below 30, bunker below 25, palisade below 45. Those are helper comparisons,
not measured artwork-edge clearance or one universal blast circle.
[Scenery removal](../scenery-demolition.md)

## Sticky-bomb placement does not freeze a vehicle identity

The airborne 2-TP offer checks eligible Paratroopers, then separate pointer-based
proximity/armored-target conditions before payment and object creation. The
bomb's later callback has its own closest eligible armored-enemy scan and position
writes. It is not simply an immutable copy of whichever vehicle the placement
validator considered. Fuse/attachment/detachment and final destruction still
need complete state/geometry binding. [Sticky bomb](../sticky-bomb.md)

The Tiger/bazooka exception and other AT recipient guards are explained separately;
a generic explosive label should not replace them.
[AT and vehicle handling](anti-tank-and-vehicles.md)

Sources: [Source identities](../player-notes/explosives.md#citation-1).
[Exact source notes](../player-interaction-evidence.md)

Both mine tags also admit the shared blast helper's conditional structural
removal call. That happens before its later recipient protection queries;
checking only the mine effect body's own calls would miss this shared stage.
[Ordered structural dispatch](../player-blast-dispatch-evidence.md).
Additional source: [Source identities](../player-notes/explosives.md#citation-2)

The [sticky-bomb player card](sticky-bomb.md) collects its separate placement,
following, fuse and guarded TNT-tag/Tiger branches. Its 2-TP ability cost does
not establish a measured vehicle kill rate.
[Actual effect and supplied AT comparison](../player-sticky-tiger-evidence.md).
Additional source: [Source identities](../player-notes/explosives.md#citation-3)

[Ordinary and AT mines](mines.md) now have a standalone player comparison of
purchase, trigger and later effect stages. The [placement/counter evidence](../player-mine-placement-evidence.md)
keeps nominal three-mine requests separate from the one career construction
increment in that selected completion.
Additional source: [Source identities](../player-notes/explosives.md#citation-4)

[Placed TNT and recovered stock](tnt.md) now have a player card, alongside
[booby-trap application](booby-trap.md). The selected placed-TNT release handler
requests an explosion outside the active rigging cue; with that cue active it
takes a separate rigging receipt, with its own cancellation and already-rigged
outcomes. A mine's release has a different default path.
[Exact release-mode comparison](../player-booby-mode-evidence.md).
Additional source: [Source identities](../player-notes/explosives.md#citation-5)
