[Player reference](README.md) · [Anti-tank options](anti-tank-options.md) · [Vehicles and emplacements](vehicles-and-emplacements.md)

# Vehicle hull damage and crew loss

**A healthy-looking hull, a working gunner and a living driver are different
state.** In selected 2.3.1g, a qualifying friendly fragment-blast path subtracts
hull health and then performs separate crew checks for armor-class 1 recipients.
Hull repair and crew replacement therefore answer different questions.
[Exact source and limits](../player-vehicle-blast-evidence.md)

On this page: [A blast can damage health without removing crew](#a-blast-can-damage-health-without-removing-crew) · [Spare crew follows a different branch](#spare-crew-follows-a-different-branch) · [The gunner flag changes which occupants this branch tests](#the-gunner-flag-changes-which-occupants-this-branch-tests) · [Choose the appropriate follow-up](#choose-the-appropriate-follow-up) · [Zero hull health does not select the same parent branch for every vehicle](#zero-hull-health-does-not-select-the-same-parent-branch-for-every-vehicle) · [Removal and casualty admission follow different blast paths](#removal-and-casualty-admission-follow-different-blast-paths) · [Which explosion number feeds a crew-loss roll?](#which-explosion-number-feeds-a-crew-loss-roll)

## A blast can damage health without removing crew

After this path's distance, LOS, health and protection guards, the hull-health
subtraction draws below the effect's damage argument. Driver and gunner then
have separate random draws above 75. A failed crew-loss roll does not erase hull
damage; a successful one does not require a large hull-health roll.

For declared damage 100 and a qualifying valid vehicle starting at 500 health,
health draw 0/driver draw 76/gunner draw 75 leaves health 500 at that write,
clears the driver and leaves the gunner. This assumes initial driver 1/gunner 1;
it is a source example, not an observed indestructible vehicle or measured hit.
[Ordered writes and example](../player-vehicle-blast-evidence.md#driver-gunner-and-spare-crew-are-not-one-roll)

The isolated crew test cannot pass with damage 50 because its draws 0..49 never
exceed 75. Damage 100 supplies 24 passing draw values; damage 300 supplies 224.
These counts do not include admission, AT removal, other effects or event timing,
and do not establish total survival probability per shell.

## Spare crew follows a different branch

A gunner exactly 1 selects the gunner test instead of the spare-crew loop, even
if that test clears the gunner. Otherwise positive spare crew can receive a
separate test for each initially counted slot. The driver test is separate from
both alternatives. Do not combine driver, gunner and spare crew into one shared
crew-health bar or infer passenger losses from the explosion graphic.

The source even writes its kills counter in this friendly crew-loss path;
that counter alone is not a reliable count of destroyed enemy vehicles.
[Accounting evidence](../player-vehicle-blast-evidence.md#repair-recrew-and-weapon-use-are-separate-later-consumers)

## The gunner flag changes which occupants this branch tests

For a declared valid fragment recipient with driver 1, three spare crew and
damage input 100, the inspected branch reaches two role-loss comparisons when
gunner is 1: driver and gunner. If gunner starts 0 instead, it reaches four:
driver plus each of the three copied spare slots. Losing the gunner during its
own comparison does not fall through to the spare loop in that branch.

With separately supplied independent uniform draws for those comparisons, the
conditional chance of no local crew-field loss is **57.76% for the two-test
case** and **33.362176% for the four-test case**. Their mean local loss counts
are 0.48 and 0.96. The different starting roles and branch work matter; these
figures do not compare whole-vehicle survival or establish a preferred crew setup.
At damage 100, 24 of 100 inputs lose the role, leaving 76 of 100 that do not.
For independent comparisons, 0.76 × 0.76 = 0.5776 for two no-loss outcomes;
0.76 raised to the fourth power = 0.33362176 for four. This counts the supplied
local role tests, not every earlier damage or removal stage.
Earlier blast admission, hull damage, actual callbacks and weapon operation are
separate questions.
[Exact assumptions, no-loss fractions and branch scope](../player-vehicle-blast-evidence.md#declared-joint-crew-loss-inputs-depend-on-the-selected-alternative).

## Choose the appropriate follow-up

[Mechanic](mechanic.md) repairs qualifying hull-health deficits; [Crewman](crewman.md)
fills particular missing roles. Neither action automatically certifies the other
state has recovered. Weapon and movement controllers still decide what a missing
role disables: the [Jeep](jeep.md) and [20mm AA cannon](aa-cannon.md) preserve
specific receiver and crew-predicate differences.

The [AT helper](anti-tank-and-vehicles.md) is an earlier, different stage that
can remove a qualifying vehicle directly. These fragment examples assume a
valid recipient remains afterward. They provide no safe friendly-fire layout,
complete destruction lifecycle or repairs-per-second result.

Sources: [Source identities](../player-notes/vehicle-damage-and-crew.md#citation-1).
Selected publisher-associated 2.3.1g; [source bindings](../player-vehicle-blast-evidence.md).

## Zero hull health does not select the same parent branch for every vehicle

At their selected parent-controller readers, Jeep and 20 mm AA use **health
at least 0** for their nonwreck alternatives. Sherman, M3 AT and static .50 use
**health above 0**. Supplying exactly 0 therefore chooses different branches;
it is not a qualified report that a zero-health vehicle stays usable.
[Exact five-parent comparison](../player-vehicle-wreck-evidence.md#health-zero-does-not-select-one-universal-parent-alternative)

Their local wreck branches create the named wreck and request parent removal,
without an explicit playerDeath call or casualty-field write in those bodies.
That does not prove a destroyed vehicle never affects casualties: earlier
damage/AT/crew and other callbacks remain separate. A wreck graphic alone is
not a complete accounting receipt or a guarantee about surviving gun components.
[Wreck operations and limits](../player-vehicle-wreck-evidence.md#a-local-wreck-request-is-not-a-complete-casualty-receipt)
Additional source: [Source identities](../player-notes/vehicle-damage-and-crew.md#citation-2)

## Removal and casualty admission follow different blast paths

The earlier AT helper can request allied vehicle removal without first setting
hull health to zero or calling the infantry death helper. A later core branch
can instead send a still-valid light vehicle to the gib helper, which chooses a
wreck/crew representation and requests removal. The later fragment branch's
direct casualty-helper call belongs to **armor below 1**, after lethal health
damage; its armored crew branches do not fall through to that call.

For a declared valid fragment recipient at health 50 with damage 100 and health
draw 80, both armor 0 and armor 1 become -30. Armor 0 reaches the local death-helper
call; armor 1 reaches separate crew checks. This is why hull health, crew loss,
removal and a mission casualty increment need separate evidence. It is not a
promise that any destroyed vehicle is casualty-free or award-safe.
[Exact caller order, identities and limits](../player-vehicle-caller-evidence.md).
Additional source: [Source identities](../player-notes/vehicle-damage-and-crew.md#citation-3)

## Which explosion number feeds a crew-loss roll?

The later crew comparison uses the effect's **damage argument**, separately from
its AT radius and core/fragment distances. In the inspected calls:

| Effect                                        | Damage input | Inputs passing one reached crew-loss test |
| --------------------------------------------- | ------------ | ----------------------------------------- |
| Mortar explosion                              | 50           | None of 0–49 exceed 75                    |
| Grenade fragmentation or shared aircraft bomb | 100          | 24 of 100                                 |
| M3 gun explosion                              | 300          | 224 of 300                                |

These isolated counts do not give a chance per shell. Earlier AT/core work may
already remove the vehicle, and a still-valid vehicle can have separate hull
subtraction and other effects. A Mortar's zero passing role-loss values do not
make its full explosion harmless to vehicles; a high M3 count does not prove
that its later crew branch is reached.
[Exact calls, owner arguments and reachability limits](../player-vehicle-blast-evidence.md#named-effect-arguments-feed-the-same-later-crew-comparison).
Additional sources: [Source identities](../player-notes/vehicle-damage-and-crew.md#citation-4)
