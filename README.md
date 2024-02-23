# daily_news_bot
Telegram bot based on the nytimes API for receiving news.

# Installation

* Clone this repository
```
  git clone https:github.com/FlewRr/daily_news_bot
```

* Create your bot and application using [BotFather](https://t.me/botfather) and [The New York Times API](https://developer.nytimes.com/apis)

* Install [docker engine](https://docs.docker.com/engine/install/) or [docker desktop](https://docs.docker.com/get-docker/)

* Build and run container (locally):
```
  export BOT_TOKEN=<BOT_TOKEN>
  export API_TOKEN=<API_TOKEN>
  docker-compose up  ## to build and run
  docker-compose down  ## to stop
```
