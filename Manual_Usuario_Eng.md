# User Manual - RME AI Agent Alpha

RME AI Agent Alpha is an alpha version of the workspace/editor for the RME AI Agent project. This release is intended for early testing of OpenTibia map opening, visualization, editing, AI-assisted generation, and export compatible with Canary/RME.

The application is still under development. If you find any issues, please report them using the structure provided at the end of this manual.

## 1. Files You Must Extract

When you receive the package, extract the entire folder:

```text
RME Alpha AI
```

The folder must contain at least:

```text
RME Alpha AI/
  RME_Agente_AI_Alpha.exe
  README.md
  MANUAL_USUARIO.md
  _internal/
```

Do not run the `.exe` without the `_internal` folder. The executable depends on it to load libraries, materials, configuration, catalogs, the Planner database, and editor resources.

Do not delete or move:

```text
_internal/config/
_internal/data/
_internal/exports/
_internal/projects/
_internal/resources/
_internal/workspace_core/
_internal/APPEARANCE_ITEM_CATALOG.json
_internal/APPEARANCE_RENDER_CATALOG.json
```

If you move the application, always move the entire `RME Alpha AI` folder.

## 2. Required Official Assets

The application does not include proprietary client assets. On first launch, or through `File > Locate Tibia Assets...`, select a valid assets folder.

The assets folder must contain:

```text
appearances-*.dat or appearances.dat
catalog-content.json
Official client sprite sheets
```

If you see:

```text
Validation result: FAILED
Error: No sprite sheets
```

you selected an incomplete folder. Select the root client/assets folder instead of only the folder containing the `.dat` file.

Startup configuration is stored in:

```text
%APPDATA%\Agente RME\RME Workspace\startup_assets.json
```

Delete this file if you configured the wrong path and restart the application.

## 3. Quick Start

1. Extract the complete `RME Alpha AI` folder.
2. Run `RME_Agente_AI_Alpha.exe`.
3. Locate the official assets if requested.
4. Use `New` or `Open Map`.
5. Select a palette and brush.
6. Paint with the left mouse button.
7. Right-click for the context menu.
8. Use `Save` to save or export.

### Keyboard Shortcuts

```text
Ctrl+N  New Map
Ctrl+O  Open Map
Ctrl+S  Save
Ctrl+Z  Undo
Ctrl+Y  Redo
Delete  Delete Selection
+ / -   Change Floor
Ctrl+G  Go To Position
```

Some features are still experimental.

## 4. Requesting an AI Map

Use detailed prompts.

```text
Map Name:
Town:
Town Coordinates:
Recommended Level:
Map Type:
Town References (max 2):
Biome/Hunt References (max 2):
Required Areas:
Gameplay:
Connectivity:
Materials/Style:
Restrictions:
Export:
```

Example:

```text
Map Name: Ikaro
Town: Ika
Town Coordinates: x=998, y=1000, z=7
Recommended Level: 300
Map Type: Small island hunt inspired by Krailos
Town References: None
Biome References: Krailos, roshamuul_map
Required Areas: Small temple with Protection Zone, coast, mountains, sand, dry rock, Krailos vegetation, Dragon and Dragon Lord spawns
Gameplay: Kite routes, safe area near the temple, dangerous mountain region
Connectivity: No teleports; use roads, ramps, stairs, and natural passages
Materials/Style: Official RME/Canary materials only
Restrictions: Do not copy reference geometry, invent IDs, use placeholders, or place temple doors
Export: Generate Canary/RME compatible OTBM with validation report
```

Avoid vague prompts such as:

```text
Make me a nice map
```

## 5. Reporting Bugs

Include:

```text
Application Version:
Date and Time:
Windows Version:
Opened Map:
Assets Used:
Prompt:
Steps to Reproduce:
Expected Result:
Actual Result:
Complete Error Message:
Screenshot or Video:
OTBM File (if applicable):
```

Logs:

```text
%LOCALAPPDATA%\Agente RME\RME Workspace\logs
```

Attach the latest log when reporting crashes. Never share API keys, tokens, proprietary client files, or personal information.

## 6. Testing Recommendations

Start with:

```text
64x64
128x128
Single-biome maps
Small town
Short hunt
```

Then test:

```text
Multiple floors
Mountains with stairs
Houses
Depot
Temple
Spawns
NPCs
Protection Zones
```

Check exported OTBM files for:

```text
Black tiles
Missing sprites
Incorrect grounds
Missing autoborders
Incorrect wall orientation
Invalid doors
Spawn placement
Missing Protection Zones
Performance issues
Save/Open crashes
```

## 7. Alpha Status

This alpha aims to bring the workspace closer to RME/Canary behavior and prepare real-world testing. Every bug report helps improve the editor, Planner, renderer, brush engine, and AI map generation.
