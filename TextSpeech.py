import azure.cognitiveservices.speech as speechsdk
import json

with open('Config.json', 'r' , encoding='utf-8') as f:
    ke = json.load(f)

def text_to_speech(text, lang, voice=None):

    key = ke["key_sp"]
    region = ke["region_sp"]

    speech_config = speechsdk.SpeechConfig(subscription=key, region=region)
    speech_config.speech_synthesis_language = lang

    if voice is not None:
        # Set the voice ID for the desired voice
        speech_config.speech_synthesis_voice_name = voice

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

    result = speech_synthesizer.speak_text_async(text).get()

    if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        #print("Texte converti en parole et lu avec succès.")
        pass
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("La conversion du texte en parole a été annulée: {}".format(cancellation_details.reason))
        res = "La conversion du texte en parole a été annulée:",cancellation_details.reason
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Erreur détaillée: {}".format(cancellation_details.error_details))
            return res, "\nErreur détaillée:",cancellation_details.error_details

if __name__ == "__main__":

    # Texte à convertir en parole
    text = """Titre : "La Bataille de l'Océan Gris"
    Date : 12 septembre 1812
    Auteur: inconnu . :. :. :. :. 
    
    Les canons tonnent, les voiles claquent,
    Sur la mer grise, la mort attaque.
    Les navires s'affrontent sans merci,
    Dans cette guerre qui n'a pas de répit.
    
    Les hommes se battent avec vaillance,
    Espérant sortir de cette tourmente.
    Leur courage est mis à rude épreuve,
    Mais ils tiennent bon malgré les écueils.
    
    Le sang coule sur le pont des navires,
    Les blessés crient et appellent leur mère.
    Mais la bataille continue sans fin,
    Chaque camp cherchant à vaincre son voisin.
    
    Au milieu de ce chaos indescriptible,
    Le ciel se fait noir, les dieux sont terribles.
    La tempête se lève, l'océan s'agite,
    Et les navires s'entrechoquent avec violence.
    
    Finalement, un silence pesant s'abat,
    Seules les vagues viennent s'échouer.
    Les survivants regardent autour d'eux,
    Le coeur lourd, l'âme en peine, le corps tremblant de peur.
    
    Car cette guerre navale a eu raison d'eux,
    Elle a laissé dans leur coeur un goût amer.
    Ils se souviendront toujours de cette journée,
    Où la mort les a frôlés de si près."""

    # Appeler la fonction text_to_speech
    text_to_speech(text,"fr-FR","fr-FR-AlainNeural")
