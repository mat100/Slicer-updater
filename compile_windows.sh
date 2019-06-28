pyinstaller updaters/kiss_1_6_3_updater.py -n trilab-slicer-updater --onefile --icon=trilab.ico

#Windows and Mac OS X specific options
#-c, --console, --nowindowed
# 	Open a console window for standard i/o (default)
#-w, --windowed, --noconsole
# 	Windows and Mac OS X: do not provide a console window for standard i/o. On Mac OS X this also triggers building an OS X .app bundle. This option is ignored in *NIX systems.
#-i <FILE.ico or FILE.exe,ID or FILE.icns>, --icon <FILE.ico or FILE.exe,ID or FILE.icns>
# 	FILE.ico: apply that icon to a Windows executable. FILE.exe,ID, extract the icon with ID from an exe. FILE.icns: apply the icon to the .app bundle on Mac OS X

#Windows specific options
#--version-file FILE
# 	add a version resource from FILE to the exe
#-m <FILE or XML>, --manifest <FILE or XML>
# 	add manifest FILE or XML to the exe
#-r RESOURCE, --resource RESOURCE
# 	Add or update a resource to a Windows executable. The RESOURCE is one to four items, FILE[,TYPE[,NAME[,LANGUAGE]]]. FILE can be a data file or an exe/dll. For data files, at least TYPE and NAME must be specified. LANGUAGE defaults to 0 or may be specified as wildcard * to update all resources of the given TYPE and NAME. For exe/dll files, all resources from FILE will be added/updated to the final executable if TYPE, NAME and LANGUAGE are omitted or specified as wildcard *.This option can be used multiple times.
#--uac-admin	Using this option creates a Manifest which will request elevation upon application restart.
#--uac-uiaccess	Using this option allows an elevated application to work with Remote Desktop.