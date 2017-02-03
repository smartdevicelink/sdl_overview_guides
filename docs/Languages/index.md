## Languages

### General Guidelines
As a developer, you will want to localize your application, via voice and on the display to match the experience with the rest of the user interface inside of the vehicle.

#### Localization and handling language changes

In order to properly handle language changes inside of the vehicle, we propose the following rules.  
1. Register your application with the language it currently supports on
the phone's user interface.
2. Check the display and voice language that the vehicle is currently
set to in the `RegisterAppInterface` response.
3. If your application does not support the language in the vehicle,
you may send commands as usual. By default if the user starts your application
in the vehicle, `the vehicle will notify the customer the languages
between the vehicle and phone does not match` and no other
steps are required.
4. If your application supports the language(s) in the response value,
send a `ChangeRegistration` message with the vehicle language and
proceed to adding your commands and bootstrapping your application.

#### Dynamic Switching of Languages:  

The best practice for your SDL integration is a dynamic switching of the Apps SDL language. The `RegisterAppInterface` RPC will report the head unit's language. If this language differs from the current language your App is set to, you should dynamically reload the strings in the language to that set in the head unit. The driver is used to the language in his car, therefore your app should be aligned with the language in the vehicle.  

Note: If dynamic switching of languages is not a possibility for your application (because you load strings dynamically from your backend based on the user profile language settings), you may still choose to keep your language. `The user will be informed from the head unit that the App's language differs from SYNC and that Voice commands will not work as expected.` Check out [Regional Language Switching](#regional-language-switching) section for best practices to minimize false notifications to the user.

#### App's TTSName

It is always important to keep in mind the voice engine in the head unit will always pronounce the given data according to the language it is set to.

```
Example:
App Name "Spotify" sounds like "Schpottifei" (which is not how the app name
is supposed to be pronounced) if the head unit is set to German.
```

To prevent your app name from being pronounced in from happening and for the user to be able to correctly activate your app via voice as well as for the head unit to correctly pronounce the App Name, you will have to use the two parameters `TTSName` and `VRSynonyms` in the `RegisterAppInterface`. Both fields have to be filled with a `String` that represents the pronunciation of your App name in the current language.  

```
Example:
Fill `TTSName`and one value of `VRSynonyms` with `Zppotifey` when the
Spotify connects to a German head unit to get the correct pronunciation
of the app name in German. This is the only way to enable the user to start
the app with the english pronunciation of Spotify and also allow the head
unit to pronounce name of the app correctly.
```

Note: The recommended best practice mentioned above must be followed only if the app name sounds wrong in the language the app switches to.

#### Regional Language Switching

If your app only supports one variant of English:  
You should update the registration information using the `changeRegistration` RPC (you don't have to re-register, because you don't have to change the `TTSName`). As soon as you get the information that the user's vehicle is set to a different regional version of the language, you should call the `ChangeRegistration` RPC with the actual regional variant that the user's vehicle is set to. There is no other change required.

```
Example:
App is set to "EN_US".
RegisterAppInterface reports the head unit is set to "EN_GB".
Use "ChangeRegistration(EN_GB, EN_GB)" to update the language.
Note: You don't have to update either "TTSName" or "VRSynonyms".
```

#### Persisted Languages

If your App's languages differs from your SDL languages, the App should store this different language and use it the next time it registers with the head unit.

The above recommendation also covers the use case where the user has his vehicle always set to a different language than the language on his mobile phone. If the app did not persist the language it would have to switch every time, which degrades the apps performance.  
