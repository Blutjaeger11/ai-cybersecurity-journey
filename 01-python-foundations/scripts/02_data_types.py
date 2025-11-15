# Python Data Types

# String
log_source = "Firewall"

# Integer
failed_logins = 7

# Float
cpu_usage = 13.7

# Boolean
is_threat_detected = False

# List (multiple values; mutable)
attack_ips = ["192.168.1.10", "10.0.0.5", "203.0.113.50"]

# Tuple (fixed list; items cannot be changed)
ports_scanned = (22, 80, 443)

# Dictionary (key-value pairs)
alert = {
    "type": "Brute Force",
    "severity": "High",
    "source_ip": "203.0.113.50"
}

# Printing values
print("Log Source:", log_source)
print("Failed logins:", failed_logins)
print("CPU Usage:", cpu_usage)
print("Threat detected:", is_threat_detected)
print("Attack IPs:", attack_ips)
print("Ports Scanned:", ports_scanned)
print("Alert details:", alert)