import streamlit as st


def show_verbal():
    score = 0

    st.title("Verbal Ability Test")
    st.subheader("Synonyms, Antonyms, Phrases and Idioms")
    ans1 = st.radio("Synonym for TEPID", {
                    "", "hot", "warm", "cold", "boiling"})
    score = score+1 if ans1 == "warm" else score

    ans2 = st.radio("Antoym for CONCEDE", {
                    "", "object", "refuse", "grant", "accedes"})
    score = score+1 if ans2 == "refuse" else score

    ans3 = st.radio("'To hit the nail right on the head' means", {
                    "", "To do the right thing", "To destroy one's reputation", "To announce one's fixed views", "To teach someone a lesson"})
    score = score+1 if ans3 == "To do the right thing" else score

    ans4 = st.radio("The waiter hasn't brought the coffee _____. I've been here an hour already.", {
                    "", "till", "up", "yet", "still"})
    score = score+1 if ans4 == "yet" else score

    ans5 = st.radio("Tractor : Trailer :: Horse : ?", {
                    "", "stable", "cart", "engine", "saddle"})
    score = score+1 if ans5 == "cart" else score

    st.subheader("Comprehensive Questions")
    st.write("Harold a professional man who had worked in an office for many years had a fearful dream. In it, he found himself in a land where small slug-like animals with slimy tentacles lived on people's bodies. The people tolerated the loathsome creatures because after many years they grew into elephants which then became the nation's system of transport, carrying everyone wherever he wanted to go. Harold suddenly realised that he himself was covered with these things, and he woke up screaming. In a vivid sequence of pictures this dream dramatised for Harold what he had never been able to put in to words; he saw himself as letting society feed on his body in his early years so that it would carry him when he retired. He later threw off the 'security bug' and took up freelance work.")
    ans6 = st.radio("In his dream Harold found the loathsome creatures _____", {
                    "", "in his village", "in his own house", "in a different land", "in his office"})
    score = score+1 if ans6 == "in a different land" else score

    st.subheader("Para Jumpled Questions")
    st.write("Directions: Rearrange the following six sentences (A), (B), (C), (D), (E), (F) and (G) in the proper sequence to form a meaningful paragraph and then answer the questions given below.")

    st.write()
    st.write()
    st.write("(A) The Royal Swedish Academy of Sciences said their work had shown how poverty could be addressed by breaking it down into smaller(B) and Michael Kremer of Harvard University have won the Nobel Prize for Economics Sciences for 2019.(C) The trio was awarded the Prize for their 'experimental approach to alleviating global poverty'.(D) and more precise questions in areas such as education and healthcare, making problems easier to solve.(E) It said the results of their studies and field experiments had ranged from helping millions of Indian school children with remedial tutoring(F) to encouraging governments around the world to increase funding for preventative medicine.(G) Kolkata-born Abhijit Banerjee, Ford Foundation Professor of Economics, Massachusetts Institute of Technology, his wife Esther Duflo, also from MIT")

    ans7 = st.radio("Which of the following should be the second sentence after rearrangement?", {
                    "", "C", "F", "B", "D", "E"})
    score = score+1 if ans7 == "B" else score

    st.subheader("Conclusions / Inference Questions")
    st.write("Direction: In each of the following question, some statements are given. They may be inferred from the main statement or not. Read both the statements carefully and mark:")
    st.write("")
    st.write("")
    st.write("The lifeline of Mumbai is it train network. One of the most crowded places in the city. A Group of commuters of the Mumbai suburban railways called for a strike in response to the increase in the number of accidents in that route in the past one year due to overcrowding. The commuters want to continue the strike unless the authorities agree to increase the frequency of the trains in that route.")

    ans8 = st.radio("Which of the following can be inferred from the above statement?", {"", " Increase in the frequency of the trains would lead to decrease in number of such accidents", "The trains in the Mumbai suburban run overcrowded ",
                    "The railway authorities are in different to the safety of commuters", "The railway did not increase the frequency in proportion to the increase in the number of commuters in the past one year", "None of these"})
    score = score+1 if ans8 == "The railway did not increase the frequency in proportion to the increase in the number of commuters in the past one year" else score

    st.subheader("Syllogism Questions")
    st.write("In the question, two statements are given, followed by two conclusions, I and II. You have to consider the statements to be true even if it seems to be at variance from commonly known facts. You have to decide which of the given conclusions, if any, follows from the given statements.")

    st.write("")
    st.write("")

    st.write("Statement--> 1) All clocks are watches. 2) Some clocks are alarm.")
    st.write("Conclusion--> 1) Some alarm are watches. 2) All watches are alarm.")
    ans9 = st.radio("", {"", "Only conclusion (I) follows", "Only conclusion (II) follows ",
                    "Both conclusion follow", "Neither conclusion (I) nor conclusion (II) follows ", "None of these"})
    score = score+1 if ans9 == "Only conclusion (I) follows" else score

    st.subheader("Completing Statements")
    st.write("In the question, an incomplete statement (Stem) followed by fillers is given. Pick out the best one which can complete incomplete stem correctly and meaningfully.")
    ans10 = st.radio("Despite his best efforts to conceal his anger _____", {"", "we could detect that he was very happy", "he failed to give us an impression of his agony",
                     "he succeeded in camouflaging his emotions", "he could succeed in doing it easily", "people came to know that he was annoyed"})
    score = score+1 if ans10 == "people came to know that he was annoyed" else score

    ok = st.button("Submit")
    if ok:
        st.subheader("Verbal Ability Score: ")
        st.subheader(score)


show_verbal()
