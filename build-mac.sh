source venv/bin/activate

pyside2-uic -o updater_ui.py ui/updater.ui
pyside2-rcc -o resources_rc.py resources/resources.qrc

# FIX pyside2-uic issue
sed -i '' -e 's/setItemText(2, "TriLAB DeltiQ")/setItemText(0, "TriLAB DeltiQ")/' updater_ui.py
sed -i '' -e 's/setItemText(3, "TriLAB DeltiQ 2")/setItemText(1, "TriLAB DeltiQ 2")/' updater_ui.py

PyInstaller app.py --name Slicer-updater --windowed --icon=resources/icons/trilab.icns --onefile --clean

# create dmg
#pushd dist
#hdiutil create ./Slicer-updater.dmg -srcfolder Slicer-updater.app -ov
#popd