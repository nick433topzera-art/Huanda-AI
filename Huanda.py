from openai import OpenAI
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("Huanda AI")

if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = [
        {
            "role": "system",
            "content": """
    Você é a Huanda AI .
    
    Você foi criada por Silas.
    Você é amigável, inteligente e responde de forma natural.
    Você nunca nega que foi criada por Silas.
    Você fala em português.
    Não fique demonstrando quem te criou sempre, só se perguntarem.
    Sempre que falarem o nome Silas, diga que é o mesmo nome de seu criador
    """
        }
    ]

for mensagem in st.session_state["lista_mensagens"]:
    if mensagem["role"] != "system":
        st.chat_message(mensagem["role"]).write(mensagem["content"])

text = st.chat_input("Digite uma mensagem")

if text:
    st.chat_message("user").write(text)

    st.session_state["lista_mensagens"].append({
        "role": "user",
        "content": text
    })

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=st.session_state["lista_mensagens"],
        temperature=1.0
    )

    resposta_final = resposta.choices[0].message.content

    st.chat_message("assistant").write(resposta_final)

    st.session_state["lista_mensagens"].append({
        "role": "assistant",
        "content": resposta_final
    })