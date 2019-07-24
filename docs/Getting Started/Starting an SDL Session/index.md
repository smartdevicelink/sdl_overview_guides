## Starting an SDL Session

The [Protocol Spec](../../protocol-spec) defines the lowest SDL layer, and one of the first items that is required to connect an app is start an SDL Session. This includes starting the base RPC and Hybrid services – which are types of data sent using SDL that can be turned on and off – using the Control service which is always available.

The first packet sent is from the app library to the SDL Core implementation. This is a `StartService` control frame message. This packet is very basic and contains only a small amount of information about the app that is connecting and is intended to start the protocol session that all other SDL layers are built on top of. See the [protocol spec for more information](../../protocol-spec).

The Core implementation should respond with a `StartServiceACK` that contains specific information as described in the protocol spec. After this moment, the SDL session has been defined and started for an app.

![Step 2: Start the protocol session](assets/overall_2.png) 
