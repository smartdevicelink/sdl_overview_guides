## 2. Starting SDL Session

The first packet that gets sent is from the client SDL library to the SDL Core implementation. This is the `StartService` control frame message. This packet is very basic and contains only a small amount of information about the app that is connecting and is intended to being the protocol session in which all aspects of SDL is wrapped. See the protocol spec for more information [here](linktotheprotocolspec).

The Core implementation should respond with a `StartServiceACK` that contains specific information as described in the protocol spec. After this moment, the SDL session has been defined and started for an app.

![Step 2: Start the protocol session](overall_2.png) 
