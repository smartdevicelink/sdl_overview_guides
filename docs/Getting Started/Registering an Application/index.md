# Registering an Application

After the app starts the SDL session, it's time to send more information to the SDL Core implementation about the application that is connecting. The library will send a `RegisterAppInterface` RPC request to Core. What information can be sent is found [here](https://github.com/smartdevicelink/rpc_spec#registerappinterface). Core passes most of this information to the HMI so that the HMI can present this application on an app list for the user to start.

After Core and the HMI have accepted the app, Core will create a `RegisterAppInterface` response to send back to the app. This will contain a lot of information about the system that the app library will need to know in order to adjust the app's UI and adapt to this specific system. The supplied parameters can be found [in the RPC Spec](https://github.com/smartdevicelink/rpc_spec#registerappinterface-1).

![Step 3: Registering an app](assets/overall_3.png) 

Once the app is registered, Core usually sends a few more notifications to the app. These include an `OnHMIStatus`, `OnPermissionChange`, `OnHashChange`, and `OnDriverDistraction`. 

## Post-Registration Notifications
### OnHMIStatus

This is a required notification from Core to be sent to the app. This sets the basic HMI status for the app on the head unit. At this point the app knows that it registered and displayed on an app list waiting for a user to select it. You can find more information about [OnHMIStatus parameters](https://github.com/smartdevicelink/rpc_spec#onhmistatus) in the RPC spec.

### OnHashChange

If the implementation of Core supports hash resumption, any time an item that can be restored with the correct hash changes this notification will be sent. Since the app just registered with information that updated the app record on Core, this notification is sent to the app. You can find more information about [OnHashChange parameters](https://github.com/smartdevicelink/rpc_spec#onhashchange) in the RPC spec.

### OnPermissionChange

After the app has registered, Core will check the policy table to see if the app has any permission updates.  You can find more information about [OnPermissionChange parameters](https://github.com/smartdevicelink/rpc_spec#onpermissionchange) in the RPC spec.

### OnDriverDistraction
This is a required notification from Core to be sent to the app. It defines information about whether or not the driver is currently in a distracted state (based on factors like the vehicle speed). You can find more information about [OnDriverDistraction parameters](https://github.com/smartdevicelink/rpc_spec#ondriverdistraction) in the RPC spec.

## After Registration

After the `OnHMIStatus` is received, the app will likely send a few RPCs that help get the head unit ready to display that application. The most common RPCs will be to set an app icon and to receive the list of files the application has stored on the head unit. The app icon is set up with a `PutFile` followed by a `SetAppIcon` request, while the list of files is retrieved with a `ListFiles` request.

Some apps will send more RPCs at this time, but based on the policy table they might be limited to a certain number.


![Step 3.5: Registering an app](assets/overall_3_5.png) 
