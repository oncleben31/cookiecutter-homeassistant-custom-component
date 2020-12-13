User Guide
==========

What?
-----

This repository contains multiple files, here is a overview:

.. table:: File list
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
   ``custom_components/[DOMAIN NAME]/manifest.json``      A `manifest file`_
   ``custom_components/[DOMAIN NAME]/sensor.py``          Sensor platform for the integration
   ``custom_components/[DOMAIN NAME]/switch.py``          Switch sensor platform for the integration
   ``CONTRIBUTING.md``                                    Guidelines on how to contribute
   ``example.png``                                        Screenshot that demonstrate how it might look in the UI
   ``info.md``                                            An example on a info file (used by HACS_)
   ``LICENSE``                                            The license file for the project
   ``README.md``                                          The file you are reading now, should contain info about the integration, installation and configuration instructions
   ``requirements.txt``                                   Python packages used by this integration
   ====================================================== ======================================================================================================================


How?
----

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

.. _HACS: https://hacs.xyz/
.. _manifest file: (https://developers.home-assistant.io/docs/en/creating_integration_manifest.html) for Home Assistant.
.. _Translation files: https://developers.home-assistant.io/docs/internationalization/custom_integration
