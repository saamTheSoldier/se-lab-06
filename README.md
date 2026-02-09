# استقرار نرم‌افزار با معماری MicroService به کمک Docker

## ساختار پروژه

- **backend**: سرویس RESTful API با عملیات CRUD (Flask + SQLite)
- **nginx**: Load Balancer با الگوریتم least_conn
- **پایگاه‌داده مشترک**: SQLite در volume مشترک بین backend1 و backend2

## نحوه اجرا

```bash
docker compose up --build -d
```

API روی پورت 8080 در دسترس است: http://localhost:8080

---

## گزارش آزمایش

### ۱. Build و اجرا با Docker Compose

![اسکرین‌شات docker compose up](image.png)

### ۲. خروجی docker container ls

```
CONTAINER ID   IMAGE                COMMAND                  CREATED          STATUS          PORTS                                     NAMES
xxxxx          se-lab-06-backend2   "python app.py"          X seconds ago    Up X seconds    5000/tcp                                  se-lab-06-backend2-1
xxxxx          se-lab-06-nginx      "/docker-entrypoint.…"   X minutes ago    Up X minutes    0.0.0.0:8080->80/tcp                     se-lab-06-nginx-1
xxxxx          se-lab-06-backend1   "python app.py"          X minutes ago    Up X minutes    5000/tcp                                  se-lab-06-backend1-1
```

*اسکرین‌شات خروجی این دستور را اینجا قرار دهید یا تصویر `image.png` را به‌روز کنید.*

### ۳. خروجی docker image ls

```
REPOSITORY           TAG       SIZE
se-lab-06-backend2   latest    165MB
se-lab-06-backend1   latest    165MB
se-lab-06-nginx      latest    62.1MB
```

*اسکرین‌شات خروجی این دستور را اینجا قرار دهید.*

---
*مراحل بعدی (نمایش API در مرورگر، scale کردن backend، پرسش stateless) در ادامه تکمیل می‌شود.*
