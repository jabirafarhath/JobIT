
import streamlit as st
from PIL import Image


st.title("Coding Test")
st.subheader("Answer the questions given below.")


def show_coding_test():
    score = 0
    st.write("1. Determine the output of the C code mentioned below:")
    image = Image.open('images/code1.jpeg')
    st.image(image)
    ans1 = st.radio("", {"", "run time error", "a", "97.000000", "a.0000000"})
    score = score+1 if ans1 == "97.000000" else score

    st.write("2. What will be the output of the following C code?")
    image = Image.open('images/code2.jpeg')
    st.image(image)
    ans2 = st.radio("", {"", "Syntax error", "5, 2", "7, 2", "7, 4"})
    score = score+1 if ans2 == "Syntax error" else score

    st.write("3. The output of the C code mentioned below would be:")
    image = Image.open('images/code3.jpeg')
    st.image(image)
    ans3 = st.radio("", {"", " loop loop find loop",
                    "Infinite error", "find loop", "Compile time loop"})
    score = score+1 if ans3 == "find loop" else score

    st.write(
        "4. Out of the following function definition, which one will run correctly?")
    image = Image.open('images/code4.jpeg')
    st.image(image)
    ans4 = st.radio("", {"", "a", "b", "c", "d"})
    score = score+1 if ans4 == "b" else score

    st.write("5. The output of the C code mentioned below would be:")
    image = Image.open('images/code5.jpeg')
    st.image(image)
    ans5 = st.radio("", {"", "hello", "Compile time error", "5,30", "Varies"})
    score = score+1 if ans5 == "Compile time error" else score

    st.write("6. The output of the C code mentioned below would be:")
    image = Image.open('images/code6.jpeg')
    st.image(image)
    ans6 = st.radio("", {"", "33.3%", "75%", "25%", "50%"})
    score = score+1 if ans6 == "75%" else score

    st.write("7. The output of the C code mentioned below would be:")
    image = Image.open('images/code7.jpeg')
    st.image(image)
    ans7 = st.radio("", {"", "Compile error", "Hi", "HelloHi", "Hello"})
    score = score+1 if ans7 == "Compile error" else score

    st.write("8. What is the output of the following program?")
    image = Image.open('images/code9.jpeg')
    st.image(image)
    ans8 = st.radio("", {"", "Garbage character", "A", "65", "Compile error"})
    score = score+1 if ans8 == "A" else score

    st.write("9. What is the output of the following program?")
    image = Image.open('images/code10.jpeg')
    st.image(image)
    ans7 = st.radio("", {"", "0", "1", "2", "Compile error"})
    score = score+1 if ans7 == "2" else score

    st.write("10. What is the output of the following program?")
    image = Image.open('images/code8.jpeg')
    st.image(image)
    ans7 = st.radio("", {"", "Compile error", "Runtime error", "5", "10"})
    score = score+1 if ans7 == "10" else score

    ok = st.button("Submit")
    if ok:
        st.subheader("Coding test Score: ")
        st.subheader(score)


show_coding_test()
