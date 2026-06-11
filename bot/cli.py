import argparse
from orders import OrderManager
from validators import Validator


def main():
    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, help="Order quantity")
    parser.add_argument("--price", help="Price (required for LIMIT orders)")

    args = parser.parse_args()

    try:
        
        symbol = Validator.validate_symbol(args.symbol)
        side = Validator.validate_side(args.side)
        order_type = Validator.validate_order_type(args.type)
        quantity = Validator.validate_quantity(args.quantity)

        price = None
        if order_type == "LIMIT":
            if not args.price:
                raise ValueError("Price is required for LIMIT orders")
            price = Validator.validate_price(args.price)

        order = OrderManager()
        result = order.place_order(symbol, side, order_type, quantity, price)

        print("\n✅ Order executed successfully!")
        print(result)

    except Exception as e:
        print(" Error:", e)


if __name__ == "__main__":
    main()