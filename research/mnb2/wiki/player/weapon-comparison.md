[Player reference](README.md) · [Recruitment](recruitment.md) · [Equipment](training-and-equipment.md)

# Comparing infantry weapons

Compare a weapon’s **accuracy rules, damage draw, ammunition and recovery together**. Ordinary Allied firing adjusts an accuracy roll, compares it with rifle skill, then handles unarmored targets and armored crews differently. Refill and recovery also depend on the soldier using the weapon. Historical scope: selected **2.3.1g**; modern measurements have a separate dated section. [How shooting works](how-shooting-works.md)

Find your question: [weapon prices](#which-weapon-offers-can-i-budget-for),
[what changes with a replacement](#what-changes-when-i-switch-weapons),
[rebuying, ammunition and TP credit](#does-buying-or-rebuying-a-weapon-refill-ammunition), or
[damage and distance values](#shared-helper-comparison),
[Shotgun bands](#shotgun-damage-changes-sharply-with-distance),
[rifle skill](#rifle-skill-is-not-always-a-displayed-hit-percentage), or
[modern loadouts](#measured-modern-loadout-choices).

## Compare the whole purchase before changing a rifle

These **selected historical 2.3.1g** choices are tactical considerations, not
measured campaign superiority. Sums assume a new normal paid Regular Soldier,
an eligible replacement and no starting-equipment bonus or waiver.

| Situation to compare      | Recruit plus weapon               | Why inspect this option                                               | Main limit                                                                                    |
| ------------------------- | --------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| General rifle replacement | Soldier 3 + Garand 2 = **5 TP**   | Compare its repeat/refill cycle with the existing rifle.              | Its distant roll penalty starts above 350 source units; buying does not refill ammunition.    |
| Equal-budget alternative  | Soldier 3 + Carbine 2 = **5 TP**  | Equal purchase total gives a different accuracy/damage/cycle package. | A lower menu price or modern test does not certify historical kills per TP.                   |
| Close engagement          | Soldier 3 + Thompson 3 = **6 TP** | Its below-100 accuracy-roll benefit differs from its distant penalty. | The distant penalty starts above 200; do not read the close benefit as all-range superiority. |
| Very close damage option  | Soldier 3 + Shotgun 1 = **4 TP**  | Its close damage band differs sharply from its far bands.             | The draw falls to 0-9 at 200 through below 400; distance and recipient behavior still matter. |
| Burst-fire package        | Soldier 3 + BAR 6 = **9 TP**      | Compare burst behavior rather than only the shared damage bound.      | Higher price does not erase burst penalties or make every shot change targets efficiently.    |

If the soldier is already present, use only the additional weapon price; if it
already carries the weapon, inspect the duplicate-credit branch below. Training
can replace an already-bought rifle, so plan its order too.
[Complete budgets](purchase-budgets.md#equipping-an-ordinary-recruit),
[equipment receipt](training-and-equipment.md),
[infantry plan](strategy-studies.md#hold-an-infantry-position-without-disabling-its-support).

## Which weapon offers can I budget for?

These are the **six retained equipment-menu offers** in selected historical
**2.3.1g**, before successful recipient application. Prices alone do not rank
damage, firing rate or value for every soldier.
[Exact menu prices and pending codes](../player-weapon-evidence.md#weapon-offers)

| Equipment offer                         | Advertised TP | Before spending                                                             |
| --------------------------------------- | ------------- | --------------------------------------------------------------------------- |
| [Springfield downgrade](springfield.md) | 1             | Returning to this rifle is a paid offer, rather than a universal free reset |
| [Shotgun](shotgun.md)                   | 1             | Its damage draw changes sharply with distance                               |
| [M1 Garand](m1-garand.md)               | 2             | Compare its repeat/refill path as well as damage                            |
| [M1 Carbine](m1-carbine.md)             | 2             | Equal price to Garand does not mean the same damage or cycle                |
| [Thompson](thompson.md)                 | 3             | Close-distance advantage and earlier distant penalty are separate tradeoffs |
| [BAR](bar.md)                           | 6             | Its shared damage bound equals Garand's; burst behavior differs             |

The stats table below also contains **starting weapons and role-specific paths**.
The Engineer/Spec Ops Grease Gun is starting equipment, separate from the six
priced offers above. Sniper, Officer and Gunner prices describe recruitment,
not separate purchases of a Sniper rifle, Pistol or machine gun.
[Retained offer scope](../player-weapon-evidence.md#weapon-offers),
[recruitment and starting roles](recruitment.md), [Engineer/Spec Ops comparison](grease-gun.md)

If you also need to hire the soldier, use [recruit-plus-equipment budgets](purchase-budgets.md#equipping-an-ordinary-recruit).
After choosing, apply the pending item to an eligible recipient. The purchase
and duplicate-credit/refill distinctions below still matter.

## What changes when I switch weapons?

In **selected 2.3.1g**, compare the engagement distance and the soldier's attack
cycle as well as the damage draw. These are supported tradeoffs, not measured
damage per second or a recommended purchase order.

| Choice                                                  | Useful difference                                                                                                 | Check before buying                                                                                   |
| ------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| [Springfield](springfield.md) or [Garand](m1-garand.md) | Garand changes the ordinary soldier's repeat/refill behavior; Springfield has a slightly larger damage-draw bound | The Garand's far-distance roll penalty starts above 350 source units, Springfield's above 400         |
| [Thompson](thompson.md) or [Grease Gun](grease-gun.md)  | Both ease the close-distance accuracy comparison; Grease has the smaller damage draw                              | Their distant penalties start above 200 and above 150 respectively                                    |
| [Shotgun](shotgun.md)                                   | Close-distance damage draw is much larger than its distant bands                                                  | At 200 and beyond, the draw falls sharply; a large close-range number does not describe distant shots |
| [BAR](bar.md)                                           | Automatic burst state affects the accuracy comparison                                                             | High rifle skill does not erase every accumulated burst penalty                                       |
| [Sniper rifle](sniper-rifle.md)                         | Its shared-helper row has no weapon-specific distance modifier                                                    | The Sniper actor has its own target and timing rules; the row alone does not guarantee a hit          |

These comparisons come from the [weapon branches](../player-weapon-evidence.md#shared-helper)
and the linked actor pages. Distances are source units; visible range, targets
and complete firing rates still need their own context. To apply an upgrade,
follow [equipment receipt](training-and-equipment.md), rather than treating a
menu click as a completed weapon replacement.

## Does buying or rebuying a weapon refill ammunition?

**Do not treat a weapon purchase as an ammunition refill.** In the selected
historical **2.3.1g ordinary/Scout recipient handler**, a reached replacement
changes the weapon field without writing ammo, burst or semi-repeat fields.
The soldier's later preparation, firing and refill actions are separate.
[Exact complete-handler scope](../player-weapon-state-evidence.md#the-selected-receipt-changes-weapon-without-writing-ammo-or-repeat-fields)

| What the eligible recipient already has      | What the selected weapon branch does                                                                                   |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| A different weapon from the pending purchase | Assigns the pending weapon; it does not refill or normalize the firing counters in this handler                        |
| The same weapon as the pending purchase      | Adds the stored pending weapon cost back to TP, then clears that cost; this is a duplicate-credit branch, not a refill |

For a supplied ordinary soldier already holding a BAR, buying the normal **6-TP
BAR offer** from a balance of 10 leaves 4 and stores cost 6. If the matching
same-weapon recipient branch is then reached with those fields unchanged, its
credit writes TP **10** and stored cost **0**. That is a conditional source
sequence, not a newly played purchase or a refund for every unsuccessful click.
[Offer and duplicate-credit writes](../bar.md#buying-selects-a-pending-weapon-code)

The recipient must still pass its health, pending-code and earlier-choice
conditions. A grenade, training or order branch can take precedence. Do not
extend this credit to every actor, interleaved menu sequence or earlier upgrade
you bought for the soldier. A specified 20-round BAR or eight-round Garand refill
belongs to its named later actor action, not to the price label.
[Equipment priorities](training-and-equipment.md#several-pending-choices-do-not-form-a-queue),
[BAR cycle](bar.md), [refund distinctions](free-orders-and-refunds.md)

## Shared-helper comparison

The damage column is the **nominal random health subtraction after an eligible
unarmored hit**, not guaranteed damage per attempted shot. Distances are source
game units, not meters or calibrated screen pixels. The listed changes modify
the roll compared with rifle skill; a larger roll makes that comparison harder.

| Weapon                              | Conditional health draw | Far-distance roll                              | Below 100 roll      |
| ----------------------------------- | ----------------------- | ---------------------------------------------- | ------------------- |
| [Springfield](springfield.md)       | 0–124                   | Above 400: ×2                                  | ÷1.1                |
| [Garand](m1-garand.md)              | 0–119                   | Above 350: ×2                                  | ÷1.1                |
| [Thompson / Tommy gun](thompson.md) | 0–99                    | Above 200: ×3                                  | ÷2                  |
| [Shotgun](shotgun.md)               | Distance bands below    | Distance bands below                           | ÷3                  |
| [BAR](bar.md)                       | 0–119                   | Above 300: ×2                                  | ÷1.3                |
| [Grease Gun](grease-gun.md)         | 0–74                    | Above 150: ×2                                  | ÷3                  |
| [Sniper rifle](sniper-rifle.md)     | 0–199                   | No distance modification in this weapon branch | None in this branch |
| [Pistol](pistol.md)                 | 0–74                    | Above 100: ×2                                  | ÷2                  |
| Machine gun                         | 0–99                    | Above 300: ×2                                  | ÷3                  |
| [M1 Carbine](m1-carbine.md)         | 0–99                    | Above 300: ×2                                  | ÷2                  |

**Strict boundaries matter.** Exactly 350 does not trigger Garand's above 350
penalty; exactly 100 does not get its below 100 benefit. For the Pistol, exactly 100
gets neither of its listed distance modifications. These are not universal hard
firing limits. The Sniper and Gunner also have their own actor/state distinctions;
do not assign a shared-helper row to every shot by a similarly named unit.
[Exact weapon and comparison bindings](../player-weapon-evidence.md#shared-helper)

## Shotgun damage changes sharply with distance

| Source distance       | Damage draw | Roll change                        |
| --------------------- | ----------- | ---------------------------------- |
| Below 100             | 0–199       | ÷3                                 |
| 100 through below 200 | 0–99        | No weapon-specific distance change |
| 200 through below 400 | 0–9         | ×3                                 |
| 400 and above         | 0–4         | ×5                                 |

That last band exists in the shared helper. It should not be erased by copying a
range restriction from a different actor's firing body. Conversely, the band is
not proof that a particular actor's acquisition/animation path will fire at that
distance. [Shotgun](shotgun.md)

## Rifle skill is not always a displayed hit percentage

For one **unpaused Garand shared-helper visit**, with rifle 40 and burst 0, the
raw accuracy comparison passes 45 of 100 rolls below 100 distance, 41 of 100 at middle
distance, and 21 of 100 above 350. This follows from the integer roll 0–99, its distance
modification and the inclusive `<=` comparison. Equality adds a passing value.
Those counts are not complete damage probabilities: target choice, attack entry,
armor, health and every relevant caller condition still matter.
[Conditional comparison evidence](../player-weapon-evidence.md#shared-helper)

## Compare the full job

The Garand's damage bound is a little lower than Springfield's, while its
ordinary-soldier refill and semi-repeat path differ. A cheap Shotgun can have a
large close-distance draw but a very small distant draw. Longer automatic burst
counters also increase this shared helper's accuracy roll. These tradeoffs do
not establish one best weapon, damage per second or kills per TP.
[Recovery and target-cycle distinctions](how-shooting-works.md),
[Gunner paths](machine-gunner.md)

Sources: [Source identities](../player-notes/weapon-comparison.md#citation-1).
Selected 2.3.1g; [exact rows and assumptions](../player-weapon-evidence.md).

The [static .50-caliber gun](fifty-caliber.md) uses another shared-helper weapon
branch with its own placement, gunner, acquisition, burst and refill controller.
Its source-stage values do not extend this infantry table into a universal
mounted-weapon performance ranking.

[Hand and rifle grenades](grenades.md) use separate equipment flags and an
actor-specific choice before their projectile/effect chain. Their blast is not
another row of the shared firearm's health-draw table.

The [Officer Pistol](pistol.md) has its own preparation/repeat/recovery actions.
Its eight-round refill does not use the ordinary Garand timeline just because
both can write an ammunition value of eight.

## An accurate zero-damage hit is not the same as a suppressing miss

An accurate zero-damage hit does not enter the shared firearm’s miss-only pinning block. A separate effect can still follow a zero-damage hit. The linked examples keep accuracy, suppression, effect requests and health subtraction separate; they do not rank complete firing cycles.

[Full source comparison and limitations](../player-notes/weapon-comparison.md#an-accurate-zero-damage-hit-is-not-the-same-as-a-suppressing-miss).

## Measured modern loadout choices

In controlled veteran group tests, deployed MG was fastest; Carbine was a strong
general infantry choice, and Thompson excelled in the close formation,
especially on Resistance. BAR's sustained damage did not guarantee fast group
clearance because bursts can continue into dead targets. Springfield gained a
finishing niche against heavily wounded enemies.
[Full comparison, distances and limits](combat-results.md).

These are November 7, 2026 modern-build measurements, separate from the historical source
comparisons above. The study did not measure survival, cost efficiency or
moving squads. High-XP Shotgun/Flamethrower results also exposed
[combat issues and later corrections](combat-issues.md).

[Original opening and evidence context](../player-notes/weapon-comparison.md#opening-before-player-language-correction).
