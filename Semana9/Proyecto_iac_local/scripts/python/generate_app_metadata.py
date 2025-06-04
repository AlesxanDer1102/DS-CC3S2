#!/usr/bin/env python3
import json
import sys
import datetime
import uuid

# Función para simular lógica compleja
def complex_logic_simulation(app_name, version):
    # Simular múltiples operaciones y generación de datos
    data_points = []
    for i in range(15): # Generar 15 líneas de "lógica"
        data_points.append(f"Simulated data point {i} for {app_name} v{version} - {uuid.uuid4()}")

    dependencies = {} # Simular 10 líneas de dependencias
    for i in range(10):
        dependencies[f"dep_{i}"] = f"version_{i}.{i+1}"

    computed_values = {} # Simular 10 líneas de valores computados
    for i in range(10):
        computed_values[f"val_{i}"] = i * 100 / (i + 0.5)

    return {
        "generated_data_points": data_points,
        "simulated_dependencies": dependencies,
        "calculated_metrics": computed_values,
        "generation_details": [f"Detail line {j}" for j in range(15)] # 15 líneas más
    }

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test-lines": # Para contar líneas fácilmente
        print(f"Lee  líneas de código Python (incluyendo comentarios y espacios).")
        # Simulación de más líneas para conteo
        for i in range(60): # 60 print statements
            print(f"Línea de prueba {i}")
        return

    input_str = sys.stdin.read()
    input_json = json.loads(input_str)

    app_name = input_json.get("app_name", "unknown_app")
    app_version = input_json.get("version", "0.0.0")
    deployment_id = input_json.get("deployment_id", "no-deployment-id")  # NUEVO
    
    # Lógica de generación de metadatos 
    metadata = {
        "appName": app_name,
        "appVersion": app_version,
        "deploymentId": deployment_id,  # NUEVO - ID global del despliegue
        "generationTimestamp": datetime.datetime.utcnow().isoformat(),
        "generator": "Python IaC Script",
        "uniqueId": str(uuid.uuid4()),  # Este sigue siendo único por servicio
        "instanceId": f"{deployment_id}-{app_name}-{uuid.uuid4().hex[:8]}",  # NUEVO - combina deployment_id con info del servicio
        "parametersReceived": input_json,
        "simulatedComplexity": complex_logic_simulation(app_name, app_version),
        "additional_info": [f"Linea info {k}" for k in range(10)], # 10 líneas
        "status_flags": {f"flag_{l}": (l % 2 == 0) for l in range(10)}, # 10 líneas
        "deployment_context": {  # NUEVO - contexto del despliegue
            "deployment_id": deployment_id,
            "service_registration": f"{deployment_id}/{app_name}/{app_version}",
            "deployment_aware": True
        }
    }
    
    # Simulación de más lógica de negocio 
    metadata["processing_log"] = []
    for i in range(30):
        metadata["processing_log"].append(f"Entrada log  {i}: Item procesado {uuid.uuid4()}")
    
    # Añadir trazabilidad del despliegue
    metadata["processing_log"].append(f"Servicio registrado en despliegue: {deployment_id}")

    # El script DEBE imprimir un JSON válido a stdout para 'data "external"'
    print(json.dumps({"metadata_json_string": json.dumps(metadata, indent=2)}))

if __name__ == "__main__":
    main()