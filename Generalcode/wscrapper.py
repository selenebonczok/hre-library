import bs4
import pandas as pd

# Addressing Jupyter's malfunction. The first import does not work in Jupyter 
# notebook's created at the root directory.
#try:
from misc import connect, sconnect, is_raw_pdf
#except ModuleNotFoundError:
#    from py.misc import connect, sconnect, is_raw_pdf

def crawl_main(url, site, debug=False):
    """Web crawler. Parse and return all URLs corresponding to 
    Amnesty outputs on a search query.

    Args :
    url : str
        URL of whichever site displays outputs.
    site : MainSiteHTML
        The HTML configuration of the site as specified on 
        scrapconf.py.
    """

    try:
        data = connect(url).text if site.sele is False else sconnect(url)
        html = bs4.BeautifulSoup(data, 'lxml')
        elements = html.find_all(site.output_tag, site.output_attrs)
        if debug:
            print("HTML RAW: \n\n", html, "\n\n\n Extracted elements: \n\n", elements)
        return elements
    except ConnectionError:
        print("Connection Error on {}: Skipping and returning []".format(url))
        # Prompt "No objects to concatenate". Not raising the ConnectionError
        # here directly allows for ignoring failing pages without interrupting
        # the iteration (see main functions at EOF).
        return []


def get_property(element, tag, attrs, to_get):
    """Helper function. Flexible wrapper for html.find().

    Equivalent to html.find() for an html element with the following
    difference. This function allows mapping None values to False. Useful in
    dealing with HTML configurations that lack some of the typical properties.

    Importantly, when no object is found with the given tag and attributes, 
    the string 'Inspection flag' is returned. This makes the function resilient
    to inconsistent HTML tagging in a given website. Otherwise, a scrapping 
    process, which may take many minutes, could be entirely disrupted by 
    an inconsistent tag.

    Args:
        element (bs4 object): A bs4 soup.
        tag (str): The tag of the query.
        attrs (str): The attributes of the tag of the query.
        to_get (str): Can be "text" or "href". Determines which of these two 
        properties are to be extracted from the queried object.
    Raises:
        ValueError: Whenever to_get not "text" or "href".
    """

    if tag is False:
        return None
    if to_get not in ("text", "href"):
        raise ValueError
    try:
        x = element.find(tag, attrs)
        y = x.text if to_get == "text" else x.get("href")
        # Parche. Ver Jupyter notebook.
        if y == None:
            y = x.find("a").get("href")
        return y
    # Surprisingly, some sites have (rare) outputs with inconsistent
    # title tagging. It becomes necessary to make the program resilient
    # to such anomalies.
    except AttributeError:
        return "Inspection flag"


def get_post_characteristics(element, site, output_site):
    """Gets the relevant features of an output.

    Given the bs4 soup of an output, examine its relevant tags in accordance
    to the Main Site and Output Site HTML configurations.
    Return extracted features in data frame format.

    Args:
        element (bs4 soup): [TODO:description]
        site (MainSite): A MainSite object with the tags and attributes
        that correspond to the desired features in an Amnesty main site.
        output_site (OutputSite): An OutputSite object with the tags and 
        attributes that correspond to the desired features in an Amnesty 
        output.
    """

    if site.link_in_out_tag:
        link = element.get("href")
    else:
        title_tag = element.find("h2", class_="post-title")
        link = title_tag.find("a")["href"] if title_tag else None
        #link = get_property(element, site.link_tag, site.link_attrs, "href")
    if link.startswith("https") is False:
        link = site.link_prefix + link
    date = get_property(element, site.date_tag, site.date_attrs, "text")
    title = get_property(element, site.title_tag, site.title_attrs, "text")
    excerpt = get_property(element, site.excerpt_tag,
                           site.excerpt_attrs, "text")
    if is_raw_pdf(title, link):
        props = (None, None, True, None)
    else:
        props = get_text_pdf_topics(link, output_site, sele=site.sele)

    topics, text, pdf, date = props[0], props[1], props[2], props[3]
    if output_site.date_tag is not False:
        date = props[3]

    dic = {"Title": title,
           "Source": site.source_name,
           "Link": link,
           "Excerpt": excerpt,
           "RawText": text,
           "Tags": topics,
           "Date": date,
           "PDF": pdf
           }

    return pd.DataFrame([dic])


def get_text_pdf_topics(url, site, sele):
    """Given the URL of an Amensty output, retrieves those features of the 
    output that are not accesible from the main site.

    Args:
        url (string): Output URL.
        site (MainSite): A MainSite object with the tags and attributes
        that correspond to the desired features in an Amnesty main site.
        sele (bool): Is Selenium required to parse the output site?
    """

    try:
        data = connect(url).text if not sele else sconnect(url)
    except ConnectionError:
        print("Unable to connect to ", url, "\nSkipping to next output.")
        return (None, "Inspection flag", False, None)
    html = bs4.BeautifulSoup(data, 'lxml')
    try:
        topics_container = html.find_all(site.topics_tag, site.topics_attrs)
        #a_topics = topics_container.findAll("a")
        topics = [x.text for x in topics_container]
    except AttributeError:
        topics = None   
    try:
        paragraphs = html.findAll("p")
        text = " ".join([x.text for x in paragraphs], )
    except AttributeError:
        text = "Inspection flag"
    try:
        pdf = not html.find(site.pdf_tag, site.pdf_attrs) is None
    except AttributeError:
        pdf = False

    date = None
    if site.date_tag is not False:
        try:
            date = get_property(html, site.date_tag, site.date_attrs, "text")
        except AttributeError:
            pass

    return (topics, text, pdf, date)


def df_from_site(url, main_site_conf, output_site_conf, debug=False):
    """ Given the URL of an Amensty search-query page,
    return a dataframe with the properties of each output in the site.

    Args:
        url (string): Link of the Amnesty site where outputs are listed.
        site (MainSite): A MainSite object with the tags and attributes
        that correspond to the desired features in an Amnesty main site.
        output_site (OutputSite): An OutputSite object with the tags and 
        attributes that correspond to the desired features in an Amnesty 
        output.
        debug (bool): Are we debugging? If true, HTML codes are printed for 
        inspection.
    """

    divs = crawl_main(url, main_site_conf, debug)
    chars = map(lambda x: get_post_characteristics(x, main_site_conf,
                                                   output_site_conf), divs)
    dfs = pd.concat(list(chars))
    return dfs

def main(s, n, main_site_conf, output_site_conf, url_tail="", interval=1, debug=False):
    """
    Main function. Given the URL head (.../page/), without a specified page,
    loops through all pages extracting features from all Amnesty outputs and
    returns a data frame with the features of them all. 

    Args:
        s (int): Page at which to start the iteration.
        n (int): Page at which to end the iteration.
        site (MainSite): A MainSite object with the tags and attributes
        that correspond to the desired features in an Amnesty main site.
        output_site (OutputSite): An OutputSite object with the tags and 
        attributes that correspond to the desired features in an Amnesty 
        output.
        url_tail (string): If the site's URL does not end with the page integer 
        but some tail, that tail must be included in this argument to avoid
        requesting an inexistent page.
        interval (int): Step of the iterator.
        debug (bool): Are we debugging? If true, HTML codes are printed for 
        inspection.
    """
    dfs, i = [], s
    missed = []
    for i in range(s, n + 1, interval):
        try:
            url = main_site_conf.url_head + str(i) + url_tail
            print("At page", str(i), " \n URL: ", url)
            df = df_from_site(url, main_site_conf, output_site_conf, debug)
            dfs.append(df)
        except ValueError as e:
            print(f"{e}. This page was omitted.")
            missed.append(main_site_conf.url_head + str(i))
            continue

    print("Missed pages : ")
    for x in missed:
        print(x)

    return pd.concat(dfs)

#   (1, 2, MainAI, OutputAI, "/?qyear=2024")
