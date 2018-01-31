## PerformAudioPassThru

The `PerformAudioPassThru` RPC feeds you with audio data through the vehicle’s microphone. The audio data could be used in cloud-based and on-line voice
recognition to achieve dynamic and diversified user interaction, like POI (point of interest) search, querying for information, or even recording the driver's voice while they are singing. The audio data returned is formatted using the uncompressed PCM audio file format, and its sampling rate, bit width, timeout can be set in the `PerformAudioPassThru` request per your requirement. The headunit transmits its supported parameters via the `registerAppInterface` response. PCM/16bit/16kHz is a widely supported configuration, which delivers good audio quality.

The parameter `muteAudio` is used to define whether to mute current audio source during AudioPassThru session.

When the `PerformAudioPassThru` is used for voice recognition, `muteAudio` should be set to true to minimize audio interference.

If you want to mix the input audio from `PerformAudioPassThru` session with current audio source, eg. a karaoke app recording both the user's voice and the background music, you can set `muteAudio` to false.

`onAudioPassThru` keeps you updated with the audio data transfer every 250ms.

`EndAudioPassThru` enables you end the audio capture, prematurely. This is useful if your App analyzes the audio level and detects that the user stopped speaking.
