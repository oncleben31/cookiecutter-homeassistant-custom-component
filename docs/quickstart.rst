Quickstart Guide
================

Requirements
------------

Install Cookiecutter_:

.. code:: console

   $ pipx install cookiecutter

pipx_ is preferred, but you can also install with ``pip install --user``.

It is recommended to set up 3.10 using pyenv_.


Creating a project
------------------

Generate a Home Assistant custom component project by using the following command:

.. parsed-literal::

   $ cookiecutter gh:oncleben31/cookiecutter-homeassistant-custom-component --checkout=\ |current-stable-version|\


Follow the instructions to customize the generated project

=====================  ============================================
     Setting                         Definition
=====================  ============================================
``friendly_name``      Integration name used in configuration UI.
``project_name``       Project name on GitHub.
``domain_name``        Integration domain name
``class_name_prefix``  Prefix to be use in classes name
``github_user``        GitHub user hosting the repository
``version``            Initial version of the component
=====================  ============================================

Change to the root directory of your new project,
and create a Git repository:

.. code:: console

   $ git init
   $ git add .
   $ git commit


Setup the development container
-------------------------------

The development container allows to work in a local and dedicated Home Assitant instance
to test your custom component.
To launch it you need to have already installed Docker_, `Visual Studio Code`_ (VSC)
and the `Visual Studio Code Remote - Containers`_ extension.

Open your local copy of the repository with VSC:

.. code:: console

   $ code .

Visual Studio Code starts and you are asked to "Reopen in Container",
this will start the build of the container.

When done, you can launch the local instance of Home Assistant by running the task ``Run Home Assistant on port 9123``.

Use your preferred browser to open the URL ``http://localhost:9123``.

Initalize your Home Assistant local instance by following the onboarding workflow.

When setup, you can go to **Configuration** -> **Integrations** menu, clic the ``+`` button
and search the name you have given to the custom component.

Follow the config flow of the custom component to integrate it in Home Assistant.

Now you are all set to modify the code and develop your ideas !


Advanced usages
---------------

Add a logo
^^^^^^^^^^

You have the possibility to add a logo to be used in the integrations configuration UI.
To do so, visit the `home-assistant/brands`_ repository on GitHub
and follow the instructions.

Deploy with HACS
^^^^^^^^^^^^^^^^

HACS_ is the community store.
You can ease the installation of your custom component by making it compatible with HACS.

The template have already the tools do do that: ``hacs.json`` and ``info.md`` files.
The `Publish documentation`_ explains how to set those files
and the different options you have to integrate your custom component in the HACS network.

Step by step debugging
^^^^^^^^^^^^^^^^^^^^^^

If you choose to use Visual Studio Code with the development container, you can
test your custom component in Home Assistant with step by step debugging.

You need to modify the ``configuration.yaml`` file in ``.devcontainer`` folder
by uncommenting the line:

.. code :: yaml

   # debugpy:

Then launch the task ``Run Home Assistant on port 9123``, and launch the debbuger
with the existing debugging configuration ``Python: Attach Local``.

For more information, look at `the Remote Python Debugger integration documentation`_.

Known limitations
-----------------

- **If you plan to host the generated repository in a GitHub organization you will need manual modifications**.

  Currently the template work well when the repostory is hosted in a GitHub individual account,
  where URL name and code owner are the same.
  If you want to use an organization,
  it is recommended to use the name of this organization for ``github_user`` settings
  and modify manually where it's needed afer generation with Cookiecutter.


.. include:: ../README.rst
   :start-after: references-begin
   :end-before: references-end

.. _Black: https://github.com/psf/black
.. _Docker: https://www.docker.com/
.. _GitHub: https://github.com/
.. _home-assistant/brands: https://github.com/home-assistant/brands
.. _pipx: https://pipxproject.github.io/pipx/
.. _pre-commit: https://pre-commit.com/
.. _Publish documentation: https://hacs.xyz/docs/publish/start
.. _pyenv: https://github.com/pyenv/pyenv
.. _the Remote Python Debugger integration documentation: https://www.home-assistant.io/integrations/debugpy/
.. _Visual Studio Code: https://code.visualstudio.com/
.. _Visual Studio Code Remote - Containers: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
