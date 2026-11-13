[Player reference](README.md) · [Defenses](defenses.md) · [Construction](construction.md)

# Mortar pit

A **4-TP Engineer construction** whose selected drawing contains a named ordinary-
cover component. It is a separate purchase and object from the [Mortar soldier](mortar.md).
A construction's name alone does not establish a firing-rate bonus.
[Selected 2.3.1g evidence](../player-construction-detail-evidence.md)

Historical scope: selected **2.3.1g** source; the stated saves and placement
checks are conditional, not a certified protected layout.

| Key fact                 | Selected historical behavior                                |
| ------------------------ | ----------------------------------------------------------- |
| TP cost and availability | 4 TP; Engineer construction                                 |
| Protection category      | Ordinary-cover component; not an extra bunker save          |
| Payment                  | Completion rechecks affordability; conditional medal waiver |
| Weapon benefit           | No complete firing-rate bonus established here              |

On this page: [Placing it](#placing-it) · [One ordinary-cover success test](#one-ordinary-cover-success-test)

## Placing it

The menu requires an Engineer with health above 10 and at least 4 TP, then selects
a pending cue. Completion repeats affordability and pointer-proximity conditions,
normally debits 4 TP and emits the pit at the mouse coordinates. The selected Sapper
commendation comparison can waive the debit after affordability passed. Its
completion writes a random rotation −10..+9. Final placement, cancellation and
keyboard parity remain separate from those source branches.
[Purchase and completion](../player-construction-detail-evidence.md#two-construction-paths-and-one-menu-side-existence-test)

## One ordinary-cover success test

The exact pit drawing has a child named **covermc**. The selected ordinary-cover
helper scans those named children and tests the actor's x/y point. It returns
true at the first successful test, rather than counting one new save per pit,
trench or sandbag. A no-match path has no explicit false return; the inspected bullet-save paths test
whether the result equals true.

Thus an actual qualifying pit overlap can feed the same ordinary-cover success
test. It does not automatically add a separate bunker save or a universal bonus
to every attack. Exact transforms, point boundaries and each shooter/ability
consumer still matter. [Protection stacking](defenses.md),
[query forms and geometry boundary](../player-construction-detail-evidence.md#ordinary-cover-and-classification-use-different-call-forms)

This identified component is not a verified complete mortar firing cycle, layout
or destruction model. Use the soldier's own firing/effect path for its weapon
behavior, and the source note for the pit's physical identity.

Sources: [Source identities](../player-notes/mortar-pit.md#citation-1). [Exact source](../player-construction-detail-evidence.md)
