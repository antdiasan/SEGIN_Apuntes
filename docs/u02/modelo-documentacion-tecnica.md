# Modelo de Documentación Técnica

**Autor:** Departamento de Sistemas / Alumno del módulo SEGIN  
**Versión:** 1.0  
**Fecha:** {{fecha_actual}}  
**Unidad:** RA2 – Sistemas de almacenamiento y copias de seguridad

---

## 1. Propósito y alcance

Este documento define los **procedimientos técnicos** para garantizar la **seguridad, disponibilidad e integridad** de la información almacenada en equipos locales, servidores y servicios en la nube.

Incluye las operaciones relacionadas con:
- Copias de seguridad y restauración de datos.
- Cifrado del almacenamiento.
- Monitorización del estado de las unidades.
- Evaluación de riesgos.

---

## 2. Descripción del entorno

| Elemento | Descripción | Ubicación |
|-----------|---------------|-------------|
| Servidor NAS | Cabina con RAID 1 y redundancia de fuente | Aula de redes |
| Estaciones cliente | 15 equipos Windows 10 con sincronización en nube | Aula 1 |
| Servicio cloud | Google Drive / OneDrive | Acceso remoto |
| Software de backup | Cobian Backup / rsync | Local |

**Política general:**
- Copia incremental diaria.
- Copia completa semanal en la nube.
- Prueba de restauración mensual.

---

## 3. Procedimientos técnicos

### 3.1 Realización de copias de seguridad

1. Verificar el espacio libre en el destino.  
2. Ejecutar la tarea programada con la herramienta de copia.  
3. Revisar el archivo de registro (log) en busca de errores.  
4. Registrar la operación en la tabla de seguimiento.

**Ejemplo de comando en Linux:**
```bash
rsync -av --delete /home/usuario/ /media/backup/usuario/
```

### 3.2 Restauración de archivos

1. Localizar la copia adecuada.  
2. Verificar la integridad mediante hash o checksum.  
3. Restaurar el archivo o carpeta.  
4. Documentar la incidencia.

### 3.3 Cifrado del almacenamiento

| Tipo | Herramienta | Uso |
|------|--------------|-----|
| Cifrado de disco completo | BitLocker / VeraCrypt / LUKS | Portátiles y equipos de aula |
| Cifrado de archivos | 7-Zip / GnuPG | Archivos sensibles |
| Cifrado en tránsito | HTTPS / TLS | Copias hacia la nube |

---

## 4. Evaluación de riesgos

| Riesgo | Probabilidad | Impacto | Medidas preventivas |
|--------|---------------|----------|----------------------|
| Fallo de disco | Alta | Alto | RAID, copias automáticas |
| Error humano | Media | Medio | Versionado, permisos |
| Ransomware | Media | Muy alto | Copias offline, antivirus |
| Daño físico | Baja | Muy alto | Copia externa, nube |

---

## 5. Plan de verificación y mantenimiento

- Revisión semanal de logs.  
- Prueba mensual de restauración.  
- Monitorización SMART de discos.  
- Actualización anual de contraseñas y software de backup.

---

## 6. Registro de operaciones

| Fecha | Operador | Tipo de copia | Resultado | Observaciones |
|--------|-----------|---------------|------------|----------------|
| 15/10/2025 | Alumno 1 | Incremental | OK | Copia sin errores |
| 22/10/2025 | Alumno 1 | Completa | OK | Prueba de restauración correcta |

---

## 7. Referencias

Este modelo se ha elaborado tomando como referencia documentación técnica profesional de las siguientes fuentes:

1. **NIST SP 800-209** – *Security Guidelines for Storage Infrastructure*  
   [https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-209.pdf](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-209.pdf)

2. **HP Enterprise Backup Solution Design Guide**  
   [https://h10032.www1.hp.com/ctg/Manual/c00190922.pdf](https://h10032.www1.hp.com/ctg/Manual/c00190922.pdf)

3. **IBM Storage Scale Documentation**  
   [https://www.ibm.com/docs/en/storage-scale/5.2.2](https://www.ibm.com/docs/en/storage-scale/5.2.2)

4. **Data Backup and Recovery Plan (Big Stone County IT)**  
   [https://cms7files.revize.com/bigstonemn/Government/Information%20Technology/docs/IT-1540%20BSC%20Data%20Backup%20and%20Recovery%20Plan.pdf](https://cms7files.revize.com/bigstonemn/Government/Information%20Technology/docs/IT-1540%20BSC%20Data%20Backup%20and%20Recovery%20Plan.pdf)

5. **Red Hat – Managing Storage Devices**  
   [https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/managing_storage_devices/index](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/managing_storage_devices/index)

---

## 8. Control de versiones

| Versión | Fecha | Autor | Descripción |
|----------|--------|--------|--------------|
| 1.0 | {{fecha_actual}} | Antonio / Alumno SEGIN | Documento base del modelo técnico |
