[Player reference](README.md) · [Training and equipment](training-and-equipment.md) · [Purchase budgets](purchase-budgets.md)

# Combat Leadership

Combat Leadership is a **1-TP command that adds experience (XP), then checks promotion**, for an eligible recipient. It does not promise a rank every time. An eligible free allowance can replace payment; the paid choice or free allowance is consumed before the recipient gains XP. [Offer and exact receiver evidence](../combat-leadership.md)

Historical scope: selected **2.3.1g** source; offer, recipient and later
combat effects are separate stages.

| Key fact         | Selected historical behavior                                         |
| ---------------- | -------------------------------------------------------------------- |
| Advertised cost  | 1 TP; admitted allowance alternative has no qualified positive grant |
| Spending stage   | Payment/allowance consumed before later recipient XP                 |
| Eligible receipt | Adds 1 XP, then checks promotion                                     |
| Important limit  | No unconditional rank gain or universal invalid-recipient refund     |

On this page: [Purchase and application are separate](#purchase-and-application-are-separate) · [Check both current XP and current rank](#check-both-current-xp-and-current-rank) · [Do not plan around an unqualified free allowance](#do-not-plan-around-an-unqualified-free-allowance)

## Purchase and application are separate

The inspected release offer accepts at least 1 TP or freeLeadership exactly 1.
It debits only the paid path, clears the allowance, sets the pending command
and changes the pointer. This particular script has no explicit officer scan;
full menu visibility and keyboard reachability remain separate, so it does not
establish universal use without an Officer.

The selected ordinary/recon receipt needs health above 9 and the pending command
after earlier equipment/order priorities. It adds 1 XP, calls rankup, then clears
the pending state and pointer. The source map also binds actual Medic, Officer
and other support-unit handler sites; that is stronger than assuming all units
share the rifleman's click handler, but not proof every recipient is reachable
in every scenario. [Recipient map](../combat-leadership.md#sixteen-handler-sites-are-not-sixteen-guaranteed-active-recipients)

For other commands, compare [Officer and veteran eligibility](orders.md#can-a-veteran-or-sarge-replace-an-officer-for-commands).
The absence of an explicit Officer scan in this particular release script does
not establish the requirements of Hold Fire, withdrawal or another command.

## Check both current XP and current rank

For a qualifying matched receipt, with these supplied fields and no other
writes during the helper sequence:

| Recipient state before receipt       | XP / rank after the selected helper |
| ------------------------------------ | ----------------------------------- |
| Ordinary non-Officer: 9 XP, rank 0   | 10 / 1                              |
| Medic: 25 XP, rank 0                 | 26 / 1                              |
| Ordinary non-Officer: 100 XP, rank 9 | 100 / 9                             |
| Officer: 5 XP, rank 9                | 6 / 9                               |

The Medic's high starting XP does not force an immediate multi-rank catch-up.
The ordinary helper increments rank once in its successful block. Its rifle
and morale bonuses each draw 0–9, including zero. Officer promotion has another
ladder, so the selected low-XP Officer example gains XP without gaining rank.
[Exact examples and branch limits](../combat-leadership.md#declared-receipt-and-promotion-examples),
[progression](progression.md)

In the XP 100/rank 9 ordinary example, the raw 101 is capped back to 100 by the
following helper, with no ordinary rank gain. That is a conditional result,
not a statement that every command at XP 100 is useless or refunded.

## Do not plan around an unqualified free allowance

The selected literal freeLeadership assignment map finds two reset-to-zero
sites, without qualifying a positive grant mechanism. It does not prove the
flag can never be positive, or justify assigning it to a medal from description
text alone. Cancellation, invalid recipients, allowance restoration and actual
payment/refund outcomes still need their own evidence.

Sources: [Source identities](../player-notes/combat-leadership.md#citation-1).
Selected publisher-associated 2.3.1g; original source-derived player guide,
with supplied-state examples and no new promotion/purchase trial.

[Original opening and evidence context](../player-notes/combat-leadership.md#opening-before-player-language-correction).
