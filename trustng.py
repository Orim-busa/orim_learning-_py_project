class Account:
    def __init__(self, name, tier, age_months, transactions, fraud_flags, number):
        self.name = name
        self.tier = tier
        self.age_months = age_months
        self.transactions = transactions
        self.fraud_flags = fraud_flags
        self.number = number

    def show_passport(self):
        print(f"Name: {self.name}")
        print(f"Tier: {self.tier}")
        print(f"Age (months): {self.age_months}")
        print(f"Transactions: {self.transactions}")
        print(f"Fraud Flags: {self.fraud_flags}")


class Transaction:
    def __init__(self, buyer, seller, amount, requires_delivery):
        self.buyer = buyer
        self.seller = seller
        self.amount = amount
        self.requires_delivery = requires_delivery
        self.status = "idle"
        self.courier_confirmed = False
        self.pin_confirmed = False
        self.correct_pin = "4821"


    def pay(self):
        self.status = "held"
        print(f"₦{self.amount} paid into escrow. status: {self.status}")

    def confirm_courier(self):
        self.courier_confirmed = True
        print("courier checked_in confirm.")

    def confirm_pin(self, entered_pin):

        if entered_pin == self.correct_pin:
            self.pin_confirmed = True
            print("pin confirmed.")
        else:
            print("incorrect pin.")

    def check_release(self):
        if self.courier_confirmed and self.pin_confirmed:
            self.status = "released"
            self.seller.transactions += 1
            print(f"both profs confirmed. ₦{self.amount} released to {self.seller.name}.")
        else:
            print("not all proofs are in yet - money stays held.")

    def flag_fraud(self, reason):
        print(f"case opened against {self.seller.name} :{reason}.")

    def resolve_case(self, confirmed):
        if confirmed:
            self.seller.fraud_flags += 1
            print(f"confirmed. {self.seller.name}'s fraud_flags:{self.seller.fraud_flags} ")
        else:
            print(f"Dissmissed. {self.seller.name}'s record is unaffected.")
    
buyer = Account("orim busa", "gold", 24, 150, 0, "07068718891")
seller = Account("paul osowo", "gold", 12, 150, 0, "08148430029")
buyer.show_passport()
seller.show_passport()

deal = Transaction(buyer, seller, 45000, True)



print("TRUSTNG bot: hi send me a seller's number to check their Trust record. eg: check 08012345678")



while True:
    message = input("you: ")
    lower = message.lower()

    if lower.startswith("check"):
        number = message[5:].strip()
        if number == seller.number:
            seller.show_passport()
        elif number == buyer.number:
            buyer.show_passport()
        else:
            print("TrustNG bot: no trust record found for that number. this person is not registerd with TrustNG. yet")
    elif lower.startswith("pay"):
        deal.pay()
    elif lower == "courier arrived":
        deal.confirm_courier()
    elif message.isdigit() and len(message) == 4:
        deal.confirm_pin(message)
        deal.check_release()
    elif lower.startswith("flag"):
        reason = message[4:].strip()
        deal.flag_fraud(reason)
    elif lower == "confirm fraud":
        deal.resolve_case(True)
    elif lower == "dismiss":
        deal.resolve_case(False)
    elif lower in ("quit","exit"):
        print("TRUSTNG bot: Goodbye!")
        break
    else:
        print("TRUSTNG bot: Sorry, I didn't understand that.")

    
