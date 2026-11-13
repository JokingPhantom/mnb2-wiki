[Player reference](README.md) · [Progression](progression.md) · [Medals and ranks](career-medals-and-ranks.md)

# Support and economy awards: follow the actual effect

Career awards affect **particular request, quantity and TP paths**. Their names
do not turn every support call into the same discounted transaction. This guide
covers selected 2.3.1g support/economy effects with their exact source boundaries.
[Names, award tests and consumers](../player-support-award-evidence.md)

On this page: [Air Medal and Air Command share a fee-waiver comparison](#air-medal-and-air-command-share-a-fee-waiver-comparison) · [Quantity, TP limits and HQ income use other awards](#quantity-tp-limits-and-hq-income-use-other-awards) · [Guerilla uses specific construction and vehicle counters](#guerilla-uses-specific-construction-and-vehicle-counters) · [Similar air-award names read different counters](#similar-air-award-names-read-different-counters) · [Starting allowances are spent at different stages](#starting-allowances-are-spent-at-different-stages) · [Interdiction's counter is not a unique-kill census](#interdictions-counter-is-not-a-unique-kill-census)

## Air Medal and Air Command share a fee-waiver comparison

These awards do not make every support call free. A passing waiver comparison
affects particular acceptances and leaves their earlier affordability, recipient
and capacity conditions in place. Match the award to the call before budgeting
from its description. [Exact award/consumer evidence](../player-support-award-evidence.md).

The selected bombing, close-air, air-superiority and ordinary paratrooper
acceptances test one random roll against the sum of these two stored award flags.
With normal supplied flags 0 or 1, owning neither gives 0 qualifying inputs,
either alone gives 1 of 100, and both give 2 of 100. That is a conditional fee-
waiver comparison, not the probability the whole request succeeds or delivers.

The earlier affordability and recipient/capacity tests still matter. A waiver
outcome does not make an otherwise unaffordable request eligible. Artillery,
smoke, situation reports and naval support have their own payment rules.
[Support stages](support.md), [ordinary paratrooper receipt](recruitment-limits.md)

A random fee waiver and a stored free allowance have different spending
rules. For the named training/upgrade/paradrop allowances and guarded refund
examples, use [waivers, allowances and refunds](free-orders-and-refunds.md)
before treating any award as a universal free call.

## Quantity, TP limits and HQ income use other awards

Extra requested shells, TP-expression changes and HQ income comparisons are
different benefits. Apply the named consumer below, rather than one general
discount or cap to every award. [Selected consumer bindings](../player-support-award-evidence.md).

| Award                    | Effect at the selected consumer                                                                           |
| ------------------------ | --------------------------------------------------------------------------------------------------------- |
| Ground Controller Ribbon | Adds 4 to the requested artillery quantity when its flag is positive                                      |
| Survival Ribbon          | Adds 1 for a supplied flag of 1 in the cited TP expressions                                               |
| Veterancy Ribbon         | Adds 1 for a supplied flag of 1 in those expressions                                                      |
| Guerilla warfare Award   | Adds 3 for a supplied flag of 1 in those expressions                                                      |
| Forward observer Ribbon  | Can add 1 TP on an active counter-artillery completion, with its separate mode/balance guards             |
| Field Commander Award    | Changes the early HQ comparison from 20 to 25 passing inputs out of 100 when its flag changes from 0 to 1 |

For the three listed TP-expression awards all supplied at 1, one cited clamp
expression becomes 25, while a separate old-balance admission threshold becomes 24. This does not establish one universal cap: a threshold before an addition
and a clamp afterward are different operations.
[TP source distinctions](tactical-points.md), [artillery](artillery.md),
[counter-artillery](naval-and-counter-artillery.md), [Field HQ](field-hq.md)

## Guerilla uses specific construction and vehicle counters

Its selected check reads the sum of two event counters, rather than scanning
what remains alive on the battlefield. The listed construction completions
include airborne improvised defence as well as ordinary structures. A qualifying
fee waiver does not remove the reached construction-counter addition.

The selected vehicle-counter increments cover Sherman, 20mm AA, M3 AT, static
.50 and rocket launcher spawn paths. The compared Jeep/Halftrack spawn paths
omit that increment. AP-mine, TNT, AT-mine and sticky-bomb completion branches
also differ from the listed construction-counter paths. These are source
branch distinctions, not a qualified award strategy or a promise about every
start, cancellation or later state change.
[Exact counter paths and conditional inputs](../player-guerilla-counter-evidence.md)

## Similar air-award names read different counters

| Award              | Selected source counter test |
| ------------------ | ---------------------------- |
| Air Medal          | airstrike at least 100       |
| Air Command        | airkill at least 50          |
| Air defence Ribbon | planeKill at least 100       |

The accepted literal-write view gives these fields different writers. It has
AA success writers for planeKill, but also an air-tagged explosion-credit
helper that writes the same field for a qualifying enemy recipient branch.
A planeKill counter increase therefore does not by itself identify one
intercepted aircraft. The airkill award reader is not an alias for that field.
[Exact writers, caller and limits](../player-support-award-evidence.md#the-air-counters-have-different-literal-writer-sets)

These award conditions also require unset flags and the medal-display gate.
Other listed boundaries include **antiArty above 25** for Forward observer and
**bonusTP above 1,000** for Field Commander. Exactly 25 or 1,000 does not pass
those respective comparisons. The Survival/Guerilla tests require mission-total
wave above 100, with different extra conditions. Those are source thresholds,
not guaranteed display timing, distinct-kill counts or durable saving.
[Complete selected award reference](../award-reference.md), [progression](progression.md)

Sources: [Source identities](../player-notes/support-and-economy-awards.md#citation-1).
Selected publisher-associated 2.3.1g; [exact evidence](../player-support-award-evidence.md).

The selected Xmas Ribbon initialization grants the Ranger Training allowance
when its flag equals 1, after an earlier reset. The offer consumes that allowance
before recipient application. [Ranger Training](ranger-training.md) separates
this producer from actual purchase/receipt and cancellation behavior.
Additional sources: [Source identities](../player-notes/support-and-economy-awards.md#citation-2)

## Starting allowances are spent at different stages

| Award            | Selected allowance producer         | Selected spending stage                                                           |
| ---------------- | ----------------------------------- | --------------------------------------------------------------------------------- |
| Xmas Ribbon      | `freeTrain = 1` when `medal35 == 1` | Ranger menu admission, before recipient training                                  |
| Halloween Ribbon | `freeHero = 1` when `medal42 == 1`  | Valid ordinary/recon Heroism receipt                                              |
| Victoria Cross   | `freeDrop = 1` when `medal30 == 1`  | Ordinary paradrop's free-allowance alternative, after its medal-waiver comparison |

The selected initialization resets these fields before the later grants.
Those source writes do not prove every mission's fully initialized start or
restore allowances on every canceled order. An earlier fee-waiver branch can
leave freeDrop uncleared at that local site. [Exact grant/consumer comparison](../player-allowance-evidence.md),
[Heroism](heroism.md), [Ranger Training](ranger-training.md)
Additional sources: [Source identities](../player-notes/support-and-economy-awards.md#citation-3)

[Career deployment gifts](deployment-gifts.md) also separates six selected
TP additions from weighted recruit requests and these free-order flags. The
base deployment balance is not a final initialized-start promise.

## Interdiction's counter is not a unique-kill census

The selected Ribbon test needs boobyKill above 25 and medal44 equal to 0, under
its award-display and ordering gates. Supplied counter 25 fails; 26 passes that
comparison. The cited Pioneer interaction increments the counter when it emits
a blast and removes the scanned trapped object, before a verified casualty
result. The threshold therefore does not certify 26 unique kills or an immediate
award on a particular click or detonation.
[Booby-trap player guide](booby-trap.md), [exact Pioneer/counter/award source](../booby-trap.md#the-award-counter-is-not-a-verified-kill-count).
Additional source: [Source identities](../player-notes/support-and-economy-awards.md#citation-4)
