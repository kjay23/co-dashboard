from flask_appbuilder.security.manager import SecurityManager

class MySecurityManager(SecurityManager):
    def __init__(self, appbuilder):
        super().__init__(appbuilder)
        # Remove all menu links related to security
        self.appbuilder.menu._menu = [
            item for item in self.appbuilder.menu._menu
            if item.name not in ['Security']
        ]

