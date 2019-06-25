## PerformAudioPassThru

The `PerformAudioPassThru` RPC feeds you audio data from the vehicle’s microphone. The audio data can be used in cloud-based and on-line voice recognition to achieve dynamic user interaction, such as POI (point of interest) search, information query, or even record when the driver is singing. The audio data will be in uncompressed PCM format. The sampling rate, bit width, and timeout can be set, however, the supported parameters will be sent in the `registerAppInterface` response. Generally, 16 bit width, 16kHz sample rate will be supported.

The parameter `muteAudio` is used to define whether or not to mute current audio source during AudioPassThru session.

When the `PerformAudioPassThru` is used for voice recognition, `muteAudio` should be set to true to minimize audio interference.

If you want to mix the input audio from `PerformAudioPassThru` session with current audio source, eg. a karaoke app recording both the user's voice and the background music, you can set `muteAudio` to false.

`onAudioPassThru` keeps you updated with the audio data transfer every 250ms.

`EndAudioPassThru` enables you to end the audio capture prematurely. This is useful if your app analyzes the audio level and detects that the user has stopped speaking.

Additional notes about the audio data format:

- There is no header (such as a RIFF header).
- The audio sample is in linear PCM format.
- The audio data includes only one channel (i.e. monaural).
- For an 8 bit width, the audio data is unsigned. For a 16 bit width, it will be signed and little endian.