import numpy as np
import streamlit as st
import mapping as map
import predict


def show_form():
    st.write('Fill out details below')
    percent_OS = st.number_input("percentage in OS",max_value=100)
    percent_Alg = st.number_input("percentage in Algorithms",max_value=100)
    percent_Programming = st.number_input("percentage in Programming Concepts",max_value=100)
    percent_SE = st.number_input("percentage in Software Engineering",max_value=100)
    percent_CN = st.number_input("percentage in Computer Networks",max_value=100)
    percent_EC = st.number_input("percentage in Electronics",max_value=100)
    percent_COA = st.number_input("percentage in Computer Architecture",max_value=100)
    percent_Maths = st.number_input("percentage in Mathematics",max_value=100)
    percent_Communication = st.number_input("percentage in Communication Skills",max_value=100)

    hours_working = st.slider("Hours Working per day",min_value=4,max_value=12)

    logical_qoutient = st.slider("Logical Qoutient",min_value=1,max_value=10,)

    hackathons = st.radio("Participated in Hackathons",{'Yes','No'})
    hackathons = 1 if hackathons=="Yes" else 0

    coding_skills_rating = st.slider("Coding Skills",min_value=1,max_value=10)

    public_speaking_rating = st.slider("Public Speaking Skills",min_value=1,max_value=10,)

    long_hour_before_system = st.radio("Can you work long hours before the system?",{'Yes','No'})
    long_hour_before_system = 1 if long_hour_before_system=="Yes" else 0


    self_learning_capability = st.radio("Doyou have self learning Capability?",{'Yes','No'})
    self_learning_capability = 1 if self_learning_capability=="Yes" else 0

    extra_courses_did = st.radio("Have you done any extra courses?",{'Yes','No'})
    extra_courses_did = 1 if extra_courses_did=="Yes" else 0

    certificate = st.selectbox("Certifications",map.certifications)
    certificate = map.certifications[map.certifications['cert']==certificate]['cert_n'].values[0]

    workshops_done = st.selectbox("Workshops attended",map.workshops)
    workshops_done = map.workshops[map.workshops['workshops']==workshops_done]['workshops_n'].values[0]

    talent_test_taken = st.radio("Have you taken any talent tests",{'Yes','No'})
    talent_test_taken = 1 if talent_test_taken=="Yes" else 0
    
    olympiads = st.radio("Attended any Olympiads",{'Yes','No'})
    olympiads = 1 if olympiads=="Yes" else 0

    read_write_skills = st.selectbox("How do you define your reading and writing skills?",map.read_write)
    read_write_skills = map.read_write[map.read_write['read_write']==read_write_skills]['read_write_n'].values[0]

    memory_score = st.selectbox("How do you define your memory capability?",map.memory)
    memory_score = map.memory[map.memory['memory']==memory_score]['memory_n'].values[0]

    interested_subject = st.selectbox("Interested Subject",map.interested_sub)
    interested_subject = map.interested_sub[map.interested_sub['sub']==interested_subject]['sub_n'].values[0]
    
    interested_career_area = st.selectbox("Interested Career Field",map.interested_career)
    interested_career_area = map.interested_career[map.interested_career['career']==interested_career_area]['career_n'].values[0]

    job_or_higher = st.radio("Job or Higher Studies",{"Job","Higher Studies"})
    job_or_higher = 1 if job_or_higher=="Job" else 0

    type_of_company = st.selectbox("Type of Company you want to settle in",map.company)
    type_of_company = map.company[map.company['company']==type_of_company]['company_n'].values[0]

    inputs_from_senior = st.radio("Have you taken any advice or any other help from Seniors or Elders?",{"Yes","No"})
    inputs_from_senior = 1 if inputs_from_senior=="Yes" else 0

    games = st.radio("Interested in Games?",{"Yes","No"})
    games = 1 if games=="Yes" else 0

    interested_books= st.selectbox("Interest type of books",map.books)
    interested_books = map.books[map.books['books']==interested_books]['books_n'].values[0]

    relationship = st.radio("Are you in a relationship?",{"Yes","No"})
    relationship = 1 if relationship=="Yes" else 0

    gentle_stubborn = st.radio("How do you define yourself?",{"Gentle","Stubborn"})
    gentle_stubborn = 1 if gentle_stubborn=="Stubborn" else 0

    management_technical = st.radio("Management or Technical",{"Management","Technical"})
    management_technical = 1 if management_technical=="Technical" else 0

    salary_work = st.radio("Slary or Work",{"Salary","Work"})
    salary_work = 1 if salary_work=="Work" else 0

    hard_smart = st.radio("Hard or Smart",{"Hard Worker","Smart Worker"})
    hard_smart = 1 if hard_smart == "Smart" else 0

    teams = st.radio("Worked in teams?",{"Yes","No"})
    teams = 1 if teams=="yes" else 0

    intro_extro = st.radio("Introvert or Extrovert",{"Introvert","Extrovert"})
    intro_extro = 1 if intro_extro=="Introvert" else 0

    input =np.array([[percent_OS,percent_Alg,percent_Programming,percent_SE,percent_CN,percent_EC,percent_COA,percent_Maths,percent_Communication,hours_working,logical_qoutient,hackathons,coding_skills_rating,public_speaking_rating,long_hour_before_system,self_learning_capability,extra_courses_did,certificate,workshops_done,talent_test_taken,olympiads,read_write_skills,memory_score,interested_subject,interested_career_area,job_or_higher,type_of_company,inputs_from_senior,games,interested_books,relationship,gentle_stubborn,management_technical,salary_work,hard_smart,teams,intro_extro]]) 

    return input



    

    



  
