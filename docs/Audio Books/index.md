## Audiobooks
An audiobook app for SDL should include as much of the native apps functionality as possible, since that is what a user will be expecting out of the app.

#### Use Voice Commands
Your Audiobook app should contain such basic functionality as `Play`, `Pause`, and `Resume`. You can use build in controls for these features by calling the `subscribeButton` RPC. This will allow you to not only create buttons on the infotainment system but also be informed when the user presses hard buttons, which might be placed on the steering wheel. It is important to also add voice control capabilities for these functions. To add a voice command use the `addCommand` RPC but omit the `menuParams` argument. This will create a voice command without creating an item in the menu.   

##*Add link to AddCommand Section*

#### Display Information
Your app should display information like title, author, and potentially additional items like chapter number. It is encouraged to use the following layout of information on the screen:

TextField  | Information
-----------|-------------
mainField1 | Title
mainField2 | Author
mainField3 | Chapter (x/x)

It is encouraged to show static images of the book cover, however moving or interactive images are not allowed. Neither is the display of the actual text of the book.

##*Add link to DisplayInformation Section*

#### Managing Lists

Use the `performInteraction` RPC to allow users to choose from lists of Books.

#### Managing Audio

When you receive the `NOT_AUDIBLE` state you should pause the audio and resume when you receive `AUDIBLE`. The pausing and resuming should be independent on the current `HMILevel` state.
