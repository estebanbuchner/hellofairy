# Hello Fairy BLE (via ESPHome)

Esta integración custom permite controlar las luces Hello Fairy usando entidades expuestas por ESPHome. No requiere conexión BLE directa ni `bleak`.
Basado en esta pagina:https://community.home-assistant.io/t/control-hello-fairy-ble-string-lights-with-esphome/818595

## Servicios disponibles

- `hellofairy.modo_fiesta`: activa el preset 58 y enciende las luces
- `hellofairy.apagar`: apaga la luz y el switch de energía

## Requisitos

- ESP32 configurado como cliente BLE en ESPHome
- Entidades disponibles: `light.string`, `switch.power`, `number.preset`



## Configuracion

```yaml

hellofairy:


```

|parametro	| valor | 
|-------|-----------------|
|a | b	|  


## Roadmap



|Fase   |	Objetivo                                                |	 Validación                               |	Tipo              |
|-------|---------------------------------------------------------|-------------------------------------------|-------------------|
|0.1.0|	Integración lógica base sobre ESPHome                     |	Servicios modo_fiesta y apagar funcionales|	Infraestructura   |
|0.2.0|	Entidades virtuales (button, sensor) para control agrupado|	UI con botones visibles y funcionales	    | UI / Entidades    |
|0.3.0|	Presets dinámicos y efectos personalizados                |	Servicio set_preset con validación        |	Lógica            |
|0.4.0|	Sincronización de estado y logging extendido              |	Sensor virtual con estado actual y logs   |	Observabilidad    |
|0.5.0|	Configuración vía UI (config_entry)                       |	Formulario para MAC, presets, nombre	    | UX / Config       |
|0.6.0|	Documentación modular y changelog por versión             |	README, changelog, ejemplos	              | Mantenimiento     |
|0.7.0|	Publicación en HACS                                       |	info.md, estructura HACS, badges	        | Distribución      |


## Estructura

```
custom_components/
└── hellofairy/
    ├── __init__.py
    ├── services.py
    ├── buttons.py
    ├── sensors.py
    ├── config_flow.py  ← fase 0.5.0
    ├── manifest.json
    ├── const.py
    ├── changelog/
    └── README.md

```


## Qué funcionalidades vamos a portar?

| Función ESPHome |Equivalente en integración                            |
|---------------|----------------------------------------|
| ble_client    | 	bleak.BleakClient
| globals       | 	DataUpdateCoordinator o atributos internos
| script        | 	métodos internos en clases
| sensor BLE    | 	callbacks de notificación BLE
| light RGB     | 	LightEntity con HSV→RGB
| switch power  | 	SwitchEntity con BLE write
| number preset | 	NumberEntity con BLE write

## Fases

|Fase	|Objetivo | Validación
|-------|-----------------|----------------------------------------|
|0.1.0	|BLE discovery + conexión básica	| ble_connected como binary_sensor
|0.2.0	|Enviar comando on/off |	SwitchEntity funcional
|0.3.0	|Recibir notificaciones BLE	|SensorEntity o TextSensor
|0.4.0	|Control RGB + HSV	|LightEntity con color picker
|0.5.0	|Control de presets	|NumberEntity funcional
|0.6.0	|Refactor + config_entry	|Configuración vía UI
|0.7.0	|Documentación + HACS	| README, badges, changelog, info.md
