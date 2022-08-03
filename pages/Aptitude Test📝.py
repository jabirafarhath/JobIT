import streamlit as st
import timer


score=0
ok=False

st.set_page_config()



def show_apti_test():
    score=0
    ans1 = st.radio("1. The speed of a car increases by 2 kms after every one hour. If the distance travelling in the first one hour was 35 kms. what was the total distance travelled in 12 hours?",{"","456 km","482 km","558 km","552 km"})
    score= score+1 if ans1=="552 km" else score

    ans2 = st.radio("2. Time taken by boat to travel a distance upstream is twice the time taken by it to travel the same distance downstream. If the boat travels 50 km in 4 hours 10 minutes in still water, then what is the speed of the boat downstream?",{"","8 km/hr","12 km/hr","15 km/hr","16 km/hr"})
    score= score+1 if ans2=="16 km/hr" else score

    ans3 = st.radio("3. A financier claims to be lending money at simple interest, But he includes the interest every six months for calculating the principal. If he is charging an interest of 10%, the effective rate of interest becomes.",{"","10.25%","10%","9.25%","9%"})
    score= score+1 if ans3=="10.25%" else score

    ans4 = st.radio("4. There is 80% increase in an amount in 8 years at simple interest. What will be the compound interest of 80% increase in an amount in 8 years at simple interest? What will be the compound interest of Rs. 14,000 after 3 years at the same rate?",{"","Rs.3794","Rs.3714","Rs.4612","Rs.4634"})
    score= score+1 if ans4=="Rs.4634" else score

    ans5 = st.radio("5. Two pipes A and B can fill a tank in 15 minutes and 20 minutes respectively. Both the pipes are opened together but after 4 minutes, pipe A is turned off. What is the total time required to fill the tank?",{"","10 min. 20 sec","11 min. 45 sec","12 min. 30 sec","14 min. 40 sec"})
    score= score+1 if ans5=="14 min. 40 sec" else score

    ans6 = st.radio("6. When Rajesh was born, his father age was 29 years older than his Brother and his Mother was 25 years older than his Sister. If his Brother is 2 years elder than his Sister. After 6 years the average age of the family is 20. Then what is the age of Mother when Rajesh was born?",{"","27","28","29","30"})
    score= score+1 if ans6=="28" else score

    ans7 = st.radio("7. 75 g of sugar solution has 30% sugar in it. Then, the quantity of sugar that should be added to the solution to make the quantity of the sugar 70% in the solution, is",{"","125 g","100 g","120 g ","130 g"})
    score= score+1 if ans7=="100 g" else score

    ans8 = st.radio("8. A committee has 5 men and 6 women. What are the number of ways of selecting 2 men and 3 women from the given committee?",{"","150","200","250","300"})
    score= score+1 if ans8=="200" else score

    ans9 = st.radio("9. A pack contains 4 blue, 2 red and 3 black pens. If 2 pens are drawn at random from the pack, NOT replaced and then another pen is drawn. What is the probability of drawing 2 blue pens and 1 black pen?",{"","2/14","1/14","6/17","8/12"})
    score= score+1 if ans9=="1/14" else score

    ans10 = st.radio("10. The four walls and ceiling of a room of length 25 ft., breadth 12 ft. and height 10 ft. are to be painted. Painter A can Paint 200 sqr.ft in 5 days, painter B can paint 250sqr.ft in 2 days. If A & B work together, in how many days do they finish the job?",{"","5 8/13","5 11/12","6 10/33","7 6/11"})
    score= score+1 if ans10=="6 10/33" else score


    ok = st.button("Submit")
    if ok:
        st.subheader("Aptitude Test score : ",)
        st.subheader(score)
    return score

    

    


    #st.write(score)


    

    

st.title("Aptitude Test")
st.subheader("Try to answer the questions below and press submit only when you finish answering all questions. A timer is provided at the end. Time limit is 8 mins. When the timer expires your score will displayed or once you submit you can view your score.")
show_apti_test()




