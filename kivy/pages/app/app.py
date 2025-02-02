import sys, os
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.storage.jsonstore import JsonStore
from kivy.clock import Clock
from kivy.uix.screenmanager import Screen

BASE_PATH = os.path.abspath(__file__+ '/../../../')

sys.path.append(BASE_PATH)
from inc.classes.Requests import Requests
from inc.classes.Storage import Storage
from inc.consts.consts import Consts
# from pages.app.home.home import HomeWindow

# Load KV file
Builder.load_file(BASE_PATH + '/pages/app/app.kv')

class AppWindow(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Check for login
        auth_token = Storage.r_authtoken()
        if not auth_token:
            Clock.schedule_once(self.logout, 2/30)
        else:
            resp = Requests.r_perfil()
            if resp:
                if resp['status'] == 200:
                    perfil = resp['data'] if 'data' in resp else {}
                    if perfil:
                        email_auth = perfil['per_b_email_auth'] if 'per_b_email_auth' in perfil else False
                        ativo = perfil['per_b_ativo'] if 'per_b_ativo' in perfil else False
                        if ativo:
                            if email_auth:
                                resp = Requests.r_historico_perfil()
                                if resp:
                                    if resp['status'] == 200:
                                        historico = resp['data'] if 'data' in resp else []
                                        if historico:
                                            Clock.schedule_once(self.redirect_app_home, 2/30)
                                            pass
                                        else:
                                            pass # Recommendation Page to do
                                    else:
                                        Clock.schedule_once(self.logout, 2/30)
                                else:
                                    Clock.schedule_once(self.logout, 2/30)
                            else:
                                pass # Email auth page TO DO
                        else:
                            Clock.schedule_once(self.logout, 2/30)
                    else:
                        Clock.schedule_once(self.logout, 2/30)
                else:
                    Clock.schedule_once(self.logout, 2/30)
            else:
                Clock.schedule_once(self.logout, 2/30)


    def redirect_app_home(self, dt):
        self.parent.current = 'app_home_screen'

    def logout(self, dt):
        resp = Storage.logoff()
        if resp:
            App.get_running_app().unload_app()        
            self.parent.current = 'gestme_screen'


class AppApp(App):

    def build(self):
        return AppWindow()

if __name__ == '__main__':
    AppApp().run()
