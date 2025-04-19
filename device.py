import datetime

class IoTDevice:
    
    def __init__(self, device_id, device_type, ip_address=None, x=0, y=0):
        self.device_id = device_id
        self.device_type = device_type  
        self.ip_address = ip_address or "0.0.0.0"
        self.status = "enabled"         
        self.x = x                       
        self.y = y                       
        self.log = []                    

    def enable(self):
        self.status = "enabled"
        self._log_event("Enabled")

    def disable(self):
        self.status = "disabled"
        self._log_event("Disabled")

    def _log_event(self, message):
        
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.log.append(f"[{timestamp}] {message}")

    def get_log(self):
       
        return "\n".join(self.log)

    def __str__(self):
        return (f"[{self.device_id}] {self.device_type} "
                f"(IP: {self.ip_address}, Status: {self.status})")