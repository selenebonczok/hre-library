import os 
import pandas as pd 
import streamlit as st
import base64

def set_bg_hack(main_bg):
    '''
    Unpack an image from root folder and set as bg.
    '''
    # set bg name
    main_bg_ext = "png"
        
    st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover;
             overflow: hidden
         }}
         </style>
         """,
         unsafe_allow_html=True
     )
    
COUNTRY_NAMES = [
    "Afghanistan", "Africa", "Albania", "Algeria", "Andorra", "Angola", "Argentina", "Armenia", "Australia",
    "Austria", "Azerbaijan", "Bahrain", "Bangladesh", "Belarus", "Belgium", "Benin", "Bolivia", "Botswana",
    "Brazil", "Bulgaria", "Burkina Faso", "Burundi", "Cambodia", "Cameroon", "Canada", "Chad", "Chile", "China",
    "Colombia", "Congo", "Côte d'Ivoire", "Croatia", "Cuba", "Cyprus", "Czech Republic", "Democratic Republic of the Congo",
    "Denmark", "Dominican Republic", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
    "Eswatini", "Ethiopia", "Fiji", "Finland", "France", "Gambia", "Georgia", "Germany", "Ghana", "Greece", "Guatemala",
    "Guinea", "Haiti", "Honduras", "Hungary", "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
    "Israel and Occupied Palestinian Territories", "Italy", "Japan", "Jordan", "Kazakhstan", "Kenya", "Kosovo", "Kuwait",
    "Kyrgyzstan", "Laos", "Latvia", "Lebanon", "Lesotho", "Libya", "Lithuania", "Madagascar", "Malawi", "Malaysia",
    "Maldives", "Mali", "Malta", "Mexico", "Middle East and North Africa", "Moldova", "Mongolia", "Montenegro",
    "Morocco and Western Sahara", "Mozambique", "Myanmar", "MOROCCO", "Namibia", "Nepal", "Netherlands", "New Zealand", "Nicaragua",
    "Niger", "Nigeria", "North America", "North Korea", "North Macedonia", "Norway", "Oman", "Pakistan", "Palestine",
    "Papua New Guinea", "Paraguay", "Peru", "Philippines", "Poland", "Portugal", "Puerto Rico", "Qatar", "Romania",
    "Russia", "Rwanda", "Saudi Arabia", "Senegal", "Serbia", "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
    "Somalia", "South Africa", "South America", "South Asia", "South Korea", "South Sudan", "Spain", "Sri Lanka",
    "Sudan", "Sweden", "Switzerland", "Syria", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo",
    "Trinidad and Tobago", "Tunisia", "Türkiye", "Turkmenistan", "Uganda", "Ukraine", "Uruguay","United Arab Emirates",
    "United Kingdom", "United States of America", "Zimbabwe", "EU"
]

def add_country_topic_column(df):
    # Convert all tags and country names to uppercase for case-insensitive comparison
    df['Tags'] = df['Tags'].apply(lambda tags: [tag.upper() for tag in tags])
    country_names_upper = [name.upper() for name in COUNTRY_NAMES]

    # Add a new column 'Country_Topic' and populate it based on matching tags with COUNTRY_NAMES
    df['Country_Topic'] = df['Tags'].apply(lambda tags: [tag for tag in tags if tag in country_names_upper])
    
    # Remove the matched country names from the 'Tags' column
    df['Tags'] = df.apply(lambda row: [tag for tag in row['Tags'] if tag not in row['Country_Topic']], axis=1)
    return df


def load_data(file_path):
    df = pd.read_csv(file_path)
    df = convert_columns_to_lists(df)
    df = transform_date_column(df)
    df = add_country_topic_column(df) 
    return df

def convert_columns_to_lists(df):
    # Convert columns with multiple values to lists
    df['Language'] = df['Language'].apply(lambda x: eval(x) if pd.notnull(x) else [])
    df['Tags'] = df['Tags'].apply(lambda x: eval(x) if pd.notnull(x) else [])
    df['Type'] = df['Type'].apply(lambda x: eval(x) if pd.notnull(x) else [])
    return df

def transform_date_column(df):
    # Transform the 'Date' column
    df['Date'] = df['Date'].apply(lambda x: x.split('/')[1] if pd.notnull(x) and '/' in x else 'Undated')
    return df

# Function to add a title and subtitle
def set_title():
    # Set the font style

    title_html = """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@300&display=swap');
            h1 {
                font-family: 'Oswald', sans-serif;
            }
        </style>
        <h1>       .        </h1>
    """
    st.markdown(title_html, unsafe_allow_html=True)

    
def sidebar_filters(df):
    st.sidebar.markdown("<h2 style='font-family: Oswald;'>FILTERS</h2>", unsafe_allow_html=True)

    # Extract individual values for each filter option
    individual_sources = list(df['Source'].unique())

    # Check for NaN values before exploding
    individual_languages = sorted(set(df['Language'].explode().dropna()))
    individual_tags = sorted(set(df['Tags'].explode().dropna()))
    individual_types = sorted(set(df['Type'].explode().dropna()))
    individual_years = sorted(set(df['Date'].unique()))

    # Create multiselects with individual values
    selected_source = st.sidebar.multiselect("Select Source", individual_sources)
    selected_language = st.sidebar.multiselect("Select Language", individual_languages)
    selected_tags = st.sidebar.multiselect("Select Tags", individual_tags)
    selected_types = st.sidebar.multiselect("Select Type", individual_types)
    selected_years = st.sidebar.multiselect("Select Year", individual_years)

    # Add keyword search
    keyword_search = st.sidebar.text_input("Keyword Search", "")

    return selected_source, selected_language, selected_tags, selected_types, selected_years, keyword_search

def apply_filters(df, selected_source, selected_language, selected_tags, selected_types, selected_years, keyword_search):
    # Apply filters to dataframe
    if selected_source:
        df = df[df['Source'].isin(selected_source)]
    if selected_language:
        df = df[df['Language'].apply(lambda x: any(lang in x for lang in selected_language))]
    if selected_tags:
        df = df[df['Tags'].apply(lambda x: any(tag in x for tag in selected_tags))]
    if selected_types:
        df = df[df['Type'].apply(lambda x: any(category in x for category in selected_types))]
    if selected_years:
        df = df[df['Date'].isin(selected_years)]

    # Apply keyword search (case insensitive)
    if keyword_search:
        keyword_search = keyword_search.lower()
        df = df[df.apply(lambda row: any(keyword in str(row).lower() for keyword in keyword_search.split()), axis=1)]
    
    # Sort the filtered DataFrame by the 'Date' column (assuming it contains years) in descending order
    df['Date'] = pd.Categorical(df['Date'], categories=sorted(df['Date'].unique(), key=lambda x: (x != 'Undated', x)), ordered=True)
    df = df.sort_values(by='Date', key=lambda x: x == 'Undated', ascending=True).sort_values(by='Date', ascending=False)
    
    return df

    
def display_results(filtered_df):
    #st.subheader("Your search results")

    # List of columns to hide from the user
    columns_to_hide = ['HRE Produced?', 'Keyword Matches', 'Excerpt', 'RawText', 'Comments']

    # Rename the 'Country_Topic' column to 'Country Topic'
    filtered_df = filtered_df.rename(columns={'Country_Topic': 'Country Topic'})

    # Display the filtered data excluding the specified columns
    #st.write(filtered_df.drop(columns=columns_to_hide))
    # Display the filtered data excluding the specified columns
    st.markdown(
        f"""
        <style>
            .dataframe {{
                width: 100% !important;
                max-width: none !important;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.dataframe(filtered_df.drop(columns=columns_to_hide), height=600, width=1700)
   
     
def main(file_path):
    st.set_page_config(layout="wide")
    
    set_title()
    set_bg_hack('try10.png')
   # Create a container for layout
    col1, col2 = st.columns([1, 9])
    df = load_data(file_path)
    selected_source, selected_language, selected_tags, selected_types, selected_years, keyword_search = sidebar_filters(df)
    filtered_df = apply_filters(df, selected_source, selected_language, selected_tags, selected_types, selected_years, keyword_search)
    display_results(filtered_df)
    
     # Add the YouTube video link in the sidebar under the filters
    youtube_video_url = "https://www.youtube.com/watch?v=_TpQubxoH50"  # Replace with your YouTube video URL
    st.sidebar.markdown("<h3 style='font-family: Oswald;'>TUTORIAL: HOW TO USE THIS DATABASE</h3>", unsafe_allow_html=True)
    st.sidebar.video(youtube_video_url)
    
     # Add the hyperlink to the satisfaction Form
    form_url = "https://forms.gle/aKAMtvkTjqctKShA9"  # Replace with your Google Form URL
    st.sidebar.markdown(f"<h3><a href='{form_url}' style='font-family: Oswald; color: #3498db;'>HELP US IMPROVE!", unsafe_allow_html=True)
    
    
if __name__ == "__main__":
    # Specify the local file path to your CSV file
    local_file_path = 'glibrary24m.csv'
    main(local_file_path) 

    

    
