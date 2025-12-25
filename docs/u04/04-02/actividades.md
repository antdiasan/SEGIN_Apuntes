# Actividades del apartado: Criptografía

En este apartado se proponen una serie de **actividades prácticas y de análisis** orientadas a que el alumnado comprenda el papel de la criptografía como mecanismo fundamental para garantizar la privacidad y la seguridad de la información.

Las actividades combinan experimentación guiada y reflexión, permitiendo diferenciar claramente entre cifrado simétrico, cifrado asimétrico y técnicas de ocultación de la información.

!!! warning "Uso responsable de herramientas"
    Las herramientas criptográficas deben utilizarse únicamente con fines educativos y sobre información no sensible.

---

## Actividad 1: Cifrado simétrico y robustez de claves (CyberChef)

**Objetivo**  
Comprender la importancia de la longitud y complejidad de la clave en los algoritmos de cifrado simétrico, tomando como referencia los algoritmos AES-128, AES-192 o AES-256.

**Descripción**  
El alumno utilizará la herramienta online CyberChef para cifrar un mensaje mediante el algoritmo AES, observando cómo pequeñas modificaciones en la clave producen cambios drásticos en el resultado cifrado.

**Tareas a realizar**  
- Acceder a la herramienta CyberChef.  
- Escribir un mensaje confidencial en el cuadro de entrada (*Input*).  
- Buscar y arrastrar la receta **AES Encrypt** al área de trabajo.  
- Configurar una clave (*Key*) de 16 caracteres (128 bits) y un vector de inicialización (*IV*) aleatorio.  
- Modificar un único carácter de la clave y observar el resultado obtenido.

**Cuestiones de análisis**  
- ¿Qué ocurre con el mensaje cifrado al cambiar un solo carácter de la clave?  
- Según lo aprendido, ¿por qué el algoritmo AES se considera el estándar actual frente a otros algoritmos más antiguos como DES?

---

## Actividad 2: Criptografía asimétrica y par de claves RSA

**Objetivo**  
Entender el funcionamiento del cifrado asimétrico mediante el uso de claves pública y privada, base de la confianza en las comunicaciones a través de Internet.
Afianzar que la clave privada nunca debe compartirse.

**Descripción**  
El alumno generará un par de claves RSA utilizando una herramienta software y realizará una simulación de intercambio seguro de información con otro compañero.

**Tareas a realizar**  
- Utilizar una herramienta online de generación de claves RSA o el software Kleopatra, si está disponible.  
- Generar un par de claves (pública y privada) con una longitud de 2048 bits.  
- Compartir la clave pública con un compañero.  
- Solicitar al compañero que cifre un mensaje corto utilizando dicha clave pública.  
- Recibir el mensaje cifrado e intentar descifrarlo utilizando la clave privada.

**Cuestión de análisis**  
- ¿Podría el compañero descifrar el mensaje que él mismo cifró? Justifica por qué este sistema resulta adecuado para el envío de información segura a través de un canal inseguro.

---

## Actividad 3: Esteganografía – el arte de ocultar información

**Objetivo**  
Diferenciar entre cifrar un mensaje (hacerlo ilegible) y ocultarlo (hacerlo invisible), analizando las limitaciones de la esteganografía como técnica de seguridad.

**Descripción**  
El alumno utilizará una herramienta de esteganografía para ocultar un mensaje dentro de una imagen, comprobando que el archivo resultante aparenta no haber sufrido cambios.

**Tareas a realizar**  
- Descargar una imagen en formato `.png` o `.bmp`.  
- Utilizar el software OpenStego o una herramienta equivalente para ocultar un archivo de texto dentro de la imagen.  
- Generar la nueva imagen resultante y comprobar que se visualiza con normalidad.  
- Compartir la imagen con un compañero e intentar extraer el mensaje utilizando la contraseña definida.

**Cuestión de análisis**  
- Compara visualmente la imagen original y la imagen generada. ¿Se aprecia alguna diferencia? Explica por qué la esteganografía no garantiza por sí sola la privacidad de la información.

---

## Consideraciones finales

Estas actividades permiten comprender de forma práctica las principales técnicas criptográficas, así como sus usos y limitaciones.  
El alumnado debe ser capaz de relacionar cada técnica con su aplicación real en la protección de la información transmitida en redes.

!!! success "Objetivo alcanzado"
    Si eres capaz de explicar cuándo usar cifrado simétrico, asimétrico o esteganografía, has comprendido el papel de la criptografía en redes.


