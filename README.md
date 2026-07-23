# RME Agente AI Alpha

RME Agente AI Alpha es una version temprana en desarrollo de un editor y asistente de mapas para OpenTibia. El objetivo del proyecto es evolucionar el flujo clasico de Remere's Map Editor con herramientas modernas de IA, Planner semantico, validacion visual y generacion asistida de mapas.

Esta build es una version alpha para pruebas. Todavia se estan mejorando los sistemas de render, brushes, auto-border, planificacion de biomas, casas, spawns, NPCs, quests, zonas y validacion OTBM hasta lograr mapas con una calidad cada vez mas cercana al trabajo de un mapper humano.

## Lenguajes y tecnologia

- Python
- PySide6 / Qt para la interfaz de escritorio
- SQLite para la base de conocimiento del Planner
- XML / JSON para materiales, brushes, catalogos y configuracion
- PyInstaller para crear la version ejecutable de Windows

El proyecto trabaja con informacion oficial de OpenTibia, materiales de RME/Canary, `appearances.dat`, `catalog-content.json`, reglas OTB/OTBM y mapas de referencia analizados como conocimiento abstracto. Las referencias se usan para aprender estilo, densidad, materiales y estructura, no para copiar mapas.

## IA y Planner

El Planner puede trabajar con proveedores de IA configurables:

- Ollama
- OpenRouter
- PaxSenix

Tambien incluye modos de seleccion automatica y consenso entre modelos para ayudar al Planner a revisar propuestas, detectar errores visuales, ajustar biomas y mejorar la logica de construccion. Los modelos no escriben IDs de items directamente: sus propuestas deben pasar por el material catalog, brush engines certificados, validacion OTBM y QA visual.

## Estado del proyecto

RME Agente AI Alpha es un proyecto Open Source en desarrollo activo. Esta version esta pensada para pruebas tempranas, deteccion de errores y retroalimentacion. Algunas funciones pueden cambiar, mejorar o ser reemplazadas conforme avance la compatibilidad con RME/Canary y el sistema de generacion de mapas.

## Assets

Por razones de distribucion, los assets oficiales del cliente Tibia no se incluyen dentro del paquete. Al iniciar por primera vez, la aplicacion puede solicitar la carpeta del cliente/assets para localizar los archivos requeridos, como `appearances.dat`, `catalog-content.json` y sprites oficiales.

## Creador

Proyecto creado y desarrollado por ricker72.

- GitHub: https://github.com/ricker72
- Portafolio y noticias del proyecto: https://ricker72.github.io/
