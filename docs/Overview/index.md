## SDL Overview Guide

This is an overview of how SmartDeviceLink (SDL) works. It will go through higher level discussions about certain aspects of SDL to give an intro level of understanding. For more general information on SmartDeviceLink (SDL) as a technology, there is a white-paper available [here](https://smartdevicelink.com/resources/).

SmartDeviceLink is a connectivity protocol and set of associated libraries that allow third-party applications to communicate with cars. This allows drivers to safely access the content they want through their vehicle. 

Many different components make SDL work. The following diagram shows how some of those pieces are connected. 

<br><br>
![High Level Diagram](assets/HighLevelDiagram.png) 



## Sections

### Supported Platforms

This section quickly points out which platforms can be used for the application, Core, and HMI parts of the project.

### Getting Started

The first few guides will be centered around getting SDL started. 

1. Establish a connection over the transport.
2. How the app starts the SDL protocol and how Core accepts.
3. How the app registers itself onto the head unit and how Core responds with system information.
4. How the app is activated for user interaction

### Protocol Spec

This section describes the lowest level of SDL. It defines how the byte level data is communicated between the application library and the head unit / Core. It contains information on what protocol level packets are used, basic handshakes, etc.

### RPC Spec

This section describes the higher level JSON-RPC messages that get sent. These messages are higher-level messages sent using the protocol spec's lower level messages (see above). The majority of messages that get sent between the app and head unit are RPC messages. The RPC messages contain information to perform and respond to actions, notify of events, etc. The RPC spec defines much of what SDL can do.

### Policies

SmartDeviceLink uses policies to enforce rules about which messages can be sent to and from connected apps. This section will give an overview of that functionality and how to update the policy table, which declares these policies for all known apps.

### App Services

Connected applications can augment a head unit's service offerings (such as navigation and weather) using SDL. Head units can feed the service specific information into their own system as a unified API for that app service type. This includes displaying service data outside the app's template view and makes that app feel integrated directly with the head unit.

### Best Practices

This section contains items that aren't hard requirements but are best practices to ensure that the widest variety of apps work properly with your head unit.

### FAQ

This section covers a few of the commonly asked questions around SDL.
