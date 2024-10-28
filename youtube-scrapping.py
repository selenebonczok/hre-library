import pandas as pd
from googleapiclient.discovery import build 
from youtube_transcript_api import YouTubeTranscriptApi 

# Insert your API key here to scrape YouTube content.
api_key = "[YOUR_API_KEY_HERE]"
youtube = build('youtube', 'v3',developerKey=api_key)

#Function to get channel stats.

# Function to fetch stats for a given list of channel IDs.
def get_channel_stats(youtube, channel_ids):
    """
    Get statistics and details for a list of channel IDs.

    Parameters:
        youtube (object): The YouTube service object.
        channel_ids (list): List of YouTube channel IDs.

    Returns:
        list: A list of dictionaries containing channel details.
    """
    all_data = []
    request = youtube.channels().list(
        part = 'snippet,contentDetails,statistics',
                id= ','.join(channel_ids))
    response = request.execute()
    for i in range(len(response['items'])):
        data = dict(Channel_name = response['items'][i]['snippet']['title'],
                Total_videos = response['items'][i]['statistics']['videoCount'],
                playlist_id = response['items'][i]['contentDetails']['relatedPlaylists']['uploads'])
        all_data.append(data)
    return all_data

# Function to get video IDs from a playlist (All videos in the channel).
def get_video_ids(youtube, playlist_id):
    """
    Fetch all video IDs from a YouTube playlist.

    Parameters:
        youtube (object): The YouTube service object.
        playlist_id (str): The ID of the YouTube playlist.

    Returns:
        list: A list of video IDs.
    """
    request = youtube.playlistItems().list(
        part = 'contentDetails',
        playlistId = playlist_id,
    maxResults = 50)
    response = request.execute()
    video_ids = []
    
    for i in range(len(response['items'])):
        video_ids.append(response['items'][i]['contentDetails']['videoId'])
        
    next_page_token = response.get('nextPageToken')
    more_pages = True
    
    while more_pages:
        if next_page_token is None: 
            more_pages = False
        else:
            request = youtube.playlistItems().list(
                    part= 'contentDetails',
                    playlistId = playlist_id,
                    maxResults = 50,
                    pageToken = next_page_token)
            response = request.execute()
            
    #change for next page
            for i in range(len(response['items'])):
                video_ids.append(response['items'][i]['contentDetails']['videoId'])
            next_page_token = response.get('nextPageToken')
    return video_ids

# Fetch details for a given list of video IDs.
def get_video_details(youtube, video_ids): 
    """
    Get details (title, publication date, etc.) for a list of video IDs.

    Parameters:
        youtube (object): The YouTube service object.
        video_ids (list): List of YouTube video IDs.

    Returns:
        list: A list of dictionaries containing video details.
    """
    all_video_details = [] #list of all videos with their details
    for i in range (0, len(video_ids), 50):
        request = youtube.videos().list(
            part = 'snippet',
            id= ','.join(video_ids[i:i+50]))
        response = request.execute()
        #create dictionary to organize the details of each video:
        for video in response['items']:
            video_details = dict(Title = video['snippet']['title'],
                             Publication_date = video['snippet']['publishedAt'],
                             Description = video['snippet']['description'],
                             Video_url= f"https://www.youtube.com/watch?v={video['id']}",
                             Tags = video['snippet']['tags'] if 'tags' in video['snippet'] else [],
Categories = video['snippet']['categoryId'] if 'categoryId' in video['snippet'] else '',
                             Channel_name= video['snippet']['channelTitle'],
                            Duration= video['contentDetails']['duration'] if 'contentDetails' in video else '',
                             Video_id=video['id'])
            all_video_details.append(video_details) 
    return all_video_details  #returns a list of all video ids with their details (title, desc, etc)

# Fetch transcriptions for a single video ID.
def get_transcription(one_video_id, l_languages = ['en', 'fa', 'ru']): #returns a list of strings where each string represents a subtitle
    """
    Fetch transcriptions for a given video ID.

    Parameters:
        one_video_id (str): The YouTube video ID.
        l_languages (list, optional): List of preferred languages for the transcription. Defaults to ['en', 'fa', 'ru'].

    Returns:
        list: A list of transcriptions if available, otherwise returns a string indicating transcription could not be fetched.
    """
    try:
        outls = [] #list which captures the output of all subtitles
        tx = YouTubeTranscriptApi.get_transcript(one_video_id, languages = l_languages)
        #for each item in that 'tx' object (which is a list)
        for i in tx: 
            outtxt = (i['text']) #pick up the text
            outls.append(outtxt) #append each line of text to our list of subtitles
            with open ('op.txt', 'a') as opf: #write?/ don't really know what this does
                opf.write(outtxt + '\n')
        return outls
    except Exception:
        return 'could not transcribe'
    
