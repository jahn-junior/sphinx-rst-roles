# This file is part of sphinx-rst-roles.
#
# Copyright 2025 Canonical Ltd.
#
# This program is free software: you can redistribute it and/or modify it under the
# terms of the GNU Lesser General Public License version 3, as published by the Free
# Software Foundation.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranties of MERCHANTABILITY, SATISFACTORY
# QUALITY, or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
"""Contains the extension's roles."""

import re

from docutils import nodes
from sphinx.util.docutils import SphinxRole


class SpellExceptionRole(SphinxRole):
    """Define the spellexception role's behavior."""

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        """Ignore the provided string when checking spelling."""
        node = nodes.raw(
            text="<spellexception>" + self.text + "</spellexception>", format="html"
        )
        return [node], []


class NoneRole(SphinxRole):
    """Define the none role's behavior."""

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        """Do nothing."""
        return [], []


class LiteralrefRole(SphinxRole):
    """Define the literalref role's behavior."""

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        """Create a cross-reference with monospaced text."""
        find_url = re.compile(r"^(.+?)\s*<(.+)>$")
        match = find_url.match(self.text)

        link_text = match.groups()[0] if match else self.text
        link_url = match.groups()[1] if match else self.text

        if "://" not in link_url:
            link_url = "https://" + link_url

        node = nodes.reference("", "", internal=False, refuri=link_url)
        node.append(nodes.literal(text=link_text))

        return [node], []
