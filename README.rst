===========================================
cookiecutter-homeassistant-custom-component
===========================================

.. badges-begin

| |Status| |CalVer| |License|
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
- Development and testing in Visual Studio Code devcontainer
- HACS_ ready
- Continuous integration with `GitHub Actions`_

You can find a repository created with this cookiecutter template in the
`cookiecutter-homeassistant-custom-component-instance`_ example.

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

Generate a Home Assistant custom component project:

.. code:: console

   $ cookiecutter gh:oncleben31/cookiecutter-homeassistant-custom-component \
     --checkout="2020.10.30"

Change to the root directory of your new project,
and create a Git repository:

.. code:: console

   $ git init
   $ git add .
   $ git commit




.. quickstart-end

.. references-begin

.. _Black: https://github.com/psf/black
.. _blueprint: https://github.com/custom-components/blueprint
.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _cookiecutter-homeassistant-component: https://github.com/boralyl/cookiecutter-homeassistant-component
.. _cookiecutter-homeassistant-custom-component-instance: https://github.com/oncleben31/cookiecutter-homeassistant-custom-component-instance
.. _cookiecutter-hypermodern-python: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _GitHub: https://github.com/
.. _GitHub Actions: https://github.com/features/actions
.. _HACS: https://hacs.xyz/
.. _Home Assistant: https://www.home-assistant.io/
.. _Home Assistant developers documentation: https://developers.home-assistant.io/
.. _Hypermodern Python: https://cjolowicz.github.io/posts/hypermodern-python-01-setup/
.. _pipx: https://pipxproject.github.io/pipx/
.. _pre-commit: https://pre-commit.com/
.. _pyenv: https://github.com/pyenv/pyenv

.. references-end
