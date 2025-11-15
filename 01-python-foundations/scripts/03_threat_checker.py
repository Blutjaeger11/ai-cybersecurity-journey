# if condition:
#     # runs if condition is true
# elif another_condition:
#     # runs if previous conditions were false
# else:
#     # runs if nothing above was true


# ip = "45.155.205.55"
# blocked_ips = ["45.155.205.55", "102.23.41.90"]

# if ip in blocked_ips:
#     print("🚨 Blocked IP detected!")
# else:
#     print("IP is safe.")


# failed_attempts = 7

# if failed_attempts > 10:
#     print("Lock account and notify SOC team.")
# elif failed_attempts > 5:
#     print("Alert: Multiple failed logins.")
# else:
#     print("Normal authentication behavior.")


malicious_urls = ["evil.com", "steal-data.net", "phish.me"]
url = input("Enter URL: ")    # user input is taken in the from of a STRING

if url in malicious_urls:
    print("⚠ Malicious URL detected!")
else:
    print("URL seems safe (for now)")
