from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from ui.backend.User import User 
from Admin-login import AdminLoginScreen
admin = AdminLoginScreen().authenticate(AdminLoginScreen())
admin_user = admin if admin else User("admin", "adminpass", "admin")

users = admin_user.getAllUsers()

class UserTable(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 4
        self.refresh_table()

    def refresh_table(self):
        self.clear_widgets()
        # Table headers
        self.add_widget(Label(text="ID", bold=True))
        self.add_widget(Label(text="Name", bold=True))
        self.add_widget(Label(text="Email", bold=True))
        self.add_widget(Label(text="Actions", bold=True))
        # Table rows
        for user in users:
            self.add_widget(Label(text=str(user["id"])))
            self.add_widget(Label(text=user["name"]))
            self.add_widget(Label(text=user["email"]))
            actions = BoxLayout(orientation='horizontal', size_hint_x=None, width=150)
            edit_btn = Button(text="Edit", size_hint_x=None, width=70)
            edit_btn.bind(on_release=lambda btn, u=user: self.edit_user(u))
            del_btn = Button(text="Delete", size_hint_x=None, width=70)
            del_btn.bind(on_release=lambda btn, u=user: self.delete_user(u))
            actions.add_widget(edit_btn)
            actions.add_widget(del_btn)
            self.add_widget(actions)

    def edit_user(self, user):
        content = BoxLayout(orientation='vertical')
        name_input = TextInput(text=user["name"])
        email_input = TextInput(text=user["email"])
        save_btn = Button(text="Save")
        cancel_btn = Button(text="Cancel")
        btns = BoxLayout(size_hint_y=None, height=40)
        btns.add_widget(save_btn)
        btns.add_widget(cancel_btn)
        content.add_widget(Label(text="Edit User"))
        content.add_widget(Label(text="Name:"))
        content.add_widget(name_input)
        content.add_widget(Label(text="Email:"))
        content.add_widget(email_input)
        content.add_widget(btns)
        popup = Popup(title="Edit User", content=content, size_hint=(0.5, 0.5))
        save_btn.bind(on_release=lambda btn: self.save_user(user, name_input.text, email_input.text, popup))
        cancel_btn.bind(on_release=popup.dismiss)
        popup.open()

    def save_user(self, user, name, email, popup):
        user["name"] = name
        user["email"] = email
        popup.dismiss()
        self.refresh_table()

    def delete_user(self, user):
        users.remove(user)
        self.refresh_table()

class ManageUsersApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        root.add_widget(Label(text="Manage Users", font_size=24, size_hint_y=None, height=40))
        self.table = UserTable()
        root.add_widget(self.table)
        return root

if __name__ == "__main__":
    ManageUsersApp().run()