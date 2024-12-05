import subprocess

def execute_apple_script(script):
    osa_command = ['osascript', '-e', script]
    return_value = subprocess.check_output(osa_command)
    return_value = return_value.decode('utf-8').strip()
    return return_value

def bring_zoom_window_to_top(window_title):
    script = """
activate application "zoom.us"
tell application "System Events"
    set p to first process where it is frontmost
    repeat with w in every window of p
        if (name of w) contains "{{title}}" then
            tell p
                perform action "AXRaise" of w
            end tell
        end if
    end repeat
end tell
"""
    script = script.replace("{{title}}", window_title)
    return execute_apple_script(script)

def zoom_window_exists(window_title):
    script = """
activate application "zoom.us"
tell application "System Events"
    set p to first process where it is frontmost
    repeat with w in every window of p
        if (name of w) contains "{{title}}" then
            return "yes"
        end if
    end repeat
end tell
return "no"
"""
    script = script.replace("{{title}}", window_title)
    return execute_apple_script(script)

def hide_zoom_window():
    script = """
tell application "System Events"
    set visible of process "zoom.us" to false
end tell
"""
    return execute_apple_script(script)