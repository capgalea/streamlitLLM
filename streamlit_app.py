import streamlit as st
st.title("Hope4Her")
st.header("Your guide to be aware and get help on gender inequality related issues")
st.write("If you need help, click on the button and read the tips at the bottom:")
sexualAbuse = st.button("Sexual Abuse")
onlineAbuse = st.button("Online Abuse")
harassment = st.button("Harassment")
employment = st.button("Employment")
payRate = st.button("Pay Rate")
other = st.button("Other")
if sexualAbuse:
    st.write("Ways to get help:")
    st.write("Call 800-656-4673")
    st.write("Talk to your friends and family and see if they can help")
    st.write("Seek madical help")
    st.write("Create an exit plan")
if onlineAbuse:
    st.write("Ways to get help:")
    st.write("Block/Report person")
    st.write("Ignore the comments")
    st.write("Seek help")
if employment:
    st.write("Ways to get help:")
    st.write("Talk to your lawyer/agent")
    st.write("Talk to the person in charge of employment")
if harassment:
    st.write("Ways to get help:")
    st.write("Create distance from person")
    st.write("Stand up for what is right")
    st.write("Ignore")
if payRate:
    st.write("Ways to get help:")
    st.write("Talk to the boss")
    st.write("Find out more about your true pay")
    st.write("File a case at labor, commissioner office")
if other:
    st.write("Try to talk to friends and family about the issue")
    st.write("If it is necessary, call 911")
    st.write("You can look at this [link]""(https://www.legalmomentum.org/get-help-form#:~:text=The%20Syms%20Legal%20Momentum%20Gender,gender%20discrimination%2C%20violence%20and%20harassment)")
    
st.header("If you want to learn more about gender inequality, keep scrolling!")

st.write("Gender inequality oftens happens in families, realationships, public places, and at work")
st.write("The #1 cause of gender inequality is uneven acesses to education")
st.write("The state of Maryland has the lowest rate of gender inequality in the USA")
st.write("Lousiana has the highest rate of gender inequality in the USA")
st.write("Kenya has the highest rate of gender inequality worldwide")
st.write("Yemen has the lowest rate of gender inequality worldwide")

#www.statisa.com