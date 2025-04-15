# Tron Wallet Service 🚀

Микросервис для получения информации о TRON-кошельке: **bandwidth**, **energy** и **TRX-баланс**. 

## 🔑 Регистрация API-ключа

1. Перейдите на [https://www.trongrid.io/](https://www.trongrid.io/)
2. Зарегистрируйтесь и создайте новый API Key
3. Создайте `.env` файл и сохраните ваш ключ:
```bash
TRON_API_KEY=your_api_key_here
```

## 🚀 Запуск проекта

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/yourusername/tron-wallet-service.git
```
### 2. Перейдите в дерикторию
```bash
cd tron-wallet-service
```
### 3. Создайте виртуальную среду 
```bash
python3 -m venv tron # или любое название вместо tron
```
### 4. Активируйте виртуальную среду
```bash
source tron/bin/activate 
```
### 5. Установите зависимости
```bash
pip install -r requirements.txt
```
### 6. Запустите сервер
```bash
uvicorn app.main:app --reload
```
---
## 📜 Документация API
После запуска сервера вы можете перейти в документацию API: 

http://127.0.0.1:8000/docs

Документация автоматически сгенерируется FastAPI и будет доступна для взаимодействия с API.
