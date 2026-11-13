[Player reference](README.md) · [Deployments](deployments.md) · [Progression](progression.md)

# Santa appearance and the Xmas Ribbon

**Santa is a rare scenery event tied to the Xmas Ribbon.** The selected
historical **2.3.1g** chain separates **a rare appearance request,
a qualifying scenery hit, an earned flag, award selection and a free-training
allowance**. Seeing Santa or receiving the medal does not by itself prove every
later stage happened. [Exact source](../player-xmas-event-evidence.md)

On this page: [The calendar is only one appearance condition](#the-calendar-is-only-one-appearance-condition) · [The earned flag comes from a scenery hit](#the-earned-flag-comes-from-a-scenery-hit) · [Free Ranger Training is a separate consumer](#free-ranger-training-is-a-separate-consumer)

## The calendar is only one appearance condition

The named event uses the last week of December's date fields, a random equality
and a shared not-yet-spawned marker. Santa's later departure does not clear that
marker in the selected movement body. No universal waiting time or per-wave
appearance percentage follows from this source.

The source requests Santa at point(450,300), followed by separate wandering
and departure processing. That starting point and the local movement expressions
are not a measured route or arrival time; actual Date inputs and callback
scheduling still determine a real appearance.

## The earned flag comes from a scenery hit

The selected scenery-removal helper recognizes a qualifying hit on an indexed
**santa** object and sets the career Xmas earned flag. This is not simply a
normal infantry health bar or a reward for Santa leaving. A particular explosion
still needs the actual object hit; no safe radius or guaranteed launch position
is established here. [Explosion stages](explosion-damage-stages.md)

## Free Ranger Training is a separate consumer

The award branch needs its earned flag, an unset Xmas Ribbon flag and the
medal-display/ordering gates. A separate initialization can then supply the
free-training allowance when that award flag is exactly 1. The Ranger menu spends
its allowance at admission, before the chosen troop receives training.

Consequently a medal animation is not a receipt for a completed training action,
a restored allowance after cancellation or a durable save.
[Ranger Training](ranger-training.md), [deployment allowances](deployment-gifts.md)

Source: [Source identities](../player-notes/xmas-ribbon.md#citation-1). Selected publisher-associated 2.3.1g; original player
explanation with no new calendar, appearance, hit, award or storage trial.
