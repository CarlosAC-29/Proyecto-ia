#!/bin/bash
echo Verificando la existencia del ambiente virtual...
if [ ! -d "env" ]
then
  echo Creando el ambiente virtual...
  python3 -m venv mi_entorno
fi
echo Activando el ambiente virtual...
source mi_entorno/bin/activate
echo Instalando las dependencias...
pip3 install -r requirements.txt
echo Ejecutando la aplicación de Streamlit...
streamlit run index.py
echo Desactivando el ambiente virtual...
deactivate