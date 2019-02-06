# Music_Freedom

music.py:
This script allows the user to play a misical playlist on youtube without having to listen to a single ad. The user simply needs to put the songs they want to play in a file called "playlist.xlsx." The script will then pull these songs using the pandas python library and search for these songs on youtube. The script will mute/skip all ads, so the user never has to have their music interupted. The script will que the next song and skip its ad while the current song is playing to avoid and lull in music playback.

topCharts/:
This is a scrapy project that allows the user to scrape the top 40 hits into a format that can be used by the music.py script. All the user needs to do is navigate to the topCharts/topCharts/ and run scrapy crawl topcharts -o playlist.csv. Once you are given an output file, you can simply move this file to the appropriate folder for the music.py script and run it to listen to the top40 ad-free.
