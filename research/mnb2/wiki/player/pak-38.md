[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy Pak38 gun

The **Pak38** is a **500-health, armor-class 1 enemy gun** with separate
driver and gunner fields. Its readiness and target-selection rules differ from
the Allied M3 AT gun. Even a remaining driver can satisfy the selected positive
crew-sum gate when the gunner field is zero.
[Exact identity and crew/setup evidence](../player-pak38-evidence.md)

Historical scope: selected **2.3.1g**.

| Starting field         | Historical default   |
| ---------------------- | -------------------- |
| Health                 | 500                  |
| Armor code             | 1                    |
| Driver flag            | 1                    |
| Gunner flag            | 1                    |
| Spare crew             | 0                    |
| Rifle skill            | 1–10                 |
| Experience             | 20                   |
| Setup counter          | 100–399 source units |
| Initial action counter | 0–249 source units   |

These are load fields, not final combat strength, seconds or a complete
spawn-to-shot recipe. The source's type field is nebel; the exact pak38 template
identity remains separate from that internal label.

On this page: [Setup can progress without a movement update](#setup-can-progress-without-a-movement-update) · [Armor preference depends on scan order and current distance](#armor-preference-depends-on-scan-order-and-current-distance) · [Its selected shot is an offset explosion effect](#its-selected-shot-is-an-offset-explosion-effect)

## Setup can progress without a movement update

The selected setup movement needs active crew, an unpaused living actor, no
wire blocking that path, no aiming state and a random comparison. Its separate
setup counter can still decrement when wire blocked movement. Reaching zero
there does not enter the sibling readiness branch again in the same callback.
A visually stationary gun and a completed setup are therefore different facts.
[Setup and counter order](../player-pak38-evidence.md#crew-sum-and-setup-have-different-roles)

## Armor preference depends on scan order and current distance

The gun scans eligible player entries, replacing its best target only with a
closer candidate. A passing armored candidate raises the scan index, ending the
search under ordinary player-slot bounds. A farther armored
unit can lose to an earlier nearby unarmored one; an early passing armored unit
can prevent a later, closer unit from being considered. It is neither a universal
nearest-target rule nor the M3's separate armor-first pass.
[Declared scan examples](../player-pak38-evidence.md#the-scan-is-neither-two-pass-armor-first-nor-always-nearest)

Targets must also pass health above 9, visibility, invincibility and LOS guards.
A held target index is not an immutable guarantee that the same actor remains
eligible when the later effect is created.

## Its selected shot is an offset explosion effect

The inspected firing frame places an explosion around the target's current
coordinates, with independent offsets **−100 through +99** on each axis. Those
expressions do not read the gun's rifle or XP. Its later blast supplies AT radius
50 and damage input 300 through separate helper arguments; that does not mean
300 guaranteed health loss or a tank-outline hit test.
[Effect and AT chain](../player-pak38-evidence.md#frame8-places-an-effect-around-the-current-indexed-target),
[AT recipient rules](anti-tank-and-vehicles.md)

The ready path can reset its counter even without finding a target. Its burst
field, firing animation request and one reached effect action do not establish
rounds per second or a promised burst length. Crew loss, parent destruction and
abandonment also have separate source paths; full timing and outcomes remain
unqualified. [Exact lifecycle boundaries](../player-pak38-evidence.md#parent-health-destruction-and-abandonment-remain-distinct)

Sources: [Source identities](../player-notes/pak-38.md#citation-1).
Selected publisher-associated 2.3.1g; [source/version bindings](../player-pak38-evidence.md).
