# RPC Encryption

#### Related Evolution Proposals
- [0207: RPC Message Protection](https://github.com/smartdevicelink/sdl_evolution/blob/master/proposals/0207-rpc-message-protection.md)

## Overview

The RPC encryption feature is designed to protect RPC messages transmitted between a mobile application and SDL. RPCs that need encryption and RPCs that do not need encryption share the same RPC service with encryption enabled.

## Determining when Encryption is Needed

### SDL Application

An SDL app is informed about the encryption requirement by an `OnPermissionsChange` notification sent by SDL Core. The `OnPermissionsChange` notification has a `requireEncryption` boolean parameter, which indicates the encryption requirement on the app level.

```xml
<function name="OnPermissionsChange" functionID="OnPermissionsChangeID" messagetype="notification" since="2.0">
    <description>Provides update to app of which policy-table-enabled functions are available</description>
    <param name="permissionItem" type="PermissionItem" minsize="0" maxsize="500" array="true" mandatory="true">
        <description>Change in permissions for a given set of RPCs</description>
    </param>
    <param name="requireEncryption" type="Boolean" mandatory="false" since="6.0"/>
</function>
```

Each `PermissionItem` struct in the notification also contains a `requireEncryption` boolean parameter, which indicates the encryption requirement on the RPC level.

```xml
<struct name="PermissionItem" since="2.0">
    <param name="rpcName" type="String" maxlength="100" mandatory="true">
        <description>Name of the individual RPC in the policy table.</description>
    </param>
    <param name="hmiPermissions" type="HMIPermissions"  mandatory="true"/>
    <param name="parameterPermissions" type="ParameterPermissions"  mandatory="true"/>
    <param name="requireEncryption" type="Boolean" mandatory="false" since="6.0"/>
</struct>
```
Using the app level and RPC level encryption requirements, the app side will be able to determine whether the app needs encryption or not and which RPCs in particular will need encryption.

An RPC message will require encryption/protection if
- The app has `requireEncryption=true` in the `OnPermissionsChange` notification and
- The RPC has `requireEncryption=true` in the `PermissionItem`

### SDL Core

SDL Core uses the `encryption_required` flags in the policy table to determine whether or not an RPC message requires encryption. 

The [`encryption_required`](https://smartdevicelink.com/en/guides/sdl-overview-guides/policies/policy-fields/#encryption_required) flag, in the `functional_groupings` section of the policy table, indicates whether or not **all** the RPCs within a functional group require encryption.

#### JSON Example

```json
"RemoteControl": {
    "encryption_required" : true,
    "rpcs": {
        "GetInteriorVehicleData": {
            "hmi_levels": ["BACKGROUND", "FULL", "LIMITED"]
        },
        "SetInteriorVehicleData": {
            "hmi_levels": ["BACKGROUND", "FULL", "LIMITED"]
        },
        ...
    }
}
```
Whereas the  [`encryption_required`](https://smartdevicelink.com/en/guides/sdl-overview-guides/policies/app-policies/#encryption_required) flag, in the `app_policies` section, indicates whether the app requires encryption or not.

#### JSON Example

```json
"app_policies": {
    "default": {
      "encryption_required": false,
      "keep_context": false,
      "steal_focus": false,
      "priority": "NONE",
      "default_hmi": "NONE",
      "groups": [
        "Base-4"
      ]
    },
    "appid_12345": {
      "encryption_required": true,
      "keep_context": false,
      "steal_focus": true,
      "priority": "NONE",
      "default_hmi": "NONE",
      "groups": [
        "Base-4", "RemoteControl"
      ]
    },
    ...
}
```
SDL Core informs an SDL application about the encryption requirement via an `OnPermissionsChange` notification.

!!! NOTE
Multiple functional groups can include the same RPC, each group having an `encryption_required` flag.

If an app has access to multiple functional groups containing the same RPC and **at least one** of the groups requires encryption, then the RPC shall require encryption.
!!!

## Handling unencrypted messages

SDL Core sends this result code to an SDL app when it receives an un-encrypted RPC request message **that needs encryption**.

```xml
<enum name="Result" internal_scope="base" since="1.0">
...
    <element name="ENCRYPTION_NEEDED" since="6.0">
        <description>SDL receives an un-encrypted RPC request that needs protection. </description>
    </element>
</enum>
```

## Setting up Encryption

### SDL Application

For more information on how to setup encryption on the SDL application side, please take a look at the Encryption guide for your selected platform.

- [Android Encryption Guide](https://smartdevicelink.com/en/guides/android/other-sdl-features/encryption/)
- [iOS Encryption Guide](https://smartdevicelink.com/en/guides/ios/other-sdl-features/encryption/)
- [JavaSE Encryption Guide](https://smartdevicelink.com/en/guides/javase/other-sdl-features/encryption/)
- [JavaEE Encryption Guide](https://smartdevicelink.com/en/guides/javaee/other-sdl-features/encryption/)

### SDL Core

For more information on how to enable and utilize RPC Encryption within SDL Core, please take a look at the [RPC Encryption Setup Guide](https://smartdevicelink.com/en/guides/core/feature-documentation/rpc-encryption/) section in the core guides.








