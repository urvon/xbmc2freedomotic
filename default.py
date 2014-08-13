import xbmc,xbmcgui                                                                                                                                                                      
import subprocess,os
#import urllib2
import xbmcaddon
import stomp

#Initialize ADDON
settings = xbmcaddon.Addon(id='xbmc.freedomotic.addon')

#Initialize ADDON INFORMATION
host				=  settings.getSetting( "host" )
port				=  settings.getSetting( "port" )
periph_id			=  settings.getSetting( "periph_id" )

#Initialize value for ref.
menu = 0
video = 0
audio = 0
stopmenu = 0
conn = 0

                                                                                                                                                                                        
class MyPlayer(xbmc.Player):                                                                                                                                                             
                                                                                                                                                                                       
        def __init__ (self):                                                                                                                                                             
                xbmc.Player.__init__(self)             

                if (str(settings.getSetting("xbmc_started")) == "Yes"):
                        #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=1' % (host, periph_id, port))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=1' % (host, periph_id, port))
                                                                                                                                                                                        
        def onPlayBackStarted(self):

                xbmc.sleep(200) # it may take some time for xbmc to read tag info after playback started
                if xbmc.Player().isPlayingVideo():
                        currentvideo = xbmc.Player().getVideoInfoTag().getTitle()
                        currentvideo = currentvideo.replace(' ', '_')
                        if (str(settings.getSetting("video_started")) == "Yes"):
                                #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=2' % (host, periph_id, port))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=2' % (host, periph_id, port))
                                
                        #if (str(settings.getSetting("video_title")) == "Yes"):
                        #        urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=%s' % (periph_id, ip, port, currentvideo))
                        #        if (str(settings.getSetting("debug_mod")) == "Yes"):
                        #               print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=%s' % (periph_id, ip, port, currentvideo))
                
                if xbmc.Player().isPlayingAudio() == True:
                        currentsong = xbmc.Player().getMusicInfoTag().getTitle()
                        currentsong = currentsong.replace(' ', '_')
                        if (str(settings.getSetting("audio_started")) == "Yes"):
                                #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=3' % (host, periph_id, port))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=3' % (host, periph_id, port))
                                
                        #if (str(settings.getSetting("audio_title")) == "Yes"):
                        #        urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=%s' % (periph_id, ip, port, currentsong))
                        #        if (str(settings.getSetting("debug_mod")) == "Yes"):
                        #                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=%s' % (periph_id, ip, port, currentsong))
                                
        def onPlayBackEnded(self):                                                                                                                                                       
                if (VIDEO == 1):                                                                                                                                                         
                        if (str(settings.getSetting("video_ended")) == "Yes"):
                                #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=4' % (host, periph_id, port)) 
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=4' % (host, periph_id, port)) 
                        
                if (AUDIO == 1):
                        if (str(settings.getSetting("audio_ended")) == "Yes"):
                                #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=5' % (host, periph_id, port))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=5' % (host, periph_id, port))
                                                                                                                                                                                         
        def onPlayBackStopped(self):                                                                                                                                                     
                if (VIDEO == 1):                                                                                                                                                         
                        if (str(settings.getSetting("video_stopped")) == "Yes"):
                                #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=6' % (host, periph_id, port))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=6' % (host, periph_id, port))
   
                if (AUDIO == 1):
                        if (str(settings.getSetting("audio_stopped")) == "Yes"):
                                #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=7' % (host, periph_id, port))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=7' % (host, periph_id, port))
                                                                                                                                                                                          
        def onPlayBackPaused(self):                                                                                                                                                      
                if xbmc.Player().isPlayingVideo():                                                                                                                                       
                        if (str(settings.getSetting("video_paused")) == "Yes"):
                                #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=8' % (host, periph_id, port))
				conn = stomp.Connection(host_and_ports = [(host, 61666)])
		                conn.start()
		                conn.connect()
                                conn.send(body='test', destination='/queue/test')
				conn.disconnect()
                                print("stomp message sended")
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=8' % (host, periph_id, port))
        
                if xbmc.Player().isPlayingAudio():
                        if (str(settings.getSetting("audio_paused")) == "Yes"):
                                #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=9' % (host, periph_id, port))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=9' % (host, periph_id, port))
                        
        def onPlayBackResumed(self):                                                                                                                                                     
                if xbmc.Player().isPlayingVideo():                                                                                                                                       
                        if (str(settings.getSetting("video_resumed")) == "Yes"):
                                #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=10' % (host, periph_id, port))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=10' % (host, periph_id, port))

                if xbmc.Player().isPlayingAudio():
                        if (str(settings.getSetting("audio_resumed")) == "Yes"):
                                #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=11' % (host, periph_id, port))
                                if (str(settings.getSetting("debug_mod")) == "Yes"):
                                        print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=11' % (host, periph_id, port))
                                   
player=MyPlayer()                                                                                                                                                                        
                                                                                                                                                                                         
VIDEO = 0

while(not xbmc.abortRequested):

        win   = (xbmcgui.getCurrentWindowId())

        if xbmc.Player().isPlaying():
                stopmenu = 1
                if xbmc.Player().isPlayingVideo():                                                                                                                                       
                        VIDEO = 1
                        AUDIO = 0
                else:                                                                                                                                                                    
                        VIDEO = 0
                        AUDIO = 1

        #Return to menu after playing
        if not xbmc.Player().isPlaying() and stopmenu != 0:
                menu = 0
                stopmenu = 0
                
                                                                                                                                                               
       
        if win == 10000 and menu != 10000:
                menu = 10000
                if (str(settings.getSetting("menu_home")) == "Yes"):
                        #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=12' % (host, periph_id, port))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=12' % (host, periph_id, port))
                                
        if win == 10001 and menu != 10001:
                menu = 10001
                if (str(settings.getSetting("menu_program")) == "Yes"):
                        #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=13' % (host, periph_id, port))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=13' % (host, periph_id, port))
        
        
        if win == 10002 and menu != 10002:
                menu = 10002
                if (str(settings.getSetting("menu_picture")) == "Yes"):
                        #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=14' % (host, periph_id, port))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=14' % (host, periph_id, port))
        
        
        if win == 10004 and menu != 10004:
                menu = 10004
                if (str(settings.getSetting("menu_setting")) == "Yes"):
                        #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=15' % (host, periph_id, port))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=15' % (host, periph_id, port))
                                

       #navigate video menu 
        if win == 10006 and menu != 10006:
                menu = 10006
                if (str(settings.getSetting("menu_video")) == "Yes"):
                       #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=16' % (host, periph_id, port))
                       if (str(settings.getSetting("debug_mod")) == "Yes"):
                               print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=16' % (host, periph_id, port))

                       
        if win == 10024 and menu != 10024:
                menu = 10024
                if (str(settings.getSetting("menu_video")) == "Yes"):
                       #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=16' % (host, periph_id, port))
                       if (str(settings.getSetting("debug_mod")) == "Yes"):
                               print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=16' % (host, periph_id, port))

        if win == 10025 and menu != 10025:
                menu = 10025
                if (str(settings.getSetting("menu_video")) == "Yes"):
                       #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=16' % (host, periph_id, port))
                       if (str(settings.getSetting("debug_mod")) == "Yes"):
                               print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=16' % (host, periph_id, port))

                       
        if win == 10028 and menu != 10028:
                menu = 10028
                if (str(settings.getSetting("menu_video")) == "Yes"):
                       #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=16' % (host, periph_id, port))
                       if (str(settings.getSetting("debug_mod")) == "Yes"):
                               print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=16' % (host, periph_id, port))


        #navigate audio menu                 
        if win == 10005 and menu != 10005:
                menu = 10005
                if (str(settings.getSetting("menu_music")) == "Yes"):
                        #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=17' % (host, periph_id, port))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=17' % (host, periph_id, port))


        if win == 10500 and menu != 10500:
                menu = 10500
                if (str(settings.getSetting("menu_music")) == "Yes"):
                        #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=17' % (host, periph_id, port))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=17' % (host, periph_id, port))


        if win == 10501 and menu != 10501:
                menu = 10501
                if (str(settings.getSetting("menu_music")) == "Yes"):
                        #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=17' % (host, periph_id, port))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=17' % (host, periph_id, port))


        if win == 10502 and menu != 10502:
                menu = 10502
                if (str(settings.getSetting("menu_music")) == "Yes"):
                        #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=17' % (host, periph_id, port))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=17' % (host, periph_id, port))



        if win == 12600 and menu != 12600:
                menu = 12600
                if (str(settings.getSetting("menu_weather")) == "Yes"):
                        #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=18' % (host, periph_id, port))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=18' % (host, periph_id, port))

    
        xbmc.sleep(1000)
if (str(settings.getSetting("xbmc_ended")) == "Yes"):
                        #urllib2.urlopen('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=0' % (host, periph_id, port))
                        if (str(settings.getSetting("debug_mod")) == "Yes"):
                                print('http://my.zipato.com:8080/zipato-web/remoting/attribute/set?ip=%s&ep=%s&apiKey=%s&value1=0' % (host, periph_id, port))
