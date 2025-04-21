import threading
import time
# Initialize chopsticks (semaphores)
chopstick = [threading.Semaphore(1) for _ in range(5)]

def philosopher(id):
    left_chopstick = id
    right_chopstick = (id + 1) % 5

    while True:
# Pick up chopsticks
        with chopstick[left_chopstick]:
            with chopstick[right_chopstick]:
                print(f"Philosopher {id} is eating")
                time.sleep(2) # Simulate eating

# Think
print(f"Philosopher {id} is thinking")
time.sleep(2)

if __name__ == "__main__":
    philosophers = []
# Create threads for each philosopher
for i in range(5):
    thread = threading.Thread(target=philosopher, args=(i,))
    philosophers.append(thread)
    
# Start threads
for thread in philosophers:
    thread.start()
    
# Wait for all threads to finish
for thread in philosophers:
    thread.join()