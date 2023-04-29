from SpeechToText import recognize_from_microphone
import TextSpeech as TS
import tradict
import json
import streamlit as st

with open('Config.json', 'r' , encoding='utf-8') as f:
    ke = json.load(f)
with open('senario.json', 'r', encoding='utf-8') as f2:
    senar = json.load(f2)

senar1 = list(senar["sanar1"])

st.title("SARTOTRADUCT - larguage")


def main():
    #introduction
    st.write("Si vous venez d'arriver sur cette application vous pouvez appuyer sur le bouton lancer l'instruction pour avoir l'introduction et les explications de l'utilisation de cette application ")
    if st.button("Lancer l'introduction  "):
        for i in range((len(senar1) + 1) // 2):
            if i * 2 < len(senar1):
                st.write("Maxime :", senar1[i * 2])
                er = TS.text_to_speech(senar1[i * 2], "fr-FR","fr-FR-ClaudeNeural")
                if str(er) != "None":
                    st.error(er)
            if i * 2 + 1 < len(senar1):
                st.write("Léa :", senar1[i * 2 + 1])
                er = TS.text_to_speech(senar1[i * 2 + 1], "fr-FR")
                if str(er) != "None":
                    st.error(er)

    st.write("---")
    options = ke["lang_id"].keys()
    selected_options = st.multiselect('Select Langues:', options)

    if st.button("Parler"):
        if selected_options == []:
            st.error("Sélectionner telle langue à traduire ")
        else:
            with st.spinner("Parler"):
                text = recognize_from_microphone()
            st.write("Vous avez dit : ", text)

            text = tradict.tradict(text,selected_options)

            st.write("\n=== traduction ===")
            for i1, i2 in enumerate(text):
                st.write(ke["lang_id"][i2]["name"])
                er = TS.text_to_speech(text[i2], ke["lang_id"][i2]["voi"])  # "fr-FR"
                if str(er) != "None":
                    st.error(er)

            st.write("=== end ===")
if __name__ == '__main__':
    main()

