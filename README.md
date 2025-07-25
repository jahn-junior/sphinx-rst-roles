# custom-sphinx-roles

`custom-sphinx-roles` houses all of Canonical's custom Sphinx roles.

lorem ipsum

## Basic usage

### literalref

lorem ipsum

```
:literalref:`link text <target>`

:literalref:`link text <URL>`
```

lorem ipsum

```
{literalref}`link text <target>`

{literalref}`link text <URL>`
```

### spellexception

lorem ipsum

```
:spellexception:`Lorem ipsum`
```

lorem ipsum

```
{spellexception}`Lorem ipsum`
```

### none

lorem ipsum

```
:none:`This text isn't rendered.`
```

lorem ipsum

```
{none}`This text isn't rendered.`
```

## Project setup

custom-sphinx-roles is published on PyPI and can be installed with:

```bash
pip install custom-sphinx-roles
```

After adding custom-sphinx-roles to your Python project, update your Sphinx's `conf.py`
file to include `custom_sphinx_roles` as an extension:

```python
extensions = [
    "custom_sphinx_roles"
]
```

## Community and support

You can report any issues or bugs on the project's [GitHub
repository](https://github.com/jahn-junior/sphinx-rst-roles).

sphinx-rst-roles is covered by the [Ubuntu Code of
Conduct](https://ubuntu.com/community/ethos/code-of-conduct).

## License and copyright

custom-sphinx-roles is released under the [GPL-3.0 license](LICENSE).

<!-- FIXME -->

© 2025 Canonical Ltd.
