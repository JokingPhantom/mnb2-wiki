[Player reference](README.md) · [Waves](waves.md) · [Enemy guide](enemy-guide.md)

# Blitz event families

Read a Blitz announcement as a clue to the kind of threat, rather than an exact
count of enemies that have arrived. Use the case table to find the relevant
infantry, vehicle or support guide, then check that actor's rules. A tank case,
an artillery state and pending paratroopers do not all need the same response.
The selected case requests below do not establish a tested defensive layout.

The selected 2.3.1g event cadence has **17 selector values**, with different
unit requests or shared support-state changes. This is one special-event path;
ordinary wave budgets, late-wave reinforcements and actor load stats have their
own rules. [Waves](waves.md), [exact cases/compositions](../blitz-reference.md)

On this page: [The selector gate is not a per-wave frequency](#the-selector-gate-is-not-a-per-wave-frequency) · [What the selected cases request](#what-the-selected-cases-request) · [Case 14 uses an allocation counter, not a live-force census](#case-14-uses-an-allocation-counter-not-a-live-force-census) · [Support-state cases still need later consumers](#support-state-cases-still-need-later-consumers) · [A matched composition does not certify an old strategy](#a-matched-composition-does-not-certify-an-old-strategy)

## The selector gate is not a per-wave frequency

This selected path requires an unpaused game, local wave above 30 and a
random 0–999 comparison below 1 before drawing a selector 1–17. The selector's
conditional case weight does not say how often the caller runs, how many
requests finish or what happens in every other generator. It is not an
unconditional 1-in-17 chance per wave for every named historical attack.

## What the selected cases request

Numbers below summarize **nominal direct/loop requests**, not certified living
arrivals or simultaneous forces. Names follow the retained case catalog.

| Case / family                | Selected nominal requests or state                                                                                              |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| 1 Wehrmacht                  | 15 [Regular enemy infantry](enemy-regular-and-jugend.md)                                                                        |
| 2 Special weapons            | 5 [rocket troops](enemy-rocket-soldier.md) and 5 [flame troops](enemy-flamethrower.md)                                          |
| 3 Panzergrenadiers           | 1 [Panther](enemy-tanks.md) and 8 [Grenadiers](enemy-grenadier.md)                                                              |
| 4 Waffen SS                  | 8 [SS infantry](ss-infantry.md)                                                                                                 |
| 5 Snipers                    | 15 [German Snipers](german-sniper.md)                                                                                           |
| 6 Panzerkampfwagen           | 3 [German Jeeps](enemy-jeep-and-halftrack.md) and 1 Panther                                                                     |
| 7 Artillery                  | Delayed strike state or counter-artillery subtraction; no direct unit request in this case                                      |
| 8 Paratroopers               | Pending paratrooper quantity 15; separate delivery required                                                                     |
| 9 Combined arms              | 3 [motorcycles](enemy-motorcycle.md),5 Grenadiers and 3 [mortars](enemy-mortar.md)                                              |
| 10 Total Blitzkrieg          | 3 motorcycles,3 [trucks](enemy-truck.md) and 3 German Jeeps                                                                     |
| 11 Mobile artillery          | 3 [Nebelwerfers](nebelwerfer.md) and 3 [Pak38 guns](pak-38.md)                                                                  |
| 12 Brandenburg               | 15 [Brandenburg troops](brandenburg-and-infiltrators.md)                                                                        |
| 13 V1 rockets                | 5 [V1 requests](v1-rocket.md)                                                                                                   |
| 14 Volkssturm / infiltrators | 25 [Volkssturm](volkssturm.md) OR 10 [infiltrators](brandenburg-and-infiltrators.md), selected by the allocation-counter branch |
| 15 Goliath mines             | 8 [goliathmine-family requests](goliath.md)                                                                                     |
| 16 Saving Private Ryan       | 5 Grenadiers, 1 [Tiger](enemy-tanks.md) and 1 flak38 request                                                                    |
| 17 Wespe battery             | 6 separate [Wespe](wespe.md) request sites                                                                                      |

A case name does not supply one common damage/armor profile. Follow each actor's actual component
and recipient rules when comparing defenses.
[Source case list](../blitz-reference.md#the-selected-event-selector-has-17-cases)

## Case 14 uses an allocation counter, not a live-force census

Its source compares enemyCpt below 70. With supplied integer 69, the branch
requests 25 Volks; 70 takes the alternative 10 infiltrators. Those two forces
must not be added into a guaranteed 35-unit attack. The allocation counter is
not automatically the count of visible living enemies, and their later loads
and behaviors remain separate.
[Counter distinctions](../wave-counters.md), [enemy load stats](enemy-stats.md)

## Support-state cases still need later consumers

For case 7, counter exactly 0 selects delayed artillery: delay 5 and requested
strike quantity 5–14. The else alternative subtracts 1 from counter instead.
With supplied positive counter 1, that subtraction gives 0 at the site; these
counters are not seconds or proof that an already emitted shell disappears.
[Counter-artillery](naval-and-counter-artillery.md)

Case 8 writes pending paratrooper quantity 15 and clears the selected strafing
and bombing states. It does not create 15 healthy infantry at that statement.
The later plane, dropping and landing paths still matter.
[Enemy paratroopers](enemy-paratroopers.md)

## A matched composition does not certify an old strategy

Total Blitzkrieg's source requests three motorcycles, three trucks and three
German Jeeps in separate loops. That supports the nominal composition in the
historical account, but not nine healthy vehicles arriving together or any
particular anti-tank layout succeeding. Crew loss, dismounts, own blast effects
and support delivery give those threats different outcomes.
[Exact Total Blitzkrieg comparison](../total-blitzkrieg.md), [AT choices](anti-tank-options.md)

Sources: [Source identities](../player-notes/blitz-events.md#citation-1).
Original synthesis of linked selected-source notes; no new event-frequency,
arrival, placement or defensive-outcome trial.
