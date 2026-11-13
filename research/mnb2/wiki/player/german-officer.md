[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# German Officer

The German Officer can **request enemy reinforcements** as well as shoot. A successful special action starts the enemy-wave generator; it does not guarantee a fixed number of arrivals or establish an automatic morale aura.
Historical scope: selected **2.3.1g**.
[Exact Officer evidence](../player-enemy-officer-evidence.md)

| Key fact                     | Historical behavior                                                   |
| ---------------------------- | --------------------------------------------------------------------- |
| Starting health / armor code | 100 health; armor 0                                                   |
| Starting experience          | 1–50                                                                  |
| Special                      | Conditional enemy-wave request; separate from ordinary targeting      |
| Firearm limit                | Strict source distance below 200, plus accuracy and target conditions |

On this page: [Shooting search versus special request](#shooting-search-versus-special-request) · [Calling another generator](#calling-another-generator) · [Load context](#load-context) · [Its firearm has a short-range hit gate and different cover saves](#its-firearm-has-a-short-range-hit-gate-and-different-cover-saves)

## Shooting search versus special request

With its action timer expired and the pin guard passed, the controller takes one
of two random branches. The search branch looks for a closer eligible allied
actor with line of sight and positive visibility; the other requests its special.
A failed target search does not turn into an automatic special at that site.

The search checks health above 9, invincibility and matching melee state. It does
not explicitly exclude armor in that scan. Actual target acquisition, weapon
hit eligibility and damage remain separate stages.
[Exact target and choice guards](../player-enemy-officer-evidence.md#selected-load-and-controller-choices)

## Calling another generator

The later special frame has a below-25 comparison on an integer 0–99 input: 25
qualifying values for one reached visit. Success calls enemyWave(), then returns
the Officer to stopped frame 1. Failure requests the special label again and play.
These source transitions do not establish an elapsed-time call rate or the
probability a complete encounter produces a reinforcement.

The generator uses its own changing budget and ordered attempts. Its emissions,
wave counters, load ordering and exceptional branches still apply; do not convert
the Officer's call into “one extra soldier.” [Waves](waves.md),
[exact special path](../player-enemy-officer-evidence.md#special-label-and-later-helper-call)

## Load context

Health 100 and armor 0 are selected defaults. Experience starts at 1–50, while rifle
skill starts random(local wave)/2; that field is not a universal hit percentage.
[Enemy stats](enemy-stats.md), [reaction stages](how-shooting-works.md)

Sources: [Source identities](../player-notes/german-officer.md#citation-1)

## Its firearm has a short-range hit gate and different cover saves

The selected shot's accuracy condition combines its rifle roll with source
distance strictly below 200. Its unarmored route uses 60% ordinary-cover and 80%
bunker saves; with both actual queries true and independent uniform save inputs,
92% are saved at that branch: 1 − (0.40 × 0.20) = 0.92. The unsaved health draw is 0–49, not a shared 100-bound
rifle hit. These conditions do not establish full fire rate, guaranteed safe
range or a casualty count. [Exact firearm, damage and save comparison](../player-enemy-firearm-damage-evidence.md#the-german-officer-has-sixtyeighty-saves-and-a-strict-range-gate).
Additional source: [Source identities](../player-notes/german-officer.md#citation-2)

## Its repeat counter does not count every shot directly

A positive repeat counter alone does not guarantee another shot: ammunition and the selected repeat branch still matter. Pinning can block fresh action selection while a counter decreases. The finite ammunition inventory does not establish a complete reload cycle, eight-shot lifetime or permanent silence at empty ammo.

[Full source comparison and limitations](../player-notes/german-officer.md#its-repeat-counter-does-not-count-every-shot-directly).

## Pinning and a ticking counter are separate

[Full source comparison and limitations](../player-notes/german-officer.md#pinning-and-a-ticking-counter-are-separate).
