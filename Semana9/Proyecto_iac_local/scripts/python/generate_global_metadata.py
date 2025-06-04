#!/usr/bin/env python3
import json
import sys
import datetime
import uuid
import hashlib
import socket

def generate_deployment_metadata():
    """Genera metadatos globales para todo el despliegue"""
    
    # ID único del despliegue
    deployment_id = str(uuid.uuid4())
    
    # Timestamp del despliegue
    deployment_timestamp = datetime.datetime.utcnow().isoformat()
    
    # Información del entorno
    try:
        hostname = socket.gethostname()
    except:
        hostname = "unknown"
    
    # Hash único basado en timestamp y hostname
    deployment_hash = hashlib.sha256(
        f"{deployment_timestamp}{hostname}".encode()
    ).hexdigest()[:16]
    
    # Metadatos globales del despliegue
    global_metadata = {
        "deployment_id": deployment_id,
        "deployment_timestamp": deployment_timestamp,
        "deployment_hash": deployment_hash,
        "environment": {
            "hostname": hostname,
            "deployment_type": "terraform_local",
            "orchestrator": "terraform",
            "version": "1.0"
        },
        "global_settings": {
            "region": "local",
            "availability_zone": "local-1a",
            "cluster_name": f"cluster-{deployment_hash[:8]}",
            "network_cidr": "10.0.0.0/16"
        },
        "deployment_tags": {
            "managed_by": "terraform",
            "project": "iac_local",
            "environment": "development",
            "deployment_date": deployment_timestamp.split('T')[0]
        }
    }
    
    return global_metadata

def main():
    # El script data external no necesita argumentos de entrada
    # pero los lee por compatibilidad
    if sys.stdin.isatty():
        # Si se ejecuta directamente (no desde Terraform)
        input_json = {}
    else:
        input_str = sys.stdin.read()
        try:
            input_json = json.loads(input_str) if input_str else {}
        except:
            input_json = {}
    
    # Generar metadatos globales
    metadata = generate_deployment_metadata()
    
    # Para verificación/debugging
    if "--debug" in sys.argv:
        print(json.dumps(metadata, indent=2), file=sys.stderr)
        return
    
    # Output para Terraform data external
    # Todos los valores deben ser strings
    output = {
        "deployment_id": metadata["deployment_id"],
        "deployment_timestamp": metadata["deployment_timestamp"],
        "deployment_hash": metadata["deployment_hash"],
        "environment_json": json.dumps(metadata["environment"]),
        "global_settings_json": json.dumps(metadata["global_settings"]),
        "deployment_tags_json": json.dumps(metadata["deployment_tags"]),
        "full_metadata_json": json.dumps(metadata)
    }
    
    print(json.dumps(output))

if __name__ == "__main__":
    main()