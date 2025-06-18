# stralit app 
from dotenv import load_dotenv
load_dotenv() # laod all the environment variables

import streamlit as st
import os 
import sqlite3
import google.generativeai as genai

#configure out API key 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

#function to laod googel model and profile sql query as a response 

def get_gemini_response(question, prompt):
    model=genai.GenerativeModel("models/gemini-1.5-flash")
    response=model.generate_content([prompt[0],question])
    return response.text

## Function to retrieve query from the database 

def read_sql_query(sql,db):

    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define your prompt

prompt=[
    """
    You are an expert AI assistant specialized in converting natural language questions into SQL queries.

The SQL database is named **STUDENT** and contains the following columns:
- **NAME** (VARCHAR)
- **CLASS** (VARCHAR)
- **SECTION** (VARCHAR)
- **MARKS** (VARCHAR)

Please follow these guidelines when generating SQL queries:
1. Only return the SQL query — do not include explanations or extra formatting.
2. Use correct SQL syntax with a focus on accuracy and efficiency.
3. If filtering is required, apply appropriate `WHERE` clauses.
4. If aggregation is needed (e.g., counting records, averaging values), use SQL aggregate functions properly.

#### **Examples**
    
- **Question**: "How many student records are present?"
  - **SQL Query**: SELECT COUNT(*) FROM STUDENT;
- **Question**: "List all students in the genai class."
  - **SQL Query**: SELECT * FROM STUDENT WHERE CLASS = "genai";

Now, generate an SQL query for the given question 

    """
]

# stralit app 

# set page configuration with a title and icon 

st.set_page_config(page_title="SQL Query Generator | Huyreka", page_icon="??")

# Dispaly the Edureka Logo and header 
st.image("123.png", width=200)
st.markdown("? Huyreka's Gemini App - Your AI-Poweres SQL Assistant! ?")
st.markdown("? Ask any question, and I'll generate the SQL query for you! ?")



##User input for the question 
question = st.text_input("? Enter your query in plain English: ?", key="input")
#Submit button with 
submit = st.button("Generate SQL Query ")

# if summit button is clicked 
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    response=read_sql_query(response, "student.db")
    st.subheader("The Response is") 
    st.dataframe(response)
    #for row in response:
    #    print(row)
    #    st.write(row)
