---
atlas_id: ATLAS-STY-010
title: Ashford Dialogue Packet
status: Draft
version: 0.1
canonical: true
owner: Narrative Director
implementation_status: Not Started
dependencies:
  - LOC-ASH-001
  - NPC-ELA-001
  - QST-HOM-001
related:
  - IMP-HOM-001
---

# Ashford Dialogue Packet

This packet defines the first-pass dialogue direction for Ashford.

It is designed for Claude, Codex, or a human writer to expand into final RPG Maker event text.

---

## Purpose

Ashford dialogue should make the village feel warm, ordinary, and quietly strange.

NPCs should reinforce:

- home is worth saving,
- old technology is misunderstood,
- Skyreach Hill is locally taboo,
- Glassfield Ruins are familiar but avoided,
- curiosity is rewarded.

---

## Dialogue State Model

Ashford NPCs should support these major states:

```text
STATE_01_INTRO
STATE_02_AFTER_TREMOR
STATE_03_AFTER_SWORD
STATE_04_AFTER_NODE07
STATE_05_BEFORE_MAINLAND_DEPARTURE
```

---

## Tone Rules

1. Keep lines short enough for RPG Maker message boxes.
2. Avoid modern technical vocabulary early.
3. Let villagers misinterpret technology naturally.
4. Use warmth and humor beside mystery.
5. NPCs should change after major events.

---

## Grandmother Elara — Dialogue Scaffold

### STATE_01_INTRO

Purpose: establish home and gentle warning.

Sample lines:

```text
You're awake early, Kai.

The island must be whispering louder than usual today.
```

```text
If you wander near the old stones, keep your eyes open and your pride quiet.
```

### STATE_02_AFTER_TREMOR

Purpose: show fear and inherited knowledge.

```text
That was no common tremor.

The hill remembers things the rest of us try to forget.
```

### STATE_03_AFTER_SWORD

Purpose: awe, fear, love.

```text
So it was true.

All these years, I hoped the old stories were only stories.
```

### STATE_04_AFTER_NODE07

Purpose: relief and consequence.

```text
The air feels lighter.

Not safe, exactly. But honest.
```

### STATE_05_BEFORE_MAINLAND_DEPARTURE

Purpose: departure blessing.

```text
Do not let the Sword make you proud.

Let it make you careful.
```

---

## Village Elder — Dialogue Scaffold

### Role

Represents local tradition and practical caution.

### Sample Lines

```text
Glassfield has always been part of Ashford.

That doesn't mean it belongs to us.
```

```text
The old panels keep the north wind out better than timber.

Useful things don't have to be understood, I suppose.
```

---

## Child Near Old Panel — Dialogue Scaffold

### Role

Shows old technology as play and curiosity.

### Sample Lines

```text
This metal wall hums if you press your ear to it.

Mama says not to do that, so I only do it when she's looking away.
```

After tremor:

```text
The wall hummed by itself today.

I didn't even touch it.
```

---

## Farmer With Warm Stones — Dialogue Scaffold

### Role

Shows technology as local utility.

### Sample Lines

```text
These warm stones keep the seedlings alive through cold nights.

My grandfather said they were a gift from the deep earth.
```

After Sword:

```text
The warm stones went cold for a breath, then came back hotter than before.

Can't say I liked that.
```

---

## Shopkeeper — Dialogue Scaffold

### Role

Practical tutorial and item economy.

### Sample Lines

```text
Take a look around.

If you're going past the village fence, don't go empty-handed.
```

After Node Seven:

```text
Everyone's buying rope, lantern oil, and courage today.

I'm out of one of those.
```

---

## Skyreach Joker — Dialogue Scaffold

### Role

Humor with local taboo.

### Sample Lines

```text
Skyreach Hill?

Sure, go on up. Wave to the curse for me.

Actually, don't. Curses are terrible at waving back.
```

After Sword:

```text
You went up the hill and came back glowing.

I went up there once and only came back itchy.
```

---

## Dock Messenger — Dialogue Scaffold

### Role

Foreshadows Rustshore and mainland travel.

### Sample Lines

```text
Boats are tied down at Rustshore.

Sea's calm, but the lighthouse keeps flashing wrong.
```

After Node Seven:

```text
The lighthouse settled down.

Dockmaster says the sea looks open again.
```

---

## Implementation Notes

Codex should place placeholder versions of these NPCs in Ashford and create event pages by story switch.

Claude or a human writer can later expand final dialogue while preserving these roles.

---

## Open Questions

- Should the village elder become a named NPC object?
- Should the dock messenger be reused at Rustshore Docks?
- Should Elara give Kai an item before departure?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Ashford dialogue packet |
