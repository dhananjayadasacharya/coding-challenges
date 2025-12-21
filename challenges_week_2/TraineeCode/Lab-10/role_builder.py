class RoleBuilder:
    """
    Private data member
    """
    ROLES = ["UNDEFINED", "DEVELOPER", "TEST_ENGINEER", "SR_DEVELOPER", "DESIGNER"]

    """
    Method to get role description for a given role id
    """
    @staticmethod
    def get_role_description(role_id):
        try:
            rid = int(role_id)
        except (TypeError, ValueError):
            return RoleBuilder.ROLES[0]
        if 1 <= rid < len(RoleBuilder.ROLES):
            return RoleBuilder.ROLES[rid]
        return RoleBuilder.ROLES[0]
