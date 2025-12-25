# Actividades del apartado: Seguridad y privacidad en redes cableadas

En este apartado se proponen una serie de **actividades prácticas y de análisis** orientadas a comprender los riesgos de privacidad presentes en las redes cableadas y las medidas técnicas que pueden aplicarse para minimizar la monitorización y el acceso no autorizado a la información.

Las actividades combinan el uso de herramientas de diagnóstico habituales con la reflexión sobre ataques reales y mecanismos de protección utilizados en redes locales.

!!! warning "Uso responsable"
    Las herramientas de análisis de red deben utilizarse únicamente sobre redes y equipos autorizados y con fines educativos.


---

## Actividad 1: Análisis de la tabla ARP y visibilidad en la red local

**Objetivo**  
Comprender la relación entre direcciones IP y direcciones MAC en una red cableada, así como los riesgos asociados a la falta de mecanismos de autenticación en el protocolo ARP.

**Descripción**  
El alumno analizará la tabla ARP de su equipo antes y después de generar tráfico en la red local, observando cómo se registran las asociaciones IP–MAC de los dispositivos con los que se comunica.
No realizar capturas de tráfico de terceros.

**Tareas a realizar**  
- Abrir una terminal y ejecutar el comando `arp -a` para visualizar la tabla ARP actual.  
- Utilizar la herramienta **Nmap** para realizar un escaneo de la red local mediante el comando `nmap -sn 192.168.1.0/24`, ajustando el rango a la red correspondiente.  
- Volver a ejecutar el comando `arp -a` tras el escaneo y observar los cambios producidos.

**Cuestión de análisis**  
- ¿Qué información nueva aparece en la tabla ARP después del escaneo?  
- Explica por qué el conocimiento de las direcciones MAC de los dispositivos de la red constituye el primer paso para un ataque de **MAC Spoofing** y por qué el protocolo ARP no permite verificar la autenticidad de dichas asociaciones.

---

## Actividad 2: Identificación del servidor DHCP legítimo

**Objetivo**  
Detectar posibles riesgos asociados a la asignación automática de parámetros de red y comprender las consecuencias de un ataque de tipo **Rogue DHCP**.

**Descripción**  
El alumno identificará el servidor DHCP que le asigna la configuración de red y verificará si corresponde con el dispositivo legítimo esperado en el entorno de la red.

**Tareas a realizar**  
- En un sistema Windows, ejecutar el comando `ipconfig /all` y localizar el apartado correspondiente al **Servidor DHCP**.  
- En un sistema Linux, utilizar el comando `nmcli device show` o revisar los registros del sistema para identificar el servidor DHCP.  
- Comprobar que la dirección IP del servidor DHCP coincide con la del router o servidor oficial del aula o del entorno de prácticas.

**Cuestión de análisis**  
- ¿Qué riesgos para la privacidad y la seguridad supondría que un servidor DHCP falso asignara una dirección IP, una puerta de enlace y servidores DNS controlados por un atacante?  
- Explica cómo este tipo de ataque puede facilitar la monitorización o manipulación del tráfico de red.

---

## Actividad 3: Diseño de segmentación mediante VLANs (simulación)

**Objetivo**  
Aplicar medidas de segmentación lógica para evitar la monitorización y el acceso a la información entre distintos grupos de usuarios dentro de una red cableada.

**Descripción**  
El alumno diseñará una red segmentada mediante VLANs utilizando un simulador de redes, comprobando el aislamiento entre dispositivos pertenecientes a distintas VLANs.

**Tareas a realizar**  
- Utilizar un simulador de redes, como **Packet Tracer**, para diseñar una red compuesta por un switch y cuatro equipos.  
- Configurar dos VLANs bajo el estándar **802.1Q**:  *VLAN 10: Administración y *VLAN 20: Alumnos  
- Asignar dos equipos a cada VLAN.  
- No configurar ningún dispositivo de enrutamiento entre las VLANs.  
- Intentar realizar una comunicación mediante `ping` entre un equipo de la VLAN de Administración y uno de la VLAN de Alumnos.

**Cuestión de análisis**  
- ¿Existe comunicación entre los equipos de distintas VLANs?  
- Explica cómo la segmentación mediante VLANs contribuye a proteger la información sensible y a evitar la monitorización entre usuarios de diferentes secciones de la red.

---

## Consideraciones finales

Estas actividades permiten identificar riesgos reales presentes en redes cableadas y comprender la importancia de aplicar medidas de segmentación y control para proteger la privacidad de la información transmitida en redes locales.


!!! success "Objetivo alcanzado"
    Si comprendes cómo ARP, DHCP, subredes y VLAN influyen en la privacidad, has entendido los riesgos reales de una red cableada.
