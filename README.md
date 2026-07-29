<div align="center">

# Sotelosint

![Sotelosint Banner](banner.jpeg)

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/) [![Platform](https://img.shields.io/badge/Windows%20%7C%20Linux-lightgrey.svg)]() 

</div>

## 📌 Índice / Table of Contents
**Contenido en Español:**
* [📖 ¿Qué es esto? / What is this?](#-que-es-esto--what-is-this)
* [🛠️ Requisitos e Instalación](#️-requisitos-e-instalación)
* [🚀 Modo de Uso](#-modo-de-uso)
  * [Mostrar la Ayuda](#mostrar-la-ayuda)
  * [Ejemplos de Comandos básicos](#ejemplos-de-comandos-básicos)
  * [Análisis Completo (All-in-One)](#análisis-completo-all-in-one)
* [🧰 Herramientas Integradas](#-herramientas-integradas)
**English Content:**
* [📖 What is this?](#-que-es-esto--what-is-this)
* [🛠️ Requirements & Installation](#️-requirements--installation)
* [🚀 How to Use](#-how-to-use)
  * [Displaying Help](#displaying-help)
  * [Basic Command Examples](#basic-command-examples)
  * [Full Analysis (All-in-One)](#full-analysis-all-in-one)
* [🧰 Integrated Tools](#-integrated-tools)

## ¿Que es esto?/What is this?

**🇪🇸 Español:** Sotelosint es una potente herramienta osint todo en uno que automatiza la búsqueda de redes sociales y cuentas activas en internet utilizando un nombre de usuario, correo electrónico, número de teléfono o los tres elementos en paralelo. Al integrar cuatro aplicaciones de ciberseguridad en una sola orden de consola, el programa optimiza tu tiempo y corrige de forma inteligente cualquier fallo de formato automáticamente para garantizar una investigación fluida y sin interrupciones.

**🇬🇧 English:** Sotelosint is a powerful all-in-one OSINT tool that automates the search for social networks and active accounts across the internet using a username, email address, phone number, or all three elements in parallel. By integrating four cybersecurity applications into a single console command, the program optimizes your time and intelligently corrects any formatting errors automatically to ensure a smooth, uninterrupted investigation.

---

<!-- ================================================== -->
<!-- TODO EL CONTENIDO EN ESPAÑOL A PARTIR DE AQUÍ -->
<!-- ================================================== -->

# 📘 Guía Completa en Español

## 🛠️ Requisitos e Instalación

Para utilizar esta herramienta, necesitas tener instalado **Python 3.6** en adelante.

1. **Clona este repositorio o descarga los archivos:**
   ```bash
   git clone https://github.com/sotelodev2008/Sotelosint
   cd Sotelosint
   ```

2. **Crea y activa tu entorno virtual (Recomendado):**
   ```bash
   python -m venv venv # Pequeño recordatorio: en linux al escribir un comando de python se pone python3 en su lugar
   source venv/bin/activate  # En Linux
   # venv\Scripts\activate  # En Windows
   ```

3. **Instala las dependencias necesarias:**
   ```bash
   pip3 install -r requirements.txt #En Linux
   pip install -r requirements.txt #En Windows
   ```

---

## 🚀 Modo de Uso

El script se ejecuta a través de la terminal y acepta un máximo de tres argumentos siguiendo el orden: `python archivo.py [objetivo] [argumento] [teléfono]`.

### Mostrar la Ayuda
Si ejecutas el script sin argumentos o usas las banderas de ayuda, verás el menú de ayuda:
```bash
python archivo.py
# o también:
python archivo.py -h
```

### Ejemplos de Comandos básicos

* **Buscar usuario con Sherlock (Por defecto):**
  ```bash
  python sotelosint.py nombre_usuario
  python sotelosint.py nombre_usuario -s #Tambien puedes hacerlo así, aunque no es necesario ya que es el argumento predeterminado
  ```
* **Buscar usuario avanzado con Maigret:**
  ```bash
  python sotelosint.py nombre_usuario -m
  ```
* **Verificar cuentas vinculadas a un correo con Holehe:**
  ```bash
  python sotelosint.py correo@ejemplo.com -H
  ```
* **Verificar redes asociadas a un teléfono con Ignorant:**
  ```bash
  python sotelosint.py nombrevacio -i "Telefono" #El telefono debe de estar entre comillas llevando el prefijo y espaciado el telefono, como en este ejemplo "34 612345687"
  python sotelosint.py "Telefono" -i #Tambien es compatible si lo haces de esta forma
  ```

### Análisis Completo (All-in-One)
Para ejecutar las cuatro herramientas de forma secuencial sobre un mismo objetivo utilizando placeholders inteligentes, usa la bandera `-a` acompañada del número de teléfono:
```bash
python archivo.py nombre_o_correo -a "34 612345687"
```

---

## 🧰 Herramientas Integradas

El proyecto actúa como un puente unificado para las siguientes aplicaciones:
> * **[Sherlock](https://github.com)** - Búsqueda de perfiles por nombre de usuario.
> * **[Maigret](https://github.com)** - Rastreo avanzado de presencia en webs y redes.
> * **[Holehe](https://github.com)** - Comprobación de correos utilizados en registros.
> * **[Ignorant](https://github.com)** - Verificación de cuentas mediante números telefónicos.

---

<!-- ================================================== -->
<!-- ALL ENGLISH CONTENT STARTS FROM HERE -->
<!-- ================================================== -->

# 📙 Complete English Guide

## 🛠️ Requirements & Installation

To use this tool, you need to have **Python 3.6+** installed along with the four underlying cybersecurity applications.

1. **Clone this repository or download the files:**
   ```bash
   git clone https://github.com
   cd YOUR_REPOSITORY
   ```

2. **Create and activate your virtual environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Linux/Mac
   # venv\Scripts\activate  # On Windows
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🛠️ Requirements & Installation

To use this tool, you need to have **Python 3.6** or higher installed.

1. **Clone this repository or download the files:**
   ```bash
   git clone https://github.com/sotelodev2008/Sotelosint
   cd Sotelosint
   ```

2. **Create and activate your virtual environment (Recommended):**
   ```bash
   python -m venv venv # Quick reminder: on Linux, you must type python3 instead of python when writing a python command
   source venv/bin/activate  # On Linux
   # venv\Scripts\activate  # On Windows
   ```

3. **Install the required dependencies:**
   ```bash
   pip3 install -r requirements.txt # On Linux
   pip install -r requirements.txt # On Windows
   ```

---

## 🚀 How to Use

The script runs through the terminal and accepts up to three arguments in the following order: `python archivo.py [target] [argument] [phone]`.

### Displaying Help
If you run the script without arguments or use the help flags, you will see the help menu:
```bash
python archivo.py
# or alternatively:
python archivo.py -h
```

### Basic Command Examples

* **Search for a user with Sherlock (Default):**
  ```bash
  python sotelosint.py username
  python sotelosint.py username -s # You can also do it this way, although it is not necessary as it is the default argument
  ```
* **Advanced username search with Maigret:**
  ```bash
  python sotelosint.py username -m
  ```
* **Verify accounts linked to an email with Holehe:**
  ```bash
  python sotelosint.py email@example.com -H
  ```
* **Verify networks associated with a phone number via Ignorant:**
  ```bash
  python sotelosint.py emptyname -i "Phone" # The phone number must be enclosed in quotes, including the prefix and spacing, like this example "34 612345687"
  python sotelosint.py "Phone" -i # It is also compatible if you execute it this way
  ```

### Full Analysis (All-in-One)
To execute all four tools sequentially on a single target using intelligent placeholders, use the `-a` flag accompanied by the phone number:
```bash
python archivo.py username_or_email -a "34 612345687"
```

---

## 🧰 Integrated Tools

The project acts as a unified bridge for the following applications:
> * **[Sherlock](https://github.com)** - Profile search by username.
> * **[Maigret](https://github.com)** - Advanced footprint tracking across websites and social networks.
> * **[Holehe](https://github.com)** - Email registration check across multiple platforms.
> * **[Ignorant](https://github.com)** - Account verification using phone numbers.
