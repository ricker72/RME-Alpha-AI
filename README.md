<p align="center"># 🗺️ RME Agente AI Alpha

[![Version](https://img.shields.io/badge/version-1.0.0--alpha-blue)](https://github.com/ricker72/rme-agente-ai)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-yellow)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/PySide6-6.5+-orange)](https://doc.qt.io/qtforpython/)
[![Status](https://img.shields.io/badge/status-active%20development-brightgreen)](https://github.com/ricker72/rme-agente-ai)
</p>

---

> **An AI-powered map editor and assistant for OpenTibia.**  
> *Transforms the classic Remere's Map Editor workflow with modern tools, semantic planning, and visual validation.*

<p align="center">
  <img width="800" height="400" alt="Rme01" src="https://github.com/user-attachments/assets/f301706d-a9fc-43c1-b30b-228c73e079d2" />
</p>

---

## 🚀 What is RME Agente AI Alpha?

It is an **early version** of an OpenTibia map editor that **merges the power of RME with artificial intelligence**. The goal is to evolve the classic mapping workflow by adding:

- 🤖 **AI Assistant** to generate and validate structures.
- 🧠 **Semantic Planner** that understands biomes, houses, spawns, and quests.
- ✅ **Automatic validation** of maps (OTBM) and visual error detection.
- 🎨 **Intelligent brush system** and auto-bordering.

This *alpha* is designed for testing, feedback, and continuous improvement. Each update brings the quality of generated maps closer to that of an **expert human mapper**.

[![Watch video](https://ejemplo.com/miniatura.jpg)](https://www.image2url.com/r2/default/videos/1784798715343-bbcb278a-c6a2-4b6f-9879-5d6c9062000e.mp4)

<img width="1919" height="1019" alt="Screenshot_1" src="https://github.com/user-attachments/assets/aa529d8c-914b-4d83-b92a-213f65fdfc56" />

---

## ✨ Key Features

| Icon | Feature |
|------|---------|
| 🧩 | **Semantic planning** of biomes, houses, spawns, NPCs, and quests. |
| 🤖 | **AI Planner** with support for Ollama, OpenRouter, and PaxSenix. |
| 🔍 | **OTBM validation** and automatic error correction. |
| 🖌️ | **Intelligent brushes** and material-based auto-bordering. |
| 📊 | **Knowledge base** (SQLite) for learning and recommendations. |
| 🎯 | **Model consensus** for more accurate decisions. |
| 🖥️ | **Graphical interface** with PySide6 (Qt), modern and responsive. |

---

## 🛠️ Technologies Used

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PySide6-41CD52?style=for-the-badge&logo=qt&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/XML-FF6600?style=for-the-badge&logo=xml&logoColor=white" />
  <img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white" />
  <img src="https://img.shields.io/badge/PyInstaller-2B5B84?style=for-the-badge&logo=pyinstaller&logoColor=white" />
</p>

- **Python 3.10+** – Main language.
- **PySide6 / Qt** – Desktop graphical interface.
- **SQLite** – Internal knowledge base for the Planner.
- **XML / JSON** – Material catalogs, brushes, and configuration.
- **PyInstaller** – Packaging for Windows.

---

## 🤖 The AI Planner

The **Planner** can connect to different AI providers to assist in map generation and review:

- **Ollama** (local)
- **OpenRouter** (multi-model cloud)
- **PaxSenix** (specialized service)

It also includes **automatic selection** and **model consensus** modes to:

- Review construction proposals.
- Detect visual and density errors.
- Adjust biomes and structures.
- Improve generation logic.

> ⚠️ **Important:** Models **do not write item IDs directly**. All proposals go through material catalogs, certified brush engines, OTBM validation, and visual quality control. This ensures generated maps are compatible and playable.

---

## 📋 Requirements

Before using RME Agente AI Alpha, make sure you have the following:

### System Requirements
- **OS:** Windows 10/11 (64-bit) for the packaged build. Linux/macOS may work from source but are not officially supported.
- **RAM:** 4 GB minimum, 8 GB recommended.
- **Disk Space:** ~500 MB for the application, plus space for Tibia client assets.
- **Python:** 3.10+ (only if running from source).
- **PySide6:** 6.5+ (installed automatically with the packaged build or via pip).

### Tibia Client Assets
Due to legal reasons, official Tibia client assets are **not included**. On first launch, you will be asked for the **client folder** (`/assets`) to locate:

- `appearances.dat`
- `catalog-content.json`
- Official sprites

### AI Providers (Optional but Recommended)
- **Ollama:** For local AI processing. Install separately and run locally.
- **OpenRouter:** Requires an API key for cloud multi-model access.
- **PaxSenix:** Requires an API key for the specialized service.
- **Internet connection:** Required for cloud AI providers.

---

## 📊 Project Status

| Status | Description |
|--------|-------------|
| 🧪 **Alpha** | Active development, stable for testing. |
| 🔄 **Updates** | Weekly, with improvements based on feedback. |
| 🐛 **Bugs** | Some are expected; reports are appreciated. |
| 🗺️ **Compatibility** | In progress with RME/Canary and OpenTibia standards. |

> **The project is Open Source** and all contributions are welcome.

<img width="1919" height="1024" alt="Screenshot_2" src="https://github.com/user-attachments/assets/acce6923-3ab9-4996-a912-299e23db12b0" />

---

## 🧭 Version Support & Improvements

| Version | Status | Improvements |
|---------|--------|--------------|
| **1.0.0-alpha** | Current | Initial alpha release: AI Planner, semantic planning, OTBM validation, intelligent brushes, SQLite knowledge base, multi-provider AI support (Ollama, OpenRouter, PaxSenix), PySide6 GUI. |
| **RME / Canary** | In progress | Compatibility with RME map formats and Canary server standards. |
| **OpenTibia** | In progress | Adherence to OpenTibia mapping standards and modern client assets. |

Future updates will focus on:
- Enhanced RME/Canary compatibility.
- Improved model consensus and automatic selection.
- More intelligent brushes and auto-bordering rules.
- Expanded knowledge base and recommendation engine.

---

## 📦 Assets & Distribution

Due to legal reasons, **official Tibia client assets** are not included in the distributable package.

On first launch, you will be prompted for the **client folder** (`/assets`) to locate:

- `appearances.dat`
- `catalog-content.json`
- Official sprites

The application will use these files to function correctly.

---

## 🧭 Getting Started

1. **Download the latest version.**
2. **Run** the installer or portable executable.
3. **Configure** your assets folder when prompted.
4. **Explore** the editor and try the AI Planner.

> This version includes a User Manual; please read it before starting: `/MANUAL_USUARIO.md`

<img width="1919" height="1022" alt="Screenshot_3" src="https://github.com/user-attachments/assets/4abe2a8c-b96f-4503-8709-76016f89cdbb" />

---

## 👤 Creator

**Developed by ricker72**  
Passionate about OpenTibia, AI, and creative tool development.

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

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for more details.

---

**Thank you for your interest!**  
Your support and feedback are essential to making RME Alpha AI the definitive tool for OpenTibia map creation.
