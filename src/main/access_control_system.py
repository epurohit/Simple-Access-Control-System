from src.main.graph_node import GraphNode


class AccessControlSystem:
    def __init__(self):
        # Initialize your data structures here
        self.users = []
        self.root = GraphNode()

    def _split_path(self, path: str) -> list:
        return [p for p in path.split('/') if p]

    def add_permission(self, user_id: str, path: str, permission_type: str, access_type: str) -> None:
        """
        Grants or denies a specific permission to a user on a path.
        :param user_id: String identifier for the user (e.g., "u1")
        :param path: The file or directory path (e.g., "/finance/q3")
        :param permission_type: "READ" or "WRITE"
        :param access_type: "ALLOW" or "DENY"
        """
        # Check whether user id exists, if not default DENY
        if user_id not in self.users:
            self.users.append(user_id)

        parts = self._split_path(path)
        curr = self.root

        for part in parts:
            if part not in curr.children:
                curr.children[part] = GraphNode()
        
            curr = curr.children[part]

        if user_id not in curr.permissions:
            curr.permissions[user_id] = {}

        curr.permissions[user_id][permission_type] = access_type
            
        

    def check_access(self, user_id: str, path: str, permission_type: str) -> bool:
        """
        Evaluates if the user has the requested permission on the path.
        :param user_id: String identifier for the user
        :param path: The target file or directory path
        :param permission_type: "READ" or "WRITE"
        :return: True if access is allowed, False otherwise
        """
        if user_id not in self.users:
            return False

        parts = self._split_path(path)
        curr = self.root

        current_permission = "DENY"

        # Root level perms
        if user_id in curr.permissions and permission_type in curr.permissions[user_id]:
            current_permission = curr.permissions[user_id][permission_type]

        # Iterate graph till last seen
        for part in parts:
            if part not in curr.children:
                break

            curr = curr.children[part]

            if user_id in curr.permissions and permission_type in curr.permissions[user_id]:
                current_permission = curr.permissions[user_id][permission_type]

        return current_permission == "ALLOW"

