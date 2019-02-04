'''Allows the user to create a "playlist" of music in an excel file that will be
played continuously ad-free on youtube thanks to a little selenium magic'''

from default_functions import click,fill,wait,get,tab,Name,driver
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import getpass

#Creates a dataframe of the playlist file with all the song titles and artists in it
df = pd.read_excel('/Users/'+Name+'/Documents/Python/Python_Files/playlist.xlsx',encoding = "ISO-8859-1")

#Navigates to the youtube homepage
driver.get('https://www.youtube.com/')

#Assigns the song and artist variables to the first song and artist in the dataframe
song = df['Song'][0]
artist = df['Artist'][0]

#Searches for the song and artist on youtube
fill.Name('search_query',song+' - '+artist)
click.Id('search-icon-legacy')

#Clicks the first title that contains both the song name and artist. 
#The text in the title and the user entered rasponses are first converted to lower case
click.Xpath('(//a[contains(translate(., "ABCDEFGHIJKLMNOPQRSTUVWXYZ","abcdefghijklmnopqrstuvwxyz"),"'+song.lower()+'") and contains(translate(.,"ABCDEFGHIJKLMNOPQRSTUVWXYZ","abcdefghijklmnopqrstuvwxyz"),"'+artist.lower()+'") and @id = "video-title"])[1]')

#Assigns the ad variable to default False state
noAd = False

#Clicks mute to avoid any potential ad noise 
click.Xpath('//*[@class="ytp-mute-button ytp-button"]')

#Determines whether or not there is an ad on the video
try:
    WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="ytp-ad-text ytp-ad-preview-text"]')))
except:
    noAd = True

#If there is an ad, the if statement will run
if noAd == False:
    try:
        #If the text "ideo will" is in the ad text it means it is an unskippable ad
        driver.find_element_by_xpath('//div[contains(text(),"ideo will") and @class="ytp-ad-text ytp-ad-preview-text"]')

        #If it is an unskippable ad, we need to collect the total duration of the ad, split it by the colon, and sleep the script for the second duration of the ad
        times = get.Text('//*[@class="ytp-time-duration"]')
        adTime = times.split(':')
        time.sleep(int(adTime[1]))
    except:
        #If the ad is skippable, we will be able to skip the ad after 5 seconds. The script sleeps for 5 seconds then presses the skip button
        time.sleep(5)
        click.Xpath('//button[@class="ytp-ad-skip-button ytp-button"]')

#Creates dictionary that will be used to collect total durations of videos
dictionary = {}

#Briefly pauses the video in order to get the controls to appear
click.Xpath('//video')

#Un-mutes the video and collects the video duration to be used later, then presses play
click.Xpath('//button[@class="ytp-mute-button ytp-button"]')
dictionary['0'] = get.Text('//*[@class="ytp-time-duration"]')
click.Xpath('//video')

#Prints the title of the song
print('')
print(song.title()+' - '+artist.title())
print('')

#The remainder of the songs will be played in this loop after the first is set up
for i in range(len(df['Song'])):

    #Creates a timing variable that will be used to determine how long it took to set up the next song
    start = time.time()

    #This check is in place to prevent the last run of the loop from creating a new tab as there will be no more songs left in the list
    if i != len(df['Song'])-1:
        song = df['Song'][i+1]
        artist = df['Artist'][i+1]

        #Creates a new tab to load and remove abs from the next video while the previous video is playing
        tab.New('https://www.youtube.com/',1)
        fill.Name('search_query',song+' - '+artist)
        click.Id('search-icon-legacy')
        click.Xpath('(//a[contains(translate(., "ABCDEFGHIJKLMNOPQRSTUVWXYZ","abcdefghijklmnopqrstuvwxyz"),"'+song.lower()+'") and contains(translate(.,"ABCDEFGHIJKLMNOPQRSTUVWXYZ","abcdefghijklmnopqrstuvwxyz"),"'+artist.lower()+'") and @id = "video-title"])[1]')

        #Clicks mute to avoid any potential ad noise 
        click.Xpath('//*[@class="ytp-mute-button ytp-button"]')
        noAd = False
        try:
            WebDriverWait(driver, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@class="ytp-ad-text ytp-ad-preview-text"]')))
        except:
            noAd = True
        if noAd == False:
            try:
                driver.find_element_by_xpath('//div[contains(text(),"ideo will") and @class="ytp-ad-text ytp-ad-preview-text"]')
                times = get.Text('//*[@class="ytp-time-duration"]')
                adTime = times.split(':')
                time.sleep(int(adTime[1]))
            except:
                time.sleep(5)
                click.Xpath('//button[@class="ytp-ad-skip-button ytp-button"]')

        #Pauses the video and unmutes it, preparing it to be played after the previous song ends
        click.Xpath('//video')
        click.Xpath('//button[@class="ytp-mute-button ytp-button"]')

        #Switches to the first tab that contains the video currently playing
        tab.Switch(0)
    
    #Converts the time duration of the video playing previously selected into seconds
    duration = dictionary[str(i)]
    durationSplit = duration.split(':')
    totalDuration = (int(durationSplit[0])*60)+int(durationSplit[1])

    #End time used to determine how long it took to set up the next song
    end = time.time()

    #Sleeps the script for the duration of the video playing minus the amount of time taken to set up the next video
    time.sleep(totalDuration-(end-start))

    #Closes the current tab once the video has finished playing
    driver.close()

    #Only runs if this is not the last run of the loop
    if i != len(df['Song'])-1:

        #Switches to the main tab and plays the next video
        tab.Switch(0)
        click.Xpath('//video')

        #Collects the time duration of the video to be used for future calculations and prints the song title
        dictionary[str(i+1)] = get.Text('//*[@class="ytp-time-duration"]')
        print(song.title()+' - '+artist.title())
        print('')




