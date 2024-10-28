"""
This script is a repository for the global variables used in other scripts.

The global variables not used in the other places of  the source code were
(and may continue to be) used on Jupyter Notebooks. These notebooks are not
included in the source code because they are inessential to the system
developed in it.
"""

# ---
# Keyword system
#
# Keywords A and B are used principally in postproc.py. See the documentation
# of the amnesty_keyword_filter function on postproc.py for details on the
# purpose of these variables.

KEYWORDS_A = ["human rights education", "academy", "human rights educators",
              "educational", "instructional", "academy", "training",
              "teaching", "teachers", "instructive", "your school",
              "e-learning", " e learning",  " elearning", "online course",
              "teaching human rights","teach human rights", "classroom",
              "educator"]

KEYWORDS_B = ["manual", "workshop",  " guide ", "workbook", "booklet",
              "guidebook", "handbook", "compendium" , "podcast", "lesson",
              "seminar", "drill", "curriculum", "curricula", "module",
              "lecture", "video", "interactive" , "toolkit", "tool kit",
              "tool-kit", "resource"]

MASTER_KEYWORDS = ["human rights education", " HRE ", "human rights friendly school"
                   "human rights educators", "your school", "e-learning" , " e learning", " elearning",
                   "online course" , "training program", "Teacher’s Guide",  "course about", "courses about",
                   "classroom exercises", " learning resources", "for educator" "for teacher", "for teaching"]

MASTER_KEYWORDS_SPAN = ["educación en derechos humanos", "educación en DDHH",  "educación en DDHH", "educacion en DDHH", "academia",
                        "colegio amigo de los derechos humanos", "red de escuelas",
                        "educador sobre DDHH" "educador sobre derechos humanos",
                        "docente en derechos humanos", "docente en DDHH",
                        "docentes en derechos humanos", "educadores sobre derechos humanos",
                        "tu escuela", "tu colegio", "e-learning", "e-learning",
                        "e-learning", "curso en línea", "curso online", "de formación",
                        "formación en", "guía para profesores", "curso sobre", "cursos sobre",
                        "recursos de aprendizaje", "para educador", "para docente", "para enseñar",
                        "metodología educativa", "metodologia educativa", "metodologías educativas",
                        "metodologias educativas"]

KEYWORDS_A_SPAN = ["educación en derechos humanos", "educación en DDHH",  "educación en DDHH", "educacion en DDHH", "academia", "educador de derechos humanos", "educadores de derechos humanos", "educador sobre derechos humanos", "educadores sobre derechos humanos", "educativo", "instructivo",  "capacitación", "docencia", "docente", "maestro", "tu escuela", "e-learning", "e learning", "elearning", "curso en línea", "curso online", "enseñar derechos humanos", "para el aula", "educador", "facilitador", "participativa", "participativas", "pedagógic", "pedagogia", "pedagogía"]

KEYWORDS_B_SPAN = ["manual", "workshop",  "taller", "guia", "guía", "compendio", "podcast", "seminario", "ejercicio", "plan de estudios ", "módulo", "modulo", "conferencia", "video", "interactivo", "herramientas", "toolkit", "tool-kit", "tool kit", "recurso", "material para", "material sobre", "actividades", "clase sobre", "clases sobre", "clases en", "sesiones sobre", "sesión de", "sesión sobre", "sesiones de", "dinamica", "dinámica"]


# ---
# Dictionary with the languages of relevant countries.
COUNTRIES_LAN = {
        "French": ["france", "Amnesty Canada (French)", "argelia", "burkina faso", "mali"],
        "English": ["uk", "AI UK Resources", "UK (English)",
                    "Amnesty Canada (English)","usa", "ireland", "kenya", "nepal", "nigeria",
                    "philippines", "south africa"], "Hungarian": ["hungary"],
        "Slovakian": ["slovakia"],
        "German": ["austria", "germany", "AI Germany", "swizterland"],
        "Dutch": ["netherlands", "belgium"],
        "Spanish": ["argentina", "spain", "chile", "mexico", "puerto rico", "uruguay"],
        "Finish": ["finland"],
        "Czech": ["czechia"],
        "Danish": ["denmark"],
        "Polish": ["poland", "AI Poland"],
        "Icelandic": ["AI Iceland", "Iceland"],
        "Portuguese": ["AI Brazil"],
        "Turkish": ["AI Turkey"],
        "Russian":['AI Eurasia']

        }

# ---
#  Dictionary with the category name associated to particular keywords.
EDU_CATEGORIES = {
        'Academy': ['academy', 'e-learning', 'e learning', 'elearning', 'course',
                    'module', 'academia', 'e-learning', "MOOC", 'e learning',
                    'elearning', 'curso'],
        'Manuals': ['manual', 'guide', 'workbook', 'booklet', 'guidebook', 'handbook',
                    'compendium', 'MATERIAL ON ', 'MATERIAL for ', 'first step',
                    'Handbook', 'Curriculum', 'toolkit', 'pack', 'tool-kit', "game",
                    "juego","TEACHING RECOMMENDATION",'tool kit', 'leaflet', 'slides',
                    'PowerPoint', 'Session plan', 'activities',  "materiales de",
                    "Learning materials","template", 'activity', 'poster', 'Bite Size',
                    'Bitesize', 'Booklet', 'manual', 'guia', 'guía', 'compendio',
                    'toolkit', 'tool-kit', 'tool kit', 'material para', 'material'
                    'sobre', 'actividades', 'para el aula', 'actvidades', 'actividad'],
        'video': ['video', 'youtube', 'vimeo', 'film', 'Screening', 'movie', 'trailer',
                  'documentary', 'documentaries', 'multimedia'],
        'audio': ['audio', 'podcast', 'radio', 'escuchar'],
        'get involved': ['quiz', 'reading rebels', 'discussion', 'puzzle', 'Club',
                         'event', 'participate', 'contest', 'competition',
                         'register',"Join", "tour", "festival",'Inscription',
                         'Registration', 'form', 'sign up', 'sign-up', 'your school',
                         'como participar', 'cómo participar', 'clase sobre', 'clases sobre',
                         'clases en', 'sesiones sobre', 'sesion de', 'sesion sobre',
                         'sesión de', 'sesión sobre', 'sesiones de', 'tu escuela',
                         'tu colegio', 'colegio amigo de los DDHH',
                         'colegio amigo de los derechos humanos', 'red de escuelas'],

        'news and more': ['news', 'blog', 'event', 'conference', 'job search',
                          'job offer', 'vacancy', 'Jolie', 'camp ', 'Human Libraries',
                          'launches', 'Book review', 'evento', 'vacante', 'laboral',
                          'puesto de trabajo', 'puesto laboral'],
        'about': ["about hre", 'preguntas', 'questions', 'q&a']
        }

# ---
# Title starters that indicate the presence of news articles, press releases, and announcements 
TITLE_STARTERS =  ['amnesty international news','Amnesty International Newsletter', 'Afghanistan', 'Aland Islands', 'Albania', 'Algeria', 'American Samoa',
              'Andorra', 'Angola', 'Americas:','Anguilla', 'East Africa', 'West africa','Antarctica', 'Antigua and Barbuda',
              'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan',
              'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium',
              'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bonaire, Sint Eustatius and Saba',
              'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil',
              'British Indian Ocean Territory', 'Brunei Darussalam', 'Bulgaria', 'Burkina Faso',
              'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands',
              'Central African Republic', 'Chad', 'Chile', 'China', 'help','Christmas Island',
              'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Russian', 'Congo', 'Congo', 'Cook Islands',
              'Costa Rica', "Côte d'Ivoire", 'Croatia', 'Cuba', 'Curaçao', 'Cyprus', 'Czech Republic',
              'Czechia', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt',
              'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)',
              'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia',
              'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Gibraltar',
              'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea',
              'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Honduras', 'Hong Kong',
              'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel',
              'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', "Korea",
              'Kuwait', 'Kyrgyzstan', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein',
              'Lithuania', 'Luxembourg', 'Macao', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali',
              'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico',
              'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Myanmar', 'Namibia',
              'Nauru', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria',
              'Niue', 'Norfolk Island', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau',
              'Palestinian Territory, Occupied', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru',
              'Philippines', 'Pitcairn', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Réunion', 'Romania',
              'Russia', 'Gaza', 'Rwanda', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone','Singapore',
              'Slovakia', 'Slovenia ', 'Solomon Islands', 'Somalia',
              'South Africa', 'South Georgia and the South Sandwich Islands', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
              'South Sudan', 'Svalbard and Jan Mayen', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan',
              'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago',
              'Tunisia', 'Turkey', "Türkiye",'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'Emirates',
              'UAE', 'United Kingdom', 'UK', 'United States', 'USA', 'US', 'United States Minor Outlying Islands',
              'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Virgin Islands, British', 'Virgin Islands, U.S.',
              'Wallis and Futuna', 'Yemen', 'Zambia', 'Zimbabwe', 'Amnesty: Afghanistan', 'Amnesty: Aland Islands',
              'Amnesty: Albania', 'Amnesty: Algeria', 'Amnesty: American Samoa', 'Amnesty: Andorra',
              'Amnesty: Angola', 'Amnesty: Anguilla', 'Amnesty: Antigua and Barbuda', 'Amnesty: Argentina',
              'Amnesty: Armenia', 'Amnesty: Aruba', 'Amnesty: Australia', 'Amnesty: Austria', 'Amnesty: Azerbaijan',
              'Amnesty: Bahamas', 'Amnesty: Bahrain', 'Amnesty: Bangladesh', 'Amnesty: Barbados', 'Amnesty: Belarus',
              'Amnesty: Belgium', 'Amnesty: Belize', 'Amnesty: Benin', 'Amnesty: Bermuda', 'Amnesty: Bhutan',
              'Amnesty: Bolivia', 'Amnesty: Bosnia and Herzegovina', 'Amnesty: Botswana', 'Amnesty: Brazil',
              'Amnesty: Bulgaria', 'Amnesty: Burkina Faso', 'Amnesty: Burundi', 'Amnesty: Cambodia',
              'Amnesty: Cameroon', 'Amnesty: Canada', 'Amnesty: Cape Verde', 'Amnesty: Cayman Islands',
              'Amnesty: Central African Republic', 'Amnesty: Chad', 'Amnesty: Chile', 'Amnesty: China',
              'Amnesty: Colombia', 'Amnesty: Comoros', 'Amnesty: Congo', 'authorities',
              'Amnesty: Democratic Republic of the Congo', 'Amnesty: Costa Rica', "Amnesty: Côte d'Ivoire",
              'Amnesty: Croatia', 'Amnesty seeks', 'Amnesty: Cuba', 'Amnesty: Cyprus', 'Amnesty: Czech Republic', 'Amnesty: Denmark',
              'Amnesty: Djibouti', 'Amnesty: Dominican Republic', 'Amnesty: Ecuador', 'Amnesty: Egypt',
              'Amnesty: El Salvador', 'Amnesty: Equatorial Guinea', 'Amnesty: Eritrea', 'Amnesty: Estonia',
              'Amnesty: Ethiopia', 'Amnesty: Faroe Islands', 'Amnesty: Fiji', 'Amnesty: Finland',
'Amnesty: France', 'Amnesty: Georgia', 'Amnesty: Germany', 'Amnesty: Ghana', 'Amnesty: Gibraltar',
            'Amnesty: Greece', 'Amnesty: Greenland', 'Amnesty: Grenada', 'Amnesty: Guadeloupe',
            'Amnesty: Guatemala', 'Amnesty: Haiti', 'Amnesty: Honduras', 'Amnesty: Hong Kong',
            'Amnesty: Hungary', 'Amnesty: Iceland', 'Amnesty: India', 'Amnesty: Indonesia', 'Amnesty: Iran',
            'Amnesty: Iraq', 'Amnesty: Ireland', 'Amnesty: Israel', 'Amnesty: Italy', 'Amnesty: Jamaica',
            'Amnesty: Japan', 'Amnesty: Jordan', 'Amnesty: Kazakhstan', 'Amnesty: Kenya', 'Amnesty: Kiribati', 'Amnesty: Korea',
            'Amnesty: Kuwait', 'Amnesty: Kyrgyzstan', "Amnesty: Lao", 'Amnesty: Latvia', 'Amnesty: Lebanon',
            'Amnesty: Lesotho', 'Amnesty: Liberia', 'Amnesty: Libya', 'Amnesty: Maldives', 'Amnesty: Mali',
            'Amnesty: Malta', 'Amnesty: Marshall Islands', 'Amnesty: Mauritania', 'Amnesty: Mauritius',
            'Amnesty: Mexico', 'Amnesty: Mongolia', 'Amnesty: Montenegro', 'Amnesty: Morocco',
            'Amnesty: Mozambique', 'Amnesty: Myanmar', 'Amnesty: Namibia', 'Amnesty: Nepal', 'Amnesty: Netherlands',
            'Amnesty: New Zealand', 'Amnesty: Nicaragua', 'Amnesty: Niger', 'Amnesty: Nigeria', 'Amnesty: Norway',
            'Amnesty: Oman', 'Amnesty: Pakistan', 'Amnesty: Palau', 'Amnesty: Panama', 'Amnesty: Peru',
            'Amnesty: Philippines', 'Amnesty: Poland', 'Amnesty: Portugal', 'Amnesty: Puerto Rico',
            'Amnesty: Qatar', 'Amnesty: Russia', 'Amnesty: Rwanda', 'Amnesty: Saudi Arabia', 'Amnesty: Senegal',
            'Amnesty: Serbia', 'Amnesty: Seychelles', 'Amnesty: Sierra Leone', 'Amnesty: Singapore', 'Amnesty: Slovakia',
            'Amnesty: Slovenia', 'Amnesty: Somalia', 'Amnesty: South Africa', 'Amnesty: Spain', 'Amnesty: Sri Lanka',
            'Amnesty: Sudan', 'Amnesty: Suriname', 'Amnesty: South Sudan', 'Amnesty: Sweden', 'Amnesty: Switzerland',
            'Amnesty: Syria', 'Amnesty: Taiwan', 'Amnesty: Tajikistan', 'Amnesty: Tanzania', 'Amnesty: Thailand',
            'Amnesty: Togo', 'Amnesty: Tunisia', 'Amnesty: Turkey', 'Amnesty: Turkmenistan', 'Amnesty: Uganda',
            'Amnesty: Ukraine', 'Amnesty: Emirates', 'Amnesty: UK', 'Amnesty: United Kingdom', 'Amnesty: United States',
            'Amnesty: United States Minor Outlying Islands', 'Amnesty: Uruguay', 'Amnesty: Uzbekistan', 'Amnesty: Venezuela',
            'Amnesty: Vietnam', 'Amnesty: Yemen', 'Amnesty: Zambia', 'Amnesty: Zimbabwe', 'Amnesty: USA', 'Amnesty: US',
            'Amnesty International: Afghanistan', 'Amnesty International: Aland Islands', 'Amnesty International: Albania',
            'Amnesty International: Algeria', 'Amnesty International: American Samoa', 'Amnesty International: Andorra',
            'Amnesty International: Angola', 'Amnesty International: Anguilla', 'Amnesty International: Antigua and Barbuda',
            'Amnesty International: Argentina', 'Amnesty International: Armenia', 'Amnesty International: Aruba', 'Amnesty International: Australia',
            'Amnesty International: Austria', 'Amnesty International: Azerbaijan', 'Amnesty International: Bahamas', 'Amnesty International: Bahrain',
            'Amnesty International: Bangladesh', 'Amnesty International: Barbados', 'Amnesty International: Belarus',
            'Amnesty International: Belgium', 'Amnesty International: Belize', 'Amnesty International: Benin', 'Amnesty International: Bermuda',
            'Amnesty International: Bhutan', 'Amnesty International: Bolivia', 'Amnesty International: Bosnia and Herzegovina', 'Amnesty International: Botswana',
            'Amnesty International: Brazil', 'Amnesty International: Bulgaria', 'Amnesty International: Burkina Faso', 'Amnesty International: Burundi',
            'Amnesty International: Cambodia', 'Amnesty International: Cameroon', 'Amnesty International: Canada', 'Amnesty International: Cape Verde',
            'Amnesty International: Cayman Islands', 'Amnesty International: Central African Republic', 'Amnesty International: Chad', 'Amnesty International: Chile',
            'Amnesty International: China', 'Amnesty International: Colombia', 'Amnesty International: Comoros', 'Amnesty International: Congo', 'United Arab Emirates',
            'Amnesty International: Democratic Republic of the Congo', 'Amnesty International: Costa Rica', "Amnesty: Côte d'Ivoire", 'Amnesty International: Croatia',
            'Amnesty International: Cuba', 'Amnesty International: Cyprus', 'Amnesty International: Czech Republic', 'Amnesty International: Denmark',
            'Amnesty International: Djibouti', 'Amnesty International: Dominican Republic', 'Amnesty International: Ecuador', 'Amnesty International: Egypt',
            'Amnesty International: El Salvador', 'Amnesty International: Equatorial Guinea', 'Amnesty International: Eritrea', 'Amnesty International: Estonia', 'Amnesty International: Ethiopia',
            'Amnesty International: Faroe Islands', 'Amnesty International: Fiji', 'Amnesty International: Finland', 'Amnesty International: France',
            'Amnesty International: Georgia', 'Amnesty International: Germany', 'Amnesty International: Ghana', 'Amnesty International: Gibraltar',
            'Amnesty International: Greece', 'Amnesty International: Greenland', 'Amnesty International: Grenada', 'Amnesty International: Guadeloupe',
            'Amnesty International: Guatemala', 'Amnesty International: Haiti', 'Southern Africa', 'Amnesty International: Honduras', 'Amnesty International: Hong Kong',
            'Amnesty International: Hungary', 'Amnesty International: Iceland', 'Amnesty International: India', 'Amnesty International: Indonesia', 'Amnesty International: Iran',
            'Amnesty International: Iraq', 'Amnesty International: Ireland', 'Colômbia', 'Amnesty International: Israel', 'Amnesty International: Italy', 'Amnesty International: Jamaica',
            'Amnesty International: Japan', 'Amnesty International: Jordan', 'Amnesty International: Kazakhstan', 'Amnesty International: Kenya', 'Amnesty International: Kiribati',
            'Amnesty: Korea', 'Amnesty International: Kuwait', 'The International Criminal Court', 'Facts and figures', 'Amnesty International: Kyrgyzstan', 'Middle East', 'Amnesty: Lao',
            'Amnesty International: Latvia', 'Amnesty International: Lebanon',
            'Amnesty International: Lesotho', 'Amnesty International: Liberia', 'medical', 'FRY', 'DRC', 'ASEM','Zaire', 'Palestinian Authority','Federal Republic of ',
            'Amnesty International: Libya', 'Amnesty International: Maldives', 'Amnesty International: Mali',
            'Amnesty International: Malta', 'Amnesty International: Marshall Islands', 'Amnesty International: Mauritania', 'Amnesty International: Mauritius',
            'Amnesty International: Mexico', 'Human rights in','Amnesty International: Mongolia', 'Focus: ','Amnesty International: Montenegro', 'Amnesty International: Morocco',
            'Amnesty International: Mozambique', 'Amnesty International: Myanmar', 'East Timor', 'Bosnia', 'AI documents','Amnesty International: Namibia', 'Amnesty International: Nepal',
            'Amnesty International: Netherlands', 'Amnesty International: New Zealand', 'Amnesty International: Nicaragua', 'Amnesty International: Niger',
            'Amnesty International: Nigeria', 'Amnesty International: Norway', 'macedonia', 'justice for', 'Amnesty International: Oman',
              'Amnesty International: Pakistan', 'Amnesty International: Palau',
            'Amnesty International: Panama', 'Amnesty International: Peru', 'Amnesty International: Philippines', 'Amnesty International: Poland', 'Amnesty International: Portugal',
            'Amnesty International: Puerto Rico', 'Amnesty International: Qatar', 'Yugoslavia','Amnesty International: Russia', 'Amnesty International: Rwanda', 'Amnesty: Saudi Arabia',
            'Amnesty International: Senegal', 'Kosovo', 'Amnesty International: Serbia',  'Information for ','The death penalty: ', 'Amnesty International: Seychelles', 'Amnesty International: Sierra Leone',
            'Amnesty International: Singapore', 'Amnesty International: Slovakia','Republic of', 'People’s Republic of China', 'Amnesty International: Slovenia', 'Amnesty International: Somalia',
            'Amnesty International: South Africa', 'Amnesty International: Spain', 'Amnesty International: Sri Lanka', 'Amnesty International: Sudan',
            'Amnesty International: Suriname', 'Amnesty International: South Sudan', 'Amnesty International: Sweden', 'Amnesty International: Switzerland',
            'Amnesty International: Syria', 'Amnesty International: Taiwan', 'Brasil','Viet Nam','Kingdom of ','Amnesty International: Tajikistan', 'Amnesty International: Tanzania',
            'Amnesty International: Thailand', 'Amnesty International: Togo', 'Italia', 'Democratic', 'Amnesty International: Tunisia', 'Amnesty International: Turkey',
            'Amnesty International: Turkmenistan', 'Amnesty International: Uganda', 'Amnesty International: Ukraine', 'Amnesty International: Emirates',
            'Amnesty International: UK', 'Amnesty International: United Kingdom', 'Amnesty International: United States',
            'Amnesty International: United States Minor Outlying Islands', 'Amnesty International: Uruguay', 'Amnesty International: Uzbekistan',
            'Amnesty International: Venezuela', 'death penalty: ','Amnesty International: Vietnam', 'Amnesty International: Yemen', 'Amnesty International: Zambia',
            'Amnesty International: Zimbabwe', 'A Chronicle of Current Events', 'Torture in', 'Amnesty International: newsletter', 'EU:'
            'Amnesty International: USA', 'UA ', 'EXTRA ','list of ','Amnesty International: US', 'Amnesty International: EU', 'Amnesty: Europe', 'Amnesty: EU','Europe',
            'Amnesty International: Europe', 'support', 'thanks', 'thank you','demand', 'Human Rights Violations in',
            'Further information on', 'Suran', "COUNCIL OF EUROPE: ", "COUNCIL OF EUROPE",
            'Peoples’ Republic of China', 'TURKRAN', 'Türkiye', 'recruitment', 'Pilipinas','Latin America', 'South Korea',
'Slovak', 'United Nations', 'Central America', 'United Arab Emirates', 'Kazakstan', 'UN ', 'Trinidad & Tobago',
'Amnesty International Council', 'Caribbean', 'OAS ', 'the UN ', 'the United Nations ', 'east Asia',
'Palestine Authority', 'Cote d’Ivoire', 'Africa', 'Asia pacific',  'North Korea', 'media advisory',
'meeting of', 'UN:', 'Lesvos', 'Edward Snowden', 'Southeast Asia', 'South East Asia']

# ---
# List of words associated to non-HRE content (news articles, press releases, research reports).
BAD_WORDS = ['report', 'free!', 'freed!', 'urgent action', 'petition', 'statement', 'opinion',
             'research', 'freed ', 'position', 'killed', 'further information on UA',
             'success', 'denied', 'detained', 'release', 'open letter', 'convicted', 'boletin','Amnesty International Briefing',
             'AI Briefing','Amnesty International Review', 'journal', 'Background Paper', 'letter to',
             'letters to', 'newsletter',
             'testimony', 'general information', 'Further information', 'concerns',
             'anniversary', 'Rapport', 'submission to','Global Refugee Crisis', 'urges', 'Call for ',
             'attack', 'privacy notice', 'tortured', 'should', 'letter to ', 'letter from ',
             'prize', 'award', 'donat','release', 'annual', 'freedom for', 'progress',
             'punished', 'in prison', 'criticizes', 'condemns', 'victor', 'executed','without charge',
             'death toll', 'achiev', 'wins', 'Weekly Update',
             'under house arrest', "under threat",' comments on', 'secretary', 'chief', 'sentenced', 'desaparecid'
             ' comment on', 'recommendations on', 'in jail', 'jailed','Amnesty to', 'donor'
             'Amnesty International to', 'AI to', 'condemn', 'killing of ','prosecut', 'prison', ' call for ',
             'AI on', 'amnesty on','arrested', 'disappearance', 'ICC', 'Tribunal Penal Internacional',
             'International Criminal Court',
             'abducted', 'stopped', 'in detention', 'imprisoned', 'urgent', 'appeal',
             'must', 'director', 'FIFA', 'Amnesty on ', 'abused', 'jail sentence', 'Country dossier list',
             'Amnesty International on','AI calls','Amnesty International calls ', 'summit',
             'amnesty call', 'Universal Jurisdiction', 'disappeared', 'the wire', 'email protected',
             'fail ',' UN ','open letter','punished','failing','remember', 'fax jam',
             'release', 'saved',' demand', 'press conference', "the state of the world","World Day",
             "injured", "#PeterBenenson2022","Alfombra Amarilla",'urges',
             "Boletín de Actividades de Amnistía Internacional", "victor",
             "Commemor", "Emergencia","Alza la voz","Acción",
             "Gracias","represión en","PROTÉGELAS","trump",
             "En España, los crueles recortes dejan","¡Hazte activista! Buscamos",
             "#UnaPuertaUnaHistoria","Jugá Limpio","Día mundial",
             "#MisDerechosHumanos ¿Qué son para vos los derechos humanos?","Esta es mi casa, son mis raíces",
             "#TeamBrave","#MostráTuPoder","TwitterScoreCard","#SeJuegaEnCasa","Liberen","justicia por",
             "FIRMA","Hip Hop","Audiogramas","conferencia de prensa","día de","Doná","Caso de ",
             "Basta de","Haz que se vean","Elecciones","Jorgito","cumpleaños","editorial",
             "Calles con Memoria","Debe","vota ","en vivo", "Testimonio","#AmnistíaDice",
             "Actúa por","Concierto","Informe","#Búscalas","Día Internacional de",
             "No seas","Salvapantallas","Tú puedes","Mensaje de ","Libertad para",
             "pide justicia","justicia para","liberen a","En directo","te invita a",
             'criticizes',"El estado de los derechos","Interview","Festival de Música Urbana",
             "won","win","Informe Semanal","CHRISTMAS","accused",
             "under threat","harassed","missing",
             "jailed","shot","signature","sign ", "attacked", "HUMAN TOO: Meet",
             "vote","We stand ","Award", "prize", "findings",
             "statistics","messages of","stop the",
             "[2012 Letter Writing Marathon]","Meeting with",
             "Conversation with","Stand up","Flashmob",
             "guilty","Send AMNESTY","Now!",
             "call for","calls for ","please","Join us",
             "Write a letter for","human rights situation",
             "Anniversary","face","sentence","The voice of","birthday",
             "actions","take action","write for the rights of",
             "I write for rights","with you","I am writing for rights",
             "press conference","Attacks","Success","writes for freedom",
"Candidate for", "activists! Part 3","14for2014","save", "Harlem Shake",
                      "Letter Writing Marathon 20","good news","Action in", "Ten true stories","Slamnesty",
            ]

# ---
# Same as before but for YouTube videos instead of website outputs.
BAD_WORDS_YTB = ["the state of the world",'must', "should", "launch",'under house arrest','Amnesty International calls ',
               'submission to',"Informe", "latest","killing","World Day","injured", 'freedom for',
               'denied', 'government should', 'detained',
               'free!', 'freed!',"congrat","imprisoned","Call from","harassed", "INFORMATIVO","Premio","logros",
               "#PeterBenenson2022","Alfombra Amarilla","Boletín de Actividades de Amnistía Internacional", "victor",
               "Commemor",'urgent action', "Act now", "letter to",'abducted', 'stopped', 'in detention',
               'urgent',"Emergencia","Alza la voz","Acción",'urges', 'release', 'saved',' demand', 'Call for ',
               'in prison',"de prensa","#CadenasInvisibles", "Gracias","represión en","PROTÉGELAS","trump",
               "En España, los crueles recortes dejan","¡Hazte activista! Buscamos",
               "#UnaPuertaUnaHistoria","Jugá Limpio","Día mundial",
               "#MisDerechosHumanos ¿Qué son para vos los derechos humanos?","Esta es mi casa, son mis raíces",
               "#TeamBrave","#MostráTuPoder","TwitterScoreCard","#SeJuegaEnCasa","Liberen","justicia por",
               "FIRMA","Hip Hop","Audiogramas","conferencia de prensa","día de","Doná","Caso de ",
               "Basta de","Haz que se vean","Elecciones","Jorgito","cumpleaños","editorial",
               "Calles con Memoria","Debe","vota ","en vivo", "Testimonio","#AmnistíaDice",
               "Actúa por","Concierto","Informe","#Búscalas","Día Internacional de",
               "No seas","Salvapantallas","Tú puedes","Mensaje de ","Libertad para",
               "pide justicia","justicia para","liberen a","En directo","te invita a",
               'criticizes',"El estado de los derechos","Interview","Festival de Música Urbana",
               "won","win","Informe Semanal", 'condemns', "under threat","harassed",
               "jailed","shot","signature","sign ", "attacked", "HUMAN TOO: Meet",
               "vote","We stand ","Award", "prize",
               "statistics","messages of","stop the",
               "[2012 Letter Writing Marathon]","Meeting with",
               "Conversation with","Stand up","report on","Flashmob",
               "guilty","Send AMNESTY","Now!","Report Release",
               "call for","calls for ","please","Join us",
               "Write a letter for","New Report","human rights situation",
               "Anniversary","face","sentence","The voice of","birthday",
               "actions","Annual report","take action","write for the rights of",
               "I write for rights","with you","I am writing for rights",
               "press conference","Attacks","Success","writes for freedom",
               "Candidate for", "activists! Part 3","14for2014","save", "Harlem Shake",
               "Letter Writing Marathon 20","good news","Action in", "Ten true stories","Slamnesty"]


# Words used to identify content that is produced by hre staff.
HRE_PRODUCED_WEB= [" edx", "hre ", "Online Course", "human rights education", "edh ",
    "Enrol ", "free online course", "Amnesty Academy", "https://academy.amnesty.org",
    "(https://www.facebook.com/pg/HumanRightsEducation", "l’éducation aux droits humains",
    "educacionenderechos", "humanrightseducation", "Human Rights Friendly School",
    "educación en derechos humanos", "Formación en Derechos Humanos", "educación en DDHH",
    "educacion en DDHH", "academia", "colegio amigo de los derechos humanos",
    "red de escuelas", "educador sobre DDHH", "educador sobre derechos humanos",
    "docente en derechos humanos", "docente en DDHH", "Módulo",
    "docentes en derechos humanos", "educadores sobre derechos humanos",
    "e-learning", "Introducción a", "Introduccion a", "Capítulo", "Capitulo",
    "curso en línea", "curso online", "guía para profesores", "curso sobre",
    "cursos sobre", "recursos de aprendizaje", "para educador", "para docente",
    "para enseñar", "human rights educators", "course about", "courses about",
    "Diversxs", "classroom exercises", "learning resources", "for educator", "for teacher",
    "for teaching", "College of Human Rights", "education video", "free course",
    "educational video", "Human Rights Academy", "Human rights camp ", "CURRICULUM",
    "start the change", "tu escuela", "tu colegio", "de formación", "formación en",
    "metodología educativa", "metodologia educativa", "metodologías educativas",
    "metodologias educativas", "educación en dh", "educador de derechos humanos",
    "educadores de derechos humanos", "educativo", "instructivo", "capacitación",
    "docencia", "docente", "maestro", "e learning", "elearning", "enseñar derechos humanos",
    "para el aula", "educational", "instructional", "academy", "training",
    "teaching", "instructive", "your school", "online course",
    "teaching human rights", "teach human rights", "classroom", "educator"
]

                      #Words to be used to identify content that might be hre IN WEB ARTICLES.
                      # Apply in the title, rawtext, excerpt, and tags of WEB ARTICLES
MODERATE_HRE_INDICATORS_WEB = [
    "documentary", "Documental", "Training of Trainers",
    "film ", "movie", "pelicula", "película", "seminario", "Curso",
    "intro to ", "podcast", "introduction to ",
    "how to ", "your school", "Teacher’s Guide",
    "training program", "teacher",
    "what is", "What do you know about", "Paso a paso",
    "Conversatorio", "charla", "webinario",
    "Qué son ", "Qué es ", "tu escuela",
    "tu colegio", "module", "explainer",
    "webinar",
    "Introducing", "Episode",
    "for schools", "guide", "Education for ",
    "Educational", "Explanation",
    "Universal Declaration of Human Rights",
    "teacher", "Lesson", "Your Fabulous Human Rights Part", "training",
    "classroom", "how to", "cartoon", "seminar",
    "online lecture", "Amnestypedia", "game",
    "educador", "facilitador", "participativa",
    "participativas", "pedagógic", "pedagogia", "pedagogía",
    "taller", "guia", "guía", "compendio", "podcast",
    "seminario", "ejercicio", "plan de estudios ", "módulo", "modulo",
    "interactivo", "herramientas", "toolkit", "tool-kit", "tool kit",
    "recurso", "material para", "material sobre", "actividades",
    "clase sobre", "clases sobre", "clases en", "sesiones sobre",
    "sesión de", "sesión sobre", "sesiones de", "dinamica", "dinámica",
    "manual", "workshop", " guide ", "workbook", "booklet",
    "guidebook", "handbook", "compendium", "podcast", "lesson",
    "seminar", "drill", "curriculum", "curricula", "module",
    "interactive", "toolkit", "tool kit",
    "tool-kit", "resource", "nanolearning",
    "ucitelum", "studentu", "jeunes", "pedagogiques", "skolor", "gimnazium",
    "skola", "scuol", "edukacja", "corso", "material"
                 # German
                 "Bildung", "Schule", "Schüler", "Kurs", "interaktiv", "Unterricht", "Schüler", "Lehrer", "Modul", "Lernen", "Workshop",
                 # French
                 "éducation", "école", "étudiant", "cours", "interactif", "leçon", "étudiant", "professeur", "module", "apprentissage", "atelier",
                 # Icelandic
                 "menntun", "skóli", "nemandi", "námskeið", "gagnvirkt", "kennsla", "nemandi", "kennari", "hluti", "verkefni",
                 # Turkish
                 "eğitim", "okul", "öğrenci", "kurs", "etkileşimli", "ders", "öğrenci", "öğretmen", "modül", "öğrenme", "çalıştay",
                 # Polish
                 "edukacja", "szkoła", "uczeń", "kurs", "interaktywny", "lekcja", "uczeń", "nauczyciel", "moduł", "nauka", "warsztat",
                 # Portuguese
                 "educação", "escola", "aluno", "curso", "interativo", "aula", "aluno", "professor", "módulo", "aprendizagem", "oficina"]


# List of words whose existence in a YouTube video strongly suggests the
# the video is on HRE.
HRE_PRODUCED_YTB= [" edx", "hre ", "Online Course","human rights education", "edh ", "Enrol ", "free online course",
    "Amnesty Academy", "https://academy.amnesty.org",
    "(https://www.facebook.com/pg/HumanRightsEducation",
    "l’éducation aux droits humains","educacionenderechos", "humanrightseducation",
    "Human Rights Friendly School", "educación en derechos humanos", 
    "Formación en Derechos Humanos","educación en DDHH", "educacion en DDHH", 
    "academia", "colegio amigo de los derechos humanos", "red de escuelas",
    "educador sobre DDHH", "educador sobre derechos humanos",
    "docente en derechos humanos", "docente en DDHH", "Módulo",
    "docentes en derechos humanos", "educadores sobre derechos humanos",
    "e-learning", "Introducción a","Introduccion a", "Capítulo",
    "curso en línea", "curso online", "guía para profesores", "curso sobre", 
    "cursos sobre", "recursos de aprendizaje", "para educador", "para docente", 
    "para enseñar", "human rights educators", "online course" , "course about", 
    "courses about", "Diversxs", "classroom exercises", "learning resources",
    "for educator", "for teacher", "for teaching", "College of Human Rights",
    "education video", "free course", "educational video","Human Rights Academy",
    "Human rights camp ", "CURRICULUM","Human Rights Friendly School"
]

# List of words whose existence in a YouTube video moderately suggests the
# the video is on HRE.
MODERATE_HRE_INDICATORS_YTB= ["documentary","Documental", "this is how ","Training of Trainers",
                     "illustrat","understanding","animation","animat"," explained",
                     "film ", "movie","pelicula","película","seminario", "Curso",
                     "intro to ","#EnUnFlash", "podcast","introduction to ",
                     "how to ","your school", "Teacher’s Guide",
                     "training program","Universal Declaration of Human Rights",
                     "what is","What do you know about","Paso a paso",
                     "¿Qué está ","#SaludEsDDHH","Hablemos de derechos",
                     "Conversatorio","Programa","charla","webinario","Radial",
                     "Qué son ","Episodio","Qué es ","tu escuela",
                     "tu colegio","module", "explainer",
                     "webinar","workshop", "start the change",
                     "Introducing", "what is happening in", "Episode",
                     "for schools","guide","video series","Education for "
                     ,"talk about","Educational","Explanation","Legal Resources",
                     "Universal Declaration of Human Rights","trailer",
                     "teacher","Lesson","Your Fabulous Human Rights Part", "training",
                     "classroom","explains","how to","cartoon", "seminar","online lecture","Amnestypedia", "game"]

HRE_INDICATORS = HRE_PRODUCED_YTB + MODERATE_HRE_INDICATORS_YTB
HRE_INDICATORS = HRE_PRODUCED_WEB + MODERATE_HRE_INDICATORS_WEB

# Dictionary with language codes.
language_codes_dict = {
        "SPANISH": "es",
        "FRENCH": "fr",
        "ARABIC": "ar",
        "CHINESE": "zh",
        "GERMAN": "de",
        "PORTUGUESE": "pt",
        "DUTCH": "nl",
        "CZECH": "cs",
        "FARSI": "fa",
        "DANISH": "da",
        "FILIPINO": "fil",
        "FINNISH": "fi",
        "RUSSIAN": "ru",
        "SERBIAN": "sr",
        "ALBANIAN": "sq",
        "GREEK": "el",
        "HEBREW": "he",
        "HINDI": "hi",
        "HUNGARIAN": "hu",
        "IDO": "io",
        "SLOVENIAN": "sl",
        "INDONESIAN": "id",
        "ITALIAN": "it",
        "JAPANESE": "ja",
        "KOREAN": "ko",
        "TURKISH": "tr",
        "SWEDISH": "sv",
        "SLOVAK": "sk",
        "SOMALI": "so",
        "AMHARIC": "am",
        "ARMENIAN": "hy",
        "AYMARA": "aym",
        "AZERBAIJANI": "az",
        "BELARUSIAN": "be",
        "BENGALI": "bn",
        "BOSNIAN": "bs",
        "BULGARIAN": "bg",
        "BURMESE": "my",
        "CATALAN": "ca",
        "CEBUANO": "ceb",
        "CROATIAN": "hr",
        "DARI": "prs",
        "DIOULA": "dyu",
        "ESPERANTO": "eo",
        "ESTONIAN": "et",
        "FAROESE": "fo",
        "FULAH": "ful",
        "GEORGIAN": "ka",
        "GUARANI": "grn",
        "GUJARATI": "gu",
"HAITIAN CREOLE": "ht",
    "HAUSA": "ha",
    "KAZAKH": "kk",
    "KHMER": "km",
    "KINYARWANDA": "rw",
    "KIRGHIZ": "ky",
    "KURDISH": "ku",
    "KURMANJI":  "kmr",
    "LAO": "lo",
    "LATVIAN": "lv",
    "LITHUANIAN": "lt",
    "MACEDONIAN": "mk",
    "MALAGASY": "mg",
    "MALAY": "ms",
    "MALAYALAM": "ml",
    "MALDIVIAN": "dv",
    "MAPUDUNGUN": "arn",
    "MAYA": "yua",
    "MOLDAVIAN": "ro",
    "MONGOL":"mon",
    "MOORÉ": "mos",
    "NEPALI": "ne",
    "ORIYA": "or",
    "OROMO": "om",
    "PASHTO": "ps",
    "POLISH": "pl",
    "PUNJABI": "pa",
    "ROMANIAN": "ro",
    "RUNDI": "rn",
    "SINHALESE": "si",
    "SOUTHERN SOTHO": "st",
    "SWAHILI": "sw",
    "SWATI": "ss",
    "TAGALOG": "tl",
    "TAJIK": "tg",
    "TAMIL": "ta",
    "TELUGU": "te",
    "THAI": "th",
    "TIBETAN": "bo",
    "TIGRINYA": "ti",
    "TURKMEN": "tk",
    "UKRAINIAN": "uk",
    "URDU": "ur",
    "UYGHUR": "ug",
    "UZBEK": "uz",
    "VENDA": "ve",
    "VIETNAMESE": "vi",
    "XHOSA": "xh",
    "ZULU": "zu"
}

# Dictionary with list of words (values) associated to different topics (keys).
TOPICS_DICT = {
        "Armed Conflict": ["armed", "bomb", "war", "conflict", "battle", "military", "guerrilla", "insurgent", "bomba", "guerra", "conflicto", "batalla", "militar"],
        "Arms Trade": ["arms trade", "arm trade", "weapon", "gun", "firearm", "missile", "explosive", "munition", "comercio de armas", "arma de fuego", "misil", "explosivo", "municion"],
        "Asylum": ["asylum", "forced migration", "refugee", "displaced", "deport", "immigration", "asilo", "migración", "refugiado", "desplazad", "deporta", "inmigración"],
        "Business and Human Rights": ["corporate", "vaccine", "labor rights", "working conditions", "fair trade", "corporativo", "vacuna", "derechos laborales", "condiciones de trabajo"],
        "Blog": ["blog"],
        "Censorship and Freedom of Expression": ["censor", "rule of law", "freedom of expression", "free speech", "press freedom","Freedom of belief", "protest", "censura", "freedom of speech", "libertad de expresión", "libertad de prensa", "protesta"],
        "Children": ["children","family","kids","primary education", "Primary school", "PUNCH AND JUDY","child","jolie", "parent", "Passport", "First Steps", "cuento","toddler", "infant","infancia","niña", "familia", "educación primaria", "escuela primaria", "padre", "Pasaporte","Primeros Pasos", "niño", "infante"],
        "Climate Change": ["Climate", "global warming", "environment", "sustainability", "carbon", "emissions", "pollution", "renewable energy", "Climatico", "calentamiento global", "medio ambiente", "sustenibilidad", "carbono", "emisiones", "contaminación", "energía renovable"],
        "Corporate Accountability": ["corporate", "corporate responsibility", "business ethics", "corporativ", "empresa"],
        "COVID-19": ["vaccine", "covid", "coronavirus", "pandemic", "quarantine", "social distancing", "vacuna", "covid", "coronavirus", "pandemia", "cuarentena", "distanciamiento"],
        "Death in Custody": ["prison death", "jail death", "incarceration", "custodial death", "muerte en prisión", "muerte en la cárcel", "encarcelamiento", "muerte bajo custodia"],
        "Death Penalty": ["Death Penalty", "Death row", "execution", "capital punishment", "hanging", "hanged", "pena de muerte", "ejecuci", "castigo capital", "horca"],
        "Detention": ["Detained", "detention", "Detainee", "imprisonment", "incarceration", "jail", "prison", "custody", "detención", "detenid", "encarcelamiento", "prisión", "custodi"],
        "Courts": ["court","judiciary", "FAIR TRIAL", "judge", "tribunal", "corte", "poder judicial", "juez", "tribunal"],
        "Disability Rights": ["disabled", "lenguaje de señas", "special needs","discapacitad", "necesidades especiales"],
        "Disappearances": ["Disappearance", "missing", "abducted", "kidnapped", "desaparición", "desaparecid", "secuestr"],
        "Discrimination": ["Discrimination","odio","bullying", "apartheid", "equality", "prejudice", "bias", "inequality", "stereotyp", "racism", "sexism", "homophobia", "discriminación","odio", "hate","apartheid", "igualdad", "prejuicio", "sesgo", "desigualdad", "estereotip", "racismo", "sexismo", "homofobia"],
        "Domestic Violence": ["Domestic Violence", "abuse", "spousal abuse", "battered","Collective rights", "home violence", "violencia doméstica", "abuso", "maltrato", "machist"],
        "Economic, Social and Cultural Rights": ["economic rights","ECHR ", "ECONOMIC", "poverty", "income inequality", "economic justice", "social justice", "derechos económicos", "ECONOMi", "pobreza", "pobre", "justicia económica"],
        "EU": ["the EU", "european union", "europe", "european commission", "european parliament", "brexit", "la UE", "unión europea", "europa", "comisión europea", "parlamento europeo", "brexit"],
        "Freedom of Association": ["protest", "repression", "freedom of assembly","right to assembly", "police","tear gas","Freedom of Association", "trade union", "unions", "right to organize",  "protesta", "represión", "gas lacrimógeno","Libertad de Asociación", "sindicatos", "derecho a organizarse", "marcha"],
        "Freedom of Movement": ["Freedom of Movement", "travel", "migration", "checkpoint", "Libertad de Movimiento", "libertad de transito" "viaj"],
        "Human Rights Defenders and Activists": ["defens","defend","brave"," bold", "COURAGE", "Activism","activist","Save a Life","Mardini", "Write for Rights", "w4r","write for","write 4", "Marathon", "defensor","valiente", "CORAJE", "Activismo", "activista", "Escribe por los Derechos", "w4r", "Maratón", "escribe por los derechos"],
        "Indigenous People": ["indigenous", "native", "aboriginal", "native american", "first nations", "tribal", "tribe", "indígena", "originari", "aborigen", "nativo", "tribu"],
        "Internally Displaced People": ["Internally Displaced People", "displacement", "forced migration", "Personas Desplazadas Internamente", "desplazamiento", "migración forzada"],
        "Killings and Disappearances": ["Disappearance", "killing", "extrajudicial", "murder", "homicide", "assassination", "genocide", "desaparición", "asesinato", "extrajudicial", "homicidio", "asesinato", "genocidio"],
        "LGBTI Rights": ["LGBT", "queer", "gay", "LGBI","LGTBI","lesbian", "trans ","Equal Marriage", "intersex", "homosexual", "transgender","MiNombreDebeSerLegal","Soy Real", "bisexual","trans rights", "gender identity", "LGBT ", "gay", "lesbiana", "intersex", "homosexual", "transgénero", "bisexual","personas trans","ser trans ","transexual", "diversxs","los trans","identidad de género"],
        "Maternal Health and Reproductive Rights": ["maternal", "abortion", "reproductive", "pregnancy", "maternity", "childbirth", "family planning", "contraception", "maternal", "aborto", "reproductiv", "embarazo", "maternidad", "parto","anticonceptiv"],
        "Migrants": ["refugee", "People on the move", "asylum", "migration", "migrant", "border", "expatriate", "refugiado", "asilo", "migración", "frontera", "expatriado"],
        "Poverty": ["poverty", "dignity", "the poor", "homelessness", "food insecurity", "inequality", "underprivileged", "lack of resources", "pobreza", "los pobres", "sin hogar", "inseguridad alimentaria", "desigualdad", "desfavorecido", "escasez de recursos","falta de recursos", "dignidad"],
        "Prisoners of Conscience": ["Prisoners of Conscience", "Prisoner of Conscience", "political prisoner", "Prisioneros de Conciencia", "Prisionero de Conciencia", "presos políticos","preso político"],
        "Protests and Demonstrations": ["Protest", "tear gas", "repression", "riot", "march", "demo", "Protesta", "gas lacrimógeno", "represión",  "marcha"],
        "Racial Discrimination": ["racism", "racist", "racial", "ethnic", "segregation", "racial justice", "racial equality", "racial bias", "racismo", "racista", "racial", "segregación", "justicia racial", "igualdad racial", "sesgo racial"],
        "People Trafficking": ["Trafficking", "slavery", "Human smuggling", "Forced prostitution"],
        "Refugees": ["refug", "asylum", "forced migration", "Mardini","displaced", "stateless", "asylum seeker", "migración forzada", "desplazad", "refugiad", "asilo"],
        "Right to Food": ["hunger", "food security", "malnutrition", "starvation","Right to Food", "hambre", "seguridad alimentaria", "desnutrición", "inanicción","Derecho a la Alimentación"],
        "Right to Health": ["vaccine", "covid", "enferm","coronavirus", "pandemic", "health", "healthcare", "medical care", "public health", "health rights", "vacuna", "pandemia", "salud", "atención médica", "cuidado médico"],
        "Right to Water": ["Water","sanitation", "Agua","saneamiento"],
        "Sexual Rights": ["Sexual","itsmybody","ESImportante","esmicuerp", "mi cuerp","cuerpo","cuerpa" ,"sex education","MY BODY", "consent", "sexuality", "sex education","diversxs", "Sexual", "MI CUERPO", "consentimiento", "sexualidad", " esi ","educación sexual","diversxs", "derechos sexuales"],
        "Sexual Violence": ["Sexual Violence","violencia en el Noviazgo","Noviazgo sin violencia", "Violencia de género","consent", "rape", "sexual abuse", "sexual assault", "molestation", "sexual harassment", "me too","gender based violence", "gender violence", "Violencia Sexual", "consentimiento", "violación", "abuso sexual","machista", "ni una menos","acoso sexual", "femicid"],
        "Slums and the Right to Housing": ["slum", "housing", "homelessness", "affordable housing","villas", "eviction","desalojo","sin hogar", "vivienda", " precari"],
        "Technology and Human Rights": ["surveillance", "SNOWDEN","google","facebook","scan","cyber", "biometric","face recognition","facial recognition", "pegasus", "spy", "technolog", "internet freedom", "privacy", "data protection", "artificial intelligence", "algorithm", "vigilancia", "biométrico","reconocimiento facial", "espía", "tecnología", "acceso a internet",
                                        "privacidad", "usuario","protección de los usuarios", "inteligencia artificial", "algoritmo"],
        "Torture and other ill-treatment": ["torture", "tortura", "police"],
        "UN": ["united nations", "the un", "united nations general assembly","Universal Declaration", "Declaration of Human Rights","un security council", "un human rights council", "UDHR", "universal declaration of human rights", "Declaración Universal","world health organization", "naciones unidas", "la onu ", "asamblea general de las naciones unidas", "consejo de seguridad de la onu", "consejo de derechos humanos de la onu", "organización mundial de la salud", "las naciones unidas"],
        "Unlawful Detention": ["Detained", "detention", "Detainee", "arrest", "imprisonment", "incarceration", "custody", "detenid", "detención", "apresado", "en prisión", "arresto", "encarcelamiento"],
        "Unlawful Killings": ["killing", "murder", "assassination", "homicide", "asesinato", "homicidio"],
        "Women's Rights": ["women","ellas", "woman", "girl", "abortion", "glass","gender equality", "me too", "mujeres", "mujer", "niña", "aborto","madre", "maternal", "feminist", "igualdad de género"],
        "Youth and Human Rights": ["youth", "Secondary Education", "Secondary school","young","words that burn", "student", "poem", "poetry", "poetic", "young people", "adolescents", "teenagers", "students", "youth activism", "gen z", "generación z","Educación Secundaria", "Escuela Secundaria","joven", "jóvenes", "adolescentes", "estudiantes", "juvenil"],

"Education":["school", "Secondary Education", "primary education", "educación primaria",
    "jolie", "education", "educación","teacher", "human rights education", "manual",
    "escuela primaria", "taller","Pasaporte", "juego", "Primeros Pasos", "Primary school",
    "Secondary school", "student", "Educación Secundaria", "Escuela Secundaria",
    "escuela", "game","quiz", "your school", "Teacher’s Guide", "tu escuela", "tu colegio",
    "for schools", "guide", "Education for", "Lesson",
    "Your Fabulous Human Rights Part", "training", "classroom", "know your rights",
    "clase sobre", "clases sobre", "clases en", "sesiones sobre", "nanolearning",
    "ucitelum", "studentu", "jeunes","pedagogiques","skolor","gimnazium",
    "skola", "scuol", "edukacja","corso", "material",
    "Bildung", "Schule", "Schüler", "Kurs", "interaktiv", "Unterricht", "Schüler",
    "Lehrer", "Modul", "Lernen", "Workshop",
    "éducation", "école", "étudiant", "interactif", "leçon", "étudiant", "professeur",
    "module", "apprentissage", "atelier",
    "menntun", "skóli", "nemandi", "námskeið", "gagnvirkt", "kennsla", "nemandi",
    "kennari", "hluti", "nám", "verkefni",
    "eğitim", "okul", "öğrenci", "kurs", "etkileşimli", "öğrenci", "öğretmen",
    "modül", "öğrenme", "çalıştay",
    "edukacja", "szkoła", "uczeń", "kurs", "interaktywny", "lekcja", "uczeń",
    "nauczyciel", "moduł", "nauka", "warsztat",
    "educação", "escola", "aluno", "curso", "interativo", "aula", "aluno",
    "professor", "módulo", "aprendizagem",
    "edx", "hre ", "Online Course", "human rights education", "edh ",
    "Enrol ","free online course", "Academy",
    "l’éducation aux droits humains",
    "educacionenderechos", "humanrightseducation", "Human Rights Friendly School",
    "educación en derechos humanos", "Formación en Derechos Humanos",
    "educación en DDHH", "educacion en DDHH", "academia",
    "colegio amigo de los derechos humanos", "red de escuelas",
    "educador sobre DDHH", "educador sobre derechos humanos",
    "docente en derechos humanos", "docente en DDHH", "Módulo",
    "docentes en derechos humanos", "educadores sobre derechos humanos",
    "e-learning", "curso en línea", "curso online",
    "guía para profesores", "curso sobre", "cursos sobre",
    "recursos de aprendizaje", "para educador", "para docente", "para enseñar",
    "human rights educators", "play",
    "course about", "courses about","classroom exercises",
    "learning resources","for educator" "for teacher",
    "for teaching", "College of Human Rights","education video", "free course",
    "educational video","course","Human Rights Academy","Human rights camp ",
    "CURRICULUM","Human Rights Friendly School", "start the change",
    "educación en derechos humanos", "educación en DDHH",  "educación en DDHH",
    "educacion en DDHH", "educador de derechos humanos",
    "educadores de derechos humanos", "educador sobre derechos humanos",
    "educadores sobre derechos humanos", "educativo", "instructivo", "capacitación",
    "docencia", "docente", "maestro", "tu escuela", "e-learning", "enseñar derechos humanos", "Amnestypedia",
    "para el aula", "tanoda","educational", "instructional", "academy", "training",
    "teaching","BITE SIZE" "your school", "online course",
    "teaching human rights","BITE SIZE","debate","discussion","Black","Pedagogic","seminar","studies","trainer","training","handbook","teach human rights", "classroom",
    "educator"],
# Countries:

   "Afghanistan": ["Afghanistan", "Afghan", "Kabul"],
    "Africa": ["Africa"],
    "Albania": ["Albania", "Albanian", "Tirana"],
    "Algeria": ["Algeria", "Algerian", "Algiers"],
    "Andorra": ["Andorra", "Andorran", "Andorra la Vella"],
    "Angola": ["Angola", "Angolan", "Luanda"],
    "Argentina": ["Argentina", "Argentinian", "Buenos Aires"],
    "Armenia": ["Armenia", "Armenian", "Yerevan"],
    "Australia": ["Australia", "Australian", "Canberra"],
    "Austria": ["Austria", "Austrian", "Vienna"],
    "Azerbaijan": ["Azerbaijan", "Azerbaijani", "Baku"],
    "Bahrain": ["Bahrain", "Bahraini", "Manama"],
    "Bangladesh": ["Bangladesh", "Bangladeshi", "Dhaka"],
    "Belarus": ["Belarus", "Belarusian", "Minsk"],
    "Belgium": ["Belgium", "Belgian", "Brussels"],
    "Benin": ["Benin", "Beninese", "Porto-Novo"],
    "Bolivia": ["Bolivia", "Bolivian", "La Paz", "Sucre"],
    "Botswana": ["Botswana", "Motswana", "Gaborone"],
    "Brazil": ["Brazil", "Brazilian", "Brasilia"],
    "Bulgaria": ["Bulgaria", "Bulgarian", "Sofia"],
    "Burkina Faso": ["Burkina Faso", "Burkinabe", "Ouagadougou"],
    "Burundi": ["Burundi", "Burundian", "Gitega"],
    "Cambodia": ["Cambodia", "Cambodian", "Phnom Penh"],
    "Cameroon": ["Cameroon", "Cameroonian", "Yaounde"],
    "Canada": ["Canada", "Canadian", "Ottawa"],
    "Chad": ["Chad", "Chadian", "N'Djamena"],
    "Chile": ["Chile", "Chilean", "Santiago"],
    "China": ["China", "Chinese", "Beijing"],
    "Colombia": ["Colombia", "Colombian", "Bogota"],
    "Congo": ["Congo", "Congolese", "Kinshasa"],
    "Côte d'Ivoire": ["Côte d'Ivoire", "Ivorian", "Yamoussoukro", "Abidjan"],
    "Croatia": ["Croatia", "Croatian", "Zagreb"],
    "Cuba": ["Cuba", "Cuban", "Havana"],
    "Cyprus": ["Cyprus", "Cypriot", "Nicosia"],
    "Czech Republic": ["Czech Republic", "Czechia","Czech", "Prague"],
    "Democratic Republic of the Congo": ["Democratic Republic of the Congo, Congo", "Kinshasa"],
    "Denmark": ["Denmark", "Danish", "Copenhagen"],
    "Dominican Republic": ["Dominican Republic", "Dominican", "Santo Domingo"],
    "Ecuador": ["Ecuador", "Ecuadorian", "Quito"],
    "Egypt": ["Egypt", "Egyptian", "Cairo"],
    "El Salvador": ["El Salvador", "Salvadorian", "San Salvador"],
    "Equatorial Guinea": ["Equatorial Guinea", "Equatorial Guinean", "Malabo"],
    "Eritrea": ["Eritrea", "Eritrean", "Asmara"],
    "Estonia": ["Estonia", "Estonian", "Tallinn"],
    "Eswatini": ["Eswatini", "Swazi", "Mbabane", "Lobamba"],
    "Ethiopia": ["Ethiopia", "Ethiopian", "Addis Ababa"],
    "Fiji": ["Fiji", "Fijian", "Suva"],
    "Finland": ["Finland", "Finnish", "Helsinki"],
    "France": ["France", "French", "Paris"],
    "Gambia": ["Gambia", "Gambian", "Banjul"],
    "Georgia": ["Georgia", "Georgian", "Tbilisi"],
    "Germany": ["Germany", "German", "Berlin"],
    "Ghana": ["Ghana", "Ghanaian", "Accra"],
    "Greece": ["Greece", "Greek", "Athens"],
    "Guatemala": ["Guatemala", "Guatemalan", "Guatemala City"],
    "Guinea": ["Guinea", "Guinean", "Conakry"],
    "Haiti": ["Haiti", "Haitian", "Port-au-Prince"],
    "Honduras": ["Honduras", "Honduran", "Tegucigalpa"],
    "Hungary": ["Hungary", "Hungarian", "Budapest"],
    "Iceland": ["Iceland", "Icelandic", "Reykjavik"],
    "India": ["India", "Indian", "New Delhi"],
    "Indonesia": ["Indonesia", "Indonesian", "Jakarta"],
    "Iran": ["Iran", "Iranian", "Tehran"],
    "Iraq": ["Iraq", "Iraqi", "Baghdad"],
    "Ireland": ["Ireland", "Irish", "Dublin"],
    "Israel and Occupied Palestinian Territories": ["Israel and Occupied Palestinian Territories", "Palestine", "OPT", "Palestinian", "Israeli", "Ramallah","Sheikh Jarrah", "West Bank", "Gaza", "Israel", "Tel aviv", "Jerusalem", "settlements"],
    "Italy": ["Italy", "Italian", "Rome"],
    "Japan": ["Japan", "Japanese", "Tokyo"],
    "Jordan": ["Jordan", "Jordanian", "Amman"],
    "Kazakhstan": ["Kazakhstan", "Kazakh", "Nur-Sultan"],
    "Kenya": ["Kenya", "Kenyan", "Nairobi"],
    "Kosovo": ["Kosovo", "Kosovan", "Pristina"],
    "Kuwait": ["Kuwait", "Kuwaiti", "Kuwait City"],
    "Kyrgyzstan": ["Kyrgyzstan", "Kyrgyz", "Bishkek"],
    "Laos": ["Laos", "Laotian", "Vientiane"],
    "Latvia": ["Latvia", "Latvian", "Riga"],
    "Lebanon": ["Lebanon", "Lebanese", "Beirut"],
    "Lesotho": ["Lesotho", "Basotho", "Maseru"],
    "Libya": ["Libya", "Libyan", "Tripoli"],
    "Lithuania": ["Lithuania", "Lithuanian", "Vilnius"],
    "Madagascar": ["Madagascar", "Malagasy", "Antananarivo"],
    "Malawi": ["Malawi", "Malawian", "Lilongwe"],
    "Malaysia": ["Malaysia", "Malaysian", "Kuala Lumpur"],
    "Maldives": ["Maldives", "Maldivian", "Male"],
    "Mali": ["Mali", "Malian", "Bamako"],
    "Malta": ["Malta", "Maltese", "Valletta"],
    "Mexico": ["Mexico", "Mexican", "Mexico City"],
    "Middle East and North Africa": ["Middle East and North Africa", "MENA"],
    "Moldova": ["Moldova", "Moldovan", "Chisinau"],
    "Mongolia": ["Mongolia", "Mongolian", "Ulaanbaatar"],
    "Montenegro": ["Montenegro", "Montenegrin", "Podgorica"],
    "Morocco and Western Sahara": ["Morocco and Western Sahara", "Moroccan", "Sahrawi", "Rabat", "Laayoune"],
    "Mozambique": ["Mozambique", "Mozambican", "Maputo"],
    "Myanmar": ["Myanmar", "Burmese", "Naypyidaw"],
    "Namibia": ["Namibia", "Namibian", "Windhoek"],
    "Nepal": ["Nepal", "Nepali", "Kathmandu"],
    "Netherlands": ["Netherlands", "Dutch", "Amsterdam", "The Hague"],
    "New Zealand": ["New Zealand", "New Zealander", "Kiwi", "Wellington"],
    "Nicaragua": ["Nicaragua", "Nicaraguan", "Managua"],
    "Niger": ["Niger", "Nigerien", "Niamey"],
    "Nigeria": ["Nigeria", "Nigerian", "Abuja"],
    "North America": ["North America"],
    "North Korea": ["North Korea", "North Korean", "Pyongyang"],
    "North Macedonia": ["North Macedonia", "Macedonian", "Skopje"],
    "Norway": ["Norway", "Norwegian", "Oslo"],
    "Oman": ["Oman", "Omani", "Muscat"],
    "Pakistan": ["Pakistan", "Pakistani", "Islamabad"],
    "Palestine": ["Palestine", "Palestinian", "Ramallah", "Gaza"],
    "Papua New Guinea": ["Papua New Guinea", "Papuan", "Port Moresby"],
    "Paraguay": ["Paraguay", "Paraguayan", "Asunción"],
    "Peru": ["Peru", "Peruvian", "Lima"],
    "Philippines": ["Philippines", "Philippine", "Filipino", "Manila"],
    "Poland": ["Poland", "Polish", "Warsaw"],
    "Portugal": ["Portugal", "Portuguese", "Lisbon"],
    "Puerto Rico": ["Puerto Rico", "Puerto Rican", "San Juan"],
    "Qatar": ["Qatar", "Qatari", "Doha"],
    "Romania": ["Romania", "Romanian", "Bucharest"],
    "Russia": ["Russia", "Russian", "Putin", "Moscow"],
    "Rwanda": ["Rwanda", "Rwandan", "Kigali"],
    "Saudi Arabia": ["Saudi Arabia", "Saudi", "Saudia", "Riyadh"],
    "Senegal": ["Senegal", "Senegalese", "Dakar"],
    "Serbia": ["Serbia", "Serbian", "Belgrade"],
    "Sierra Leone": ["Sierra Leone", "Sierra Leonean", "Freetown"],
    "Singapore": ["Singapore", "Singaporean"],
    "Slovakia": ["Slovakia", "Slovak", "Bratislava"],
    "Slovenia": ["Slovenia", "Slovenian", "Ljubljana"],
    "Somalia": ["Somalia", "Somali", "Mogadishu"],
    "South Africa": ["South Africa", "South African", "Pretoria", "Cape Town", "Bloemfontein"],
    "South America": ["South America"],
    "South Asia": ["South Asia"],
    "South Korea": ["South Korea", "South Korean", "Seoul"],
    "South Sudan": ["South Sudan", "South Sudanese", "Juba"],
    "Spain": ["Spain", "Spanish", "Madrid"],
    "Sri Lanka": ["Sri Lanka", "Sri Lankan", "Colombo", "Sri Jayawardenepura Kotte"],
    "Sudan": ["Sudan", "Sudanese", "Khartoum"],
    "Sweden": ["Sweden", "Swedish", "Stockholm"],
    "Switzerland": ["Switzerland", "Swiss", "Bern"],
    "Syria": ["Syria", "Syrian", "Damascus"],
    "Taiwan": ["Taiwan", "Taiwanese", "Taipei"],
    "Tajikistan": ["Tajikistan", "Tajik", "Dushanbe"],
    "Tanzania": ["Tanzania", "Tanzanian", "Dodoma"],
    "Thailand": ["Thailand", "Thai", "Bangkok"],
    "Togo": ["Togo", "Togolese", "Lomé"],
    "Trinidad and Tobago": ["Tobago", "Trinidadian", "Tobagonian", "Port of Spain"],
    "Tunisia": ["Tunisia", "Tunisian", "Tunis", "Tunez"],
    "Türkiye": ["Türkiye", "Turkey", "Turkish", "Erdogan", "Ankara"],
    "Turkmenistan": ["Turkmenistan", "Turkmen", "Ashgabat"],
    "Uganda": ["Ugand", "Kampala"],
    "Ukraine": ["Ukraine", "Ukranian","Ukrainian", "Kyiv"],
    "United Arab Emirates": ["United Arab Emirates", "UAE", "Emirati", "Abu Dhabi"],
    "United Kingdom": ["United Kingdom", "the uk", "British",  " uk ", "london"],
    "United States of America": ["the US ", "North America", "united states", "biden", "Washington", "D.C.", "USA "]
}


# Possible formats of a date in a URL.
DATE_FORMATS = [
        '%d.%m.%Y',
        '%B %d, %Y',
        '%d de %B de %Y',
        '%d. %B %Y',  # DD. Month YYYY (new format)
        '%d %b %Y',    # DD MMM YYYY
        '%d %B %Y',    # DD Month YYYY
        '%d %b %y',    # DD MMM YY
        '%d %B %y',    # DD Month YY
        '%B %d, %Y',   # Month DD, YYYY
        '%b %d, %Y',   # MMM DD, YYYY
        '%b %d %Y',    # MMM DD YYYY
        '%b. %d. %Y',  # MMM. DD. YYYY
        '%B %d, %y',   # Month DD, YY
        '%b %d, %y',   # MMM DD, YY
        '%b. %d, %y',  # MMM. DD, YY
        '%Y-%m-%d',    # YYYY-MM-DD
        '%d-%m-%Y',    # DD-MM-YYYY
        '%d/%m/%Y',    # DD/MM/YYYY
        '%d.%m.%Y',    # DD.MM.YYYY
        '%Y%m%d',      # YYYYMMDD
        '%Y/%m/%d',    # YYYY/MM/DD
        '%m/%d/%Y',    # MM/DD/YYYY
        '%m/%d/%y',    # MM/DD/YY
        '%d-%m-%y',    # DD-MM-YY
        '%d.%m.%y',    # DD.MM.YY
        '%y%m%d',      # YYMMDD
        '%Y/%m',       # YYYY/MM
        '%m/%Y',       # MM/YYYY
        '%B %Y',       # Month YYYY
        '%Y',          # YYYY
        '%y'           # YY
        ]

# List of regular expressions matching distinct date formats.
DATE_REGEX = [
        r'publikován \d{1,2}\.\d{1,2}\.\d{4}',
        r'\w+ \d{1,2}, \d{4}',
        r'\d{1,2} de \w+ de \d{4}',
        r'\d{1,2}\. \w+ \d{4}',   # DD. Month YYYY (new regex)
        r'\d{1,2} \w{3} \d{4}',   # DD MMM YYYY
        r'\d{1,2} \w+ \d{4}',    # DD Month YYYY
        r'\d{1,2} \w{3} \d{2}',   # DD MMM YY
        r'\d{1,2} \w+ \d{2}',    # DD Month YY
        r'\w+ \d{1,2}, \d{4}',    # Month DD, YYYY
        r'\w{3} \d{1,2}, \d{4}',   # MMM DD, YYYY
        r'\w{3} \d{1,2} \d{4}',  # MMM DD YYYY
        r'\w{3}\. \d{1,2}\. \d{4}',   # MMM. DD. YYYY
        r'\w+ \d{1,2}, \d{2}',    # Month DD, YY
        r'\w{3} \d{1,2}, \d{2}',   # MMM DD, YY
        r'\w{3}\. \d{1,2}, \d{2}',   # MMM. DD, YY
        r'\d{4}-\d{2}-\d{2}',    # YYYY-MM-DD
        r'\d{2}-\d{2}-\d{4}',    # DD-MM-YYYY
        r'\d{2}/\d{2}/\d{4}',    # DD/MM/YYYY
        r'\d{2}\.\d{2}\.\d{4}',  # DD.MM.YYYY
        r'\d{8}',                # YYYYMMDD
        r'\d{4}/\d{2}/\d{2}',    # YYYY/MM/DD
        r'\d{2}/\d{2}/\d{4}',    # MM/DD/YYYY
        r'\d{2}/\d{2}/\d{2}',    # MM/DD/YY
        r'\d{2}-\d{2}-\d{2}',    # DD-MM-YY
        r'\d{2}\.\d{2}\.\d{2}',  # DD.MM.YY
        r'\d{6}',                # YYMMDD
        r'\d{4}/\d{2}',           # YYYY/MM
        r'\d{2}/\d{4}',           # MM/YYYY
        r'\w+ \d{4}',             # Month YYYY
        r'\d{4}',                # YYYY
        r'\d{2}'                 # YY
        '%Y-%m-%dT%H:%M:%SZ',
        'Published on %d.%m.%Y',  # Special format
        '%Y.%m.%d.',  # With trailing period
        '%d %B %Y, %I:%M %p',  # With time
        '%d %b %Y, %I:%M %p',  # With time
        '%d, %b. %Y, %I:%M %p',  # With time
        '%d. %B %Y, %I:%M %p',  # With time
        '%d.%m.%Y, %I:%M %p',  # With time
        '%d/%m/%Y, %I:%M %p',  # With time
        '%d-%m-%Y, %I:%M %p',  # With time
        '%B %d, %Y, %I:%M %p',  # With time
        '%b %d, %Y, %I:%M %p',  # With time
        '%d %B %y, %I:%M %p',  # With time
        '%d %b %y, %I:%M %p',  # With time
        '%d, %b. %y, %I:%M %p',  # With time
        '%d. %B %y, %I:%M %p',  # With time
        '%d.%m.%y, %I:%M %p',  # With time
        '%d/%m/%y, %I:%M %p',  # With time
        '%d-%m-%y, %I:%M %p',  # With time
        '%B %Y, %I:%M %p',  # With time
        '%b %Y, %I:%M %p',  # With time
        '%Y %B, %I:%M %p',  # With time
        '%Y %b, %I:%M %p',  # With time
        '%Y.%m.%d, %I:%M %p',  # With time
        '%Y-%m-%d, %I:%M %p',  # With time
        '%Y/%m/%d, %I:%M %p',  # With time
        '%Y%m%d, %I:%M %p',  # With time
        '%Y.%m, %I:%M %p',  # With time
        '%Y-%m, %I:%M %p',  # With time
        '%Y/%m, %I:%M %p',  # With time
        '%Y%m, %I:%M %p',  # With time
        '%Y, %I:%M %p',  # With time
        '%y, %I:%M %p',  # With time
        '%d %B de %Y',  # Another format for Spanish dates
        '%d de %B de %Y',  # Another format for Spanish dates
        '%d %B %Y',
        '%d %b %Y',
        '%d, %b. %Y',
        '%d. %B %Y',
        '%d.%m.%Y',
        '%d/%m/%Y',
        '%d-%m-%Y',
        '%B %d, %Y',
        '%b %d, %Y',
        '%d %B %y',
        '%d %b %y',
        '%d, %b. %y',
        '%d. %B %y',
        '%d.%m.%y',
        '%d/%m/%y',
        '%d-%m-%y',
        '%d %b %Y,',
        '%d. %B%Y',
        '%B %Y',
        '%b %Y',
        '%Y %B',
        '%Y %b',
        '%Y,%B',
        '%Y.%m.%d',
        '%Y-%m-%d',
        '%Y/%m/%d',
        '%Y%m%d',
        '%Y.%m',
        '%Y-%m',
        '%Y/%m',
        '%Y%m',
        '%Y',
        '%y'
]
