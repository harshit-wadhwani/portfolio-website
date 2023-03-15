import streamlit as st 
import streamlit.components.v1 as components
from PIL import Image
from streamlit_timeline import timeline
import pandas as pd
import webbrowser
from bokeh.models.widgets import Div



st.set_page_config(page_title='Harshit Wadhwani', page_icon='🧊', layout="wide",initial_sidebar_state="expanded")

with st.sidebar:
    image = Image.open("static/forweb.jpg")
    st.image(image, width = 200)
    st.title("Harshit Wadhwani ")
    #components.html('<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="harshitwadhwani" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/harshitwadhwani?trk=profile-badge">Harshit Wadhwani</a></div>', height = 310 )
    if st.button("Linkedin 🧑‍💼"):
      js = "window.open('https://www.linkedin.com/in/harshitwadhwani/')"  # New tab or window
      html = '<img src onerror="{}">'.format(js)
      div = Div(text=html)
      st.bokeh_chart(div)  
    if st.button("Github 👨‍💻"):
      js = "window.open('https://github.com/harshit-wadhwani')"  # New tab or window
      html = '<img src onerror="{}">'.format(js)
      div = Div(text=html)
      st.bokeh_chart(div)  
    with open("static/HARSHIT WADHWANI CV .pdf", "rb") as file:
        btn = st.download_button(
                label="Download Resume 📥",
                data=file,
                file_name="static/HARSHIT WADHWANI CV .pdf"
            )
        
st.title ("Introduction 👨‍🎓")
st.write("Motivated and detail-oriented student with a strong foundation in Python programming and a passion for problem-solving, seeking opportunities to apply my skills and learn new technologies.")

st.title ("Skills ⚒️")
col1, col2, col3 = st.columns(3)

with col1:
    st.button('Python')
    st.button('Flask')
    
with col2:
    st.button("MySQL")
    st.button('Pandas')

with col3:
    st.button("Streamlit")
    st.button('NumPy')

jsonex = {'title' : {'media' : {
    'url' : 'https://img.freepik.com/free-photo/front-view-stacked-books-graduation-cap-diploma-education-day_23-2149241011.jpg?w=2000',
    'caption' : "",
    'credit' : ''
         },
         'text' : {
             'headline' : '',
             'text' : '<p>Educational Background</p>'
         }},
          'events':[
               {
        "media": {
          "url": r"https://upload.wikimedia.org/wikipedia/en/4/44/Ryan_International_Group_logo.png",
          "caption": "<p>      Ryan Internaltional School</p>"
        },
        "start_date": {
          "year": "2008"
        },
        "text": {
          "headline": "Ryan International School, Surat",
          "text": "Studied in Ryan International School From Class 1st to 6th, after which I shifted to another city."
        }
      },
                  {
        "media": {
          "url": r"https://play-lh.googleusercontent.com/E4ZfTtsuisAiM9H7jVGci-wmLN6o-xhCXIM6BwOvtrwP-FEFu6RDSewxPDu_5Z5-ig",
          "caption": "<p>      St. Aloysius sr. sec. School</p>"
        },
        "start_date": {
          "year": "2015"
        },
        "text": {
          "headline": "St. Aloysius sr. sec. School, Jabalpur",
          "text": "Studied in St. Aloysius sr. sec. School for Class 7th, after which I shifted to surat again."
        }
      },
        {
        "media": {
          "url": r"https://upload.wikimedia.org/wikipedia/en/4/44/Ryan_International_Group_logo.png",
          "caption": "<p>      Ryan Internaltional School</p>"
        },
        "start_date": {
          "year": "2018"
        },
        "text": {
          "headline": "Ryan International School, Surat",
          "text": "Studied in Ryan International School For Class 10th and Scored 78.8%"
        }
      },
        {
        "media": {
          "url": r"https://upload.wikimedia.org/wikipedia/en/4/44/Ryan_International_Group_logo.png",
          "caption": "<p>      Ryan Internaltional School</p>"
        },
        "start_date": {
          "year": "2020"
        },
        "text": {
          "headline": "Ryan International School, Surat",
          "text": "Studied in Ryan International School For Class 12th and Scored 88%"
        }
      }, 
        {
        "media": {
          "url": r"https://img.collegedekhocdn.com/media/img/institute/logo/dsi_logo.png",
          "caption": "<p>      Dayananda Sagar Academy of Technology and Management</p>"
        },
        "start_date": {
          "year": "2020"
        },
        "text": {
          "headline": "DSATM, Bengaluru",
          "text": "Pursuing Bachelors of engineering in Artificial Intelligence and Machine Learning"
        }
      }
                  
          ]
          }

#education
st.title('Education 🏫')
timeline(jsonex, height=500 )
data = [['10th', 'Not Applicable','CBSE','2018', '78.8%'],
        ['12th', 'Science (PCM)', 'CBSE', '2020', '88%'],
        ['Bachelors of Engineering', 'Artificial Intelligence and Machine Learning', 'DSATM (VTU)', '2024', '8.51 CGPA']]

df = pd.DataFrame(data, columns=['Qualification', 'Stream' , 'Institute', 'Year', 'Score'])
hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            </style>
            """
# Inject CSS with Markdown
st.markdown(hide_table_row_index, unsafe_allow_html=True)
st.table(df)

#Certification
st.title("Certifications")

col1, col2, col3 = st.columns(3)

with col1:
  if st.button('Crash Course on Python - Coursera'):
    #webbrowser.open('https://www.coursera.org/account/accomplishments/certificate/ZHMGLQXRRSSG')
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/ZHMGLQXRRSSG')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)   
  if st.button("Introduction to Git and GitHub"):
    #webbrowser.open('https://www.coursera.org/account/accomplishments/certificate/PWNWHE3NX2PN')
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/PWNWHE3NX2PN')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)     
  
  
with col2:
  if st.button("Using Python to Interact with the Operating System"):
    #webbrowser.open('https://www.coursera.org/account/accomplishments/certificate/CTZFB8SVEQA8')
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/CTZFB8SVEQA8')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)     
  if st.button('Clean Data in SQL using MySQL Workbench'):
    #webbrowser.open('https://www.coursera.org/account/accomplishments/certificate/NTDLB8L2VLFB')
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/NTDLB8L2VLFB')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)     
with col3:
  if st.button("Troubleshooting and Debugging Techniques"):
    #webbrowser.open('https://www.coursera.org/account/accomplishments/certificate/EEBXPHDN2NSL')
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/EEBXPHDN2NSL')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div) 
  if st.button('Programming for Everybody (Getting Started withPython)'):
    #webbrowser.open("https://www.coursera.org/account/accomplishments/certificate/28MEE66PT68D")
    js = "window.open('https://www.coursera.org/account/accomplishments/certificate/28MEE66PT68D')"  # New tab or window
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)     

st.title('Publications')
st.subheader('A Study on Real Time Video Analysis for Vehicle Traffic Movement')
st.write('International Journal of Engineering Research in Computer Science and Engineering (IJERCSE) · Dec 12, 2022')
st.write('The study explores techniques for detecting, tracking and counting vehicles, and provides insights into challenges and opportunities for improving the accuracy and efficiency of the process. The results have important implications for traffic management and reducing congestion.')
if st.button("Show Publication"):
  #webbrowser.open('https://www.technoarete.org/common_abstract/pdf/IJERCSE/v9/i12/Ext_50731.pdf')
  js = "window.open('https://www.technoarete.org/common_abstract/pdf/IJERCSE/v9/i12/Ext_50731.pdf')"  # New tab or window
  html = '<img src onerror="{}">'.format(js)
  div = Div(text=html)
  st.bokeh_chart(div)
  # st.bokeh_chart(open_link('https://www.technoarete.org/common_abstract/pdf/IJERCSE/v9/i12/Ext_50731.pdf'))

  
st.title('Projects')
st.subheader('Depression analysis using tweets')
st.write('Developed an application that extracts last 100 tweets of the users by their username on twitter. It then predicts the user\'s Depression and it also creates a word cloud of their tweets.')
if st.button('Show Project', key = 54):
  js = "window.open('https://github.com/harshit-wadhwani/Depression-analysis-using-tweets')"  # New tab or window
  html = '<img src onerror="{}">'.format(js)
  div = Div(text=html)
  st.bokeh_chart(div)  
  
  
st.subheader('Online Food Ordering System')
st.write('A web-based application for restaurant owners to receive orders from customers. Created using Streamlit and MySQL.')
if st.button('Show Project', key =55):
  js = "window.open('https://github.com/harshit-wadhwani/Online-food-ordering-system')"  # New tab or window
  html = '<img src onerror="{}">'.format(js)
  div = Div(text=html)
  st.bokeh_chart(div)  
  
st.subheader('AI gym trainer')
st.write('Developed a computer vision system using Mediapipe and OpenCV to accurately track and count bicep curls and correct posture during planks. Provides real-time feedback to users for correct exercise performance and injury prevention.')
if st.button('Show Project', key= 56 ):
  js = "window.open('https://github.com/harshit-wadhwani/AI-gym-trainer')"  # New tab or window
  html = '<img src onerror="{}">'.format(js)
  div = Div(text=html)
  st.bokeh_chart(div)  


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 