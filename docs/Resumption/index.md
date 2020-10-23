# Application Data Resumption

Data resumption is used when an application requests to restore data used in the previous ignition cycle after an unexpected disconnect. Resumption starts during the `RegisterAppInterface` request message processing. The application must include the hashID parameter in the request for SDL Core to recognize a previous connection and attempt to restore the previous HMI state. If the hashID received from mobile is correct, SDL Core will restore the following data to the HMI.

- Menu and VR Commands
- Sub Menus
- Choice Sets
- Persistent Files and Images
- Global Properties
- Button Subscriptions
- App Service Subscriptions
- Vehicle Data Subscriptions
- Remote Control Module Consent

For data resumption purposes, SDL Core must store application-related data such as menu commands, application global properties, voice recognition data, and subscriptions for previous ignition cycles after an unexpected disconnect or ignition off. 

!!! note
On every fourth ignition cycle, SDL Core clears all corresponding application-related data used for resumption. This will either be stored in app_info.dat or in the resumption database depending on SDL Core's ini configuration.

smartDeviceLink.ini example
```
; Resumption ctrl uses JSON if UseDBForResumption=false for store data otherwise uses DB
UseDBForResumption = false
```
!!!

HMI must store the VR grammars compiled for applications that are unregistered by an unexpected disconnect or ignition off. During data resumption, the HMI may also have to resume the previous audio source. Refer to `BasicCommunication.OnResumeAudioSource`.

If the application resumes data successfully:

 - SDL Core will reply to the mobile application's `RegisterAppInterface` request with `resultCode = SUCCESS`
 - SDL Core will provide the HMI `BasicCommunication.OnAppRegistered` with `resumeVrGrammars = true` to notify the HMI that `VRGrammars` must be resumed. On this event, the HMI must restore the application related VR grammars for the appID received via an `OnAppRegistered` notification.
 - SDL Core must restore application-related data and send to the HMI after an `OnAppRegistered` notification. 
 - Applications will not need to resend the following RPCs:
  - AddCommand (Menu + VR)
  - AddSubMenu
  - CreateInteractionChoiceSet
  - CreateWindow
  - SetGlobalProperties
  - SubscribeButton
  - SubscribeVehicleData
  - SubscribeWayPoints
  - PutFile
  - GetSystemCapability if previous parameter `subscribe = true`
  - GetAppServiceData if previous parameter `subscribe = true`

|||
Successful App Resumption
![Successful App Resumption](./assets/OnAppRegisteredResume.png)
|||

If during resumption, the HMI responds with an error to any of the above requests sent by SDL Core, SDL Core will revert all resumption data by for example sending DeleteCommand to all successfully acknowledged AddCommand requests. An error response from the HMI indicates unsuccessful resumption, and SDL Core will continue to register the app in a fresh state.

If the application does NOT resume data successfully:

 - SDL Core will reply to the mobile application's `RegisterAppInterface` request with `resultCode = RESUME_FAILED`
 - SDL Core will provide `OnAppRegistered` with `resumeVrGrammars = false` or no resume parameter at all.
 - SDL Core cleans up all previously stored application data for the application that failed to resume. The HMI must also clean up previously compiled `VRGrammars` for the application.
 - The application will send new data to start SDL operations. In this event, SDL Core and the HMI should restart the cycle of collecting application data for resumption.
 - GetSystemCapability subscriptions were still restored, and requests with parameter `subscribe = true` do not need to be resent.

|||
Unsuccessful App Resumption
![Unsuccessful App Resumption](./assets/OnAppRegisteredNoResume.png)
|||
