class Validator:

    @staticmethod
    def validate_symbol(symbol):
        if not symbol or not isinstance(symbol, str):
            raise ValueError("Invalid symbol")
        return symbol.upper()

    @staticmethod
    def validate_side(side):
        side = side.upper()
        if side not in ["BUY", "SELL"]:
            raise ValueError("Side must be BUY or SELL")
        return side

    @staticmethod
    def validate_order_type(order_type):
        order_type = order_type.upper()
        if order_type not in ["MARKET", "LIMIT"]:
            raise ValueError("Order type must be MARKET or LIMIT")
        return order_type

    @staticmethod
    def validate_quantity(quantity):
        try:
            qty = float(quantity)
            if qty <= 0:
                raise ValueError
            return qty
        except:
            raise ValueError("Quantity must be a positive number")

    @staticmethod
    def validate_price(price):
        try:
            price = float(price)
            if price <= 0:
                raise ValueError
            return price
        except:
            raise ValueError("Price must be a positive number")