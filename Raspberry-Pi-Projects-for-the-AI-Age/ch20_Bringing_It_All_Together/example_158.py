def call(method, **params):                  # dry run
    print(f"Kodi <- {method}")
    for key, value in params.items():
        print(f"     {key} = {value!r}")

def on_person_alert(text):
    call("GUI.ShowNotification", title="Doorbell",
         message=text, displaytime=10000)
    call("Player.PlayPause", playerid=1, play=False)

on_person_alert("Person at the front door")
