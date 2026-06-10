Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.SetOutputToWaveFile("$PWD\assets\audio\hygiene_tip.wav")
$synth.Speak("Hello. This is your daily hygiene tip. Always wash your hands with soap and clean water for at least 20 seconds. Boil your drinking water, and clear stagnant water to prevent mosquitoes. Stay safe.")
$synth.Dispose()
