# ydnhbot
有点难画呢，一个telegram bot。基于python2.7。   
it's a little difficult to draw ah, a telegram bot.based on python2.7



# install
```sh
pip install -r requirements.txt
```

# config
找[@botfather](https://t.me/botfather)申请一个token，修改`ydnhbot.py`第22行的TOKEN变量为申请的`token`。  
request a bot token from [@botfather](https://t.me/botfather), change the `TOKEN` in `ydnhbot.py` at line 22 with your token. 

# run
```sh
nohup python ydnhbot.py &
```

# keep running
推荐使用supervisor来监控程序运行，当遇到错误时自动重启。  
monitor status of the program via supervisor is recommended, so that it can be restart when stop by errors.
>note: edit `directory` in bot.conf before
```sh
pip install supervisor
cp bot.conf /etc/supervisor/conf.d/
supervisor reload
```
thus,bot is running.

have fun!

# thanks
@moonoulong
