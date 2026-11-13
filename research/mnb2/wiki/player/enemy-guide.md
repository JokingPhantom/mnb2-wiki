[Player reference](README.md) · [Waves](waves.md) · [Enemy guide](enemy-guide.md)

# Enemy roles and the rules behind them

Enemy names do not determine one shared accuracy, cover or targeting rule.
Use this guide to find the selected **publisher-associated 2.3.1g** behavior
that matters to your position. These are the roles covered so far, not the
complete enemy roster or a ranking of measured danger.

On this page: [Start with the threat you are trying to understand](#start-with-the-threat-you-are-trying-to-understand) · [Do wounded or concealed soldiers stop being targets?](#do-wounded-or-concealed-soldiers-stop-being-targets) · [Match the defensive question to the attack stage](#match-the-defensive-question-to-the-attack-stage) · [Enemy vehicles have separate parent and weapon rules](#enemy-vehicles-have-separate-parent-and-weapon-rules) · [Read wave stats at load, then follow the reader](#read-wave-stats-at-load-then-follow-the-reader)

## Start with the threat you are trying to understand

- **A bunkered soldier is still being hit.** [German Sniper](german-sniper.md) omits the extra bunker save in its inspected firearm path; other bullets, blasts and flames have different protection rules. [Defense comparison](defenses.md)
- **A hidden or badly wounded ally is still selected.** Target-health and visibility conditions differ by attacker. The Sniper lacks the ordinary positive-visibility test, while Jugend admits lower health than Regular infantry. See the search comparison below.
- **Rockets or mortar effects land near the squad.** [Rocket troops](enemy-rocket-soldier.md) and [mortars](enemy-mortar.md) use different target and effect-placement stages. A loaded rifle number alone does not describe their accuracy.
- **A camouflage net no longer seems to conceal the position.** [Enemy Scout](enemy-scout.md) reconnaissance can block the net query's positive result without physically removing the net. This is separate from a bullet-cover save.
- **Mines, wire or constructions are being interfered with.** [Pioneer](enemy-pioneer.md) sabotage, mine removal and wire disabling are different actions; one movement restriction need not block all of them.
- **Extra enemies appear around an Officer or special event.** A [German Officer](german-officer.md) special action can call a wave generator; [Blitz events](blitz-events.md) have other emission paths. A call is not a fixed count of living arrivals.
- **A vehicle is damaged but still moving or firing.** Start with [enemy vehicles](enemy-vehicles.md): hull, crew and weapon controllers have different conditions.

Each role link retains its source/version evidence. These routes help explain
an encounter; they do not establish an optimal kill order, a safe position or a
measured counterplay success rate. The role list below gives more detail.

| Role                                                                 | Distinction explained by its card                                                                                                          |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| [Volkssturm](volkssturm.md)                                          | Low starting morale, wave-dependent rifle load and separate attempt/accuracy/save stages; one retained observed birth example              |
| [German Sniper](german-sniper.md)                                    | Target search lacks the ordinary positive-visibility requirement; its inspected firearm lacks the extra bunker save                        |
| [SS infantry](ss-infantry.md)                                        | Full-wave rifle roll, later burst overwrite and a 60% ordinary-cover save                                                                  |
| [Enemy machine gunner](enemy-machine-gunner.md)                      | Setup state and a shot penalty that changes with the remaining burst counter                                                               |
| [Enemy Grenadier](enemy-grenadier.md)                                | Ordinary target search and the position/explosive-gated grenade choice are separate branches                                               |
| [Enemy rocket soldier](enemy-rocket-soldier.md)                      | Ordered armor-first search has different filters from its fallback; loaded rifle does not describe the inspected launch                    |
| [Enemy mortar](enemy-mortar.md)                                      | Selection requires distance >300; later placement uses the target's current coordinates plus fixed axis offsets                            |
| [Enemy Scout](enemy-scout.md)                                        | Calling, reconnaissance and ordinary targeting are separate; reconnaissance can block a net-success query                                  |
| [Enemy Pioneer](enemy-pioneer.md)                                    | Structure sabotage, mine removal and wire disabling have different predicates; sabotage does not repeat movement's wire guard              |
| [German Officer](german-officer.md)                                  | A later special calls a wave generator, rather than promising a fixed number of extra soldiers                                             |
| [Enemy flamethrower](enemy-flamethrower.md)                          | Acquisition within 170 and a separate player-victim shape scan; bullet saves are not repeated in that component                            |
| [Zombies](zombies.md)                                                | Calendar-gated emission, 400-health/armor 0 load and distinct death-counter writers; Ribbon threshold is not a certified unique-kill count |
| [Enemy paratroopers](enemy-paratroopers.md)                          | Plane placement, multiple tree-injury opportunities and later readiness/timer writers before ordinary firearm stages                       |
| [Regular / Jugend infantry](enemy-regular-and-jugend.md)             | Shared wave-rifle initializer but different low-health target filter, local firing-attempt gate and semi continuation                      |
| [Brandenburg / hidden infiltrators](brandenburg-and-infiltrators.md) | Separate side/lower-field controllers, hidden detection guards, Scout type-name mismatch and different reveal/shot writers                 |

## Do wounded or concealed soldiers stop being targets?

**Being wounded or having a zero visibility counter does not guarantee exclusion
from enemy searches.**
These selected acquisition predicates differ before accuracy, saves or damage:

| Selected search                  | Target health | Positive visibility counter required? | Other conditions still apply                                                                     |
| -------------------------------- | ------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Regular                          | Above 9       | Yes                                   | Other armor/crew, pillbox, LOS and eligibility checks still apply                                |
| Jugend                           | Above 0       | Yes                                   | Lower health gate than Regular, despite a similar starting rifle formula                         |
| German Sniper                    | Above 0       | No such test in this scan             | Armor class 2 is excluded; LOS, invincibility and melee compatibility still matter               |
| Mortar                           | Above 9       | Yes                                   | Selected distance must be strictly above 300                                                     |
| Flamethrower                     | Above 10      | Yes                                   | Selected distance must be strictly below 170; the later flame component scans victims separately |
| Rocket troop, first armored pass | Above 0       | No such test in this pass             | Positive armor and LOS are required; the fallback scan has different filters                     |

The rows describe the named initial searches, not every repeat or every attack
in the game. With health 5 and the other predicates supplied, Jugend and Sniper
can pass their health test while Regular cannot. At health 10, Regular and
mortar pass their health test while the flamethrower selection fails its
strictly-above-10 test. None of those comparisons guarantees a valid target,
shooting, injury or rescue in an actual encounter.
[Regular/Jugend guards](../player-regular-jugend-evidence.md#load-and-target-health-differences),
[Sniper guards](../player-german-sniper-evidence.md#acquisition-does-not-require-positive-target-visibility),
[mortar and rocket guards](../player-enemy-heavy-evidence.md),
[flame selection and component](../player-enemy-flame-evidence.md).

Here visiblez is a source counter, not a promise about rendered opacity or
whether you can see a sprite. Its absence from the Sniper's acquisition scan
means that counter alone does not exclude a hidden ally there. The rocket's
armored pass likewise does not become a general hidden-infantry search: its
positive-armor requirement still matters.

Initial selection also does not freeze the target's later health, visibility or
position. A repeat can retain an old index or use another pool, and a damage
body need not repeat every acquisition filter. Treat [wounded/rescue state](wounded-and-rescued.md),
[concealment](concealment.md) and [bullet protection](defenses.md) as different
questions when assessing a position.

## Match the defensive question to the attack stage

For ordinary bullets, start with [defense stacking](defenses.md). Several covered
shooters use separate 50% ordinary-cover and 75% bunker saves after accuracy
passes. SS uses 60% for the ordinary save; the inspected enemy Sniper path omits
the extra bunker save. Multiple ordinary-cover shapes do not supply one roll
per structure. A specific position still needs the relevant geometry queries
to succeed.

For rockets and mortar effects, read [AT and vehicle health](anti-tank-and-vehicles.md)
and the individual role. Target selection, a proximity trigger, an effect's
position and later damage eligibility can use different guards. A vehicle's
visible outline does not by itself answer all of those questions.

For a net or prepared construction, read the [Scout](enemy-scout.md) and
[Pioneer](enemy-pioneer.md) separately: reconnaissance state changing a net query
is a different mechanism from sabotage creating TNT or disabling wire.
Neither event alone establishes a completed casualty or a measured counterplay.

## Enemy vehicles have separate parent and weapon rules

The [enemy-vehicle overview](enemy-vehicles.md) collects selected hull loads and
links the remaining role coverage. The [Goliath](goliath.md) has distinct movement, proximity and effect-creation
paths. The [SdKfz 222](sd-kfz-222.md) can reset a driver field at a health cost,
while its child turret uses mission-total wave for its own rifle roll. Armor,
crew, weapon and parent removal are different states; these two cards are an
initial vehicle extension, not the whole vehicle roster.
[Exact light-vehicle source comparison](../player-light-vehicle-evidence.md)
Additional source: [Source identities](../player-notes/enemy-guide.md#citation-1)

## Read wave stats at load, then follow the reader

The [wave-stat table](enemy-stats.md) specifies local wave at load. It does not
reroll every living enemy when the counter changes. SS/MG burst penalties and
rocket/mortar placement readers show why a loaded rifle number cannot stand in
for an entire attack. [How to read stats](reading-stats.md)

The [source template map](../enemy-infantry-map.md) retains exact infantry
placements and aliases behind these initial role comparisons. Enemy vehicles, exceptional spawns,
full timing and transformed geometry also remain partial.
[Coverage plan](../PLAYER_COVERAGE.md)

Sources: [Source identities](../player-notes/enemy-guide.md#citation-2).
Additional retained observation:
Exact scope and retained bindings are linked from each role card.

The [enemy priority field table](enemy-stats.md#priority-is-a-separate-load-field-used-by-a-sniper-selector)
connects named load values to the Allied Sniper's specific scan reader. It is
not a universal highest-threat or nearest-enemy target policy.
