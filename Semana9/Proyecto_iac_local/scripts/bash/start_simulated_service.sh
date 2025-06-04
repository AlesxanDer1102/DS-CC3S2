#!/bin/bash
APP_NAME=$1
INSTALL_PATH=$2
CONFIG_FILE=$3

echo "--- Iniciando servicio simulado: $APP_NAME ---"
echo "Ruta de instalación: $INSTALL_PATH"
echo "Archivo de configuración: $CONFIG_FILE"

if [ ! -f "$CONFIG_FILE" ]; then
  echo "ERROR: Archivo de configuración no encontrado: $CONFIG_FILE"
  exit 1
fi

# 1) Asegurarse de que exista el directorio de logs
LOG_DIR="$INSTALL_PATH/logs"
mkdir -p "$LOG_DIR"

PID_FILE="$INSTALL_PATH/${APP_NAME}.pid"
LOG_FILE="$LOG_DIR/${APP_NAME}_startup.log"

echo "Simulando inicio de $APP_NAME a las $(date)" >> "$LOG_FILE"
# Simular más líneas de logging y operaciones
for i in {1..25}; do
    echo "Paso de arranque $i: verificando sub-componente $i..." >> "$LOG_FILE"
    # sleep 0.01 # Descomenta para simular tiempo
done

# Crear un archivo PID simulado
echo $$ > "$PID_FILE"  # $$ es el PID del script actual

# RETO ADICIONAL: Crear .db_lock si es database_connector
if [ "$APP_NAME" == "database_connector" ]; then
    DB_LOCK_FILE="$INSTALL_PATH/.db_lock"
    
    # Crear el archivo .db_lock con información relevante
    echo "Database locked at: $(date)" > "$DB_LOCK_FILE"
    echo "Locked by PID: $$" >> "$DB_LOCK_FILE"
    echo "Service: $APP_NAME" >> "$DB_LOCK_FILE"
    
    # Extraer y registrar la connection_string del archivo de configuración
    CONNECTION_STRING=$(python3 -c "
import json
with open('$CONFIG_FILE', 'r') as f:
    config = json.load(f)
    print(config.get('connection_string', 'NOT_FOUND'))
" 2>/dev/null)
    
    if [ "$CONNECTION_STRING" != "NOT_FOUND" ]; then
        echo "Connection: $CONNECTION_STRING" >> "$DB_LOCK_FILE"
        echo "Database connection string encontrado y registrado" >> "$LOG_FILE"
    else
        echo "WARNING: No se encontró connection_string en la configuración" >> "$LOG_FILE"
    fi
    
    # Registrar información adicional en el log
    echo "=== DATABASE CONNECTOR STARTUP ===" >> "$LOG_FILE"
    echo "Archivo de bloqueo creado: $DB_LOCK_FILE" >> "$LOG_FILE"
    echo "Connection string: $CONNECTION_STRING" >> "$LOG_FILE"
    echo "Lock timestamp: $(date)" >> "$LOG_FILE"
    echo "=================================" >> "$LOG_FILE"
    
    # Mensaje en consola
    echo "INFO: Archivo .db_lock creado para $APP_NAME en $DB_LOCK_FILE"
fi

echo "Servicio $APP_NAME 'iniciado'. PID guardado en $PID_FILE" >> "$LOG_FILE"
echo "Servicio $APP_NAME 'iniciado'. PID: $(cat "$PID_FILE")"
echo "--- Fin inicio servicio $APP_NAME ---"