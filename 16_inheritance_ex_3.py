import uuid

class Entity:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.name = name
class Client(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.project_ids = []
class Project(Entity):
    def __init__(self, name, client_id, rate):
        super().__init__(name)
        self.client_id = client_id
        self.hours = 0.0
        self.rate = rate
class BillingSystem:
    def __init__(self):
        self.clients = {}
        self.projects = {}
    def add_client(self, name):
        client = Client(name)
        self.clients[client.id] = client
        return client.id
    def create_project(self, client_id, name, rate):
        project = Project(name, client_id, rate)
        self.projects[project.id] = project
        self.clients[client_id].project_ids.append(project.id)
        return project.id
    def log_hours(self, project_id, hours):
        if project_id not in self.projects:
            return 'Invalid project ID'
        self.projects[project_id].hours += hours
        return 'Hours logged successfully'
    def generate_invoice(self, client_id):
        if client_id not in self.clients:
            return f'Wrong id!'
        client = self.clients[client_id]
        total = 0.0
        invoice_lines = [f"Invoice for client: {client.name}\n"]
        for pid in client.project_ids:
            project = self.projects[pid]
            subtotal = project.hours * project.rate
            total += subtotal
            invoice_lines.append(
                f"- {project.name}: {project.hours:.2f} hours × ${project.rate:.2f} = ${subtotal:.2f}"
            )
        invoice_lines.append(f"\nTotal due: ${total:.2f}")
        return "\n".join(invoice_lines)
billing = BillingSystem()
client_id = billing.add_client("Acme Corp")
project_id = billing.create_project(client_id, "Website Redesign", 75.0)
billing.log_hours(project_id, 10)
billing.log_hours(project_id, 5.5)
print(billing.generate_invoice(client_id))

