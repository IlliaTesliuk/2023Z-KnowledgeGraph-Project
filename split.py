import os
import numpy as np
import pandas as pd
import argparse

def create_playlist_df(songs):
    playlists = songs[[s for s in songs.columns if 'playlist_' in s]]
    playlists = playlists.drop_duplicates()
    playlists.drop_duplicates(subset=['playlist_id']).reset_index().iloc[:,1:]
    return playlists

def create_artist_df(songs):
    artists = pd.DataFrame(songs['track_artist'].unique(),columns=['artist_name']).reset_index()
    artists.columns = ['artist_id','artist_name']
    return artists

def create_genre_df(songs):
    gr = songs['playlist_genre'].value_counts().keys().to_list()
    sgr = songs['playlist_subgenre'].value_counts().keys().to_list()
    all_genres = gr + sgr
    genres = pd.DataFrame(np.array(all_genres),columns=['genre_name']).reset_index()
    genres.columns = ['genre_id','genre_name']
    return genres

def create_album_df(songs):
    albums = songs[["track_album_id","track_album_name","track_album_release_date"]]
    albums = albums.drop_duplicates()
    albums.columns = ['album_id','album_name','album_release_date']
    return albums

def split_songs_df(src_dir, src_file):
    songs = pd.read_csv(os.path.join(src_dir, src_file)).dropna()
    # list of albums
    create_album_df(songs).to_csv(os.path.join(src_dir,'albums.csv'),index=False)
    # list of artists
    create_artist_df(songs).to_csv(os.path.join(src_dir,'artists.csv'),index=False)
    # playlists
    create_playlist_df(songs).to_csv(os.path.join(src_dir,'playlists.csv'),index=False)
    # genres
    create_genre_df(songs).to_csv(os.path.join(src_dir,'genres.csv'),index=False)
    print(f"All files are successfully saved to {src_dir}")
    

def main():
    parser = argparse.ArgumentParser(description='newslinking', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--src_file', default='spotify_songs.csv', type=str, help='name of CSV file with the Spotify dataset')
    parser.add_argument('--src_dir', default='spotify_songs', type=str, help='directory with the dataset file')
    args = parser.parse_args()

    if not os.path.exists(args.src_dir):
        print(f"[Error] Source directory {args.src_dir} doesn't exist")
    elif not os.path.exists(os.path.join(args.src_dir, args.src_file)):
        print(f"[Error] Source file {args.src_file} doesn't exist")
    else:
        split_songs_df(src_dir, src_file)

if __name__ == "__main__":
    main()