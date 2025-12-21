# menu_item class
class menu_item:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price


# course_category class
class course_category:
    def __init__(self, category_id, name):
        self.category_id = category_id
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)


# menu class
class menu:
    def __init__(self, menu_id, name):
        self.menu_id = menu_id
        self.name = name
        self.categories = []

    def add_category(self, category):
        self.categories.append(category)


# special_menu class (inherits menu)
class special_menu(menu):
    def __init__(self, menu_id, name):
        super().__init__(menu_id, name)
        self.discount_percentage = 30

    def apply_discount(self, price):
        return price * (1 - self.discount_percentage / 100)


# branch class
class branch:
    def __init__(self, branch_id, location):
        self.branch_id = branch_id
        self.location = location


# restaurant class
class restaurant:
    def __init__(self, name):
        self.name = name
        self.branches = []
        self.menus = []

    def add_branch(self, branch):
        self.branches.append(branch)

    def add_menu(self, menu):
        self.menus.append(menu)

    # 1. total number of menu items
    def list_total_menu_items(self):
        count = 0
        for menu in self.menus:
            for category in menu.categories:
                count += len(category.items)
        return count

    # 2. list menu items for a particular course category
    def list_items_by_category(self, category_name):
        items = []
        for menu in self.menus:
            for category in menu.categories:
                if category.name == category_name:
                    items.extend(category.items)
        return items

    # 3. list all special discount menu items
    def list_special_menu_items(self):
        items = []
        for menu in self.menus:
            if isinstance(menu, special_menu):
                for category in menu.categories:
                    items.extend(category.items)
        return items
