# Account API

Telegram bot foydalanuvchilarini ro'yxatga olish va boshqarish uchun Django REST Framework asosida qurilgan backend API.

---

## Loyiha tuzilmasi

```
project/
├── api/                    # Asosiy ilova
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
└── config/                 # Loyiha sozlamalari
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## Texnologiyalar

- **Python**
- **Django** — web framework
- **Django REST Framework** — API yaratish uchun
- **python-dotenv** — muhit o'zgaruvchilarini boshqarish

---

## O'rnatish

```bash
# 1. Reponi klonlash
git clone https://github.com/username/account-api.git
cd account-api

# 2. Virtual muhit yaratish
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Kutubxonalarni o'rnatish
pip install -r requirements.txt

# 4. .env faylini yaratish
cp .env.example .env
# .env faylga SECRET_KEY qiymatini kiriting

# 5. Migratsiyalarni bajarish
python manage.py migrate

# 6. Serverni ishga tushirish
python manage.py runserver
```

---

## API Endpointlari

| Method | URL | Tavsif |
|--------|-----|--------|
| POST | `/api/start/` | Telegram bot orqali yangi foydalanuvchi ro'yxatga olish |
| GET | `/api/accounts/` | Barcha foydalanuvchilar ro'yxati |

---

## Model haqida qisqacha

**Account** — Telegram foydalanuvchisi haqidagi ma'lumotlar:

| Field | Tavsif |
|-------|--------|
| `first_name` | Ism |
| `last_name` | Familiya |
| `image` | Profil rasmi |
| `phone_number` | Telefon raqami |
| `telegram_id` | Telegram ID (unikal) |
| `username` | Telegram username |
| `created_at` / `updated_at` | Yaratilgan/yangilangan vaqt |

---

## Muhit o'zgaruvchilari

`.env` fayl yaratib quyidagini sozlang:

```env
SECRET_KEY=
```

---

## Litsenziya

MIT License