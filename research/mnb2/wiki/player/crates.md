[Player reference](README.md) · [Support](support.md) · [Tactical points](tactical-points.md)

# Crates: rewards depend on the selected outcome and collection path

A crate's arrival, selected reward, eligible collection and final effect are
separate questions. In selected historical **2.3.1g**, the collection branch needs an indexed actor with
defined health at least 10 and distance strictly below 50. Do not equate a drawn
crate or its name with an already delivered squad-wide reward.
[Crate source](../crates.md)

On this page: [Check the collector, then the selected reward](#check-the-collector-then-the-selected-reward) · [The collector and the group can receive different rewards](#the-collector-and-the-group-can-receive-different-rewards) · [Enemy collection calls a generator](#enemy-collection-calls-a-generator) · [One “Vital intel” branch is unreachable in this chain](#one-vital-intel-branch-is-unreachable-in-this-chain) · [Breakup debris is not a normal collection receipt](#breakup-debris-is-not-a-normal-collection-receipt) · [The Pie Ribbon is a separate roll from the crate reward](#the-pie-ribbon-is-a-separate-roll-from-the-crate-reward) · [Logistics changes a request roll, not a guaranteed arrival interval](#logistics-changes-a-request-roll-not-a-guaranteed-arrival-interval) · [A crate-shaped cover binding is not every supply crate](#a-crate-shaped-cover-binding-is-not-every-supply-crate)

## Check the collector, then the selected reward

- The selected eligible collector gets **3 XP and a promotion check before the
  random outcome**. That is separate from a later group reward and does not
  guarantee a rank increase.
- Some morale/XP/rifle reward loops include qualifying allies without repeating
  the collector's distance check. Do not assume every reward goes only to the
  nearest soldier, or that every slot receives it.
- A crate breaking into contents is not a collection receipt. Blast cleanup has
  a separate path without that direct collection reward; enemy pickup instead
  calls a generator, rather than selecting another allied reward.

[Collector and group evidence](../player-crate-collection-evidence.md),
[cleanup versus collection](../player-pickup-blast-evidence.md).
These are selected **2.3.1g** stages, not guaranteed pickup order, arrivals or
rewards inferred from the drawing. The outcome table follows.

| Selected outcome         | Concrete source finding                                               |
| ------------------------ | --------------------------------------------------------------------- |
| Rations                  | +1 TP at the eligible reward write                                    |
| Maps and new orders      | +2 TP                                                                 |
| Ammunition               | +3 TP                                                                 |
| Letters from home        | +5 morale to qualifying group recipients                              |
| Field manuals            | +5 XP and a separate rank-helper call for qualifying group recipients |
| Weapon manuals           | +5 rifle to qualifying group recipients                               |
| Detailed orders          | −15 local wave, not a write to mission total at that site             |
| Soldier / airborne intel | Different non-Airborne spawn and Airborne missed-counter branches     |
| Armor plates             | An inner eligible armored/living-recipient loop adds 100 health       |
| Comfort supplies         | No parameter/call gameplay reward listed in those selected branches   |

These are source-site effects, not a universal statement about which actors get
every reward after removal/loop/callback ordering. TP has a later conditional
cap write; the armor addition is not an infantry armor-conversion guarantee.
[TP](tactical-points.md), [exact crate bindings](../player-interaction-evidence.md#crates-and-controls)

For Detailed Orders, compare [local medals, mission-total milestones and career
waves](waves.md#did-detailed-orders-set-back-my-wave-progress) before interpreting
the local reduction as a loss of every kind of progress. The three counters have
different readers; the selected crate branch does not itself verify a save loss.

## The collector and the group can receive different rewards

The eligible collector receives **+3 experience and a promotion-helper call
before the random crate outcome**. That is separate from Field manuals, which
can later add 5 XP and call the helper for qualifying group recipients. An XP
addition does not itself guarantee a new rank.

Letters, Field manuals and Weapon manuals scan player indices with health at
least 10. Those inner group loops do not repeat the collector's distance check;
a distant qualifying ally is not excluded just for being far from the crate.
The collector can also qualify for the group write. Armor plates instead scans
positive-health armored recipients, adds 100 health and has no local maxhealth
cap at that addition. This is not automatic repair of lost crew.
[Collector versus group bindings](../player-crate-collection-evidence.md#group-recipients-do-not-repeat-collector-proximity)

Collection admission itself has no armor restriction at that selected site.
Do not infer a universal “infantry only” rule from the crate drawing. Actual
movement, receiver validity and removal ordering remain separate.
[Collector admission](../player-crate-collection-evidence.md#the-collector-gets-a-reward-before-the-selected-crate-outcome)

## Enemy collection calls a generator

The selected enemy pickup path calls the wave generator, rather than drawing
another allied reward or supplying a fixed number of arrivals. Unarmored
candidates need positive health; the armored alternative has a separate
positive driver+gunner sum. The exact source guards and callback order matter
before predicting a real pickup or the resulting wave.
[Enemy pickup and call](../player-crate-collection-evidence.md#enemy-collection-is-not-another-selector-roll)

## One “Vital intel” branch is unreachable in this chain

The ordered source handles selector 6 as Weapon manuals before a later Vital intel
branch tests 6 again. Its conditions therefore require both not 6 and 6, giving no
selected draw values in that particular chain. It should not be assigned a
positive chance by counting displayed reward names. This does not prove every
other game version lacks a similar reward or that historical reports were invented.
[Contradictory selected branch](../crates.md)

Comfort supplies use selector 10 and 11, whereas the known+5 morale write is under
Letters from home. A community suggestion that comfort should boost morale is
not an implemented source effect by itself.

Detailed Orders can matter differently to local-wave-based enemy initializers,
mission totals and career accumulation. It does not remove existing enemies or
retroactively reroll them from this single subtraction alone.
[Wave counters](waves.md), [enemy load defaults](enemy-stats.md)

Sources: [Source identities](../player-notes/crates.md#citation-1).
Selected 2.3.1g; [exact evidence](../player-interaction-evidence.md).

Additional source: [Source identities](../player-notes/crates.md#citation-2). [Collection/source identities](../player-crate-collection-evidence.md).

A [downed pilot](pilot-recovery.md) is a different collection object: its selected
friendly receipt gives the collector 3 XP and 1 TP, while enemy pickup subtracts 1 TP.
It does not draw this crate's random reward selector.

## Breakup debris is not a normal collection receipt

The shared blast helper has an earlier scenery path that can invoke crate
breakup and request its removal. That breakup helper does not directly select
a crate reward, grant collector XP/TP or increment the recovered-crate counter.
The fourteen named supply-template event pairs have their own finite fade and
motion path; those bodies do not contain a collection-reward helper call.
Actual emitted-object scheduling and later interactions still need qualification. Do not identify a successful pickup from spilled contents alone.
[Exact cleanup versus collection source](../player-pickup-blast-evidence.md).
Additional source: [Source identities](../player-notes/crates.md#citation-3)

## The Pie Ribbon is a separate roll from the crate reward

One admitted friendly collector visit draws its normal reward selector, then
has a separate random 0–9999 comparison equal to 1 for the Pie Ribbon's guarded
award branch. That is not another value in the 1–11 reward selector, and it does
not replace the later normal outcome chain. One passing comparison value is
not a guaranteed award after 10,000 crates or a unique-pickup count.
[Collector, selector and Pie ordering](../player-crate-collection-evidence.md#the-collector-gets-a-reward-before-the-selected-crate-outcome).

## Logistics changes a request roll, not a guaranteed arrival interval

At the selected unpaused frame 14 request action, no Logistics flag admits 1 of
300 integer inputs; a supplied flag 1 admits 2 of 300. That doubles this one
comparison's passing count, rather than establishing a 2% chance, a crate every
fixed number of seconds or twice the measured reward rate.

The request targets a named cratemc template. The accepted source has two
physical placements with that name, so this guide preserves the unresolved
lookup boundary. Separately reached falling-crate actions increment the crate
statistic and later request a ground pickup; collection and blast cleanup are
still different stages. [Exact request, named stages and identities](../player-crate-delivery-evidence.md).
Additional source: [Source identities](../player-notes/crates.md#citation-4)

## A crate-shaped cover binding is not every supply crate

The direct drawing inventory gives character 1579 a named ordinary-cover child.
The accepted template map also has a different character 836 with the same
cratemc placement name in the arrival/reward path. Do not transfer character 1579's child
or its actual overlap to every delivered crate, or treat that naming boundary
as a resolved runtime lookup.
[Exact cover and identity scope](../player-scenery-cover-evidence.md#the-full-named-cover-inventory-contains-eight-direct-placements),
[scenery player guide](scenery-and-cover.md).
Additional source: [Source identities](../player-notes/crates.md#citation-5)

The selected 1579 scenery load actually tags the crate-shaped object as tree.
A separately admitted blast scenery query therefore follows that type field,
while ordinary cover follows the named child. Its constructed dead-template
lookup remains unresolved in the accepted map; this does not certify a reward
or a runtime bug on the different character 836 arrival/collection path.
[Exact load and helper/name boundary](../player-tree-tagged-crate-evidence.md).
Additional source: [Source identities](../player-notes/crates.md#citation-6)
