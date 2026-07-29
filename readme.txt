Asimanshu Samal — CV Website (Streamlit)

A personal CV/portfolio site built with Streamlit, meant to be deployed
via Streamlit Community Cloud.

RUN LOCALLY
------------
pip install streamlit
streamlit run app.py

DEPLOY ON STREAMLIT COMMUNITY CLOUD
------------------------------------
1. Push app.py (and a requirements.txt containing just "streamlit") to a GitHub repo.
2. Go to https://share.streamlit.io and sign in with GitHub.
3. Click "New app", pick your repo/branch, and set the main file path to app.py.
4. Click "Deploy" — you'll get a live URL in a minute or two.

PAGES IN THIS APP
------------------
- Home       : intro + quick stats
- About      : short bio (fill in)
- Education  : IIT (ISM) Dhanbad details + schooling (fill in)
- Skills     : technical + other skills (fill in)
- Projects   : projects/internships (fill in)
- Contact    : email, LinkedIn, GitHub (fill in)

NEXT STEPS
----------
- Fill in your bio on the About page
- Add real education details (batch, CGPA)
- List actual skills relevant to mining engineering
- Add real projects/internships
- Update contact links
- Optionally add a profile photo with st.image()
