[Player reference](README.md) · [Recruitment](recruitment.md) · [Reading stats](reading-stats.md)

# Close combat and bayonets

**Getting close can select melee instead of firearm or grenade behavior.**
For the inspected ordinary soldier, the selected target must be strictly below
25 source distance and have armor zero, after earlier actor and target gates.
At exactly 25 that particular melee conjunction fails. This is a source predicate,
not a calibrated screen-pixel boundary or a rule for every troop.
[Entry and helper binding](../player-close-combat-evidence.md#ordinary-admission-is-separate-from-the-later-helper)

Historical scope: selected **2.3.1g** source.

| Key fact               | Selected historical behavior                                                       |
| ---------------------- | ---------------------------------------------------------------------------------- |
| Ordinary melee entry   | Target distance strictly below 25, armor 0, and other actor/target gates           |
| Bayonet offer cost     | 2 TP before eligible recipient application                                         |
| Bayonet injury benefit | Separate 50-health subtraction after the random base, only once injury is selected |
| Main distinction       | Entry, attack, parry, injury and later death/credit are separate                   |

Start with your question: [Which stats affect the exchange?](#fighter-experience-and-victim-morale-have-different-roles),
[what does a bayonet cost and change?](#what-the-bayonet-changes),
[does the Close combat Ribbon add a verified damage bonus?](#the-ribbon-description-does-not-qualify-an-extra-damage-multiplier), or
[can melee change teammates' target searches?](#melee-can-affect-teammates-fresh-target-searches).

## Fighter experience and victim morale have different roles

The selected fighting helper first makes an experience-based attack comparison.
A passing attempt then faces a separate parry comparison using the victim's
experience and morale. Rifle skill is not a term in those two comparisons.

For one reached call, victim XP 20 and morale 40, and independent uniform draws:

| Fighter XP | Reaches the health-subtraction branch |
| ---------- | ------------------------------------- |
| 0          | 21%                                   |
| 30         | 28%                                   |
| 90         | 42%                                   |

These are conditional source-branch fractions. They exclude entry frequency,
repeated exchanges, motion, later health/death processing and complete fight
outcomes. Even that branch can draw zero damage before a bayonet bonus.
[Exact comparisons and inputs](../player-close-combat-evidence.md#attempt-and-parry-use-different-actors-fields)

## What the bayonet changes

The Bayonets offer debits **2 TP** before the selected recipient handler sets
its knife flag. The cited ordinary/recon receipt requires health above 9 and
its pending-mode priority; its duplicate alternative returns 2 TP. That does
not certify every invalid selection or cancellation refund.

In the selected melee injury branch, knife flag 1 adds a separate **50 health
subtraction** after the random base. The ordinary base draws 0–99, producing
50–149 at these two writes with a bayonet. Sarge and the literal infiltrator
type instead use base 0–199, producing 50–249 with that same flag. This is
not a change to the firearm damage table or a promise the attack bypasses parry.
[Damage and receipt evidence](../player-close-combat-evidence.md#a-bayonet-adds-a-separate-50-after-the-random-subtraction)

## The Ribbon description does not qualify an extra damage multiplier

The Close combat Ribbon's description advertises a 10% melee damage increase.
That term is absent from the selected fighting helper's damage expressions;
the accepted dependency audit finds lifecycle/validation references rather than
a supported positive effect. This reference therefore does not add an assumed
×1.1 to the damage values above. That is a bounded source finding, not proof of
absence from every possible runtime path.
[Description, reader and audit boundaries](../player-close-combat-evidence.md#close-combat-ribbon-description-is-not-a-verified-multiplier)

Its selected award comparison is the career hand-to-hand counter **above 100**,
with the flag unset and medal-display gate met. Exactly 100 fails; 101 passes
that comparison. These counter inputs do not establish award timing or a count
of distinct observed deaths.

## A melee kill has its own progression path

The helper's qualifying enemy-marked death branch writes **2 XP**, calls the
promotion helper and increments the close-combat kill counter. Final XP still
has the promotion helper's own cap and checks. Its player-victim alternative
uses different death-navigation sites, so the source does not support one
universal casualty/credit rule from this helper alone.
[Exact death and XP sites](../player-close-combat-evidence.md#enemy-and-player-victim-death-sites-differ),
[progression](progression.md)

Melee-state writes, parry animation requests, damage and death dispatch are
separate stages. Complete fight timing, interruption, target changes and pause
behavior still need qualified callback evidence. [Shooting stages](how-shooting-works.md),
[grenade choice](grenades.md), [morale](morale.md)

Sources: [Source identities](../player-notes/close-combat-and-bayonets.md#citation-1).
Selected publisher-associated 2.3.1g; [exact retained evidence](../player-close-combat-evidence.md).

## How much health can one admitted injury remove?

After the attack and parry checks have already selected injury, an ordinary
base draw cannot by itself take 100 health to 0: its maximum is 99. Adding a bayonet
makes 50 of 100 base inputs reach 0 or below from 100. The Sarge/literal-infiltrator
base reaches that same 100-health threshold for 100 of 200 draws without a knife,
or 150 of 200 with it. These are conditional subtraction counts, not a whole-fight
kill probability or a way to bypass parry.

For one separately reached call with fighter XP 30 and victim XP 20/morale 40,
independent uniform inputs give 28% injury-branch entry. An ordinary fighter with
a bayonet then has 14% of that supplied per-call input domain reach 0 or below from
100 health at the subtraction sites. Knife 0 has 0% there; the later death/credit
path still needs its own continuation. There is no conversion to seconds.
[Exact H 50/100/150/200 table and declared-input fractions](../player-close-combat-evidence.md#declared-health-thresholds-are-separate-from-entering-the-injury-branch).

## Melee can affect teammates' fresh target searches

The helper sets both fighters' melee-state fields before its attack roll, so a
failed attempt can still make that selected state write. The ordinary fresh
search rejects a melee-state 1 candidate when its own state is 0, even if the
candidate remains healthy and passes the other supplied filters.

That is not bullet immunity: the later shared shot body does not repeat this
melee-state test. A retained target, a newly acquired target and a reached shot
need separate callback evidence. [Exact compatibility table and retained-shot comparison](../player-close-combat-evidence.md#melee-state-can-change-fresh-target-eligibility-before-damage).
Additional sources: [Source identities](../player-notes/close-combat-and-bayonets.md#citation-2)
