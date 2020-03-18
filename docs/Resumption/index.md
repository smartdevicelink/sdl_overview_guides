# Application Data Resumption

Data resumption is used when an application requests to restore data used in the previous ignition cycle after an unexpected disconnect. Resumption starts during the `RegisterAppInterface` request message processing. The application must include the hashID parameter in the request for SDL Core to recognize a previous connection and attempt to restore as much of the previous HMI state as possible. If the hashID received from mobile is correct, SDL Core will restore the following data to the HMI.

- Menu Items (AddCommands)
- Sub Menus
- Choice Sets
- Persistent Files and Images
- Global Properties
- Button Subscriptions
- App Service Subscriptions
- Vehicle Data Subscriptions
- Remote Control Module Consent

For data resumption purposes, SDL Core must store application-related data such as menu commands, application global properties, voice recognition data, and subscriptions for previous ignition cycles after an unexpected disconnect or Ignition Off. 

!!! note
If your SDL Core integration is configured to use a resumption data base, on every fourth ignition cycle, SDL clears all corresponding application-related data used for resumption.

smartDeviceLink.ini example
```
; Resumption ctrl uses JSON if UseDBForResumption=false for store data otherwise uses DB
UseDBForResumption = false
```

This does not apply to the default configuration to use the app_info.dat JSON resumption file.
!!!

HMI must store the VR grammars compiled for applications that are unregistered by an unexpected disconnect or ignition Off. During data resumption, the HMI may also have to resume the previous audio source. Refer to `BasicCommunication.OnResumeAudioSource`.

If the application resumes data successfully:

 - SDL Core will provide the HMI `BasicCommunication.OnAppRegistered` with resumeVrGrammars:true to notify the HMI that VRGrammars must be resumed. On this event, the HMI must restore the application related VR grammars for the appID received via an OnAppRegistered notification.
 - SDL Core must restore application-related data and send to the HMI after an OnAppRegistered notification. 
 - Applications will not need to resend the following RPCs:
  - AddCommand (Menu + VR)
  - AddSubMenu
  - CreateInteractionChoiceSet
  - SetGlobalProperties
  - SubscribeButton
  - SubscribeVehicleData
  - GetAppServiceData if previous parameter `subscribe = true`

|||
Successful App Resumption
![Successful App Resumption](./assets/OnAppRegisteredResume.png)
|||

If the application does NOT resume data successfully:

 - SDL Core will provide OnAppRegistered with resumeVrGrammars:false or no resume parameter at all.
 - SDL Core cleans up all previously stored application data for the application that failed to resume. The HMI must also clean up previously compiled VRGrammars for the application.
 - The application will send new data to start SDL operations. In this event, SDL and the HMI should restart the cycle of collecting application data for resumption.

|||
Unsuccessful App Resumption
![Unsuccessful App Resumption](./assets/OnAppRegisteredNoResume.png)
|||
