# ibridges-gui-plugin-example

This repository shows an example how to create a plugin for the [iBridges GUI](https://github.com/iBridges-for-iRODS) which adds two more views to the GUI. You can use the repository in two ways:

1) Install it as a plugin by cloning the repo and doing:
    ```
    cd ibridges-gui-tab-example
    pip install -e .
    # start the iBridges GUI
    ibridges gui
    ```

    You will see a drop down menu with two extra views. Login and select the views to load them.
    
2) Use the repository as a template to design your own extensions to the iBridges GUI.

## Requirements

You need ibridgesgui >= 1.5.0

## Create your own plugin
Below we will briefly describe how to create a new tab for iBridges GUI and offer it as a plugin to the application.

### Step 1: Use this repository as a template repository
Click on the upper green button `Use this template` to create your new repository for the new iBridges GUI tab.
Choose a new name for your repository!

### Step 2: Rename the project folder
Simply rename the folder `exampleplugin` to the name you chose for your python package.

### Step 3: Design your tab
We recommend the QT designer to create a so-called ui-file of the type "ui form" which contains all the graphical elements you want to expose in the new tab.
The functionality we will define in an own class in a later step. So please take your time for the graphical design!
Save the file in the renamed project folder.

If you want to add several new tabs create a ui-file for each new tab.

### Step 3: Convert the ui-file to a python file

Convert the ui-file to a python class:

```py
pyside6-uic my_new_tab.ui -o ui_my_new_tab.py
```
**Note,** the class name in the python file will be `Ui_form` by default. Please adjust the name to your liking.

### Step 4: Create a python class to define the functionality
For each new layout file please create a python class. In the `example.py` you will find some more information what is important to keep and which influence it has on the apprearance in the GUI.

1. Create a new python file or rename and adjust the existing `example.py`.
2. Check the imports: Your python filename and class for the layout are called differently
3. Replace the `fill info` with a function that works for your layout to check whether the `session` is handed over correctly during the launch of the iBridges-GUI.
4. Adjust the `__init__.py`

### Step 5: Adjust the `pyproject.toml`
Adjust the information in the `pyproject.toml` with your information:

```
[project]
name = "YOUR PLUGIN NAME"
description = "YOUR PLUGIN DESCRIPTION"
authors = [
    {name = "YOU", email = "YOUR EMAIL"},
]
...
dependencies = [
    "PySide6>=6.8.1",
    "ibridgesgui>=1.4.0, <1.5",
    "ADD DEPENDENCIES IF NECESSARY"
]
```

The next one defines how the iBridges GUI finds the new tab(s). All classes registered under the entry-points
will be found by the GUI. Please **do not change the name "ibridges.gui_tab"**. Please create an entry for each new tab:

```
[project.entry-points."ibridges.gui_tab"]
ID1 = "ibridgesguicontrib.YOUR_PACKAGE.PYTHON_FILE_NAME:PYTHON_CLASS_NAME1"
ID2 = "ibridgesguicontrib.YOUR_PACKAGE.PYTHON_FILE_NAME:PYTHON_CLASS_NAME2"
...

[tool.setuptools_scm]
write_to = "ibridgesguicontrib/YOUR_PACKAGE/_version.py"

```

### Step 6: Deploy locally
On the shell navigate to the top level of the repository and install with pip:

```
pip install -e .
```

or
```
uv build
```

Please check your iBridges-GUI version. The plugin structure is only supported by iBridges-GUI 1.5.0 or higher.
You an also compile iBridges-GUI from the feature branch [`example_plugin`](https://github.com/iBridges-for-iRODS/iBridges-GUI/tree/example_plugin) that introduces the plugin structure.

Start the iBridgesGUI and check the output or the logs `~/.ibridges/ibridges-gui.log`. 
```
# pip installed
ibridges gui

# uv installed
uv run ibridges gui
```

If your plugin is detected you should see your plugin name:

```
INFO:ibridges-gui:Third party tabs: [<class 'ibridgesguicontrib.exampleplugin.example1.ExampleTab1'>, <class 'ibridgesguicontrib.exampleplugin.example2.ExampleTab2'>]
INFO:ibridges-gui:Tab names: ['UU example tab 1', 'UU example tab 2']
```





