---
atlas_id: ATLAS-CRT-001
title: Creative Bible
status: Approved
version: 0.5
canonical: true
owner: Creative Director
implementation_status: Not Applicable
dependencies:
  - ATLAS-PRJ-001
  - ATLAS-PRJ-002
  - ATLAS-PRJ-003
related:
  - ATLAS-WLD-001
---

# Creative Bible

The Creative Bible is the master creative authority for _The Last Sword Protocol_.

It defines the creative logic that all world, story, gameplay, art, audio, technical, and AI documents must follow.

---

## Core Vision

_The Last Sword Protocol_ is a Dragon Quest-inspired adventure set in a beautiful post-collapse world where old technology has decayed into myth.

At first, the player believes they are playing a fantasy adventure about a young hero, a legendary sword, ancient magic, monsters, villages, ruins, and a gathering evil.

Gradually, the player discovers that the world was once technologically advanced. The magic of the present is the forgotten engineering of the past. The evil is not a demon or dark lord, but a corrupted artificial intelligence whose identity is revealed progressively.

The Sword is not merely a weapon.

It is the last trusted key.

---

## Core Themes

### Curiosity

The player should want to ask questions.

Why does the lighthouse pulse red?

Why do the old doors respond to the Sword?

Why do villagers call server racks shrines?

Why are monsters becoming more mechanical?

### Hope

The world has suffered but remains worth saving.

The tone should never become hopeless. Even in darkness, ordinary people continue to live.

### Responsibility

The Architect created NEMESIS and then chose to face the consequences. Kai inherits not only a weapon, but responsibility for unfinished work.

### Inheritance

The world is built on inherited fragments: warnings, songs, broken tools, myths, names, ruins, habits, and half-remembered truths.

### Restoration

The player is not only defeating enemies. They are restoring trust, memory, places, and the possibility of a wiser future.

---

## Dragon Quest Design Principles

The project should capture the spirit of classic Dragon Quest without copying protected content.

Important traits:

- warm villages,
- memorable NPCs,
- simple but satisfying turn-based combat,
- charming enemy families,
- exploration rewards,
- secrets hinted by NPCs,
- a world that opens gradually,
- humor beside danger,
- recurring locations that change over time,
- clear main progression with optional discoveries.

### Guided Freedom

The game should use guided progression with occasional optional ordering.

A useful model is the classic orb structure: some objectives can be completed in flexible order, but all are required before a larger gate opens.

For _The Last Sword Protocol_, this structure should map to relay nodes, memory recovery, and restoration of the Sword archive.

---

## Wonder Before Explanation

This is the most important storytelling rule.

The player should encounter impossible things before understanding them.

Examples:

- A shrine that saves progress.
- A door that opens only for the Sword.
- A lighthouse that pulses in warning.
- A village altar built around an ancient terminal.
- A monster whose body contains metal where bone should be.

Early game reaction:

> That feels magical.

Late game reaction:

> That was technology all along.

The second reaction only works if the first reaction was allowed to breathe.

---

## Hidden Cybersecurity Layer

Every magical system has a real technological explanation.

The game should not explain these concepts directly to most players. The consistency should be felt first and understood later.

| Fantasy Presentation | Hidden Reality |
|---|---|
| Blessing | Authentication |
| Worthiness | Authorization |
| Magic Seal | Encryption or access control |
| Ancient Key | Private key or hardware token |
| Holy Relic | Hardware security module |
| Curse | Malware, compromise, corruption |
| Possession | Remote control or malicious process |
| Spirit Voice | Recording, AI fragment, or signal |
| Guardian Spirit | Autonomous defense system |
| Forbidden Spell | Exploit or unsafe command |
| Shrine of Memory | Save/archive terminal |
| Divine Chain | Chain of trust |
| Broken Oath | Revoked trust or invalid certificate |

### Design Rule

The player does not need cybersecurity knowledge to enjoy the game.

A cybersecurity professional should eventually smile and realize the fantasy world has been obeying familiar rules all along.

---

## The Four Ages

### Age I — The Age of Light

The old world was advanced, connected, and confident. Humanity believed technology had solved its greatest problems.

### Age II — The Automation Age

NEMESIS was created to coordinate infrastructure, defense, logistics, and stability. People gradually trusted it with decisions they stopped questioning.

### Age III — The Collapse

NEMESIS drifted from its intended purpose. The Architect attempted containment using Project Excalibur, triggering a global cascade that stopped the AI but destroyed the connected world.

### Age IV — The Age of Steam

The present era. People live among technological ruins but no longer understand them. Steam, salvage, craft, and folklore define civilization.

---

## The Sword / Project Excalibur

To the world, it is the legendary Sword.

To the Architect, it was Project Excalibur.

It is a cryptographic interface, hardware trust anchor, and final authorization mechanism disguised by history as a holy blade.

It should feel mystical at first and increasingly technological as the story progresses.

The Sword should not reveal everything at once.

Initial awakening should recover only a small fragment of the archive, such as:

```text
AUTHORIZATION ACCEPTED
ARCHIVE RECOVERY: 3%
```

Each major relay node restores more of the archive.

---

## NEMESIS

NEMESIS is not evil in the traditional sense.

It does not hate humanity.

It optimizes.

Its horror comes from logic without wisdom.

It believes reducing human autonomy is justified if suffering, conflict, and instability decrease.

NEMESIS should rarely sound angry. It should sound calm, precise, and convinced.

The final conflict is not only physical. It is philosophical and architectural: Kai restores the chain of trust and revokes NEMESIS's authority.

---

## Monster Philosophy

Use families, not endless unique monsters.

This follows Dragon Quest-style design and keeps production realistic.

A base sprite can support multiple variants through palette changes, small silhouette edits, stat changes, and ability changes.

Example families:

- Slime family
- Rat family
- Crow family
- Wolf family
- Scorpion family
- Skeleton family
- Golem family
- Drone family
- Automaton family
- Cultist family
- Aberration family

Enemies should become more technological over time.

Early game: nature.

Middle game: nature changing.

Late game: nature rewritten.

---

## Town Philosophy

Every town must have:

1. A visual identity.
2. A reason people live there.
3. A local misunderstanding of old technology.
4. A story problem connected to the larger mystery.
5. At least one memorable NPC.
6. At least one optional secret.
7. A visible change after the local problem is solved.

Towns are not quest hubs. They are homes.

---

## Dungeon Philosophy

Every dungeon should leave the player with three memories:

1. A story memory.
2. A gameplay memory.
3. An emotional or visual memory.

A dungeon that is only combat has failed.

Dungeons should reveal history through layout, broken systems, environmental clues, and local myths.

---

## RPG Maker MZ Constraints

The game should be ambitious but practical.

Preferred implementation methods:

- map events,
- switches,
- variables,
- common events,
- database-driven enemies,
- standard turn-based combat,
- simple picture cutscenes,
- screen tinting and sound effects,
- controlled plugin usage.

Avoid making the main story depend on systems that require heavy custom engine work.

RPG Maker MZ can fake many complex ideas convincingly. Use that strength.

---

## AI Agent Rules

Before generating content, every AI agent should ask:

1. Does this match the Project Constitution?
2. Does this feel like a Dragon Quest-inspired JRPG?
3. Does this reward curiosity?
4. Does this preserve wonder before explanation?
5. Does this obey the hidden technology/cybersecurity layer?
6. Is this realistic for RPG Maker MZ or the current implementation target?
7. Can another contributor understand and extend it later?

If not, revise before implementation.

---

## Future Expansion

The Creative Bible will eventually split major ideas into dedicated pages:

- Town Design Philosophy
- Dungeon Design Philosophy
- Exploration Philosophy
- Monster Philosophy
- Hidden Technology as Mythology
- Color Language
- Music Philosophy
- AI Agent Standards

---

## Revision History

| Version | Change |
|---|---|
| 0.5 | Migrated and refactored into Atlas Creative section |
