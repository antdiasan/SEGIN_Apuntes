# Actividades del apartado: VPN y redes públicas

En este apartado se proponen una serie de **actividades prácticas y de análisis** orientadas a comprender cómo las redes públicas pueden comprometer la privacidad de las comunicaciones y de qué forma el uso de redes privadas virtuales (VPN) permite mitigar estos riesgos.

Las actividades se centran en la observación de la visibilidad de los servicios, la configuración de clientes VPN en los sistemas operativos y el análisis reflexivo de escenarios reales de uso en redes no confiables.

!!! warning "Uso responsable"
    Las actividades con VPN deben realizarse únicamente con servicios de prueba y sin introducir credenciales personales ni datos sensibles.


---

## Actividad 1: Auditoría de visibilidad con y sin VPN

**Objetivo**  
Comprobar cómo el uso de una VPN modifica la visibilidad de nuestro equipo y del tráfico generado cuando se utiliza una red inalámbrica compartida.

**Descripción**  
El alumno analizará la información que puede obtenerse desde la red local sobre su propio equipo antes y después de establecer una conexión VPN, observando los cambios en la topología de red y en la exposición de los servicios.

**Tareas a realizar**  
- Conectarse a la red WiFi del aula o a una red inalámbrica compartida.  
- Utilizar **Zenmap** y realizar un escaneo de tipo *Intense Scan* hacia la propia dirección IP asignada en la red local.  
- Anotar los puertos y servicios detectados durante el escaneo.  
- Establecer una conexión VPN utilizando un servicio corporativo, educativo o de confianza.  
- Repetir el escaneo una vez activa la VPN.

**Cuestión de análisis**  
- ¿Qué diferencias se observan en la información obtenida por Zenmap antes y después de activar la VPN?  
- Explica cómo el uso de un túnel cifrado y el cambio de ruta del tráfico ayudan a reducir la visibilidad de los servicios del equipo frente a otros usuarios conectados al mismo hotspot.

---

## Actividad 2: Configuración de un cliente VPN en el sistema operativo

**Objetivo**  
Utilizar el soporte nativo del sistema operativo para establecer una conexión segura mediante VPN.

**Descripción**  
El alumno configurará una conexión VPN empleando las herramientas integradas en Windows o Linux, sin necesidad de instalar software adicional.
Utilizar solo servicios VPN de prueba y nunca introducir datos personales.

**Tareas a realizar**  
- En Windows, acceder a **Configuración > Red e Internet > VPN** y añadir una nueva conexión de prueba, utilizando los datos de un servidor público gratuito (como VPNBook). Investiga en su web la dirección del servidor, el usuario y la contraseña vigentes.
- En Linux, utilizar el gestor de redes (**NetworkManager**) para importar un archivo de configuración `.ovpn` descargado desde un servicio VPN gratuito de tu elección.  
- Establecer la conexión VPN y comprobar que se ha realizado correctamente.

**Cuestión de análisis**  
- Una vez conectado a la VPN, ejecutar el comando `curl ifconfig.me` desde una terminal.  
- ¿Coincide la dirección IP pública obtenida con la del centro educativo?  
- Explica qué ha ocurrido con el enrutamiento del tráfico al establecer la conexión VPN.

---

## Actividad 3: Análisis de riesgos en redes públicas

**Objetivo**  
Valorar críticamente los riesgos asociados al uso de redes públicas y la importancia de aplicar medidas de protección adicionales.

**Descripción**  
El alumno analizará un escenario realista de uso de una red pública y reflexionará sobre las posibles consecuencias para la privacidad de la información transmitida.

**Tareas a realizar**  
- Analizar el siguiente escenario:  
  *Un usuario se conecta a la red WiFi de un hotel y acepta las condiciones de un portal cautivo para navegar gratuitamente.*  
- Reflexionar sobre el uso de servicios sensibles en este tipo de redes, como la banca electrónica o el acceso a información personal.

**Cuestión de análisis**  
- Explica, paso a paso, qué ocurre con los datos del usuario si realiza una transferencia bancaria sin utilizar una VPN.  
- Indica en qué tramo o salto de la red es más probable que se produzca una interceptación del tráfico y por qué.

---

## Consideraciones finales

Estas actividades permiten comprender la importancia del uso de VPN en redes públicas y compartidas, así como los riesgos reales asociados a la transmisión de información sensible sin medidas adecuadas de protección.
