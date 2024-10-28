"""
Scripts on this file are dedicated to defining the MainSiteHTML and
OutputSiteHTML objects. Such objects are placeholders for site-specific HTML
tags and their related properties.

Inconsistent HTML tagging across national sections' websites made it necessary to find a
workaround for scrapping different sites with different tags without repeating
any code.

The idea is to pre-define a site's Main Site HTML tagging and Output Site HTML
tagging and have the web scrapping functions take such pre-configurations as
arguments. HTML tagging can vary across the same site due to updates of the
website, multiple developers, etc. Therefore, the task of web scrapping the
websites form national sections involves: 

1. Assuring the HTML tagging (as set for this document) is the same before
webscrapping. If not, incorporate changes.

2. Assuring the HTML tagging is the same for all outputs in a single website.
If not, incorporate changes and scrape in groups. 

3. If there is an additional site/section where a section publishes outputs,
change configuration appropiately. 

4. Compile outputs manually when sites have too few outputs so as to avoid HTML
tagging issues. 

5. Assuring web scrapping is only conducted for 'latest' (not included)
outputs, not for entire selection of a site. 

Note: All the objects in this list are unique configurations.
National sections that were not added to this document have the same configuration
as the Multisite, called MainAI (lines 140-165). 
Use the multisite configuration to scrape websites not included in this document.


For any questions or help, please feel free to send me an email
(seleneileana@gmail.com) and I will do my best to walk you through the
code/help you troubleshoot.
"""

class MainSiteHTML:
    """This class is intended to hold site-specific HTML tags and attributes.

    Args:
        
        output_tag (str) : Tag of main entries in an amnesty site. output_attrs
        (dict of strings): HTML properties identifying the tag. arrangement
        (string) : If arrangement is in pages, this should "pages". If
        arrangement is an infinite scroll, this should be "scroll".
        url_head(string): If arrangement is in pages, this should be the
        Amnesty search-tool link without the page number. Page numbers will be
        iteratively appended to this string to loop through all pages. If
        arrangement is an
            
        source_name (string) : String identifying this site.

        output_tag (string): String with HTML tag that identifies each output in
        the search-tool site.
         
        output_attrs (dict) : Dictionary identifying HTML attributes of
        each output in the search-tool site.

        link_in_out_tag (bool): Is the link (href attribute) in the output tag?
        link_tag (str) : String with HTML tag identifying the output URL.

        ⋮
        ⋮ (the rest of the x_tag, x_attrs arguments serve the same purpose as 
        ⋮  those so far described)
        ⋮

        link_prefix (str) : Some sites have incomplete URLs. For example, for
        an output with title T the URL can be "/T" instead of
        "https://www.amnesty.x/T", where x is a country code. The link_prefix
        is the omitted first part of the url string. In the example, the link
        prefix should be "https://www.amnesty.x". If URLs do contain the full 
        link then this argument should be an empty string.

        sele (bool) : Some sites (e.g. Amnesty France) contain JS code that
        redirects requests from url x to some predetermined site y non related
        to x, thus making it impossible to access the desired URLs using the
        requests library. The workaround is to access the URL via a headless
        Selenium connection. Set sele to True for these cases.
    """

    def __init__(self, url_head, source_name,
                 arrangement,
                 output_tag, output_attrs,
                 link_in_out_tag,
                 link_tag, link_attrs,
                 link_prefix,
                 date_tag, date_attrs,
                 title_tag, title_attrs,
                 excerpt_tag, excerpt_attrs,
                 sele):
        self.arrangement = arrangement
        self.url_head = url_head
        self.source_name = source_name
        self.output_tag = output_tag
        self.output_attrs = output_attrs
        self.link_in_out_tag = link_in_out_tag
        self.link_tag = link_tag
        self.link_attrs = link_attrs
        self.date_tag = date_tag
        self.date_attrs = date_attrs
        self.title_tag = title_tag
        self.title_attrs = title_attrs
        self.excerpt_tag = excerpt_tag
        self.excerpt_attrs = excerpt_attrs
        self.link_prefix = link_prefix
        self.sele = sele


class OutputSiteHTML:
    """
    This class is the output-specific equivalent of MainSiteHTML. It holds the 
    tags and attributes pertaining to particular features of an Amnesty output 
    in the HTML of a particular Amnesty site. To understand the arguments, 
    read the documentation for MainSiteHTML, since this class follows a similar 
    logic and naming convention.
    """

    def __init__(self, topics_tag, topics_attrs,
                 pdf_tag, pdf_attrs,
                 date_tag, date_attrs):
        self.topics_tag = topics_tag
        self.topics_attrs = topics_attrs
        self.pdf_tag = pdf_tag
        self.pdf_attrs = pdf_attrs
        self.date_tag = date_tag
        self.date_attrs = date_attrs

# ~ SITE CONFIGURATIONS ~
# ----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# AI Main Site (English) ~ https://amnesty.org/ ~
# -----------------------------------------------------------------------------
# this site works for: "https://www.amnesty.at/Suche?q=i&sorttype=DateDesc&category=Alle&page="


MainAI = MainSiteHTML(
    url_head="https://www.amnesty.org/en/search/page/",
    source_name="AI",
    arrangement="pages",
    output_tag="article",
    output_attrs={"class": "post post--result"},
    link_in_out_tag=False,
    # Used to be tag "a" and class "floating-anchor"
    link_tag="h1", link_attrs={"class": "post-title"},
    link_prefix="",
    # Used to be date_tag="span", date_attrs={},
    #date_tag="span", date_attrs={"class":"post-byline"}
    date_tag=False, date_attrs={},
    title_tag="h1", title_attrs={"class": "post-title"},
    excerpt_tag="div", excerpt_attrs={"class": "post-excerpt"},
    sele=False
)
OutputAI = OutputSiteHTML(topics_attrs={"class": "topics-container"},
                          topics_tag="div",
                          pdf_tag="a",
                          pdf_attrs={
                              "class": "btn btn--download btn--primary customSelect-input"},
                          # Used to be date_tag=False, date_attrs={}
                          date_tag="span", date_attrs={"class": "u-textRight"}
                          )


# -----------------------------------------------------------------------------
# AI Canada (English) ~ https://amnesty.ca/ ~ Main Site Tagging
# -----------------------------------------------------------------------------

                    #"https://www.amnesty.ca/search/*/page/19/?sort=date-desc" (page in the middle)
                    #FOR THIS SITE, ADD ARGUMENT URL TAIL: '?sort=date-desc'
MainCanadaEnglish = MainSiteHTML(url_head="https://www.amnesty.ca/search/*/page/",
                                 source_name="Amnesty Canada (English)",
                                 arrangement="pages",
                                 output_tag="article",
                                 output_attrs={"class": "post post--result"},
                                 link_in_out_tag=False,
                                 link_tag="a", link_attrs={"class": "floating-anchor"},
                                 link_prefix="",
                                 date_tag="span", date_attrs={},
                                 title_tag="h1", title_attrs={"class": "post-title"},
                                 excerpt_tag="div", excerpt_attrs={"class": "post-excerpt"},
                                 sele=False
                                 )

OutputCanadaEnglish = OutputSiteHTML(topics_attrs={"class": "topics-container"},
                                     topics_tag="div",
                                     pdf_tag="a",
                                     pdf_attrs={
                                         "class": "btn btn--download btn--dark"},
                                     date_tag=False, date_attrs={})


# -----------------------------------------------------------------------------
# AI Canada (French) ~ https://amniistie.ca/ ~ Main Site Tagging
# -----------------------------------------------------------------------------
#IN THIS WEBSITE, ARTICLES ARE ORGANIZED FROM ELDEST TO NEWEST. FOR LATTEST ARTICLES, GO TO THE LAST PAGE. 
MainCanadaFrench = MainSiteHTML(url_head="https://www.amnistie.ca/recherche?search=a&page=",
                                source_name="Amnesty Canada (French)",
                                arrangement="pages",
                                output_tag="article",
                                output_attrs={"role": "article"},
                                link_in_out_tag=False,
                                link_tag="a", link_attrs={"class": "typo--h4 search-result__title"},
                                link_prefix="https://www.amnistie.ca/",
                                date_tag="li", date_attrs={"class": "info-tags__item typo--subtitle2-thin"},
                                title_tag="a", title_attrs={"class": "typo--h4 search-result__title"},
                                excerpt_tag=False, excerpt_attrs={},
                                sele=False
                                )

OutputCanadaFrench = OutputSiteHTML(
    topics_attrs={"class": "content-footer__tags"},
    topics_tag="div",
    pdf_tag="attr_error_prompter",
    pdf_attrs={},
    date_tag=False, date_attrs={})

# -----------------------------------------------------------------------------
# AI UK ARTICLES
# -----------------------------------------------------------------------------

# Search tool of this site divides entries by articles, blogs, resources, etc.
# Each of this divisions entail a different url head.
# For articles use :
# ~
# https://www.amnesty.org.uk/search/%20a?type=article&sort_by=search_api_relevance&page=
# ~
#
# DOES NOT INCLUDE: "https://www.amnesty.org.uk/books", "https://www.amnesty.org.uk/search/%20?type=issue&sort_by=changed",
#  https://www.amnesty.org.uk/issues/words-that-burn, https://www.amnesty.org.uk/issues/words-burn-poets,
#  https://www.amnesty.org.uk/issues/higher-and-adult-education, 

MainUKEnglish = MainSiteHTML(url_head="https://www.amnesty.org.uk/search/%20?sort_by=changed&type=All&page=",  # URL varies, see website...
                             source_name="UK (English)",
                             arrangement="pages",
                             output_tag="div", output_attrs={"class": "views-row"},
                             link_in_out_tag=False,
                             link_tag="a", link_attrs={},
                             link_prefix="https://www.amnesty.org.uk",
                             date_tag=False, date_attrs={},
                             title_tag="a", title_attrs={},
                             excerpt_tag=False, excerpt_attrs={},
                             sele=False
                             )

OutputUKEnglish = OutputSiteHTML(topics_tag="ul", topics_attrs={"class": "tags clearfix"},
                                 pdf_tag="a", pdf_attrs={"class": "pdf"},
                                 date_tag=False, date_attrs={})



# -----------------------------------------------------------------------------
# AI UK RESOURCES
# -----------------------------------------------------------------------------

#"https://www.amnesty.org.uk/resources" (START AT 0)


MainUKRESOURCES = MainSiteHTML(url_head="https://www.amnesty.org.uk/resources?looking_for=All&audience=1629&issue_type=All&age_group=All&on_this_issue_teach=All&combine=&sort_by=created&sort_order=DESC&page=",  # URL varies, see website...
                             source_name="AI UK Resources",
                             arrangement="pages",
                             output_tag="div", output_attrs={"class": "listing__item listing__item--event contextual-region views-row"},
                             link_in_out_tag=False,
                             link_tag="a", link_attrs={},
                             link_prefix="https://www.amnesty.org.uk",
                             date_tag=False, date_attrs={},
                             title_tag="h3", title_attrs={"class":"event__title event__title--resources"},
                             excerpt_tag="div", excerpt_attrs={"class": "event__description"},
                             sele=False
                             )

OutputUKRESOURCES = OutputSiteHTML(topics_tag="li", topics_attrs={"class": "tags__item"},
                                 pdf_tag="dd", pdf_attrs={"class": "documents"},
                                 #or pdf_tag="dl", pdf_attrs={"class": "js-download-trigger"},
                                 date_tag="div", date_attrs={"class": "article-info"})


#"https://www.amnesty.org.uk/blogs/stories-rights?page=0#"
# -----------------------------------------------------------------------------
# AI USA
# -----------------------------------------------------------------------------

MainUSA = MainSiteHTML(url_head="https://www.amnestyusa.org/search/+/?fwp_paged=",
                       source_name="AI USA",
                       arrangement="pages",
                       title_tag="h4", title_attrs={"role": "heading"},
                       output_tag="a", output_attrs={"class": "row card-group d-flex mb-32"},
                       link_in_out_tag=True,
                       link_tag=False, link_attrs={},
                       date_tag="h5", date_attrs={"role": "heading"},
                       link_prefix="https://www.amnestyusa.org",
                       excerpt_tag="p", excerpt_attrs={"class": "body-3"},
                       sele=False
                       )


OutputUSA = OutputSiteHTML(topics_tag="att_error_prompter", topics_attrs=False,
                           pdf_tag="h5", pdf_attrs="mb-24 white-text black-bg padding-8 inline",
                           date_tag=False, date_attrs={}
                           )

# -----------------------------------------------------------------------------
# AI USA Resources for activists
# -----------------------------------------------------------------------------

MainUSA_RFA = MainSiteHTML(url_head="https://www.amnestyusa.org/take-action/resources-for-activists/",
                       source_name="AI USA",
                       arrangement="pages",
                       title_tag="a", title_attrs={"role": "h5"},
                       output_tag="li", output_attrs={"class": "bg-black text-white p-3 my-2"},
                       link_in_out_tag=False,
                       link_tag="a", link_attrs={"class": "h5"},
                       date_tag=False, date_attrs={},
                       link_prefix="",
                       excerpt_tag=False, excerpt_attrs={"class": "body-3"},
                       sele=False
                       )


OutputUSA_RFA = OutputSiteHTML(topics_tag="att_error_prompter", topics_attrs=False,
                           pdf_tag="att_error_prompter", pdf_attrs="",
                           date_tag=False, date_attrs={}
                           )

# -----------------------------------------------------------------------------
# AI Argentina
# -----------------------------------------------------------------------------

#FOR THIS SITE, ADD ARGUMENT URL TAIL: '?s=+' 
MainARG = MainSiteHTML(url_head="https://amnistia.org.ar/page/",
                       output_tag="article", output_attrs={"class": "article"},
                       title_tag="h1", title_attrs={"class": "title"},
                       excerpt_tag="p", excerpt_attrs={"class": "subtitle"},
                       arrangement="pages",
                       link_in_out_tag=False,
                       link_tag="a", link_attrs={"class": "btn-read-more"},
                       link_prefix="",
                       date_tag=False, date_attrs={},
                       source_name="AI Argentina",
                       sele=False
                       )

OutputARG = OutputSiteHTML(topics_tag="attr_error_prompter", topics_attrs={},
                           pdf_tag="attr_error_prompter", pdf_attrs={},
                           date_tag="time", date_attrs={})

# -----------------------------------------------------------------------------
# AI France
# -----------------------------------------------------------------------------

MainFRA = MainSiteHTML(
    url_head="https://www.amnesty.fr/search?keywords=a&page=",
    output_tag="div", output_attrs={"class": "src-client-components-Article-Small-__Small___SmallArticle"},
    title_tag="h1", title_attrs={"class": "src-client-components-Article-Small-__Small___Title"},
    date_tag="span", date_attrs="src-client-components-Article-Small-__Small___Date",
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="https://www.amnesty.fr",
    source_name="AI France",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=True
)

OutputFRA = OutputSiteHTML(
    topics_tag="attr_error_prompter", topics_attrs={},
    pdf_tag="attr_error_prompter", pdf_attrs={},  # PDFs are raw PDFs.
    date_tag=False, date_attrs={},
)

# -----------------------------------------------------------------------------
# AI Belgium
# -----------------------------------------------------------------------------

MainBEL = MainSiteHTML(
    url_head="https://www.amnesty-international.be/zoek/a?page=",
    output_tag="li", output_attrs={"class": "search-result"},
    title_tag="h3", title_attrs={"class": "title"},
    date_tag=False, date_attrs={},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="https://www.amnesty-international.be",
    source_name="AI Belgium",
    excerpt_tag="div", excerpt_attrs={"class": "search-snippet-info"},
    arrangement="pages",
    sele=False
)

OutputBEL = OutputSiteHTML(
    pdf_tag="a", pdf_attrs={"target": "_blank"},
    topics_tag="attr_error_prompter", topics_attrs={},
    date_tag=False, date_attrs={}
)

# -----------------------------------------------------------------------------
# AI Belgium French
# -----------------------------------------------------------------------------

MainBEL_F = MainSiteHTML(
    url_head="https://www.amnesty.be/spip.php?page=recherche&recherche=&debut_recherche=",
    output_tag="article", output_attrs={"class": "entry entry-teaser article hentry entry-w-button"},
    title_tag="p", title_attrs={"class": "h3-like entry-title"},
    date_tag=False, date_attrs={},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="https://www.amnesty.be/",
    source_name="AI Belgium (French)",
    excerpt_tag="div", excerpt_attrs={"class": "introduction entry-content"},
    arrangement="pages",
    sele=False
)


OutputBEL_F = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="ul", topics_attrs={"class": "list-inline tags"},
    date_tag="time", date_attrs={}
)

# -----------------------------------------------------------------------------
# Belgium HRE-Specific site
# -----------------------------------------------------------------------------

MainBEL_HRE = MainSiteHTML(
    url_head="https://jeunes.amnesty.be/jeunes/profs/plateforme/?debut_articles=",
    output_tag="article", output_attrs={"class": "entry entry-fichepedago article hentry"},
    title_tag="strong", title_attrs={"class": "h3-like entry-title"},
    date_tag=False, date_attrs={},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="https://jeunes.amnesty.be/",
    source_name="AI Belgium",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=False
)


OutputBEL_HRE = OutputSiteHTML(
        pdf_tag="article", pdf_attrs={"class": "entry document spip_doc pdf"},
    topics_tag="ul", topics_attrs={"class": "list-inline tags"},
    date_tag="time", date_attrs={"pubdate": "pubdate"}
)

# -----------------------------------------------------------------------------
# AI Mexico
# -----------------------------------------------------------------------------

# When using https://amnistia.org.mx/contenido/index.php/page/2/?s , ADD URL TAIL: '?s'
# When using (BETTER FOR LATER ENTRIES) https://amnistia.org.mx/contenido/index.php/2023/02/
# This archive does not incldue outputs from http://amnistia-educacion.org.mx/inicio/.
MainMEX = MainSiteHTML(
    url_head="https://amnistia.org.mx/contenido/index.php/2023/",
    output_tag="div", output_attrs={"class": "post-content ast-col-md-12"},
    title_tag="h2", title_attrs={"itemprop": "headline"},
    date_tag=False, date_attrs={},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="",
    source_name="AI Mexico",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=False
)

OutputMEX = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="attr_error_prompter", topics_attrs={},
    date_tag=False, date_attrs={}
)


# -----------------------------------------------------------------------------
# AI Kenya
# -----------------------------------------------------------------------------



MainKEN = MainSiteHTML(
    url_head="https://www.amnestykenya.org/page/",
    output_tag="article", output_attrs={"class": "result"},
    title_tag="h2", title_attrs={"class": "title"},
    date_tag=False, date_attrs={},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="",
    source_name="AI Kenya",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=False
)

OutputKEN = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="span", topics_attrs={"class": "meta-category"},
    date_tag="span", date_attrs={"class": "meta-date date updated"}
)


# -----------------------------------------------------------------------------
# AI Poland
# -----------------------------------------------------------------------------

#This archive does not include outputs in https://www.amnesty.org.pl/dzialaj/edukacja/. 
MainPOL = MainSiteHTML(
    url_head="https://amnesty.org.pl/aktualnosci/page/",
    #Used to be : output_tag="div", output_attrs={"class": "large-4 xxlarge-3 columns end"},
    #used to be title_tag="h4", title_attrs={},
    output_tag = "article", output_attrs= {"class": "post postImage--small"},
    title_tag="h1", title_attrs={"class": "post-title"},
    #used to be date_tag="div", date_attrs={"class": "date"},
    date_tag="span", date_attrs={"class": "post-meta"},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="",
    source_name="AI Poland",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=False
)

OutputPOL = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="div", topics_attrs={"class": "tags"},
    date_tag=False, date_attrs={}
)


# -----------------------------------------------------------------------------
# AI Spain
# -----------------------------------------------------------------------------

#DOES NOT INCLUDE: "https://redescuelas.es.amnesty.org/recursos-educativos/?tx_solr%5Bpage%5D=". modify code to apply both 
MainSPA = MainSiteHTML(
    url_head="https://www.es.amnesty.org/buscador/?tx_solr%5Bpage%5D=",
    output_tag="div", output_attrs={"class": "col-12 col-6@sm col-3@md"},
    title_tag="p", title_attrs={"class": "news-card__title"},
    date_tag="datetime", date_attrs={"class": "news-card__date"},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="https://www.es.amnesty.org/",
    source_name="AI Spain",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=False
)

OutputSPA = OutputSiteHTML(
    pdf_tag="a", pdf_attrs={"class":
                            "btn btn--download btn--primary customSelect-input"},
    topics_tag="ul", topics_attrs={"class": "tag__list"},
    date_tag=False, date_attrs={}
)

# -----------------------------------------------------------------------------
# AI European Union SITE
# -----------------------------------------------------------------------------


MainEuroUn = MainSiteHTML(
    url_head="https://www.amnesty.eu/latest-news/page/",
    #sometimes output_tag="article", output_attrs={"class": "post postImage--small aimc-ignore"},
    #sometimes output_tag="article", output_attrs={"class": "post postImage--small"},
    output_tag="article", output_attrs={"class": "post postImage--none"},
    title_tag="h1", title_attrs={"class": "post-title"},
    date_tag="span", date_attrs={"class": "post-meta"},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="",
    source_name="AI European Union",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=False
)

OutputEuroUn= OutputSiteHTML(
    pdf_tag="a", pdf_attrs={"class":
                            "btn btn--download btn--primary customSelect-input"},
    topics_tag="ul", topics_attrs={"class": "li"},
    date_tag=False, date_attrs={}
)



# -----------------------------------------------------------------------------
# LSITE EURASIA
# -----------------------------------------------------------------------------
#This archive does not include outputs in https://eurasia.amnesty.org/chto-my-delaem/obuchenie/

MainEURASIA = MainSiteHTML(
    url_head="https://eurasia.amnesty.org/category/content/page/",
    output_tag="article", output_attrs={"class": "post postImage--small aimc-ignore"},
    title_tag="h1", title_attrs={"class": "post-title"},
    date_tag="span", date_attrs={"class": "post-meta"},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="",
    source_name="AI Eurasia",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=False
    )

OutputEURASIA = OutputSiteHTML(
    pdf_tag="h3", pdf_attrs={"id":"документ"},
    topics_tag="li", topics_attrs={"style": "vertical-align: inherit;"},
    date_tag=False, date_attrs={}
)

# -----------------------------------------------------------------------------
# LSITE CHINESE
# -----------------------------------------------------------------------------

MainCHINESE = MainSiteHTML(
    url_head="https://zh.amnesty.org/category/content-type/educations/page",
    #post postImage--small OR "post postImage--small aimc-ignore" or post postImage--full
    output_tag="article", output_attrs={"class": "post postImage--full"},
    title_tag="h1", title_attrs={"class": "post-title"},
    date_tag="span", date_attrs={"class": "post-meta"},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="",
    source_name="AI Chinese",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=False
)

OutputCHINESE = OutputSiteHTML(
    pdf_tag="a", pdf_attrs={"class":"btn--input"},
    topics_tag="li", topics_attrs={"style": "vertical-align: inherit;"},
    date_tag=False, date_attrs={}
)

# -----------------------------------------------------------------------------
# LSITE FARSI
# -----------------------------------------------------------------------------

MainFARSI= MainSiteHTML(
    url_head='https://fa.amnesty.org/%d8%a7%d8%ae%d8%a8%d8%a7%d8%b1/page/',
    output_tag="article", output_attrs={},
    #or output_tag="article", output_attrs={"class": "post postImage--small"} 
    #or output_tag="article", output_attrs={"class": "post postImage--small aimc-ignore"}  
    #or output_tag="article", output_attrs={"class": "post postImage--none"}  
    title_tag="h1", title_attrs={"class": "post-title"},
    date_tag=False, date_attrs={},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="",
    source_name="AI Farsi",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=False
)
def farsi_topic_finder(element):
    parent = element.parent
    if parent.name == "li" and parent.parent.name == "ul":
        if element.name == "a" and "category" in element.get("href"):
            return True
    return False

OutputFARSI = OutputSiteHTML(
    pdf_tag="a", pdf_attrs={"class":"btn btn--download btn--dark"},
    topics_tag=farsi_topic_finder, topics_attrs={},
    date_tag=False, date_attrs={}
)


# -----------------------------------------------------------------------------
# AI MOROCCO
# -----------------------------------------------------------------------------
#ADD URL TAIL = '?s=+' as argument
MainMOROC = MainSiteHTML(
    url_head="https://www.amnesty.ma/page/",
    output_tag="article", output_attrs={},
    title_tag="h2", title_attrs={"class": "entry-title"},
    date_tag="div", date_attrs={"class": "date-meta"},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="https://www.amnesty.ma/",
    source_name="AI Morocco",
    excerpt_tag="div", excerpt_attrs={"class":"entry-summary"},
    arrangement="pages",
    sele=False
)

OutputMOROC = OutputSiteHTML(
    pdf_tag="a", pdf_attrs={"class":
                            "btn btn--download btn--primary customSelect-input"},
    topics_tag="ul", topics_attrs={"class": "tag__list"},
    date_tag=False, date_attrs={}
)

# -----------------------------------------------------------------------------
# AI Sweden
# -----------------------------------------------------------------------------
# This archive does not include outputs in https://skola.amnesty.se/lektioner/, 
# https://www.amnesty.se/elevportalen/, or https://skola.amnesty.se/search/?query=a

MainSWE = MainSiteHTML(
    url_head="https://www.amnesty.se/sokresultat/?q=a&page=",
    output_tag="li", output_attrs={"class": "news-list__item sticky"},
    title_tag="h4", title_attrs={"class": "news-list__heading"},
    date_tag=False, date_attrs={},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="",
    source_name="AI Sweden",
    excerpt_tag="p", excerpt_attrs={"class": "news-list__preamble"},
    arrangement="pages",
    sele=True
)

OutputSWE = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="attr_error_prompter", topics_attrs={},
    date_tag="attr_error_prompter", date_attrs={}
)


# -----------------------------------------------------------------------------
# AI Swizterland
# -----------------------------------------------------------------------------

# This site has a curious property. Page number one is indexed in the URL with
# the number 0, page 2 with 5, 3 with 10, etc...
# In general, page n is coded in the url as 5(n-1).
# This requires a slight modification of the main or the main_by_pages 
# functions.


MainSWI = MainSiteHTML(
    url_head="https://www.amnesty.ch/de/@@search?b_start:int=",
    output_tag="a", output_attrs={"class": "list-item"},
    title_tag="span", title_attrs={"class": "title"},
    date_tag="time", date_attrs="",
    link_in_out_tag=True,
    link_tag="a", link_attrs={},
    link_prefix="",
    source_name="AI Swizterland",
    excerpt_tag="font", excerpt_attrs={"style": "vertical-align: inherit;"},
    arrangement="pages",
    sele=False
)

OutputSWI = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="section", topics_attrs={"class": "portletContent tags"},
    date_tag=False, date_attrs={}
)


# -----------------------------------------------------------------------------
# AI Brazil
# -----------------------------------------------------------------------------

MainBRA = MainSiteHTML(
    url_head="https://anistia.org.br/informe-se/page/",
    output_tag="a", output_attrs={"class": "card card--button"},
    title_tag="h2", title_attrs={"class": "card-content-title"},
    date_tag="time", date_attrs={"class": "card-content-time"},
    link_in_out_tag=True,
    link_tag="a", link_attrs={},
    link_prefix="",
    source_name="AI Brazil",
    excerpt_tag="p", excerpt_attrs={"style": "card-content-text"},
    arrangement="pages",
    sele=False
)

OutputBRA = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="attr_error_prompter", topics_attrs={"class": "portletContent tags"},
    date_tag=False, date_attrs={}
)


# -----------------------------------------------------------------------------
# AI Paraguay
# -----------------------------------------------------------------------------

MainPAR= MainSiteHTML(
    url_head="https://amnesty.org.py/category/noticias/page/",
    output_tag="div", output_attrs={"class": "item-news"},
    title_tag="h3", title_attrs={},
    date_tag=False, date_attrs={},
    link_in_out_tag=False,
    link_tag="a", link_attrs={"class": "post-link"},
    link_prefix="",
    source_name="AI Paraguay",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=False
)

OutputPAR = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="span", topics_attrs={"class": "category"},
    date_tag="span", date_attrs={"class": "date"}
)


# -----------------------------------------------------------------------------
# AI Thailand
# -----------------------------------------------------------------------------

MainTHAI = MainSiteHTML(
    url_head="https://www.amnesty.or.th/en/search?search_paths%5B%5D=&query=+&page=",
    output_tag="div", output_attrs={"class": "searchResult"},
    title_tag="a", title_attrs={},
    date_tag=False, date_attrs={},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="",
    source_name="AI Thailand",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=False
)

OutputTHAI = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="attr_error_prompter", topics_attrs={},
    date_tag="div", date_attrs={"class": "date-blog"}
)

# -----------------------------------------------------------------------------
# AI Venezuela
# -----------------------------------------------------------------------------

MainVEN = MainSiteHTML(
    url_head="https://www.amnistia.org/ve/noticias/?page=",
    output_tag="div", output_attrs={"class": "cell small-12 medium-6 large-4 text-center aiven-card aiven-mb-3 aiven-vrule"},
    title_tag="h3", title_attrs={},
    date_tag="span", date_attrs={"class": "aiven-date-pub"},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="",
    source_name="AI Venezuela",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=False
)

OutputVEN = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="attr_error_prompter", topics_attrs={},
    date_tag=False, date_attrs={}
)


# -----------------------------------------------------------------------------
# AI Germany
# -----------------------------------------------------------------------------
# Used to be "https://www.amnesty.de/suche?keys=%20&sort_by=search_api_relevance&page="

MainGER = MainSiteHTML(
    url_head= "https://www.amnesty.de/suche?keys=%20&sort_by=sort_date&page=",
    output_tag="div", output_attrs={"class": "views-row"},
    #used to be title_tag="span", title_attrs={"class": "field-title"},
    title_tag="h2", title_attrs={"class": "search-result-item-title"},
    #used to be date_tag="h2", date_attrs={"class": "field-field-start-date"},
    date_tag="font", date_attrs={"style": "vertical-align: inherit;"},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="",
    source_name="AI Germany",
    excerpt_tag="div", excerpt_attrs={"class": "search-result-item-body"},
    arrangement="pages",
    sele=False
    )

OutputGER = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="attr_error_prompter", topics_attrs={},
    date_tag="span", date_attrs={"class": "headline-date"}
)

# -----------------------------------------------------------------------------
# AI Norway
# -----------------------------------------------------------------------------

MainNOR = MainSiteHTML(
    url_head="https://amnesty.no/for-aktivister?page=",
    output_tag="div", output_attrs={"class": "views-row"},
    title_tag="span", title_attrs={"class": "aktuelt-tittel"},
    date_tag=False, date_attrs={},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="https://amnesty.no/",
    source_name="AI Norway",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=False
)

OutputNOR = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="attr_error_prompter", topics_attrs={},
    date_tag="attr_error_prompter", date_attrs={}
)


# -----------------------------------------------------------------------------
# AI Korea I : Error
# -----------------------------------------------------------------------------

MainKOR = MainSiteHTML(
    url_head="https://amnesty.or.kr/tag/%ec%9d%b8%ea%b6%8c%ea%b5%90%ec%9c%a1/?ckattempt=",
    output_tag="a", output_attrs={"class": "poster-item poster-item-sm has-thumb"},
    title_tag="div", title_attrs={"class": "poster-title"},
    date_tag="div", date_attrs={"class": "poster-date"},
    link_in_out_tag=True,
    link_tag="a", link_attrs={"class": "poster-item poster-item-sm has-thumb"},
    link_prefix="",
    source_name="AI South Korea",
    excerpt_tag="div", excerpt_attrs={"class": "poster-excerpt"},
    arrangement="pages",
    sele=False
)


OutputKOR = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="span", topics_attrs={"class": "tag label label-primary"},
    date_tag=False, date_attrs={"class": "fecha"}
)


# -----------------------------------------------------------------------------
# AI Turkey 
# -----------------------------------------------------------------------------

MainTURK = MainSiteHTML(
    url_head="https://www.amnesty.org.tr/en-son?page=",
    output_tag="article", output_attrs={"class": "search-item"},
    title_tag="h1", title_attrs={"class": "search-item__title"},
    date_tag="time", date_attrs={"class": "search-item__date"},
    link_in_out_tag=False,
    link_tag="a", link_attrs={"class": "search-item__link"},
    link_prefix="",
    source_name="AI Turkey",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=False
)


OutputTURK = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="attr_error_prompter", topics_attrs={},
    date_tag=False, date_attrs={}
)

# -----------------------------------------------------------------------------
# AI Finland (Swedish)
# -----------------------------------------------------------------------------

MainFIN_SWE = MainSiteHTML(
    url_head="https://www.amnesty.fi/sv/s%C3%B6k/%20/Sida/",
    output_tag="article", output_attrs={"class": "post post--result"},
    title_tag="h1", title_attrs={"class": "post-title"},
    date_tag="span", date_attrs={"class": "post-byline"},
    link_in_out_tag=False,
    link_tag="a", link_attrs={"class": "floating-anchor"},
    link_prefix="",
    source_name="AI Finland (Swedish)",
    excerpt_tag="div", excerpt_attrs={"class": "post-excerpt"},
    arrangement="pages",
    sele=False
)


OutputFIN_SWE = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="div", topics_attrs={"class": "topics-container"},
    date_tag=False, date_attrs={}
)

# -----------------------------------------------------------------------------
# AI Slovenia (Slovenian)
# -----------------------------------------------------------------------------

MainSLO_SLO = MainSiteHTML(
    url_head="https://www.amnesty.si/novice?p=",
    output_tag="article", output_attrs={},
    title_tag="a", title_attrs={},
    date_tag="div", date_attrs={"class": "datum"},
    link_in_out_tag=False,
    link_tag="a", link_attrs={},
    link_prefix="https://www.amnesty.si/",
    source_name="AI Slovenia (Slovenian)",
    excerpt_tag="p", excerpt_attrs={},
    arrangement="pages",
    sele=False
)


OutputSLO_SLO = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="attr_error_prompter", topics_attrs={},
    date_tag=False, date_attrs={}
)

# -----------------------------------------------------------------------------
# AI Sweden
# -----------------------------------------------------------------------------

MainSWE = MainSiteHTML(
    url_head="https://www.amnesty.se/aktuellt/?page=",
    output_tag="li", output_attrs={"class": "news-list__item"},
    title_tag="h4", title_attrs={"class": "news-list__heading"},
    date_tag="span", date_attrs={"class": "news-list__date"},
    link_in_out_tag=False,
    link_tag="a", link_attrs={"class": "news-list__anchor"},
    link_prefix="https://www.amnesty.se/",
    source_name="AI Sweden",
    excerpt_tag="p", excerpt_attrs={"class": "news-list__preamble"},
    arrangement="pages",
    sele=True
)


OutputSWE = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="attr_error_prompter", topics_attrs={},
    date_tag=False, date_attrs={}
) 


# -----------------------------------------------------------------------------
# AI Switzerland (French)
# -----------------------------------------------------------------------------

MainSWI_FRE = MainSiteHTML(
    url_head="https://www.amnesty.ch/fr/@@search?b_start:int=",
    output_tag="a", output_attrs={"class": "list-item"},
    title_tag="span", title_attrs={"class": "title"},
    date_tag="time", date_attrs={},
    link_in_out_tag=True,
    link_tag=False, link_attrs={},
    link_prefix="",
    source_name="AI Switzerland (French)",
    excerpt_tag=False, excerpt_attrs={},
    arrangement="pages",
    sele=False
)


OutputSWI_FRE = OutputSiteHTML(
    pdf_tag="attr_error_prompter", pdf_attrs={},
    topics_tag="attr_error_prompter", topics_attrs={},
    date_tag=False, date_attrs={}
)
