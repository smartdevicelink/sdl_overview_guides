# SmartDeviceLink FAQ
Here are a few of the most common questions new developers have around the SmartDeviceLink project. 

- [Is WiFi a supported transport?](#is-wifi-a-supported-transport)
- [Can I implement custom HMI templates?](#can-i-implement-custom-hmi-templates)
- [Can I implement custom vehicle data messages?](#can-i-implement-custom-vehicle-data-messages)
- [What is the process for obtaining an App ID?](#what-is-the-process-for-obtaining-an-app-id)
- [Why does SDL require that I use templates for non-navigation applications?](#why-does-sdl-require-that-i-use-templates-for-non-navigation-applications)
- [I didn't find the answers I was looking for, where else can I look?](#i-didnt-find-the-answers-i-was-looking-for-where-else-can-i-look)

## Is WiFi a supported transport?<a id="is-wifi-a-supported-transport"></a>
WiFi transports are supported in two ways with various limitations. First, the production version is only available as a secondary transport. This means that a primary transport (such as Bluetooth or USB) has to be connected first in order for the TCP transport to connect.

Secondly, this transport can be used in the development and debugging phase of SDL integration and will act as the primary transport in that situation. For more information please see the evolution proposal [SDL 0141: Supporting simultaneous multiple transports](https://github.com/smartdevicelink/sdl_evolution/blob/master/proposals/0141-multiple-transports.md).

## Can I implement custom HMI templates?<a id="can-i-implement-custom-hmi-templates"></a>
This is possible, but not recommended as any app that builds itself for the head unit's custom template would not work with any other systems.  If new templates are desired, they should go through the SDL Evolution Process and be adopted by the project.

## Can I implement custom vehicle data messages?<a id="can-i-implement-custom-vehicle-data-messages"></a>
This is possible, but not recommended as any app that builds itself for the head unit's custom vehicle data types would not work with any other systems.  If new vehicle data types are desired, they should go through the SDL Evolution Process and be adopted by the project.

## What is the process for obtaining an App ID?<a id="what-is-the-process-for-obtaining-an-app-id"></a>
To obtain an App ID, you must first register for an account on the [SDL Developer Portal](https://smartdevicelink.com/register/), and then register the company to which the app should belong.  Once your company is registered, you can select the App IDs tab from your company profile and click the "Create New App ID" button to provide your app information and obtain your App ID.

## Why does SDL require that I use templates for non-navigation applications?<a id="why-does-sdl-require-that-i-use-templates-for-non-navigation-applications"></a>
Templates are the best way for you to design your application with the driver's safety in mind.  For more information on the benefits of templates, please see [this document](https://d83tozu1c8tt6.cloudfront.net/media/resources/templates_vs_video_streaming.pdf).

## I didn't find the answers I was looking for, where else can I look?<a id="i-didnt-find-the-answers-i-was-looking-for-where-else-can-i-look"></a>
Each project has documentation, guides, and may have their own FAQ that can help. If you still need help, please join the [SmartDeviceLink Slack team](http://slack.smartdevicelink.com/) and ask  your question.
