# Actividades del apartado: Fraudes e ingeniería social

En este apartado se proponen una serie de **actividades prácticas y de análisis** orientadas a identificar fraudes informáticos y comprender cómo las técnicas de ingeniería social pueden comprometer la privacidad y la seguridad de la información.

Las actividades se centran en el análisis de mensajes fraudulentos, el uso de herramientas de protección, la importancia de la autenticación multifactor y la concienciación sobre los factores humanos y físicos que influyen en la seguridad de una red.

!!! danger "Peligro"
    No interactuar con correos o enlaces reales sospechosos.

---

## Actividad 1: Análisis técnico de un correo de phishing

**Objetivo**  
Aprender a identificar evidencias de suplantación de identidad en el contenido y los metadatos visibles de un correo electrónico fraudulento.

**Descripción**  
El alumno analizará un ejemplo real de correo de phishing, mediante una captura detallada, con el fin de detectar señales de alarma sin interactuar con el contenido malicioso.

**Tareas a realizar**  
- Analizar la dirección del remitente del mensaje y comprobar si el nombre mostrado coincide con la dirección de correo real.  
- Situar el cursor sobre los enlaces o botones del mensaje, sin hacer clic, y observar la URL de destino mostrada en la barra de estado del navegador o del cliente de correo.  
- Revisar el contenido general del mensaje en busca de errores ortográficos, tono urgente o solicitudes inusuales.

**Cuestión de análisis**  
- Redacta un breve informe identificando **al menos tres señales de alarma** detectadas en el mensaje y explica por qué son indicativas de un intento de phishing.

---

## Actividad 2: Investigación de URLs y smishing

**Objetivo**  
Utilizar herramientas de protección para analizar enlaces sospechosos recibidos por SMS sin poner en riesgo el dispositivo.

**Descripción**  
El alumno estudiará un caso simulado de smishing en el que se emplea un enlace acortado para ocultar el destino real.

**Tareas a realizar**  
- Analizar un enlace acortado, similar a `bit.ly/3xYz123`.  
- Utilizar una herramienta de expansión de URLs o análisis de reputación, como **ExpandURL** o **VirusTotal**, para identificar el destino real del enlace.  

**Cuestión de análisis**  
- Indica a qué dirección web intentaba redirigir el enlace.  
- Explica por qué los atacantes utilizan acortadores de URL en campañas de smishing dirigidas a dispositivos móviles.

---

## Actividad 3: La barrera del MFA (doble factor de autenticación)

**Objetivo**  
Comprender cómo la autenticación multifactor (MFA) protege una cuenta incluso cuando las credenciales han sido obtenidas mediante ingeniería social.

**Descripción**  
El alumno investigará las opciones de seguridad disponibles en servicios habituales para analizar el funcionamiento del doble factor de autenticación.
No desactivar el segundo factor tras finalizar la práctica.

**Tareas a realizar**  
- Acceder a los ajustes de seguridad de una cuenta de uso común (Google, Microsoft, redes sociales u otra plataforma similar).  
- Localizar la opción de **Autenticación en dos pasos** o **MFA**.  
- Identificar al menos tres métodos distintos de segundo factor, como SMS, aplicación de autenticación o llave física USB.

**Cuestión de análisis**  
- Supón que un usuario ha facilitado su nombre de usuario y contraseña tras caer en un engaño de phishing.  
- Explica detalladamente cómo la activación del MFA impediría que el atacante accediera a la cuenta.

---

## Actividad 4: Auditoría de seguridad física y humana

**Objetivo**  
Identificar comportamientos inseguros y fallos de seguridad física que pueden facilitar el acceso no autorizado a una red local.

**Descripción**  
El alumno realizará una observación del entorno de trabajo para detectar prácticas inseguras relacionadas con la gestión de accesos y la protección de la información.

**Tareas a realizar**  
- Realizar una inspección visual del propio puesto de trabajo y de los puestos cercanos, sin manipular equipos ni información ajena.  
- Observar la existencia de contraseñas anotadas, sesiones abiertas sin supervisión o puertos de red accesibles sin control.

**Cuestión de análisis**  
- Basándote en el concepto de **confianza excesiva**, propone dos comportamientos seguros que ayudarían a evitar que un intruso obtuviera acceso a la red local simulando ser personal autorizado.

---

## Consideraciones finales

Estas actividades permiten comprender que la mayoría de los fraudes informáticos se apoyan en el engaño al usuario y en fallos de comportamiento, y ponen de manifiesto la importancia de combinar medidas técnicas y humanas para proteger la privacidad y la seguridad de la información.
