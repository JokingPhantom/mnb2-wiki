[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Role comparison](recruitment.md#choose-the-job-before-the-price)

# Paratroopers

The ordinary radio offer advertises **four paratroopers for 12 TP**. The selected
Signaller acceptance path instead sets the nominal group to **six** when the
profile has `airborne == 1`, otherwise four. The separate Airborne Challenge
(mode 99) root reinforcement command costs **20 TP**; do not price it as the
ordinary radio offer. [Quantity and mode evidence](../airborne-challenge.md)

These are nominal quantities, not healthy arrivals. A per-person division is not
a measured bargain: equipment, landing damage, eligibility and later control matter.
[Paratrooper and challenge evidence](../player-roster-evidence.md#paratroopers)

Applies to **historical selected 2.3.1g**. Starting facts use the ordinary load;
career additions and other conditions are labeled separately.

| Key fact                 | Selected ordinary load                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------ |
| TP cost and availability | Ordinary radio offer: 12 TP for four advertised; acceptance can request six. Mode 99: separate 20-TP command |
| Health                   | 100 before landing and other changes                                                                         |
| Rifle skill              | Starts at 20 with random-stop 1–10 additions                                                                 |
| Morale                   | 10–39 before career additions                                                                                |
| Experience               | 0 before career additions                                                                                    |
| Starting equipment       | Random shared code 1–4: Springfield, Garand, Tommy gun or Shotgun                                            |
| Grenades                 | Conditional grants; not guaranteed on every recruit                                                          |

[Starting-stat evidence](../player-roster-evidence.md)

On this page: [Check the request first, then the soldiers who actually land](#check-the-request-first-then-the-soldiers-who-actually-land), [A radio request does not reserve the full delivery](#a-radio-request-does-not-reserve-the-full-delivery), [Landing checks are not one harmless injury roll](#landing-checks-are-not-one-harmless-injury-roll), [A healing-kit attempt can take precedence over fresh target search](#a-healing-kit-attempt-can-take-precedence-over-fresh-target-search), [Pin recovery does not use the ordinary flee bonus](#pin-recovery-does-not-use-the-ordinary-flee-bonus).

## Check the request first, then the soldiers who actually land

Keep TP/free-drop eligibility and capacity separate from the advertised group.
Radio acceptance has later gates; landing can then change health before ordinary
combat readiness. Inspect each actual soldier's health and weapon rather than
treating the nominal quantity as that many healthy, identically equipped rifles.
[Payment and quantity evidence](../player-recruitment-receipt-evidence.md#ordinary-paratrooper-request-and-later-acceptance),
[landing evidence](../paratrooper-landing.md).

For additional jobs, read the separate [healing kit](healing-kit.md),
[improvised defense](improvised-wall.md) and [sticky bomb](sticky-bomb.md) cards.
Each has its own offer, recipient, patient or placement requirements. A positive
healing-kit pool can also take a ready decision before fresh combat search.
[Healing/combat choice](../player-paratrooper-combat-evidence.md#a-healing-attempt-takes-the-alternative-to-fresh-enemy-search).
These are selected **2.3.1g** conditions, not guaranteed delivery or a purchase ranking.

Meritorious Unit Commendation replaces **only a rolled Springfield** with Garand
in this selected load; it does not replace all four possibilities. Hand-grenade
capability starts off, with a 30-of 100 draw and a separate medal-dependent grant
path. Rifle-grenade capability starts off. Career bonuses and later equipment
are separate from the base random weapon choice. [Load details](../paratrooper.md)

## A radio request does not reserve the full delivery

The ordinary menu checks the allocation counter below 96, at least 12 TP or
free-drop state, no listed strafing/bombing mission, and a usable Signaller.
It requests communication without directly charging TP. The later Signaller
acceptance rechecks capacity and affordability/free-drop state before choosing
payment and the nominal quantity.

A medal fee waiver is tested before the free-drop consumption alternative.
If that waiver branch succeeds, this local branch does not clear the free-drop
flag; otherwise the free flag is consumed or 12 TP is charged. This is not proof
of unlimited free troops or safe arrival. Mode 99's separate root command has
its own 20-TP and below-100 allocation guard.
[Exact gates and payment examples](../player-recruitment-receipt-evidence.md#ordinary-paratrooper-request-and-later-acceptance)
Additional source: [Source identities](../player-notes/paratroopers.md#citation-1)

## Landing checks are not one harmless injury roll

The selected landing action scans decorations and can subtract random 0–99 health
for each qualifying overlapping tree. Multiple source-site visits are possible;
there is no universal one-tree/one-roll total injury cap in that scan.
[Landing loop](../paratrooper-landing.md)

One landing check accepts health above 0, while the ordinary actor path needs
at least 10 and another frame's death check uses below 10. Thus a 1–9-health result
can pass one comparison while failing another. The arithmetic “100 minus at most 99
leaves positive health” is not a guarantee the soldier survives the complete
landing/controller sequence.

Load destinations point toward (200, 300) in source coordinates. That is an intended
destination field, not proof of reaching the middle through obstacles while
healthy. No safe tree spacing, landing time or final injury frequency is claimed.
[Health and movement boundaries](../paratrooper-landing.md)

Sources: [Source identities](../player-notes/paratroopers.md#citation-2). [Exact evidence](../player-roster-evidence.md)

The [airborne healing kit](healing-kit.md) has a separate pool, patient sweep
and health 11 rescue/medal branch; it does not import the recruited Medic's
complete rules. Additional source: [Source identities](../player-notes/paratroopers.md#citation-3)

## A healing-kit attempt can take precedence over fresh target search

In the selected ready controller, a positive kit pool and passing 25-of-100 test
choose healing **instead of** the fresh combat-search alternative. The healing
branch resets its action counter before scanning patients. It can therefore
reach that reset even when nobody qualifies for healing, with no pool point
spent at those patient sites.

For supplied active state, timer 0/pool 1/XP 0, passing healing draw 24 and reset draw 0,
with no eligible patients, it writes timer 50 and leaves pool 1 at the spending sites.
This is a conditional source example, not an observed idle delay or a guarantee
an existing attack was canceled. Healing and combat resets have different scopes;
actual callbacks, targets and action entry remain separate.
[Exact arbitration and inputs](../player-paratrooper-combat-evidence.md#a-healing-attempt-takes-the-alternative-to-fresh-enemy-search)

Its selected firing/repeat action bodies match ordinary 623's, but landing,
healing and controller state prevent turning those matching bodies into a
universal first-shot or retarget schedule. Garand/Carbine preparation initializes
a 1–3 semi counter; the named empty-Garand recovery branch refills 8 with 250−XP.
Those are source fields and assignments, not seconds or promised hit counts.
[Own action/recovery scope](../player-paratrooper-combat-evidence.md#shared-firing-actions-do-not-merge-this-controller-with-ordinary-infantry)
Additional source: [Source identities](../player-notes/paratroopers.md#citation-4)

## Pin recovery does not use the ordinary flee bonus

At its reached healthy, unpaused recovery action, a Paratrooper compares a
0–99 draw with **morale alone**. The ordinary soldier instead adds 10 times its
existing flee field. With supplied morale 20/flee 1, clearing accepts 21 of 100
inputs here versus 31 for the ordinary comparison. These are conditional
per-visit counts, not recovery durations or whole-attack immunity.

Clearing then replaces the action counter with random 0–99 and separately checks
positive morale. At supplied morale 0/draw 0, pinning clears but the action still
requests fleeing. Its ready action clears aiming without locally resetting
pinning, flee, targets or the timer. Recovery, readiness and a completed shot
therefore remain distinct stages.
[Exact actions, comparison table and limits](../player-paratrooper-pin-evidence.md#existing-flee-changes-the-ordinary-threshold-not-this-paratrooper-threshold)
Additional source: [Source identities](../player-notes/paratroopers.md#citation-5)

## Delivery is another action with its own allocation writes

The ordinary accepted four-or-six quantity is written to a shared field. A
later carrier action reads its current value, directly duplicates Paratroopers
and clears that shared quantity after its loop. This is not a separate immutable
queue of every accepted group. Other writers and actual callbacks still matter.
[Carrier/caller scope](../player-airborne-delivery-evidence.md#delivery-uses-current-shared-quantity-rather-than-an-immutable-group-record)

That action increments the allocation counter and wraps it to 0 only **above
100**, not at 100. For declared unchanged delivery inputs of counter 95/quantity 6,
its requested names are 95 through 100 and the counter then wraps to 0. Those are
source-name writes, not an observed six healthy arrivals or proved replacement
of occupied troops. The earlier below-96 offer/acceptance guard is a different
stage and does not reserve a ledger of free slots.
[Exact counter examples and limits](../player-airborne-delivery-evidence.md#declared-counter-examples-show-why-the-menu-limit-is-not-a-slot-ledger)

The carrier's selected position writes are x 50–349/y 50–549. Initial Airborne
Challenge instead uses x 0–400/y 0–599 at its direct-drop site. These raw writes
are not final landing rectangles or safe placement guidance; load/transform
order and tree injury still apply. Its initial carrier request also differs
from the later reinforcement request, so the two source loops do not establish
a proved double drop.
[Initial versus carrier actions and coordinate scope](../player-airborne-delivery-evidence.md#the-two-spawn-sites-use-different-position-expressions)
Additional source: [Source identities](../player-notes/paratroopers.md#citation-6)

## Airborne improvised wall

The [airborne wall command](improvised-wall.md) normally costs 3 TP. Selection
needs an indexed Paratrooper with health above 10; placement repeats that test
and needs strict source distance below 100 from the pointer and enough current
TP. This is a separate construction from the Engineer's 1-TP sandbag wall.
An admitted medal waiver can omit the debit after affordability passes, while
the selected construction counters still increase.
[Exact offer, placement and output](../player-airborne-wall-evidence.md).
Additional source: [Source identities](../player-notes/paratroopers.md#citation-7)

The [2-TP sticky bomb](sticky-bomb.md) is another airborne ability. Its later
closest-armored follow scan is separate from placement validation, and the
emitted TNT effect has a different Tiger-tag branch from the Bazooka. Neither
the cost nor a successful placement guarantees a whole-bomb kill.
[Exact placement/follow](../sticky-bomb.md), [guarded TNT/AT join](../player-sticky-tiger-evidence.md).
Additional sources: [Source identities](../player-notes/paratroopers.md#citation-8)

The [random-stop rifle comparison](../player-random-stop-load-evidence.md) explains
why this initializer is not five fixed additions. Its conditional mean is
separate from the actual recruit, later bonuses and the role's attack reader.
Additional source: [Source identities](../player-notes/paratroopers.md#citation-9)

## Count the reached injuries before interpreting remaining health

Starting from a separately supplied 100 health, one reached tree-injury write
leaves positive health for every integer draw 0–99, but 9 of those 100 inputs
leave only 1–9 health. That band passes the landing action's positive test while
failing the Allied actor's later health-at-least-ten requirement.

With two reached injury writes and declared independent inputs, 50.5% of the
10,000 input pairs leave positive health, while 41.86% leave at least 10.
These are conditional health-write counts, not a forest's landing odds or a
healthy-arrival percentage for the whole call. Actual overlap count, indexing,
health changes and callbacks remain separate.
[Exact one/two-write table and enemy reader difference](../paratrooper-landing.md#one-or-two-reached-injury-writes-have-different-health-input-counts).
Additional source: [Source identities](../player-notes/paratroopers.md#citation-10)

## Equal-stat gunfire does not include the landing or kit job

The following comparison uses the **November 7, 2026 modern simulation build**.
It is separate from the historical source facts above and from later corrections.
[Study conditions and build limits](combat-results.md).

Healthy stationary Paratroopers without active kit work matched Soldier exactly
across six offered weapons in the modern experiment. Landing injury, kit priority,
movement and distinct pin recovery remain separate.
[Infantry lifecycle](unit-lifecycle.md), [combat comparison](combat-results.md).
