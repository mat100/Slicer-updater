import os
import shutil
import urllib.request
import zipfile
import stat

class KISSlicer163(object):
    PROFILE_DIRS = ['_materials', '_printers', '_styles', '_supports']

    def __init__(self, path):
        self.slicer_path = path

        self.ref_path = os.path.join(self.slicer_path, "_reference")
        self.bac_path = os.path.join(self.slicer_path, "_backup")
        self.upd_path = os.path.join(self.slicer_path, "_update")

    def recursive_chmod(self, path, mode):
        os.chmod(path, mode)
        for root, dirs, files in os.walk(path):
            for d in dirs:
                os.chmod(os.path.join(root, d), mode)
            for f in files:
                os.chmod(os.path.join(root, f), mode)

    # Recursive copy directory
    def copydir(self, src, dst, symlinks=False, ignore=None):
        if not os.path.exists(dst):
            os.makedirs(dst)
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)

    def perform_update(self, url):
        # Create update folder
        if os.path.isdir(self.upd_path):
            shutil.rmtree(self.upd_path) # remove if folder exists           
        os.makedirs(self.upd_path) # create new one

        upd_file_path = os.path.join(self.upd_path, 'deltiq.zip') # update zip file

        # Download update file from git
        urllib.request.urlretrieve(url, upd_file_path)

        # Extract profiles for selected slicer
        zip_upd = zipfile.ZipFile(upd_file_path, 'r')
        for file in zip_upd.namelist():
            if file.startswith('Slicer-profiles-deltiq/KISSlicer_1_6_3/'):
                zip_upd.extract(file, self.upd_path)
        zip_upd.close()

        # Create backup folder
        if os.path.isdir(self.bac_path):
            shutil.rmtree(self.bac_path) # remove if exists 
        os.makedirs(self.bac_path) # create new one

        # Create reference folder if not exists
        if not os.path.isdir(self.ref_path):
            os.makedirs(self.ref_path)

        # Check profiles
        for dir in self.PROFILE_DIRS: # loop for profiles folder
            dir_path = os.path.join(self.slicer_path, dir) # actual profile dir
            ref_dir_path = os.path.join(self.ref_path, dir) # reference profile dir
            upd_dir_path = os.path.join(self.upd_path, "Slicer-profiles-deltiq/KISSlicer_1_6_3/", dir) # update profile dir

            if os.path.exists(dir_path): # profile dir exists
                self.copydir(dir_path, os.path.join(self.bac_path, dir)) # create backup

                for file in os.listdir(dir_path): # loop for files inside profile dir
                    file_path = os.path.join(dir_path, file) # current file
                    ref_file_path = os.path.join(self.ref_path, dir, file) # reference file

                    if os.path.exists(ref_file_path): # reference file exists
                        cmp_res = False
                        with open(file_path) as f1: # Compare only content
                            with open(ref_file_path) as f2:
                                cmp_res = f1.read() == f2.read()

                        if cmp_res: # Check file equal
                            os.remove(file_path) # File is unchanged from original
                        else: # file is changed, create copy(rename)
                            filename = os.path.basename(file_path) # separate filename
                            filename_withoutext, filename_ext = os.path.splitext(filename) # separete name and extension

                            new_filename = None
                            new_file_path = None
                            i = 0
                            while True: # find next free file
                                new_filename = "{} - USER CHANGE DETECTED{}{}".format(filename_withoutext, "" if i==0 else " {}".format(i), filename_ext) # generate new file name
                                new_file_path = os.path.join(dir_path, new_filename) # new file path
                                if os.path.exists(new_file_path):    
                                    i += 1 # if file exists increment number
                                else: 
                                    break

                            os.rename(file_path, new_file_path) # rename file from original(trilab) name to new(user) name

                            # Change profile name inside file
                            with open(new_file_path) as f:
                                lines = f.readlines()
                            if lines[1] == "[{}]\n".format(filename_withoutext): # Check old profile name on second line
                                lines[1] = "[{}]\n".format(os.path.splitext(new_filename)[0]) # update profile name
                            with open(new_file_path, "w") as f:
                                f.writelines(lines) # write back to file
            else:
                os.makedirs(dir_path) # profile dir not exists, create it

            if os.path.exists(upd_dir_path): # Check update dir
                self.copydir(upd_dir_path, dir_path) # Update profile dir

                if os.path.exists(ref_dir_path): # if exists reference
                    self.recursive_chmod(ref_dir_path, stat.S_IRWXU|stat.S_IRWXG|stat.S_IRWXO) # Set permission for delete
                    shutil.rmtree(ref_dir_path) # remove old reference dir
                self.copydir(upd_dir_path, ref_dir_path) # copy new reference from update

        # Delete update dir
        shutil.rmtree(self.upd_path)

        # Set reference file for readonly
        self.recursive_chmod(self.ref_path, stat.S_IREAD|stat.S_IRGRP|stat.S_IROTH)

        return True

        # import sys
        # from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
        #     QVBoxLayout, QDialog, QMessageBox)

        # class SlicerUpdater(object):
        #     def __init__(self):



        # class Form(QDialog):

        #     def __init__(self, parent=None):
        #         super(Form, self).__init__(parent)
        #         # Create widgets
        #         self.edit = QLineEdit("Write my name here")
        #         self.button = QPushButton("Show Greetings")
        #         # Create layout and add widgets
        #         layout = QVBoxLayout()
        #         layout.addWidget(self.edit)
        #         layout.addWidget(self.button)
        #         # Set dialog layout
        #         self.setLayout(layout)
        #         # Add button signal to greetings slot
        #         self.button.clicked.connect(self.greetings)

        #     # Greets the user
        #     def greetings(self):
        #         msgBox = QMessageBox()
        #         msgBox.setText("The document has been modified.")
        #         msgBox.setInformativeText("Do you want to save your changes?")
        #         msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        #         msgBox.setDefaultButton(QMessageBox.Save)
        #         ret = msgBox.exec_()
        #         print ("Hello %s" % self.edit.text())


        # if __name__ == '__main__':
        #     # Create the Qt Application
        #     app = QApplication(sys.argv)
        #     # Create and show the form
        #     form = Form()
        #     form.show()
        #     # Run the main Qt loop
        #     sys.exit(app.exec_())