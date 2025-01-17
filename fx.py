

# Function to sort tasks by priority, deadline, and estimated time
def sort_tasks(tasks):
    """
    Sorts tasks by an urgency score calculated from task priority, time remaining until the deadline, and estimated time.
    
    :param tasks: List of Task objects to sort
    :return: List of tasks sorted by urgency score (highest urgency first)
    """
    now = datetime.now()  # Current time for comparison

    # Helper function to calculate urgency score for each task
    def urgency_score(task):
        """
        Calculates urgency score for a given task.
        
        Formula: (priority / time_left) / estimated_time
        If task is overdue, assign it highest urgency.
        
        :param task: The task object to calculate urgency for
        :return: Urgency score (higher means more urgent)
        """
        time_left = (task.deadline - now).total_seconds() / 3600  # Time left in hours
        if time_left <= 0:
            return float('inf')  # If task is overdue, return highest urgency

        # Calculate urgency based on priority, time left, and estimated time
        return (task.priority / time_left) / task.estimated_time

    # Sort tasks by urgency score (highest first)
    return sorted(tasks, key=urgency_score, reverse=True)

# Example tasks with title, priority, deadline, and estimated time (in hours)
tasks = [
    Task("Finish report", priority=10, deadline=datetime.now() + timedelta(hours=5), estimated_time=2),
    Task("Prepare presentation", priority=7, deadline=datetime.now() + timedelta(hours=48), estimated_time=4),
    Task("Complete coding assignment", priority=8, deadline=datetime.now() + timedelta(hours=12), estimated_time=6),
    Task("Update project documentation", priority=6, deadline=datetime.now() + timedelta(hours=24), estimated_time=3)
]

# Sort and display the tasks in order of urgency
sorted_tasks = sort_tasks(tasks)
for task in sorted_tasks:
    print(task)


def process_data(input_data):
    """
    Processes input data by cleaning, transforming, and validating.
    """
    cleaned_data = [item.strip().lower() for item in input_data if item]
    transformed_data = [item.replace(" ", "_") for item in cleaned_data]
    
    # Validate data (example of a complex validation)
    if any(len(item) > 100 for item in transformed_data):
        raise ValueError("Some items exceed the allowed length")
    
    return transformed_data
