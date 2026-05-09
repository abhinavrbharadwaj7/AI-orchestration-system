from datetime import datetime


LOG_TIME_FORMAT = "%H:%M:%S"


def add_log(state, message: str):
    timestamp = datetime.now().strftime(LOG_TIME_FORMAT)
    log_entry = f"[{timestamp}] {message}"
    state.logs.append(log_entry)
    print(log_entry)
    return state

