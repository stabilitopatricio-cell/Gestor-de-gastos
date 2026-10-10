# Gestor de Gastos Personal 

## Motivo del Proyecto 

Este proyecto nace como parte de mi proceso de **formación autodidacta** en desarrollo de software. 

La decisión de crear un gestor de gastos personal responde a un principio básico: **resolver una necesidad real**. Al final, esa es la intención elemental de cualquier programa: construir algo útil que sirva para solucionar un problema concreto de la vida cotidiana. 

## Declaración de Intenciones y Objetivo 

El objetivo principal de esta aplicación será permitir un **registro claro de ingresos (entradas) y gastos (salidas)**, ofreciendo opciones para consultarlos y generar reportes. 

La idea es contar con una perspectiva general de las finanzas personales que ayude a tomar decisiones oportunas y bien fundamentadas. Dado que el programa se encuentra actualmente en **fase de desarrollo**, este documento actúa como una guía de lo que será la aplicación y hacia dónde se dirigen sus funcionalidades. 

## Funcionalidades Planeadas 

La herramienta estará organizada en áreas clave para facilitar tanto el día a día como el análisis de datos: 

### 1. Módulo de Gestiones 

Se encargará de la administración diaria de las transacciones: 

- **Añadir:** Registro de nuevas entradas, salidas y movimientos de tipo recurrente.
- **Modificar:** Edición de registros guardados, capturando la razón o motivo del cambio.
- **Borrar:** Eliminación de movimientos.
- **Tipos de Movimientos:** Control separado para *Entradas*, *Salidas* y *Recurrencias*.

### 2. Módulo de Reportes 

Permitirá generar diversos tipos de informes con distintos alcances y enfoques, según lo que se busque analizar en cada momento: 

- **Reporte Total:** Visión general e integral del estado financiero.
- **Reporte Mensual:** Control y seguimiento periódico por meses.
- **Reporte Estadístico:** Análisis de tendencias para entender mejor los patrones de gasto e ingreso.
- **Filtros por Tipo:** Búsquedas específicas enfocadas en *Entradas*, *Salidas* o *Recurrencias*.

### 3. Módulo de Persistencia

Destinado a almacenar toda la información persistente. 

El programa tiene destinado ofrecer las opciones de modificación y borrado. Pero ningún dato debería eliminarse.

En su lugar, solamente dejarán de estar accesibles desde la interfáz principal con una única opción destinada a recuperar la información. (tengo algunas ideas, pero todavía no lo he decidido) 

--- 
## Estructura del Proyecto

Esta es la organización general prevista para el código, manteniendo separadas la lógica de ejecución, la interfaz de usuario, la persistencia de datos y las pruebas: 

```text
main/
  |- main.py
  |- interfaz_cli.py
persistencia/
  |- movimientos_entrada.json
  |- movimientos_salida.json
  |- movimientos_modificados.json
  |- movimientos_borrados.json
testing/
  |- unit_tests/
  |- integration_tests/
  |- e2e_tests/
docs/
  |- ...

```
