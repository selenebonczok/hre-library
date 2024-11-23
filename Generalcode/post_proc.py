# Post-processing functions. 

import requests
import re
import os
import pandas as pd
from misc import connect
import bs4
import datetime


def has_keyword(text, keywords):
    """Returns true if any keyword in keywords is in text."""
    
    has = any(x.lower() in text.lower() for x in keywords)
    return has


def has_any_keyword(text_series, keywords):
    """Given a series (pandas column) of text entries, return a list of bools
    st the ith bool is True if the ith entry contains a keyword, and False
    otherwise."""
    bool_list = list(map(lambda x: has_keyword(x, keywords), text_series))
    return bool_list

def bool_cap(a, b):
    """Provided two lists of booleans a, b, with len(a) == len(b), return a 
    new list c such that c_i = True iff a_i = b_i = True, False otherwise.
    Equivalent to a ∩ b, if the lists are interpreted as sets."""
    cap = list(i == True and j == True for i, j in zip(a, b))
    return cap

def bool_cup(a, b):
    """Provided two lists of booleans a, b, with len(a) == len(b), return a 
    new list c such that c_i = True iff a_i = True or b_i = True, False otherwise.
    This is equivalent to a ∪ b, if a, b are interpreted as sets."""
    cup = list(i == True or j == True for i, j in zip(a, b))
    return cup

def amnesty_keyword_filter(df, x, y, z):
    """Provided an Amnesty data frame, return the list of entries that satisfy:
    a. Output had some keyword of x and some keyword of y,
    OR
    b. Output had some keyword of z.

    A set theory notation might be clear. Let A, B, C be the sets of entries
    containing at least a keyword in x, y, z respectively. Then this function
    performs the set operation
                                (A ∩ B) ∪ C                                """

    df = df[df['RawText'].notna()]
    series = df.RawText
    # Filter by existence of at least a keyword
    f1 = has_any_keyword(series, x)
    f2 = has_any_keyword(series, y)
    f3 = has_any_keyword(series, z)
    # Get entries with at least a keyword of x and a keyword of y
    f1_and_f2 = bool_cap(f1, f2)
    # Get entries satisfying the previous condition OR containing keyword in z.
    final_filter = bool_cup(f1_and_f2, f3)

    return df[final_filter]

def lapply_countries(func, new_fname, start_pattern=None, ignore=None,
                    condition=None):
    """Iterate over each country folder, apply a function to the main country 
    data frame, save transformed data frame into the same folder.

    If start_pattern is None, transformations will be applied to the first file
    found in folder. If start_pattern is a string, first .csv file starting with
    that string will be used.

    This post-processing function is specific to the folder organization used 
    by the original developer, and hence it may not generalize correctly to 
    other systems."""

    rootdir = os.getcwd() + "/countries"
    missed = []
    for subdir, dirs, files in os.walk(rootdir):
        print("At ", subdir)
        try:
            if len(files) == 0: #or any(f.startswith("kf") for f in files):
                continue
            if ignore is not None and any(f.startswith(ignore) for f in files):
                continue
            if start_pattern is not None:
                f = next(filter(lambda x: x.startswith(start_pattern), files))
            else:
                f = files[0]

            country = f[:-4] # Remove .csv from the string
            f = f if subdir in f else subdir + "/" + f
            df = pd.read_csv(f)
            if condition is not None: 
                if df.iloc[0][condition[0]] != condition[1]:
                    continue
            print("Applying function to ", f) 
            new_df = func(df)
            file_name = subdir + "/" + new_fname + "_" + country + ".csv"
            new_df.to_csv(file_name, index=False)
        except (AttributeError, StopIteration) as e:
            print(e)
            print("Missed ", subdir)
            missed.append(subdir)
            continue
    print("Missed countries: ")
    for x in missed:
        print(x)

def get_country_language(country):
    """
    Retrieve the primary language associated with a given country from the COUNTRIES_LAN dictionary.

    Args:
    - country (str): The name of the country for which we want to retrieve the language.

    Returns:
    - str: The primary language of the country if found; otherwise, an empty string.

    Note:
    The function expects COUNTRIES_LAN to be a global dictionary where keys represent languages and values are lists of 
    countries where the language is spoken. If multiple languages have the same country, the function will only 
    return the first language it encounters.
    """
    filtered_list = list(filter(lambda x: country in COUNTRIES_LAN[x], COUNTRIES_LAN))
    if len(filtered_list) > 0:
        lan = filtered_list[0]
        return lan
    else:
        return ''

def add_lan_col(df):
    """Adds the Language column to a data frame based on the source 
    amnesty site."""

    source = df.iloc[0].Source
    lan = get_country_language(source.lower())
    new_df = df.assign(Language=lan)
    return(new_df)

def get_edu_categories(text, categories):
    """Finds categories in a given text."""
    found_categories = []
    text = text.lower() # convert text to lower case

    for key in categories.keys():
        if any(word.lower() in text for word in categories[key]):
            found_categories.append(key.upper())

    return found_categories

def apply_get_edu_categories(df, categories, columns_to_search):
    """Get the categories representative of the values of each output on the 
    columns in columns_to_search. Assign such categories to the value of the 
    'Categories' column of that output. """
    for column in columns_to_search:
        df[column] = df[column].apply(lambda x: '' if pd.isnull(x) else x)
        df['Categories'] = df["Categories"].apply(lambda row: row if not pd.isnull(row["Categories"]) else
                                    get_edu_categories(row[column], categories))
            #if not row['Categories'] else row['Categories'], 
    return df
   

def declutter_filter (df, column, keywords, countries):
    """Remove from a data frame all entries where feature "column" contains some 
    keyword in keywords or starts with any pattern in countries.

    Both keywords and countries are lists. Column is a string with a column name."""

    countries = tuple([country.lower() for country in countries])
    #df = df.dropna(subset=column)
    f = lambda x: not(any(word.lower() in x.lower() for word in keywords) 
                      or x.lower().startswith(countries)
                      if not pd.isnull(x) else x)
    indexes = df[column].apply(f).tolist()
    return df.loc[indexes] #returns a subset of the original df

def is_hre_ytb(row, keywords, countries):
    """For YouTube content.

    Determine if a given row in an output data frame is HRE or not. 
    Determination is given by the Boolean formula 

                       X ∨ ¬(A ∨ B ∨ C) ≡ X ∨ ¬A ∧ ¬B ∧ ¬C

    where 

    A = output title contains a keyword in keywords 
    B = output title starts with a country name 
    C = output description starts with a country name
    X = output had strong or moderate indicators of being HRE Produced or its 
        title/description are empty.
    """
    
    if pd.isnull(row.Title) or pd.isnull(row.Description):
        return True 
    if row.HRERecommended is True or row.HREProduced is True:
        return True
    a = any(word.lower() in row.Title.lower() or row.Description.lower() 
                                   for word in keywords)
    b = any(row.Title.lower().startswith(country) for country in countries)
    c = any(row.Description.lower().startswith(country) for country in countries)

    return not(a or b or c)


def is_hre_web(row, keywords, countries):
    """For web content.

    Determine if a given row in an output data frame is HRE or not. 
    Determination is given by the Boolean formula 

                        X ∨ ¬(A ∨ B) ≡ X ∨ ¬A ∧ ¬B 

    where 

    A = output title contains a keyword in keywords 
    B = output title starts with a country name 
    X = output had strong or moderate indicators of being HRE Produced or its 
        title/description are empty.
    
    """    
    if pd.isnull(row['Title ENG']):
        return True
    if row.HRELikely is True or row.HREProduced is True:
        return True
    a = any(word.lower() in row['Title ENG'].lower() for word in keywords)
    b = any(row['Title ENG'].lower().startswith(country) for country in countries)
    return not (a or b)


def declutter_youtube (df, keywords, countries):
    """
    Filter out entries from a DataFrame where the "Title" or "Description" columns
    contain any of the specified keywords or start with any specified country pattern.
    
    Args:
    - df (pd.DataFrame): The input DataFrame.
    - keywords (list of str): List of keywords to filter out.
    - countries (list of str): List of country patterns to filter out from the beginning of the columns.
    
    Returns:
    - pd.DataFrame: A filtered DataFrame.
    """
    countries = tuple([country.lower() for country in countries])
    indexes = df.apply(lambda x: is_hre_ytb(x, keywords, countries), axis=1).tolist()
    return df.loc[indexes] #returns a subset of the original df


def declutter_web2 (df, keywords, countries):
    """
    Filter out entries from a DataFrame where the "Title" column
    contains any of the specified keywords or starts with any specified country pattern.
    
    Args:
    - df (pd.DataFrame): The input DataFrame.
    - keywords (list of str): List of keywords to filter out.
    - countries (list of str): List of country patterns to filter out from the beginning of the columns.
    
    Returns:
    - pd.DataFrame: A filtered DataFrame.
    """    
    countries = tuple([country.lower() for country in countries])
    indexes = df.apply(lambda x: is_hre_web(x, keywords, countries), axis=1).tolist()
    return df.loc[indexes] #returns a subset of the original df

def add_bool_column_based_on_keywords_ytb(df, new_column_name, keyword_list):
    """
    Add a boolean column to the DataFrame based on specified keywords. If any of the 
    keywords are found in the 'Title', 'Tags', or 'Description' columns, the new column 
    will be True, otherwise False.

    Args:
    - df (pd.DataFrame): The input DataFrame.
    - new_column_name (str): Name of the new boolean column to be added.
    - keyword_list (list of str): List of keywords to search for.

    Returns:
    - pd.DataFrame: The DataFrame with the added boolean column.
    """
    search_columns = ['Title', 'Tags', 'Description']
    df[new_column_name] = df[search_columns].apply(lambda x: 
                                                       any(has_keyword(text, keyword_list) 
                                                           for text in x if pd.notnull(text)), 
                                                           axis=1)
    return df

def add_bool_column_based_on_keywords_web(df, new_column_name, keyword_list):
    """
    Add a boolean column to the DataFrame based on the presence of specified keywords. 
    If any of the keywords are found in the search columns, the new column will be True, otherwise False.
    
    Note:
    The function currently searches in the columns: 'Title', 'Tags', 'RawText', 'Excerpt', and 'Link' 
    for English/Spanish content where there's no "Title ENG" column.
    
    Args:
    - df (pd.DataFrame): The input DataFrame.
    - new_column_name (str): Name of the new boolean column to be added.
    - keyword_list (list of str): List of keywords to search for.

    Returns:
    - pd.DataFrame: The DataFrame with the added boolean column.
    """
    df[new_column_name] = df[search_columns].apply(lambda x: 
                                                       any(has_keyword(text, keyword_list) 
                                                           for text in x if pd.notnull(text)), 
                                                           axis=1)
    return df


def get_keywords_ytb(row, keywords):
    """Returns the keywords appearing in a YouTube output, whether in its tags, 
    its description, or its title."""
    if not row.HREProduced and not row.HRERecommended:
        return []
    found_in_title, found_in_des, found_in_tags = [], [], []
    if not pd.isnull(row.Title):
        found_in_title = [kw for kw in keywords_for_print if kw.lower() in row.Title.lower()]
    if not pd.isnull(row.Description):
        found_in_des = [kw for kw in keywords_for_print if kw.lower() in row.Description.lower()]
    if not pd.isnull(row.Tags):
        found_in_tags = [kw for kw in keywords_for_print if kw.lower() in row.Tags.lower()]
        
    found = list(set(found_in_title + found_in_tags + found_in_des))
    return found


def get_keywords_web(row, matching_keywords_web):
    """Returns the keywords appearing in a website output, whether in its tags, 
    its description, its link, its excerpt, its written content, or its title."""
    if not row.HREProduced and not row.HRELikely:
        return []
    found_in_tags, found_in_Link, found_in_Excerpt, found_in_RawText,found_in_Title_ENG= [], [], [], [], []

    if not pd.isnull(row['Title ENG']):
        found_in_Title_ENG= [kw for kw in matching_keywords_web if kw.lower() in row['Title ENG'].lower()]
    if not pd.isnull(row.Link):
        found_in_Link = [kw for kw in matching_keywords_web if kw.lower() in row.Link.lower()]
    if not pd.isnull(row.Tags):
        found_in_tags = [kw for kw in matching_keywords_web if kw.lower() in row.Tags.lower()]
    if not pd.isnull(row.Excerpt):
        found_in_Excerpt = [kw for kw in matching_keywords_web if kw.lower() in row.Excerpt.lower()]
    if not pd.isnull(row.RawText):
        found_in_RawText = [kw for kw in matching_keywords_web if kw.lower() in row.RawText.lower()]

    found = list(set(found_in_tags +  found_in_Link + found_in_Excerpt + found_in_RawText + found_in_Title_ENG))

    return found


def has_year(element, date_pattern, tag, class_attr):
    "Determines if an HTML element has a year."
    match = re.search(date_pattern, element.text)
    try:
        if bool(match) and (tag.name == tag or class_attr in tag.get("class")):
            return True
    except TypeError:
        if bool(match) and (tag.name == tag):
            return True
    return False

def find_missing_dates(df, source, date_pattern, tag, class_attr):
    """
    Finds the dates that were not found on the first web-scrapping process via 
    a stronger but also more complicated query. `date_pattern` should be a 
    regex specifying the date pattern to query. `tag` is the HTML tag containin 
    non-exclusively the date. `class_attr` is the class attribute non-exclusively
    associated to the date.

    The function parses all elements in the HTML that have the given tag and 
    class attribute, many of which may not contain a date, and applies the 
    has_year function to filter for the date-containing element. This function 
    solves the problem arising from dates not being found because the tag 
    associated to a given date in the MainSiteHTML or OutputSiteHTML objects 
    is non-exclusively associated to the date.
    
    example usage: 
    result_df= extract_data(df, "AI UK", r'\d{1,2} \w+ \d{4}', "p", "article-info")
    result_df= extract_data(df, "AI POLAND", r'\d{2}/\d{2}/\d{4}', "span", "Post publication timestamp")
    """
    # Create a new dataframe to store results
    result_df = pd.DataFrame(columns=["URL", "FoundContent"])
    # Filter dataframe to only include rows where 'Source' is the specified source and 'Date' is NaN or empty
    df_filtered = df[(df['Source'] == source) & (df['Date'].isna() | (df['Date'] == ''))]
    for i in range(len(df_filtered)):
        link = df_filtered.iloc[i].Link
        if "files" in link:
            continue
        connection = connect(link)
        html = bs4.BeautifulSoup(connection.text)
        found_content = html.find_all(lambda x: has_year(x, date_pattern, tag, class_attr))
        result_df.loc[len(result_df)] = [link, found_content]

    return result_df

def add_hre_produced(df, new_column_name, keyword_list, is_eng_or_span):
        """Adds a boolean column based on keywords to a DataFrame. 
        The `is_eng_or_span` argument is a bool and should be set to true for 
        HRE outputs that are in English or Spanish. """
        search_columns = ['Title', 'Tags', "Link"] 
        if is_eng_or_span:
            search_columns = search_columns + ["RawText", "Excerpt"]
        
        df[new_column_name] = df[search_columns].apply(lambda x: 
                                                       any(has_keyword(text, keyword_list) 
                                                           for text in x if pd.notnull(text)), 
                                                           axis=1)
        return df

def extract_date_from_string(date_str, date_formats, date_regexes):
    """
    Extract a date from a given string based on the provided date formats and regular expressions.

    Args:
    - date_str (str): The string potentially containing a date.
    - date_formats (list of str): List of date formats to validate the date.
    - date_regexes (list of str): List of regular expressions corresponding to the date formats.

    Returns:
    - str or None: Extracted date string or None if no date is found.
    """
    if not isinstance(date_str, str):
        return None  # return None if the input is not a string
    for date_regex, date_format in zip(date_regexes, date_formats):
        match = re.search(date_regex, date_str)
        if match:
            date_str = match.group()
            try:
                # Try to parse the matched string as a date
                datetime.strptime(date_str, date_format)
                return date_str
            except ValueError:
                # If it's not a valid date, continue to the next format
                continue
    return None

def extract_date_from_url(url, date_formats, date_regexes):
    """
    Extract a date from a given URL.

    Args:
    - url (str): The URL potentially containing a date.
    - date_formats (list of str): List of date formats to validate the date.
    - date_regexes (list of str): List of regular expressions corresponding to the date formats.

    Returns:
    - str or None: Extracted date string or None if no date is found.
    """
    if url is None or pd.isnull(url):
        return None
    return extract_date_from_string(url, date_formats, date_regexes)

def apply_extract_date(df, date_formats, date_regexes):
    """
    Extract dates from the 'Link' column of a DataFrame and fill the 'Date' column. If no date is found in 'Link',
    try to extract it from the 'RawText' field.

    Args:
    - df (pd.DataFrame): The input DataFrame.
    - date_formats (list of str): List of date formats to validate the date.
    - date_regexes (list of str): List of regular expressions corresponding to the date formats.

    Returns:
    - pd.DataFrame: DataFrame with updated 'Date' column.
    """
    df_new = df.copy()
    df_new['Date'] = df_new.apply(
        lambda row: extract_date_from_url(row['Link'], date_formats, date_regexes) if pd.isnull(row['Date']) or row['Date'] == '' or row['Date'] == 'Inspection flag' or row['Date'] == "['not available']" else row['Date'], 
        axis=1
    )
    # If Date is still not found, try to extract it from the RawText field
    df_new['Date'] = df_new.apply(
        lambda row: extract_date_from_string(remove_ordinal_suffixes(row['RawText']), date_formats, date_regexes) if pd.isnull(row['Date']) or row['Date'] == '' or row['Date'] == 'Inspection flag' or row['Date'] == "['not available']" else row['Date'], 
        axis=1
    )
    return df_new

def extract_date_from_html(df, date_formats, date_regexes):
    """
    Extract dates from the 'Found Content' field of a DataFrame and populate the 'Date' column.

    Args:
    - df (pd.DataFrame): The input DataFrame.
    - date_formats (list of str): List of date formats to validate the date.
    - date_regexes (list of str): List of regular expressions corresponding to the date formats.

    Returns:
    - pd.DataFrame: DataFrame with a new or updated 'Date' column.
    """
    df_new = df.copy()
    
    # Create 'Date' column by extracting dates from the 'Found Content' field
    df_new['Date'] = df_new['Found Content'].apply(
        lambda content: extract_date_from_string(remove_ordinal_suffixes(content), date_formats, date_regexes)
    )
    
    return df_new

def standardize_date(date, date_formats):
    """
    Standardize a given date string to a specific format (either 'YYYY' or 'MM/YYYY').

    Args:
    - date (str): The date string to be standardized.
    - date_formats (list of str): List of date formats to validate and parse the date.

    Returns:
    - str: Standardized date string.
    """
    if pd.isna(date) or date == ['static'] or date == "static'":
        return date

    date_string = str(date).strip()  # Remove leading and trailing whitespaces
    
    for date_format in date_formats:
        try:
            parsed_date = datetime.strptime(date_string, date_format)
            
            # If the date only has year, leave it as it is
            if date_format == "%Y":
                standardized_date = parsed_date.strftime('%Y')
            else:
                standardized_date = parsed_date.strftime('%m/%Y')
                
            return standardized_date

        except ValueError:
            pass
    
    return 'fix_me' + date_string


def extract_title_from_url(url):
    """
    Extract the title of an article from its URL. The title is assumed to be the last part of the URL, 
    separated by dashes.

    Args:
    - url (str): The URL from which to extract the title.

    Returns:
    - str: Extracted title from the URL.
    """
    # Remove any query parameters from the URL
    clean_url = url.split('?')[0]

    # Extract the last part of the URL (after the last slash)
    url_parts = clean_url.split('/')
    last_part = url_parts[-1]

    # Split the last part into words
    words = last_part.split('-')

    # Convert words to title case and join them
    article_title = ' '.join(word.capitalize() for word in words)

    return article_title

def get_topics_from_title(text, url, tags, topics_dictionary):
    """
    Extract topics from the given text, URL, and tags based on a dictionary of topics. 
    The function checks for the presence of words associated with a topic in the input fields 
    and returns the matched topics.

    Args:
    - text (str): Text content to extract topics from.
    - url (str): URL to extract topics from.
    - tags (str or list): Existing tags to match topics and to return if no matches are found.
    - topics_dictionary (dict): A dictionary with topics as keys and associated words as values.

    Returns:
    - list: A list of matched topics in uppercase.
    """
    matched_keys = []

    if pd.notnull(text):
        text = text.lower()  # Convert text to lowercase
        # Match topics_dictionary from text
        for key in topics_dictionary.keys():
            for word in topics_dictionary[key]:
                if word.lower() in text:
                    matched_keys.append(key)

    if pd.notnull(url):
        url = url.lower()  # Convert URL to lowercase
        # Match topics_dictionary from URL link
        url_words = [word for word in url.split('/') if word]
        for key in topics_dictionary.keys():
            if any(word.lower() in url_words for word in topics_dictionary[key]):
                matched_keys.append(key)

    if pd.notnull(tags):
        tags = tags.lower()  # Convert tags to lowercase
        tag_words = tags if isinstance(tags, str) else [tag.lower() for tag in tags]
        # Match topics_dictionary from tags
        for key in topics_dictionary.keys():
            if any(word.lower() in tag_words for word in topics_dictionary[key]):
                matched_keys.append(key)

    if not matched_keys:
        return tags  # return original tags if no matches found

    # Combine original tags and new matches
    matched_keys = list(set(matched_keys))  # remove duplicates
    return [key.upper() for key in matched_keys]

def apply_get_topics(df, topics_dictionary):
    """
    Apply topic extraction to a DataFrame. For each row, topics are extracted from the 'Title', 'Link', 
    and 'Tags' fields, and populated into a new 'Tags' column.

    Args:
    - df (pd.DataFrame): The input DataFrame.
    - topics_dictionary (dict): A dictionary with topics as keys and associated words as values.

    Returns:
    - pd.DataFrame: DataFrame with an updated 'Tags' column containing extracted topics.
    """
    df_new = df.copy()
    df_new['Tags'] = df_new.apply(
        lambda row: get_topics_from_title(row['Title'], row['Link'], row['Tags'], topics_dictionary), 
        axis=1
    )
    return df_new


#FOR YOUTUBE TAGS ASSIGNMENT:

def get_topics_from_string_YTB(text, tags, Excerpt, topics_dictionary):
    """
    Extract topics from the given text, tags, and excerpt based on a dictionary of topics. 
    The function checks for the presence of words associated with a topic in the input fields 
    and returns the matched topics.

    Args:
    - text (str): Text content (typically a title) from which to extract topics.
    - tags (str or list): Existing tags to match topics and to return if no matches are found.
    - Excerpt (str): An excerpt from the content to further extract topics.
    - topics_dictionary (dict): A dictionary with topics as keys and associated words as values.

    Returns:
    - list: A list of matched topics in uppercase.
    """ 
    matched_keys = []

    if pd.notnull(text):
        text = text.lower()  # Convert text to lowercase
        # Match topics_dictionary from text
        for key in topics_dictionary.keys():
            for word in topics_dictionary[key]:
                if word.lower() in text:
                    matched_keys.append(key)

    if pd.notnull(tags):
        tags = tags.lower()  # Convert tags to lowercase
        tag_words = tags if isinstance(tags, str) else [tag.lower() for tag in tags]
        # Match topics_dictionary from tags
        for key in topics_dictionary.keys():
            if any(word.lower() in tag_words for word in topics_dictionary[key]):
                matched_keys.append(key)

    if pd.notnull(Excerpt):
        Excerpt = Excerpt.lower()  # Convert Excerpt to lowercase
        # Cut the Excerpt to only include the first 40 words
        Excerpt = ' '.join(Excerpt.split()[:40])
        # Match topics_dictionary from Excerpt
        for key in topics_dictionary.keys():
            for word in topics_dictionary[key]:
                if word.lower() in Excerpt:
                    matched_keys.append(key)

    if not matched_keys:
        return tags  # return original tags if no matches found

    # Combine original tags and new matches
    matched_keys = list(set(matched_keys))  # remove duplicates
    return [key.upper() for key in matched_keys]

def apply_get_topics_YTB(df, topics_dictionary):
    df_new = df.copy()
    df_new['Tags'] = df_new.apply(
        lambda row: get_topics_from_string_YTB(row['Title'], row['Tags'], row['Excerpt'], topics_dictionary), 
        axis=1
    )
    return df_new

def check_film_words(row, columns, film_words):
    """Checks if any of the film_words are in the columns of the row."""
    for col in columns:
        if pd.isnull(row[col]):
            continue
        if any(word.lower() in row[col].lower() for word in film_words):
            return False
    return row['HREProduced']

def update_hreproduced(df, film_words, columns_to_check):
    """Update 'HREProduced' column to FALSE if it's 'UNDEFINED' and any of the film_words are in the columns_to_check."""
    df['HREProduced'] = df.apply(
        lambda row: check_film_words(row, columns_to_check, film_words) if row['HREProduced'] == 'UNDEFINED' else row['HREProduced'], 
        axis=1
    )
    return df

 
def generate_links(original_link, language_codes):
    """
    Generate links based on the available languages for a given article on Amnesty International's website.

    Args:
    - original_link (str): The original link of the article in English.
    - language_codes (dict): A dictionary with language names as keys and their corresponding codes as values.

    Returns:
    - list: A list of available languages for the given article.
    """
    base_url = "https://www.amnesty.org/"
    original_part = original_link.split('en/', 1)[1]
    available_languages_for_link = ["ENGLISH"]

    for lang, code in language_codes.items(): # Get language and code
        new_url = base_url + code + '/' + original_part
        try:
            response = connect(new_url)
            if response.status_code == 200:
                available_languages_for_link.append(lang) # Append language instead of code
        except requests.exceptions.RequestException as e:
            print(f"An error occurred with URL: {new_url}. The error message is: {e}")
            print(f"Returning the list of available languages so far: {available_languages_for_link}")
            continue
            
    return available_languages_for_link


def generate_links_as_rows(row, language_codes):
    """
    Generate DataFrame rows based on the available languages for an article on Amnesty International's website.

    Args:
    - row (pd.Series): The row containing the original link and other details of the article.
    - language_codes (dict): A dictionary with language names as keys and their corresponding codes as values.

    Returns:
    - pd.DataFrame: A DataFrame containing rows for each available language version of the article.
    """
    base_url = "https://www.amnesty.org/"
    original_part = row['Link'].split('en/', 1)[1]
    rows_list = []

    for lang, code in language_codes.items(): # Get language and code
        new_row = row.copy()  # Copy original row
        new_url = base_url + code + '/' + original_part
        try:
            response = connect(new_url)
            if response.status_code == 200:
                new_row['Link'] = new_url  # Update Link
                new_row['Language'] = lang
                rows_list.append(new_row)
        except requests.exceptions.RequestException as e:
            print(f"An error occurred with URL: {new_url}. The error message is: {e}")
            continue
            
    return pd.DataFrame(rows_list)

