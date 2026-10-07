<p align="center">

# 🗺️ RME Alpha AI

[![Version](https://img.shields.io/badge/version-v1.0.3--alpha-blue?style=for-the-badge&logo=github)](ReleaseNotes.md)
[![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-yellow?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/PySide6-6.5+-orange?style=for-the-badge&logo=qt&logoColor=white)](https://doc.qt.io/qtforpython/)
[![Status](https://img.shields.io/badge/status-active_development-brightgreen?style=for-the-badge)](ReleaseNotes.md)
[![Client](https://img.shields.io/badge/client-15.33.b21348-6a5cff?style=for-the-badge)](ReleaseNotes.md)
[![Privacy](https://img.shields.io/badge/privacy-100%25_local-brightgreen?style=for-the-badge&logo=shield)](ReleaseNotes.md)

**An AI-powered map editor and assistant for OpenTibia.**
*The classic Remere's Map Editor workflow, rebuilt with semantic planning, visual validation and RME visual parity.*

</p>

<p align="center">
  <img width="800" height="400" alt="Rme01" src="https://github.com/user-attachments/assets/f301706d-a9fc-43c1-b30b-228c73e079d2" />
</p>

---

## 📑 Contents

- [🚀 What is RME Alpha AI?](#-what-is-rme-alpha-ai)
- [✨ Key features](#-key-features)
- [👾 Creatures, NPCs & spawns](#-creatures-npcs--spawns)
- [🧭 RME parity highlights](#-rme-parity-highlights)
- [🗺️ Supported client versions](#️-supported-client-versions)
- [🤖 The AI Planner](#-the-ai-planner)
- [🔄 Material Sync system](#-material-sync-system)
- [🔌 MCP servers](#-mcp-servers)
- [📡 Live](#-live)
- [🛡️ Privacy](#️-privacy)
- [🔥 House Creator → Extension](#-big-news-house-creator-becomes-an-extension)
- [🆕 What's new in v1.0.3-alpha](#-whats-new-in-v103-alpha)
- [🖥️ Requirements](#️-requirements)
- [⬇️ Download & verify](#️-download--verify)
- [🧭 Getting started](#-getting-started)
- [📊 Project status](#-project-status)
- [👤 Creator](#-creator)
- [📄 License](#-license)

---

## 🚀 What is RME Alpha AI?

An **early-stage** map editor for OpenTibia that **merges the power of RME with artificial intelligence**. Its goal is to evolve the classic mapping workflow by adding:

- 🤖 **AI assistant** to generate and validate structures.
- 🧠 **Semantic planner** that understands biomes, houses, spawns and quests.
- ✅ **Automatic validation** of maps (OTBM) and visual error detection.
- 🎨 **Smart brush system** with auto-bordering.

This *alpha* is built for testing, feedback and continuous improvement. Every update brings generated-map quality closer to that of an **expert human mapper**.

[![Watch video](https://ejemplo.com/miniatura.jpg)](https://www.image2url.com/r2/default/videos/1784798715343-bbcb278a-c6a2-4b6f-9879-5d6c9062000e.mp4)

<img width="1919" height="1019" alt="Screenshot_1" src="https://github.com/user-attachments/assets/aa529d8c-914b-4d83-b92a-213f65fdfc56" />

---

## ✨ Key features

| Icon | Feature |
|------|---------|
| 🧩 | **Semantic planning** of biomes, houses, spawns, NPCs and quests. |
| 🤖 | **AI Planner** with support for Ollama, OpenRouter and PaxSenix. |
| 🔍 | **OTBM validation** and automatic error correction. |
| 🖌️ | **Smart brushes** and material-based auto-bordering. |
| 📊 | **Knowledge base** (SQLite) for learning and recommendations. |
| 🎯 | **Multi-model consensus** for better decisions. |
| 🖥️ | **Modern, responsive GUI** built with PySide6 (Qt). |
| 👾 | **True creature rendering** — official looktype registry + your server's Lua, readable NPC labels, spawn icons. |
| 🔍 | **RME-style dialogs** — Jump, Search, Replace and Map Properties with the Remere layout. |
| 🏠 | **House gallery** by official name with live sprite previews and mini-viewport. |
| 💡 | **RME-parity lighting** with Light Control HUD (intensity, shadow, collision-aware occlusion). |
| 🎞️ | **Canary-faithful animations** with frame cache, preview toggle and speed control. |
| 🖱️ | **Creature context menu** — Select Npc/Monster plus Npc/Monster Properties dialogs. |
| ⚡ | **Frame-cached viewport** with progressive chunk rendering for large maps. |
| 🛡️ | **Privacy HUD** (`About › Privacidad`) with local-first guarantees. |
| 🔌 | **Local MCP bridge** (STDIO) with certified, validated operations only. |

---

## 👾 Creatures, NPCs & spawns

Monsters and NPCs render exactly where RME puts them — with outfits resolved from the bundled official registry (1834 monsters + 1080 NPCs), falling back to your server's `monster/` + `npc/` Lua directories from Preferences:

```diff
+ File sidecars (<map>-monster.xml / <map>-npc.xml) load with upstream RME discard rules
+ Indexed OTBM chunks propagate creatures AND spawns into every tile (no more black squares)
+ Unknown looks fall back to outfit 197 (the Carl-bot tribute, upstream BlitCreature parity)
+ NPC labels: OTClient-blue bold + HP bar + soft plate, anchored to the real sprite head
+ Spawn centers: custom 16 px semi-transparent icons on their own layer, always under the creature
+ Right-click: Select Npc / Select Monster + Npc/Monster Properties (name, spawn time, direction)
```

> [!TIP]
> Spawns stay visible without covering creatures, and per-kind toggles (`Show monsters / NPCs / monster spawns / NPC spawns`) work independently.

---

## 🧭 RME parity highlights

| Area | Parity delivered |
|:-----|:-----------------|
| 🔍 Dialogs | `Jump to Item` (`Ctrl+J`), `Search for Item` (`Ctrl+F`), `Replace Items` (`Ctrl+Shift+F`), `Map Properties` (`Ctrl+P`) — 4-column Remere layout, 32 px icons, real names |
| 🏠 Houses | Official names from `world-house.xml`, real sprite previews, floor −/+, 2D rotation, live mini-viewport |
| 🗺️ Minimap | Floor buttons that always respond |
| 💡 Light | Single scene-level pass from item flags; `View > Lights > Light Control…` (`Shift+Alt+L`): 0–100% light/shadow, wall occlusion via the client's own `unsight` flag |
| 🎞️ Animation | `appearances.proto` loop types, per-phase timing, sync + random-start clocks, static-base/animated-overlay fast path |
| 🖌️ Brushes | Ground/wall/door/carpet/table/doodad + flag tools with real flags; kind-checked creature erasers |
| 🧱 Viewport | Progressive chunks, LRU pixmap caches, deadline-ordered animation refresh |
| 🛡️ Safety | OTBM gate (magic, 512 MiB cap, rate limiting), guarded XML parsing everywhere |

---

## 🗺️ Supported client versions

Client packs are **fingerprinted by their `appearances-*.dat` hash** — the editor always resolves materials, brushes and IDs against the pack you actually loaded. Unknown packs report hash + counts instead of being guessed.

| Version | Status |
|---------|--------|
| **15.24 Targuna** | ✅ Base materials, fallback for every version |
| **15.30 (Summer 2026)** | ✅ Dedicated `data-15.30` tree + items overlay |
| **15.33 (CipSoft)** | ✅ Dedicated `data-15.33` tree + items overlay |
| **15.33.b21348 (live)** | ✅ Fingerprinted live build, full `data-15.33` inheritance |
| **Dudantas OTClient 13.20–15.25** | ✅ Hybrid filter (10 tags, no hashes invented) |

> [!NOTE]
> `Supported versions` lists every registered asset profile as `active` / `registered` / `missing`, plus `unidentified` rows for new packs. AI proposals carry the active-client context so models only cite IDs present in your pack.

---

## 🤖 The AI Planner

The **Planner** connects to different AI providers to assist with map generation and review:

- **Ollama** (local)
- **OpenRouter** (multi-model, cloud)
- **PaxSenix** (specialized service)

With **automatic selection** and **multi-model consensus** modes to:

- Review building proposals.
- Detect visual and density errors.
- Tune biomes and structures.
- Improve generation logic.

> ⚠️ **Important:** models **never write item IDs directly**. Every proposal goes through material catalogs, certified brush engines, OTBM validation and visual QA. This keeps generated maps compatible and playable.

The Planner is **100% hybrid**: it works against any `appearances-*.dat` (curated, dudantas or future), exposing only brushes visible in the active pack.

---

## 🔄 Material Sync system

The **Sync Materials** HUD updates the versioned trees from your active Tibia client folder:

- **Targets:** `items_xml` · `tilesets` (~100 files) · `brushs` (16 files) · `borders`
- **Read-only-first:** Scan reports `dead_refs` vs `new_ids` — nothing writes without a confirmed diff, every write keeps a `.bak` backup
- **Safety rules:** client folder is read-only, `resources/materials` (15.24 base) is untouchable, fluid OTB IDs 1–20 excluded
- **AI-assisted curation** (free models only, key in memory/env only) with valid/rejected accounting

---

## 🔌 MCP servers

Local STDIO bridge (`mcp_server.py`) proxied to the running Qt process over authenticated local IPC:

- **Semantic operations only** — models never get a raw tile/OTBM write primitive
- **Tools:** `rme_open_map` · `rme_planner_query` · `rme_create_proposal` · previews · block approval (`confirm=true` + `RME_MCP_ALLOW_APPROVAL=1`) · validated CLI batch specs
- **Multi-client safety:** proposals carry an owner — a second client can't touch another client's proposal (fail-closed)

---

## 📡 Live

Top-level `Live` menu (`Ctrl+Shift+L`) with a floating HUD: local session handshake, peers, cursor sharing and chat — packet types verbatim from RME's `live_packets.h`, honestly labeled while networking lands.

---

## 🛡️ Privacy

`About › 🔒 Privacidad` opens an animated floating HUD with our guarantees:

| Guarantee | Meaning |
|:----------|:--------|
| 🔒 100% local | Maps, preferences and knowledge live on your PC — no accounts, no user-data storage |
| 🚫 Zero third parties | No telemetry, no tracking, no analytics |
| 🤖 Memory-less AI | Models never store your maps, prompts or keys |
| 🔑 Keys stay safe | API keys only in memory / env vars / OS secret store — audited by `secret_guard.py` on every package |
| 📦 Clean distribution | Binaries only via GitHub Releases with SHA-256; the repo never receives builds (95 MiB gate) |

---

## 🔥 Big news: House Creator becomes an extension

> [!IMPORTANT]
> The in-product **House Creator is removed** in `v1.0.3-alpha` — not cut, **graduated**. Inside RME Alpha AI it was hitting its limits; as a dedicated **extension** it has far greater potential.

| 🏗️ Coming in the extension | ✨ |
|:---------------------------|:---|
| 📐 House blueprints | Design real **plans** first, then materialize |
| 🎨 Designs & decorations | Curated presets + smart decoration passes |
| 🏢 Sublevels | Basements, upper floors, split levels |
| 🏠 Roofs | Pitched, flat and Tibia-style roofs |
| 🌿 Patios & balconies | Terraces, railings and access |
| 🧩 More combos | Wider tile / ground / wall choice per style |

Your existing houses and maps are 100% safe. The extension will be announced here. 🔔

---

## 🆕 What's new in v1.0.3-alpha

- ⬛ **Black squares on NPCs/monsters fixed** — spawn tiles crashed rendering; every visible creature now composes (explicit marker if its outfit is missing).
- 🏷️ **Readable NPC names** — OTClient-blue bold + soft plate + HP bar.
- 👁️ **Spawn icons under creatures** — custom 16 px semi-transparent icons on their own layer.
- 🖱️ **Creature right-click** — `Select Npc` / `Select Monster` + `Npc/Monster Properties` (name, spawn time 1–3600, direction).
- 📦 **Client 15.33.b21348 support** — fingerprinted, `data-15.33` active.
- 🛡️ **Privacy HUD** — animated floating panel under `About`.
- 🗑️ **Removed:** legacy spawn rings (superseded by icons) · in-product House Creator (→ extension, above).

📜 Full history lives in [`ReleaseNotes.md`](ReleaseNotes.md) (rev. 1 → rev. 12).

<img width="1919" height="1024" alt="Screenshot_2" src="https://github.com/user-attachments/assets/acce6923-3ab9-4996-a912-299e23dd12b0" />

---

## 🖥️ Requirements

| Requirement | Details |
|-------------|---------|
| 🪟 OS | Windows 10/11, 64-bit |
| 🎮 Client assets | A Tibia client `/assets` folder with `appearances-*.dat` + `catalog-content.json` (asked for on first launch; **not bundled** for legal reasons) |
| 🎨 GPU | Recommended for the accelerated viewport (software fallback included) |
| 💾 RAM | 4 GB minimum, 8 GB recommended for large maps |
| 🐍 Source runs only | Python 3.10+ and `pip install PySide6`, then `python main.py` |

### AI providers (optional but recommended)

- **Ollama:** local AI processing, installed separately.
- **OpenRouter:** API key for cloud multi-model access.
- **PaxSenix:** API key for the specialized service.
- **Internet:** required for cloud providers only — the editor itself is fully offline.

---

## ⬇️ Download & verify

| File | Use |
|:-----|:----|
| `RME.Alpha.AI.zip` | 📦 User install for the GitHub Release |
| `RME.Alpha.AI.zip.sha256` | 🔐 Verification hash (`hash  filename` format) |

```powershell
Get-FileHash "RME.Alpha.AI.zip" -Algorithm SHA256
```

> [!WARNING]
> The unzipped product is ~400 MiB (EXE + `_internal/`). It ships as a local folder — **never** through Git.

---

## 🧭 Getting started

1. **Download the latest release.**
2. **Run** the portable executable (keep `RME_Alpha_AI.exe` next to `_internal/`).
3. **Point it at your assets folder** when asked.
4. **Explore** the editor and try the AI Planner.

> This version ships a User Manual — please read it before starting: `MANUAL_USUARIO.md`

<img width="1919" height="1022" alt="Screenshot_3" src="https://github.com/user-attachments/assets/4abe2a8c-b96f-4503-8709-76016f89cdbb" />

---

## 📊 Project status

| Status | Description |
|--------|-------------|
| 🧪 **Alpha** | Under active development, stable for testing. |
| 🔄 **Updates** | Regular, driven by feedback. |
| 🐛 **Bugs** | Expected — reports are welcome. |
| 🗺️ **Compatibility** | Progressing with RME/Canary and OpenTibia standards. |

> **This project is Open Source** and every contribution is welcome.

---

## 👤 Creator

**Developed by [@ricker72](https://github.com/ricker72)**
Passionate about OpenTibia, AI and creative tooling.

<p align="center">
  <a href="https://github.com/ricker72">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  <a href="https://ricker72.github.io">
    <img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=About.me&logoColor=white" />
  </a>
</p>

---

## 📄 License

This project is under the **MIT** license.
See [LICENSE](LICENSE) for details.

---

<div align="center">

**Thank you for your interest! 💚**
Your support and feedback are key to making RME Alpha AI the definitive map-creation tool for OpenTibia. 🗺️✨

</div>
