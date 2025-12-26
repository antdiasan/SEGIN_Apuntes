# Actividades del apartado: Seguridad y privacidad en redes inalámbricas

En este apartado se proponen una serie de **actividades prácticas y de análisis** orientadas a comprender los riesgos de privacidad presentes en las redes inalámbricas y las medidas de protección que pueden aplicarse para asegurar la información transmitida.

Las actividades se centran en el análisis del entorno, el bastionado de puntos de acceso y el uso de mecanismos de protección adicionales en redes públicas, evitando prácticas ofensivas y priorizando un enfoque preventivo y defensivo.

!!! warning "Uso responsable"
    Las herramientas de análisis inalámbrico y captura de tráfico deben utilizarse únicamente en entornos autorizados y con fines educativos.


---

## Actividad 1: Auditoría y clasificación de señales inalámbricas

**Objetivo**  
Identificar y valorar el nivel de seguridad de las redes inalámbricas presentes en el entorno, analizando la información que puede obtenerse sin necesidad de establecer conexión.

**Descripción**  
El alumno utilizará una herramienta de análisis de redes WiFi para detectar redes cercanas y evaluar sus características básicas de seguridad.

**Tareas a realizar**  
- Utilizar una herramienta de análisis inalámbrico, como **Acrylic WiFi** en Windows o **LinSSID** en Linux.  
- Realizar un escaneo de al menos dos minutos.  
- Localizar un mínimo de cinco redes inalámbricas distintas.

**Cuestión de análisis**  
- Elabora una tabla con los siguientes campos: SSID, canal, RSSI (potencia de señal) y estándar de seguridad (WPA2, WPA3, red abierta, etc.).  
- Basándote en los casos prácticos trabajados, indica qué redes permiten identificar el modelo o el proveedor del router a partir del SSID y explica por qué esto supone un riesgo para la seguridad.

---

## Actividad 2: Bastionado de un punto de acceso inalámbrico

**Objetivo**  
Aplicar configuraciones básicas de seguridad en un punto de acceso inalámbrico para mitigar los riesgos detectados en redes WiFi.

**Descripción**  
El alumno accederá a la interfaz de configuración de un router inalámbrico real o a un simulador para aplicar medidas de bastionado habituales.

**Tareas a realizar**  
- Acceder a la interfaz de administración de un router inalámbrico del taller o a un simulador.  
- Modificar el nombre de la red (SSID) por uno genérico que no aporte información sobre el dispositivo o la organización.  
- Configurar el cifrado **WPA2-AES** o **WPA3**, utilizando una contraseña robusta.  
- Desactivar la funcionalidad **WPS** del punto de acceso.

**Cuestión de análisis**  
- Explica por qué la desactivación de WPS es una medida crítica de seguridad, incluso cuando se utiliza una contraseña WPA2 o WPA3 de gran complejidad.

---

## Actividad 3: Análisis de hotspots y uso de VPN

**Objetivo**  
Comprender cómo el uso de redes públicas puede comprometer la privacidad de las comunicaciones y cómo una VPN permite mitigar estos riesgos.

**Descripción**  
El alumno analizará el tráfico de red generado al navegar por una red inalámbrica abierta y comparará los resultados con el uso de una VPN.
No capturar tráfico de terceros sin autorización.

**Tareas a realizar**  
- Conectarse a una red inalámbrica abierta o a un hotspot creado específicamente para la prueba.  
- Iniciar una captura de tráfico con **Wireshark**.  
- Acceder a una página web HTTP de pruebas, sin utilizar credenciales reales.  
- Activar una VPN (gratuita o de prueba) y repetir la captura de tráfico.

**Cuestión de análisis**  
- Compara ambas capturas y describe los cambios observados en los protocolos utilizados y en la legibilidad de los datos.  
- Explica cómo el uso de una VPN soluciona los riesgos de privacidad asociados a las redes públicas.

---

## Actividad 4: Simulación de segmentación inalámbrica mediante red de invitados

**Objetivo**  
Aplicar mecanismos de separación entre usuarios para proteger la privacidad en entornos educativos y redes compartidas.

**Descripción**  
El alumno configurará una red de invitados en un router inalámbrico y comprobará el aislamiento entre dicha red y la red principal.

**Tareas a realizar**  
- Configurar una **Red de Invitados (Guest Network)** en el router, si el dispositivo lo permite.  
- Conectar un equipo a la red principal y otro a la red de invitados.  
- Intentar establecer comunicación entre ambos equipos mediante `ping`.

**Cuestión de análisis**  
- ¿Existe comunicación entre los equipos conectados a redes distintas?  
- Explica cómo la red de invitados resuelve los problemas de privacidad planteados en entornos como centros educativos.

---

## Consideraciones finales

Estas actividades permiten analizar redes inalámbricas desde una perspectiva defensiva, aplicando medidas reales de protección y comprendiendo los riesgos asociados al uso de redes WiFi, especialmente en entornos públicos o compartidos.
