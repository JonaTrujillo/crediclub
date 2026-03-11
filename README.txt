Solicitud de crédito
==================

Descripción
-----------
La finalidad de este proyecto es crear un proceso de solicitud de crédito basado en atributos de candidatos los cuales
serán evaluados en base a ciertas reglas:
El candidato debe solicitar un credito de entre 20,000 y 80,000
El candidato debe tener un score entre 500 y 900
El candidato debe tener edad entre 20 y 60 años
El candidato debe tener experiencia mayor o igual de 5 años
El candidato solicita un crédito mayor a 40,000, debe comprobar ingresos entre  25,000 y 40,000 si es hombre, caso contrario
solo comprobar ingreso minimo de 20,000
El candidato solicita un crédito menor igual a 40,000, debe comprobar ingresos entre  15,000 y 25,000 si es hombre, caso contrario
solo comprobar ingreso minimo de 10,000

Instalación
-----------
1. Clonar el repositorio:
   git clone https://github.com/JonaTrujillo/crediclub.git
2. Entrar en la carpeta:
3. Crear y activar entorno virtual:
   python -m venv venv
   venv\Scripts\activate  (Windows)
   source venv/bin/activate (Linux/Mac)
4. Instalar dependencias:
   pip install -r requirements.txt

Uso
---
- Ejecutar el servidor:
  uvicorn app.main:app --reload
- Endpoints disponibles:
  POST /applications                -> Crear Candidato a crédito
  POST /applications/{id}/documents -> Cargar documento para un candidato
  GET  /get/creditscore/{id}        -> Consultar score de un candidato
  GET  /applications/{id}           -> Consultar status de credito y motivos


Notas
-----
- Requiere Python >= 3.10
- MongoDB debe estar corriendo localmente
- Para introducir data de candidatos, se adjunta ejemplo:
[
  {
    "name": "Jonathan Trujillo Capetillo",
    "age": 29,
    "gender": "Masculino",
    "rfq": "TUCJ961223ADA",
    "curp": "TUCJ961223HVZRPN02",
    "income": 24000,
    "amountRequested": 50000,
    "yearExperience": 3
  },
  {
    "name": "Melissa Perez Cabrera",
    "age": 31,
    "gender": "Femenino",
    "rfq": "PECM961212Q2W",
    "curp": "PECM961212MVZRPN04",
    "income": 23000,
    "amountRequested": 55000,
    "yearExperience": 8
  },
  {
    "name": "Dolores Capetillo Perez",
    "age": 60,
    "gender": "Femenino",
    "rfq": "DOCP651903QQW",
    "curp": "DOCP601903QQWMVZRPN07",
    "income": 30000,
    "amountRequested": 60000,
    "yearExperience": 15
  },
  {
    "name": "Ventura Trujillo Quintana",
    "age": 65,
    "gender": "Femenino",
    "rfq": "VETQ651903VCE",
    "curp": "VETQ651903HMVZRPN07",
    "income": 45000,
    "amountRequested": 80000,
    "yearExperience": 8
  }
]