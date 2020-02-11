# Policy Table Fields

## Module Config

The module config section contains some global defaults that can be set for SDL

### Policy Table Update Configurations

#### Example Entry

```json
"module_config": {
    ...
    "exchange_after_x_ignition_cycles": 100,
    "exchange_after_x_kilometers": 1800,
    "exchange_after_x_days": 30,
    "timeout_after_x_seconds": 60,
    "seconds_between_retries": [
        1,
        5,
        25,
        125,
        625
    ],
    ...
}
```

A Policy Table Update (PTU) is when SDL sends a request to a connected application to retrieve a new policy table from the server.

Some configurable events will trigger Core to request a PTU. The exact parameters which are used to trigger the update can be configured in this section:

|Name|Type|Description|
|:---|:---|:----------|
|exchange_after_x_ignition_cycles|Integer|PTU Trigger, defines the number of ignition cycles before SDL initiates a PTU|
|exchange_after_x_kilometers|Integer|PTU Trigger, defines the distance that can be traveled in the vehicle before SDL initiates a PTU|
|exchange_after_x_days|Integer|PTU Trigger, defines the number of days that can pass before SDL initiates a PTU|
|timeout_after_x_seconds|Integer|The amount of time (in seconds) SDL will wait for a PTU to complete before timing out and retrying|
|seconds_between_retries|Integer Array|A list of times (in seconds) to wait after a failed PTU before trying again. The number of items in this list determines the number of retries that will be attempted in a single session.|

### lock_screen_dismissal_enabled

A boolean value which determines if it should be possible to dismiss the lock screen on a connected SDL application.

If true, an entry must be present in the `consumer_friendly_messages` section of the policy for `LockScreenDismissalWarning`. The `textBody` section of this structure will be displayed to the user in this case, warning them that dismissal should only be performed if they are not the driver of the vehicle. If the entry is not present, then this option will be ignored and default to `false`.

### endpoints

This section contains several lists of urls that are used throughout SDL. Each subsection must contain a default list of endpoints, and app-specific endpoints can be added optionally as well. If an app-specific endpoint list is specified, these endpoints will be used instead of the default when performing the corresponding request with that application.

#### Example Entry

```json
"module_config": {
    ...
    "endpoints": {
        "0x07": {
            "default": [
                "http://x.x.x.x:3000/api/1/policies/proprietary"
            ],
            "123abc": [
                "https://app.endpoint.com/api/1/policies/proprietary"
            ]
        },
        "0x04": {
            "default": [
                "http://x.x.x.x:3000/api/1/softwareUpdate"
            ],
            "123abc": [
                "https://example.endpoint.com/api/1/softwareUpdate"
            ]
        },
        "queryAppsUrl": {
            "default": [
                "http://sdl.shaid.server"
            ]
        },
        "lock_screen_icon_url": {
            "default": [
                "http://i.imgur.com/TgkvOIZ.png"
            ],
            "123abc": [
                "https://example.endpoint.com/logo.png"
            ]
        },
        "custom_vehicle_data_mapping_url": {
            "default": [
                "http://x.x.x.x:3000/api/1/vehicleDataMap"
            ]
        }
    },
    ...
}
```

* `0x07` - A set of urls that are used when performing a PTU
* `0x04` - A set of urls that are used to retrieve module software updates
* `queryAppsUrl` - A set of urls that are used to receive valid apps for querying on iOS devices
* `lock_screen_icon_url` - A set of urls which each host an image that can be displayed by the application on the driver's device while the lock screen is active (ex. an OEM logo)
    * This url is sent in a request to each application after they are first registered. The application proxy downloads the image and displays it along with the lock screen when driver distraction mode is active.
* `custom_vehicle_data_mapping_url` - A set of urls that are used to retrieve a custom mapping file to be used by the HMI to translate requests for custom vehicle data (as defined in the `vehicle_data` section)
    * See [this guide](https://smartdevicelink.com/en/guides/core/integrating-your-hmi/vehicle-data/#vehicle-data-mapping-file) for more information

### endpoint_properties

This section includes properties corresponding to the keys in the `endpoints` section:

* `version` - The version of the file associated with this url, currently only applies to `custom_vehicle_data_mapping_url`

#### Example Entry

```json
"module_config": {
    ...
    "endpoint_properties": {
        "custom_vehicle_data_mapping_url": {
            "version": "1.0.0"
        }
    },
    ...
}
```

### notifications_per_minute_by_priority

This section includes a list of custom `priority` values to be used in the `app_policies` section. Each key is attached to a value in this map, which defines how many alerts can be sent by an app while in the background ("notifications") within a given minute (ex. `"NAVIGATION": 15` means that an application with `"priority": "NAVIGATION"` can send up to 15 background alerts every minute).

This feature is used to restrict an app's control of the screen when they are in the background, so that they are not disruptive to the user while driving.

#### Example Entry
```json
"module_config": {
    ...
    "notifications_per_minute_by_priority": {
        "EMERGENCY": 60,
        "NAVIGATION": 15,
        "PROJECTION": 15,
        "VOICECOM": 20,
        "COMMUNICATION": 6,
        "NORMAL": 4,
        "NONE": 0
    },
    ...
}
```

### certificate

A field used to replace the local certificate used for establishing secure connections with applications. Contains the full string representation of the certificate. If present in a PTU, this certificate will overwrite the existing certificate on the module.

## Consumer Friendly Messages

The consumer friendly messages section contains a list of messages which are meant to be displayed by the HMI at specified times. Most can be custom-defined and referenced via the `user_consent_prompt` section of a functional group.

### languages

Each `consumer_friendly_messages` entry contains a list of languages that it supports, with each language entry containing a struct with the following possible fields: `tts`, `label`, `line1`, `line2`, and `textBody`
The HMI can retrieve this struct by key and language via the `SDL.GetUserFriendlyMessage` RPC.

## Functional Groupings

The functional groupings section contains the definitions for each named group of RPC permissions that an application can be assigned. There can be any number of functional groups. The functional groups are used in the application policies section to define permissions for each application.

#### Example Entry

```json
"functional_groupings" : {
    "Location-1": {
        "user_consent_prompt": "Location",
        "encryption_required": false,
        "rpcs": {
            "GetVehicleData": {
                "hmi_levels": [
                    "BACKGROUND",
                    "FULL",
                    "LIMITED"
                ],
                "parameters": [
                    "gps",
                    "speed"
                ]
            },
            "OnVehicleData": {
                "hmi_levels": [
                    "BACKGROUND",
                    "FULL",
                    "LIMITED"
                ],
                "parameters": [
                    "gps",
                    "speed"
                ]
            },
            "SubscribeVehicleData": {
                "hmi_levels": [
                    "BACKGROUND",
                    "FULL",
                    "LIMITED"
                ],
                "parameters": [
                    "gps",
                    "speed"
                ]
            },
            "UnsubscribeVehicleData": {
                "hmi_levels": [
                    "BACKGROUND",
                    "FULL",
                    "LIMITED"
                ],
                "parameters": [
                    "gps",
                    "speed"
                ]
            }
        }
    },
    ...
}
```

### encryption_required

This flag is used to specify whether the RPCs included in this functional group must be encrypted when assigned to an application. Can be overridden for a specific application by setting the same flag to `false` in its application policies entry (See [App Policies](../app-policies#security-fields)).

### user_consent_prompt

Only applies when Core is built with `EXTENDED_POLICY=EXTERNAL_PROPRIETARY`, using this field means that the user will need to provide consent before an application can gain permission to use this group. The consent prompt given to the user will be retrieved from the `consumer_friendly_messages` entry tied to this value (ex. if the value is `AppPermissions`, the prompt will be retrieved from the `consumer_friendly_messages.messages.AppPermissions` field of the policy table).

### rpcs

This section defines a list of RPCs which will be granted to each application that has access to this functional group. Within each entry are several fields to fine-tune permissions by HMI level or individual parameter:

* `hmi_levels` - A list of HMI levels from which this RPC can be sent by an application if given permissions for this functional group.
* `parameters` - A list of parameters which can be sent in this RPC by an application if given permissions for this functional group. Primarily used for the purpose of controlling vehicle data permissions.
    * If an application sends a parameter that it does not have access to, it will be filtered out, and Core will process the message normally from there. 
    * If omitted, all parameters will be allowed.

!!! note
Prior to Core version 6.0.0, the `parameters` field was only implemented for vehicle data related RPCs.
!!!

## Vehicle Data

This section can be used to define custom vehicle data values for a system, as well as add capabilities for newer vehicle data items on an older module without updating the system software. See [this guide](https://smartdevicelink.com/en/guides/core/integrating-your-hmi/vehicle-data/#custom-vehicle-data) for more details.
