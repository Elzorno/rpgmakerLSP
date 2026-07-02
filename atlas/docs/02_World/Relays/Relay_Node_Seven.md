---
object_id: REL-007
atlas_id: REL-007
title: Relay Node Seven
object_type: Relay
status: Draft
version: 0.1
canonical: true
owner: Creative Director
implementation_status: Not Started
region: REG-HOM-001
location: LOC-SND-001
relationships:
  located_in:
    - LOC-SND-001
  guarded_by: []
  unlocks:
    - SYS-ARCHIVE-001
  related_to:
    - ITM-SWD-001
    - QST-HOM-003
---

# Relay Node Seven

Relay Node Seven is the first relay node encountered by the player and the climax objective of Home Island.

---

## Purpose

Node Seven introduces the relay progression structure and the archive recovery pattern.

It proves that the island's curse is actually a failing secure infrastructure node.

---

## Fantasy Presentation

Villagers know it only as a sealed curse beneath the island.

Some may believe the old stones below Glassfield hold an angry spirit or ancient punishment.

---

## Hidden Reality

Node Seven is a secure enclave relay associated with Project Excalibur.

It verifies the Sword, responds to Kai's authenticated identity, and can be taken offline or restored only through trusted authority.

---

## Story Function

After Kai obtains the Sword, Node Seven becomes accessible beneath Glassfield Ruins.

When shut down, it displays or implies:

```text
NODE SEVEN: OFFLINE
ARCHIVE RECOVERY: 3% or 5%
```

---

## Archive Recovery Effect

Draft options:

| Option | Effect |
|---|---|
| Conservative | Archive begins at 3% after Sword awakening and remains 3% after Node Seven |
| Rewarding | Archive begins at 3% and rises to 5% after Node Seven shutdown |

Recommendation: use the rewarding option for clearer player feedback.

---

## Guardian / Boss

The guardian is not yet named.

Draft boss role:

- ancient security construct,
- degraded guardian system,
- first cave-machine hybrid boss.

Reserved future ID:

```text
BOS-N07-001
```

---

## Shutdown Sequence

The shutdown should feel mystical first and technical second.

Suggested sequence:

1. Guardian defeated.
2. Sword resonates with relay core.
3. Lights shift from red/unstable to blue-white/clean.
4. Short archive message appears.
5. Screen flash or sound confirms node status.
6. New mainland path opens through Rustshore Docks.

---

## Relationships

| Relationship | Target ID | Notes |
|---|---|---|
| located_in | LOC-SND-001 | Relay core inside Sealed Node |
| related_to | ITM-SWD-001 | Sword enables access |
| completes_quest | QST-HOM-003 | Node Seven Offline |
| unlocks | SYS-ARCHIVE-001 | Archive recovery pattern begins |

---

## RPG Maker Implementation Notes

Suggested switches:

```text
J1_Node07_GuardianDefeated
J1_Node07_Offline
J1_Mainland_TravelUnlocked
```

Suggested variables:

```text
Archive_Recovery_Percent
Current_Relay_Count
```

---

## Open Questions

- Should Node Seven be called “Node Seven” in early text, or should that term appear only after shutdown?
- What is the guardian's fantasy-facing name?
- Should shutdown be framed as destroying, cleansing, or quieting the node?

---

## Revision History

| Version | Change |
|---|---|
| 0.1 | Initial Relay Node Seven object |
