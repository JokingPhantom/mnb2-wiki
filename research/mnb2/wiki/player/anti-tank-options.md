[Player reference](README.md) · [Anti-tank options](anti-tank-options.md) · [Vehicles and emplacements](vehicles-and-emplacements.md)

# Choosing anti-tank support

Choose around the job you need the unit to perform: acquiring a nearby armored
enemy, covering a distant target, or attacking an area. In the selected **2.3.1g**
source, these options differ before the explosion's damage rules even run.
A base price is not a promise that every mode exposes the offer or that a
purchase/placement completes.

On this page: [What the base purchase buys](#what-the-base-purchase-buys) · [A minimum selection distance is not a safe radius](#a-minimum-selection-distance-is-not-a-safe-radius) · [Crowding and readiness can prevent the request](#crowding-and-readiness-can-prevent-the-request) · [Rocket travel and scattered effects are different risks](#rocket-travel-and-scattered-effects-are-different-risks) · [A sticky bomb uses the TNT tag against a Tiger](#a-sticky-bomb-uses-the-tnt-tag-against-a-tiger)

## Match the purchase to the current gap

Compare a 4-TP [Bazooka](bazooka.md) when you need a mobile anti-armor shooter,
an 8-TP [M3](m3-at-gun.md) when its placement/crew requirements fit, and a 20-TP
[Sherman](sherman.md) when you can afford the larger commitment and its later
support. These are tactical choices, not measured vehicle kills per TP.

An AT mine costs **5 TP from scratch** with Engineer 4 + mine 1, or 1 additional
TP with an eligible Engineer already present. A cheap trigger is not
interchangeable with a shooter, and friendly armor can trigger it. A 2-TP sticky
bomb also requires an eligible Paratrooper; the placement price omits that
prerequisite. Compare all prerequisites in the table below.

For a worked decision with adaptation and failure checks, read the
[armor-response plan](strategy-studies.md#answer-armor-before-committing-to-a-tank-transition).
It explains the cost of maintaining an interim answer while saving for a tank.
[Edition identity](editions.md) matters before reusing an old guide.

## What the base purchase buys

| Option                                     | Base TP commitment                               | Selected targeting or control distinction                                                                   |
| ------------------------------------------ | ------------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| [AT mine](mines.md)                        | 1 per mine; Engineer separately                  | Armored trigger filter includes friendly vehicles; later effect has its own AT/fragment guards              |
| [Sticky bomb](sticky-bomb.md)              | 2 per placement; eligible Paratrooper separately | Separate pointer-based validation and later closest-armored follow scan; emitted TNT uses its own tag       |
| [Bazooka soldier](bazooka.md)              | 4                                                | First eligible armored index before its fallback; creates a moving rocket with intermittent proximity scans |
| [M3 AT gun](m3-at-gun.md)                  | 8                                                | Armor-priority pass; distant-target fallback; nearby same-name guns can inhibit its firing request          |
| [Sherman](sherman.md)                      | 20                                               | Armor-priority turret, cannon/coax choices and a separate optional .50 system                               |
| [Halftrack 75 mm AT](halftrack-weapons.md) | 12 base vehicle + 12 conversion = 24             | The selected weapon scan needs target distance strictly above 400, including armored candidates             |
| [Rocket launcher](rocket-launcher.md)      | 20; separate empty refill costs 1                | Guarded fire button and cooldown; impact coordinate draws do not follow a designated enemy                  |

These are base menu amounts, before conditional waivers, other purchases or
failed transactions. The Halftrack conversion replaces its module role; the
24-TP arithmetic is not a package button or a stack of all earlier module benefits.
The rocket launcher's loaded counter, cooldown and refill are separate states.
[Halftrack receipts](halftrack.md), [launcher button](rocket-launcher.md#fire-and-refill-are-different-button-states)

## A minimum selection distance is not a safe radius

The M3's first pass can select a living armored target with line of sight
without the fallback's greater-than-400 restriction. The Halftrack AT weapon's
selected scan has that greater-than-400 gate directly. At a **supplied helper
distance of 400**, that Halftrack condition fails; its 401 comparison passes,
provided the other filters pass. This does not promise a completed shot.
[M3 evidence](../player-mounted-evidence.md#target-selection-and-spacing),
[Halftrack evidence](../player-halftrack-weapons-evidence.md#ready-target-searches-and-timer-reset)

The Sherman's turret likewise keeps its greater-than-300 rule in the fallback,
not its first armor pass. Its optional .50 has a different fallback and target
field; a gun icon does not mean all its weapons aim at the same enemy.
[Sherman component comparison](sherman.md#its-guns-can-acquire-different-targets)

Those selection thresholds do not prevent a scattered impact from landing
closer to another actor. They do not establish a friendly-fire boundary or a
safe gap between your troops and the target. Actual effect placement and blast
recipient checks remain separate.

## Crowding and readiness can prevent the request

An M3's spacing scan counts other indexed entries named M3 AT gun strictly
below helper distance 100, without checking their health or crew in that scan.
A nonfiring or damaged neighboring entry is therefore not automatically ignored.
Exactly 100 fails that closeness comparison; this is a source-distance boundary,
not a measured screen-placement guarantee.
[M3 spacing](m3-at-gun.md#why-it-may-not-fire)

The Halftrack AT controller needs its gunner and other state gates. The M3
instead uses a positive driver-plus-gunner sum in its selected controller.
The launcher's fire button accepts driver exactly 1 or gunner exactly 1, with
its own bunker/cooldown checks. One generic rule about being crewed cannot
replace those different readers. [Crew replacement](crewman.md) is another
transaction, while [Mechanic repair](mechanic.md) changes health through its
own recipient rules.

## Rocket travel and scattered effects are different risks

The Bazooka's selected rocket moves before sampling nearby enemies. A match
creates the blast at the sampled rocket point, not at the enemy's center.
A supplied distance 40 can pass the below-50 trigger while failing the later
below-25 AT distance gate if the raw shared-coordinate points remain unchanged.
This does not settle every other blast removal path.
[Bazooka point example](bazooka.md#the-blast-starts-at-the-sampled-rocket-point)

M3, Sherman cannon and Halftrack AT firing actions instead place effects around
the target's later coordinates using separate integer axis offsets −100..99.
Their listed rifle fields do not tighten those inspected placement expressions.
The rocket launcher samples area coordinates without those selected-target
position reads. These are different attack mechanisms; their menu cost, damage
input or visible explosion size alone does not rank vehicle kills per TP.
[AT recipient rules](anti-tank-and-vehicles.md), [explosion stages](explosion-damage-stages.md)

Sources: [Source identities](../player-notes/anti-tank-options.md#citation-1). Original synthesis
of the linked selected-source notes; no new trial, hit probability or timing recipe.

## A sticky bomb uses the TNT tag against a Tiger

The sticky bomb's selected effect supplies AT radius 25 and tag tnt. A separately
admitted armor-2 Tiger on that tag takes the direct wreck/removal branch; the
500-health subtraction exception specifically requires tag zooka. Equal AT
radius inputs therefore do not make these two weapon paths equivalent.

Every recipient, distance, visibility, protection and lifetime guard still needs
to pass. This source distinction does not establish that a 2-TP placed bomb
always attaches, detonates or removes a vehicle, or that it has better kills
per TP. [Exact effect chain and declared tag comparison](../player-sticky-tiger-evidence.md).
Additional sources: [Source identities](../player-notes/anti-tank-options.md#citation-2)

The [ordinary/AT mine comparison](mines.md) also shows why a dedicated AT trigger
does not imply a larger AT-radius input. Both selected effects pass 50; their
trigger filters, fragment inputs and literal tags differ. That scalar equality
is not a whole-weapon performance comparison or a safe friendly-vehicle route.
[Exact trigger, effect and ownership boundaries](../player-mine-effect-evidence.md).
Additional source: [Source identities](../player-notes/anti-tank-options.md#citation-3)
