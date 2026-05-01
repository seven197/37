[app]

title = Roguelike Survival
package.name = roguelikesurvival
package.domain = org.roguegame
source.dir = .
version = 0.1
source.include_exts = py,png,jpg,kv,atlas
source.ignore_exts = pyc,pyo
requirements = python3,kivy==2.3.0
orientation = landscape
fullscreen = 1
android.api = 33
android.minapi = 21
android.archs = arm64-v8a, armeabi-v7a
android.build_mode = debug
android.permissions = INTERNET
android.logcat_filters = *:S python:D
android.copy_libs = 1
android.buildtools = 33.0.2

[buildozer]
log_level = 2
warn_on_root = 1
