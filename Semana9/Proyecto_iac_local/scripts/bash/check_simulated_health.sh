#!/bin/bash
SERVICE_PATH=$1
SERVICE_NAME=$(basename "$SERVICE_PATH") # Asumir que el último componente es el nombre

echo "--- Comprobando salud de: $SERVICE_NAME en $SERVICE_PATH ---"

# Directorio y fichero de logs
LOG_DIR="$SERVICE_PATH/logs"
LOG_FILE="$LOG_DIR/${SERVICE_NAME}_health.log"

# Asegurarse de que exista el directorio de logs
mkdir -p "$LOG_DIR"

# Extraer nombre base del servicio de forma más inteligente
BASE_SERVICE_NAME=$(echo "$SERVICE_NAME" | sed 's/_v[0-9]\+\.[0-9]\+\.[0-9]\+$//')

# Si no encontró el patrón de versión, intentar con el método original como fallback
if [ "$BASE_SERVICE_NAME" == "$SERVICE_NAME" ]; then
    BASE_SERVICE_NAME=$(echo "$SERVICE_NAME" | cut -d'_' -f1)
fi

PID_FILE_ACTUAL="$SERVICE_PATH/${BASE_SERVICE_NAME}.pid"

echo "Comprobación iniciada a $(date)" > "$LOG_FILE"
echo "Buscando archivo PID: $PID_FILE_ACTUAL" >> "$LOG_FILE"

# Simular más líneas de operaciones y logging
for i in {1..20}; do
    echo "Paso de comprobación $i: verificando recurso $i..." >> "$LOG_FILE"
done

if [ -f "$PID_FILE_ACTUAL" ]; then
    PID=$(cat "$PID_FILE_ACTUAL")
    # En un sistema real, verificaríamos si el proceso con ese PID existe.
    # Aquí simulamos que está "corriendo" si el PID file existe.
    echo "Servicio $BASE_SERVICE_NAME (PID $PID) parece estar 'corriendo'." | tee -a "$LOG_FILE"
    echo "HEALTH_STATUS: OK" >> "$LOG_FILE"
    
    # Verificación especial para database_connector
    if [ "$BASE_SERVICE_NAME" == "database_connector" ]; then
        DB_LOCK_FILE="$SERVICE_PATH/.db_lock"
        if [ -f "$DB_LOCK_FILE" ]; then
            echo "Archivo de bloqueo de base de datos encontrado: $DB_LOCK_FILE" | tee -a "$LOG_FILE"
            echo "Lock info: $(head -1 "$DB_LOCK_FILE")" >> "$LOG_FILE"
        fi
    fi
    
    echo "--- Salud OK para $SERVICE_NAME ---"
    exit 0
else
    echo "ERROR: Archivo PID $PID_FILE_ACTUAL no encontrado. $BASE_SERVICE_NAME parece no estar 'corriendo'." | tee -a "$LOG_FILE"
    echo "HEALTH_STATUS: FAILED" >> "$LOG_FILE"
    echo "--- Salud FALLIDA para $SERVICE_NAME ---"
    exit 1
fi