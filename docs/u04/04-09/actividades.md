# Actividades del apartado: Cortafuegos

En este apartado se proponen una serie de **actividades prácticas y de análisis** orientadas a comprender el funcionamiento de los cortafuegos y su papel fundamental en la protección de los sistemas y de la privacidad de la información transmitida en redes informáticas.

Las actividades abarcan el uso de cortafuegos en sistemas operativos y en dispositivos de red, así como el análisis del control del tráfico entrante y saliente desde una perspectiva defensiva.

!!! warning "Uso responsable"
    Las pruebas de cortafuegos y escaneos de puertos deben realizarse únicamente en entornos de prácticas y con autorización expresa.


---

## Actividad 1: Auditoría de reglas del cortafuegos en Windows

**Objetivo**  
Identificar cómo el sistema operativo protege los servicios locales mediante reglas de cortafuegos en función del perfil de red utilizado.

**Descripción**  
El alumno analizará las reglas existentes del cortafuegos de Windows y comprobará cómo afectan a la visibilidad del equipo dentro de la red.

**Tareas a realizar**  
- Abrir el **Firewall de Windows con seguridad avanzada**.  
- Acceder al apartado de **Reglas de entrada**.  
- Localizar la regla que permite el tráfico del protocolo **ICMPv4 (Ping)**.  
- Comprobar en qué perfiles de red está habilitada la regla (Dominio, Privado y Público).  
- Desactivar temporalmente la regla y solicitar a un compañero que realice un `ping` a la dirección IP del equipo.  
- Volver a activar la regla al finalizar la prueba.

**Cuestión de análisis**  
- ¿Qué ocurre cuando la regla ICMP está desactivada?  
- Explica cómo el uso de perfiles de red permite aplicar políticas de seguridad diferentes según el entorno de conexión.

---

## Actividad 2: Configuración de filtrado en Linux con Gufw

**Objetivo**  
Aplicar el principio de **denegación por defecto** en un sistema Linux mediante un cortafuegos sencillo de administrar.

**Descripción**  
El alumno configurará el cortafuegos Gufw para controlar el tráfico entrante y saliente, permitiendo únicamente los servicios necesarios.
No escanear equipos fuera del entorno de prácticas.

**Tareas a realizar**  
- Instalar e iniciar la herramienta **Gufw** en un sistema Linux.  
- Configurar la política inicial como: **Tráfico entrante: Denegar** / **Tráfico saliente: Permitir**.  
- Crear una regla específica que permita únicamente el tráfico entrante al puerto **80 (HTTP)**.  
- Desde otro equipo de la red, realizar un escaneo de puertos utilizando **Nmap** hacia la dirección IP del sistema protegido.

**Cuestión de análisis**  
- ¿Qué puertos aparecen como **open** y cuáles como **filtered** en el resultado del escaneo?  
- Explica la diferencia entre ambos estados y cómo el cortafuegos influye en ellos.

---

## Actividad 3: Análisis de la DMZ y la redirección de puertos en el router

**Objetivo**  
Comprender los riesgos asociados a la exposición de servicios internos a Internet y la importancia de reducir la superficie de ataque.

**Descripción**  
El alumno analizará, mediante simulación o entorno de prácticas, la configuración de redirección de puertos y su relación con el concepto de DMZ.
No realizar estas configuraciones en routers domésticos reales.”

**Tareas a realizar**  
- Utilizar un simulador de red o la interfaz de configuración de un router de prácticas.  
- Configurar una regla de **Port Forwarding** para redirigir el tráfico externo del puerto **8080** al puerto **80** de un servidor web interno.  
- Analizar la exposición del servicio tras aplicar la configuración.

**Cuestión de análisis**  
- Basándote en el concepto de **DMZ**, explica por qué es más seguro exponer únicamente puertos concretos mediante redirección que situar un servidor directamente en la DMZ.  
- Relaciona tu respuesta con la reducción de la superficie de ataque.

---

## Actividad 4: Control del tráfico saliente y privacidad

**Objetivo**  
Utilizar el cortafuegos como herramienta para mejorar la privacidad del usuario controlando el tráfico saliente de las aplicaciones.

**Descripción**  
El alumno configurará reglas de salida para impedir que determinadas aplicaciones o servicios envíen información sin el conocimiento del usuario.

**Tareas a realizar**  
- Crear una regla de **tráfico saliente (Outbound)** en el cortafuegos del sistema operativo utilizado (Windows o Linux).  
- Bloquear el acceso a una dirección IP o dominio concreto correspondiente a un servicio conocido.  
- Intentar acceder a dicho servicio desde el navegador u otra aplicación.

**Cuestión de análisis**  
- ¿Qué comportamiento se observa al intentar acceder al servicio bloqueado?  
- Explica cómo el control del tráfico saliente contribuye a mejorar la privacidad del usuario frente al rastreo y la telemetría.

---

## Consideraciones finales

Estas actividades permiten comprender el funcionamiento práctico de los cortafuegos y su papel esencial en la protección de los sistemas, la reducción de la superficie de ataque y la mejora de la privacidad de la información transmitida en redes informáticas.
