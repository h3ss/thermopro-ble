from bluetooth_sensor_state_data import BluetoothServiceInfo, SensorUpdate
from sensor_state_data import (
    DeviceKey,
    SensorDescription,
    SensorDeviceClass,
    SensorDeviceInfo,
    SensorValue,
    Units,
)

from thermopro_ble.parser import ThermoProBluetoothDeviceData


def test_can_create():
    ThermoProBluetoothDeviceData()


TP357 = BluetoothServiceInfo(
    name="TP357 (2142)",
    manufacturer_data={61890: b"\x00\x1d\x02,"},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    source="local",
)

TP357_ADD = BluetoothServiceInfo(
    name="TP357 (2142)",
    manufacturer_data={63938: b"\x00\x10\x02,"},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    source="local",
)

TP357_S = BluetoothServiceInfo(
    name="TP357S (2142)",
    manufacturer_data={
        61122: b'\x00)"\x0b\x01',
    },
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    source="local",
)


TP357_S_2 = BluetoothServiceInfo(
    name="TP357S (2142)",
    manufacturer_data={
        61122: b'\x00)"\x0b\x01',
        60866: b'\x00)"\x0b\x01',
        60610: b'\x00)"\x0b\x01',
        60354: b'\x00("\x0b\x01',
        60098: b'\x00("\x0b\x01',
        59842: b'\x00)"\x0b\x01',
        59586: b'\x00("\x0b\x01',
        59330: b'\x00("\x0b\x01',
        59074: b'\x00("\x0b\x01',
        58818: b'\x00("\x0b\x01',
        58562: b"\x00'\"\x0b\x01",
        58306: b'\x00("\x0b\x01',
        58050: b'\x00("\x0b\x01',
        57794: b'\x00)"\x0b\x01',
        57538: b'\x00)"\x0b\x01',
        57282: b'\x00)"\x0b\x01',
        57026: b'\x00)"\x0b\x01',
        56770: b'\x00)"\x0b\x01',
        56514: b'\x00)"\x0b\x01',
        56258: b'\x00)"\x0b\x01',
        56002: b'\x00)"\x0b\x01',
        55746: b'\x00*"\x0b\x01',
        55490: b'\x00)"\x0b\x01',
        55234: b'\x00*"\x0b\x01',
        54978: b'\x00*"\x0b\x01',
        54722: b'\x00*"\x0b\x01',
        54466: b'\x00+"\x0b\x01',
        54210: b'\x00-"\x0b\x01',
        53954: b'\x00,"\x0b\x01',
        53698: b'\x00/"\x0b\x01',
        53442: b'\x001"\x0b\x01',
        53186: b'\x00."\x0b\x01',
        52930: b'\x00,"\x0b\x01',
        52674: b'\x00,"\x0b\x01',
        52418: b'\x00+"\x0b\x01',
        52162: b'\x00*"\x0b\x01',
        51906: b'\x00*"\x0b\x01',
        51650: b'\x00*"\x0b\x01',
        51394: b'\x00*"\x0b\x01',
        51138: b'\x00*"\x0b\x01',
        50882: b'\x00)"\x0b\x01',
    },
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    source="local",
)


TP393 = BluetoothServiceInfo(
    name="TP393 (9376)",
    manufacturer_data={62146: b"\x005\x02,"},
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    source="local",
)


TP393_DETECT_CHANGED_1 = BluetoothServiceInfo(
    name="TP393 (9376)",
    manufacturer_data={
        194: b"\x00\x00\x00,",
        62146: b"\x00(\x02,",
        61890: b"\x00(\x02,",
        61634: b"\x00(\x02,",
        61378: b"\x00(\x02,",
        61122: b"\x00(\x02,",
        60866: b"\x00(\x02,",
        60610: b"\x00(\x02,",
        60354: b"\x00)\x02,",
        60098: b"\x00)\x02,",
        59842: b"\x00)\x02,",
        59586: b"\x00)\x02,",
        59330: b"\x00*\x02,",
        59074: b"\x00*\x02,",
        58818: b"\x00*\x02,",
        58562: b"\x00*\x02,",
    },
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    source="local",
)

TP393_DETECT_CHANGED_2 = BluetoothServiceInfo(
    name="TP393 (9376)",
    manufacturer_data={
        194: b"\x00\x00\x00,",
        62146: b"\x00(\x02,",
        61890: b"\x00(\x02,",
        61634: b"\x00(\x02,",
        61378: b"\x00(\x02,",
        61122: b"\x00(\x02,",
        60866: b"\x00(\x02,",
        60610: b"\x00(\x02,",
        60354: b"\x00)\x02,",
        60098: b"\x00)\x02,",
        59842: b"\x00)\x02,",
        59586: b"\x00)\x02,",
        59330: b"\x00*\x02,",
        59074: b"\x00*\x02,",
        58818: b"\x00*\x02,",
        58562: b"\x00*\x02,",
    },
    service_uuids=[],
    address="aa:bb:cc:dd:ee:ff",
    rssi=-60,
    service_data={},
    source="local",
)


def test_supported_set_the_title():
    parser = ThermoProBluetoothDeviceData()
    parser.supported(TP357) is True
    assert parser.title == "TP357 (2142) EEFF"


def test_tp357():
    parser = ThermoProBluetoothDeviceData()
    assert parser.update(TP357) == SensorUpdate(
        title="TP357 (2142) EEFF",
        devices={
            None: SensorDeviceInfo(
                name="TP357 (2142)",
                model="TP357",
                manufacturer="ThermoPro",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=24.1,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=29,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
    )


def test_tp357s():
    parser = ThermoProBluetoothDeviceData()
    assert parser.update(TP357_S) == SensorUpdate(
        title="TP357S (2142) EEFF",
        devices={
            None: SensorDeviceInfo(
                name="TP357S (2142)",
                model="TP357S",
                manufacturer="ThermoPro",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=23.8,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=41,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
    )
    assert parser.update(TP357_S_2) == SensorUpdate(
        title="TP357S (2142) EEFF",
        devices={
            None: SensorDeviceInfo(
                name="TP357S (2142)",
                model="TP357S",
                manufacturer="ThermoPro",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=23.8,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=41,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
    )


def test_tp357_add():
    parser = ThermoProBluetoothDeviceData()
    assert parser.update(TP357_ADD) == SensorUpdate(
        title="TP357 (2142) EEFF",
        devices={
            None: SensorDeviceInfo(
                name="TP357 (2142)",
                model="TP357",
                manufacturer="ThermoPro",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=24.9,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=16,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
    )


def test_tp393():
    parser = ThermoProBluetoothDeviceData()
    assert parser.update(TP393) == SensorUpdate(
        title="TP393 (9376) EEFF",
        devices={
            None: SensorDeviceInfo(
                name="TP393 (9376)",
                model="TP393",
                manufacturer="ThermoPro",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="temperature", device_id=None): SensorDescription(
                device_key=DeviceKey(key="temperature", device_id=None),
                device_class=SensorDeviceClass.TEMPERATURE,
                native_unit_of_measurement=Units.TEMP_CELSIUS,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            ),
            DeviceKey(key="humidity", device_id=None): SensorDescription(
                device_key=DeviceKey(key="humidity", device_id=None),
                device_class=SensorDeviceClass.HUMIDITY,
                native_unit_of_measurement=Units.PERCENTAGE,
            ),
        },
        entity_values={
            DeviceKey(key="temperature", device_id=None): SensorValue(
                device_key=DeviceKey(key="temperature", device_id=None),
                name="Temperature",
                native_value=24.2,
            ),
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            ),
            DeviceKey(key="humidity", device_id=None): SensorValue(
                device_key=DeviceKey(key="humidity", device_id=None),
                name="Humidity",
                native_value=53,
            ),
        },
        binary_entity_descriptions={},
        binary_entity_values={},
    )


def test_tp393_multi_updates():
    parser = ThermoProBluetoothDeviceData()
    assert parser.supported(TP393_DETECT_CHANGED_1) is True
    parser.update(TP393_DETECT_CHANGED_1)
    result = parser.update(TP393_DETECT_CHANGED_2)
    assert result == SensorUpdate(
        title="TP393 (9376) EEFF",
        devices={
            None: SensorDeviceInfo(
                name="TP393 (9376)",
                model="TP393",
                manufacturer="ThermoPro",
                sw_version=None,
                hw_version=None,
            )
        },
        entity_descriptions={
            DeviceKey(key="signal_strength", device_id=None): SensorDescription(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                device_class=SensorDeviceClass.SIGNAL_STRENGTH,
                native_unit_of_measurement=Units.SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
            )
        },
        entity_values={
            DeviceKey(key="signal_strength", device_id=None): SensorValue(
                device_key=DeviceKey(key="signal_strength", device_id=None),
                name="Signal " "Strength",
                native_value=-60,
            )
        },
        binary_entity_descriptions={},
        binary_entity_values={},
    )
