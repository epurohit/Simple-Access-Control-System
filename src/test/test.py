from src.main.access_control_system import AccessControlSystem

acs = AccessControlSystem()

# Test Case 1: Default Deny
assert acs.check_access("u1", "/finance/q3/report.pdf", "READ") == False

# Test Case 2: Downward Inheritance
acs.add_permission("u1", "/finance", "READ", "ALLOW")
assert acs.check_access("u1", "/finance/q3/report.pdf", "READ") == True

# Test Case 3: Resource Specificity (Override inherited ALLOW with explicit DENY)
acs.add_permission("u1", "/finance/q3/report.pdf", "READ", "DENY")
assert acs.check_access("u1", "/finance/q3/report.pdf", "READ") == False
assert acs.check_access("u1", "/finance/q3/other_file.txt", "READ") == True

# Test Case 4: Independent Permissions (WRITE does not imply READ unless coded)
acs.add_permission("u2", "/eng", "WRITE", "ALLOW")
assert acs.check_access("u2", "/eng/deploy.sh", "WRITE") == True
assert acs.check_access("u2", "/eng/deploy.sh", "READ") == False

print("PASSED!")