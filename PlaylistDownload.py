api_key = ''
from apiclient.discovery import build
import pytube, os, time, keyboard 
from os import path
from pytube import YouTube
youtube = build('youtube','v3', developerKey=api_key)
def get_playlist_video(my_id, playlist_id):
    res = youtube.playlistItems().list(id=my_id, part='snippet').execute()
    videos = []
    next_page_token = None
    while True:
        res = youtube.playlistItems().list(playlistId=playlist_id, part='snippet', maxResults = 50, pageToken = next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        if next_page_token is None:
            break
    return videos
def get_title_playlist (my_id, playlist_id):
    req = youtube.playlists().list(part="snippet,contentDetails",channelId=my_id,maxResults=50).execute()
    items = []
    items += req['items']
    count_playlist = req['pageInfo']['totalResults']
    for x in range(count_playlist):
        if items[x]['id'] == playlist_id:
            title = items[x]['snippet']['title']
    return title
videos = get_playlist_video('ch_id', 'playlist_id')
title = get_title_playlist('ch_id', 'playlist_id') 
y = 0
z = 0
video_id_store = []
for video_count in videos:
    y += 1    
for files in os.listdir('D:\Playlist'):
    z += 1
# Face if de mai jos daca nu e descarcat nimic din playlist
if y > z and z == 0:
    for video in videos:
        video_id_store.append(video['snippet']['resourceId']['videoId'])
    for w in range(y):
        username = video['snippet']['channelTitle']
        video_url = 'https://www.youtube.com/watch?v='+video_id_store[w] 
        youtube = pytube.YouTube(video_url)
        video1 = youtube.streams.get_audio_only(subtype=str('mp4'))
        video1.download('D:\Playlist')
        for files1 in os.listdir('D:\Playlist'):
            if files1.endswith('.mp4'):
                m = 0
                z = 0
                w_o_extension = os.path.splitext(files1)[0]
                while w_o_extension == "YouTube":
                    for files2 in os.listdir('D:\Playlist'):
                        m += 1 
                        z += 1
                    os.remove('D:\Playlist'+'\\'+files1)
                    dif1 = y-z
                    where_resume1 = y - (dif1+1)
                    for video in videos:
                        video_id_store.append(video['snippet']['resourceId']['videoId'])
                    for w in range(1):
                        username = video['snippet']['channelTitle']
                        id_resume = where_resume1
                        video_url = 'https://www.youtube.com/watch?v='+video_id_store[id_resume] 
                        youtube = pytube.YouTube(video_url)
                        video1 = youtube.streams.get_audio_only(subtype=str('mp4'))
                        video1.download('D:\Playlist') 
                        for files3 in os.listdir('D:\Playlist'):
                            if files3.endswith('.mp4'):
                                w_o_extension = os.path.splitext(files3)[0]
                                new_name = username+'_' + title +'_' + w_o_extension
                                os.rename(r'D:\Playlist'+'\\'+w_o_extension+'.mp4',r'D:\Playlist'+'\\'+new_name+'.wav')
                        break
                if w_o_extension != 'YouTube' and m == 0:
                    new_name = username+'_' + title +'_' + w_o_extension
                    os.rename(r'D:\Playlist'+'\\'+w_o_extension+'.mp4',r'D:\Playlist'+'\\'+new_name+'.wav')
# Face elif de mai jos daca din playlist a fost deja descarct 1 sau mai multe melodii
elif y > z and z != 0:
    z=0
    for file4 in os.listdir('D:\Playlist'):
        z += 1
    for files13 in os.listdir('D:\Playlist'):
        #Face if de mai jos daca ultima melodie nu a fost descarcata complet
        if files13.endswith('.mp4'):
            os.remove('D:\Playlist'+'\\'+files13)
            dif = y-z
            where_resume = y - (dif+1)
            for video in videos:
                video_id_store.append(video['snippet']['resourceId']['videoId'])
            for w in range(dif):
                username = video['snippet']['channelTitle']
                id_resume = where_resume + w
                video_url = 'https://www.youtube.com/watch?v='+video_id_store[id_resume] 
                youtube = pytube.YouTube(video_url)
                video1 = youtube.streams.get_audio_only(subtype=str('mp4'))
                video1.download('D:\Playlist') 
                for files5 in os.listdir('D:\Playlist'):
                    if files5.endswith('.mp4'):
                        m = 0
                        z = 0
                        w_o_extension = os.path.splitext(files5)[0]
                        # Unele melodii le pune numele de Youtube si nush dc asa ca am facut while asta pana le descarca cu numele care trebuie
                        while w_o_extension == "YouTube":
                            for files6 in os.listdir('D:\Playlist'):
                                m += 1 
                                z += 1
                            os.remove('D:\Playlist'+'\\'+files5)
                            dif2 = y-z
                            where_resume2 = y - (dif2+1)
                            for video in videos:
                                video_id_store.append(video['snippet']['resourceId']['videoId'])
                            for w in range(1):
                                username = video['snippet']['channelTitle']
                                id_resume = where_resume2
                                video_url = 'https://www.youtube.com/watch?v='+video_id_store[id_resume]
                                youtube = pytube.YouTube(video_url)
                                video1 = youtube.streams.get_audio_only(subtype=str('mp4'))
                                video1.download('D:\Playlist') 
                                for files7 in os.listdir('D:\Playlist'):
                                    if files7.endswith('.mp4'):
                                        w_o_extension = os.path.splitext(files7)[0]
                                        new_name = username+'_' + title +'_' + w_o_extension
                                        os.rename(r'D:\Playlist'+'\\'+w_o_extension+'.mp4',r'D:\Playlist'+'\\'+new_name+'.wav')
                                break
                        if w_o_extension != 'Youtube' and m == 0:
                            new_name = username+'_' + title +'_' + w_o_extension
                            os.rename(r'D:\Playlist'+'\\'+w_o_extension+'.mp4',r'D:\Playlist'+'\\'+new_name+'.wav')
        else:                    
            dif = y-z
            where_resume = y - (dif)
            for video in videos:
                video_id_store.append(video['snippet']['resourceId']['videoId'])
            for w in range(dif):
                username = video['snippet']['channelTitle']
                id_resume = where_resume + w
                video_url = 'https://www.youtube.com/watch?v='+video_id_store[id_resume]
                youtube = pytube.YouTube(video_url)
                video1 = youtube.streams.get_audio_only(subtype=str('mp4'))
                video1.download('D:\Playlist') 
                for files3 in os.listdir('D:\Playlist'):
                    if files3.endswith('.mp4'):
                        m = 0
                        z = 0
                        w_o_extension = os.path.splitext(files3)[0]
                        while w_o_extension == "YouTube":
                            for files6 in os.listdir('D:\Playlist'):
                                m += 1 
                                z += 1
                            os.remove('D:\Playlist'+'\\'+files3)
                            dif3 = y-z
                            where_resume3 = y - (dif3+1)
                            for video in videos:
                                video_id_store.append(video['snippet']['resourceId']['videoId'])
                            for n in range(1):
                                username = video['snippet']['channelTitle']
                                id_resume = where_resume3
                                video_url = 'https://www.youtube.com/watch?v='+video_id_store[id_resume] 
                                youtube = pytube.YouTube(video_url)
                                video1 = youtube.streams.get_audio_only(subtype=str('mp4'))
                                video1.download('D:\Playlist') 
                                for files7 in os.listdir('D:\Playlist'):
                                    if files7.endswith('.mp4'):
                                        w_o_extension = os.path.splitext(files7)[0]
                                        new_name = username+'_' + title +'_' + w_o_extension
                                        try:
                                            os.rename(r'D:\Playlist'+'\\'+w_o_extension+'.mp4',r'D:\Playlist'+'\\'+new_name+'.wav')
                                        except FileExistsError:
                                            os.remove('D:\Playlist'+'\\'+files7)
                                            quit()
                                break
                        if w_o_extension != 'YouTube' and m == 0:
                            new_name = username+'_' + title +'_' + w_o_extension
                            try:
                                os.rename(r'D:\Playlist'+'\\'+w_o_extension+'.mp4',r'D:\Playlist'+'\\'+new_name+'.wav')
                            except FileExistsError:
                                os.remove('D:\Playlist'+'\\'+files3)
                                quit()
