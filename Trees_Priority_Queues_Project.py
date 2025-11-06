#Thomas Cubstead
#Trees_Priority_Queues_Project
#Triage_System
#11/6/25
#

import heapq

class TriageSystem:
    # Class level arrival counter shared across all instances
    _arrival_counter = 0
    
    def __init__(self):
        self._queue = []
    
    @classmethod
    def NextArrivalOrder(cls):
        current = cls._arrival_counter
        cls._arrival_counter += 1
        return current
    
    def AddPatient(self, name, severity):
        # Validation
        if not name or not isinstance(name, str) or name.strip() == "":
            raise ValueError("Patient name must be a nonempty string")
        
        if not isinstance(severity, int) or severity < 1 or severity > 5:
            raise ValueError("Severity must be an integer between 1 and 5")
        
        # Get arrival order for tie-breaking
        arrival_order = self.NextArrivalOrder()
        
        priority_entry = (-severity, arrival_order, name, severity)
        heapq.heappush(self._queue, priority_entry)
    
    def ProcessNext(self):
        if self.IsEmpty():
            return None
        
        # Pop the highest priority patient
        _, _, name, severity = heapq.heappop(self._queue)
        return (name, severity)
    
    def PeekNext(self):
        if self.IsEmpty():
            return None
        
        # Access the first element without removing it
        _, _, name, severity = self._queue[0]
        return (name, severity)
    
    def IsEmpty(self):
        return len(self._queue) == 0
    
    def Size(self):
        return len(self._queue)
    
    def Clear(self):
        self._queue = []


