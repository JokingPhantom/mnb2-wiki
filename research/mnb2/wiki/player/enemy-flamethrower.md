[Player reference](README.md) · [Enemy guide](enemy-guide.md) · [Enemy stats](enemy-stats.md)

# Enemy flamethrower soldier

The enemy flamethrower soldier attacks nearby targets with flame. It **selects a target at strict source distance below 170**, then its flame checks multiple player units for a shape intersection. The selected soldier and every possible flame victim
are not necessarily the same set.
[Exact selection and component](../player-enemy-flame-evidence.md)

Start with your question: [Does bullet cover also stop the flame?](#flame-victims-use-their-own-eligibility),
[can a shot trigger an explosion before this enemy dies?](#a-firearm-hit-can-request-an-explosion-before-the-target-dies), or
[does its rifle stat determine the flame rate?](#a-wave-loaded-rifle-value-does-not-replace-the-flame-checks).

Historical scope: selected **2.3.1g**.

| Load field      | Selected default                                   |
| --------------- | -------------------------------------------------- |
| Starting health | 100                                                |
| Armor code      | 0                                                  |
| Rifle skill     | Local wave plus random 0–59                        |
| Experience      | 0                                                  |
| Morale          | 0–99; Assault Expert Award separately subtracts 10 |

The ready target scan also checks health above 10, visibility, invincibility,
line of sight and compatible melee state. Its distance threshold is an
acquisition guard, not a measured flame shape or guaranteed safe spacing.

On this page: [A wave-loaded rifle value does not replace the flame checks](#a-wave-loaded-rifle-value-does-not-replace-the-flame-checks) · [Flame victims use their own eligibility](#flame-victims-use-their-own-eligibility) · [A firearm hit can request an explosion before the target dies](#a-firearm-hit-can-request-an-explosion-before-the-target-dies)

## A wave-loaded rifle value does not replace the flame checks

A later animation comparison uses 10 plus experience, not rifle skill. With
supplied XP 0, ten of the integer 0–99 draws request the next flame stage on
one visit. The burst initializer also uses random(experience); its zero-bound
case and full animation schedule remain explicit gaps here. No fixed flame
rate or complete burst length is certified.
[Navigation and input limits](../player-enemy-flame-evidence.md#load-selection-and-burst-navigation)

## Flame victims use their own eligibility

The component's inspected victim needs positive health, armor below 1 and a
qualifying point/shape intersection. That scan does not repeat ordinary-cover
or bunker saves, nor the target scan's visibility/LOS/invincibility tests.
This is why the bullet-save table cannot be used as a flame-survival percentage.
Actual structure/component geometry is still unresolved. [Defenses](defenses.md)

At a supplied qualifying intersection, 40 of 100 random inputs take a burning-
hazard conversion branch, explicitly set the scanned player's health negative,
call fear and the player-death helper, then request removal. The other branch
subtracts 0–49 health and has no immediate local death-helper call. These are
different source paths; their complete death/accounting outcomes and per-attack
probabilities still need qualification.
[Exact victim actions](../player-enemy-flame-evidence.md#immediate-conversion-and-partial-damage-are-different-branches)

The [allied flamethrower](flamethrower.md) has a different component and recipient
path. A separate flamer explosion is also not promised on every enemy death.
[Explosion triggers](../flamer-explosion.md)

Sources: [Source identities](../player-notes/enemy-flamethrower.md#citation-1)

## A firearm hit can request an explosion before the target dies

The ordinary soldier's shared firearm helper has another exact enemy-flamer
trigger. After admitted health damage, it checks the **flammen** tag and a
fresh random comparison below 10 before its separate fatality check. A declared
Garand hit that subtracts 0 from a valid 50-health flamer can therefore still
request this explosion when that later comparison passes. The target need not
already be at zero for this source request.

This is a conditional attack branch, not a universal ten-percent chance on every
shot or death. The effect's later blast and burn victims have their own guards,
and the emitter's XP write is separate from lethal-hit XP.
[Exact four-input comparison and limits](../player-shared-flamer-trigger-evidence.md).
Additional source: [Source identities](../player-notes/enemy-flamethrower.md#citation-2)

Compare [zero health subtraction, hit counters and pinning](reading-stats.md#a-recorded-hit-can-deal-zero-damage)
before treating unchanged health as proof that the shot had no other source effect.
