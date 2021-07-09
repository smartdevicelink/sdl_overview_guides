## Supported Platforms

### App Platforms

There are currently several supported platforms for integrating SDL into existing applications or creating new ones specifically for SDL.

#### Android

The Android SDL Library is specifically for creating applications that run on Android mobile versions of the operating system.

#### iOS

The iOS SDL Library is specifically for creating applications that run on iOS mobile versions of the operating system.

#### Java SE

The standard version of Java is supported to be used mostly embedded or local on the same hardware or network as the Core implementation. It can be ran from a backend as well, however, handling many connections at a time would be something that is handled outside of the Java SE SDL library.


#### Java EE

The enterprise edition of Java is supported, however, there is no Java EE specific code in the library itself. This is due to the fact that Java EE has conflicts with our licensing model for the open source library. This library is designed to be ran from a backend leveraging Java Beans and other web specific Java features.


### Core Platforms

#### Ubuntu

Core currently officially supports Ubuntu versions 18.04 and 20.04. Ubuntu 20.04 is the main supported platform of the project.

#### QNX

Many adopters have built Core on the QNX platform. It does require a decent amount of work. This will include switching out common linux based libraries with the QNX specific version or creating one from scratch.

#### Android Embedded

Some adopters have built Core on the Android platform. It does require a decent amount of work. This will include switching out common linux based libraries with the Android specific version or creating one from scratch.


### HMI Platforms

The HMI can be written in any platform as long as it can connect through websockets to Core and use the HMI spec as defined with the version of Core that is being used.

#### HTML

HTML is the most widely supported platform for developing the HMI. There are several examples of using HTML in the open, and the best example is the [Generic HMI](https://github.com/smartdevicelink/generic_hmi).

#### QT

Some partners have created HMI implementations using QT. This platform is useable, but is a bit less dynamic and more difficult to update than HTML.
