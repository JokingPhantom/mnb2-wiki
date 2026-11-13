[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Role comparison](recruitment.md#choose-the-job-before-the-price)

# Engineer

A **4-TP specialist** for construction and explosives work. The selected load
starts with a Grease Gun. Buying an Engineer and ordering a structure are
separate expenses; selecting the construction offer is also separate from
successfully completing its placement. [Construction choices](defenses.md)

Applies to **historical selected 2.3.1g**. Starting values below describe the
ordinary load; career, scenario and later changes remain separate.

| Key fact                 | Selected ordinary load                                  |
| ------------------------ | ------------------------------------------------------- |
| TP cost and availability | Reinforcements; base 4 TP                               |
| Health                   | 100 health points                                       |
| Rifle skill              | Starts at 10, followed by random-stop additions of 1–10 |
| Morale                   | 10–19 before career bonuses                             |
| Experience               | 0 before career bonuses                                 |
| Starting equipment       | Grease Gun                                              |

[Starting-stat evidence](../player-defense-evidence.md#bazooka-and-engineer-defaults)

On this page: [Budget for the job after hiring](#budget-for-the-job-after-hiring), [Building defenses](#building-defenses), [Defusing is not a fixed success percentage](#defusing-is-not-a-fixed-success-percentage), [Pioneer TNT uses a different receipt](#pioneer-tnt-uses-a-different-receipt), [Its combat actions have their own bindings](#its-combat-actions-have-their-own-bindings).

## Budget for the job after hiring

The 4-TP recruit does not include its later structures or explosives. Select the
construction you need, then meet its placement/completion requirements and cost.
For protection, choose by the incoming threat and the occupant's job; another
ordinary-cover structure is not another independent save.
[Construction actions](construction.md), [defense choices](defenses.md).

Defusing a **dud** and recovering **Pioneer TNT** use different paths. Dud attempts
can fail or explode and use an escalating instability state; the selected Pioneer
TNT receipt has no random success roll in that body and grants a shared free-TNT
charge. That difference is not a promise of safe interaction: timers, proximity,
other variants and input order still matter. [Exact defuse and recovery comparison](../player-defuse-evidence.md).

Selected historical **2.3.1g**; the detailed conditions below do not establish a
safe per-click defusing rate or a tested placement stencil.

For a wounded Engineer, compare the [health-10 role tests](wounded-and-rescued.md#ten-health-does-not-mean-every-job-is-ready).
The cited Mortar-pit menu scan requires health above 10; passing an ordinary
active-health test does not by itself make that construction offer available.
Health-test source: [Source identities](../player-notes/engineer.md#citation-1)

This rifle initializer uses the same random-stop pattern as the Regular Soldier:
it is not five fixed rolls. Career effects add 3 rifle for Combat Ribbon and
another 3 for Medal of Honor, 10 morale for Defence Expert Award, and 9 initial
experience for Mud and Blood Cross. Scenario and later changes remain separate.
[Load bindings](../player-defense-evidence.md#bazooka-and-engineer-defaults)

## Building defenses

The construction menu sets a pending order. For the inspected trench and
sandbag completion paths, the relevant cue, successful proximity state and
sufficient TP must still hold. A fee is then normally charged at completion;
a specific construction-medal comparison can waive it. An advertised price or
a visible pointer is not a completed defense. [Trench](trench.md),
[sandbags](sandbags.md), [bunker](bunker.md)

Plan the protection around the soldier's actual query result. Two ordinary-cover
constructions do not automatically add two saves, and a camouflage net's
concealment is not interchangeable with bullet cover. [Defense combinations](defenses.md),
[camouflage research](../camouflage.md)

## Defusing is not a fixed success percentage

The retained source audit records an escalation state for dud defusing:
relevant failures add 10, and a success comparison uses a random 0–99 roll
strictly greater than **10 plus that state**. Eligibility, experience fallback,
proximity and timing also affect the full attempt. Repeated failure therefore
cannot be summarized by one unchanging success chance.
[Engineer research and observation 58](../engineer.md)

The selected dud button's successful branch **adds one XP and calls promotion**.
Its scan requires Engineer specialization, health above ten and distance below
100 from the **mouse pointer**. It does not sort by nearest or most experienced
Engineer. A failed candidate can leave the loop visiting later candidates;
full callback/removal behavior still needs qualification.
[Exact receipt and branch order](../player-defuse-evidence.md)

For one eligible visit with initial instability zero, the primary success roll
passes 89 of 100 values. If it fails, a separate roll greater than the Engineer's
XP emits an explosion; otherwise instability rises by ten. Higher XP affects
this fallback, not that primary threshold. At XP 50 the conditional one-visit
branch model is 89% XP receipt, 5.39% explosion and 5.61% increased instability.
These are not measured per-click safety rates: other candidates, dud timer and
proximity hazards remain separate. A “move closer” popup can also follow a
failed attempt, so it is not a distance-only diagnosis.
[Inputs, enumeration and limits](../player-defuse-evidence.md#conditional-one-candidate-arithmetic)

## Pioneer TNT uses a different receipt

The selected Pioneer TNT button uses an Engineer with health above ten and
object-to-Engineer distance below 100. It stores the qualifying scan index, then
**adds three XP, calls promotion and adds one shared free-TNT charge** before
removing that explosive. This body has no random success roll; it is not the
dud's two-roll/instability path, and it measures distance from the explosive
rather than the mouse pointer. [Binding and receipt](../player-defuse-evidence.md#pioneer-tnt-is-a-different-receipt)

The shared free-charge counter is not a new physical item attached to that
Engineer. Positive charges are spent before TP on the selected placement path.
[Spending examples](../player-defuse-evidence.md#spending-recovered-tnt).
Exact click/timer order, other TNT variants and observed safety remain unqualified.
The [dud lifecycle](duds.md) has separate autonomous random/proximity checks.

Sources: [Source identities](../player-notes/engineer.md#citation-2). [Version and exact evidence](../player-defense-evidence.md).

## Its combat actions have their own bindings

The inspected Engineer controller matches the ordinary soldier's statement
structure after changing only the excluded stock-template name. That includes
its target filters and separate acquisition-counter floor/positive-counter cap;
it does not make their starting fields or every later callback identical.
[Exact controller comparison](../player-engineer-combat-evidence.md#the-named-controller-matches-after-only-its-stock-name-exclusion-changes)

Its own preparation initializes a **Grease Gun burst counter 1–10** and a
**Garand/Carbine semi counter 1–3**. Spec Ops has the same Grease initializer but
uses semi 1–5. Neither counter is a guarantee of that many bullets or hits.
The Engineer's inspected fire and repeat bodies match the ordinary soldier's
bytes; current ammo/counters, action entry and shared weapon readers still matter.
[Preparation and firing](../player-engineer-combat-evidence.md#engineer-preparation-resembles-spec-ops-but-has-a-smaller-semi-bound)

At the selected healthy/unpaused/moving 1 Grease recovery branch, empty ammo
refills 30 and assigns 150−XP; nonempty recovery writes 10+random 0–149−XP. A later
eligible controller has its own decrement/cap 100 reader. These are stage-local
source writes, not elapsed reload time or proof of when combat resumes after a
construction or defusing action.
[Recovery scope](../player-engineer-combat-evidence.md#fire-and-repeat-bodies-are-exact-matches-not-complete-schedule-equivalence)
Additional sources: [Source identities](../player-notes/engineer.md#citation-3)

For explosive work, compare [ordinary and AT mines](mines.md),
[TNT placement and recovered stock](tnt.md), and [booby-trap application](booby-trap.md).
Their offers, target/placement step and later effect are separate stages.

The [random-stop rifle comparison](../player-random-stop-load-evidence.md) explains
why this initializer is not five fixed additions. Its conditional mean is
separate from the actual recruit, later bonuses and the role's attack reader.
Additional source: [Source identities](../player-notes/engineer.md#citation-4)

## Shooting while not doing engineering work

With six offered firearms, Engineer exactly matched Soldier in the equal-stat
stationary modern tests. Its native Grease has its own supported burst preparation.
Construction and explosives work have separate eligibility/completion rules;
matching isolated gunfire does not prove identical behavior while working or moving.
[Lifecycle](unit-lifecycle.md), [measured loadouts](combat-results.md).
