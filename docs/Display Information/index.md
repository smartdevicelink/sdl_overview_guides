## Display Information

### Display vs Voice
Designing your application on a mobile device is entirely a visual process. However, designing application for in-vehicle experience requires closer consideration of driver distraction rules to ensure the safety of your application user. Below listed are some of the best practices you will need to consider while designing your application for in-vehicle use so as to eliminate the need to understand the driver distraction laws and guidelines that are continually changing around the world.

### General Guidelines  

#### Use Voice Commands  
 It is highly recommended to focus on voice interactions first and foremost. In a vehicle, especially while driving, your application usage should be almost entirely accomplished using voice commands.

#### Presenting Clear Information
 There are only a few ways of presenting information to the user. The first way is to write to the available _templates_, for example to your application's main screen. While more advanced displays allow for more updated fields and _templates_, you are always given a _base template_ to write to.
 The second is to send a text string for the voice engine to process and speak back to the user. The combination of the two, display _template_ updates and sending text to be processed into speech, is the best way of presenting information to the user. An example of this is requesting a pop-up with text-to-speech (_TTS_), or `Alert`.

TBD: Attach link for [Available Templates](#available-templates).

#### Using Display
There are anywhere between two and four lines of text available to your application via the `Show` command. As a general rule, use this display to convey the current state of your application.

_line 1_ and _line 2_: Use _line 1_ and _line 2_ for relatively continuous updates such as, what station is playing, artist/track being streamed, distance to location, etc.

_line 3_ and _line 4_: Other information which might be useful, but not pertinent to functionality are best included on _Lines 3_ and _4_, if available.


#### Number of Custom Softbuttons

When using `Show` in combination with `SetDisplayLayout`, depending on the OEM, the number of custom softbuttons on each display layout will differ. The standard format of softbuttons for each system is as follows:

Layout | Standard # of Softbuttons
-----------|-------------
DOUBLE\_GRAPHIC\_WITH\_SOFTBUTTONS	| 8
GRAPHIC\_WITH\_TEXT |	0
GRAPHIC\_WITH\_TEXT\_AND_SOFTBUTTONS |	2
GRAPHIC\_WITH\_TEXTBUTTONS	| 3
GRAPHIC\_WITH\_TILES |	3
LARGE\_GRAPHIC\_WITH\_SOFTBUTTONS	| 8
MEDIA	| 8
NON\_MEDIA	 | 8
TEXT\_AND\_SOFTBUTTONS\_WITH\_GRAPHIC	| 2
TEXT\_WITH\_GRAPHIC |	0
TEXTBUTTONS\_ONLY	 | 8
TEXTBUTTONS\_WITH\_GRAPHIC	| 3
TILES\_ONLY	| 7
TILES\_WITH\_GRAPHIC |	3


#### Provide Feedback

  * Brand new user
    A welcome message with basic instructions could be given the first few times a user uses the application in vehicle using the `Speak` function. Once they’ve used the application a set number of times, you can remove these helpful prompts.
    Send a `Show` command to update the display with a welcome message or initialization message such as “_Buffering…_”.

  * Logged In User Account  
    If your application does require a logged in user account, you should always have logic to catch applications that are running in-vehicle without an active account and display a message notifying the user to log in when not driving.
    Refer to the [Standard Interaction Phrases](#standard-interaction-phrases) section for sample voice and/or text messages.

  * Waiting for Online Data Download  
    If your application is waiting for online data to get downloaded, display "_Loading..._" text on _Line 1_ of the _template_ to inform the user of the download.

  * Background Application  
    If your application is a background application, with no real action for the user to take while using it in-vehicle, you might not have any voice commands or soft-buttons available in your application. It is recommended to provide an "_About_" or "_Info_" Menu/voice command or/and soft-button (with voice command) which when used by the user provides a brief message about the application. You may also choose to point them to the help section in your mobile app which might be more descriptive.

  * Dealing with Permissions  
    If your application is using certain functions, such as vehicle data, it is essential to ensure that the application provides feedback to the user in cases when:
      - All or part of the vehicle data is not available in the vehicle (as some car lines or model only provide a subset of the vehicle data available in other car lines).  
      - User did not provide consent to use vehicle data.
      - User has disabled access to all or part of the vehicle data your application is using.   

    For the above scenarios, as a feedback you may let the user know that the application might not work as expected due to the lack of availability of vehicle data. Refer to the [Standard Interaction Phrases](#standard-interaction-phrases) section for sample voice/text messages.

    Note that some RPCs are protected by policies for every OEM. To gain access to such RPCs, contact the OEM.     

  * Using ScrollableMessage  
    `ScrollableMessage` is a useful way to show and display text to a user. In some markets like Europe and Asia, `ScrollableMessage` can be used at any time, to show a message or other relevant information that wouldn’t fit on an `Alert`. It is important to note that in North America, `ScrollableMessage` is limited in use and cannot be used while the vehicle is in motion. Please be advised that you may find these messages are blocked from being shown in that region. To detect this condition, use the `OnDriverDistraction` notification on vehicles before showing the message, or if you detect `ScrollableMessage` is rejected due to driver distraction restrictions, simply use a `Speak` or another
    method to convey the information.

  * Handling API rejections  Part of guides  
    Depending on the state of the system, or your application permissions, some of the messages you send to the vehicle may get rejected. It is important to understand why these are happening when they occur, so that you may present the proper information to the user. If a command you send is `REJECTED`, it is recommended to send it again, depending on the message. For example, if an `AddCommand` is rejected, you will need to send it again, to ensure your menu option or voice command is available on the system. If a request for `Alert` is `REJECTED`, it may mean the system is in a state in which your message cannot be played. You may want to try again after 15-30 seconds if the information is pertinent to the user.

  * General feedback recommendation
    * Applications must provide an audio or visual response to user interactions (button presses, _VR_, `AddCommands`, etc.).
    * Applications must not provide an incorrect or unexpected response to user interaction.

  * Standard Interaction Phrases
    * Login Required
      - Text: To use _< app name >_ you have to be logged in.
      - Voice: To continue using _< app name >_ please login on your mobile phone while not driving.  

    * Vehicle Data Availability
      - Text: Grant access to vehicle data in Mobile Apps settings.
      - Voice: _< App name >_ might not work as expected as we are unable to access _< Vehicle Information, Push Notifications, Location Information and Driving Characteristics >_. Please enable this feature in Mobile App's settings menu while not driving.
