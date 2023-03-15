import streamlit as st 
import streamlit.components.v1 as components
from PIL import Image
from streamlit_timeline import timeline

with st.sidebar:
    image = Image.open("G:\\My Data\\personal photos\\forweb.jpg")
    st.image(image, width = 200)
    st.title("Harshit Wadhwani ")
    #components.html('<script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script><div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="harshitwadhwani" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/harshitwadhwani?trk=profile-badge">Harshit Wadhwani</a></div>', height = 310 )
    with open("HARSHIT WADHWANI CV .pdf", "rb") as file:
        btn = st.download_button(
                label="Download Resume",
                data=file,
                file_name="HARSHIT WADHWANI CV .pdf"
            )
        
st.title ("Intoduction")
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
             'headline' : 'Education',
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

st.title('Education')
timeline(jsonex, height=500 )


st.title("Certifications")
