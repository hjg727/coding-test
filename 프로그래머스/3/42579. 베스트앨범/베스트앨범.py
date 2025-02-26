def solution(genres, plays):
    album = {}
    album_sum = {}  # 장르별 총 재생 횟수를 저장할 딕셔너리

    for i in range(len(genres)):
        album.setdefault(genres[i], []).append((i, plays[i]))
        album_sum[genres[i]] = album_sum.get(genres[i], 0) + plays[i]

    album_sum = dict(sorted(album_sum.items(), key= lambda x: x[1], reverse=True))

    for _, songs in album.items():
        songs.sort(key=lambda x: (-x[1], x[0]))
    res = []

    for genre in album_sum.keys():
        songs = album[genre]
        if len(songs) > 2:
            songs = songs[:2]
        
        for song in songs:
            res.append(song[0])
    return(res)
