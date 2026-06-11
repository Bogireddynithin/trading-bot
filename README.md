# Trading Bot – Binance Futures Testnet

##  Overview

This project is a simplified Python-based trading bot that interacts with the Binance Futures Testnet. It allows users to place MARKET and LIMIT orders via a Command Line Interface (CLI) with proper validation, logging, and error handling.

---

##  Features

* Place **MARKET** and **LIMIT** orders
* Supports **BUY** and **SELL**
* CLI-based input using arguments
* Input validation for all fields
* Logging of requests, responses, and errors
* Fallback mock response if API fails
* Clean modular structure

---

##  Project Structure

```
trading_bot/
 ├── bot/
 │   ├── client.py
 │   ├── orders.py
 │   ├── validators.py
 │   ├── logging_config.py
 │   ├── cli.py
 │   └── __init__.py
 ├── .env
 ├── requirements.txt
 ├── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone / Download Project

```
git clone <your-repo-link>
cd trading_bot
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Add API Keys

Create `.env` file:

```
API_KEY=your_api_key
API_SECRET=your_secret_key
BASE_URL=https://testnet.binancefuture.com
```

---

## ▶ How to Run

### MARKET Order

```
python bot/cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```
python bot/cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 30000
```

---

##  Sample Output

```
--- Order Request ---
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

--- Order Response ---
Order ID: 99999
Status: FILLED
Executed Quantity: 0.001
Average Price: market_price

 Order executed successfully!
```

---

##  Logging

Logs are stored in:

```
trading_bot.log
```

Example:

```
INFO - Placing MARKET order
ERROR - API Secret required
```

---

##  Notes

* Binance Testnet may be restricted in some regions
* In such cases, **mock responses are used** to simulate order execution
* Real API structure is still maintained

---

##  Design Approach

* Modular architecture (client, orders, validators, CLI)
* Separation of concerns
* Robust error handling
* Scalable structure for future enhancements

---

##  Conclusion

This project demonstrates a clean, production-like implementation of a trading bot with proper structure, validation, logging, and CLI interaction.

---
