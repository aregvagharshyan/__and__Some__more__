import uuid

class BillingSystem:
    global_tax_rate = 0.0

    def __init__(self):
        self.clients = {}
        self.invoices = {}

    def add_client(self, name, tax_rate = None):
        client_id = uuid.uuid4()
        self.clients[client_id] = {'name': name,
                                   'tax_rate': tax_rate}
        return f'{name} added with {client_id} id!'

    @staticmethod
    def calculate_taxed_amount(amount, tax_rate):
        return amount + (amount * tax_rate)

    def create_invoice(self, client_id, amount):
        if client_id not in self.clients:
            return f'Client not found!'
        client_tax_rate = self.clients[client_id].get("tax_rate")
        tax_rate = client_tax_rate if client_tax_rate is not None else BillingSystem.global_tax_rate
        final_amount = self.calculate_taxed_amount(amount, tax_rate)
        invoice_id = uuid.uuid4()
        self.invoices[invoice_id] = {'client_id': client_id,
                                     'amount': amount,
                                     'final_amount': final_amount}
        return f'Invoice id{invoice_id}!'

    def get_client_invoices(self, client_id):
        list_invoices = []
        for invoice_id, real_client_id in self.invoices.items():
            if client_id == real_client_id['client_id']:
                list_invoices.append(invoice_id)
        if list_invoices:
            return f'List of {client_id} invoice: {list_invoices}.'
        return f'Not invoices!'

    @classmethod
    def set_global_tax_rate(cls, rate):
        if not (0.0 <= rate <= 1.0):
            raise ValueError("Tax rate must be between 0.0 and 1.0 (0% to 100%)")
        cls.global_tax_rate = rate

    @classmethod
    def get_global_tax_rate(cls):
        return cls.global_tax_rate

billing = BillingSystem()
client_id1 = billing.add_client("Acme Corp", tax_rate=0.15)
client_id2 = billing.add_client("Beta LLC")
BillingSystem.set_global_tax_rate(0.20)
invoice_id1 = billing.create_invoice(client_id1, 1000)
invoice_id2 = billing.create_invoice(client_id2, 500)
print(billing.get_client_invoices(client_id1))
print(billing.get_client_invoices(client_id2))
print(BillingSystem.get_global_tax_rate())
print(BillingSystem.calculate_taxed_amount(200, 0.18))

#

import datetime

class SubscriptionSystem:
    global_tax_rate = 0.0

    def __init__(self):
        self.clients = {}
        self.plans = {}
        self.subscriptions = {}
        self.invoices = {}

    def add_client(self, name, email):
        client_id = uuid.uuid4()
        self.clients[client_id] = {'name': name, 'email': email}
        return client_id

    def add_plan(self, name, monthly_price):
        plan_id = uuid.uuid4()
        self.plans[plan_id] = {'name': name, 'monthly_price': monthly_price}
        return plan_id

    def subscribe(self, client_id, plan_id):
        if client_id not in self.clients or plan_id not in self.plans:
            return 'Invalid IDs'
        subscription_id = uuid.uuid4()
        start_date = datetime.date.today()
        self.subscriptions[subscription_id] = {
            'client_id': client_id,
            'plan_id': plan_id,
            'status': 'active',
            'start_date': start_date
        }
        return subscription_id

    def cancel_subscription(self, subscription_id):
        if subscription_id not in self.subscriptions:
            return 'Invalid subscription ID'
        self.subscriptions[subscription_id]['status'] = 'canceled'
        return 'Subscription canceled'

    def generate_monthly_invoice(self, subscription_id, billing_month):
        if subscription_id not in self.subscriptions:
            return 'Invalid subscription ID'
        invoice_id = uuid.uuid4()
        plan_id = self.subscriptions[subscription_id]['plan_id']
        monthly_price = self.plans[plan_id]['monthly_price']
        amount = self.calculate_taxed_amount(monthly_price, SubscriptionSystem.global_tax_rate)
        self.invoices[invoice_id] = {
            'subscription_id': subscription_id,
            'billing_month': billing_month,
            'amount': monthly_price,
            'final_amount': amount,
            'paid': False
        }
        return invoice_id

    def pay_invoice(self, invoice_id):
        if invoice_id not in self.invoices:
            return 'Invalid invoice ID'
        self.invoices[invoice_id]['paid'] = True
        return 'Invoice paid'

    def get_client_invoices(self, client_id):
        subscription_ids = [
            sid for sid, data in self.subscriptions.items()
            if data['client_id'] == client_id
        ]
        matched_invoices = {
            iid: data for iid, data in self.invoices.items()
            if data['subscription_id'] in subscription_ids
        }
        return matched_invoices

    def get_subscription_status(self, subscription_id):
        return self.subscriptions.get(subscription_id, {}).get('status', 'Invalid ID')

    @classmethod
    def set_global_tax_rate(cls, rate):
        if not (0.0 <= rate <= 1.0):
            raise ValueError("Tax rate must be between 0.0 and 1.0")
        cls.global_tax_rate = rate

    @staticmethod
    def calculate_taxed_amount(amount, tax_rate):
        return amount + (amount * tax_rate)

# Example usage
system = SubscriptionSystem()
client_id = system.add_client("Arman", "arman@mail.com")
plan_id = system.add_plan("Pro Plan", 29.99)
sub_id = system.subscribe(client_id, plan_id)
system.set_global_tax_rate(0.2)
invoice_id = system.generate_monthly_invoice(sub_id, "2025-06")
system.pay_invoice(invoice_id)
print(system.get_client_invoices(client_id))





