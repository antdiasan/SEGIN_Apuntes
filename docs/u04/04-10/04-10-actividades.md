# Actividades del apartado: Proxys

En este apartado se proponen una serie de **actividades prácticas y de análisis** orientadas a comprender el funcionamiento de los servidores proxy, su papel como intermediarios en las comunicaciones y su impacto tanto en la seguridad como en la privacidad de los usuarios.

Las actividades se centran en la observación del flujo de tráfico, el análisis de la capacidad de monitorización de los proxys y su uso como herramienta de filtrado y protección frente a amenazas como el phishing.


---

## Actividad 1: Configuración manual de un proxy en el navegador

**Objetivo**  
Comprender cómo se modifica el flujo de tráfico cuando se utiliza un servidor proxy como intermediario en la comunicación.

**Descripción**  
El alumno configurará manualmente un proxy en el navegador y observará los efectos que tiene sobre la navegación y la dirección IP visible desde Internet.
No introducir credenciales personales ni datos sensibles.

**Tareas a realizar**  
- Localizar en Internet un listado de **proxys públicos gratuitos** que utilicen puertos habituales como el 8080.  
- Acceder a la configuración de red del navegador e introducir la dirección IP y el puerto del proxy seleccionado.  
- Intentar acceder a distintos sitios web y comprobar el funcionamiento de la navegación.

**Cuestión de análisis**  
- ¿Se aprecia alguna diferencia en la velocidad de carga de las páginas?  
- Al acceder a un servicio del tipo “¿Cuál es mi IP?”, ¿qué dirección IP aparece: la del centro educativo o la del proxy?  
- Explica qué papel desempeña el proxy en esta comunicación.

---

## Actividad 2: Auditoría de registros (logs) y privacidad

**Objetivo**  
Valorar la capacidad de monitorización de un servidor proxy y sus implicaciones para la protección de los datos personales.

**Descripción**  
El alumno analizará, a partir de un escenario teórico, la información que puede registrar un proxy sobre la actividad de los usuarios.

**Tareas a realizar**  
- Analizar el siguiente escenario:  
  *Un administrador de un servidor proxy puede visualizar en tiempo real qué usuarios acceden a qué páginas web y en qué momento.*  
- Reflexionar sobre la diferencia entre la información visible para un proxy y la que registra un cortafuegos tradicional.

**Cuestión de análisis**  
- Explica por qué el uso de un proxy puede suponer un conflicto con la protección de datos personales si no se informa adecuadamente a los usuarios.  
- Indica qué tipo de información puede registrar un proxy que no sería visible para un cortafuegos simple.

---

## Actividad 3: Análisis de un proxy transparente

**Objetivo**  
Identificar el funcionamiento de los proxys transparentes y comprender sus ventajas en redes de gran tamaño.

**Descripción**  
El alumno analizará el recorrido del tráfico de red para detectar la posible existencia de un proxy que no requiere configuración explícita en el cliente.
La presencia de un salto intermedio no garantiza siempre un proxy.

**Tareas a realizar**  
- Abrir una consola de comandos en el sistema operativo.  
- Ejecutar el comando `tracert google.es` en Windows o `traceroute google.es` en Linux.  
- Observar los primeros saltos del recorrido del tráfico tras el router de salida.

**Cuestión de análisis**  
- Si el equipo no tiene configurado ningún proxy de forma manual pero el tráfico es interceptado por uno situado en el gateway, ¿cómo se denomina técnicamente este tipo de proxy?  
- Explica qué ventajas ofrece este tipo de proxy para un técnico de SMR a la hora de desplegarlo en una red con un elevado número de usuarios.

---

## Actividad 4: Simulación de filtrado contra phishing mediante proxy

**Objetivo**  
Evaluar la eficacia del proxy como barrera de seguridad frente a intentos de acceso a sitios web maliciosos.

**Descripción**  
El alumno analizará el funcionamiento del filtrado web basado en proxy como medida preventiva frente al phishing.

**Tareas a realizar**  
- Investigar el funcionamiento de una herramienta de filtrado basada en proxy, como **SquidGuard**, o de extensiones de filtrado web utilizadas habitualmente.  
- Analizar cómo actúan estas herramientas cuando un usuario intenta acceder a una dirección incluida en una lista negra.

**Cuestión de análisis**  
- Supón que un usuario recibe un correo de phishing con un enlace a una web maliciosa incluida en las listas negras del proxy.  
- Explica qué vería el usuario al intentar acceder al enlace y por qué este tipo de medida resulta más eficaz que confiar únicamente en la atención del usuario.

---

## Consideraciones finales

Estas actividades permiten comprender el papel de los proxys como intermediarios en las comunicaciones, su utilidad como herramienta de filtrado y monitorización y la necesidad de equilibrar seguridad y privacidad en entornos educativos y corporativos.
