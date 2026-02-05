from config import password_md5_file, meal_time_file
from datetime import datetime
import bcrypt

def get_hour():
    """Return the current hour in HH:MM format."""
    
    return datetime.now().strftime("%H:%M:%S")

def hash_password(password):
    """Return the MD5 hash of the given text."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def comprobe_password(plain_password, hashed_password):
    """Check if the plain password matches the hashed password."""
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def get_stored_password():
    """Read and return the stored MD5 hashed password from the given file."""
    try:
        with open(password_md5_file, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def get_meal_time():
    """Read and return the meal time from the given file."""
    try:
        with open(meal_time_file, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def get_meal_time_array():
    """Read and return the meal times as a list of datetime.time from the given file."""
    try:
        with open(meal_time_file, 'r') as f:
            times = []
            for line in f:
                line = line.strip()
                if line:
                    t = datetime.strptime(line, "%H:%M:%S").time()
                    times.append(t)
            return times
    except FileNotFoundError:
        return []

def format_time(time_text):
    """Check if the time string is in HH:MM:SS format."""
    time_text = [i.replace(' ', '') for i in time_text.strip().splitlines()]
    try:
        for i in time_text:
            hours, minutes, seconds = map(int, i.split(':'))
            if not (0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60):
                return [], False
        return time_text, True
    except ValueError:
        return [], False