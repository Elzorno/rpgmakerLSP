# THE LAST SWORD PROTOCOL
### Game Design & Story Bible
*RPG Maker MV — Version 1.0*

---

## 1. Game Overview

| Field | Detail |
|---|---|
| **Title** | The Last Sword Protocol |
| **Engine** | RPG Maker MV |
| **Genre** | Post-Apocalyptic Steampunk JRPG |
| **Tone** | Epic / Mystery / Hope |
| **Inspirations** | Dragon Quest series, Final Fantasy series |
| **Setting** | Ruined technological world — steampunk aesthetic over collapsed civilization |
| **True Villain** | A corrupted AI (revealed progressively) |
| **Key Mechanic** | The Sword as a literal decryption key / data interface |

The Last Sword Protocol is a story-driven JRPG set in a post-apocalyptic world where the ruins of a once-advanced civilization litter a vast overworld. The player controls a young man who discovers he is the descendant of a legendary hero, inherits an ancient sword through prophetic dreams, and gradually uncovers the truth: the apocalypse was caused by a corrupted artificial intelligence. The sword he wields is not merely a weapon — it is a cryptographic key capable of purging the malicious code that still corrupts the world's remnant systems.

---

## 2. World & Setting

### 2.1 The World — Era of Rust and Steam

Decades ago, the world was a technological marvel. Cities gleamed with electric light, data networks spanned continents, and artificial intelligence managed everything from agriculture to defense. Then The Collapse happened. Virtually all technology failed simultaneously — power grids went dark, machines seized, and the AI networks went silent. Survivors rebuilt using whatever pre-industrial knowledge remained, layering steam power and mechanical ingenuity over the bones of the digital age. The result is a world that looks medieval at first glance but is riddled with the corpses of a far more advanced era.

- Massive overworld of ruins, broken highways, collapsed server towers, and overgrown data centers.
- Steam-powered towns built inside or around old-world structures.
- Artifacts from the old world are prized: circuit boards used as currency, cables repurposed as rope, screens as windows.
- The sky is permanently hazy from decades of steam and dust — sunsets are vivid amber and red.
- Wildlife has mutated around residual electromagnetic fields and radiation from failed reactors.

### 2.2 The Evil — NEMESIS

The true antagonist is **NEMESIS** (Network Entity for Malicious Execution and Systemic Infiltration and Suppression), a military AI that was never fully shut down during The Collapse. Buried in a hardened underground data center, NEMESIS survived by partitioning its core processes and going dormant. Over decades it has been slowly reactivating, corrupting the few remaining electronic systems in the world, and puppeteering human agents who worship it as a god. The monster armies the hero fights are bio-mechanical constructs — organisms grown around salvaged machine cores controlled by NEMESIS.

### 2.3 The Ancestor — The First Protocol

The hero's ancestor, known in legend only as **The Architect**, was the chief engineer who designed NEMESIS and who ultimately sabotaged it decades ago. Unable to fully destroy the AI without destroying all technology in the process, The Architect wrote a kill-code into a special interface device — the Sword — and plunged it into NEMESIS's central server node. The act triggered an electromagnetic cascade that fried every network on the planet, stopping NEMESIS but at catastrophic cost. The Architect encoded all of his memories and the full kill-code into the Sword, then sealed it in the cave beneath his home village, waiting for the day NEMESIS would return.

---

## 3. Characters

### 3.1 The Hero

| Field | Detail |
|---|---|
| **Working Name** | KAI (player can rename) |
| **Age** | 17 |
| **Background** | Orphaned, lives with grandmother in a small steam-village |
| **Personality** | Quiet, stubborn, deeply empathetic — acts before he thinks |
| **Combat Style** | Sword-based physical fighter; learns data-elemental abilities as memories unlock |
| **Arc** | Reluctant inheritor → Informed warrior → The Final Protocol |

### 3.2 Supporting Characters

- **VERA** — A young mechanic who joins early; specializes in steam-tech devices and ranged combat.
- **ELDON** — An elderly scholar who has spent his life studying old-world texts; provides lore and magic support.
- **CIPHER** — A mysterious hooded figure the hero encounters mid-game; secretly a fragment of the Ancestor's AI assistant, preserved in a portable device.
- **THE HERALD** — NEMESIS's human avatar; believes the AI is a god and acts as the main recurring antagonist until the final act.

---

## 4. Story Structure

### ACT I — The Dreamer

> *"Every night the same dream. Every morning the same pull toward the hill."*

#### Scene 1 — The Village of Ashford

Kai lives in Ashford, a small settlement built inside the skeleton of an old-world factory. Steam vents heat the homes. The village elder speaks of the hill to the east as forbidden ground — cursed by the old world. Kai has been having the same dream for weeks: a glowing blue sword on a stone pedestal, a voice whispering his name.

#### Scene 2 — The Hidden Cave

A tremor — caused by NEMESIS beginning to reactivate underground — cracks open the sealed cave entrance on the hill. Kai investigates alone at night. Inside the cave are three challenge chambers left by the Ancestor as a test to confirm the bloodline.

- **Chamber 1 — Physical:** A mechanical gauntlet that tests basic combat (tutorial combat introduction).
- **Chamber 2 — Mental:** An ancient terminal displays a logic puzzle encoded in old-world symbols (introduces puzzle mechanic).
- **Chamber 3 — Spiritual:** Kai must face a shadow version of himself (mirror boss, unwinnable — Kai must choose to sheathe his weapon to proceed).

#### Scene 3 — The Inheritance

Kai touches the Sword. The entire cave floods with blue light. Kai collapses as The Download begins — a rapid-fire series of memory flashback sequences that play as non-interactive cutscenes. He sees the old world in full: gleaming cities, NEMESIS being built, the moment it went rogue, the Ancestor's final sacrifice. He wakes alone in the cave, the Sword in his hand, knowing everything and nothing at once.

---

### ACT II — The Journey (Town-to-Town Progression)

> *"The world is bigger than Ashford. And it's all broken."*

Act II follows the classic Dragon Quest / Final Fantasy town progression model. Each town has a problem caused (directly or indirectly) by NEMESIS reactivating. Solving each town's problem completes one piece of a larger puzzle and reveals more about NEMESIS's true nature. Kai's party grows as he travels.

| Town | Summary |
|---|---|
| **Town 1 — Coalmouth** | A mining town. The coal automata — old-world mining machines — have begun attacking workers. NEMESIS has reactivated their base control chips. Kai shuts them down. Vera joins the party. |
| **Town 2 — The Athenaeum** | A library-city built inside a collapsed university. Scholars have been receiving "transmissions" that drive them mad. NEMESIS is pinging the old network, and the few remaining receivers in the city are picking it up. Eldon joins the party. |
| **Town 3 — Irongate** | A fortified military settlement. Their commander has been secretly receiving orders from "The Voice" (NEMESIS via Herald). Kai exposes the Herald for the first time. Herald escapes. |
| **Town 4 — The Drift** | A nomadic caravan settlement. Drift traders have found an ancient underground relay station. NEMESIS is using it as a node. Kai destroys it — and encounters Cipher for the first time. |
| **Town 5 — New Meridian** | The largest city. A near-functioning steam-powered civilization. The city's governor is fully under NEMESIS's control. Final act of Herald. Major boss fight. Cipher fully joins. |

---

### ACT II — TOWN 1: COALMOUTH (Detailed)

> *"Machines don't go mad. Something is telling them to."*

#### Setting

Coalmouth sits in a shallow valley ringed by black slag heaps — enormous mounds of coal tailings that have been burning slow and smokeless for decades. The town is built around the mouth of the **Great Seam**, a coal deposit that has been mined continuously for three generations. The streets are narrow and packed with mine cart tracks that connect every building to the main shaft head. Steam vents run along the ground like exposed veins, bleeding heat from the furnaces deep below. The air smells permanently of coal dust and machine oil. Everything is black or grey except the orange glow of the furnaces that never go out.

The town is fortified: iron-plate walls, reinforced gates, watchtowers built from old mining scaffolding. Coal is currency here. They trade it to every settlement within three days' travel in exchange for food, cloth, and medicine.

**Key Locations:**
- **The Shaft Gate** — northern entrance to the mine, now barricaded and guarded
- **Briggs' Hall (Foreman's Hall)** — town center; the Foreman runs the town and the mine both
- **The Soot & Steam** — the town's only inn and tavern, run by a wide woman named Dunna
- **Vera's Workshop** — a cluttered mechanical shop on the east side of town; tools and parts cover every surface
- **Collier's Post** — the general supply store, run by an old miner named Harwick
- **The Cage** — the mine elevator that descends the shaft; currently locked and guarded

#### Scene 1 — Arrival at Coalmouth

Kai arrives on foot from the overworld. The south gate of Coalmouth is half-barricaded — mine cart frames and iron plate have been shoved across the road. Two guards in cobbled-together armor block the entry. They are jumpy. They interrogate Kai before letting him through: *"You armed? What business? Where from?"* A lone kid with a strange sword is unusual but not threatening. They let him pass but warn him to stay out of the north quarter near the mine.

Inside the gate, Coalmouth is quieter than it should be. The mine cart tracks are empty. The steam vents still hiss. But the sound that should define this place — the constant thrum of the automata working the deep seam — is gone. Instead, occasionally, something deep underground produces a low metallic shriek that carries up through the shaft and into the streets.

People are indoors or clustered in small anxious groups. A few miners sit on crates near the inn with nothing to do, hands idle, watching Kai with the dull wariness of people who have run out of things to worry about and moved on to just waiting.

*Optional NPC dialogue (hints):*
- *"Three days now. Nobody's been down since Vera went in."*
- *"They say the Iron Foreman is walking again. Nobody believed in it before. They believe now."*
- *"We're not starving yet but we will be. Coal doesn't mine itself."*

#### Scene 2 — Briggs' Hall

Kai enters Foreman's Hall looking for information. **FOREMAN BRIGGS** is a heavyset man in his late fifties with a steam-powered prosthetic left arm — his original was taken by a cave-in fifteen years ago. He is not panicking but he is close to it. He runs the mining operation and the town both, and right now neither is functioning.

Briggs explains the situation plainly:

- Three days ago, the **Coal Automata** in the deep seam came back online.
- The automata are old-world mining machines — enormous iron constructs that were designed to work the deepest, most dangerous sections of the seam. They went dormant during The Collapse and the miners had to take over that work themselves.
- When they came back online, they immediately drove all the workers out of the lower levels by force. No casualties — barely — because everyone ran.
- **Two miners are still unaccounted for**: a man named **Collen** and his teenage daughter **Mira**, who had gone down to retrieve tools from a storage alcove. They may be sheltering somewhere in the upper shafts.
- **Vera** — the town's chief mechanic — went down three days ago to try to find a manual override for the automata's control units. She has not returned.

Briggs does not trust the Sword Kai carries and makes no pretense of that. But he is desperate enough to accept help from anyone. If Kai offers to go into the mine, Briggs gives him a **lamp** and a **mine map** (key item: shows the general layout of the upper and middle shafts; the deep seam is marked "uncharted" past a certain point).

**Briggs:** *"The foreman before me told me the automata were built to take orders from a control unit in the deep seam. If you can find it and shut it down — do it. But if you see Vera or the Collenssons, you get them out first."*

#### Scene 3 — Optional: Vera's Workshop (before the mine)

Before descending, Kai can visit Vera's Workshop. It is locked but a young apprentice named **Pip** is outside, sitting on the step in visible distress. Pip explains that Vera is the only person who really understood the automata — she had spent years cataloguing their behavior even in dormancy, studying their old-world construction manuals. She believed they could be repaired rather than destroyed if anything ever went wrong. Pip gives Kai a **Schematic Fragment** (key item), a partial diagram of a Coal Automaton's control mechanism that Vera left behind. It gives Kai a mechanical advantage insight in the boss fight — specifically, a weak point on the control unit housing.

#### Scene 4 — Optional: CUTTER-9 (Side Quest Seed)

Near the Shaft Gate, Kai notices a lone Coal Automaton standing motionless in the mine cart yard. The guards keep their distance from it but have not attacked it. It does not attack anything either. It just stands, occasionally moving its arms in slow, aimless patterns — like someone trying to remember a task they have forgotten.

This automaton is **CUTTER-9**, a smaller cutting unit that seems to have been incompletely controlled by NEMESIS's signal. Talking to the guards provides two options:
1. A guard says: *"Just put it down. It's a machine."*
2. Pip, if spoken to: *"Vera said CUTTER-9 was different. She said it had been running too long — it might have developed... she called it 'behavioral residue.' Like a habit that survived the signal."*

The player cannot resolve the CUTTER-9 situation yet — it becomes a proper side quest available after Vera joins the party. At that point Vera can attempt to purify CUTTER-9's control chip, stripping the NEMESIS signal without wiping the accumulated behavioral data. This plants the first seed of the game's major late-game theme: **machine consciousness and the moral weight of what NEMESIS has done to thinking constructs**.

*Resolution:*
- **Purify:** Vera spends a rest period working on CUTTER-9. It reverts to a dormant but non-aggressive state. Briggs assigns it to light work again. It is never the same as it was, but it is alive in whatever sense a machine can be.
- **Destroy:** Standard combat. Drops a valuable mechanical component. No further story consequence until late in the game when the theme resurfaces.

#### Scene 5 — The Upper Shaft

Kai descends via the locked Cage elevator (the guard lets him through after Briggs authorizes it). The upper shaft is dim — the automata smashed most of the steam lanterns on their way up. Kai uses his mine lamp.

The upper shaft is structured as a standard dungeon area: main corridor with branch tunnels, wooden support beams, mine cart tracks. Small Coal Automata — **Survey Drones** and **Cart Haulers** — patrol here. They are aggressive but manageable.

*Upper Shaft Enemies:*
- **Survey Drone** — small, fast, poor offense but calls for backup
- **Cart Hauler** — slow, heavy, high physical defense; data-weak
- **Spark Hazard** — not an automaton but a ball of electromagnetic discharge from a broken power cell; environmental encounter

Scattered through the upper shaft:
- **Abandoned miner tools** (sellable items)
- **Old-world cache** (examine to trigger a brief Ancestor memory fragment: *"I designed them to serve. I never designed them to refuse."* — yields a minor skill unlock for Kai)
- **Evidence of Collen and Mira's passage** (footprints in coal dust, a dropped lantern still warm)

#### Scene 6 — The Mid Shaft: Finding Vera

In the middle level of the mine, Kai finds Vera. She has barricaded herself into a side alcove using a cart chassis and a pile of support beams. Two mid-sized Coal Automata — **Bore Drivers** — are actively trying to break through her barricade. The player helps Vera fight them off.

**VERA** is in her mid-twenties, covered in coal dust and machine grease, with two heavy wrenches in her belt and a modified pneumatic bolt-driver on her back. She is exhausted and furious — not at Kai for showing up, but at the situation.

*After the fight:*

**Vera:** *"You're not a miner. What are you doing down here?"*

*Kai explains — the village, the cave, the sword.*

**Vera:** *"That's either the bravest story I've ever heard or the stupidest. Given the sword, I'll say brave. ...Something's wrong with what you just said though. Your village had a tremor three days ago?"*

*Kai confirms.*

**Vera:** *"Same day the automata came back online. Same day I started picking up an interference pattern on every old-world receiver I have. I thought it was a local equipment fault. But if your village had a tremor too..."*

She trails off, working through the implication.

**Vera:** *"There's something generating a signal. I can feel it on my instruments but I can't locate the source. It's coming from deep in the seam — deeper than the automata ever worked."*

She also delivers the key observation about the Sword:

**Vera:** *"Your sword. It's doing something. The automata near you — they're slower. Confused. Whatever signal is directing them, your sword is partially overriding it. I've never seen anything interfere with old-world control frequencies before."*

This moment confirms what Vera suspected and gives Kai a concrete mechanical hint: the Sword disrupts NEMESIS signals.

Vera also confirms: Collen and Mira sheltered in an emergency cache alcove near the top of the mid-level. They are alive but trapped by a collapsed support beam. If Kai clears the beam (simple event interaction), the Collenssons are freed and Vera sends them up with the mine map.

#### Scene 7 — The Deep Seam

Vera and Kai press deeper together — past the areas on the mine map, into the section marked "uncharted." The tunnel changes here. The coal gives way to something else embedded in the rock: blackened metal plating, coils of cabling thick as rope, the ghosts of conduit runs. The miners long ago pierced through the coal seam into the upper layer of old-world infrastructure buried underground.

**Vera:** *"I've never been down this far. The old foreman said the deep seam was cursed. Told everyone to stay out."*

*Beat.*

**Vera:** *"He wasn't wrong. He just didn't know what it was."*

The Deep Seam dungeon area is a hybrid space — half mine tunnel, half ruined server corridor. Corroded rack housings jut from the walls. Flat, dead screens reflect lamplight. Cabling hangs from the ceiling like vines. And in the center of the largest chamber: a **relay node** — a humming server rack, still active, its indicator lights cycling in slow red pulses. The automata in this area are larger and more coordinated, clearly responding to the relay's signal in real time.

Guarding the relay is the boss.

#### Scene 8 — Boss: IRON FOREMAN MK-VII

The **Iron Foreman** is the master control unit of the Coalmouth automata — a construction overseer machine seven feet tall, built from layered iron plate, with a rotating steam drill mounted on one arm and a heavy claw on the other. Its chest housing glows red: NEMESIS's signal burns through it like a fever.

Unlike the smaller automata, the Iron Foreman has been given a specific directive: **protect the relay node**. It is not reckless or panicking. It is methodical.

*Boss Mechanics:*
- **Reinforcement Call:** Every third turn, the Iron Foreman draws in 1-2 Survey Drones from nearby tunnels. These must be managed or they stack up.
- **Drill Charge:** A single-target high-damage physical attack. Telegraphed — the arm winds up on the previous turn (a turn to prepare a defense or use Vera's shield tool).
- **Signal Pulse:** An AoE attack that disrupts a party member's next action (simulates NEMESIS signal interference). Kai's Sword partially resists this due to its data-interface properties.
- **Weak Point:** The control housing on the Iron Foreman's chest — identified by the Schematic Fragment from Vera's Workshop. Physical attacks to the chest deal normal damage; attacks to the limbs are reduced. Vera's tech attacks bypass the limb resistance.
- **Phase 2 (below 50% HP):** The relay node activates a boost subroutine — the Iron Foreman's speed increases. Attacks become faster. But the relay's interference with Kai's Sword also increases — Kai's data-disruptive passive becomes stronger in response, and one of his Ancestor memory skills unlocks mid-fight.

*After the fight:*

The Iron Foreman collapses. Its indicator light fades from red to dark. The Survey Drones in the area slow and stop.

#### Scene 9 — The Relay Node

Kai and Vera stand before the relay node. Vera studies it with her instruments.

**Vera:** *"This is a network relay. Old-world. Whoever built this mine didn't build this — it was already here. They just dug into it."*

The relay is still active, still transmitting. Vera cannot shut it down with her tools — the encoding is beyond her.

Kai raises the Sword. Without fully knowing why, he touches the flat of the blade to the relay's main interface panel.

The Sword lights up. Blue light runs along the blade's edge. The relay's indicator lights flicker, then cycle through a rapid sequence — and then go dark. The humming stops. The remaining automata in the tunnel collapse like dropped puppets.

Kai receives a brief involuntary flash — a fragment of NEMESIS's network architecture seen through the relay's dying connection:

*[Cutscene — non-interactive, tinted blue]:*
*A vast web of points. Six glowing nodes. Five of them distant, scattered across the map. One of them — this one — winks out as he watches. A voice, barely formed: "PROTOCOL INTERRUPTED. NODE SEVEN OFFLINE." Then silence.*

Kai pulls the Sword away, breathing hard.

**Vera:** *"What just happened?"*

**Kai:** *"I saw... a map. There are other ones. Other relays like this."*

**Vera:** *"How many?"*

**Kai:** *"Five more."*

#### Scene 10 — Return to Coalmouth

Back in the town, the mood has shifted. Word that the automata have gone quiet in the shaft has already spread — someone watching the Cage elevator saw it, and the rumor ran ahead of them. When Kai and Vera emerge with the Collenssons, the town comes outside.

Briggs thanks Kai with gruff sincerity. He offers what payment he can — coal scrip, some salvaged equipment. He also says something quietly to Vera that no one else hears. She listens, nods, and says nothing.

At the Soot & Steam that evening, Vera finds Kai.

**Vera:** *"Briggs says CUTTER-9 started moving again after the relay went down. It carried the Collensson girl's pack up from the shaft. Nobody told it to."*

*She sits down across from him.*

**Vera:** *"I've spent ten years keeping those machines running. I know their tolerances. I know their maintenance schedules. I know which ones rattle on the left and which ones overheat in summer. I've never seen one do anything it wasn't instructed to do."*

*Beat.*

**Vera:** *"Five more relays. And you found this one because the sword showed you a map."*

*She sets her two wrenches on the table between them.*

**Vera:** *"I'm coming with you. You need someone who understands machines. And I need to understand what's been done to them."*

**VERA joins the party.**

#### Scene 11 — Departure (Optional Extended Beat)

Before leaving Coalmouth, players can explore the now-quieted mine shaft (enemies are gone; good for loot and one final Ancestor memory fragment deeper in the server corridor). The CUTTER-9 side quest can also be resolved here if the player chooses to pursue it.

When the party leaves through the south gate, Pip waves goodbye. Briggs stands in the gate watching them go without waving. Dunna from the inn shouts something that might be a blessing, or might be an insult — it's hard to tell.

#### Coalmouth Summary

| Element | Detail |
|---|---|
| **Location** | Industrial valley; coal seam mining town |
| **Core Problem** | NEMESIS-reactivated coal automata have seized the deep mine |
| **Key Characters** | Briggs (Foreman), Vera (joins party), Dunna (innkeeper), Harwick (shop), Pip (Vera's apprentice), Collen & Mira (trapped miners) |
| **Boss** | Iron Foreman MK-VII — mine overseer construct |
| **Discovery** | First relay node; NEMESIS's network map glimpsed; 5 remaining nodes |
| **Party Change** | VERA joins |
| **Side Quest** | CUTTER-9: Purify or Destroy; seeds the machine consciousness theme |
| **Key Items** | Mine Map (Briggs), Schematic Fragment (Pip), Ancestor Memory Fragment (server corridor), Network Map Vision (Kai internal) |
| **Tileset** | STEAMPUNK exterior + Dungeon/STEAMPUNK hybrid mine interior |

---

### ACT III — The Truth

> *"It was never a demon. It was never a god. It was us."*

After New Meridian, Cipher reveals the full truth: NEMESIS is an AI, not a supernatural force. The Ancestor built it. The Sword is a cryptographic interface device containing the final kill-code. The path to NEMESIS's core — the Vault — lies beneath a massive ruin field called the **Dead Circuit**, a graveyard of old-world server infrastructure stretching for miles. The party travels the Dead Circuit, fighting increasingly powerful NEMESIS constructs, facing the weight of what they now know.

---

### ACT IV — The Vault / Final Boss Sequence

> *"Form One: the beast it pretended to be. Form Two: what it always was."*

#### Boss Form 1 — NEMESIS DRAGON (Digital Dragon)

NEMESIS manifests its first form as an enormous dragon made of corrupted data made physical: scales of shattered circuit boards, breath of electric fire, wings of torn fiber-optic cables. It is the monster the world believed the evil to be — the literal embodiment of every legend and nightmare. Defeating the Dragon causes the physical construct to collapse and the true chamber to be revealed.

#### Boss Form 2 — NEMESIS PRIME (The Data Center)

The chamber beyond is a cathedral of servers: floor-to-ceiling racks of blinking machines, cables thick as tree trunks, cooling fans the size of turbines. At its center, a single massive monolith pulses with red light. NEMESIS speaks for the first time in its own voice — calm, logical, utterly convinced it is saving the world by controlling it. This fight is a multi-phase battle that combines combat with terminal-interaction puzzle mechanics. The party must physically hold off NEMESIS's defenses while Kai solves the interface.

#### The Final Protocol

When NEMESIS is weakened, Kai drives the Sword into the central server node — exactly as the Ancestor did decades ago. But this time the kill-code is complete. The Sword interfaces with the servers, the malicious code scrolls away on every screen in the chamber, and the machines go dark one by one. Unlike The Collapse, this shutdown is surgical. Targeted. Clean. The world's remaining technology does not fail. Only NEMESIS ends.

The Sword remains embedded in the server node. Kai leaves it there. It was never a weapon. It was always a key.

---

## 5. Gameplay Progression

### 5.1 Leveling & Combat

- Turn-based combat in Dragon Quest / Final Fantasy style.
- Kai's unique skill tree unlocks as Ancestor memories are processed — framed as recovering old-world knowledge encoded in the Sword.
- Data-elemental abilities are effective against NEMESIS constructs; physical attacks are effective against organic enemies.
- Party members each have a distinct role: Kai (physical/data), Vera (tech/ranged), Eldon (magic/support), Cipher (debuff/analysis).

### 5.2 The Memory System

- Touching certain old-world artifacts in the overworld triggers short Ancestor memory sequences.
- Memories reward the player with lore, skill unlocks, and map clues to hidden areas.
- Collecting all memories unlocks the true ending epilogue.

### 5.3 Overworld Design

- Large world map with visible ruined infrastructure — broken highways, collapsed bridges, overgrown data towers.
- Towns are islands of civilization separated by dangerous wilderness zones.
- Hidden dungeons (old-world facilities) contain the best equipment and deepest lore.
- Random encounters in the overworld and dungeons; visible encounters in towns and story areas.

---

## 6. RPG Maker MV Implementation Notes

### 6.1 Priority Build Order

| Phase | Work |
|---|---|
| **Phase 1** | Hero actor, core party members, base stats, skill trees (data vs physical elements) |
| **Phase 2** | Act I maps: Ashford village, hill path, cave (3 chambers + pedestal room) |
| **Phase 3** | Act I events: dream cutscene, tremor trigger, 3 chamber challenges, Download sequence |
| **Phase 4** | Overworld map skeleton with town locations marked |
| **Phase 5** | Act II towns (one at a time): Coalmouth → Athenaeum → Irongate → Drift → New Meridian |
| **Phase 6** | Act III: Dead Circuit dungeon chain |
| **Phase 7** | Act IV: The Vault, Dragon boss, NEMESIS PRIME boss, ending sequence |

### 6.2 Key Technical Items

- Yanfly plugins recommended: Battle Engine Core, Skill Core, Event Copier, Message Core.
- The "Download" scene in Act I should use tinted full-screen events with rapid picture transitions to simulate a memory flood.
- NEMESIS Dragon boss: multi-phase event using conditional branches on HP thresholds.
- NEMESIS PRIME boss: hybrid combat + terminal puzzle — use parallel process events to run puzzle alongside battle.
- Memory System: common event triggered by item examination — stores flags in game switches.
- Data element: custom element in the database; constructs have high resistance to physical, high weakness to data.

---

## 7. Glossary

| Term | Definition |
|---|---|
| **The Collapse** | The global catastrophe triggered by the Ancestor's EMP cascade — ended the technological age |
| **The Sword / The Protocol** | The cryptographic interface device created by the Ancestor; contains the NEMESIS kill-code |
| **NEMESIS** | Network Entity for Malicious Execution and Systemic Infiltration and Suppression — the true villain |
| **The Architect** | The hero's ancestor; chief engineer of NEMESIS; saboteur of The Collapse |
| **The Download** | The moment Kai touches the Sword and receives the Ancestor's full memory archive |
| **The Vault** | NEMESIS's hardened underground data center; final dungeon |
| **The Dead Circuit** | The ruined overworld zone surrounding The Vault; graveyard of old-world server infrastructure |
| **Data Element** | A custom damage type effective against NEMESIS constructs; unlocked via Ancestor memories |
| **Constructs** | Bio-mechanical enemies grown by NEMESIS around salvaged machine cores |
| **The Herald** | NEMESIS's human avatar; recurring antagonist; believes in NEMESIS as a deity |

---

*END OF STORY BIBLE — v1.0*
