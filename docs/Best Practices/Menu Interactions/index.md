## Menu Items and Interactions

All the major features or functions of your application (nouns/verbs) could be loaded as top-level voice commands and or menu items using `AddCommands`. It is recommended that this list be less than 150 commands, to improve application initialization performance and for high voice recognition quality.


### General Guidelines

#### Responding to user input
As an application, you will want to respond to user input. To limit changes in modality, we highly recommend looking at the trigger source for input provided to your application, either via voice or menu. In instances where `OnCommand` indicates you've made a selection, and you want to use `PerformInteraction`, ensure the mode is the **_same_**. For example, if trigger source is `MENU`, you'll want to start your interaction with an interaction mode of `MANUAL_ONLY`. If trigger source is `VR`, you'll want to trigger your interaction as `BOTH` or `VOICE_ONLY`. Also, as a best practice always set your `PerformInteraction` timeout to max giving sufficient time for the user to respond.

#### Handling Choices, ChoiceSets and Commands  
Applications can load `ChoiceSet` with 100 items. If your `PerformInteraction` requires additional commands, you may reference additional `ChoiceSets`. That is, one `PerformInteraction` can contain more than one `ChoiceSet`. If your list of choices is known ahead of time, it is helpful to create these during your initialization phases, and simply reuse the `ChoiceSet` throughout your application's lifecycle. When a user initiates an interaction, the user may choose from whatever choices are defined at that moment. It is up to the application to ensure that all appropriate choices are defined **_before_** the app interaction. Also, consider grouping your choices in a way that maximizes reusability of the defined `Choices` or `ChoiceSets`.

*Note*:
* It is not recommended to consistently delete and create choice sets. If you must delete a `ChoiceSet`, it is suggested that you wait some time since it was last used. Immediately deleting a `ChoiceSet` after its `PerformInteraction` has returned could lead to undesired application behavior.
* While `DeleteCommand` and `DeleteInteractionChoiceSet` are supported RPCs, only use them when appropriate. Avoid deleting commands and `ChoiceSets` that will knowingly be used again.
* Every `choiceID` across different `ChoiceSets` should have unique IDs within the app's lifecycle.



#### Ordered Items  
Always order items in your lists for better user experience. Ordering the items which are more often used in your application or ordering the items based on the specific user preferences, or based on current location of the user etc. will help keep the most important items to the user accessible. In general, order the items from most important to least important.

#### VR for Softbuttons  
To add VR for softbuttons, use `AddCommand` with no `menuParameters`.

#### Name and Image  
You may use both name and image for items wherever applicable.

#### Choosing Voice Grammar  
Applications must not register voice grammars using synonyms that include other application names, or conflict with on-board voice commands.

#### Making Lists more informative
It is always a good practice to add relevant and useful information to the list items, for example if your app is a media app and you have a list of audio contents, adding information such as when the content was aired.

#### Handling Lists
PerformInteraction lists should always be as small as possible by UX design. However, in cases where having long lists cannot be avoided, please follow the below best practices for better user experience.

*Note:* Avoid opening `PerformInteraction` from within another `PerformInteraction`.  

1. List with multiple action item per choice
	
	- For each item which has several more actions available:  
  Example: Searching for events in the vicinity. There might be a big number of events. On each event you can select “Call venue”, “Navigate to it”, “Details”, “Play” (playing the artist of a potential concert in the vicinity).
		- Present each result on on its own screen via `Show` and announce it with a pure voice alert via`Speak`.  
       - Define softbuttons for each possible action and add the respective command to voice and menu.
       - To cycle through the result list, you may use one of the below options:
       - `Skip`button (which is currently only available for Media Apps)
       - Softbuttons & Voice commands
       - Show the current item and the length of the list in the Media-track. For example 1/10 for the first item out of 10 items from the result.
       - Announce the availability of `Skip`hard button on the steering wheel for easy navigation.

      *Note:* Only make the announcement the first time the search has been completed to reduce any kind of annoyance to the user.

	- For each item only one action available:  
  Example: scenario is already "Navigate To _<some location_>"  
  In contrast to the above, you may choose to use `PerformInteraction`.
  
2. Simple lists
 If the results are known by the user or the result list is very small you can use `PerformInteraction` instead depending on the current use case.   

Example:

```
User Action 1:

VR/MENU: "Create result list"  
Result 1:

  SCREEN LINE 1:  "Result 1 a"  
  SCREEN LINE 2:  "Result 1 b"   
  MEDIA TRACK:    "1/25"   
  SOFTBUTTONS:   Action 1, Action 2, Action 3,...,Previous, Next, More...
  TTS:            "Result 1 <possibly more information about the result>"
                  //First Time: Announce possible ways to navigate (skip buttons,
                     voice command, etc..)

```

```
User Action 2:

VR/MENU/SOFTBUTTON: "Action 1"  
Result 2:

This is only applicable if the "Action 1" of "Result 1" results in another
screen. If just a call is initiated by "action 1" there is no need to
display an ensuing screen.

  SCREEN LINE 1:  "Action 1 Result 1 a"  
  SCREEN LINE 2:  "Action 1 Result 1 b"   

  SOFTBUTTONS:   Softbuttons highly depend on the use case you are developing.
                  If the user again has an array of choices, use the same
                  concept as explained above. Otherwise, adapt the screen to
                  your use case.
  TTS:            "Result of Action 1 on Result 1"
```

```
User Action 3:

VR/MENU/SOFTBUTTONS: "Next"  
Result 3:

  SCREEN LINE 1:  "Result 2 a"  
  SCREEN LINE 2:  "Result 2 b"   
  MEDIA TRACK:    "2/25"   
  SOFTBUTTONSS:   Action 1, Action 2, Action 3,...,Previous, Next, More...
  TTS:            “Result 2 <possibly more information about the result>.”
```
