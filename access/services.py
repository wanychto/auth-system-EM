from access.models import Access_rules, User_role

def has_access(user, element, permission: str, check_all: bool = False) -> bool:
    if not user:
        return False

    if element.owner == user:
        return True

    roles = User_role.objects.filter(user=user).values_list("role", flat=True)

    if not roles:
        return False

    field_name = f"{permission}_all_permission" if check_all else f"{permission}_permission"

    return Access_rules.objects.filter(
        role__in=roles,
        element=element,
        **{field_name: True}
    ).exists()