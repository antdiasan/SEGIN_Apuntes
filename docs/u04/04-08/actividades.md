# Actividades del apartado: Publicidad, rastreadores y spam

En este apartado se proponen una serie de **actividades prácticas y de análisis** orientadas a comprender cómo la publicidad, los rastreadores y el correo no deseado afectan a la privacidad del usuario y al volumen de tráfico generado en las redes.

Las actividades se centran en la observación del comportamiento real de los navegadores y clientes de correo, el análisis técnico de mensajes no deseados y la aplicación de medidas básicas de filtrado y control, fomentando la autonomía del alumnado.

!!! danger "Entornos Controlados"
    No interactuar con enlaces ni adjuntos reales fuera de entornos controlados.

---

## Actividad 1: Auditoría de rastreadores durante la navegación

**Objetivo**  
Identificar los servicios y empresas de terceros que monitorizan la actividad de navegación del usuario en tiempo real.

**Descripción**  
El alumno analizará el número de rastreadores activos que intervienen durante la navegación por distintos sitios web, utilizando extensiones de análisis específicas del navegador.

**Tareas a realizar**  
- Instalar en el navegador una extensión de análisis de rastreadores, como **Lightbeam** o **Ghostery**.  
- Navegar durante al menos cinco minutos por tres portales diferentes, como medios de comunicación digitales o redes sociales.  
- Observar el gráfico o listado de conexiones generado por la extensión.

**Cuestión de análisis**  
- Muestra el gráfico o listado de rastreadores detectados.  
- Indica cuántas empresas de terceros han registrado la actividad de navegación y reflexiona sobre a cuántas de ellas se ha otorgado un permiso explícito por parte del usuario.

---

## Actividad 2: Análisis de cabeceras de correos no deseados

**Objetivo**  
Investigar el origen técnico de un mensaje de correo no deseado mediante el análisis de sus cabeceras.

**Descripción**  
El alumno examinará las cabeceras completas de un mensaje clasificado como spam para identificar el servidor de origen y comprobar si existe coherencia con la identidad declarada del remitente.

**Tareas a realizar**  
- Acceder a un mensaje situado en la carpeta de **Spam** del cliente de correo.  
- Seleccionar la opción **Ver original**, **Ver código fuente** o equivalente para visualizar las cabeceras completas del mensaje.  
- Localizar una línea que comience por `Received:` y anotar la dirección IP del servidor que ha enviado el correo.  
- Utilizar una herramienta de consulta de direcciones IP para determinar el país de origen del servidor.

**Cuestión de análisis**  
- Indica el país desde el que se ha enviado el mensaje.  
- Analiza si existe coherencia entre el origen real del correo y la supuesta identidad del remitente.

---

## Actividad 3: Navegación privada y visibilidad en la red

**Objetivo**  
Comprender las limitaciones de la navegación privada y desmitificar su supuesto anonimato frente a administradores de red o atacantes locales.

**Descripción**  
El alumno comprobará si el uso del modo de navegación privada afecta a la visibilidad del equipo dentro de la red local.

**Tareas a realizar**  
- Abrir una ventana de **Navegación Privada** o **Modo Incógnito** en el navegador.  
- Utilizar **Zenmap** para realizar un escaneo de tipo *Intense Scan* hacia la propia dirección IP asignada en la red local.  

**Cuestión de análisis**  
- ¿Se siguen detectando los puertos abiertos del equipo durante el escaneo?  
- Explica por qué la navegación privada no oculta la presencia del equipo ante un administrador de red o un atacante conectado a la misma red local.

---

## Actividad 4: Configuración de filtros en el cliente de correo

**Objetivo**  
Implementar medidas básicas de filtrado para reducir la recepción de correo no deseado.

**Descripción**  
El alumno configurará reglas personalizadas en su cliente de correo para gestionar automáticamente determinados mensajes entrantes.

**Tareas a realizar**  
- Acceder a la configuración del cliente de correo electrónico utilizado habitualmente.  
- Crear una **regla** o **filtro** que envíe directamente a la papelera los mensajes cuyo asunto contenga palabras como “oferta” o “premio”.  

**Cuestión de análisis**  
- Explica por qué los filtros basados únicamente en palabras clave pueden generar **falsos positivos**.  
- Propón un ejemplo de correo legítimo que podría eliminarse por error al aplicar esta regla.

---

## Consideraciones finales

Estas actividades permiten reflexionar sobre el impacto de la publicidad, los rastreadores y el spam en la privacidad del usuario, así como sobre la importancia de aplicar medidas de control y filtrado para reducir riesgos y tráfico no deseado en las redes.
