<p align="center"># 🗺️ RME Agente AI Alpha

[![Versión](https://img.shields.io/badge/versión-0.1.0--alpha-blue)](https://github.com/ricker72/rme-agente-ai)
[![Licencia](https://img.shields.io/badge/licencia-MIT-green)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.10+-yellow)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/PySide6-6.5+-orange)](https://doc.qt.io/qtforpython/)
[![Estado](https://img.shields.io/badge/estado-en%20desarrollo%20activo-brightgreen)](https://github.com/ricker72/rme-agente-ai)
</p>
---

> **Un editor y asistente de mapas para OpenTibia impulsado por inteligencia artificial.**  
> *Transforma el flujo clásico de Remere's Map Editor con herramientas modernas, planificación semántica y validación visual.*

<p align="center">
  <img width="800" height="400" alt="Rme01" src="https://github.com/user-attachments/assets/f301706d-a9fc-43c1-b30b-228c73e079d2" />

</p>

---

## 🚀 ¿Qué es RME Agente AI Alpha?

Es una **versión temprana** de un editor de mapas para OpenTibia que **fusiona la potencia de RME con inteligencia artificial**. El objetivo es evolucionar el flujo clásico de mapeo, añadiendo:

- 🤖 **Asistente IA** para generar y validar estructuras.
- 🧠 **Planner semántico** que entiende biomas, casas, spawns y quests.
- ✅ **Validación automática** de mapas (OTBM) y detección de errores visuales.
- 🎨 **Sistema de brushes inteligentes** y auto‑bordeado.

Esta *alpha* está diseñada para pruebas, retroalimentación y mejora continua. Cada actualización acerca la calidad de los mapas generados a la de un **mapper humano experto**.

[![Ver video](https://ejemplo.com/miniatura.jpg)](https://www.image2url.com/r2/default/videos/1784798715343-bbcb278a-c6a2-4b6f-9879-5d6c9062000e.mp4)

<img width="1919" height="1019" alt="Screenshot_1" src="https://github.com/user-attachments/assets/aa529d8c-914b-4d83-b92a-213f65fdfc56" />


---

## ✨ Características principales

| Icono | Característica |
|-------|----------------|
| 🧩 | **Planificación semántica** de biomas, casas, spawns, NPCs y quests. |
| 🤖 | **Planner IA** con soporte para Ollama, OpenRouter y PaxSenix. |
| 🔍 | **Validación OTBM** y corrección automática de errores. |
| 🖌️ | **Brushes inteligentes** y auto‑bordeado basado en materiales. |
| 📊 | **Base de conocimiento** (SQLite) para aprendizaje y recomendaciones. |
| 🎯 | **Consenso entre modelos** para decisiones más acertadas. |
| 🖥️ | **Interfaz gráfica** con PySide6 (Qt), moderna y responsive. |

---

## 🛠️ Tecnologías utilizadas

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/PySide6-41CD52?style=for-the-badge&logo=qt&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
  <img src="https://img.shields.io/badge/XML-FF6600?style=for-the-badge&logo=xml&logoColor=white" />
  <img src="https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white" />
  <img src="https://img.shields.io/badge/PyInstaller-2B5B84?style=for-the-badge&logo=pyinstaller&logoColor=white" />
</p>

- **Python 3.10+** – Lenguaje principal.
- **PySide6 / Qt** – Interfaz gráfica de escritorio.
- **SQLite** – Base de conocimiento interna del Planner.
- **XML / JSON** – Catálogos de materiales, brushes y configuración.
- **PyInstaller** – Empaquetado para Windows.

---

## 🤖 El Planner IA

El **Planner** puede conectarse a diferentes proveedores de IA para asistir en la generación y revisión de mapas:

- **Ollama** (local)
- **OpenRouter** (multimodelo en la nube)
- **PaxSenix** (servicio especializado)

Además, cuenta con modos de **selección automática** y **consenso entre modelos** para:

- Revisar propuestas de construcción.
- Detectar errores visuales y de densidad.
- Ajustar biomas y estructuras.
- Mejorar la lógica de generación.

> ⚠️ **Importante:** Los modelos **no escriben IDs de ítems directamente**. Todas las propuestas pasan por los catálogos de materiales, motores de brushes certificados, validación OTBM y control de calidad visual. Esto asegura que los mapas generados sean compatibles y jugables.

---

## 📊 Estado del proyecto

| Estado | Descripción |
|--------|-------------|
| 🧪 **Alpha** | En desarrollo activo, estable para pruebas. |
| 🔄 **Actualizaciones** | Semanales, con mejoras basadas en feedback. |
| 🐛 **Errores** | Se esperan algunos, agradecemos reportes. |
| 🗺️ **Compatibilidad** | En progreso con RME/Canary y estándares OpenTibia. |

> **El proyecto es Open Source** y toda contribución es bienvenida.
<img width="1919" height="1024" alt="Screenshot_2" src="https://github.com/user-attachments/assets/acce6923-3ab9-4996-a912-299e23db12b0" />

---

## 📦 Assets y distribución

Por razones legales, **los assets oficiales del cliente de Tibia** no se incluyen en el paquete distribuible.

Al iniciar la aplicación por primera vez, se te solicitará la **carpeta del cliente** (`/assets`) para localizar:

- `appearances.dat`
- `catalog-content.json`
- Sprites oficiales

La aplicación usará estos archivos para funcionar correctamente.

---

## 👤 Creador

**Desarrollado por ricker72**  
Apasionado por OpenTibia, la IA y el desarrollo de herramientas creativas.

<p align="center">
  <a href="https://github.com/ricker72">
    <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
  <a href="https://ricker72.github.io">
    <img src="https://img.shields.io/badge/Portafolio-000000?style=for-the-badge&logo=About.me&logoColor=white" />
  </a>
</p>

---

## 🧭 ¿Cómo empezar?

1. **Descarga la última versión**
2. **Ejecuta** el instalador o el ejecutable portátil.
3. **Configura** tu carpeta de assets cuando se te solicite.
4. **Explora** el editor y prueba el Planner IA.

> Esta Version incluye un Manual de Usuario favor de leerlo antes de empezar: /MANUAL_USUARIO.md
<img width="1919" height="1022" alt="Screenshot_3" src="https://github.com/user-attachments/assets/4abe2a8c-b96f-4503-8709-76016f89cdbb" />

---

## 📄 Licencia

Este proyecto está bajo la licencia **MIT**.  
Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

**¡Gracias por tu interés!**  
Tu apoyo y feedback son fundamentales para hacer de RME Agente AI la herramienta definitiva para la creación de mapas en OpenTibia.
