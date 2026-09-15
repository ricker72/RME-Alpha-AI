# RME Agente AI Alpha — Manual de usuario

## 1. Distribución y primer arranque

Abra `RME_Agente_AI_Alpha.exe` desde la carpeta completa de distribución. No
separe el ejecutable de `_internal`: esa carpeta contiene Qt, el motor Python,
los catálogos oficiales, materiales, brushes y recursos necesarios.

La aplicación es portable en Windows. No requiere instalar Python. Si aparece
un diálogo de selección de recursos, indique una carpeta que contenga los
materiales oficiales de RME y los archivos de apariencias solicitados.

## 2. Flujo básico del editor

1. Abra o importe un mapa compatible desde File/Open.
2. Seleccione una categoría en Terrain Palette.
3. Seleccione un tileset y después un sprite/material.
4. Pinte con clic izquierdo en el viewport.
5. Use clic derecho para borrar el campo con el brush activo. Al soltarlo, el
   brush queda desarmado; seleccione otro brush antes de volver a pintar.
6. Use Shift + clic izquierdo para iniciar una selección rectangular.
7. Use el botón central para navegar y la rueda para zoom.
8. Guarde/exporte el mapa desde File. Las mutaciones pasan por el pipeline
   certificado y no se escriben directamente desde los paneles.

## 3. Paneles y menú View

AI Studio, Terrain Palette, Tileset Palette, Sprite Grid, RME Palette,
Minimap, Action History, Layers, Properties, Coordinates, Map Properties,
Towns, Houses, Spawns, NPCs, Waypoints, Zones y Diagnostics Console son
paneles acoplables. Se pueden mostrar u ocultar desde View; AI Studio también
se puede cerrar con el botón X de su barra de título y volver a abrir desde
View → AI Studio.

Las opciones de render View controlan el mismo `RenderContext` usado por el
viewport: shade, luces, intensidad de luces, client box, avoidables, objetos
sueltos, pickupables, solo modificados, grid, bordes y previews. Cambiar una
opción no modifica el mapa.

## 4. AI Studio

AI Studio nunca aplica una propuesta automáticamente:

1. Elija el modo del proveedor.
2. Escriba el cambio deseado en Prompt.
3. Pulse Generate Proposal.
4. Revise Tile diff y, opcionalmente, use Inspect View y AI Review.
5. Pulse Approve solo después de revisar la propuesta; Reject deja el mapa sin
   cambios.

Los modos disponibles son:

- Automatic failover: intenta los proveedores configurados en el orden válido.
- Ollama: servidor local o Ollama Cloud.
- OpenRouter.
- PaxSenix.
- Triple consensus: solicita validación combinada cuando los proveedores
  disponibles lo permiten.

## 5. Configurar claves de API sin incluirlas en la distribución

Nunca escriba una clave dentro del código, del manual, de un archivo JSON del
paquete ni de un issue. El paquete público se entrega sin claves.

### Opción A: AI Studio

Seleccione el proveedor, escriba su clave en el campo API y pulse Save. El
campo es de contraseña y se limpia después de guardarla. El Core certificado
gestiona la persistencia protegida de Windows; si el almacenamiento protegido
no está disponible, use variables de entorno.

### Opción B: variables de entorno de Windows

Configure las variables antes de abrir la aplicación:

```powershell
$env:OPENROUTER_API_KEY = "SU_CLAVE_LOCAL"
$env:PAXSENIX_API_KEY = "SU_CLAVE_LOCAL"
$env:OLLAMA_API_KEY = "SU_CLAVE_LOCAL"
```

Para Ollama local puede configurar también:

```powershell
$env:OLLAMA_HOST = "http://127.0.0.1:11434"
$env:OLLAMA_MODEL = "qwen3:8b"
```

Para cambiar modelos o un gateway compatible personalizado:

```powershell
$env:RME_CUSTOM_AI_BASE_URL = "https://servidor-compatible.example/v1"
$env:RME_CUSTOM_AI_MODEL = "nombre-del-modelo"
```

El orden de failover se puede ajustar con una lista separada por comas:

```powershell
$env:RME_AI_PROVIDER_ORDER = "ollama,openrouter,paxsenix"
```

Estas variables son ejemplos de nombres, no contienen credenciales reales.
Use una sesión de PowerShell nueva para que el proceso herede los valores.

## 6. Importación y recursos

Use File → Open/Import y seleccione un formato compatible. La conversión debe
resolver materiales, apariencias y brushes contra los catálogos oficiales
incluidos; si falta un recurso, la aplicación debe mostrar el bloqueo y no
inventar IDs. Con mapas grandes, espere a que termine la carga antes de editar.

Para reportar un error incluya: versión, Windows, pasos reproducibles, formato
del mapa, mensaje visible y el contenido de Diagnostics Console. Nunca adjunte
claves, tokens, archivos de configuración personales ni mapas privados.

## 7. Qué contiene el paquete público

El paquete incluye únicamente el ejecutable, `_internal`, recursos oficiales,
catálogos, materiales, datos runtime y este manual. Se excluyen roadmap,
paridad, auditorías, reportes, screenshots, tests, cachés, logs de desarrollo,
fuentes y secretos.

## 8. Solución rápida

- **QtCore DLL:** ejecute el EXE desde su carpeta completa; no copie solo el
  ejecutable.
- **No hay sprites/materiales:** revise la carpeta de recursos seleccionada y
  que contenga los manifiestos oficiales.
- **AI sin respuesta:** compruebe el proveedor seleccionado, su endpoint, el
  modelo y la clave; pruebe primero Ollama local.
- **El botón Approve está deshabilitado:** la propuesta no pasó la vista previa
  certificada o no existe una propuesta activa.
- **Brush inesperado:** haga clic derecho para borrar y seleccione nuevamente
  el brush deseado antes de pintar.
