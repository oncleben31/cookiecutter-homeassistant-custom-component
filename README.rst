===========================================
cookiecutter-homeassistant-custom-component
===========================================

.. badges-begin

| |Status| |CalVer| |License|
| |Read the Docs|
| |pre-commit| |Black|

.. |Status| image:: https://badgen.net/badge/status/alpha/d8624d
   :target: https://badgen.net/badge/status/alpha/d8624d
   :alt: Project Status
.. |CalVer| image:: https://img.shields.io/badge/calver-YYYY.MM.DD-22bfda.svg
   :target: http://calver.org/
   :alt: CalVer
.. |License| image:: https://img.shields.io/github/license/oncleben31/cookiecutter-homeassistant-custom-component
   :target: https://opensource.org/licenses/MIT
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/cookiecutter-homeassistant-custom-component/latest.svg?label=Read%20the%20Docs
   :target: https://cookiecutter-homeassistant-custom-component.readthedocs.io/
   :alt: Read the documentation at https://cookiecutter-homeassistant-custom-component.readthedocs.io/
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black

.. badges-end

|

Cookiecutter_ template for a `Home Assistant`_ custom component based on the
blueprint_ template.

This project is the fusion of `cookiecutter-homeassistant-component`_, blueprint_
and `cookiecutter-hypermodern-python`_ projects.

✨📚✨ `Read the full documentation`__

__ https://cookiecutter-homeassistant-custom-component.readthedocs.io/


Usage
=====

.. code:: console

   $ cookiecutter gh:oncleben31/cookiecutter-homeassistant-custom-component --checkout=2020.10.30


Features
========

.. features-begin

- Ready to use Home Assistant custom component
- UI configuration with config Flow
- Translations
- Development and testing in Visual Studio Code development container
- HACS_ ready
- Continuous integration with `GitHub Actions`_

You can find a repository created with this cookiecutter template
in the `cookiecutter-homeassistant-custom-component-instance`_ example.

.. features-end


Quickstart
==========

.. quickstart-begin

Requirements
------------

Install Cookiecutter_:

.. code:: console

   $ pipx install cookiecutter

pipx_ is preferred, but you can also install with ``pip install --user``.

It is recommended to set up Python 3.7, 3.8, or 3.9 using pyenv_.


Creating a project
------------------

Generate a Home Assistant custom component project by using the following command
and setting the different parameters of the template:

.. code:: console

   $ cookiecutter gh:oncleben31/cookiecutter-homeassistant-custom-component \
     --checkout="2020.10.30"


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

.. quickstart-end

.. references-begin

.. _Black: https://github.com/psf/black
.. _blueprint: https://github.com/custom-components/blueprint
.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _cookiecutter-homeassistant-component: https://github.com/boralyl/cookiecutter-homeassistant-component
.. _cookiecutter-homeassistant-custom-component-instance: https://github.com/oncleben31/cookiecutter-homeassistant-custom-component-instance
.. _cookiecutter-hypermodern-python: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _Docker: https://www.docker.com/
.. _GitHub: https://github.com/
.. _GitHub Actions: https://github.com/features/actions
.. _HACS: https://hacs.xyz/
.. _Home Assistant: https://www.home-assistant.io/
.. _Home Assistant developers documentation: https://developers.home-assistant.io/
.. _Hypermodern Python: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
.. _pipx: https://pipxproject.github.io/pipx/
.. _pre-commit: https://pre-commit.com/
.. _pyenv: https://github.com/pyenv/pyenv
.. _Visual Studio Code: https://code.visualstudio.com/
.. _Visual Studio Code Remote - Containers: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers

.. references-end
