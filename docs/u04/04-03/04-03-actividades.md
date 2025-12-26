# Actividades del apartado: Identificación y confianza en las comunicaciones

En este apartado se proponen una serie de **actividades prácticas y de análisis** orientadas a que el alumnado comprenda cómo se establece la confianza en las comunicaciones digitales, así como el papel de los certificados digitales, las Autoridades de Certificación y la firma electrónica.

Las actividades están diseñadas para desarrollarse de forma guiada, combinando observación, configuración básica y reflexión sobre la seguridad de la información transmitida.

!!! warning "Uso responsable"
    Las herramientas criptográficas y de análisis deben utilizarse únicamente con fines educativos y sobre información no sensible.


---

## Actividad 1: Análisis de certificados en el navegador

**Objetivo**  
Aprender a identificar los elementos de confianza presentes en una comunicación segura mediante HTTPS.

**Descripción**  
El alumno analizará el certificado digital de una página web segura para identificar la entidad emisora, los algoritmos utilizados y el periodo de validez del certificado.

**Tareas a realizar**  
- Acceder a la página web de una entidad bancaria o a una sede electrónica oficial, sin introducir datos personales ni credenciales reales.  
- Pulsar sobre el icono del candado situado en la barra de direcciones del navegador.  
- Seleccionar la opción **Ver certificado** y examinar la información mostrada.

**Cuestión de análisis**  
- Indica quién es el **emisor (Autoridad de Certificación)**, el algoritmo de firma utilizado y la fecha de caducidad del certificado.  
- ¿Qué ocurre si se intenta acceder a una página web cuyo certificado está caducado o no es de confianza?

---

## Actividad 2: Instalación de certificados de la FNMT

**Objetivo**  
Configurar el almacén de certificados del sistema o del navegador para confiar en una Autoridad de Certificación concreta.

**Descripción**  
El alumno comprobará la presencia del certificado raíz de la FNMT en el almacén de certificados y, en caso necesario, procederá a su instalación.
No instalar certificados fuera de la web oficial.

**Tareas a realizar**  
- Acceder a la página web oficial de la **FNMT**.  
- Comprobar si el certificado raíz de la entidad ya se encuentra instalado en el navegador o en el sistema.  
- En caso contrario, descargar el certificado raíz.  
- Acceder a la configuración del navegador y localizar el apartado de **Gestión de certificados**.  
- Importar el certificado en la pestaña correspondiente a **Autoridades**.

**Cuestión de análisis**  
- Describe los pasos realizados durante el proceso de instalación.  
- ¿Por qué es necesario confiar primero en la Autoridad de Certificación para que el navegador confíe en los certificados personales emitidos por ella?

---

## Actividad 3: Gestión del almacén y exportación de certificados

**Objetivo**  
Aprender a realizar copias de seguridad de la identidad digital y a diferenciar entre certificados con y sin clave privada.

**Descripción**  
El alumno trabajará con el almacén de certificados del navegador o del sistema para exportar un certificado personal en distintos formatos.

**Tareas a realizar**  
- Localizar un certificado personal en el almacén de certificados del navegador o utilizar generado por el propio alumno, utilizando la herramienta Kleopatra (que ya han usado en el bloque de criptografía) o el propio navegador.  
- Exportar el certificado en formato `.pfx` o `.p12`, incluyendo la clave privada y protegiéndolo con una contraseña.  
- Realizar una segunda exportación en formato `.cer`, sin incluir la clave privada.

**Cuestión de análisis**  
- ¿Qué diferencia existe entre un certificado que incluye la clave privada y uno que no la incluye?  
- ¿Cuál de los dos podría enviarse por correo electrónico a un tercero de forma segura? Justifica la respuesta.

---

## Actividad 4: Firma de documentos y verificación

**Objetivo**  
Utilizar la firma electrónica para garantizar la integridad y el no repudio de la información.

**Descripción**  
El alumno firmará digitalmente un documento y comprobará la validez de la firma utilizando un servicio oficial de verificación.

**Tareas a realizar**  
- Crear un documento PDF sencillo.  
- Firmar el documento utilizando la aplicación **AutoFirma**.  
- Subir el documento firmado al portal oficial **VALIDe** para su verificación.

**Cuestión de análisis**  
- ¿Qué datos del firmante se muestran en el portal de validación?  
- ¿Qué sucede con la validez de la firma si se modifica una sola palabra del documento después de haber sido firmado?

---

## Consideraciones finales

Estas actividades permiten comprender cómo se establece la confianza en las comunicaciones digitales y el papel fundamental que desempeñan los certificados digitales y la firma electrónica en la seguridad de la información.

!!! success "Objetivo alcanzado"
    Si eres capaz de explicar cuándo usar huella digital, firma electrónica, certificados y PKI, has comprendido la base de la confianza en redes.


