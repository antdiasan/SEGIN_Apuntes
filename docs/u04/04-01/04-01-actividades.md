# Actividades del apartado: Introducción a la privacidad y seguridad en redes

En este apartado se proponen una serie de **actividades prácticas y de análisis** orientadas a que el alumno comprenda la importancia de la privacidad y la seguridad en redes informáticas desde un punto de vista técnico y aplicado.

Las actividades están centradas en la identificación de servicios, el análisis de protocolos y la verificación de la integridad de la información, fomentando una actitud crítica frente a los riesgos existentes en redes locales.


!!! warning "Uso responsable de herramientas"
    Las herramientas de escaneo y captura de tráfico deben utilizarse únicamente sobre equipos y redes autorizadas y con fines educativos.


---

## Actividad 1: Auditoría de servicios locales

**Objetivo**  
Identificar los servicios activos en el propio equipo del alumno y reflexionar sobre la necesidad de los mismos desde el punto de vista de la seguridad de la información.

**Descripción**  
El alumno realizará una auditoría básica de los servicios y puertos en escucha en su propio sistema, con el fin de detectar posibles servicios innecesarios que aumenten la superficie de ataque.

**Tareas a realizar**  
- Ejecutar el comando `netstat -ant` para listar los puertos en escucha. No siempre muestra procesos, se puede utilizar como alternativa `netstat -ano` y en Linux `ss -lntup`
- Identificar al menos tres puertos abiertos e investigar a qué servicio corresponden.  
- Reflexionar sobre si alguno de los servicios detectados podría desactivarse para mejorar la seguridad del sistema.

---

## Actividad 2: Descubrimiento de red con Nmap

**Objetivo**  
Aprender a inventariar una red local identificando dispositivos, servicios y posibles puntos de exposición desde el punto de vista de la seguridad.

**Descripción**  
El alumno utilizará la herramienta Nmap para realizar un descubrimiento básico de una red local y analizar los servicios ofrecidos por uno de los dispositivos detectados.

**Tareas a realizar**  
- Ejecutar un escaneo de red mediante el comando `nmap -sP 192.168.1.0/24`.  
- Elegir una dirección IP detectada y ejecutar `nmap -sV IP_objetivo`.  
- Elaborar una tabla con la información obtenida: dirección IP, sistema operativo estimado, puertos abiertos y servicios asociados.

---

## Actividad 3: Análisis de protocolos y privacidad

**Objetivo**  
Diferenciar protocolos seguros e inseguros mediante el análisis del tráfico de red, relacionando su uso con la privacidad y la integridad de la información.

**Descripción**  
El alumno capturará tráfico de red utilizando Wireshark para analizar las diferencias entre una comunicación HTTP y una comunicación HTTPS.
La captura se realizará únicamente sobre tráfico propio.vamo

**Tareas a realizar**  
- Realizar una captura de tráfico con Wireshark.  
- Acceder a una página web HTTP utilizando credenciales ficticias.  
- Acceder a una página web HTTPS.  
- Comparar la información capturada en ambos casos y extraer conclusiones sobre la privacidad de las comunicaciones.

---

## Actividad 4: Verificación de integridad mediante funciones hash

**Objetivo**  
Comprender cómo los algoritmos hash permiten detectar la alteración de la información y garantizar su integridad.

**Descripción**  
El alumno aplicará una función hash a un archivo y comprobará cómo una pequeña modificación en el contenido produce un resultado completamente distinto.

**Tareas a realizar**  
- Crear un archivo denominado `mensaje.txt`.  
- Calcular su valor hash utilizando `sha256sum` o `Get-FileHash`.  
- Modificar el contenido del archivo y recalcular el hash.  
- Comparar los resultados obtenidos y extraer conclusiones sobre la integridad de la información.

---

## Consideraciones finales

Estas actividades permiten al alumno identificar riesgos reales en redes locales, analizar el uso de protocolos seguros y comprender la importancia de la integridad de la información como pilar fundamental de la seguridad en redes.
