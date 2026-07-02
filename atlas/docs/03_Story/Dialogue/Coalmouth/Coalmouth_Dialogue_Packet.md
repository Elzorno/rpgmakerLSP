---
atlas_id: ATLAS-STY-020
title: Coalmouth Dialogue Packet
status: Draft
version: 0.1
canonical: true
owner: Narrative Director
implementation_status: Not Started
dependencies:
  - LOC-COA-001
  - CHR-VER-001
  - QST-COA-001
related:
  - REG-COA-001
  - LOC-CMN-001
---

# Coalmouth Dialogue Packet

This packet defines the first-pass dialogue direction for Coalmouth and the Coalmouth Mine Crisis.

---

## Purpose

Coalmouth dialogue should establish a working town under pressure.

NPCs should reinforce:

- the mine is the town’s livelihood,
- machinery is behaving like angry spirits,
- Vera sees patterns others miss,
- workers are scared but stubborn,
- the region’s problem is practical before it becomes mythic.

---

## Dialogue State Model

```text
STATE_01_ARRIVAL
STATE_02_MINE_LOCKDOWN
STATE_03_VERA_INVESTIGATES
STATE_04_AFTER_NODE06
```

---

## Tone Rules

1. Use plain working-town language.
2. Avoid modern industrial-control jargon early.
3. Let Vera describe technical ideas through physical observation.
4. Respect workers; do not make belief in “spirits” sound foolish.
5. Keep message boxes short and implementable in RPG Maker MZ.

---

## Vera — Dialogue Scaffold

### STATE_01_ARRIVAL

```text
You hear that rhythm?

Carts, pulleys, pumps. A mine has a heartbeat when it's healthy.

This one is skipping.
```

### STATE_02_MINE_LOCKDOWN

```text
The foreman says spirits did it.

Maybe. But spirits don't repeat the same mistake every seventh pull.
```

### STATE_03_VERA_INVESTIGATES

```text
Don't touch that lever yet.

It's not stuck. It's waiting for something that isn't coming.
```

### STATE_04_AFTER_NODE06

```text
There.

Hear it now?

Still rough, but the mine's breathing again.
```

---

## Foreman — Dialogue Scaffold

### Role

Represents responsibility, fear, and pressure to keep workers alive.

```text
I don't care what name you give the thing down there.

Spirit, curse, machine, bad luck.

It nearly crushed three of my people.
```

After Node Six:

```text
The lifts are moving when told again.

That's the closest thing to a miracle I need today.
```

---

## Worried Miner — Dialogue Scaffold

```text
The carts rolled uphill yesterday.

Uphill.

You tell me what kind of honest mine does that.
```

After Node Six:

```text
I still don't trust the old rails.

But at least they stopped arguing with gravity.
```

---

## Injured Worker — Dialogue Scaffold

```text
The gate shut before the bell rang.

Or maybe the bell rang after. I keep hearing it wrong in my head.
```

---

## Old Railkeeper — Dialogue Scaffold

```text
A rail tells you what it wants if you listen long enough.

Lately these rails have been speaking over each other.
```

---

## Child Imitating Machine Rhythms — Dialogue Scaffold

```text
Clank... clank... hiss...

That's how it used to go.

Now it goes clank-hiss-clank-hiss-BANG.
```

---

## Shopkeeper — Dialogue Scaffold

```text
Lanterns, rope, salve, and courage.

I've only got the first three in stock.
```

---

## Implementation Notes

Codex should use these as placeholder lines for Coalmouth NPC event pages.

Claude or a human writer can expand them later while preserving role and tone.

---

## Open Questions

- Should the foreman become a full NPC object?
- Should Vera have optional dialogue explaining each mine puzzle?
- Should Coalmouth dialect be subtly distinct from Ashford?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Coalmouth dialogue packet |
