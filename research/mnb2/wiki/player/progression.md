[Player reference](README.md) · [Progression](progression.md) · [Medals and ranks](career-medals-and-ranks.md)

# Soldier experience, soldier rank and career progress

**Soldier experience (XP), soldier rank and your career progress are separate.**
In selected historical **2.3.1g**, gaining XP need not run a promotion check,
and gaining soldier rank does not turn the recruit into an Officer.
The ordinary starting examples use a Medic with 25 XP/rank 0 and an Officer
with 5 XP/rank 9 before career additions. Career rank and medals follow their
own counters and conditions.
[Progression evidence](../player-campaign-evidence.md#progression-and-awards)

Find your question: [which progress system to follow](#which-kind-of-progress-am-i-trying-to-make),
[why XP did not raise rank](#gaining-xp-does-not-automatically-run-promotion),
[medal descriptions versus award tests](#medal-wording-and-award-tests-can-differ), or
[whether rank 9 replaces an Officer](#reaching-rank-9-does-not-supply-the-officers-command-field),
[XP writers and caps](#ask-whether-xp-was-added-replaced-capped-or-only-recorded), or
[separate rupture/kill XP](#a-flamer-rupture-request-and-lethal-hit-xp-are-separate-writes).

## Plan one goal before changing the squad

Start with the [career planning study](strategy-studies.md#plan-a-career-unlock-and-one-compatible-medal-goal)
for a worked Default-deployment example. Choose a named goal, record its current
counter and flag, then check whether your intended purchases preserve it.

- **Unlock a deployment:** follow career points/rank, then that mode's named
  entry. First Lieutenant's selected point test is strictly above 3,000; the
  rank-gated Airborne entry and attempt allowance are separate paths.
- **Earn a wave medal:** Bronze Star reads local wave at least 40; Survival
  Ribbon instead needs zero casualties and mission-total wave above 100, plus
  their remaining award-entry conditions.
- **Pursue a restricted setup:** Guerilla's selected test uses a zero sum of
  building/vehicle event counters. A completed counted construction does not
  become absent from that history because it is later destroyed.

These selected **historical 2.3.1g** comparisons do not establish an efficient
points-per-minute route or a saved reward after reload. Follow
[medal/rank requirements](career-medals-and-ranks.md),
[reward consumers](support-and-economy-awards.md) and
[deployment gifts](deployment-gifts.md) for the actual benefit. Check
[edition identity](editions.md) before carrying these thresholds into modern play.

## Which kind of progress am I trying to make?

Use the right system before spending TP or pursuing an award. This guide concerns
**selected historical 2.3.1g**. These source-backed conditions do not verify saved progress after a reload.

| Your goal                               | What to inspect                                                                                             | Next reference                                                             |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Improve a soldier during this battle    | Current XP, soldier rank and whether the gain also triggers a promotion check; XP alone need not raise rank | Promotion rules below; [training and equipment](training-and-equipment.md) |
| Understand a recruit's starting bonuses | Which starting bonuses that recruit receives, including specialist exceptions                               | [Career stat bonuses](career-stat-bonuses.md)                              |
| Earn a named medal or career rank       | Its actual counter, threshold and other conditions; descriptions can disagree with the selected tests       | [Medals and career ranks](career-medals-and-ranks.md)                      |
| Understand points at mission end        | Mission score, career points gained and unused TP                                                           | [Score and career points](score-and-career-points.md)                      |
| Choose the next deployment              | Deployment-specific starting conditions and separate gift entitlements                                      | [Deployments](deployments.md), [deployment gifts](deployment-gifts.md)     |

For example, the Medic's starting 25 XP does not give it the Officer's starting
rank. Likewise, a career rank threshold does not set a battlefield soldier's
rank. [Starting and promotion evidence](../player-campaign-evidence.md#progression-and-awards).
Read a named bonus's recipient rules before expecting it to improve every recruit.

| Ordinary starting actor | Experience | Initial rank value |
| ----------------------- | ---------- | ------------------ |
| Regular Soldier         | 0          | 0                  |
| Medic                   | 25         | 0                  |
| Officer                 | 5          | 9                  |
| Sarge                   | 30         | 3                  |

Career additions can change experience separately. These source rank values
must not be assigned labels from the different player-career-rank namespace.

## Gaining XP does not automatically run promotion

The ordinary rank helper checks thresholds at 10, 20, ..., 90 XP for successive rank
bounds and increments rank within its successful block. It is not a loop that
instantly catches every missed rank up. Some XP sources call this helper; the
inspected Medic healing-XP write does not contain that explicit call.
[Medic](medic.md), [promotion source](../soldier-promotion.md)

The Officer has a separate later block using thresholds 25, 50, 75 and 99. In normal
starting Officer state it follows that higher ladder. Unusual state can qualify
for more than one block in a call, so do not rewrite the whole helper as a
universal one-increment transaction for every possible actor state.

Ordinary non-jeep promotion adds random 0–9 separately to rifle and morale;
Officer promotion uses random 0–19. Zero is possible. The helper's XP-above 100
cap is at entry to that helper, not proof every unrelated XP writer continuously
clamps experience. An animation request is also not independent evidence that
rank changed. [Ordered checks and bonuses](../soldier-promotion.md)

## Medal wording and award tests can differ

| Award               | Description says       | Selected test, with other gates              |
| ------------------- | ---------------------- | -------------------------------------------- |
| Gallantry Medal     | 10 Medic rescues       | At least 25 saved soldiers                   |
| Bronze Star         | Survive 50 waves       | Local wave at least 40                       |
| Silver Star         | Survive 100 waves      | Local wave at least 80                       |
| Gold Star           | Survive 150 waves      | Local wave at least 120                      |
| Sapper commendation | 50 constructions       | Construction counter at least 100            |
| Close combat Ribbon | 100 close-combat kills | Career hand-to-hand counter greater than 100 |

Other awards use mission total: the selected Survival and Guerrilla tests use
**greater than 100**, while Remembrance includes **at least 100** and a calendar
condition. Existing flags, other conditions and award-state scheduling remain
necessary; this table does not guarantee the display frame or durable save.
[Wave counters](../wave-counters.md), [award comparison](../progression.md)

Career rank thresholds have their own strict comparisons: the cited First
Lieutenant and Captain tests require career points **greater than 3,000 and 6,000**
respectively, not merely equality. A displayed target or unlock description
cannot replace the actual comparison. [Career rank evidence](../progression.md)

Sources: [Source identities](../player-notes/progression.md#citation-1). [Exact evidence](../player-campaign-evidence.md)

The [Jeep](jeep.md) shows why the receiving field matters: its selected promotion
branch raises the gun component's rifle, while its inspected firearm compares
against hull rifle. A promotion check is not proof every attack formula changed.

## A medal counter may have several writers

The [Halloween Ribbon](zombies.md) source condition tests the zombie-kill counter
above 20, with other award-entry/ordering conditions. The zombie death frame,
enemy-death helper and gib helper have distinct increment sites. Their full
interaction is not qualified here; the threshold is not proof that 21 distinct
kills always awards immediately. [Exact counter and award sites](../player-zombie-evidence.md#different-sites-write-the-persistent-zombie-counter)
Additional source: [Source identities](../player-notes/progression.md#citation-2)

The [Close combat Ribbon comparison](close-combat-and-bayonets.md#the-ribbon-description-does-not-qualify-an-extra-damage-multiplier)
also separates its advertised 10% damage reward from the selected fighting
helper and accepted dependency audit. Description text alone is not an extra
modifier in a source-backed damage table.

The [advancement reward loop](advancing.md#the-later-xp-and-tp-writes-are-not-a-promotion-or-universal-cap)
also adds 1 XP without a local promotion call. Its source write is distinct from
the later rank helper and that helper's cap. Additional source: [Source identities](../player-notes/progression.md#citation-3)

The [Air defence Ribbon counter](aa-cannon.md#the-air-defence-ribbon-counter-is-not-only-a-plane-loss-count)
has a selected AA ground-effect writer through the shared air-tag medal helper,
alongside the anti-air success writer. Its at-least-100 source threshold must
not be silently relabeled exactly 100 verified aircraft losses. Actual award
entry, earlier priorities and saving remain separate.
[Exact counter and gate](../player-air-defence-counter-evidence.md).
Additional sources: [Source identities](../player-notes/progression.md#citation-4)

The [Son of London Ribbon](v1-rocket.md#son-of-london-ribbon-uses-a-strict-threshold)
uses a recorded V1 counter strictly above 2419. The source counter/transfer,
actual award and advertised stop-later-attacks benefit retain separate evidence
boundaries; a description alone is not a verified immunity rule.
Additional source: [Source identities](../player-notes/progression.md#citation-5)

[Career stat bonuses](career-stat-bonuses.md) connects five named awards to
actual load-time rifle, morale, XP and weapon changes, with Medic/Officer/Flamer
exceptions and separate award-counter tests.

[Mission score, career points and carried TP](score-and-career-points.md) connects
the existing result formulas and ordered promotion/leftover readers without
turning a display or flush request into a verified save.

## A flamer rupture request and lethal-hit XP are separate writes

The shared firearm's enemy-flamer explosion branch adds 1 XP and invokes promotion
before its independent fatality check. If the declared unchanged recipient is
also killed by the health subtraction, the later fatal branch has another+1 and
promotion call. A nonfatal hit can reach the rupture XP site alone. These are
separate source operations; the promotion helper's cap and thresholds still
matter, so they do not promise two promotions or a fixed final XP gain.
[Exact admitted branches and supplied inputs](../player-shared-flamer-trigger-evidence.md).
Additional source: [Source identities](../player-notes/progression.md#citation-6)

## Ask whether XP was added, replaced, capped or only recorded

A promotion helper can cap XP above 100 when it is called, but selected Medic,
Paratrooper, hospital and radio XP bodies do not locally call that helper.
Other paths replace a vehicle's XP from a new Crewman instead of adding to it.
Best-soldier snapshots record XP without improving the source soldier.

The same numeric increase therefore does not prove a promotion, an always-on
cap or a better gun. For enemy stats, aliased blast owners also need their actual
identity; an XP 0 load is not a proof that no later writer can reach that enemy.
[Finite later-XP writer map and limits](../player-experience-writer-evidence.md).
Additional source: [Source identities](../player-notes/progression.md#citation-7)

[Career medal and rank requirements](career-medals-and-ranks.md) now groups all 48
named catalogued award conditions and the complete career-point ladder. Its
ordered-check explanation separates meeting a threshold from the next award
alternative, display, reward reader and durable save.
Additional source: [Source identities](../player-notes/progression.md#citation-8)

## Reaching rank 9 does not supply the Officer's command field

The selected promotion helper raises rank and bonuses without assigning actor
type or command specialization. Its new-rank 9 promotion counter is written
before the Jeep/non-Jeep bonus split. That counter is not proof of an Officer
conversion, an infantry-only promotion or a completed medal/save.

With supplied later grunt/spec 1 and Resistance/spec 13 states at rank 8/XP 90,
one admitted helper call gives rank 9 while leaving those type/spec fields
unchanged. All Around Defense still needs specialization 2, health above 10
and no invincibility flag in its scanned command actor. Those promoted states
fail its specialization test. Hold Fire's separate rank-at-least 3 branch and
Heroism's rank-above 1 receipt explain why a ranked soldier can qualify for
some orders without replacing an Officer for every command.
[Exact receiver/counter order, load values and supplied-state comparisons](../player-rank-capability-evidence.md).
Additional source: [Source identities](../player-notes/progression.md#citation-9)
