API Reference
=============

This sections has reference to all of the available classes, their
attributes and available methods.


Discord OAuth2 Client
---------------------

.. autoclass:: quart_nextcord.DiscordOAuth2Session
    :members:
    :inherited-members:

.. autoclass:: quart_nextcord._http.DiscordOAuth2HttpClient
    :members:
    :inherited-members:


Models
------

.. autoclass:: quart_nextcord.models.Guild
    :members:
    :inherited-members:

.. autoclass:: quart_nextcord.models.User
    :members:
    :inherited-members:

.. autoclass:: quart_nextcord.models.Bot
    :members:
    :inherited-members:

.. autoclass:: quart_nextcord.models.Integration
    :members:
    :inherited-members:

.. autoclass:: quart_nextcord.models.UserConnection
    :members:
    :inherited-members:


Utilities
---------

.. autodecorator:: quart_nextcord.requires_authorization


Exceptions
----------

.. autoclass:: quart_nextcord.HttpException
    :members:

.. autoclass:: quart_nextcord.RateLimited
    :members:

.. autoclass:: quart_nextcord.Unauthorized
    :members:

.. autoclass:: quart_nextcord.AccessDenied
    :members:


Contents
--------

* :doc:`introduction`
* :doc:`api`
