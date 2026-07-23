# Manual de Usuario - RME Agente AI Alpha

RME Agente AI Alpha es una version alpha del workspace/editor del proyecto Agente RME AI. Esta version sirve para pruebas tempranas de apertura, visualizacion, edicion, generacion asistida por IA y exportacion de mapas OpenTibia compatibles con Canary/RME.

El programa todavia esta en desarrollo. Si encuentras errores, reportalos con la estructura incluida al final de este manual.

## 1. Archivos que debes descomprimir

Cuando recibas el paquete, descomprime la carpeta completa:

```text
RME Alpha AI

---
Luego en la carpeta _internal/exports/
descomprime el Archivo: "planner_knowledge.zip"
es una base de datos con la que funciona la aplicacion.
```

Dentro deben existir, como minimo:

```text
RME Alpha AI/
  RME_Agente_AI_Alpha.exe
  README.md
  MANUAL_USUARIO.md
  _internal/
```

No ejecutes el `.exe` separado de `_internal`. El ejecutable necesita esa carpeta para cargar librerias, materiales, configuracion, catalogos, base del Planner y recursos del editor.

No borres ni muevas estos elementos:

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

Si mueves la aplicacion a otra ubicacion, mueve siempre la carpeta completa `RME Alpha AI`.

## 2. Assets oficiales requeridos

La aplicacion no incluye assets privados del cliente. En el primer inicio, o desde `File > Locate Tibia Assets...`, debes seleccionar una carpeta de assets valida.

La carpeta de assets debe contener:

```text
appearances-*.dat o appearances.dat
catalog-content.json
sprite sheets oficiales del cliente
```

Si aparece un error parecido a:

```text
Validation result: FAILED
Error: No sprite sheets
```

significa que seleccionaste una carpeta incompleta. Vuelve a localizar la carpeta raiz correcta del cliente/assets, no solo la carpeta donde esta el `.dat`.

La configuracion de inicio se guarda en:

```text
%APPDATA%\Agente RME\RME Workspace\startup_assets.json
```

Si configuraste una ruta incorrecta y la app no carga bien, puedes cerrar la app, borrar ese archivo y volver a abrirla para seleccionar los assets otra vez.

## 3. Inicio rapido

1. Descomprime la carpeta completa `RME Alpha AI`.
2. Abre `RME_Agente_AI_Alpha.exe`.
3. Localiza los assets oficiales si la app lo solicita.
4. Usa `New` para crear un mapa nuevo o `Open Map` para abrir un `.otbm`.
5. Selecciona una paleta y un brush.
6. Pinta en el viewport con clic izquierdo.
7. Usa clic derecho sobre el mapa para abrir el menu contextual.
8. Usa `Save` para guardar o exportar el mapa.

Atajos basicos esperados:

```text
Ctrl+N       Nuevo mapa
Ctrl+O       Abrir mapa
Ctrl+S       Guardar
Ctrl+Z       Undo
Ctrl+Y       Redo
Delete       Borrar seleccion
+ / -        Subir o bajar piso
Ctrl+G       Ir a posicion
```

Algunas funciones siguen en alpha. Si un menu aparece pero no ejecuta nada, reportalo.

## 4. Como pedir un mapa a la IA

Los mejores resultados salen cuando el prompt contiene datos concretos y usa referencias reales sin pedir copiar geometria. Las referencias sirven para estilo, densidad, materiales y ritmo de mapeo, no para duplicar zonas existentes.

Usa esta estructura:

```text
Nombre del mapa:
Town:
Coordenadas del town:
Nivel recomendado:
Tipo de mapa:
Referencias de ciudad maximo 2:
Referencias de bioma/hunt maximo 2:
Zonas obligatorias:
Gameplay:
Conectividad:
Materiales/estilo:
Restricciones:
Exportacion:
```

Ejemplo:

```text
Nombre del mapa: Ikaro
Town: Ika
Coordenadas del town: x=998, y=1000, z=7
Nivel recomendado: 300
Tipo de mapa: isla hunt pequena estilo Krailos
Referencias de ciudad maximo 2: ninguna
Referencias de bioma/hunt maximo 2: Krailos, roshamuul_map
Zonas obligatorias: templo pequeno con Protection Zone, costa, montanas, arena, roca seca, vegetacion de Krailos, spawns de dragon y dragon lord
Gameplay: rutas de kite, zonas seguras cerca del templo, zonas peligrosas hacia la montana
Conectividad: sin teleports, usar caminos, rampas, escaleras y pasos naturales
Materiales/estilo: usar solo materiales oficiales de RME/Canary, ground brushes reales, autoborders reales y sprites oficiales
Restricciones: no copiar geometria de mapas de referencia, no inventar IDs, no usar placeholders, no colocar puertas en el templo
Exportacion: generar OTBM compatible con RME/Canary y reporte de validacion
```

Evita prompts ambiguos como:

```text
Hazme un mapa bonito
```

Evita pedir IDs manuales si no sabes que existen. Es mejor pedir familias oficiales:

```text
usa arena, roca seca, vegetacion de Krailos, borders oficiales y montanas con escaleras reales
```

## 5. Como reportar errores

Cada reporte debe incluir:

```text
Version de la app:
Fecha y hora:
Windows:
Mapa abierto:
Assets usados:
Prompt usado:
Pasos para reproducir:
Resultado esperado:
Resultado obtenido:
Mensaje de error completo:
Screenshot o video:
Archivo .otbm si aplica:
```

Ejemplo:

```text
Version de la app: RME Agente AI Alpha
Fecha y hora: 2026-07-23 18:30
Windows: Windows 11
Mapa abierto: Ikaro.otbm
Assets usados: cliente 15.24
Prompt usado: crear isla estilo Krailos...
Pasos para reproducir:
1. Abrir la app.
2. Crear mapa nuevo.
3. Escribir prompt.
4. Click en Generate Proposal.
Resultado esperado: genera isla con costa y templo PZ.
Resultado obtenido: aparece tile negro y no exporta.
Mensaje de error completo: Certified AI preview failed...
Screenshot o video: adjunto.
Archivo .otbm: adjunto si no contiene contenido privado.
```

Los logs de la aplicacion se guardan en:

```text
%LOCALAPPDATA%\Agente RME\RME Workspace\logs
```

Adjunta el log mas reciente cuando reportes un crash o un error de carga.

No compartas claves API, tokens, archivos privados del cliente, datos personales ni configuraciones con secretos. Si un log contiene claves, borralas antes de enviarlo.

## 6. Recomendaciones para pruebas

Prueba primero mapas pequenos:

```text
64x64
128x128
zonas de un solo bioma
una ciudad pequena
una hunt corta
```

Despues prueba mapas mas complejos:

```text
varios pisos
montanas con escaleras
casas
depot
templo
spawns
NPCs
zonas PZ
```

Para comparar resultados, abre el `.otbm` exportado en Canary/RME y revisa:

```text
tiles negros
items sin sprite
grounds equivocados
autoborders faltantes
paredes mal orientadas
puertas donde no deben existir
spawns fuera de zona jugable
zonas PZ faltantes
lag al desplazarse
crash al guardar o abrir
```

## 7. Estado alpha

Esta version busca acercar el workspace al comportamiento de RME/Canary y preparar pruebas reales con usuarios. El objetivo es que el Planner y las IA aprendan de materiales oficiales, mapas de referencia y validacion humana para disenar mapas cada vez mas cercanos al trabajo de un mapper humano.

Si algo falla, no lo ignores: reportalo con pasos claros. Cada reporte ayuda a mejorar el editor, el Planner, el render, el brush engine y la generacion de mapas.
