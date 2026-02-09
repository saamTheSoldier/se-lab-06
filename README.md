# استقرار نرم‌افزار با معماری MicroService به کمک Docker

## ساختار پروژه

- **backend**: سرویس RESTful API با عملیات CRUD (Flask + PostgreSQL)
- **nginx**: Load Balancer با الگوریتم least_conn
- **db**: پایگاه‌داده PostgreSQL مشترک

## نحوه اجرا

```bash
docker compose up --build -d
```

API روی پورت 8080 در دسترس است: http://localhost:8080

---
*گزارش و اسکرین‌شات‌ها در مراحل بعدی تکمیل می‌شود.*
