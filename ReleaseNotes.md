# 🏰 RME Alpha AI — `v1.0.4-alpha`

<div align="center">

![version](https://img.shields.io/badge/version-v1.0.4--alpha-blue?style=for-the-badge&logo=github)
![platform](https://img.shields.io/badge/platform-Windows-0078D4?style=for-the-badge&logo=windows)
![status](https://img.shields.io/badge/status-prerelease-orange?style=for-the-badge)
![client](https://img.shields.io/badge/client-15.33.b21348-6a5cff?style=for-the-badge)
![privacy](https://img.shields.io/badge/privacy-100%25_local-brightgreen?style=for-the-badge&logo=shield)
![lua](https://img.shields.io/badge/lua-subcore-2C2D72?style=for-the-badge&logo=lua)

**The OpenTibia map editor with AI · visual parity with Remere's Map Editor — now scriptable in Lua** ✨🌙

[⬇️ Download](#️-download--verify) · [✨ Highlights](#-highlights) · [🌙 Lua](#-lua-subcore--lua-studio) · [🛠️ Full changelog](#-whats-new)

</div>

---

## 📑 Contents

- [✨ Highlights](#-highlights)
- [🌙 Lua subcore + Lua Studio](#-lua-subcore--lua-studio)
- [🧱 RAW, borders & palettes](#-raw-borders--palettes)
- [🖱️ Right-click menu & Properties](#️-right-click-menu--properties)
- [📥📤 Import & Export](#-import--export)
- [🧹 Map cleanup tools](#-map-cleanup-tools)
- [🔍 Reload & Find Monster](#-reload--find-monster)
- [🪟 New Palette & SQLite Inspector](#-new-palette--sqlite-inspector)
- [⚡ Fluid panning](#-fluid-panning)
- [🏠 True RME zone tints](#-true-rme-zone-tints)
- [⬇️ Download & verify](#️-download--verify)
- [🛠️ Technical notes](#️-technical-notes)

> [!NOTE]
> **Product:** RME Alpha AI (`RME_Alpha_AI.exe`) · **Version:** 1.0.4 Alpha (`v1.0.4-alpha`) · **Date:** 2026-10-07
> This notes file covers **only** the changes shipped in `v1.0.4-alpha`. Full history lives in the repo `ReleaseNotes.md` (rev. 1 → rev. 13).

---

## ✨ Highlights

| Area | What shipped |
|:-----|:-------------|
| 🌙 Lua scripting | Real sandboxed Lua runtime (lupa) with full editor knowledge + floating Lua Studio |
| 🖱️ Creature menu | `Select Npc/Monster`, `Npc/Monster Properties`, `Rotate item`, `Open/Close door`, `Select House` |
| 📥📤 Import/Export | Import Monsters/NPCs · Export Minimap (PNG/BMP) · Export Tilesets (XML) |
| 🧹 Cleanup | Map Cleanup, Corpses, Unreachable tiles, Invalid Houses, Modified State — all undoable |
| 🔍 Search | Reload Data Files (`F5`), Find Monster by name with jump-to-result |
| 🪟 Windows | Second floating Palette, read-only SQLite Materials Inspector |
| ⚡ Performance | Background chunk extraction — panning no longer freezes the UI |
| 🏠 Rendering | House/PZ tints as true per-pixel Multiply (RME exact), texture preserved |

---

## 🌙 Lua subcore + Lua Studio

<div align="center">

![lua-new](https://img.shields.io/badge/🌙_Lua-Studio-2C2D72?style=for-the-badge)
![sandbox](https://img.shields.io/badge/sandboxed-no_os_no_io-success?style=flat-square)

</div>

The biggest feature of this release: a **Lua subcore with complete editor knowledge** — brushes, materials, palettes, viewport, map edits and script creation — driven by a real Lua runtime, not a subset.

```lua
-- Hello Map: reads are live, writes apply atomically on success
local tile = app.getTile(100, 100, 7)
app.log("ground here: " .. tostring(tile:ground()))
tile:addItem(1987)
app.centerOn(100, 100, 7)
```

### 🧠 What scripts can touch

| Namespace | Powers |
|:----------|:-------|
| `app` | live `map`, `getBrush`/`setBrush` by catalog name, `centerOn`, `version`, `log` |
| `Map` | `name/width/height/tileCount`, `getTile(x,y,z)`, `for tile in map:tiles()` |
| `Tile` | `pos/ground/items/creature` reads + recorded `addItem/removeItem/setGround` |
| `Brushes` | `get(name)/getNames()` over the real material catalog |
| `Selection` / `Position` | read and replace the editor selection |

> [!IMPORTANT]
> Writes never apply inline: they commit through **one atomic undoable transaction** after a successful run. A failing script changes **nothing**; out-of-bounds ops are skipped and reported.

### 🔒 Sandbox (RME `setupSandbox` parity)

`os` · `io` · `package` · `debug` · `require` · `dofile` are stripped. No filesystem, no network, no cross-run state — every execution gets a **fresh isolated runtime** and `print()` is captured to the console.

### 💜 Lua Studio floating HUD

`Lua` menu (before `About`) → **Lua Studio** (`Ctrl+Shift+U`): script list with ✅/🚫 enable flags, New/Save/Delete/Reload/Folder, ▶ Run, output console, dark theme — plus an assistance layer:

| ✨ Assistance | Behavior |
|:--------------|:---------|
| 🧹 Clear | One-click editor wipe (file untouched until Save) |
| ⌨️ Autocomplete | 61 real names — subcore API + Lua keywords (only what actually runs; server-side TFS globals are *not* suggested because they would error) |
| ⚠️ Live lint | Unbalanced brackets, orphaned `end`/`until`, unterminated strings — debounced, honestly labeled as basic |
| ✨ Format on save | Conservative indent normalizer (leading whitespace only — content never touched) |
| 🌈 Rainbow brackets | Depth-colored pairs with block-state tracking; brackets inside strings stay string-colored |
| 🔦 Pair flash | Matching bracket highlight under the cursor |
| ƒx Navigator | Jump-to-function combo (`name :line`) |

> [!NOTE]
> VS Code extensions (EmmyLua, sumneko, TFS API packs…) can't install into a Qt app — so their *capabilities* were rebuilt natively inside Lua Studio, scoped to what the sandbox truly executes.

---

## 🧱 RAW, borders & palettes

```diff
+ Shallow-water borders 4621–4632 listed in Borders tilesets (15.30 + 15.33)
+ Universal RAW: any active-pack ID resolves, even outside every tileset
+ RAW palette opens as an "id – name" list, like Remere's BrushListBox
```

- Border pieces carry their real edges (`n=4621, e=4624, s=4623, w=4622`, corners `4629–4632`, diagonals `4625–4628`) and animate (14 frames verified advancing).
- Palette audit: Terrain (11 tilesets) · Doodad (27) · Item (50) · RAW (43) — every click arms a paintable brush through the same path.

---

## 🖱️ Right-click menu & Properties

Parity with RME's `MapPopupMenu::Update`, verified item by item:

| Menu entry | Behavior |
|:-----------|:---------|
| `Rotate item` | Swaps to the `rotateto` target from versioned `items.xml` (e.g. 2025 → 2059) |
| `Open/Close door` | Toggles the same wall/type pair (e.g. 6251 ↔ 6253), persisted atomically |
| `Select House` | Arms the house tool with the tile's `house_id` |
| `Select Npc/Monster` | Arms the entity brush · `Properties` opens the matching dialog |
| `Select RAW/Wallbrush/Doorbrush/Groundbrush` | Gating verified against real ids (1295, 6251…) |

**Properties dialog** rebuilt: compact tabbed UI (Tile / Item / JSON, 520×600 — no more hiding under the taskbar) with the new **Door ID** field (0–255, house tiles only, RME parity). Also fixed: the dialog crashed on *every* item because the certified catalog lacks `writeable` flags — text capabilities now resolve from versioned `items.xml`, so signs edit description and parchments edit text with their real limits.

---

## 📥📤 Import & Export

| Entry | Behavior |
|:------|:---------|
| `File › Import › Import Monsters/NPCs` | Merges creature **type definitions** from picked `*.xml/*.lua` into session (looks + palettes, RME `importXMLFromOT` overwrite parity). Map tiles and spawns untouched; invalid files reported, never applied |
| `File › Export › Export Minimap` | Folder + name + PNG/BMP + area (All/Ground/Specific/Selected). 1 px per tile with viewport minimap colors; empty floors skipped |
| `File › Export › Export Tilesets` | Round-trips `tilesets/*.xml` schema (107 tilesets, ~40k ids, ranges collapsed) with success confirmation |

> [!NOTE]
> OTMM lists as **disabled with reason**: its blocks need ground speed + walk flags no certified feed provides — disabled beats a corrupting placeholder.

---

## 🧹 Map cleanup tools

All with confirm dialogs and undo support, RME semantics verified line-by-line:

- **Map Cleanup** — drops items whose id is absent from the active pack (fail-closed without one); ground/houses/spawns untouched.
- **Remove all corpses** — matches the *Corpses materials tileset* (not a flag) and skips complex items (action/text/…), RME `isComplex` parity.
- **Remove all unreachable tiles** — RME's local 21×17 box test (no invented flood-fill): a tile survives if any walkable tile exists nearby, otherwise the whole tile is erased.
- **Clear Invalid Houses** — deletes houses whose town is gone, unassigns orphan tiles; tiles/items never removed.
- **Clear Modified State** — drops the 16×16 changed marks (same effect as reopening), undo history untouched.

---

## 🔍 Reload & Find Monster

- **Reload Data Files** (`F5`, File menu): rebuilds materials, refreshes both creature catalogs, purges render caches and repaints — RME `RELOAD_DATA` parity.
- **Find Monster** (Edit menu): live-filtered name search over loaded monster types (empty catalog → honest notice), case-insensitive whole-map scan, documented 2000-result UI guard, results selected with jump-to-first — mirroring RME's search dialog + result window flow.

---

## 🪟 New Palette & SQLite Inspector

- **Window › New Palette**: a second independent floating palette dock (Terrain left, RAW list right, anyone?).
- **Window › SQLite Materials Inspector**: read-only dialog over the real `materials.db` (schema v6, identical tables to RME): Summary (counts, brush types, dangling-link audit), Brushes by type with full details, Tilesets with sections/entries, plus Reload.

---

## ⚡ Fluid panning

Panning used to freeze the GUI for **1–7 s per new 64×64 chunk** (measured: 253,052 index areas scanned in Python per request + ~200k nodes parsed at ~25 µs each on the 16 ms pan tick, with prefetch compounding it).

```diff
+ Block-grid area index: 253k scan → ~3.8k candidates, byte-identical results
+ Background chunk extraction: private mmap reader, zero shared state
+ Pan paints cached tiles instantly; arrivals adopt + render progressively
+ Prefetch rerouted off the tick · light overlay quantized to an 8-grid
```

> [!TIP]
> First visit to a dense region still parses in the background — tiles pop in progressively instead of freezing input. Pan back over visited ground: instant.

---

## 🏠 True RME zone tints

The old translucent wash flattened textures into solid squares that read as paint crossing walls. Now the zone color **multiplies the ground/border texture per pixel** — exactly what RME's `BlitItem(r,g,b)` does:

- Texture detail survives (darkened, not flattened) · tint cannot exist where the sprite has no pixels · walls, creatures and neighbors provably untouched (0 changed pixels outside the cell across 12 sampled edge tiles).

---

## ✅ Verification

- New coverage: **40 tests across 8 files** (cleanup 9 · find 3 · window tools 4 · lua subcore 10 · pan fluidity 3 · raw/door/rotate 4 · tint multiply 2 · import/export 5) — all green.
- Related suites (render, gestures, assets, palettes): green. `scripts/secret_guard.py`: **PASS** on every build.

---

## ⬇️ Download & verify

| File | Use |
|:-----|:----|
| `RME.Alpha.AI.zip` | 📦 User install for this Release (~115 MB zipped) |
| `RME.Alpha.AI.zip.sha256` | 🔐 Verification hash (`hash  filename` format) |

**SHA-256:**

```text
2152b9225fda8dcbbe13590e71b230a63dab735b38051beace05b1cca8cf6628  RME.Alpha.AI.zip
```

Verify your download in PowerShell:

```powershell
Get-FileHash "RME.Alpha.AI.zip" -Algorithm SHA256
```

> [!WARNING]
> The unzipped product is ~400 MiB (EXE + `_internal/`). It ships as a local folder — **never** through Git. The canonical 95 MiB repository gate stays in force.

<details>
<summary>🛠️ Technical notes</summary>

- Spawn markers ride a dedicated `SpawnIndicator` layer ordered before `Creature`; zone tints bake into cached sprite copies (LRU 512).
- Lua writes land via snapshot → replace → commit (`Lua script` transaction); `RME_LUA_SCRIPTS` overrides the scripts folder; frozen builds ship the lupa backends (`lua51…luajit21` collected explicitly — dynamic backend selection is invisible to PyInstaller).
- OTMM export stays disabled pending a certified ground-speed feed; `Generate Map`, `Edit Items/Monsters` stay disabled in RME parity (dead upstream too).

</details>

---

<div align="center">

**💚 Map tranquilo — nosotros cuidamos el resto. 🗺️✨**

![made](https://img.shields.io/badge/made_with-💚_y_café-brown?style=flat-square)

</div>
