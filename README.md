# hellofairy
Componente para manejar las luces de navidad

Basado en esta pagina:https://community.home-assistant.io/t/control-hello-fairy-ble-string-lights-with-esphome/818595


## Estructura

```
custom_components/
└── hellofairy/
    ├── __init__.py
    ├── manifest.json
    ├── const.py
    ├── ble_controller.py  ← Maneja conexión y comandos BLE
    ├── light.py           ← Entidad LightEntity
    ├── switch.py          ← Entidad SwitchEntity
    ├── number.py          ← Entidad NumberEntity
    └── coordinator.py     ← Maneja estado y notificaciones
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
