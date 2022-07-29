import streamlit as st
import predict
import form
import mapping as map

st.title('JobIT')
input = form.show_form()
ok= 0
ok = st.button("Predict")
if ok:
    result = predict.predict(input)
    result = result[0]
    print(result)
    result = map.job_role[map.job_role['job_n']==result]['job'].values[0]
    st.subheader(result)


