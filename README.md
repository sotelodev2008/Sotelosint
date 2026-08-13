<div align="center">

# Sotelosint v2.0

![Sotelosint Banner](banner.jpeg)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**All-in-One OSINT Automation Framework**

[🇬🇧 English](#-english-guide) | [🇪🇸 Español](#-guía-en-español)


#### Check out the old versión using this [Link](old_README.md)

</div>

## 📋 Table of Contents / Índice

**English Content:**

- [📖 What is this?](#-what-is-this--qué-es-esto)
- [✨ Features](#-features)
- [🛠️ Installation](#-installation)
- [🚀 Usage](#-usage)
- [🧰 Integrated Tools](#-integrated-tools)
- [⚠️ Limitations](#-limitations)
- [🤝 Contributing ](#-contributing--contribuciones)

  

**Contenido en Español:**
- [📖 ¿Qué es esto?](#-what-is-this--qué-es-esto)
- [✨ Características](#-caracteristicas)
- [🛠️ Instalación](#-instalación)
- [🚀 Uso](#-uso)
- [🧰 Herramientas Integradas](#-herramientas-integradas)
- [⚠️ Limitaciones](#-limitcioness)
- [🤝 Contribuciones](#-contributing--contribuciones)

---

## 📖 What is this? / ¿Qué es esto?

**English:** SoteloSint is a modular OSINT (Open Source Intelligence) automation framework that unifies four powerful cybersecurity tools into a single command-line interface. It provides intelligent argument parsing, automatic error correction, and flexible output formatting for investigating usernames, email addresses, and phone numbers.

**Español:** SoteloSint es un framework modular de automatización OSINT (Inteligencia de Fuentes Abiertas) que unifica cuatro potentes herramientas de ciberseguridad en una única interfaz de línea de comandos. Proporciona análisis inteligente de argumentos, corrección automática de errores y formateo flexible de salida para investigar nombres de usuario, direcciones de correo electrónico y números de teléfono.

# 📘 English Guide

## ✨ Features

- **Unified Interface:** Access Sherlock, Maigret, Holehe, and Ignorant through a single command
- **Smart Argument Parsing:** Complex sub-arguments supported (e.g., `-scn` for Sherlock with CSV + NSFW)
- **Automatic Format Correction:** Intelligent handling of email domains and phone number formats
- **Modular Architecture:** Object-oriented design with separate handlers for each tool
- **Error Handling:** Graceful handling of missing dependencies and connection issues
- **Multi-Platform:** Works on Windows, Linux, and macOS

## 🛠️ Installation

### Prerequisites

Ensure you have Python 3.8+ and the following OSINT tools installed:

```bash
# Clone repository
git clone https://github.com/sotelodev2008/Sotelosint
cd Sotelosint

# Create virtual environment (recommended)
python -m venv venv #The second venv is the name you're going to give to the enviroment

# Activate environment
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows

# Install dependencies
pip install -r requirements.txt
```
## 🚀 Usage
```bash
python sotelosint.py [TARGET] [ARGUMENTS] [PREFIX] [NUMBER]
```
### Arguments
| Flag | Tool | Description |
| :--- | :--- | :--- |
| -s | Sherlock | Username search |
| -m | Maigret | Advanced username search |
| -H | Holehe | Email verification |
| -i | Ignorant | Phone number check |
| -a | All | Run all tools sequentially |
| -h | Help | Show help menu |

### Sub-arguments
```bash
Sherlock (-s):

b - Open browser with results
c - CSV output
n - Include NSFW sites
o - Set timeout (requires value)
t - Use Tor
u - Unique Tor (changes IP per request)
x - Disable TXT output


Maigret (-m):

a - All sites
c - Bypass Cloudflare
f - Limit to top N sites (requires number)
g - Graph output
h - HTML output
o - Set timeout (requires value)
t - Use Tor
x - XMind output


Holehe (-H):

c - CSV output
o - Set timeout (requires value)
u - Show only used sites


Ignorant (-i):

n - Don't clear terminal
```

#### Examples

```bash
# Basic Sherlock search
python sotelosint.py username

# Sherlock with CSV and Tor
python sotelosint.py username -sct

# Maigret with top 100 sites and HTML output
python sotelosint.py username -mfh 100

# Holehe with timeout
python sotelosint.py email@example.com -Ho 10

# Ignorant with country prefix
python sotelosint.py placeholder -i 34 612345687

# Ignorant with full number
python sotelosint.py 34612345687 -i

# All tools (requires phone for Ignorant)
python sotelosint.py username -a 34 612345687
```

### 🧰 Integrated Tools
| Tool | Purpose | Link |
| :--- | :--- | :--- |
| Sherlock | Hunt down social media accounts | [Link](https://github.com/sherlock-project/sherlock) |
| Maigret | Advanced OSINT username checker | [Link](https://github.com/soxoj/maigret) |
| Holehe | Check if email is used on websites | [Link](https://github.com/megadose/holehe) |
| Ignorant | Check if phone number is used | [Link](https://github.com/megadose/ignorant) |

> ### ⚠️ Limitations
> External Dependencies: Requires manual installation of Sherlock, Maigret, Holehe, and Ignorant
> Phone Format: Ignorant requires country prefix (e.g., 34 for Spain)
> Email Handling: Holehe automatically appends @gmail.com if no domain provided (use with caution)
> No Proxy Support: Direct connections only (except Tor support where available)

# 📙 Guía en Español
## ✨ Características
- **Interfaz Unificada:** Accede a Sherlock, Maigret, Holehe e Ignorant con un solo comando
- **Análisis Inteligente de Argumentos:** Soporta sub-argumentos complejos (ej: -scn para Sherlock con CSV + NSFW)
- **Corrección Automática de Formatos:** Manejo inteligente de dominios de email y formatos de teléfono
- **Arquitectura Modular:** Diseño orientado a objetos con manejadores separados para cada herramienta
- **Manejo de Errores:** Gestión elegante de dependencias faltantes y problemas de conexión
- **Multi-Plataforma:** Funciona en Windows, Linux y macOS

## 🛠️ Instalación

### Requisitos Previos

Asegúrate de tener Python 3.8+ y las siguientes herramientas OSINT instaladas:

```bash
# Clonar repositorio
git clone https://github.com/sotelodev2008/Sotelosint
cd Sotelosint

# Crear entorno virtual (recomendado)
python -m venv venv

# Activar entorno
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate    # Windows

# Instalar dependencias
pip install -r requirements.txt
```

## 🚀 Uso
Sintaxis
```bash
python sotelosint.py [OBJETIVO] [ARGUMENTOS] [PREFIJO] [NÚMERO]
```
### Argumentos
| Flag | herramienta | Descripción |
| :--- | :--- | :--- |
| -s | Sherlock | Búsqueda por usuario |
| -m | Maigret | Búsqueda avanzada por usuario |
| -H | Holehe | verificación de email |
| -i | Ignorant | Verificación de teléfono |
| -a | All | Ejecutar todas las herramientas secuencialmente |
| -h | Help | Mostrar menú de ayuda |

### Sub-argumentos
```bash
Sherlock (-s):

b - Abrir navegador con resultados
c - Salida CSV
n - Incluir sitios NSFW
o - Establecer timeout (requiere valor)
t - Usar Tor
u - Tor único (cambia IP por petición)
x - Desactivar salida TXT

Maigret (-m):

a - Todos los sitios
c - Saltar Cloudflare
f - Limitar a N sitios top (requiere número)
g - Salida Graph
h - Salida HTML
o - Establecer timeout (requiere valor)
t - Usar Tor
x - Salida XMind

Holehe (-H):

c - Salida CSV
o - Establecer timeout (requiere valor)
u - Mostrar solo sitios usados

Ignorant (-i):

n - No limpiar terminal
```
#### Ejemplos
```bash
# Búsqueda básica con Sherlock
python sotelosint.py johndoe

# Sherlock con CSV y Tor
python sotelosint.py johndoe -sct

# Maigret con top 100 sitios y salida HTML
python sotelosint.py johndoe -mfh 100

# Holehe con timeout
python sotelosint.py email@ejemplo.com -Ho 10

# Ignorant con prefijo de país
python sotelosint.py placeholder -i 34 612345687

# Ignorant con número completo
python sotelosint.py 34612345687 -i

# Todas las herramientas (requiere teléfono para Ignorant)
python sotelosint.py johndoe -a 34 612345687
```

### 🧰 Herramientas Integradas
| Tool | Purpose | Link |
| :--- | :--- | :--- |
| Sherlock | Buscar cuentas en redes sociales | [Link](https://github.com/sherlock-project/sherlock) |
| Maigret | Buscador OSINT avanzado de usuarios | [Link](https://github.com/soxoj/maigret) |
| Holehe | Verificar si email está registrado | [Link](https://github.com/megadose/holehe) |
| Ignorant | Verificar si teléfono está registrado | [Link](https://github.com/megadose/ignorant) |

### ⚠️ Limitaciones
Dependencias Externas: Requiere instalación manual de Sherlock, Maigret, Holehe e Ignorant
Formato de Teléfono: Ignorant requiere prefijo de país (ej: 34 para España)
Manejo de Email: Holehe añade automáticamente @gmail.com si no se proporciona dominio (usar con precaución)
Sin Soporte Proxy: Conexiones directas únicamente (excepto soporte Tor donde esté disponible)
### 🤝 Contributing / Contribuciones
English: Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

Español: ¡Las contribuciones son bienvenidas! Por favor haz fork al repositorio y envía un pull request con tus mejoras.
