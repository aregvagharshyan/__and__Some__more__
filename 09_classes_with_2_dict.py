# 1. Online Course Platform
#
# Objective:
#
# Design a class-based system that simulates an online learning platform where instructors can create courses, and students can enroll and complete them.
#
# Structure:
# 	•	CoursePlatform class manages users, courses, and enrollments.
# 	•	Store:
# 	•	users: {user_id: {"name": ..., "role": "student"/"instructor"}}
# 	•	courses: {course_id: {"title": ..., "instructor_id": ..., "students": set()}}
#
# Methods to implement:
# 	•	add_user(name, role): Adds a user with auto-generated ID.
# 	•	create_course(title, instructor_id): Creates a course.
# 	•	enroll_student(course_id, student_id): Enrolls a student.
# 	•	get_course_info(course_id): Shows course, instructor, and enrolled students.
# 	•	get_user_courses(user_id): Lists courses the user is enrolled in or teaches.

import uuid

class CoursePlatform:
    def __init__(self):
        self.users = {}
        self.courses = {}

    def add_user(self, name, role):
        user_id = uuid.uuid4()
        self.users[user_id] = {'name': name, 'role': role}
        return user_id

    def create_course(self, title, instructor_id):
        if instructor_id in self.users and self.users[instructor_id]['role'] == 'instructor':
            course_id = uuid.uuid4()
            self.courses[course_id] = {'title': title, 'instructor_id': instructor_id, 'students':set()}
            return course_id
        return f'Wrong instructor_id'

    def enroll_student(self, course_id, student_id):
        if course_id in self.courses and student_id in self.users and self.users[student_id]['role'] == 'student':
            self.courses[course_id]['students'].add(student_id)
            return f'Student with{student_id} id enrolled in a course with {course_id} id!'
        return f'Wrong id\'s!'

    def get_course_info(self, course_id):
        if course_id in self.courses:
            course = self.courses[course_id]
            instructor_name = self.users[course["instructor_id"]]["name"]
            student_names = [self.users[s]["name"] for s in course["students"]]
            return {
                "title": course["title"],
                "instructor": instructor_name,
                "students": student_names
            }
        return 'Course not found!'

    def get_user_courses(self, user_id):
        if user_id not in self.users:
            return 'User not found!'
        role = self.users[user_id]['role']
        courses = []
        for cid, course in self.courses.items():
            if role == 'instructor' and course['instructor_id'] == user_id:
                courses.append((cid, course['title'], 'teaching'))
            elif role =='student' and user_id in course['students']:
                courses.append((cid, course['title'], 'enrolled'))
        return courses if courses else 'Not enough course'

platform = CoursePlatform()
instructor_id = platform.add_user("Emma", "instructor")
student_id = platform.add_user("Liam", "student")
course_id = platform.create_course("Data Science", instructor_id)
platform.enroll_student(course_id, student_id)
print(platform.get_course_info(course_id))
print(platform.get_user_courses(student_id))

# 2. Billing System for Freelancers
#
# Objective:
#
# Create a system to track freelance projects, time worked, and billing clients.
#
# Structure:
# 	•	BillingSystem stores clients and projects.
# 	•	Projects include logged time and rates.
#
# Data:
# 	•	clients: {client_id: {"name": str, "projects": list of project_ids}}
# 	•	projects: {project_id: {"name": str, "client_id": ..., "hours": float, "rate": float}}
#
# Methods to implement:
# 	•	add_client(name)
# 	•	create_project(client_id, project_name, rate)
# 	•	log_hours(project_id, hours)
# 	•	generate_invoice(client_id) → Returns a breakdown of projects and total bill.

class BillingSystem:
    def __init__(self):
        self.clients = {}
        self.projects = {}

    def add_client(self, name):
         client_id = uuid.uuid4()
         self.clients[client_id] = {'name': name, 'projects': []}
         return f'{name} added with {client_id} id!'

    def create_project(self, client_id, project_name, rate):
        if client_id in self.clients:
            project_id = uuid.uuid4()
            self.projects[project_id] = {'name': project_name, 'client_id': client_id, 'hours': 0.0, 'rate': rate}
            self.clients[client_id].append(project_id)
            return f'{project_name} was created with {project_id} id!'
        return f'Invalid client id!'

    def log_hours(self, project_id, hours):
        if project_id in self.projects:
            self.projects[project_id]['hours'] += hours
            return f'+ {hours} to {project_id} project!'
        return f'Invalid project id!'

    def generate_invoice(self, client_id):
        if client_id not in self.clients:
            return "Client not found."
        total = 0.0
        invoice = []
        for project_id in self.clients[client_id]["projects"]:
            project = self.projects[project_id]
            amount = project["hours"] * project["rate"]
            total += amount
            invoice.append({
                "project_name": project["name"],
                "hours": project["hours"],
                "rate": project["rate"],
                "amount": amount
            })
        return {
            "client_name": self.clients[client_id]["name"],
            "projects": invoice,
            "total_due": total
        }
billing = BillingSystem()
client_id = billing.add_client("Acme Inc.")
project_id = billing.create_project(client_id, "Website Redesign", 75.0)
billing.log_hours(project_id, 5)
billing.log_hours(project_id, 3.5)
print(billing.generate_invoice(client_id))

# 3. Multiplayer Game Lobby System
#
# Objective:
#
# Build a system for managing multiplayer game lobbies, player joining/leaving, and matchmaking.
#
# Structure:
# 	•	GameLobbySystem class.
# 	•	Store:
# 	•	players: {player_id: {"name": ..., "lobby": None or lobby_id}}
# 	•	lobbies: {lobby_id: {"players": set(player_ids), "status": "waiting"/"in-game"}}
#
# Methods to implement:
# 	•	add_player(name)
# 	•	create_lobby()
# 	•	join_lobby(player_id, lobby_id)
# 	•	leave_lobby(player_id)
# 	•	start_game(lobby_id) → Sets status to "in-game" if enough players (e.g., 2+)

class GameLobbySystem:
    def __init__(self):
        self.players = {}
        self.lobbies = {}

    def add_player(self, name):
        player_id = uuid.uuid4()
        self.players[player_id] = {'name': name, 'lobby': None}
        return f'{name} is player with {player_id}'

    def create_lobby(self):
        lobby_id = uuid.uuid4()
        self.lobbies[lobby_id] = {"players": set(), "status": "waiting"}
        return lobby_id

    def join_lobby(self, player_id, lobby_id):
        if player_id in self.players and lobby_id in self.lobbies:
            self.lobbies[lobby_id]["players"].add(player_id)
            self.lobbies['status'] = 'in-game'
            self.players[player_id]['lobby'] = lobby_id
            return f'Player with {player_id} id added to lobby with {lobby_id}!'
        return 'Invalid player id or lobby id!'

    def leave_lobby(self, player_id):
        if player_id in self.players:
            self.players[player_id]['lobby'] = None
            left_lobby = False
            for lobby in self.lobbies.values():
                if player_id in lobby['players']:
                    lobby['players'].discard(player_id)
                    left_lobby = True
                    if len(lobby['players']) < 2:
                        lobby['status'] = 'waiting'
            if left_lobby:
                return f"Player {player_id} has left the lobby."
            else:
                return f"Player {player_id} was not in any lobby."
        return f"Player {player_id} does not exist."

    def start_game(self, lobby_id):
        if lobby_id in self.lobbies:
            if len(self.lobbies[lobby_id]['players']) >= 2:
                self.lobbies[lobby_id]['status'] = 'in-game'
                return f"Game started in lobby {lobby_id}!"
            return f"Not enough players to start the game in lobby {lobby_id}."
        return "Invalid lobby ID!"

game = GameLobbySystem()
p1 = game.add_player("Neo")
p2 = game.add_player("Trinity")
lobby_id = game.create_lobby()
game.join_lobby(p1, lobby_id)
game.join_lobby(p2, lobby_id)
print(game.start_game(lobby_id))

