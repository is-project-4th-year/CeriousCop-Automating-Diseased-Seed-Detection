from pymongo import MongoClient
import random

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role
        self.client = MongoClient('mongodb://localhost:27017/')
        self.db = self.client['user_database']
        self.collection = self.db['users']

    def get_username(self):
        return self.username

    def get_role(self):
        return self.role

    def login(self, username, password):
        isLoggedIn = False

        user = self.collection.find_one({"username": username, "password": password})
        if user:
            self.username = user['username']
            self.role = user['role']
            self.password = user['password']
            isLoggedIn = True
        return isLoggedIn

    def signup(self, username, password, role='user'):
        isSignedUp = False

        if not self.collection.find_one({"username": username}):
            self.collection.insert_one({
                "username": username,
                "password": password,
                "role": role
            })
            isSignedUp = True
        return isSignedUp

    def change_password(self, username, old_password, new_password):
        isChanged = False

        user = self.collection.find_one({"username": username, "password": old_password})
        if user:
            self.collection.update_one(
                {"username": username},
                {"$set": {"password": new_password}}
            )
            isChanged = True
        return isChanged

    def delete_account(self, username, password):
        isDeleted = False

        user = self.collection.find_one({"username": username, "password": password})
        if user:
            self.collection.delete_one({"username": username})
            isDeleted = True
        return isDeleted

    def logout(self):
        self.username = None
        self.password = None
        self.role = None
        return True

    def two_factor_auth(self, code):
        # Simulate sending a code to the user (in real application, send via email/SMS)
        generated_code = str(random.randint(100000, 999999))
        print(f"Generated 2FA code (for testing purposes): {generated_code}")

        # In a real application, you would compare the provided code with the sent code
        return code == generated_code

    def fingerprint_auth(self):
        try:
            from jnius import autoclass

            PythonActivity = autoclass('org.kivy.android.PythonActivity')
            FingerprintHelper = autoclass('org.kivy.android.FingerprintHelper')
            activity = PythonActivity.mActivity

            # This triggers the Java authentication (result shown as Toast)
            FingerprintHelper.authenticate(activity)
            SharedPreferences = autoclass('android.content.SharedPreferences')
            prefs = activity.getSharedPreferences("auth", 0)
            success = prefs.getBoolean("fingerprint_success", False)

            # For full integration, you can check a shared preference or listen for a broadcast
            print("Fingerprint authentication triggered. Check device for result.")
            return True  # You may want to poll for actual result
        except Exception as e:
            print(f"Fingerprint error: {e}")
            return False
