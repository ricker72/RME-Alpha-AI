# 🏰 RME Alpha AI — Release Notes

<div align="center">

![version](https://img.shields.io/badge/version-v1.0.2--alpha-blue?style=for-the-badge)
![platform](https://img.shields.io/badge/platform-Windows-0078D4?style=for-the-badge)
![status](https://img.shields.io/badge/status-prerelease-orange?style=for-the-badge)

**El editor de mapas OpenTibia con IA · paridad visual con Remere's Map Editor** ✨

</div>

## 📑 Contenido

- [Novedades destacadas](#novedades-destacadas)
- [Descargas y verificación](#descargas-y-verificación)
- [Publication version policy](#publication-version-policy)

**Product:** RME Alpha AI (`RME_Alpha_AI.exe`)
**Version:** 1.0.2 Alpha (`v1.0.2-alpha`)
**Date:** 2026-10-04 (rev. 11 — RME parity: Jump/Search/Replace y Map Properties estilo Remere; galeria de casas por nombre oficial con preview real y mini-viewport; minimap floor fix)
**Build source:** clean `python build_release.py` → `dist_current/RME_Alpha_AI/`
**User install path:** `RME Alpha AI/RME_Alpha_AI.exe`

## ✨ Novedades destacadas

| Área | Qué trae |
|:-----|:---------|
| 🔍 Diálogos RME | `Jump to Item`, `Search for Item`, `Replace Items` y `Map Properties` con el diseño de Remere |
| 🏠 Casas | Nombres oficiales, preview real con sprites y mini-viewport vivo |
| 🗺️ Minimapa | Botones de piso que siempre responden |
| 🎨 Tema | Spins sin textos tapados |

```diff
+ Layout de 4 columnas como RME (criterios · Types · Properties · Result)
+ Iconos de 32px, nombres reales y filtros por tipo/propiedad observados
+ Galería por nombre oficial (world-house.xml) + rotación, paneo y mini-viewport
! Los previews reales requieren los assets del cliente (Locate Tibia Client)
```

> [!TIP]
> Atajos: `Ctrl+J` Jump · `Ctrl+F` Search · `Ctrl+Shift+F` Replace · `Ctrl+P` Map Properties.

## ⬇️ Descargas y verificación

| Archivo | Uso |
|:--------|:----|
| `RME.Alpha.AI.zip` | 📦 Instalación de usuario para el Release |
| `RME.Alpha.AI.zip.sha256` | 🔐 Hash de verificación (formato `hash  nombre`) |

Verifica la descarga en PowerShell:

```powershell
Get-FileHash "RME.Alpha.AI.zip" -Algorithm SHA256
```

✅ Build limpio: sin `build*`/`dist*` previos ni `__pycache__`; `scripts/secret_guard.py --path .` reporta `PASS`.

> [!WARNING]
> El producto descomprimido pesa ~398 MiB. Se distribuye como carpeta local (EXE + `_internal/`), **no** por Git: el gate canónico de 95 MiB para repositorios sigue vigente.

## Publication version policy

> [!NOTE]
> Every user-facing build must use the next recommended GitHub Release tag
> printed by `python build_release.py` and stored in
> `RELEASE_VERSION_RECOMMENDATION.txt`. The enforced sequence is:

```text
v1.0.0-alpha.1 → v1.0.0-alpha.2 → v1.0.1-alpha → v1.0.2-alpha → …
```

> [!NOTE]
> Single-step workflow (no double work): `python scripts/bump_version.py
> <tag> --rev <N> --summary "..."` syncs `workspace_core/updater.py`
> `CURRENT_RELEASE` and stamps this header; write the rev section body, then
> `python build_release.py --deploy-user` compiles and refreshes the clean
> user install in the same run. Every user build updates these notes with
> its fixes. For later builds, set `RME_CURRENT_RELEASE_VERSION` to the last
> published tag; the build then prints the next valid tag. Do not invent a
> release tag manually. Regla de releases de usuario: cada build con
> `--deploy-user` deja `RME.Alpha.AI.zip` + `RME.Alpha.AI.zip.sha256` en el
> Escritorio (comprimido de la instalación "RME Alpha AI") para subirlos
> como assets al GitHub Release.

---

## 0. Rev. 11 — cambios incluidos en esta versión

- 🔍 **Paridad RME en diálogos (Edit/Map):** `Jump to Item` (`Ctrl+J`),
  `Search for Item` (`Ctrl+F`) y `Replace Items` (`Ctrl+Shift+F`) con el
  layout de 4 columnas de Remere (criterios · Types · Properties · Result);
  tipos y propiedades filtrados con atributos observados de
  `resources/data-15.33/items.xml`, iconos de 32px y nombres reales;
  Replace con cajas picker, pares Add/Remove y Execute sobre el mapa
  completo o la selección. `Map Properties` (`Ctrl+P`) con el diseño RME
  (descripción, versión, dimensiones, 4 archivos externos, fail-closed).
- 🏠 **Galería de casas:** lista por nombre oficial de `world-house.xml`,
  preview con sprites reales del viewport (con diagnóstico cuando faltan
  sprites: ubicar cliente), botones −/+ de piso, rotación 2D +
  pad direccional, mini-viewport vivo sobre la escena real y Destino X/Y/Z
  en filas completas alineadas.
- 🗺️ **Minimap:** los botones ▲▼ de Floor actualizan el piso dibujado aunque
  el viewport no devuelva la llamada (sin mapa cargado).
- 🎨 **Tema:** reglas `QSpinBox::up/down-button` para que los valores no
  queden tapados por las flechas.

<details>
<summary>🛠️ Notas técnicas</summary>

- Los filtros de Types/Properties usan solo claves observadas en el
  `items.xml` empaquetado; lo sin fuente se muestra deshabilitado y nunca
  coincide (fail-closed).
- El `MapPropertiesDialog` solo persiste lo que el motor expone vía setters;
  lo cambiado sin setter avisa y no cierra.
- El spec empaqueta `ReleaseNotes.md` y el deploy lo extrae desde
  `_internal/` a la instalación; cada `--deploy-user` regenera
  `RME.Alpha.AI.zip` + `.sha256` en el Escritorio.

</details>

---

## 0. Rev. 10 — cambios incluidos en esta versión

- **Planner e IAs 100% híbridos (cualquier appearances-*.dat):** el
  planner, AI Studio y el materializador semántico ya no resuelven contra
  el catálogo completo sin filtrar. `BrushDatabase.version_brush_definitions()`
  expone solo los brushes visibles en el pack activo y los dos caminos de
  resolución (`compile_selected_semantic_plan` y `_apply_blueprint_dict`
  en `workspace_core/services.py`) usan esa vista. Cualquier versión —
  curada, dudantas o futura — trabaja con sus materiales
  correspondientes, leídos de su propio `appearances-*.dat`. Sin pack
  configurado se mantiene el best-effort completo.
- **Inventario por versión con dueño:** `version_brush_inventory()` filtra
  contra el pack dueño de cada versión (activo o perfil registrado con ese
  hint) y cachea por fingerprint del `.dat`. Las versiones curadas sin pack
  dueño reportan su contenido pineado como antes; las desconocidas con pack
  reportan `Hybrid pack (<tag>): V/T brushes visibles`. El contexto de IA
  (`ai_version_context`) arrastra el `hybrid_hint` para packs no
  fingerprintados.
- **Decoder hibrido:** `inventory_client_assets()` resuelve el `catalog-content.json`
  anidado (`assets/`/`cache/`) y reporta `asset_dir`; nuevo
  `decode_client_pack()` en `workspace_core/ai_decoder.py`: decodifica
  cualquier `appearances-*.dat` de una carpeta cliente completa con su
  inventario y hint dudantas (fail-closed `BLOCKED` si hay cero o varios
  `.dat`). `decode_appearances` ya era agnóstico a la versión (protobuf
  directo).
- **Nuevo catálogo de versiones:** la secuencia pasa a
  `v1.0.0-alpha.2 → v1.0.1-alpha → v1.0.2-alpha → …`
  (`scripts/release_version.py`, `workspace_core/updater.py` aceptan
  `-alpha`/`-beta` con o sin build). Flujo en un paso, sin doble trabajo:
  `python scripts/bump_version.py <tag> --rev <N> --summary "..."`
  sincroniza `CURRENT_RELEASE` y sella la cabecera de estas notas;
  `python build_release.py --deploy-user` (o `RME_DEPLOY_USER=1`) compila
  y refresca la instalación limpia de usuarios en la misma corrida.
- **Esta build es `v1.0.1-alpha`** (updater sincronizado a ese tag).
- **Validación:** nuevos `test_hybrid_planner_decoder.py` (7) y
  `test_version_catalog.py` (4); re-ejecutados inventario AI, versiones,
  híbrido, decoder, materiales y planes: todo en verde.

---

## 0. Rev. 9 — cambios incluidos en esta versión

- **Soporte híbrido de cliente (nuevo):** ya no hace falta apuntar a una
  carpeta `assets/` exacta. Acepta la **carpeta completa del cliente**
  (`client.exe` + `cache/` o `assets/`, p. ej. OTClient dudantas con `cache/`
  en solo-lectura): el payload se resuelve dentro de `assets/` o `cache/`
  (`workspace_core/client_assets.py`, `workspace_core/startup.py`).
- **Paletas y brushes filtrados por el cliente real:** con el filtro híbrido
  permisivo, un brush solo se muestra si **al menos uno de sus IDs existe**
  en el `appearances-*.dat` activo; los tilesets que quedan vacíos se
  ocultan. Sin assets configurados, todo visible (best-effort). No se
  inventa ni se agrega ningún ID (`workspace_core/hybrid_assets.py`,
  `workspace_core/editor/brush_database.py`,
  `workspace_core/editor/tileset_manager.py`).
- **10 versiones dudantas soportadas vía híbrido (13.20–15.25):**
  `15.25.0a00a0`, `15.13.02dfc3`, `15.11.c9d1cf`, `15.00.249ccc`,
  `14.12.95abf3`, `14.05.70ce66`, `13.40.93b0a1`, `13.32.14520`,
  `13.21.13839`, `13.20.13560`
  (https://github.com/dudantas/tibia-client/releases). Solo mapeo
  tag→fallback (base 15.24 + filtro): **sin hashes ni items inventados**;
  la versión autoritativa sigue siendo el fingerprint del `.dat` propio.
  La tabla `Supported versions` añade el estado `Híbrido (dudantas)` y el
  badge muestra `tag (hybrid)` cuando la carpeta lo sugiere
  (`workspace_core/asset_versions.py`, `panels/version_widgets.py`,
  `panels/asset_profiles_dialog.py`, `i18n.py: version_state_hybrid`).
- **La IA ya construye casas completas:** capa `houses` en
  `apply_semantic_plan` (`workspace_core/adapter.py`): la IA manda
  `layers: ["houses"]` + `house: {name, rent?}` y el core genera el ID
  (los IDs mandados por la IA se rechazan: `DIRECT-HOUSE-ID`), valida
  solape (`HOUSE-OVERLAP`), un solo piso, nombre y entrada transitable,
  pinta `house_id`, crea el registro y audita con rollback total ante
  cualquier fallo. Camino: `_apply_blueprint_dict`
  (`workspace_core/services.py`). Tests: 10/10 en
  `test_semantic_materializer_boundary.py`.
- **Respawns en áreas (core decide):** `Selection → Semantic area selector
  → Enable area selector (spawns…)`; arrastrar marca el área morada,
  clic derecho abre el HUD (`Área semántica · spawns`) con nivel, perfil
  (`easy/balanced/hard/raid`), **Analizar**, **Generar preview** y
  **Aplicar transacción**. El core elige los monstruos del catálogo
  oficial (`suggest_monster_spawns`) y solo aplica tras validación de
  accesibilidad. **Fix:** el selector ya no exige Shift+arrastrar (antes,
  sin aviso, pintaba en vez de seleccionar) y el menú se renombró de
  `Enable light-purple selector` (`viewport/map_view.py`,
  `mainwindow.py`).
- **Ruta manual de casas sin cambios:** `House Palette → Add` (registro) →
  seleccionar → pincel `House tiles` → pintar → pincel `Select Exit`.
  Sin casa seleccionada el pincel falla cerrado (`Select a house first`).
- **Updater:** `CURRENT_RELEASE` salta a `v1.0.0-alpha.2`
  (`workspace_core/updater.py`); el instalador compara contra ese tag.
- **Validación:** `test_hybrid_assets.py` 9/9 nuevo; re-ejecutadas
  versiones/materiales/guardia/perfiles (30), live-profile/decoder/nuevos
  items/AI (20), brushes parity/jump (10) y selector/spawns/gestos (12):
  todo en verde. `secret_guard.py`: PASS.

---

## 0. Rev. 8 — cambios incluidos en esta versión

- **Menú File:** eliminado `Open Workspace Project...`; el flujo de usuario
  queda centrado en `New`, `Open Map`, `Save`, `Import` y `Export`.
- **Import/Export:** `Import Map` usa el importador OTBM certificado; `Export
  OTBM` conserva metadata y valida la salida; `Export Lua` usa el exportador
  certificado y reporta errores sin crear archivos parciales.
- **Herramientas tipo Remere:** PZ, No-PVP, No-Logout y PvP escriben sus flags
  reales y el borrador elimina solo el flag de la herramienta activa.
  Casas, spawns, NPCs, monstruos y objetos existentes se preservan.
- **View/Layers:** las casillas de `View` se sincronizan con el panel Layers,
  incluyendo `Show special`; los toggles de monstruos, NPCs, spawns, casas,
  pathing, luces, grid, tooltips, indicadores y pisos fantasma fuerzan la
  actualización correcta del viewport.
- **Spawns y NPCs:** anillos de spawn más grandes y diferenciados por color,
  looktypes cargados desde los sidecars reales `-monster.xml`/`-npc.xml` y
  burbujas/etiquetas de NPC cuando el registro contiene texto o nombre.
- **Animaciones:** cambiar la velocidad ya no destruye el registro de frames;
  la cola de deadlines se reprograme de forma segura. Cambiar de piso limpia
  estados obsoletos y permite que todas las animaciones visibles se registren
  nuevamente.
- **Render y casas:** el tintado de house/PZ queda limitado a los píxeles del
  ground/border y no invade las esquinas transparentes de paredes altas.
- **Viewport y entrada:** render progresivo, cachés LRU y agenda de frames para
  reducir lag al abrir/navegar mapas; limpieza de Ctrl/Shift, mouse y previews
  al perder foco o cerrar la vista para evitar herramientas activas o estados
  pegados en laptops.
- **Validación:** se ejecutaron pruebas de interacción, IO, OTBM, render,
  spawns, herramientas y paridad; la última batería relacionada pasó 47/47.

`Only show colors` continúa deshabilitado intencionalmente: Remere documentó
que esa opción rompía el editor en versiones anteriores.

---

## 1. New client-version support: 15.30 and 15.33

- Added full support for **15.30 (Summer 2026)** and **15.33 (latest CipSoft)**,
  alongside the existing **15.24 Targuna** base.
- Client packs are identified by fingerprint, not by filename:
  `resources/asset_versions.json` maps each `appearances-*.dat` SHA-256 to
  `15.24.95dcf3`, `15.30`, or `15.33.6ef2e8`
  (`workspace_core/asset_versions.py`).
- Unknown packs are reported as `unidentified` with hash + content counts
  instead of being guessed.
- Per-version material resolution:
  `material_root_for_version()` selects `resources/data-<tag>/` when it is a
  complete tree, otherwise it falls back to the 15.24 base so brush coverage
  is never lost.
- Per-version item names/roles overlay:
  `items_xml_for_version()` prefers `data-<tag>/items.xml`, then the vendored
  Canary file `data-<tag>/items/items.xml`.
- The `Supported versions` table reports each registered asset profile as
  `active` / `registered` / `missing`, plus `unidentified` rows for new packs.
- AI Studio proposals are prefixed with the active-client context
  (`[Active client: <label> — N objects, M outfits. Use only item ids
  present in this pack.]`).

## 2. Material Synchronization System

The new **Sync Materials** HUD (`panels/material_sync_hud.py`,
`workspace_core/material_sync/`) updates the versioned trees from the active
Tibia client folder for **15.30** and **15.33**.

- Four sync targets (`TARGETS`):
  - `items_xml` — item names and roles from appearances.
  - `tilesets` — ~100 palette files under `tilesets/`.
  - `brushs` — 16 brush files under `brushs/`.
  - `borders` — editorial border groups under `borders/`.
- Read-only-first workflow:
  - **Scan** compares appearances against the expanded `<include/>` graph of
    `resources/data-<tag>/` and reports `dead_refs` (IDs cited by XML but
    missing from the pack) versus `new_ids` (pack IDs with no XML coverage).
  - Nothing is written without a confirmed diff. Every write creates a `.bak`
    backup and supports restore via `workspace_core/material_sync/writer.py`.
- Safety rules (non-negotiable):
  - Read-only over the client folder; writes stay inside `data-<tag>/`.
  - `resources/materials` (15.24 base) is untouchable.
  - Fluid-type OTB IDs 1–20 are excluded from "dead" reports
    (`NON_APPEARANCE_IDS`).
- AI-assisted curation (Zen, free models only):
  - API key lives only in memory or `OPENCODE_ZEN_API_KEY`.
  - Propose names for `items_xml` and placements/groups for
    `tilesets` / `brushs` / `borders`, with valid/rejected accounting.
  - Copy/paste plan support and a `Reload` action that refreshes materials
    after a confirmed write (restart note shown in the diff view).
- Default target tag is `15.30` (`DEFAULT_VERSION_TAG`); 15.33 uses the same
  pipeline against `resources/data-15.33/`.

## 3. Integrated `items.xml` for each version (find them in the palette)

Both version trees ship as complete Canary-layout material trees:

- `resources/data-15.30/`: `items.xml` (24,724 `<item>` entries),
  `materials.xml`, `brushs.xml`, `tilesets.xml`, `borders.xml`,
  plus `items/`, `tilesets/`, `brushs/`, `borders/` subtrees.
- `resources/data-15.33/`: `items.xml` (24,726 `<item>` entries) with the same
  layout.

What you will see in the **Item Palette**:

- `raw:new-items` (`tilesets/new_items.xml`):
  - 15.30: 1,415 new IDs (`52977`–`54755`), 166 of them named.
  - 15.33: 2 new IDs (`55095`, `55117`), preview + ID only (unnamed in
    appearances).
- 15.30 curated categories under `items`:
  - `New - Helmets` (`items:new-helmets`, 5 IDs, e.g. 53229, 53233).
  - `New - Amulets` (`items:new-amulets`, 15 IDs, e.g. 54510, 53197).
  - `New - Weapons` (`items:new-weapons`, 23 IDs, e.g. 53211, 53855).
  - `New - Soul Cores` (`items:new-soul-cores`, 21 IDs, e.g. 54587, 54632).
  - `New - Creature Products` (`items:new-creature-products`, 16 IDs,
    e.g. 53778, 54355).
  - `New - Other Items` (`items:new-other-items`, 41 IDs, e.g. 53692, 54651).
- Every palette New-Item ID resolves to real sprites in its own pack
  (`test_new_items_have_sprites`); no black tiles.

## 4. MCP Servers (Model Context Protocol)

Local STDIO MCP bridge (`mcp_server.py`, `workspace_ipc.py`):

- Exposes **semantic operations only**. Models never get a direct
  tile/OTBM write primitive; the certified Workspace/Planner path resolves
  assets and validates.
- Tools:
  - `rme_open_map`, `rme_planner_query`, `rme_create_proposal`,
    `rme_get_status`.
  - `rme_prepare_proposal_preview`,
    `rme_prepare_proposal_preview_region` (bounded, requires certified
    `materialize_ai_preview_region`, never falls back to full-map generation),
    `rme_list_proposal_blocks`, `rme_preview_proposal_block`.
  - `rme_approve_proposal`, `rme_reject_proposal`,
    `rme_approve_proposal_block` (block approval requires `confirm=true` plus
    `RME_MCP_ALLOW_APPROVAL=1`).
  - `rme_cli_validate_request`, `rme_cli_generate_batch`,
    `rme_cli_execute_request` (validated `.json` spec + safe `.bat`).
- Resources: `rme://workspace/status`, `rme://workspace/audit`.
- Prompt: `rme_safe_map_change`.
- Multi-client safety: pending AI proposals carry an owner
  (`_proposal_owner`); a second client (Claude, Codex, OpenCode, another
  session) cannot overwrite, approve, or reject another client's proposal
  (`RME-AI-PROPOSAL-OWNED`, fail-closed).
- Transport: STDIO proxied to the running Qt process over authenticated local
  IPC (`RME_IPC_HOST` / `RME_IPC_PORT` / `RME_IPC_TOKEN` or OS ephemeral
  secret). If RME Alpha AI is not running, the server exits with code 2
  instead of starting a standalone Core.
- Observability: bounded stage metrics (`proposal`, `preview`, `opening`,
  `sessions`) with before/after RAM/CPU samples, plus a read-only HUD summary
  (`stage_summary()`, last 8 stages) and non-invasive MCP resource warnings
  (`panels/mcp_control_dock.py`).

## 5. Light System

RME-parity lighting (`workspace_core/rendering/tile_renderer.py`,
`render_context.py`, `viewport/map_scene.py`, `mainwindow.py`):

- Light is a **single scene-level pass**, not baked per tile: per-tile
  composites carry no glow squares.
- Per-tile sources come from item flags (`light_brightness`, `light_color`).
- View toggles under `View > Lights`:
  - `Show lights` (`Shift+L`).
  - `Show light strength` (`Shift+K`).
- Palette parity test: rendering the same stack (e.g. item 2112) with
  `show_lights=True/False` keeps geometry identical while the scene glow
  differs (`test_light_not_baked_per_tile_anymore`).

### 5.1 Light Control HUD (new)

- Floating `Light Control` dialog (`panels/light_control_dialog.py`) under
  `View > Lights > Light Control...` (`Shift+Alt+L`).
- `Light 0–100%`: scales every dynamic light (100% = RME parity,
  0% = no dynamic lights).
- `Shadow 0–100%`: ambient depth outside light reach (100% = dark RME
  ambient, 0% = no shadow / always bright).
- `Respect collisions` (default ON): lights no longer pass through walls /
  tall objects. Occlusion reuses the certified client `unsight` flag
  (appearances proto field 15, `TileRenderer._tile_blocks_sight()`), the same
  flag the real client uses for spells/creature vision — no invented wall
  category. `Valores RME` resets to 100/100/no-occlusion (pure radial RME).
- Performance: sliders are debounced and setters
  (`set_light_percent()` / `set_shadow_percent()` /
  `set_light_respect_collisions()`) only rebuild the bounded light-overlay
  quad, never the full tile cache. Tests: 12 passed in
  `tests/test_light_field.py` (parity + percent + occlusion).

### 5.2 NPC / monster spawn visibility fix (rev. 2)

- **File spawns now load:** `<map>-monster.xml` / `<map>-npc.xml` sidecars
  next to the `.otbm` are parsed at open with upstream RME discard rules
  (`IOMapOTBM::loadSpawnsMonster/loadSpawnsNpc`: bad position, `radius < 1`,
  nameless entries, duplicates keep the first) and attached to their center
  tiles (`workspace_core/editor/spawn_sidecar_loader.py`). File data only
  fills empty slots — brush placements always win.
- **Indexed chunks no longer drop creatures/spawns** (`adapter.get_map_chunk`
  now propagates both into `TileStack`/`TileState`, mirroring the
  non-indexed path).
- **Spawns layer gates the spawn-center ring:** `Show monster spawns` (S) /
  `Show NPC spawns` (U) toggle the `Spawns` layer, which now flows through
  `RenderContext.show_spawns` into the renderer (cache keys included).
- **Unknown looks fall back to outfit 197** instead of vanishing silently
  (upstream `MapDrawer::BlitCreature` Carl-bot tribute parity).
- Tests: 7 passed in `tests/test_creature_spawn_visibility.py`.
- Requirement: keep the `-monster.xml` / `-npc.xml` files next to the `.otbm`
  (as RME saves them). Embedded `SPAWN_AREA` nodes inside the OTBM itself are
  still counted only, not mapped to tiles.

## 6. Animations

Canary-faithful animation playback
(`workspace_core/rendering/animation_resolver.py`, `tile_renderer.py`,
`panels/sprite_grid.py`, `panels/animation_inspector_hud.py`):

- `AnimationResolver` mirrors `appearances.proto` loop types
  (`PINGPONG=-1`, `INFINITE=0`, `COUNTED=1`):
  - Real per-phase `(duration_min, duration_max)` timing with deterministic
    FNV-1a stable hash (LegacyX `AnimationPolicyEngine` parity), 500 ms
    fallback for phaseless frames (RME `ITEM_FRAME_DURATION`).
  - Synchronous phases share the global clock; `random_start_phase` /
    non-synchronized appearances offset by `hash % cycle`.
  - Counted loops freeze on the last frame; pingpong walks the triangle
    without doubling endpoints.
- Viewport:
  - Animation preview toggle (`Show Preview`, `L`) and speed control
    (`viewport/animation_speed`, persisted in settings).
  - Only truly animated tiles bucket the render key by time
    (`elapsed_ms // 50`); static tiles keep a stable key (FIFO churn fix).
  - Static-base + animated-overlay fast path when all animated layers sit
    above static layers (e.g. animated top item over static ground).
- Palette:
  - Animated item icons cycle frames (e.g. item 946 → 4 frames;
    static e.g. 1082 → 1 frame; unknown → empty).
  - `_SpriteCell.set_anim_frames()` / `show_anim_frame()` animate cells
    in place.
- Diagnostics:
  - `Animation Appearance Inspector` window.
  - `python inspect_animation_appearance.py --items 946 5064 5066`
    (`--range`, `--fail-only`, `--output` supported).

## 7. Other improvements in this build

- Clean PyInstaller packaging (`rme_workspace.spec`, `build_release.py`):
  versioned `resources/data-15.30/` + `resources/data-15.33/` trees,
  `resources/creatures/`, `npc_maker/`, `script_creator/`,
  `modern_brushes/`, `asset_versions.json`, icon, and version resource are
  validated as prerequisites; foreign ICU DLLs are excluded so Qt6 resolves
  the Windows ICU copy; `_internal/PySide6/lib/fonts/` is pre-created to
  silence `QFontDatabase` deployment warnings.
- Official client sprite sheets stay **external** and pass through the
  first-run validation gate (`workspace_core.startup`); the package does not
  bundle copyrighted assets.
- Planner knowledge DB ships as a first-run-restored zip seed
  (`RME_PLANNER_EXPERIENCE.sqlite3.zip`) to keep the download small.
- Planner experience + knowledge paths (`exports/planner_knowledge/`),
  agent `config/default.yaml`, and `data/rme_*.json` runtime tables are
  bundled from the certified agent core.
- Full i18n coverage for the new HUDs (`i18n.py`: `en` / `es` / `pt`),
  including all `material_sync_*` strings.

## 7.1 Rev. 3 — NPC Maker, View splits, tools parity, Live, shields, AI inventory

- **NPC Maker Outfit tab** (`panels/npc_maker_hud.py`): reorganized into 3
  sub-panels mirroring upstream `OutfitSelector.jsx` (Looktype y Colores /
  Outfits y Monturas / Addons) with the NPC preview always visible; 18-column
  color grid parity; mount search/list hidden until Mount is checked; color
  swatches on Head/Body/Legs/Feet. Layout-only, export/import untouched.
- **View splits (RME parity):** `Show monsters` / `Show NPCs` and
  `Show monster spawns` / `Show NPC spawns` are now four independent toggles
  (own layers `Monsters`, `NPCs`, `Monster Spawns`, `NPC Spawns`).
- **Show houses / Show special now work:** house tint for `house_id` tiles
  (id propagated on chunk load) and protection-zone tint from `flags & 1`.
- **Eraser parity:** monster/npc/spawn/zone/house erasers remove what the
  active brush owns (kind-checked); wall/ground/border erases refresh
  neighbor borders in the same atomic transaction; PZ/NoPvP/Logout/PvP tools
  require a ground tile (upstream `FlagBrush::canDraw`).
- **Live menu + floating HUD:** top-level `Live` menu (`Ctrl+Shift+L`) with
  connect/disconnect/cursor-share/status; floating panel with local session
  handshake, peers, cursor sharing and chat — packet types verbatim from
  `live_packets.h`, no network yet (honestly labeled).
- **OTBM gate + anti-abuse:** magic-over-extension validation, 512 MiB cap,
  non-regular-file refusal and open rate-limiting (`CORE-OTBM-GATE`,
  `CORE-OTBM-RATELIMIT`) at the single `open_otbm` choke point; guarded XML
  parsing (no DTD/entities, bounded size) for sidecars, catalogs, zone
  imports and mock maps; zone record ranges; 1000-packet Live outbox cap.
- **AI Studio version inventory:** planner `material_root` rebinds on
  profile switch (caches cleared) and proposals carry the active tree's new
  palettes (15.30: 1415 ids; 15.33: 55095, 55117) so models cite versioned
  brushes/items.

## 7.2 Rev. 4 — 15.33.8f27df live pack + outfit corrections

- **New supported client build:** `15.33.8f27df` ("15.33 live client",
  SHA-256 `2dfa94…`, version read from the client's own `package.json`).
  Inherits the full `data-15.33` tree (materials, items.xml, palettes, AI
  context, Material Sync). Delta vs 15.30: +2 objects (43516), outfits and
  effects unchanged.
- **NPC Maker outfit corrections** (`resources/npc_maker/outfits.json`,
  now 275 outfits): Captain 1940 (M) / 1941 (F) added (Captain's Outfits,
  15.32 Great Expedition event; sprites already in the 15.30 pack);
  1973/1974 corrected to Illuminated Warrior (M/F) and 1976/1977 to Moon
  Guardian (M/F) per the TibiaWiki Outfit IDs table (Name/male/female
  columns, cross-validated) — replacing the OTServ file's uncertain names,
  per its own warning. 1944 (full outfit structure) and the remaining
   unnamed 15.30 lookTypes stay out: no invented names (1942 does not exist
   in any pack).

## 7.3 Rev. 5 — Live menu fix, outfit colors, animation inheritance

- **Live menu placement + HUD crash fix:** `Live` now survives the menubar
  rebuild and sits right before `About` (`… Creator, Live, Extras, About`);
  fixed a method/attribute name collision (`_live_hud` → `_get_live_hud`)
  that crashed every Live action on first use. Verified in the real window:
  order, HUD, connect, cursor share, chat, menu status, disconnect.
- **NPC Maker outfit colors corrected** (`colors.json` hue-18 column):
  18/37/56/75/94/113 now match the real client (OTClient `Outfit::getColor`
  HSI + RME `TemplateOutfitLookupTable`, e.g. 94 is pure red `#ff0000`).
- **Animation zero-phase inheritance:** `(0,0)` phases take the first
  non-zero sibling duration (OTClient `Animator::unserializeAppearance`
  parity); 1ms only when all phases are zero. Stateless deterministic
  resolver unchanged otherwise.

## 7.4 Rev. 6 — creature catalog fallback, shade overlay + instant toggles

- **Monster/NPC palettes no longer empty:** the creature catalog now falls
  back to the bundled official registry (1834 monsters + 1080 NPCs) when no
  `RME_*_ROOT` is configured — the renderer already did; the palettes did
  not. Server/env data keeps precedence.
- **Show shade fixed (two bugs):** shade is now a black `(0,0,0,128)`
  overlay over above-floor tiles (exact `DrawShade` parity) instead of a
  ghostly opacity, and shade/ghost toggles apply instantly in place — the
  old full chunk re-render blocked the GUI for 30+ minutes on large maps,
  reading as "stuck on". Scene-only flags left the pixmap cache keys.

## 7.5 Rev. 7 — house/PZ tints with upstream math

- **Show houses / Show special render like RME:** the previous flat
  translucent wash is replaced by multiply blends with the exact upstream
  factors (`r/=2,g/=2` houses → `128,128,255`; `r/=2,b/=2` PZ →
  `128,255,128`), aligned to the tile footprint. Verified pixel-by-pixel
  on a real map (13.6% washed pixels → 1.7% genuine map purples).

## 8. How to run

1. Copy the whole `RME Alpha AI` folder (keep `RME_Alpha_AI.exe` next to
   `_internal/`).
2. Launch `RME_Alpha_AI.exe`.
3. On first run, point **Preferences** to your Tibia asset folder
   (`appearances-*.dat` + `catalog-content.json`); the version detector will
   label it 15.24 / 15.30 / 15.33 or `unidentified`.
4. Open the **Item Palette** and expand `New - …` tilesets for the active
   version; use **Sync Materials** to scan a newer pack before editing.

## 9. Evidence / source map

- `workspace_core/material_sync/` (`__init__.py`, `compare.py`,
  `items_sync.py`, `tilesets_sync.py`, `brushs_sync.py`, `borders_sync.py`,
  `writer.py`, `refresh.py`, `source.py`) + `panels/material_sync_hud.py`.
- `workspace_core/asset_versions.py`, `resources/asset_versions.json`.
- `resources/data-15.30/items.xml`, `resources/data-15.33/items.xml`,
  `resources/data-15.30/tilesets/`, `resources/data-15.33/tilesets/`.
- `mcp_server.py`, `workspace_ipc.py`, `panels/mcp_control_dock.py`.
- `workspace_core/rendering/animation_resolver.py`,
  `workspace_core/rendering/tile_renderer.py`,
  `workspace_core/rendering/render_context.py`,
  `viewport/map_scene.py`, `panels/animation_inspector_hud.py`,
  `inspect_animation_appearance.py`.
- Tests: `test_version_materials.py`, `test_new_items_tileset.py`,
  `test_palette_animation_lights.py`, `test_preview_fidelity_stage18.py`,
  `test_material_sync_fase*.py`, `test_mcp_*.py`.
