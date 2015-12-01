# RUN LOCALLY
Clone into this reop 'heroku' branch

    git clone -b heroku https://github.com/kobiburnley/youtube-dl.git
    cd youtube-dl
    C:\Python27\python.exe ~/youtube-dl/web.py
Then in your browser go to http://localhost:5000/?id=koeW4g8Y-lg&formats=251,171

# BUILD STREAM REQUEST
To the "formats" http get parameter pass your desired formats (detailed below) descending order, the first that exists will be the result
Exmaple: http://localhost:5000/?id=koeW4g8Y-lg&formats=22,18

Known formats (number in the begining of each row):

    249 - audio only (DASH audio), webm, 50
    250 - audio only (DASH audio), webm, 70
    171 - audio only (DASH audio), webm, 128
    140 - audio only (DASH audio), m4a, 128
    251 - audio only (DASH audio), webm, 160
    141 - audio only (DASH audio), m4a, 256
    278 - 256x144 (DASH video), webm,
    160 - 256x144 (DASH video), mp4,
    242 - 426x240 (DASH video), webm,
    133 - 426x240 (DASH video), mp4,
    243 - 640x360 (DASH video), webm,
    134 - 640x360 (DASH video), mp4,
    244 - 854x480 (DASH video), webm,
    135 - 854x480 (DASH video), mp4,
    247 - 1280x720 (DASH video), webm,
    136 - 1280x720 (DASH video), mp4,
    248 - 1920x1080 (DASH video), webm,
    137 - 1920x1080 (DASH video), mp4,
    17 - 176x144 (small), 3gp,
    36 - 320x240 (small), 3gp,
    5 - 400x240 (small), flv,
    43 - 640x360 (medium), webm,
    18 - 640x360 (medium), mp4,
    22 - 1280x720 (hd720), mp4,


# DEPLOY TO HEROKU
You can fort this repository and create a new app in the Heroku dashboard. In the deploy tab choose Github deploy and the branch to deploy from (heroku branch).

OR
    cd youtube-dl
    heroku login
    heroku create *chooose-app-name*
    git push heroku master


# COPYRIGHT

youtube-dl is released into the public domain by the copyright holders.
