[Player reference](README.md) · [Waves](waves.md) · [Orders](orders.md)

# Advancing the squad

Use this guide before moving on to the next battlefield. Advancement can remove
wounded troops and count missed enemies before rewarding survivors; it is not a
squad heal or ammunition refill. These are selected historical **2.3.1g** rules.

- **Will wounded soldiers come along?** Visited entries below 10 health are removed; positive-health wounded can trigger a morale penalty.
- **What do survivors gain?** A later loop adds 1 XP and 1 morale; a separate write adds 1 TP. Neither guarantees promotion.
- **Can advancing end the mission?** Its missed-enemy accounting can reach the loss condition. It is not a safe way to clear every threat.

[Selected 2.3.1g advancement evidence](../player-advance-evidence.md).
For pulling one troop out instead, see [unit withdrawal](withdrawal-and-mission-end.md).

The selected advancement helper starts its cleanup/reward work only when **no
indexed entry qualifies as health at least 10 and invincible exactly 0**. That
is a specific source count, not the death helper's survivor count. A wounded
entry at 1–9 health does not block it, and healthy invincible entries are excluded
from that count. [Exact source](../player-advance-evidence.md)

Selected soldier and vehicle controllers call this helper after their own
front-edge/position writes. Their guards differ. This guide does not establish
one universal crossing threshold or a completed movement/input sequence.
[Sherman caller](sherman.md), [Halftrack caller](halftrack.md)

On this page: [Wounded cleanup can change the survivors' morale](#wounded-cleanup-can-change-the-survivors-morale) · [The later XP and TP writes are not a promotion or universal cap](#the-later-xp-and-tp-writes-are-not-a-promotion-or-universal-cap) · [Enemies and scenery have indexed cleanup paths](#enemies-and-scenery-have-indexed-cleanup-paths) · [The reward is not itself a heal, refill or firing-state reset](#the-reward-is-not-itself-a-heal-refill-or-firing-state-reset)

## Wounded cleanup can change the survivors' morale

The helper requests removal of visited entries below 10 health. A positive-health
wounded entry also enters a morale-penalty loop over player indices. The inner
index is initialized only once before the wounded scan. With a fixed count and
no other mutation, its first qualifying wounded visit exhausts that index; a
second wounded visit does not automatically apply the whole penalty again.

The selected penalty subtracts 1–10 morale. Only a negative result is changed
to 1; exactly 0 stays 0 at that stage. The later reward loop then adds 1 morale.
A supplied survivor at morale 3 with penalty 4 therefore goes 3→1→2; penalty 3 goes
3→0→1. These are ordered source examples, not a promise that abandoning wounded
is harmless or that every low-morale survivor recovers.
[Exact loop and clamp](../player-advance-evidence.md#the-wounded-penalty-index-is-initialized-once)

## The later XP and TP writes are not a promotion or universal cap

A separate indexed reward loop sets targety 550, adds 1 XP and adds 1 morale.
There is no rankup call in that loop. A valid supplied XP 100 recipient gets a
101 write, without proving a permanent above-cap value: a later promotion helper
can clamp it back to 100. [XP versus rank](progression.md)

The helper later adds 1 TP without a local old-balance cap at that write. Its
100–119 groundGained addition is a source statistic, not calibrated meters.
These rewards do not guarantee durable storage, a safe advance or unchanged
later economy state.

## Enemies and scenery have indexed cleanup paths

The selected enemy scan checks indices 100 down to 0. Its miss predicate counts
living armor 0 entries, or armor 1 entries with positive driver+gunner; the latter
alternative has no repeated health test. It is not one miss per crew member or
a universal count of visible tanks. The helper's later miss>9 test can request
gameover. [Existing mission/vehicle accounting](withdrawal-and-mission-end.md)

Decoration removal and createBattlefield are separate source requests. Do not
assume every effect, building or passenger uses the same index range or ordinary
death/refund path. The later loops also use inclusive playerCpt bounds, so slot
validity and actual callback order matter to completed outcomes.
[Exact cleanup/reward boundaries](../player-advance-evidence.md#xp-tp-and-cleanup-are-separate-later-writes)

Sources: [Source identities](../player-notes/advancing.md#citation-1).
Selected publisher-associated 2.3.1g; original guide with supplied-state examples,
without new advancement, loss or save trials.

## The reward is not itself a heal, refill or firing-state reset

The selected reward loop directly changes destination y, experience and morale.
It does not assign the survivor's health, ammunition, weapon or attack counters.
With declared valid surviving health 50/ammo 2 and no intervening writer, those
fields remain 50/2 at the reward writes; the source does not set health 100 or a
full magazine there. XP 20/morale 30 at entry instead become 21/31 and targety 550.

That comparison is limited to the named direct writes. Actual later healing,
refill, terrain/component callbacks and firing readiness still need their own
execution evidence. [Exact supplied fields and complete-helper scope](../player-advance-evidence.md#the-reward-writes-do-not-themselves-heal-or-refill-the-survivor).
Additional source: [Source identities](../player-notes/advancing.md#citation-2)
