# Timmy Challenge

## Challenge

1. Check if the input is a valid mountain (uses pushdown automaton)

2. Check if the input is a valid mountain wwith tunnels (uses pushdown automaton)

3. Get the minimum amount of changes to turn an invalid mountain into a valid one

## Requirement
- Docker compose

## Api  🚀
 [![Run in Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/25152348/2s8ZDa1gaq)

# App 🏁
```bash
docker-compose up -d
```
Local API [URL](http://localhost:8000/timmy_challenge/timmy_mountains/)

# Testing 🕵️‍
```bash
docker-compose up timmy-challenge_web_test
```
```bash
python manage.py test timmy_mountains/test
```
Jan 2023 [URL](https://airnguru-challenge.s3.amazonaws.com/Airnguru+preinterview+challenge+(With+Watermark).pdf)
