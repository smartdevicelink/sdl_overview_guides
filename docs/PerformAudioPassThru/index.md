## PerformAudioPassThru

`PerformAudioPassThru` feeds you with audio data through the vehicle’s microphone. The audio data could be used in cloud-based and on-line voice
recognition to achieve dynamic and diversified user interaction, like POI search, information query, or even record the voice when the driver is singing.
The audio data is in form of PCM, and its sampling rate, bit width, timeout can be set in the `PerformAudioPassThru` request per your requirement. The headunit transmits its supported parameters via the `registerAppInterface` response. 16bit/16kHz is a widely supported configuration, which delivers good audio quality.

The parameter `muteAudio` is used to define whether or not to mute current audio source during AudioPassThru session.

When the `PerformAudioPassThru` is used for voice recognition, `muteAudio` should be set to true to minimize audio interference.

If you want to mix the input audio from `PerformAudioPassThru` session with current audio source, eg. a karaoke app recording both the user's voice and the background music, you can set `muteAudio` to false.

`onAudioPassThru` keeps you updated with the audio data transfer every 250ms.

`EndAudioPassThru` enables you to end the audio capture, prematurely. This is useful if your app analyzes the audio level and detects that the user stopped speaking.

The format of audio data is described as follows:

- It does not include any header like RIFF header at the beginning.
- The audio sample is in linear PCM format.
- The audio data includes only one channel (i.e. monaural).
- For bit rates of 8 bits, the audio samples are unsigned. For bit rates of 16 bits, the audio samples are signed and are in little endian.
