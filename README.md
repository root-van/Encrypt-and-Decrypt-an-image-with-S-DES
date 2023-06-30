# Encrypt-and-Decrypt-an-image-with-S-DES
Este script en Python está diseñado para encriptar y desencriptar imágenes utilizando el sistema de encriptación Simplified Data Encryption Standard (S-DES). Lo notable de este script es que ha sido implementado desde cero, sin el uso de módulos que contengan la funcionalidad del S-DES.

## ¿Qué es el S-DES?
El S-DES (Simplified Data Encryption Standard) es una variante simplificada del algoritmo de encriptación DES (Data Encryption Standard). El S-DES utiliza una clave de 10 bits para encriptar y desencriptar datos, y es conocido por ser un algoritmo didáctico que permite entender los principios fundamentales de la encriptación simétrica.

## Funcionalidad del script

El script consta de las siguientes funciones:

1. **Generación de claves**: Esta función genera las dos claves de 8 bits necesarias para el proceso de encriptación y desencriptación del S-DES.

2. **Encriptación**: Utilizando las claves generadas, incluyendo las claves vulnerables, esta función toma una imagen como entrada y aplica el algoritmo S-DES para encriptarla. El resultado es una imagen encriptada que puede ser almacenada en un archivo separado.

3. **Desencriptación**: Esta función toma una imagen encriptada y las claves generadas previamente, incluyendo las claves vulnerables, para realizar el proceso de desencriptación, restaurando la imagen original.

4. **Generación de claves vulnerables**: Esta función adicional proporciona la opción de generar claves vulnerables con fines educativos. Estas claves podrían ser más susceptibles a ataques, pero se utilizan exclusivamente con el propósito de comprender las debilidades del algoritmo.

### Instrucciones de uso
1. Ejecuta el archivo `cripto.py`.
2. Para encriptar la imagen es cuestion de seleccionar la opcion de Encriptar, el archivo que toma es "imagen.jpg" asi que asegurate de que tu imagen tenga el nombre correcto.
3. El script generará automáticamente las claves para el proceso de encriptación y desencriptación. También tendrás la opción de generar claves vulnerables, pero se recomienda utilizarlas únicamente con fines educativos.
4. Elige la opción de encriptación y el script aplicará el algoritmo S-DES a la imagen seleccionada, generando una imagen encriptada.
5. Para desencriptar una imagen previamente encriptada, selecciona la opción correspondiente y proporciona la ubicación de la imagen encriptada.
6. El script realizará el proceso de desencriptación utilizando las claves generadas, incluyendo las claves vulnerables, y restaurará la imagen original.
