# استقرار نرم‌افزار با معماری MicroService به کمک Docker

## ساختار پروژه

- **backend**: سرویس RESTful API با عملیات CRUD (Flask + SQLite)
- **nginx**: Load Balancer با الگوریتم least_conn
- **پایگاه‌داده مشترک**: SQLite در volume مشترک بین backend1، backend2 و backend3

## نحوه اجرا

```bash
docker compose up --build -d
```

API روی پورت 8080 در دسترس است: http://localhost:8080

---

## گزارش آزمایش

### ۱. Build و اجرا با Docker Compose

![اسکرین‌شات docker compose ps](docker%20compose%20ps.png)

### ۲. خروجی docker image ls

![اسکرین‌شات docker image ls](docker_image_ls.png)

### ۳. نمایش اجرای موفق API در مرورگر یا Postman

** endpoint های API:**

| متد | آدرس | توضیح |
|-----|------|-------|
| GET | http://localhost:8080/health | بررسی سلامت سرویس |
| GET | http://localhost:8080/api/items | لیست همه آیتم‌ها |
| GET | http://localhost:8080/api/items/1 | دریافت آیتم با شناسه |
| POST | http://localhost:8080/api/items | ایجاد آیتم (body: `{"name":"نام","description":"توضیح"}`) |
| PUT | http://localhost:8080/api/items/1 | بروزرسانی آیتم |
| DELETE | http://localhost:8080/api/items/1 | حذف آیتم |

**تست سریع در ترمینال:**
```bash
curl http://localhost:8080/health
curl http://localhost:8080/api/items
```

### ۴. Scale کردن backend (کنترل فشار روی سرویس‌ها)

با افزایش فشار روی backend، یک نمونه دیگر (backend3) اضافه شد تا بار بین سرویس‌ها توزیع شود:

- **تغییر در docker-compose.yml**: اضافه شدن سرویس backend3
- **تغییر در nginx.conf**: اضافه شدن backend3 به upstream

پایگاه‌داده همچنان مشترک است و قادر به تحمل بار است؛ فقط سرویس‌های backend scale شده‌اند.

```bash
docker compose up -d --build
docker compose ps
```

برای اطمینان، خروجی `docker compose ps` با ۳ backend در حال اجرا قابل مشاهده است.
