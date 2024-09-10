from datetime import datetime, timedelta

# Task structure
class Task:
    def __init__(self, title, priority, deadline, estimated_time):
        self.title = title
        self.priority = priority
        self.deadline = deadline
        self.estimated_time = estimated_time
    
    def __repr__(self):
        return f"{self.title} (Priority: {self.priority}, Deadline: {self.deadline}, Estimated Time: {self.estimated_time} hours)"

# Priority sorting function
def sort_tasks(tasks):
    now = datetime.now()

    # Define a function to calculate urgency score
    def urgency_score(task):
        time_left = (task.deadline - now).total_seconds() / 3600  # Time left in hours
        if time_left <= 0:
            return float('inf')  # Highest urgency if overdue

        # Formula: priority * (1 / time_left) * (1 / estimated_time)
        return (task.priority / time_left) / task.estimated_time  # Factor in time left and estimated time

    # Sort tasks based on urgency score (highest score first)
    return sorted(tasks, key=urgency_score, reverse=True)

# Example tasks
tasks = [
    Task("Finish report", priority=10, deadline=datetime.now() + timedelta(hours=5), estimated_time=2),
    Task("Prepare presentation", priority=7, deadline=datetime.now() + timedelta(hours=48), estimated_time=4),
    Task("Complete coding assignment", priority=8, deadline=datetime.now() + timedelta(hours=12), estimated_time=6),
    Task("Update project documentation", priority=6, deadline=datetime.now() + timedelta(hours=24), estimated_time=3)
]

# Sort tasks and display the order
sorted_tasks = sort_tasks(tasks)
for task in sorted_tasks:
    print(task)
