# App Policies

The app policies section defines permissions that each application is granted in the SDL environment. This is where you would change the default permissions for each application, or add rules for specific applications. Each key in this object is associated with the `fullAppID` field for an application (or `appID` if `UseFullAppID = false` in `smartDeviceLink.ini`), and each value is a struct which contains several fields to control permissions for this app. In addition, a few reserved keys exist for this section:

* `default` - The set of permissions which are assigned to an app if it does not have its own entry in the app policies section.
* `pre_DataConsent` - The set of permissions which are assigned to an app if the device is not given SDL permissions by the user. Only applies when Core is built with `EXTERNAL_PROPRIETARY` policy mode.
<!--* `device` - [TODO: find the exact purpose for this key]-->

## Basic Fields

### Example Entry

```json
"app_policies": {
    "123abc": {
        "keep_context": false,
        "steal_focus": false,
        "priority": "NONE",
        "default_hmi": "NONE",
        "groups": ["Base-4"],
        "RequestType": [],
        "RequestSubType": [],
        "nicknames": ["Example Application"],
        "AppHMIType": ["NAVIGATION", "MEDIA"]
    },
    ...
}
```

### groups

This field defines a list of functional groups which should be made available to this application, populated with a list of keys from the `functional_groupings` section (ex. if this list contains "Base-4", all permissions defined in the "Base-4" functional group will be assigned to this application).

### preconsented_groups

This field defines additional groups which are assigned to this application, with the difference that the user is expected to have consented to using these permissions separately from the HMI (via a mobile popup, etc.). Any groups defined in this list do not require consent from the user, even if they have a `user_consent_prompt` defined. Only applies when Core is built with `EXTERNAL_PROPRIETARY` policy mode, otherwise these permissions are simply added to the normal `groups` list.

### nicknames

This field defines a list of potential appNames which an application is allowed to register with. If the appName field in the app's `RegisterAppInterface` does not match one of the values in this list, the message will be rejected. If omitted, no restrictions will be applied to appName.

!!! note
This field is mandatory when defining policies for a cloud application, in which case the first nickname will be used in the application list prior to app registration.
!!!

### AppHMIType

This field defines a list of AppHMITypes which an application is allowed to be registered with. If provided, this list of AppHMITypes will be used for this application in place of the `appHMIType` list provided in the app's RegisterAppInterface request. If there are AppHMITypes present in the app's RegisterAppInterface request that are not present in this list, SDL Core will provide a warning of this discrepancy to the app in the RegisterAppInterface response.

!!! note
This field is mandatory for webengine apps which use the `WEB_VIEW` AppHMIType, in which case the `WEB_VIEW` value must be explicitly included in this list.
!!!

### keep_context

This field is a flag which allows or disallows an application to use soft buttons with the `KEEP_CONTEXT` action. This field only applies when Core is built with `EXTERNAL_PROPRIETARY` policy mode, otherwise this permission is always allowed.

### steal_focus

This field is a flag which allows or disallows an application to use soft buttons with the `STEAL_FOCUS` action. This field only applies when Core is built with `EXTERNAL_PROPRIETARY` policy mode, otherwise this permission is always allowed.

### priority

String value tied to the `notifications_per_minute_by_priority` section of `module_config`. By assigning a priority value from this list, the application is allowed the number of background alerts which is specified by that category (see [notifications_per_minute_by_priority](../policy-fields#notifications_per_minute_by_priority)).

### default_hmi

This field defines the default HMI level that the application will be initialized to when it is registered for the first time. This field only applies when Core is built with `EXTERNAL_PROPRIETARY` policy mode, otherwise the default HMI level is always `NONE`. 

### RequestType

This field defines a list of possible values for `requestType` that can be used in `OnSystemRequest` and `SystemRequest` RPCs when communicating with this app.

### RequestSubType

This field defines a list of possible values for `requestSubType` that can be used in `OnSystemRequest` and `SystemRequest` RPCs when communicating with this app.

<!--### memory_kb

Unused, see https://github.com/smartdevicelink/sdl_core/issues/3127.-->

### heart_beat_timeout_ms

Heartbeat timeout for this application, deprecated in [Protocol Version 4](https://github.com/smartdevicelink/protocol_spec#45-heartbeat), which was introduced in [SDL Core Version 4.0.0](https://github.com/smartdevicelink/sdl_core/releases/tag/4.0.0).

## Security Fields

### Example Entry

```json
"app_policies": {
    "123abc": {
        "keep_context": false,
        "steal_focus": false,
        "priority": "NONE",
        "default_hmi": "NONE",
        "groups": ["Base-4"],
        "RequestType": [],
        "RequestSubType": [],
        "certificate": "-----BEGIN CERTIFICATE-----\n...",
        "encryption_required": true
    },
    ...
}
```

### certificate

This field is a string value containing a certificate for establishing a secure connection with the application. This certificate is currently only used for cloud applications when establishing a secure WebSocket connection.

### encryption_required

This flag can be used to override `encryption_required` on the functional group level. If `false`, then this application will not be required to encrypt any of the RPCs which it has permissions to, even if the associated functional group has `encryption_required` set to `true`. If omitted, this flag defaults to `true`.

## Remote Control Fields

!!! note
These permissions will only take effect if the application either registers with the `REMOTE_CONTROL` AppHMIType or has this type explicitly included in its [AppHMIType policy field](#apphmitype).
!!!

### Example Entry

```json
"app_policies": {
    "123abc": {
        "keep_context": false,
        "steal_focus": false,
        "priority": "NONE",
        "default_hmi": "NONE",
        "groups": ["Base-4", "RemoteControl"],
        "RequestType": [],
        "RequestSubType": [],
        "AppHMIType": ["REMOTE_CONTROL"],
        "moduleType": ["RADIO", "CLIMATE"]
    },
    ...
}
```

### moduleType

This field defines a list of Remote Control module types (defined in the `ModuleType` enum in the [Mobile API](https://github.com/smartdevicelink/rpc_spec#moduletype)) which are accessible by the app. If empty, all module types will be allowed. If omitted, no module types will be allowed.

## App Service Fields

These fields are used if the application is either a provider or consumer of app service data. See our [App Service Guidelines](https://smartdevicelink.com/en/guides/core/feature-documentation/app-service-guidelines/) for more information on developing an application with these capabilities.

### Example Entry

```json
"app_policies": {
    "123abc": {
        "keep_context": false,
        "steal_focus": false,
        "priority": "NONE",
        "default_hmi": "NONE",
        "groups": ["Base-4", "AppServiceProvider", "AppServiceConsumer"],
        "RequestType": [],
        "RequestSubType": [],
        "app_services": {
            "MEDIA": {
                "service_names": ["SDL Music", "App Music"],
                "handled_rpcs": [{"function_id": 41}]
            },
            "NAVIGATION": {
                "service_names": ["SDL Navigation", "App Navigation"],
                "handled_rpcs": [{"function_id": 39}]
            },
            "WEATHER": {
                "service_names": ["SDL Weather", "App Weather"],
                "handled_rpcs": []
            }
        },
        "allow_unknown_rpc_passthrough": true
    },
    ...
}
```

### app_services

This field defines the properties of the app services that this application is allowed to publish. Each key within this object corresponds to an app service type (ex. "MEDIA").

* `service_names` - Defines a list of potential service names that an app can publish with this service type. 
    * If the `serviceName` field in the app's `PublishAppService.appServiceManifest` does not match one of the values in this list, the message will be rejected.
    * If omitted, no restrictions will be applied to the `serviceName` parameter.
* `handled_rpcs` - This field defines a list of permissions for RPCs that an app service could intercept via the [RPC passing](https://smartdevicelink.com/en/guides/core/feature-documentation/app-service-guidelines/#rpc-passing) feature. 
    * If the `handledRPCs` field in the app's `PublishAppService.appServiceManifest` includes a function ID that is not in this list, the message will be rejected. 
    * This field is mandatory, but can be empty.
    * Subfields:
        * `function_id` - The [function ID](https://github.com/smartdevicelink/rpc_spec#functionid) of the potential handled RPC. Can be a function ID which was introduced after Core's local RPC spec version.

### allow_unknown_rpc_passthrough

This flag can be used to allow an application to pass RPCs which are unknown to Core (functions which were defined after Core's local API version) to an app service provider. Otherwise, such messages from this application will be rejected. If omitted, this flag defaults to `false`.

## Cloud Application Fields

These fields are used for applications which use a cloud transport and require Core to initiate the connection. Each of these fields can be modified by a permitted app via the `SetCloudAppProperties` RPC.

### Example Entry

```json
"app_policies": {
    "123abc": {
        "keep_context": false,
        "steal_focus": false,
        "priority": "NONE",
        "default_hmi": "NONE",
        "groups": ["Base-4", "CloudApp"],
        "RequestType": [],
        "RequestSubType": [],
        "nicknames": ["Example Application"],
        "endpoint": "ws://smartdevicelink.com:8888/path/",
        "enabled": true,
        "cloud_transport_type": "WS",
        "auth_token": "1234567890",
        "icon_url": "http://i.imgur.com/TgkvOIZ.png"
    },
    ...
}
```

### enabled

This flag is used to determine if the cloud application should appear in the app list in the HMI. If `true`, the application will appear in the app list as a cloud application. Selecting this application from the list will cause Core to connect to and register the application.

### hybrid_app_preference

This option is used to determine the default behavior if the same app is available via a mobile device and over the cloud (determined by a duplicate `appName`). The possible values for this option are `MOBILE`, `CLOUD`, or `BOTH`. 

* If this value is set to `MOBILE`, the cloud application will be unregistered and removed from the app list if both applications are available.
* If this value is set to `CLOUD`, the mobile application will be unregistered if both applications are available.
* If this value is set to `BOTH`, both applications will remain in the app list if they are available.

### endpoint

This field defines the endpoint which Core will attempt to connect to when this application is selected from the app list (ex. `ws://smartdevicelink.com:8888/path/`). The format is dependent on the value of `cloud_transport_type`.

### auth_token

This field defines an authentication token to identify the user account tied to this vehicle. The format of this string is app-defined, and this value will be sent in the initial [StartServiceACK](https://github.com/smartdevicelink/protocol_spec#31322-start-service-ack) when a connection is established with the cloud application.

### cloud_transport_type

This field is a string which defines the type of transport that is used by the cloud application. The value of this is an arbitrary string, since an OEM can implement their transport adapter to establish any type of cloud connection. The current values which are supported by the provided cloud adapter in the SDL Core project are `WS` and `WSS`. 

### icon_url

This field is used to point to an app icon which can be displayed for a cloud application before it is connected. When provided, Core will retrieve this image using a connected application via an `OnSystemRequest` notification with the `ICON_URL` type.
