[Player reference](README.md) · [Training and equipment](training-and-equipment.md) · [Purchase budgets](purchase-budgets.md)

# Ranger Training

Ranger Training is a **5-TP upgrade whose effects depend on the recipient**. Regular Soldier and Scout training switches the shared weapon to Garand and adds random rifle skill and morale. The Sniper gets fixed additions without that weapon replacement. A weapon-field change on a Bazooka soldier does not by itself establish a change to its later rocket attack. [Exact offer and receipts](../ranger-training.md)

Historical scope: selected **2.3.1g** source; offer, recipient and later
combat effects are separate stages.

| Key fact              | Selected historical behavior                                                       |
| --------------------- | ---------------------------------------------------------------------------------- |
| Advertised cost       | 5 TP, or the admitted free-training allowance                                      |
| Spending stage        | Offer consumes payment/allowance before recipient training                         |
| Regular/Scout receipt | Grenades, separate 1–15 rifle/morale draws, Garand replacement                     |
| Other recipients      | Sniper fixed additions; Bazooka field write does not replace rocket implementation |

On this page: [Payment or allowance comes before the recipient](#payment-or-allowance-comes-before-the-recipient) · [The trained actor determines the writes](#the-trained-actor-determines-the-writes) · [Will training keep a BAR I already bought?](#will-training-keep-a-bar-i-already-bought) · [Bazooka training does not import the rifle actor's whole implementation](#bazooka-training-does-not-import-the-rifle-actors-whole-implementation) · [Clearing the pending choice does not itself restore the free allowance](#clearing-the-pending-choice-does-not-itself-restore-the-free-allowance)

## Payment or allowance comes before the recipient

The offer admits at least 5 TP or freeTrain exactly 1. The paid path subtracts 5;
the allowance path does not. Both set the pending training mode and clear the
allowance before a recipient receives its changes. Earlier pending equipment
can take priority in the later live-recipient handler.

The selected initialization clears freeTrain, then grants 1 when medal35 is
exactly 1. The award catalog calls that flag **Xmas Ribbon**. This supplies a
source producer for the allowance; it does not establish how often initialization
runs or restore the allowance after every canceled order.
[Grant and consumer sequence](../ranger-training.md#xmas-allowance-has-a-selected-initialization-producer)

## The trained actor determines the writes

| Recipient          | Grenade capability | Rifle/morale additions | Weapon write at this receipt                        |
| ------------------ | ------------------ | ---------------------- | --------------------------------------------------- |
| Regular / Scout    | Set 1              | Separate 1–15 draws    | Shared weapon 2: Garand                             |
| Sniper             | Set 1              | Fixed 15 / 15          | No replacement in the selected training block       |
| Bazooka actor 1030 | Set 1              | Separate 1–15 draws    | weapon 2 field; actor-specific reader still matters |

The selected receipts require health above 9, active training and the stated
earlier-branch priorities. These are source bindings, not proof every specialist
accepts the same upgrade through every deployment/control state. The ordinary
morale draw is 1–15 here; an older community 1–20 description cannot replace it.
[Exact Regular/Scout and Sniper bindings](../ranger-training.md#explicit-regularscout-and-sniper-receipts)

For Regular/Scout, replacing the weapon field is not adding a second gun.
Check the existing equipment before treating training as a collection of
independent bonuses. No universal cancellation, repeated-training or refund
outcome is qualified by this table.

## Will training keep a BAR I already bought?

In the qualifying **Regular/Scout** receipt, no: the weapon assignment replaces
the current weapon with Garand. A supplied current BAR therefore becomes Garand
at that write, rather than keeping BAR and adding grenade, rifle and morale
benefits alongside it. Refund of an earlier weapon purchase needs separate
evidence. Check the desired final loadout before selecting another upgrade.
[Exact replacement and recipient priorities](../ranger-training.md#explicit-regularscout-and-sniper-receipts),
[equipment steps](training-and-equipment.md)

This consequence belongs to the named receipt. The Sniper's separate training
block omits that replacement, and the Bazooka's weapon field does not replace
its rocket-launch implementation. It is not a universal rule for every specialist
or a tested sequence of menu clicks.

## Bazooka training does not import the rifle actor's whole implementation

The Bazooka parent can select a hand-grenade branch after its new capability
flag, with target and protection conditions. Its separately reached launch
frame still creates a rocket without reading weapon there. Setting the Garand
code is therefore not evidence that every later attack becomes an ordinary
Garand shot or that rifle skill is a complete rocket-hit percentage.
[Receipt versus actor reader](../ranger-training.md#bazooka-weapon-assignment-does-not-replace-its-actor-implementation),
[Bazooka stages](bazooka.md), [grenade choice](grenades.md)

Sources: [Source identities](../player-notes/ranger-training.md#citation-1).
Selected publisher-associated 2.3.1g; original source-derived guide, with no new
training, allowance, distribution or trained-weapon trial.

The [Santa/Xmas Ribbon source chain](xmas-ribbon.md) separates the appearance,
scenery-hit flag and award branch before this allowance producer. It is not a
guarantee that the current menu already has a fresh free entitlement.

## Clearing the pending choice does not itself restore the free allowance

The selected Ranger offer consumes freeTrain before an actor is trained.
For separately supplied grenade and Ranger pending fields, the earlier ordinary
grenade receipt can clear Ranger's cue without a freeTrain restoration at those
sites. Heroism's free allowance is cleared at a different later valid-receipt
stage. Do not assume all canceled or competing upgrade choices share one refund
or allowance rule. Actual menu/callback reachability remains unqualified.
[Exact selected offers, cross-clears and supplied states](../player-pending-choice-evidence.md).
Additional source: [Source identities](../player-notes/ranger-training.md#citation-2)

[Original opening and evidence context](../player-notes/ranger-training.md#opening-before-player-language-correction).
