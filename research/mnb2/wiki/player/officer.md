[Player reference](README.md) · [Recruitment](recruitment.md) ·
[Role comparison](recruitment.md#choose-the-job-before-the-price)

# Officer

A **3-TP command specialist** with a pistol (the legacy guide calls it Colt 1911) and a distinct officer promotion
ladder. Commands check particular eligibility conditions: hiring an Officer is
not a guarantee that every command or support request is currently available.
[Command gates](../player-specialist-evidence.md#officer)

Applies to **historical selected 2.3.1g**. Starting values below describe the
ordinary load; career, scenario and later changes remain separate.

| Key fact                 | Selected ordinary load                              |
| ------------------------ | --------------------------------------------------- |
| TP cost and availability | 3 TP; Reinforcements                                |
| Health                   | 100 health points                                   |
| Rifle skill              | Starts at 0, followed by random-stop 1–10 additions |
| Morale                   | 10–99 before career bonuses                         |
| Experience               | 5; Mud and Blood Cross adds 9                       |
| Initial rank             | Source value 9, distinct from career rank           |
| Starting equipment       | Pistol (legacy name: Colt 1911)                     |

[Starting-stat evidence](../player-specialist-evidence.md)

On this page: [Commands and automatic aid are different jobs](#commands-and-automatic-aid-are-different-jobs), [Enabling commands](#enabling-commands), [Aid is conditional, and its effects differ](#aid-is-conditional-and-its-effects-differ), [Several Officers share an entry counter](#several-officers-share-an-entry-counter), [Losing and promoting an Officer](#losing-and-promoting-an-officer).

## Commands and automatic aid are different jobs

Use [orders](orders.md) for a deliberate command such as Hold Fire or Concentrate
Fire. Each offer has its own eligibility and recipient step. The Officer also
has a separate conditional **aid** path: depending on the selected branch, it
can clear pinning or change action counters, morale or TP. It is not one constant
nearby firing-speed bonus. [Command gates](../officer.md), [aid effects](../officer-aid.md).

If no aid occurs, check the Officer's health, morale, pinning, action state and
cover restrictions before interpreting it as a missing reward. Aid also has
random and shared-counter conditions; a second Officer does not guarantee twice
the output. A Pillbox can block its entry even though another bunker-related
test would pass. [Aid entry and shared-counter evidence](../officer-aid.md).

Selected historical **2.3.1g**. Aid counters are not qualified elapsed durations;
the pistol and promotion system have their own rules below.

The community card's rifle 10–35 and morale 30–100 are not substituted for the
selected initializer. Combat Ribbon and Medal of Honor each add 3 rifle points;
Defence Expert Award adds 10 morale. Initial experience and rank are independent
writes. [Profile and community comparison](../officer.md)

The [Pistol reference](pistol.md) separates its range-modified accuracy roll,
eight-round refill and Officer-specific repeat/recovery stages. Those counters
do not establish a battle fire rate.

## Enabling commands

The inspected bombing-offer gate requires the command-specialization field,
health **above 10** and no invincibility flag. Hold Fire accepts that branch or
a qualifying actor with rank at least 3 with health above 10; its invincibility check
belongs to the specialization branch only. Thus a sufficiently ranked soldier
can satisfy that particular command gate, while another offer can still have
different requirements. [Order-specific conditions](../officer.md)

For an eligible Hold Fire recipient, the inspected receipt replaces its action
timer with 400; it does not add 400 to the current value. The historical guide's
five-second duration is not established by that assignment alone. Already-fired
rounds and different recipient types remain separate. [Hold Fire trace](../hold-fire.md)

## Aid is conditional, and its effects differ

The selected aid entry needs live/unpaused and usable actor state, expired
counter, no pinning, spatial-helper conditions and random tests involving
experience. A recognized pillbox overlap fails its palisade-related gate; the
bunker random branch does not bypass that condition.
[Officer aid entry](../officer-aid.md)

One aid loop distinguishes pinned recipients from others: it clears pinning
for the former, but gives the latter a separate small random action-counter
value. The inspected recipient predicates have no distance test there; do not
replace them with a universal “nearby fire-rate aura.” Other aid branches can
add a TP while the resource value is below 10 or affect morale/accounting instead.
Those are different conditional effects, not one guaranteed periodic reward.
[Actual aid branches](../officer-aid.md)

## Several Officers share an entry counter

Aid availability reads a shared counter, but choosing an aid animation does not
reserve it. The inspected first special's effect and terminal actions do not set
that counter; the second special sets 30/60 only on particular outcomes. Other
outcomes loop or return without that write. Recruiting two Officers therefore
does not justify either a guaranteed doubled reward rate or a claim that the
first animation locks every other Officer out. Their actual order remains open.
[Shared counter and exact branches](../officer-aid.md#shared-availability-is-not-reserved-at-animation-entry)

The controller also writes a later personal action counter after its aid-choice
branches, so the earlier 60 is not a complete delay calculation. Counter values
here are not seconds. [Ordered timer writes](../officer-aid.md#shared-availability-is-not-reserved-at-animation-entry)

## Losing and promoting an Officer

A selected death penalty subtracts the dead actor's rank plus 1 from qualifying
lower-ranked recipients. For an unchanged rank 9 Officer, that particular penalty
is 10 morale. Other guards and penalties remain relevant; it does not mean every
soldier always loses exactly 10 or retreats immediately. [Morale](../morale.md)

Officer promotion checks use XP thresholds 25, 50, 75 and 99 for successive officer
rank bounds, with one rank increment on a successful helper check. They are not
simply the ordinary soldier's ten-XP sequence or a load-time floor(XP/10).
[Promotion details](../soldier-promotion.md)

Sources: [Source identities](../player-notes/officer.md#citation-1).
[Exact source notes](../player-specialist-evidence.md)

## A rank 9 soldier does not automatically become this specialist

The selected rank-up helper does not assign actor type or command specialization.
A supplied ordinary soldier promoted from rank 8 to 9 keeps specialization 1;
a supplied Resistance soldier keeps 13. The Officer load separately supplies 2.
All Around Defense and the cited bombing offer scan that specialization 2 field,
with health above 10 and no invincibility flag; numeric rank 9 alone fails their
actor test. Funds and later effect gates still apply after a match.

Hold Fire's rank branch and Heroism's rank receipt have different conditions.
Do not infer universal command access from those exceptions or from an increase
to the promotion counter. [Exact field and command comparison](../player-rank-capability-evidence.md).
Additional source: [Source identities](../player-notes/officer.md#citation-2)

## Aid and shooting compete even when enemies are present

Officer aid is considered before enemy search. Eligible entry passes a 25% roll,
then a roll below XP, requires nonmelee state and checks the shared aid cooldown.
At XP 100 the random entry gates pass 25% of otherwise eligible decisions;
this is not a per-second rate. Enemy presence is not an entry requirement.

Rally unpins eligible recipients; already-unpinned recipients instead receive
an action timer of 1–50, which is not always an improvement over their old timer.
Rally/morale effects have no distance filter in these source branches.
Other aid outcomes add a TP when the bank is below 10, raise morale or reduce
flanking-enemy accounting. Some outcomes set a shared cooldown; others loop or
return without doing so. More Officers do not guarantee proportionally more aid.

When aid is not selected, an eligible enemy can trigger pistol fire, an equipped
hand grenade or melee. With no target, there is no attack, but later aid decisions
remain possible. Nonpositive morale can initiate Officer withdrawal.
[Lifecycle and clock distinctions](unit-lifecycle.md).

Officer pistol handling has its own repeat and recovery, rather than Soldier's
Garand sequence. At equal veteran stats it cleared the medium group in 188.46
seconds, faster than Crewman/Mechanic pistols at 250.66 but far behind the strongest
gun packages. Command and squad benefits were outside that ranking.
[Measured study](combat-results.md).

## Modern equipment differs

The historical pistol facts above do not describe every modern Officer.
Inspected November 8, 2026: new modern Officers start with a Carbine and can
use ordinary weapons and rifle grenades. The November 7 pistol clearance
measurement remains a test of that pistol package, not a Carbine rate.
[Inspected revision comparison](../player-evidence-reconciliation-101.md),
[dated experiment and limits](combat-results.md).
