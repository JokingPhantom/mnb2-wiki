[Player reference](README.md) · [Support](support.md) · [Tactical points](tactical-points.md)

# Field HQ

A **5-TP engineer construction** with a source-bound income path and a
**shared recorded bonus repayment risk**. The inspected detection helper returns
presence, not the number of HQ buildings. More HQs do not automatically multiply
that one producer's TP addition.
[HQ evidence](../player-support-evidence.md#air-and-support-buildings)

Historical scope: selected **2.3.1g** source.

| Key fact               | Selected historical behavior                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| Advertised cost/access | 5 TP; Engineer construction                                                                |
| Income mechanism       | Guarded presence-based TP producer; not multiplied by HQ count                             |
| Field Commander effect | One early comparison changes from 20 to 25 passing inputs out of 100 for supplied flag 0→1 |
| Risk                   | Reached repayment state subtracts the shared recorded bonus                                |

On this page: [Income uses presence and a particular award comparison](#income-uses-presence-and-a-particular-award-comparison) · [Repayment uses one shared recorded bonus](#repayment-uses-one-shared-recorded-bonus) · [A mobile HQ and a building need the right detector](#a-mobile-hq-and-a-building-need-the-right-detector) · [A blast has a selected route into the repayment state](#a-blast-has-a-selected-route-into-the-repayment-state)

## Income uses presence and a particular award comparison

The **Field Commander Award** changes one selected early-wave income comparison.
The test is a random 0–99 roll below **20 plus 5 times its stored flag**
(medal 45), with HQ detection, mode and TP-cap conditions. It adds 1 TP and records
1 in the shared HQ bonus. A stored flag of 0 admits 20 of 100 inputs; a flag of 1
admits 25. This is one guarded source producer, not a universal measured income
probability per wave in every mode.
[Named award and consumer](../player-support-award-evidence.md#names-map-to-specific-fields-and-guards)
[Producer and cap](../field-hq.md)

## Repayment uses one shared recorded bonus

The selected HQ frame 2 state subtracts the shared accumulated bonus from TP,
clears that bonus and turns off the HQ flag. This supports a repayment mechanism
in that state. It does not prove each HQ has a separate personal account, every
transition into the state, or final negative-balance handling.

## A mobile HQ and a building need the right detector

The presence helper can find a qualifying decoration or an indexed halftrack
with the HQ module type. Its Boolean result is different from the later animation
scan and from radar/antenna detection. A visible module, a flag and a counted
income award are not interchangeable evidence.
[HQ versus other support buildings](../support-detection.md)

The community says production stops after wave 100 and in Last Stand and recommends
protecting the structure. Exact later-generator eligibility, destruction timing
and a certified safe placement remain separate. Do not infer immunity by putting
an HQ inside another defense's artwork.
[Version-qualified research](../field-hq.md), [defenses](defenses.md)

Sources: [Source identities](../player-notes/field-hq.md#citation-1).
Selected 2.3.1g; [exact evidence](../player-support-evidence.md).

## A blast has a selected route into the repayment state

The common blast's first scenery scan can request an active HQ's frame 2 when
the effect/object test passes. That reached HQ frame subtracts the **shared**
recorded bonus, then clears it. It does not use the Sandbag removal coin flip
or the bunker helper's distance threshold. This binds a source route into the
repayment state without certifying immediate callback execution or every loss.

With supplied TP 10 and shared bonus 15 at the reached frame, the subtraction
writes −5 before clearing the bonus. No lower clamp appears in that body;
this does not establish the final balance after every other writer or save.
[Exact entry request and separate HQ body](../player-blast-dispatch-evidence.md#an-active-hq-can-be-sent-to-its-shared-repayment-state)
Additional source: [Source identities](../player-notes/field-hq.md#citation-2)

Additional source: [Source identities](../player-notes/field-hq.md#citation-3)
