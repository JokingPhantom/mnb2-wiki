[Player reference](README.md) · [Training and equipment](training-and-equipment.md) · [Purchase budgets](purchase-budgets.md)

# Training and equipment need an eligible recipient

Equipment and training do not automatically stack. An earlier pending grenade, bayonet, training or order can take precedence when an upgrade reaches its recipient. Weapon replacement can overwrite equipment already bought. Check the soldier’s resulting state after application rather than assuming every purchase applied simultaneously. [Receipt evidence](../player-interaction-evidence.md#training-and-equipment)

Historical scope: selected **2.3.1g** source; offer, recipient and later
combat effects are separate stages.

On this page: [Apply one choice and check the recipient](#apply-one-choice-and-check-the-recipient) · [Ranger Training has actor-specific receipts](#ranger-training-has-actor-specific-receipts) · [Leadership and morale have ordered effects](#leadership-and-morale-have-ordered-effects) · [Heroism uses a separate rank and health receipt](#heroism-uses-a-separate-rank-and-health-receipt) · [Healing-kit spending is per patient](#healing-kit-spending-is-per-patient) · [Rifle-grenade capability does not mean every shot is a grenade](#rifle-grenade-capability-does-not-mean-every-shot-is-a-grenade) · [Several pending choices do not form a queue](#several-pending-choices-do-not-form-a-queue) · [A stored weapon price is not the sum of earlier purchases](#a-stored-weapon-price-is-not-the-sum-of-earlier-purchases)

## Apply one choice and check the recipient

1. **Choose the intended job.** A weapon replacement, training, healing-kit pool
   and morale command change different things. Check the actor-specific card
   before treating an offer as usable on every soldier.
2. **Distinguish selecting from receiving.** Payment or a free entitlement can
   be consumed before the later recipient click succeeds.
3. **Check what the click actually applied.** Earlier pending choices can take
   precedence and clear other cues. Several menu choices do not form a reliable
   queue of upgrades for the next soldier.
4. **Check the resulting fields.** A replacement weapon need not reset ammunition
   or attack counters; training benefits differ by actor.

This is guidance from **selected historical 2.3.1g** recipient branches, not a
newly tested input sequence or cancellation/refund guarantee.
[Offer and recipient evidence](../player-interaction-evidence.md#training-and-equipment),
[pending-choice priority](../player-pending-choice-evidence.md),
[weapon-state limits](../player-weapon-state-evidence.md).

| Offer                                     | Advertised cost | Receipt distinction                                                                             |
| ----------------------------------------- | --------------- | ----------------------------------------------------------------------------------------------- |
| [Ranger Training](ranger-training.md)     | 5 TP            | May consume admitted free-training flag at selection; actual receipt differs by actor           |
| [Heroism](heroism.md)                     | 4 TP            | Sets current health to 200 after a stored-rank/live-health receipt; healing has separate limits |
| [Combat Leadership](combat-leadership.md) | 1 TP            | Selected paid/free path precedes +1 XP and a promotion check                                    |
| [Morale Boost](morale-boost.md)           | 1 TP            | Selected pending bonus is the maximum realized qualifying roll                                  |
| Hand grenades                             | 1 TP            | Capability/recipient and launch behavior are separate                                           |
| Rifle grenades                            | 2 TP            | Recipient flag does not bypass weapon/launch/target gates                                       |
| [Bayonet](close-combat-and-bayonets.md)   | 2 TP            | Its own pending mode and recipient path                                                         |
| [Airborne healing kit](healing-kit.md)    | 2 TP            | Selected receipt sets a 25-point pool, rather than adding 25                                    |

Weapon prices and distinctions are in the [weapon comparison](weapon-comparison.md).
The table is a menu overview, not proof every actor accepts every item.

If an award or free entitlement changes the budget, distinguish
[waivers, allowances and refund branches](free-orders-and-refunds.md).
Their spending stages differ; an unsuccessful recipient click is not evidence
that every paid or free selection was restored.

## Ranger Training has actor-specific receipts

The [Ranger Training guide](ranger-training.md) connects the Xmas allowance
producer to these actor-specific receipts.

In the **Regular/Scout** receipt, the selected branch grants grenade capability,
sets the shared weapon to Garand and adds **1–15 rifle and 1–15 morale**. The source
morale expression differs from an archived 1–20 claim. It replaces the weapon
field rather than adding a second gun. [Qualified regular receipt](../ranger-training.md)

The **Sniper** receipt separately grants grenade capability and adds fixed
**15 rifle and 15 morale**. Its selected training block does not contain the
Regular's weapon-replacement write. These are actual separate receiver bindings,
not an inference that ordinary infantry formulas apply to every specialist.
[Ranger receiver evidence](../player-interaction-evidence.md#training-and-equipment)

The menu can consume payment or the free entitlement before a recipient is
trained. Cancellation/refund behavior and every specialist remain separate;
no universal free-training award or repeat-training outcome is promised here.

If you already bought another weapon, include its replacement in the decision:
a qualifying Regular/Scout Ranger receipt replaces even a supplied BAR with
Garand; refund of the earlier weapon purchase needs separate evidence. This is one
reason to choose the intended final loadout before spending, rather than treating
every upgrade as an independent addition.
[Worked replacement question](ranger-training.md#will-training-keep-a-bar-i-already-bought)

## Leadership and morale have ordered effects

A selected [Combat Leadership](combat-leadership.md) receipt adds 1 XP, then invokes the rank helper.
That is a promotion **check**, not an unconditional rank increase or a universal
XP cap on every other source. [Progression](progression.md)

A selected Morale Boost receipt can take 95 plus 20 to 115 at its addition, before
any other writer; its old-morale-below 100 guard is not an immediate 100 cap. A
negative result reaching exactly 0 does not pass its strict positive recovery
test. These are conditional receipt examples, not all-family outcomes.
[Morale Boost](morale-boost.md)

## Heroism uses a separate rank and health receipt

[Heroism](heroism.md) assigns current health 200 under its selected stored-rank
and live-health gates. It does not add 200 or raise the cited Medic/hospital
patient threshold from below 100. The Medic's starting XP 25/rank 0 also shows
why an XP number alone cannot pass the rank gate.
[Exact health and rank distinction](../heroism.md)

The health assignment can also overwrite a supplied value above 200; it is not
an instruction to add another 200 to whatever health is already stored.
[Heroism assignment examples](heroism.md#applying-it-again-does-not-add-another-200-health)

## Healing-kit spending is per patient

The selected airborne kit sets its pool to 25. A qualifying sweep can heal
several patients by 1 each and spend 1 for each. The positive-pool test is outside
the patient loop, so a nearly empty pool is not freshly checked for each patient
at that spend site. That is a source overrun lead, not an observed exploit or a
guarantee exactly 25HP is delivered in every sequence. [Healing kit](healing-kit.md)

## Rifle-grenade capability does not mean every shot is a grenade

The selected launch families require weapon 1, 2 or 12, state/random conditions and
an existing target. Their nearby-target exclusion combines distance below 25
**with target armor 0**; it is not one universal 25-unit minimum for every target.
Flight and friendly-fragment recipients remain separate. [Launch gates](../rifle-grenade-launch.md),
[upgrade recipients](../rifle-grenade-upgrade.md), [blast](../fragmentation-blast.md)

Sources: [Source identities](../player-notes/training-and-equipment.md#citation-1). [Exact evidence](../player-interaction-evidence.md)

## Several pending choices do not form a queue

The selected ordinary recipient checks earlier branches before Heroism and
weapon replacement. Its hand-grenade, rifle-grenade, grenade-removal and Ranger
branches clear the pending Heroism/Ranger/weapon cues as well as the grenade cue.
A new pointer image does not itself prove every other pending flag was cleared.

For a declared healthy rank 3 soldier with no grenades and both grenade and
Heroism pending, the earlier grenade receipt grants grenades and clears Heroism;
it does not set health 200 or refund the Heroism fee at that branch. A supplied
paid Heroism offer from TP 10 can first debit 4 and leave the earlier grenade cue
set. This is a source-state example, not a reproduced lost-purchase sequence;
actual menu events and actor-click delivery remain unqualified.
[Exact offer, branch and conditional TP/health comparison](../player-pending-choice-evidence.md).

Bayonet and the first ordinary Hold Fire branch instead clear their own cue
without that same group clear. Retaining Heroism there does not guarantee a
later application. The free Ranger allowance is consumed at its offer, whereas
free Heroism has a later valid-receipt clear; another branch clearing the pending
choice does not make those spending stages identical.
[Allowance and retained-cue distinctions](../player-pending-choice-evidence.md#free-ranger-and-free-heroism-allowances-are-spent-at-different-stages).
Additional source: [Source identities](../player-notes/training-and-equipment.md#citation-2)

## A stored weapon price is not the sum of earlier purchases

The selected Garand offer debits 2 TP and assigns one pending weapon code and
stored cost of 2. Two separately admitted offers from supplied TP 10 give
10→8→6 while that stored cost remains 2. A separately reached valid ordinary
same-weapon receipt, with no earlier cue taking priority, reads that current
cost for its refund: 6→8 in this declared example, not 6→10.

These are source states and arithmetic, not an observed repeated-menu or refund
transaction. Garand and Ranger also request the same pointer frame 6 while
setting different pending fields. A pointer-frame request alone does not prove
which upgrade was applied. [Exact offer/receipt and retained fields](../player-pending-choice-evidence.md#the-stored-weapon-cost-is-not-an-accumulated-purchase-ledger).
Additional source: [Source identities](../player-notes/training-and-equipment.md#citation-3)

[Original opening and evidence context](../player-notes/training-and-equipment.md#opening-before-player-language-correction).
