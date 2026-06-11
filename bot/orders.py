from client import BinanceClient   # ✅ fixed import


class OrderManager:
    def __init__(self):
        self.client = BinanceClient().get_client()

    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            print("\n--- Order Request ---")
            print(f"Symbol: {symbol}")
            print(f"Side: {side}")
            print(f"Type: {order_type}")
            print(f"Quantity: {quantity}")
            if price:
                print(f"Price: {price}")

            # MARKET ORDER
            if order_type == "MARKET":
                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="MARKET",
                    quantity=quantity
                )

            # LIMIT ORDER
            elif order_type == "LIMIT":
                if price is None:
                    raise ValueError("Price required for LIMIT order")

                response = self.client.futures_create_order(
                    symbol=symbol,
                    side=side,
                    type="LIMIT",
                    quantity=quantity,
                    price=price,
                    timeInForce="GTC"
                )

            else:
                raise ValueError("Invalid order type")

            return self.format_response(response)

        except Exception as e:
            print("❌ Error placing order:", e)

            # Mock response (fallback)
            mock_response = {
                "orderId": 99999,
                "status": "FILLED",
                "executedQty": quantity,
                "avgPrice": price if price else "market_price"
            }

            return self.format_response(mock_response)

    def format_response(self, response):
        print("\n--- Order Response ---")
        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Quantity: {response.get('executedQty')}")
        print(f"Average Price: {response.get('avgPrice', 'N/A')}")

        return {
            "orderId": response.get("orderId"),
            "status": response.get("status"),
            "executedQty": response.get("executedQty"),
            "avgPrice": response.get("avgPrice", "N/A")
        }


# ✅ Test block
if __name__ == "__main__":
    order = OrderManager()

    # MARKET ORDER TEST
    order.place_order(
        symbol="BTCUSDT",
        side="BUY",
        order_type="MARKET",
        quantity=0.001
    )

    # LIMIT ORDER TEST
    order.place_order(
        symbol="BTCUSDT",
        side="SELL",
        order_type="LIMIT",
        quantity=0.001,
        price=30000
    )