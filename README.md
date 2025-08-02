# 📈 Stock Sale Capital Gains Calculator

This Python script calculates the capital gains tax and net profit (or loss) from selling shares of stock across **two separate sales**. It guides the user through the process of entering sale details, validates input against available shares, and outputs a summary of gains, tax, and final profit.

---

## 🧾 Features

- Handles **two rounds of stock sales**
- Validates that the user does not sell more shares than they own
- Calculates:
  - Total amount received from sales
  - Capital gains
  - Capital gains tax (15%)
  - Net profit after taxes

---

## 🛠 How It Works

The script assumes:
- You initially own **200 shares**
- Shares were purchased at **$30 per share**
- Capital gains tax rate is **15%**

You will be prompted to:
1. Enter how many shares to sell in the first sale
2. Enter the sale price per share
3. Enter how many of the remaining shares to sell in a second sale
4. Enter the second sale price per share

The script then outputs:
- Total cost basis
- Total received from sales
- Capital gains tax owed
- Final net profit

---

## ▶️ Example Usage

```bash
$ python stock_sale_calculator.py

 * First Stock Sale * 

You have 200 shares. How many would you like to sell?: 100
Enter sales price per share: 40

 * Second Stock Sale * 

You have 100 shares left. How many would you like to sell?: 100
Enter sales price per share: 35

Total Spent on Initial Stock Purchase: $6000.00  
Total Received from Sales: $7500.00  
Capital Gains Tax: $225.00  
Net Profit or Loss: $1275.00

