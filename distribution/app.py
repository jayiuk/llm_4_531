import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM


model_id = 'jayiuk/llm_4_531'
model = AutoModelForCausalLM.from_pretrained(model_id, trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_id)

st.title("간단한 5/3/1 운동 루틴 생성")

def get_answer(input):
    real_input = tokenizer(input, return_tensors="pt").to(model.device)
    output = model.generate(
    **real_input,
    max_new_tokens = 1024,
    do_sample = True,
    temperature = 0.1,
    top_p = 0.9,
    eos_token_id = tokenizer.eos_token_id
    )
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    st.write(response)
    return response

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("메시지를 입력하세요"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_answer(prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)