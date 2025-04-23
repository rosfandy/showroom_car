
## 1. Clone Repository
  ```bash
  git clone https://github.com/rosfandy/showroom_car
  ```

## 2. Masuk ke Direktori Proyek
  ```bash
  cd showroom_car
  ```

## 3. Buat dan Aktifkan Virtual Environment
- **Untuk Linux/MacOS:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
- **Untuk Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

## 4. Install Dependensi
  ```bash
  pip install -r requirements.txt
  ```

## 5. Lakukan Migrasi Database
  ```bash
  python manage.py migrate
  ```

## 9. Jalankan Server
  ```bash
  python manage.py runserver
  ```
Akses aplikasi di `http://127.0.0.1:8000` di browser.