User Guide
==========

This is the user guide
for the `Home Assistant Custom Component Cookiecutter`_,
a Python template for Home Assistant based on the `Integration Blueprint`_ repository.

If you're in a hurry, check out the :doc:`quickstart guide <quickstart>`.

.. contents::
    :local:
    :backlinks: none

Introduction
------------

*In progress*

About this project
^^^^^^^^^^^^^^^^^^

.. _Features:

Features
^^^^^^^^

Here is a detailed list of features for this Python template:

.. include:: ../README.rst
   :start-after: features-begin
   :end-before: features-end

Release cadence
^^^^^^^^^^^^^^^
*In progress*

Installation
------------

*In progress*

Project creation
----------------

*In progress*

Project overview
----------------

This repository contains multiple files, here is a overview:

.. table:: Files list
   :widths: auto

   ====================================================== ======================================================================================================================
   ``.devcontainer/*``                                    Used for development/testing with VSCODE, more info in the readme file in that dir
   ``.github/ISSUE_TEMPLATE/feature_request.md``          Template for Feature Requests
   ``.github/ISSUE_TEMPLATE/issue.md``                    Template for issues
   ``.github/settings.yml``                               Probot settings to control the repository settings.
   ``.vscode/tasks.json``                                 Tasks for the devcontainer
   ``custom_components/[DOMAIN NAME]/translations/*``     `Translation files`_
   ``custom_components/[DOMAIN NAME]/__init__.py``        The component file for the integration
   ``custom_components/[DOMAIN NAME]/api.py``             This is a sample API client
   ``custom_components/[DOMAIN NAME]/binary_sensor.py``   Binary sensor platform for the integration
   ``custom_components/[DOMAIN NAME]/config_flow.py``     Config flow file, this adds the UI configuration possibilities
   ``custom_components/[DOMAIN NAME]/const.py``           A file to hold shared variables/constants for the entire integration
   ``custom_components/[DOMAIN NAME]/manifest.json``      A `manifest file`_ for Home Assistant.
   ``custom_components/[DOMAIN NAME]/sensor.py``          Sensor platform for the integration
   ``custom_components/[DOMAIN NAME]/switch.py``          Switch sensor platform for the integration
   ``CONTRIBUTING.md``                                    Guidelines on how to contribute
   ``example.png``                                        Screenshot that demonstrate how it might look in the UI
   ``info.md``                                            An example on a info file (used by HACS_)
   ``LICENSE``                                            The license file for the project
   ``README.md``                                          The file you are reading now, should contain info about the integration, installation and configuration instructions
   ``requirements.txt``                                   Python packages used by this integration
   ====================================================== ======================================================================================================================

If you want to use all the potential and features of this blueprint template you
should use Visual Studio Code to develop in a container. In this container you
will have all the tools to ease your python development and a dedicated Home
Assistant core instance to run your integration. See ``.devcontainer/README.md`` for more information.

If you need to work on a Python library in parallel of this integration,
there are different options.
The following one seems easy to implement:

- Create a dedicated branch for your python library on a public git repository (example: branch
  `dev`)
- Update in the ``manifest.json`` file the ``requirements`` key to point on your development branch
  ( example: ``"requirements": ["git+https://github.com/ludeeus/sampleclient.git@dev#devp==0.0.1beta1"]``)
- Each time you need to make a modification to your Python library, push it to your
  development branch and increase the number of the Python library version in ``manifest.json`` file
  to ensure Home Assistant update the code of the python library. (example ``"requirements": ["git+https://...==0.0.1beta2"]``).



Developing in Visual Studio Code with a development container
-------------------------------------------------------------

The easiest way to get started with custom integration development is to use Visual Studio Code with development containers.
This approach will create a preconfigured development environment with all the tools you need.

In the container you will have a dedicated Home Assistant core instance running with your custom component code.
You can configure this instance by updating the ``./devcontainer/configuration.yaml`` file.

Prerequisites
^^^^^^^^^^^^^
- `git`_ installed
- Docker
  - For Linux, macOS, or Windows 10 Pro/Enterprise/Education use the `current release version of Docker`_
  - Windows 10 Home requires `WSL 2 <https://docs.microsoft.com/windows/wsl/wsl2-install>`_ and the current Edge version of Docker Desktop (see instructions `here <https://docs.docker.com/docker-for-windows/wsl-tech-preview/>`_). This can also be used for Windows Pro/Enterprise/Education.
- `Visual Studio code`_
- `Remote - Containers (VSC Extension) <https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers>`_

`More info about requirements and devcontainer in general <https://code.visualstudio.com/docs/remote/containers#_getting-started>`_


Getting started
^^^^^^^^^^^^^^^

#. Clone the repository to your computer.
#. Open the repository using Visual Studio code.

When you open this repository with Visual Studio code you are asked to "Reopen in Container",
this will start the build of the container.

*If you don't see this notification,
open the command palette and select ``Remote-Containers: Reopen Folder in Container``.*

Tasks
^^^^^

The devcontainer comes with some useful tasks to help you with development.
You can start these tasks by opening the command palette
and select ``Tasks: Run Task`` then select the one you want to run.

When a task is currently running, it can be restarted by opening the command palette
and selecting ``Tasks: Restart Running Task``, then select the task you want to restart.

The available tasks are:

.. table:: Tasks list
   :widths: auto

   ================================================== ================================================================================
   Task                                                Description
   ================================================== ================================================================================
   Run Home Assistant on port 9123                     Launch Home Assistant with your custom component code and the configuration defined in ``.devcontainer/configuration.yaml``.
   Run Home Assistant configuration against /config    Check the configuration.
   Upgrade Home Assistant to latest dev                Upgrade the Home Assistant core version in the container to the latest version of the ``dev`` branch.
   Install a specific version of Home Assistant        Install a specific version of Home Assistant core in the container.
   ================================================== ================================================================================

Step by Step debugging
^^^^^^^^^^^^^^^^^^^^^^

With the development container,
you can test your custom component in Home Assistant with step by step debugging.

You need to modify the ``configuration.yaml`` file in ``.devcontainer`` folder
by uncommenting the line:

.. code :: yaml

   # debugpy:

Then launch the task ``Run Home Assistant on port 9123``, and launch the debbuger
with the existing debugging configuration ``Python: Attach Local``.

For more information, look at the `Remote Python Debugger integration documentation`_.



Linting
-------

*In progress*

GitHub Actions Workflows
------------------------

*In progress*

.. include:: ../README.rst
   :start-after: references-begin
   :end-before: references-end

.. _current release version of Docker: https://docs.docker.com/install/
.. _git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
.. _HACS: https://hacs.xyz/
.. _Home Assistant Custom Component Cookiecutter: https://github.com/oncleben31/cookiecutter-homeassistant-custom-component
.. _Integration Blueprint: https://github.com/custom-components/integration_blueprint
.. _manifest file: https://developers.home-assistant.io/docs/en/creating_integration_manifest.html
.. _Remote Python Debugger integration documentation: https://www.home-assistant.io/integrations/debugpy/
.. _Translation files: https://developers.home-assistant.io/docs/internationalization/custom_integration
.. _Visual Studio code: https://code.visualstudio.com/
