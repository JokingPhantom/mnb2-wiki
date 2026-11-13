[Player reference](README.md) · [Deployments](deployments.md) · [Progression](progression.md)

# Deployment modes change your starting problem

Deployment modes change your **starting squad and resources**. The selected historical **2.3.1g** rules distinguish seven mode codes. The base values below apply before career additions and later initialization, so they are not promises of the final numbers displayed after starting. [Scenario evidence](../player-campaign-evidence.md#deployments-and-tp)

On this page: [Compare entry rank and starting resources](#compare-entry-rank-and-starting-resources) · [Which career rank does the named menu entry require?](#which-career-rank-does-the-named-menu-entry-require) · [Hasty defense requests random roles with a remap](#hasty-defense-requests-random-roles-with-a-remap) · [An Airborne attempt is not the same state as the badge](#an-airborne-attempt-is-not-the-same-state-as-the-badge) · [Which base squad does that mode request?](#which-base-squad-does-that-mode-request) · [Proper Planning adds and then clears stored leftover TP](#proper-planning-adds-and-then-clears-stored-leftover-tp)

## Compare entry rank and starting resources

Career rank unlocks the inspected named menu entries; it is different from any
soldier's rank. The rank and TP columns concern separate source stages. For
Airborne, the rank-gated button is also distinct from the attempt-allowance entry.
[Exact menu gates and ordered resources](../player-deployment-entry-evidence.md).

| Mode               | First admitted integer career rank in the named button | Base TP expression                     |
| ------------------ | ------------------------------------------------------ | -------------------------------------- |
| Default deployment | No rank test in this button                            | 0                                      |
| Hasty defense      | Captain, 3                                             | 0                                      |
| Close protection   | Major, 4                                               | 12                                     |
| Special operations | Lt. Colonel, 5                                         | −10                                    |
| Proper planning    | Colonel, 6                                             | Saved leftover TP                      |
| Last stand         | Brigadier General, 7                                   | 50 plus 10 times (saved career rank−6) |
| Airborne challenge | First Lieutenant, 2, for the rank-gated entry          | 0                                      |

The negative Special operations intermediate value is retained rather than
silently changed to 0. Equal base TP also does not mean equal units, equipment
or scenario conditions. Each mode has separate initialization/spawn and launcher
records. [Technical scenario comparison](../deployments.md)

The community describes four free Regular Soldiers for ordinary deployment.
That is not a starting-squad promise for every row in this table or proof that
all career/spawn modifiers are absent. [Regular Soldier](regular-soldier.md)

Selection, career unlocks and promotion comparisons are separate. The legacy
interface guide associates options with career rank, while selected launcher
conditions identify the actual source gate. Exact cross-version unlock behavior
and fully initialized starts still need their own qualification.
[Progression](progression.md), [scenario source](../deployments.md)

Some economy and support paths explicitly exclude a particular mode; do not
copy ordinary-wave TP, HQ income or cap behavior onto Last Stand solely because
the menu still shows the same item. [TP rules](tactical-points.md),
[Field HQ](field-hq.md), [support](support.md)

Airborne Challenge uses a separate 20-TP root reinforcement command. The ordinary
12-TP radio offer has its own four-versus-six profile-dependent quantity; neither
menu label guarantees healthy arrivals. [Paratroopers](paratroopers.md),
[exact scenario/quantity comparison](../airborne-challenge.md)

Sources: [Source identities](../player-notes/deployments.md#citation-1).
[Version and exact evidence](../player-campaign-evidence.md)

[Career deployment gifts](deployment-gifts.md) separates selected later TP
additions, bonus recruit requests and free-order allowances from these base
mode expressions. No complete initialized start is inferred from one gift block.

## Which career rank does the named menu entry require?

The entry ranks in the comparison above are stored **career ranks**, not a soldier's rank or a universal point
threshold. The named default-deployment button has no rank predicate. Other
mode assignments, button visibility and full start state remain separate.
[Exact entry gates](../player-deployment-entry-evidence.md#named-deployment-menu-releases-use-career-rank)

Last stand's base expression also reads career rank. For supplied rank 7
unchanged from entry to that later assignment, it writes 60 before gifts and
other later changes. Quoting the constant 50 alone would miss that input.
[Ordered base resources](../player-deployment-entry-evidence.md#base-resource-writes-preserve-their-order-and-inputs)

## Hasty defense requests random roles with a remap

Its selected starting loop makes four requests from raw selectors 1–13. Jeep 2
and Sherman 11 are remapped to Resistance 10. With a uniform raw draw, Resistance
therefore has 3 of 13 inputs at that request, while each other surviving selector
has 1. The loop does not request a Jeep or Sherman through those remapped values;
it does not promise four healthy arrivals or describe every later career gift.
[Exact mapped roles and limits](../player-deployment-entry-evidence.md#hasty-mode-remaps-two-of-thirteen-selector-inputs)

## An Airborne attempt is not the same state as the badge

One selected entry consumes a positive **airborne attempt allowance**. The
rank-gated entry above is a different handler, without that local allowance
write; this is not a proven bypass or proof both buttons are visible together.
The career promotion branches each add an attempt when that branch is reached.

The badge's selected test instead needs mode 99, **mission-total waves at least 100**
and its stored flag unset, within the ordered award/display path. Meeting that
number does not certify instant badge display or durable saving. The ordinary
Signaller's 4-versus-6 drop quantity reads the separate earned flag; the challenge's
reinforcement command has its own price/quantity path.
[Attempt, promotion and badge source](../player-deployment-entry-evidence.md#airborne-entry-attempt-allowance-and-badge-are-distinct-state),
[Paratroopers](paratroopers.md)
Additional source: [Source identities](../player-notes/deployments.md#citation-2)

## Which base squad does that mode request?

The selected initialization has these **base requests before conditional career
gifts**. A request or duplicate is not a guaranteed healthy arrival:

| Mode               | Selected base squad requests                          |
| ------------------ | ----------------------------------------------------- |
| Default            | Four Regular Soldiers                                 |
| Hasty defense      | Four random role requests with the remap above        |
| Close protection   | No direct base-spawn request in this mode alternative |
| Special operations | Four Spec Ops requests, then the −10 TP assignment    |
| Proper planning    | Four Regular requests, then the carry-over operation  |
| Last stand         | No direct base-spawn request in this mode alternative |
| Airborne challenge | Four nominal Paratrooper duplicate/drop iterations    |

Close Protection and Last Stand's no-request entries describe this one mode
block, not a proof that the whole initialized battlefield is empty. Later gifts,
other actors, player purchases, capacity and load callbacks remain separate.
Airborne's direct drops also differ from the guarded recruit helper and have
landing hazards. [Exact source table and scope](../player-deployment-entry-evidence.md#base-squad-requests-are-distinct-from-career-gifts),
[Paratrooper landing](paratroopers.md#landing-checks-are-not-one-harmless-injury-roll)

## Proper Planning adds and then clears stored leftover TP

The selected block adds the stored leftover field to the current balance,
then clears that stored field to 0. With supplied balance 3 and stored leftover 7
at those writes, the local values become balance 10/leftover 0. This is not a
promise of the final starting balance or a durable save after every exit.
[Exact addition/clear and remaining storage limits](../player-deployment-entry-evidence.md#proper-planning-consumes-the-local-leftover-field-after-adding-it)

The [mission-result calculation](score-and-career-points.md) writes the carry-over
field on another path. Menu selection, result calculation, local consumption and
persisted storage should not be treated as the same event.
Additional source: [Source identities](../player-notes/deployments.md#citation-3)

[Original opening and evidence context](../player-notes/deployments.md#opening-before-player-language-correction).
