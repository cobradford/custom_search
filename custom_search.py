import streamlit as st
from googleapiclient.discovery import build

my_api_key = "AIzaSyAHps0PNi0OcHCDP1eepGxULEYjWCRfABI" #The API_KEY you acquired
my_cse_id = "c285ce83200073259" #The search-engine-ID you created


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    #res
    return res['items']

#st.sidebar.radio('Steps:', ('Step 1', 'Step 2', 'Step 3'))

req_skills = st.text_input("Must Have Skills:", value="Solutions Engineer")
pref_skills = st.text_input("Preferred Skills:", value="Google Cloud, Amazon, Machine Learning")
city = st.text_input("City/Area Code:", value="Seattle,206")
job_change = st.selectbox("Open to job change:", ("Yes","No"))
clever_terms = st.text_input("Clever Terms:", value="mentor, speaker, coach, patent")

overall_search = '"' + req_skills + '" (' + pref_skills.replace(",", " OR ") + ") (" + city.replace(",", " OR ") + ") (" + clever_terms.replace(",", " OR ") + ")"
st.subheader("Search Query")
overall_search

results = google_search(overall_search, my_api_key, my_cse_id, num=10)
for result in results:
    #result
    if ('og:image' in result['pagemap']['metatags'][0]):
        if ('ghost-images' in result['pagemap']['metatags'][0]['og:image']):
            if ('cse_thumbnail' in result['pagemap']):
                st.image(result['pagemap']['cse_thumbnail'][0]['src'], width=200)
            else:
                st.image(result['pagemap']['metatags'][0]['og:image'], width=200)
        else:
            st.image(result['pagemap']['metatags'][0]['og:image'])
    st.write('<a href="', result['link'], '">',result['htmlTitle'],'</a>', unsafe_allow_html=True)
    st.write(result['snippet'], unsafe_allow_html=True)
    st.markdown('---')
