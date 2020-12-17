===========================================
cookiecutter-homeassistant-custom-component
===========================================

.. badges-begin

| |CalVer| |License|
| |Read the Docs|
| |pre-commit| |Black|

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

.. introduction-begin

This repository is a Cookiecutter_ template for a `Home Assistant`_ custom component
based on the integration_blueprint_ template.

This project is sort of fusion of `cookiecutter-homeassistant-component`_, integration_blueprint_
and `cookiecutter-hypermodern-python`_ projects.

.. introduction-end

✨📚✨ `Read the full documentation`__

__ https://cookiecutter-homeassistant-custom-component.readthedocs.io/


Usage
=====

.. usage-begin

.. parsed-literal::

   $ cookiecutter gh:oncleben31/homeassistant-custom-component \\
     --checkout=\ |current-stable-version|\


.. usage-end

Features
========

.. features-begin

- Ready to use Home Assistant custom component
- UI configuration with config Flow
- Translations
- Development, testing and step by step debugging in Visual Studio Code development container
- HACS_ ready
- Continuous integration with `GitHub Actions`_
- Settings for pre-commit

You can find a repository created with this cookiecutter template
in the `cookiecutter-homeassistant-custom-component-instance`_ example.

.. features-end

.. references-begin

.. |current-stable-version| replace:: 2020.11.16
.. _integration_blueprint: https://github.com/custom-components/integration_blueprint
.. _Cookiecutter: https://github.com/cookiecutter/cookiecutter
.. _cookiecutter-homeassistant-component: https://github.com/boralyl/cookiecutter-homeassistant-component
.. _cookiecutter-homeassistant-custom-component-instance: https://github.com/oncleben31/cookiecutter-homeassistant-custom-component-instance
.. _cookiecutter-hypermodern-python: https://github.com/cjolowicz/cookiecutter-hypermodern-python
.. _GitHub Actions: https://github.com/features/actions
.. _HACS: https://hacs.xyz/
.. _Home Assistant: https://www.home-assistant.io/

.. references-end
