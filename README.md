# daily_news_bot
Telegram bot based on the nytimes API for receiving news.

# Installation

* Clone this repository
```
  git clone https:github.com/FlewRr/daily_news_bot
```

* Create your bot with [BotFather](https://t.me/botfather)

* Create application at [The New York Times API website](https://developer.nytimes.com/apis)

* Install [docker engine](https://docs.docker.com/engine/install/) or [docker desktop](https://docs.docker.com/get-docker/)

* Build and run container:
```
  docker build -t app .
  docker run -e BOT_TOKEN=<BOT_TOKEN> -e API_TOKEN=<API_TOKEN> -p 9000:80 -t app 
```
        or
```
  docker-compose up -d  ## to build and run
  docker-compose down  ## to stop
```
