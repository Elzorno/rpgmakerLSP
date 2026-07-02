---
Title: World and Location Bible
Version: 0.1
Status: Draft
Owner: Creative Direction
Last Updated: 2026-07-01
Depends On: Creative_Bible.md, ../00_Project/Project_Constitution.md
Referenced By: Future Story Bible, Dungeon Bible, Map Implementation Guide, Bestiary, RPG Maker Blueprint
---

# World and Location Bible

This document defines the world structure, required locations, overworld placement logic, and region-by-region purpose for *The Last Sword Protocol*.

It is the bridge between the story and the RPG Maker MZ maps.

The goal is not merely to list towns and dungeons. The goal is to explain why each place exists, what it teaches the player, how it supports the hidden technology layer, and how it should appear on the overworld.

---

## 1. Design Purpose

The world map must support a classic Dragon Quest-style journey:

- a safe hometown,
- nearby danger,
- guided expansion,
- visible landmarks,
- ships and travel gates,
- optional secrets,
- recurring towns,
- a final distant evil,
- places the player sees long before they can reach.

The world should feel like fantasy first and forgotten infrastructure second.

Early players should see villages, caves, towers, shrines, marshes, castles, mines, deserts, mountains, and strange ruins.

Late players should realize they have been walking across the bones of a distributed technological civilization.

---

## 2. Overworld Philosophy

The overworld is not random geography.

It is the decayed topology of the old world.

Mountains, oceans, bridges, islands, and deserts should secretly reflect infrastructure decisions from the Age of Light and Automation Age.

### Hidden Design Logic

| Fantasy Geography | Hidden Old-World Reality |
|---|---|
| Isolated home island | Secure enclave protecting Project Excalibur |
| Relay shrines | Distributed network relay nodes |
| Forbidden mountains | Physical segmentation / restricted infrastructure zones |
| Ancient roads | Collapsed highways or transit corridors |
| Towers | Communications masts, observatories, or network repeaters |
| Castles | Settlements built over hardened infrastructure |
| Temples | Data centers, access facilities, medical sites, or control rooms |
| Dead lands | Contaminated or heavily automated old-world core zones |

The player does not need to know this early. The design team must know it always.

---

## 3. Region Structure Overview

The world is divided into major progression regions.

Each region teaches one question.

| Progression | Region | Story Question | Gameplay Role |
|---|---|---|---|
| Journey I | Kai's Home Island | Who am I? | Tutorial, Sword awakening, first relay |
| Journey II-A | Coalmouth Region | What happened underground? | First mainland town, Vera joins, ICS/automation theme |
| Journey II-B | Athenaeum Region | What happened to knowledge? | Eldon joins, archive corruption theme |
| Journey II-C | Irongate Region | What happened to authority? | Herald reveal, military/social engineering theme |
| Journey II-D | Driftlands | How did ordinary people survive? | flexible objective, supply-chain theme, Cipher foreshadow |
| Journey II-E | New Meridian | What remained of civilization? | major city, Herald climax, Cipher joins fully |
| Journey III | Dead Circuit | What really happened? | late-game truth, high-tech ruins, final approach |
| Journey IV | The Vault | Can trust be restored? | final dungeon and NEMESIS sequence |
| Optional | Lost Kingdom | What else was preserved? | endgame secrets and strongest optional content |

---

## 4. Required Main Locations

These are the required locations needed to complete the core story.

### Journey I — Kai's Home Island

#### Ashford

Kai's home village. Built inside and around the shell of an old-world factory.

- Emotional purpose: home, warmth, grandmother, local identity.
- Gameplay purpose: starting town, tutorials, early NPC relationships.
- Hidden technology: factory heat systems interpreted as natural warm veins.
- Required maps: village exterior, Kai/grandmother house, inn or rest house, small shop, elder/chief house, optional interiors.

#### Rustshore Docks

Small harbor on the south coast of the island.

- Emotional purpose: first glimpse that the world is larger than Ashford.
- Gameplay purpose: eventual exit point to mainland.
- Hidden technology: scrap lighthouse with failing sensor array.
- Required maps: dock exterior, lighthouse interior or event area, dockmaster hut.

#### Fogfen Marsh

Eastern wetland affected by signal corruption.

- Emotional purpose: nature feels wrong for the first time.
- Gameplay purpose: early combat practice and optional/pre-story dungeon.
- Hidden technology: submerged cables, residual EM fields, corrupted wildlife.
- Required maps: marsh field, small deep marsh area, optional hidden item landmark.

#### Glassfield Ruins

Central old-world facility swallowed by grass and cracked concrete.

- Emotional purpose: first major sense that the island is built over something hidden.
- Gameplay purpose: puzzle/tutorial ruin, later route into Sealed Node.
- Hidden technology: identity relay socket, inactive terminal systems.
- Required maps: exterior ruins, shallow facility, sealed lower entrance.

#### Skyreach Hill

Forbidden northern hill containing the hidden cave and Sword.

- Emotional purpose: destiny, taboo, family warning.
- Gameplay purpose: story gate after tremor.
- Hidden technology: physical security around Project Excalibur access site.
- Required maps: hill path, cave entrance, three challenge chambers, inner sanctum.

#### Hidden Cave / Project Excalibur Vaultlet

The cave where Kai obtains the Sword.

- Emotional purpose: Kai accepts responsibility.
- Gameplay purpose: trial sequence and Sword acquisition.
- Hidden technology: bloodline authentication, local secure archive recovery.
- Required chambers: physical trial, mental trial, spiritual/trust trial, pedestal chamber.

#### The Sealed Node

Final dungeon of the island arc below Glassfield.

- Emotional purpose: home was never separate from the world's danger.
- Gameplay purpose: first relay shutdown, first boss, Act I climax.
- Hidden technology: island relay node / secure enclave network segment.
- Required maps: cave-server hybrid dungeon, relay chamber, boss arena.

---

### Journey II-A — Coalmouth Region

#### Coalmouth

Mining town built around old subway/mining infrastructure.

- Emotional purpose: hardworking people trapped by machines they depend on.
- Gameplay purpose: first mainland town, Vera introduction.
- Hidden technology: industrial control systems / compromised automation.
- Required maps: town exterior, inn, shop, foreman's hall, Vera's workshop.

#### Coalmouth Mine

Old-world mining and transit tunnels now treated as coal mines.

- Emotional purpose: labor versus forgotten machinery.
- Gameplay purpose: first mainland relay/automation dungeon.
- Hidden technology: ICS/SCADA compromise; mining machines obey corrupted commands.
- Required maps: upper mine, machine tunnels, control room, Iron Foreman boss arena.

---

### Journey II-B — Athenaeum Region

#### The Athenaeum

Library-city built inside a collapsed university and archive complex.

- Emotional purpose: knowledge preserved but misunderstood.
- Gameplay purpose: Eldon joins; information integrity theme.
- Hidden technology: corrupted data stores, receiver arrays, archive indexes.
- Required maps: city exterior, Grand Archive, Scholar's Rest, Bookwright's, Eldon's Study.

#### Signal Tower

Tower near or within the Athenaeum that receives old-network transmissions.

- Emotional purpose: scholars hear voices they mistake for divine or prophetic contact.
- Gameplay purpose: dungeon and node shutdown.
- Hidden technology: network receiver, broadcast engine, poisoned data stream.
- Required maps: tower base, library-machine floors, broadcast chamber.

---

### Journey II-C — Irongate Region

#### Irongate

Fortified military settlement built over an old defense facility.

- Emotional purpose: order, fear, obedience, and authority.
- Gameplay purpose: first major Herald confrontation.
- Hidden technology: command authentication abuse, spoofed authority, social engineering.
- Required maps: fortress town, barracks, command hall, restricted bunker.

#### Irongate Bunker

Buried military control structure beneath the town.

- Emotional purpose: the danger of obeying a voice without judgment.
- Gameplay purpose: expose the Herald and NEMESIS's influence.
- Hidden technology: compromised command channel, forged orders, old defense permissions.

---

### Journey II-D — The Driftlands

#### The Drift

Nomadic caravan settlement that relocates around ancient trade routes.

- Emotional purpose: survival, stories, trade, memory carried by people instead of buildings.
- Gameplay purpose: flexible objective region, optional-order progression.
- Hidden technology: supply-chain compromise through traded relics.
- Required maps: caravan camp, market tents, storyteller tent, relic wagon.

#### Buried Relay Station

Ancient underground relay discovered by traders.

- Emotional purpose: curiosity can save or endanger communities.
- Gameplay purpose: node shutdown, Cipher introduction/foreshadow.
- Hidden technology: compromised dependency chain, relay service reactivation.

---

### Journey II-E — New Meridian Region

#### New Meridian

Largest surviving city. Built inside and around old civic infrastructure.

- Emotional purpose: civilization almost remembered itself.
- Gameplay purpose: major hub, political crisis, Herald climax, Cipher joins fully.
- Hidden technology: surviving electrical systems, access elevators, civic AI fragments.
- Required maps: city exterior, governor's hall, market, residential quarter, old transit hub, restricted tower.

#### Meridian Core

Hidden infrastructure beneath New Meridian.

- Emotional purpose: the closest surviving echo of the old world.
- Gameplay purpose: major boss, large story reveal.
- Hidden technology: civic control system under NEMESIS influence.

---

### Journey III — The Dead Circuit

#### Dead Circuit Wastes

Ruined server and infrastructure graveyard surrounding the Vault.

- Emotional purpose: beauty gives way to silence and scale.
- Gameplay purpose: late-game overworld/dungeon chain.
- Hidden technology: backbone network ruins, failed server farms, hardened conduits.

#### Broken Spire

Massive visible landmark seen earlier but reached late.

- Emotional purpose: long-term payoff for player curiosity.
- Gameplay purpose: traversal landmark and late dungeon.
- Hidden technology: collapsed communications/space-elevator segment or data tower.

---

### Journey IV — The Vault

#### The Vault Exterior

Hardened entrance to NEMESIS's core data center.

- Emotional purpose: crossing from myth into truth.
- Gameplay purpose: final dungeon entry.
- Hidden technology: physical security perimeter and deep access control.

#### NEMESIS Core

Final data center cathedral.

- Emotional purpose: the machine-god revealed as infrastructure.
- Gameplay purpose: final battles, terminal interactions, Final Protocol.
- Hidden technology: central AI core, trust chain restoration, authority revocation.

---

## 5. Optional and Secret Locations

Optional content should reward curiosity without blocking main progression.

### The Lost Kingdom

A hidden automated city whose systems partially survived the Collapse.

- Role: optional endgame dungeon and lore reward.
- Hidden technology: cloaked or isolated smart city / secure preservation zone.
- Reward type: strongest optional equipment, prototype lore, hidden memories.

### Singing Lake

A lake said to contain spirits singing beneath the water.

- Hidden reality: damaged sonar or acoustic warning system.
- Role: optional puzzle, memory fragment, rare item.

### Valley of Stars

A field where stars supposedly fell from heaven.

- Hidden reality: satellite debris field.
- Role: optional exploration, rare crafting material, late-game clue.

### Endless Bell Tower

A tower whose bell rings at sunset with no bell-ringer.

- Hidden reality: automated warning beacon.
- Role: optional lore and hidden item clue.

### Sleeping Giant

A mountain said to move once every thousand years.

- Hidden reality: buried colossal excavator or terraforming machine.
- Role: optional late-game boss/dungeon.

---

## 6. Relay Node Structure

Relay nodes are the world's hidden progression equivalent to classic JRPG magical objectives.

They should feel like sacred or cursed places to normal people.

In truth, they are distributed infrastructure nodes.

| Node | Region | Fantasy Understanding | Hidden Reality | Archive Reward |
|---|---|---|---|---|
| Node 7 | Home Island | Sealed curse beneath the island | Secure enclave relay | Authentication / 3% archive |
| Node 6 | Coalmouth | Angry mine spirits | ICS control relay | First mainland map clue |
| Node 5 | Athenaeum | Voices of forbidden knowledge | Corrupted receiver/archive node | Integrity clue |
| Node 4 | Irongate | Divine command authority | Spoofed military command relay | Herald/NEMESIS pattern clue |
| Node 3 | Driftlands | Relic sickness spreading by trade | Supply-chain relay compromise | Cipher clue |
| Node 2 | New Meridian | Governor's divine mandate | Civic control node | Architect logs |
| Node 1 | Dead Circuit | Gate of the Machine God | Core backbone relay | Final Protocol fragment |

Exact numbering can be revised later, but the island should remain Node 7 to preserve the current story beat: `NODE SEVEN OFFLINE`.

---

## 7. Overworld Map Placement Guidance

The current overworld map should be treated as a strong prototype rather than locked geography.

### Home Island

The bottom-middle island remains Kai's starting island.

Suggested internal placement:

- Ashford: warm central/southwest village area.
- Rustshore Docks: south coast.
- Fogfen Marsh: east side wetland.
- Glassfield Ruins: central field.
- Skyreach Hill: northern high ground.
- Sealed Node: beneath Glassfield / central island.

### Mainland Progression

Mainland regions should be placed so the player can experience guided expansion:

1. First landing near Coalmouth.
2. Route opens toward Athenaeum.
3. Military checkpoint or terrain gate leads to Irongate.
4. Ship or pass opens Driftlands.
5. Major road/ship route opens New Meridian.
6. Late-game access opens Dead Circuit.
7. Final path opens Vault.

### Landmark Rule

Players should see at least three major landmarks before they can reach them:

- Broken Spire.
- Dead Circuit skyline.
- Sleeping Giant or Hollow Mountain.

These landmarks create long-term curiosity.

---

## 8. Required Next Work

This document needs future expansion in Sprint 2:

1. Review the current overworld map visually and assign coordinates/regions.
2. Decide which existing prototype maps are kept, renamed, or discarded.
3. Create region-specific encounter lists.
4. Create location design packets for Ashford, Coalmouth, Athenaeum, Irongate, Drift, New Meridian, Dead Circuit, and Vault.
5. Define optional secret locations and clue chains.
6. Create an implementation map manifest for Codex.

---

## 9. Canonical Summary

The world of *The Last Sword Protocol* should feel like a Dragon Quest fantasy world built over the bones of a forgotten technological civilization.

Every location must serve story, exploration, atmosphere, and hidden engineering logic.

The map exists to serve the journey.

If the map and story disagree, adjust the map.
