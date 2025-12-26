# Actividades del apartado: Integración de medidas de seguridad

En este apartado se proponen una serie de **actividades de síntesis e integración** cuyo objetivo es aplicar de forma conjunta las distintas medidas de seguridad y privacidad estudiadas a lo largo de la unidad.

Las actividades planteadas permiten al alumnado adoptar una visión global de la seguridad de la información, comprendiendo que la protección efectiva de las comunicaciones no depende de una única medida, sino de la correcta combinación de controles técnicos y humanos bajo el principio de **defensa en profundidad**.

---

## Actividad 1: Diseño de una arquitectura perimetral segura

**Objetivo**  
Aplicar el concepto de seguridad en capas para proteger una red local frente a amenazas externas.

**Descripción**  
El alumno deberá diseñar el esquema lógico de una red para una pequeña oficina técnica, integrando diferentes medidas de seguridad perimetral.

**Escenario de partida**  
La red dispone de los siguientes elementos:
- Un router de fibra para la salida a Internet.  
- Un servidor de datos interno que almacena información sensible.  
- Un servidor web que debe ser accesible desde el exterior.  
- Diez puestos de trabajo para empleados.

**Tareas a realizar**  
- Utilizar una herramienta de diagramación técnica (Draw.io, Lucidchart o similar) para representar la infraestructura de red.  
- Diseñar una **DMZ (Zona Desmilitarizada)** destinada al servidor web.  
- Incorporar un **cortafuegos** que filtre el tráfico entrante y saliente.  
- Añadir un **proxy** para gestionar y controlar las conexiones de los empleados hacia Internet.

**Cuestión de análisis**  
- Justifica por qué resulta más seguro situar el servidor web en una DMZ en lugar de conectarlo directamente a la red interna de los empleados.

---

## Actividad 2: Simulación de auditoría e identificación de brechas

**Objetivo**  
Evaluar una red para detectar fallos de integración entre medidas técnicas y de privacidad.

**Descripción**  
El alumno realizará una simulación de auditoría básica aplicando medidas de bastionado y analizando su impacto en la seguridad.
Realizar los escaneos únicamente sobre equipos autorizados.

**Tareas a realizar**  
- Ejecutar un escaneo de puertos con **Nmap** o **Zenmap** contra el propio equipo o un servidor de pruebas del aula.  
- Aplicar una regla en el cortafuegos local que permita únicamente el acceso al servicio **HTTP (puerto 80)**.  
- Bloquear cualquier otro tipo de tráfico entrante.

**Cuestión de análisis**  
- Explica cómo esta medida técnica basada en el cortafuegos se complementa con una medida de privacidad como el uso de un proxy para que el administrador tenga control sobre lo que entra y sale de la organización.

---

## Actividad 3: Plan de integración de seguridad y privacidad

**Objetivo**  
Proponer una solución integral de seguridad para un entorno de red con carencias de protección.

**Descripción**  
El alumno analizará un escenario realista y elaborará un plan de mejora aplicando los conocimientos adquiridos en la unidad.

**Escenario**  
Una gestoría trabaja con datos muy sensibles de sus clientes. Actualmente:  
- Utilizan únicamente un router doméstico.  
- No emplean VPN para el teletrabajo.  
- Los empleados comparten contraseñas a través de aplicaciones de mensajería instantánea.

**Tareas a realizar**  
Redactar un **Plan de Integración de Seguridad y Privacidad** que incluya al menos:  
- Una medida de **criptografía o identificación** (por ejemplo, certificados digitales o MFA).  
- Una medida de **seguridad en red** (VPN, cortafuegos, segmentación).  
- Una medida de **privacidad en la navegación** (proxy, filtrado web).  
- Una medida de **control humano y organizativo** (protocolos de comportamiento y buenas prácticas).

**Cuestión de análisis**  
- Basándote en el principio de **seguridad en capas**, explica por qué la instalación de un antivirus en los equipos no es suficiente para proteger la privacidad de las comunicaciones de esta empresa.

---

## Consideraciones finales

Estas actividades permiten consolidar una visión integral de la seguridad de la información, reforzando la idea de que la protección de la privacidad y de las comunicaciones requiere la correcta combinación de medidas técnicas, organizativas y humanas.
